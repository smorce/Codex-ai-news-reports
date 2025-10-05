#!/usr/bin/env python3
# scripts/codex_daily_with_agents.py

import os
import sys
import subprocess
import tempfile
import shutil
import json
import threading
import time
from datetime import datetime, timezone
from pathlib import Path
from dotenv import load_dotenv
from rich.console import Console
from rich.panel import Panel
from turso_push_report import push_daily_report
from get_github_trending import collect_github_trending_report
from get_reddit import collect_reddit_raw_data
from get_rss import collect_rss_sources


class CodexDailyRunner:
    def __init__(self):
        # --- 設定（環境に合わせて修正してください） ---
        # スクリプトの場所から相対的にリポジトリパスを決定
        script_dir = Path(__file__).parent
        self.repo_path = script_dir.parent  # scriptsディレクトリの親ディレクトリ
        self.console = Console()
        
        # .envファイルを読み込む
        env_file = self.repo_path / ".env"
        if env_file.exists():
            load_dotenv(env_file)
            print(f"Loaded .env from: {env_file}")
        else:
            print(f"Warning: .env file not found at: {env_file}")
        
        self.branch = "main"
        self.report_dir = self.repo_path / "reports"
        self.logs_dir = self.repo_path / "logs"
        self.log_file = self.logs_dir / "codex_daily_with_agents.log"
        # self.agents_file = self.repo_path / "AGENTS.md"
        self.agents_reddit_file = self.repo_path / "AGENTS_Reddit_Simple.md"
        self.agents_rss_file = self.repo_path / "AGENTS_rss.md"
        self.agents_github_trending_file = self.repo_path / "AGENTS_github_trending.md"
        
        # ディレクトリ作成
        self.report_dir.mkdir(exist_ok=True)
        self.logs_dir.mkdir(exist_ok=True)
        # ---------------------------------------
    
    def log(self, message):
        """ログメッセージを記録"""
        timestamp = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
        log_entry = f"{timestamp}\t{message}\n"
        
        # ログファイルに追記
        with open(self.log_file, 'a', encoding='utf-8') as f:
            f.write(log_entry)
        
        # コンソールにも出力
        print(f"[{timestamp}] {message}")
    
    def cleanup_temp_files(self):
        """一時ファイルを検索して削除する"""
        self.log("Checking for temporary files to clean up...")
        deleted_count = 0
        temp_patterns = [
            'temp_tasklist.md',                 # Codexタスクリスト
            'report.json',                      # Codex生成の一時JSON
            'report_ai.json',                   # AI News成果物
            'report_reddit.json',               # Reddit成果物
            'report_reddit_raw.json',           # Reddit生データ（Codex処理前）
            'report_github_trending.json',      # GitHub Trending成果物
            'report_github_trending_raw.json',  # GitHub Trending生データ（Codex処理前）
            'report_rss.json',                  # RSS成果物
            'rss_sources.json',                 # RSSソース収集結果
            'codex_raw_output_*.txt',           # Codexエラーログ
            'codex_prompt_*.md',                # 一時プロンプトファイル
        ]
        
        try:
            for pattern in temp_patterns:
                for f in self.repo_path.rglob(pattern):
                    try:
                        if f.is_file():
                            f.unlink()
                            self.log(f"Deleted temporary file: {f}")
                            deleted_count += 1
                    except Exception as e:
                        self.log(f"Warning: Could not delete temporary file {f}: {e}")
            
            if deleted_count > 0:
                self.log(f"Cleaned up {deleted_count} temporary file(s).")
            else:
                self.log("No temporary files found to clean up.")
        except Exception as e:
            self.log(f"Warning: An error occurred during temp file cleanup: {e}")

    def run(self):
        """メイン実行処理"""
        try:
            self.log("=== Start ===")

            # 一時ファイルのクリーンアップ
            self.cleanup_temp_files()

            # パスの存在確認
            if not self.repo_path.exists():
                raise FileNotFoundError(f"Repo not found: {self.repo_path}")
            # if not self.agents_file.exists():
            #     raise FileNotFoundError(f"AGENTS.md not found: {self.agents_file}")
            if not self.agents_reddit_file.exists():
                raise FileNotFoundError(f"AGENTS_Reddit_Simple.md not found: {self.agents_reddit_file}")
            if not self.agents_rss_file.exists():
                raise FileNotFoundError(f"AGENTS_rss.md not found: {self.agents_rss_file}")
            # GitHub Trending は Codex を使用しないため存在チェックは不要

            # 日付と出力ディレクトリ
            date_dir = datetime.now().strftime("%Y-%m-%d")
            output_dir = self.report_dir / date_dir
            output_dir.mkdir(parents=True, exist_ok=True)

            # # 1) 通常の AGENTS.md を処理（AI Devニュース）
            # RSS で対応しているのでコメントアウトしたが、この処理自体は完成している
            # self.log("Processing AGENTS.md → report_ai.json / report_ai.md ...")
            # ai_report_obj, ai_md_content = self.process_agents(
            #     agents_path=self.agents_file,
            #     json_output_name="report_ai.json",
            #     md_output_name="report_ai.md",
            # )

            # 2) Reddit を収集（機械的な生データ収集）
            try:
                self.log("Collecting Reddit raw data → report_reddit_raw.json ...")
                reddit_raw_obj = collect_reddit_raw_data(
                    tech_subs=["artificial", "compsci", "coding"],
                    news_subs=["technology", "Futurology"],
                    num_articles=2,
                )

                # 生データを一時保存（Codexが読み込む用）
                raw_json_path = output_dir / "report_reddit_raw.json"
                with open(raw_json_path, 'w', encoding='utf-8') as f:
                    json.dump(reddit_raw_obj, f, ensure_ascii=False, indent=2)
                self.log(f"Saved raw Reddit data to {raw_json_path}")
            except Exception as e:
                self.log(f"ERROR: Reddit raw data collection failed: {e}")
                raise

            # 3) Reddit を Codex で要約・分析
            self.log("Processing Reddit with Codex → report_reddit.json / report_reddit.md ...")
            reddit_report_obj, reddit_md_content = self.process_agents(
                agents_path=self.agents_reddit_file,
                json_output_name="report_reddit.json",
                md_output_name="report_reddit.md",
            )

            # 4) GitHub Trending を収集（機械的な生データ収集）
            try:
                self.log("Collecting GitHub Trending raw data → report_github_trending_raw.json ...")
                languages_file = Path(__file__).parent / "languages.toml"
                trending_raw_obj = collect_github_trending_report(
                    languages_file=languages_file,
                    general_limit=10,
                    specific_limit=5,
                )

                # 生データを一時保存（Codexが読み込む用）
                raw_json_path = output_dir / "report_github_trending_raw.json"
                with open(raw_json_path, 'w', encoding='utf-8') as f:
                    json.dump(trending_raw_obj, f, ensure_ascii=False, indent=2)
                self.log(f"Saved raw GitHub Trending data to {raw_json_path}")
            except Exception as e:
                self.log(f"ERROR: GitHub Trending raw data collection failed: {e}")
                raise

            # 5) 処理が重たいので、GitHub Trending は Codex による要約を行わない
            # self.log("Processing GitHub Trending with Codex → report_github_trending.json / report_github_trending.md ...")
            # trending_report_obj, trending_md_content = self.process_agents(
            #     agents_path=self.agents_github_trending_file,
            #     json_output_name="report_github_trending.json",
            #     md_output_name="report_github_trending.md",
            # )

            # 6) GitHub Trending の最終レポートを reports/{YYYY-MM-DD}/report.json に保存
            try:
                self.log("Saving GitHub Trending final report to report.json ...")
                final_report_path = output_dir / "report.json"
                with open(final_report_path, 'w', encoding='utf-8') as f:
                    json.dump(trending_raw_obj, f, ensure_ascii=False, indent=2)
                self.log(f"Saved final GitHub Trending JSON to {final_report_path}")
            except Exception as e:
                self.log(f"ERROR: Failed to save final GitHub Trending JSON: {e}")
                raise

            # GitHub Trending の Markdown レポートを生成
            try:
                self.log("Generating GitHub Trending Markdown report ...")
                md_content = self._convert_report_json_to_markdown(trending_raw_obj)
                final_md_path = output_dir / "report_github_trending.md"
                final_md_path.write_text(md_content, encoding='utf-8')
                self.log(f"Markdown report saved to {final_md_path}")
            except Exception as e:
                self.log(f"ERROR: Failed to save GitHub Trending Markdown: {e}")
                raise

            # 7) RSS ソースを機械的に収集・保存（LLMなし）
            try:
                self.log("Collecting RSS sources (mechanical) → rss_sources.json ...")
                feed_file = Path(__file__).parent / "feed.toml"
                rss_sources_obj = collect_rss_sources(
                    feed_file=feed_file,
                    days=1,
                    limit_per_feed=NUM_FEED_LIMIT if 'NUM_FEED_LIMIT' in globals() else 3,
                )
                rss_sources_path = output_dir / "rss_sources.json"
                with open(rss_sources_path, 'w', encoding='utf-8') as f:
                    json.dump(rss_sources_obj, f, ensure_ascii=False, indent=2)
                self.log(f"Saved RSS sources to {rss_sources_path}")
            except Exception as e:
                self.log(f"ERROR: RSS sources collection failed: {e}")
                raise

            # 8) AGENTS_rss.md を使って要約とレポート生成（LLM/Codex CLI）
            self.log("Processing AGENTS_rss.md → report_rss.json / report_rss.md ...")
            rss_report_obj, rss_md_content = self.process_agents(
                agents_path=self.agents_rss_file,
                json_output_name="report_rss.json",
                md_output_name="report_rss.md",
            )


            # Git操作（出力物と新規/更新された scripts もコミット）
            self.git_operations(output_dir, date_dir)
            try:
                self.git_operations(self.repo_path / "scripts", date_dir)
            except Exception as e:
                self.log(f"WARNING: git add for scripts failed: {e}")

            self.log("=== Finished ===")

        except Exception as e:
            self.log(f"ERROR: {e}")
            raise

    def process_agents(self, agents_path: Path, json_output_name: str, md_output_name: str):
        """指定の AGENTS ファイルを使って Codex を実行し、所定のファイル名で保存して返す。"""
        # 出力基準パス
        date_dir = datetime.now().strftime("%Y-%m-%d")
        output_dir = self.report_dir / date_dir
        output_dir.mkdir(parents=True, exist_ok=True)

        # Codex が生成する一時ファイル（固定名）
        temp_json = output_dir / "report.json"

        # タイムスタンプの埋め込み
        utc_now = datetime.now(timezone.utc).strftime("%Y-%m-%dT%H:%M:%SZ")
        agents_content = agents_path.read_text(encoding='utf-8')
        agents_content = agents_content.replace('{utc_timestamp}', utc_now)

        # 直前実行の残骸を削除
        if temp_json.exists():
            try:
                temp_json.unlink()
            except Exception:
                pass

        # 一時プロンプトファイル（デバッグや履歴のために残す）
        safe_name = agents_path.stem
        temp_prompt_file = Path(tempfile.gettempdir()) / f"codex_prompt_{safe_name}_{date_dir}.md"
        temp_prompt_file.write_text(agents_content, encoding='utf-8')
        self.log(f"{agents_path.name} content written to {temp_prompt_file} (length {temp_prompt_file.stat().st_size} bytes)")

        # Codex 実行
        self.log("Invoking codex exec...")
        try:
            _ = self.run_codex(agents_content, expected_report_path=temp_json)
        except Exception as e:
            # 非ゼロ終了でも temp_json が存在すれば続行
            if not (temp_json.exists() and temp_json.stat().st_size > 0):
                raise

        # 生成された JSON を読み込み
        if (not temp_json.exists()) or (temp_json.stat().st_size == 0):
            raise FileNotFoundError(f"report.json not found or empty: {temp_json}")
        with open(temp_json, 'r', encoding='utf-8') as f:
            report_obj = json.load(f)
        self.log(f"JSON report detected at {temp_json}")

        # 所定のファイル名に保存（JSON）
        final_json_path = output_dir / json_output_name
        with open(final_json_path, 'w', encoding='utf-8') as f:
            json.dump(report_obj, f, ensure_ascii=False, indent=2)
        self.log(f"Saved JSON to {final_json_path}")

        # JSON -> Markdown 変換と保存（所定名）
        md_content = self._convert_report_json_to_markdown(report_obj)
        final_md_path = output_dir / md_output_name
        final_md_path.write_text(md_content, encoding='utf-8')
        self.log(f"Markdown report saved to {final_md_path}")

        # Turso へ PUSH（JSON + Markdown）
        try:
            report_id = push_daily_report(report_obj, md_content, date_dir)
            self.log(f"Pushed report to Turso: {report_id}")
        except Exception as e:
            self.log(f"ERROR: Turso push failed: {e}")
            raise

        # 一時の report.json は混乱の元なので削除
        try:
            if temp_json.exists():
                temp_json.unlink()
        except Exception:
            pass

        return report_obj, md_content
    
    
    def find_codex_command(self):
        """Codex CLIのパスを検索"""
        # まずPATHから検索
        codex_path = shutil.which("codex")
        if codex_path:
            return codex_path
        
        # 一般的なインストール場所を検索
        common_paths = [
            "C:\\Program Files\\codex\\codex.exe",
            f"C:\\Users\\{os.environ.get('USERNAME', '')}\\AppData\\Local\\Programs\\codex\\codex.exe",
            f"C:\\Users\\{os.environ.get('USERNAME', '')}\\AppData\\Roaming\\npm\\codex.cmd",
        ]
        
        for path in common_paths:
            if os.path.exists(path):
                return path
        
        return None

    def run_codex(self, agents_content, expected_report_path: Path | None = None):
        """Codex CLIを実行"""
        # 期待する report.json の場所（呼び出し元から明示的に受け取り、日付ずれを防止）
        if expected_report_path is not None:
            report_file = Path(expected_report_path)
        else:
            date_dir = datetime.now().strftime("%Y-%m-%d")
            output_dir = self.report_dir / date_dir
            report_file = output_dir / "report.json"
        
        # Codex コマンドのパスを検索
        codex_cmd = self.find_codex_command()
        
        if not codex_cmd:
            error_msg = ("Codex CLI が見つかりません。以下を確認してください:\n"
                        "1. Codex CLI がインストールされているか\n"
                        "2. PATH に Codex が設定されているか")
            self.log(f"ERROR: {error_msg}")
            raise FileNotFoundError(error_msg)
        
        self.log(f"Using Codex CLI: {codex_cmd}")
        # リッチ表示: 実行概要をパネルで表示
        config_path = f'C:\\Users\\{os.environ.get("USERNAME", "")}\\\.codex\\config.toml'
        try:
            self.console.print(Panel.fit(f"Codex CLI: [bold]{codex_cmd}[/]\nConfig: [yellow]{config_path}[/]\nMode: [cyan]exec --yolo -c model_reasoning_effort=\"medium\"[/]", title="Codex Runner", border_style="blue"))
        except Exception:
            pass
        
        try:
            # codex exec --yolo コマンドを実行（ストリーミング表示）
            process = subprocess.Popen(
                [codex_cmd, '--config', config_path, 'exec', '--yolo', '-m', 'gpt-5-codex', '-c', 'model_reasoning_effort="medium"'],
                stdin=subprocess.PIPE,
                stdout=subprocess.PIPE,
                stderr=subprocess.PIPE,
                text=True,
                encoding='utf-8'
            )

            # エージェントへのプロンプトを投入
            assert process.stdin is not None
            process.stdin.write(agents_content)
            process.stdin.close()

            stdout_lines: list[str] = []
            stderr_lines: list[str] = []
            last_output_time = time.time()
            output_lock = threading.Lock()

            def reader(stream, collector, tag, style):
                nonlocal last_output_time
                for line in iter(stream.readline, ''):
                    line = line.rstrip('\n')
                    collector.append(line)
                    with output_lock:
                        last_output_time = time.time()
                    try:
                        self.console.print(f"[{style}]{tag}[/]: {line}")
                    except Exception:
                        print(f"{tag}: {line}")

            assert process.stdout is not None and process.stderr is not None
            t_out = threading.Thread(target=reader, args=(process.stdout, stdout_lines, 'stdout', 'cyan'), daemon=True)
            t_err = threading.Thread(target=reader, args=(process.stderr, stderr_lines, 'stderr', 'red'), daemon=True)

            with self.console.status("[bold green]Codex 実行中...[/]", spinner="dots"):
                t_out.start()
                t_err.start()
                
                # タイムアウト監視（最大10分、出力停止後60秒で終了）
                M = 10 * 60
                IDLE_TIMEOUT = 60
                idle_termination_detected = False
                
                try:
                    while process.poll() is None:
                        current_time = time.time()
                        with output_lock:
                            time_since_output = current_time - last_output_time
                        
                        # 全体のタイムアウトチェック
                        if current_time - last_output_time > M:
                            process.kill()
                            raise subprocess.TimeoutExpired('codex exec --yolo', timeout=M)
                        
                        # 出力が停止してから一定時間経過したら終了
                        if time_since_output > IDLE_TIMEOUT and stdout_lines:
                            self.log(f"No output for {IDLE_TIMEOUT}s, assuming completion")
                            process.terminate()
                            time.sleep(2)  # 終了処理を待つ
                            if process.poll() is None:
                                process.kill()
                            idle_termination_detected = True
                            break
                        
                        time.sleep(1)
                        
                except subprocess.TimeoutExpired:
                    process.kill()
                    # 念のためスレッドの終了を待つ
                    t_out.join(timeout=5)
                    t_err.join(timeout=5)
                    raise subprocess.TimeoutExpired('codex exec --yolo', timeout=M)

                # プロセス終了後、リーダーースレッドが完了するのを待つ
                t_out.join(timeout=5)
                t_err.join(timeout=5)

            rc = process.returncode if process.returncode is not None else -1
            
            # 実行結果の表示（成功・失敗問わず）
            stdout_content = "\n".join(stdout_lines)
            stderr_content = "\n".join(stderr_lines)

            # アイドルタイムアウトで強制終了したが report.json が生成済みなら成功扱い
            if idle_termination_detected:
                # ファイルフラッシュ待ちの短いリトライ
                for _ in range(4):
                    if report_file.exists() and report_file.stat().st_size > 0:
                        break
                    time.sleep(0.5)
                if report_file.exists() and report_file.stat().st_size > 0:
                    self.log(f"Idle timeout reached; report found at {report_file}. Treating as success.")
                    return stdout_content
            
            self.log(f"Codex execution completed with return code: {rc}")
            
            # stdout の内容をログに出力
            if stdout_content.strip():
                self.log("=== Codex stdout output ===")
                for line in stdout_lines:
                    self.log(f"STDOUT: {line}")
                self.log("=== End of stdout output ===")
            else:
                self.log("Codex stdout is empty")
            
            # stderr がある場合も表示
            if stderr_content.strip():
                self.log("=== Codex stderr output ===")
                for line in stderr_lines:
                    self.log(f"STDERR: {line}")
                self.log("=== End of stderr output ===")
            
            if rc != 0:
                # エラーの場合、生の出力を保存
                date_tag = datetime.now().strftime("%Y%m%d")
                err_file = self.report_dir / f"codex_raw_output_{date_tag}.txt"
                error_content = (
                    "STDOUT:\n" + stdout_content +
                    "\n\nSTDERR:\n" + stderr_content +
                    f"\n\nReturn code: {rc}"
                )
                err_file.write_text(error_content, encoding='utf-8')
                self.log(f"Codex exited with code {rc}. Saving raw output for diagnosis.")
                
                # 少し待って report.json が現れるか再確認（遅延フラッシュ対策）
                for _ in range(6):
                    if report_file.exists() and report_file.stat().st_size > 0:
                        break
                    time.sleep(0.5)

                # report.json が存在する場合は成功扱いで終了
                if (report_file.exists() and report_file.stat().st_size > 0):
                    self.log(f"report.json found despite non-zero exit. Treating as success: {report_file}")
                    return stdout_content
                
                # report.json がない場合のみ例外を投げる
                raise subprocess.CalledProcessError(
                    rc,
                    [codex_cmd, '--config', config_path, 'exec', '--yolo', '-m', 'gpt-5-codex', '-c', 'model_reasoning_effort="medium"'],
                    f"Codex failed. See {err_file}"
                )

            return stdout_content
            
        except subprocess.TimeoutExpired:
            # タイムアウトでも report.json が存在すれば成功扱い
            for _ in range(6):
                if report_file.exists() and report_file.stat().st_size > 0:
                    break
                time.sleep(0.5)
            if report_file.exists() and report_file.stat().st_size > 0:
                self.log(f"Timeout occurred but report found at {report_file}. Treating as success.")
                return ""
            error_msg = "Codex コマンドがタイムアウトしました（10分）"
            self.log(f"ERROR: {error_msg}")
            raise RuntimeError(error_msg)
        except subprocess.CalledProcessError:
            # CalledProcessError は既に上で処理済みなので再送出
            raise
        except Exception as e:
            # その他の例外でも report.json が存在すれば成功扱い
            for _ in range(6):
                try:
                    if report_file.exists() and report_file.stat().st_size > 0:
                        break
                except Exception:
                    pass
                time.sleep(0.5)
            try:
                if report_file.exists() and report_file.stat().st_size > 0:
                    self.log(f"Exception occurred but report found at {report_file}. Treating as success.")
                    return ""
            except Exception:
                pass
            error_msg = f"Codex コマンドの実行に失敗しました: {e}"
            self.log(f"ERROR: {error_msg}")
            raise RuntimeError(error_msg)
    
    def git_operations(self, target_path, date):
        """Git操作（add, commit, push）。target_path はファイルまたはディレクトリ"""
        try:
            # リポジトリディレクトリに移動
            original_cwd = os.getcwd()
            os.chdir(self.repo_path)
            
            try:
                # git add（相対パスで追加）
                rel_path = target_path.relative_to(self.repo_path)
                subprocess.run(['git', 'add', str(rel_path)], check=True)
                
                # git statusで変更があるかチェック
                status_result = subprocess.run(
                    ['git', 'status', '--porcelain'], 
                    capture_output=True, 
                    text=True, 
                    check=True
                )
                
                if status_result.stdout.strip():
                    # 変更がある場合はコミットとプッシュ
                    commit_msg = f"Auto: AI News report {date} (JSON)"
                    subprocess.run(['git', 'commit', '-m', commit_msg], check=True)
                    
                    subprocess.run(['git', 'push', 'origin', self.branch], check=True)
                    
                    self.log(f"Committed and pushed to {self.branch}")
                else:
                    self.log("No changes to commit")
                    
            finally:
                # 元のディレクトリに戻る
                os.chdir(original_cwd)
                
        except subprocess.CalledProcessError as e:
            raise RuntimeError(f"Git operation failed: {e}")
        except Exception as e:
            raise RuntimeError(f"Git operation error: {e}")

    def _normalize_report(self, data):
        """（未使用）将来的な入力ゆらぎ対応のために残置。現状は Codex 生成JSONをそのまま使用。"""
        return data

    def _validate_articles_schema(self, report_obj):
        """（簡易）スキーマ検証。Codex 生成JSONを前提に最低限でチェック。"""
        if not isinstance(report_obj, dict):
            raise ValueError("Report root must be an object")
        if not isinstance(report_obj.get("articles"), list):
            raise ValueError("'articles' must be an array")

    def _convert_report_json_to_markdown(self, report_obj):
        """report.json 相当のオブジェクトを Markdown に整形して返す。"""
        def esc(text):
            if text is None:
                return ""
            return str(text).strip()

        lines = []
        # ヘッダー
        lines.append(f"# AI News Report ({esc(report_obj.get('site'))})")
        lines.append("")
        lines.append(f"- Generated at: {esc(report_obj.get('generated_at'))}")
        lines.append(f"- Articles: {report_obj.get('num_articles', len(report_obj.get('articles', [])))}")
        lines.append("")

        # 各記事
        for idx, art in enumerate(report_obj.get('articles', []), start=1):
            title = esc(art.get('title')) or f"Article {idx}"
            date_val = esc(art.get('date'))
            lines.append(f"## {title}")
            if date_val:
                lines.append(f"- Date: {date_val}")
            lines.append("")

            # Executive Summary
            es = art.get('executive_summary', []) or []
            if es:
                lines.append("### Executive Summary")
                for s in es:
                    if isinstance(s, str) and s.strip():
                        lines.append(f"- {s.strip()}")
                lines.append("")

            # Key Findings
            kfs = art.get('key_findings', []) or []
            if kfs:
                lines.append("### Key Findings")
                for kf in kfs:
                    if isinstance(kf, dict):
                        point = esc(kf.get('point'))
                        foot = esc(kf.get('footnote'))
                        if foot:
                            lines.append(f"- {point} [^]")
                            lines.append(f"  - Footnote: {foot}")
                        else:
                            lines.append(f"- {point}")
                    elif isinstance(kf, str) and kf.strip():
                        lines.append(f"- {kf.strip()}")
                lines.append("")

            # References
            refs = art.get('references', []) or []
            if refs:
                lines.append("### References")
                for r in refs:
                    if isinstance(r, str) and r.strip():
                        lines.append(f"- {r.strip()}")
                lines.append("")

        return "\n".join(lines).rstrip() + "\n"

def main():
    """メイン関数"""
    runner = CodexDailyRunner()
    runner.run()

if __name__ == "__main__":
    main()
