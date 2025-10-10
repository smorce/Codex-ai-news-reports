# AI News Report (github-trending)

- Generated at: 2025-10-10T02:09:56Z
- Articles: 39

## Stremio/stremio-web

### Executive Summary
- Stremio - Freedom to Stream
- ---
- Stremio - Freedom to Stream
Stremio is a modern media center that's a one-stop solution for your video entertainment. You discover, watch and organize video content from easy to install addons.
Build
Prerequisites
Node.js 12 or higher
pnpm
10 or higher
Install dependencies
pnpm install
Start development server
pnpm start
Production build
pnpm run build
Run with Docker
docker build -t stremio-web
.
docker run -p 8080:8080 stremio-web
Screenshots
Board
Discover
Meta Details
License
Stremio is copyright 2017-2023 Smart code and available under GPLv2 license. See the
LICENSE
file in the project for more information.
- 今日の獲得スター数: 1,576
- 累積スター数: 6,765

### References
- https://github.com/Stremio/stremio-web

## TibixDev/winboat

### Executive Summary
- Run Windows apps on 🐧 Linux with ✨ seamless integration
- ---
- WinBoat
Windows for Penguins.
Run Windows apps on 🐧 Linux with ✨ seamless integration
Screenshots
⚠️
Work in Progress
⚠️
WinBoat is currently in beta, so expect to occasionally run into hiccups and bugs. You should be comfortable with some level of troubleshooting if you decide to try it, however we encourage you to give it a shot anyway.
Features
🎨 Elegant Interface
: Sleek and intuitive interface that seamlessly integrates Windows into your Linux desktop environment, making it feel like a native experience
📦 Automated Installs
: Simple installation process through our interface - pick your preferences & specs and let us handle the rest
🚀 Run Any App
: If it runs on Windows, it can run on WinBoat. Enjoy the full range of Windows applications as native OS-level windows in your Linux environment
🖥️ Full Windows Desktop
: Access the complete Windows desktop experience when you need it, or run individual apps seamlessly integrated into your Linux workflow
📁 Filesystem Integration
: Your home directory is mounted in Windows, allowing easy file sharing between the two systems without any hassle
✨ And many more
: Smartcard passthrough, resource monitoring, and more features being added regularly
How Does It Work?
WinBoat is an Electron app which allows you to run Windows apps on Linux using a containerized approach. Windows runs as a VM inside a Docker container, we communicate with it using the
WinBoat Guest Server
to retrieve data we need from Windows. For compositing applications as native OS-level windows, we use FreeRDP together with Windows's RemoteApp protocol.
Prerequisites
Before running WinBoat, ensure your system meets the following requirements:
RAM
: At least 4 GB of RAM
CPU
: At least 2 CPU threads
Storage
: At least 32 GB free space in
/var
Virtualization
: KVM enabled in BIOS/UEFI
How to enable virtualization
Docker
: Required for containerization
Installation Guide
⚠️
NOTE:
Docker Desktop is
not
supported, you will run into issues if you use it
Docker Compose v2
: Required for compatibility with docker-compose.yml files
Installation Guide
Docker User Group
: Add your user to the
docker
group
Setup Instructions
FreeRDP
: Required for remote desktop connection (Please make sure you have
Version 3.x.x
with sound support included)
Installation Guide
[OPTIONAL]
Kernel Modules
: The
iptables
/
nftables
and
iptable_nat
kernel modules can be loaded for network autodiscovery and better shared filesystem performance, but this is not obligatory in newer versions of WinBoat
Module loading instructions
Downloading
You can download the latest Linux builds under the
Releases
tab. We currently offer four variants:
AppImage:
A popular & portable app format which should run fine on most distributions
Unpacked:
The raw unpacked files, simply run the executable (
linux-unpacked/winboat
)
.deb:
The intended format for Debian based distributions
.rpm:
The intended format for Fedora based distributions
Known Issues About Container Runtimes
Podman is
unsupported
for now
Docker Desktop is
unsupported
for now
Distros that emulate Docker through a Podman socket are
unsupported
Any rootless containerization solution is currently
unsupported
Building WinBoat
For building you need to have NodeJS and Go installed on your system
Clone the repo (
git clone https://github.com/TibixDev/WinBoat
)
Install the dependencies (
npm i
)
Build the app and the guest server using
npm run build:linux-gs
You can now find the built app under
dist
with an AppImage and an Unpacked variant
Running WinBoat in development mode
Make sure you meet the
prerequisites
Additionally, for development you need to have NodeJS and Go installed on your system
Clone the repo (
git clone https://github.com/TibixDev/WinBoat
)
Install the dependencies (
npm i
)
Build the guest server (
npm run build-guest-server
)
Run the app (
npm run dev
)
Contributing
Contributions are welcome! Whether it's bug fixes, feature improvements, or documentation updates, we appreciate your help making WinBoat better.
Please note
: We maintain a focus on technical contributions only. Pull requests containing political/sexual content, or other sensitive/controversial topics will not be accepted. Let's keep things focused on making great software! 🚀
Feel free to:
Report bugs and issues
Submit feature requests
Contribute code improvements
Help with documentation
Share feedback and suggestions
Check out our issues page to get started, or feel free to open a new issue if you've found something that needs attention.
License
WinBoat is licensed under the
MIT
license
Inspiration / Alternatives
These past few years some cool projects have surfaced with similar concepts, some of which we've also taken inspirations from.
They're awesome and you should check them out:
WinApps
Cassowary
dockur/windows
(🌟 Also used in WinBoat)
Socials & Contact
Star History
- 今日の獲得スター数: 859
- 累積スター数: 8,356

### References
- https://github.com/TibixDev/winboat

## TapXWorld/ChinaTextbook

### Executive Summary
- 所有小初高、大学PDF教材。
- ---
- 项目的由来
虽然国内教育网站已提供免费资源，但大多数普通人获取信息的途径依然受限。有些人利用这一点，在某站上销售这些带有私人水印的资源。为了应对这种情况，我计划将这些资源集中并开源，以促进义务教育的普及和消除地区间的教育贫困。
还有一个最重要的原因是，希望海外华人能够让自己的孩子继续了解国内教育。
学习数学
希望未来出现更多不是为了考学而读书的人。
小学数学
一年级上册
一年级下册
二年级上册
二年级下册
三年级上册
三年级下册
四年级上册
四年级下册
五年级上册
五年级下册
六年级上册
六年级下册
初中数学
初一上册
初一下册
初二上册
初二下册
初三上册
初三下册
高中数学
目录
大学数学
高等数学
线性代数
离散数学
概率论
更多数学资料-(大学数学网)
问题：如何合并被拆分的文件？
由于 GitHub 对单个文件的上传有最大限制，超过 100MB 的文件会被拒绝上传，超过 50MB 的文件上传时会收到警告。因此，文件大小超过 50MB 的文件会被拆分成每个 35MB 的多个文件。
示例
文件被拆分的示例：
义务教育教科书 · 数学一年级上册.pdf.1
义务教育教科书 · 数学一年级上册.pdf.2
解决办法
要合并这些被拆分的文件，您只需执行以下步骤(其他操作系统同理)：
将合并程序
mergePDFs-windows-amd64.exe
下载到包含 PDF 文件的文件夹中。
确保
mergePDFs-windows-amd64.exe
和被拆分的 PDF 文件在同一目录下。
双击
mergePDFs-windows-amd64.exe
程序即可自动完成文件合并。
下载方式
您可以通过以下链接，下载文件合并程序：
下载文件合并程序
文件和程序示例
mergePDFs-windows-amd64.exe
义务教育教科书 · 数学一年级上册.pdf.1
义务教育教科书 · 数学一年级上册.pdf.2
重新下载
如果您位于内地，并且网络不错，想重新下载，您可以使用
tchMaterial-parser
项目（鼓励开源），进行重新下载。
如果您位于国外，和内地网络通信速度较慢，建议使用本存储库进行签出。
教材捐献
如果这个项目帮助您免费获取教育资源，请考虑支持我们推广开放教育的努力！您的捐献将帮助我们维护和扩展这个资源库。
加入我们的 Telegram 社区，获取最新动态并分享您的想法：
https://t.me/+1V6WjEq8WEM4MDM1
支持我
如果您觉得这个项目对您有帮助，您可以扫描以下二维码进行捐赠：
- 今日の獲得スター数: 606
- 累積スター数: 52,156

### References
- https://github.com/TapXWorld/ChinaTextbook

## aandrew-me/ytDownloader

### Executive Summary
- Desktop App for downloading Videos and Audios from hundreds of sites
- ---
- ytDownloader
A modern GUI video and audio downloader supporting
hundreds of sites
Features 🚀
✅ Supports hundreds of sites including Youtube, Facebook, Instagram, Tiktok, Twitter and so on.
✅ Multiple themes
✅ Video Compressor with Hardware Acceleration
✅ Advanced options like Range Selection, Subtitles
✅ Download playlists
✅ Available on Linux, Windows & macOS
✅ Fast download speeds
✅ And of-course no trackers or ads
Screenshots
Installation
Windows 🪟
Traditional way
Download and install the exe or msi file. Exe file lets you choose custom download location, msi file doesn't ask for location. Windows defender may show a popup saying
Windows Protected Your PC
. Just click on
More info
and click on
Run Anyway
Chocolatey
App can be installed from
Chocolatey
using the following command
choco install ytdownloader
Scoop
App can be installed with
Scoop
using the following command
scoop install https://raw.githubusercontent.com/aandrew-me/ytDownloader/main/ytdownloader.json
Winget
App can be installed with
Winget
using the following command
winget install aandrew-me.ytDownloader
Linux 🐧
Linux has several options available - Flatpak, AppImage and Snap.
Flatpak is recommended. For arm processors, download from flathub.
AppImage
AppImage
format is supported on most Linux distros and has Auto-Update support.
It just needs to be executed after downloading. See more about
AppImages here
.
AppImageLauncher
is recommended for integrating AppImages.
Flatpak
flatpak install flathub io.github.aandrew_me.ytdn
Snapcraft
sudo snap install ytdownloader
macOS 🍎
Since the app is not signed, when you will try to open the app, macOS will not allow you to open it.
You need to open terminal and execute:
sudo xattr -r -d com.apple.quarantine /Applications/YTDownloader.app
You will also need to install
yt-dlp
with
homebrew
brew install yt-dlp
Internationalization (Localization) 🌍
Translations into other languages would be highly appreciated. If you want to help translating the app to other languages, you can join from
here
. Open a new issue and that language will be added to Crowdin. Please don't make pull requests with json files, instead use Crowdin.
✅ Available languages
Name
Status
Arabic
✔️
English
✔️
Simplified Chinese
✔️
Finnish
✔️
French
✔️
German
✔️
Greek
✔️
Hungarian
✔️
Italian
✔️
Japanese
✔️
Persian
✔️
Polish
✔️
Portuguese (Brazil)
✔️
Russian
✔️
Spanish
✔️
Turkish
✔️
Ukrainian
✔️
Vietnamese
✔️
Thanks to
nxjosephofficial
,
LINUX-SAUNA
,
Proxycon
,
albanobattistella
,
TheBlueQuasar
,
MrQuerter
,
KotoWhiskas
,
André
,
haggen88
,
XfedeX
,
Jok3r
,
TitouanReal
,
soredake
,
yoi
,
HowlingWerewolf
,
Kum
,
Mohammed Bakry
,
Huang Bingfeng
and others for helping.
Used technologies
yt-dlp
Electron
ffmpeg
nodeJS
flaticon
For building or running from source code
Nodejs
(along with npm) needs to be installed.
Required commands to get started.
git clone https://github.com/aandrew-me/ytDownloader.git
cd ytDownloader
npm i
To run with
Electron
:
npm start
You need to download ffmpeg and put it in the root directory of the project. If you don't need to build for arm processor, you can download ffmpeg by executing any of the files - linux.sh / mac.sh / windows.sh depending on the platform. Otherwise you need to download ffmpeg from
here
for windows/linux and from
here
for mac (not tested)
To build for Linux (It will create packages as specified in package.json). The builds are stored in
release
folder.
npm run linux
To build for Windows
npm run windows
To build for macOS
npm run mac
If you only want to build for one format, you can do
npx electron-builder -l appimage
It will just create a linux appimage build.
- 今日の獲得スター数: 541
- 累積スター数: 4,281

### References
- https://github.com/aandrew-me/ytDownloader

## browserbase/stagehand

### Executive Summary
- The AI Browser Automation Framework
- ---
- The AI Browser Automation Framework
Read the Docs
If you're looking for the Python implementation, you can find it
here
Vibe code
Stagehand with
Director
Why Stagehand?
Most existing browser automation tools either require you to write low-level code in a framework like Selenium, Playwright, or Puppeteer, or use high-level agents that can be unpredictable in production. By letting developers choose what to write in code vs. natural language, Stagehand is the natural choice for browser automations in production.
Choose when to write code vs. natural language
: use AI when you want to navigate unfamiliar pages, and use code (
Playwright
) when you know exactly what you want to do.
Preview and cache actions
: Stagehand lets you preview AI actions before running them, and also helps you easily cache repeatable actions to save time and tokens.
Computer use models with one line of code
: Stagehand lets you integrate SOTA computer use models from OpenAI and Anthropic into the browser with one line of code.
Example
Here's how to build a sample browser automation with Stagehand:
// Use Playwright functions on the page object
const
page
=
stagehand
.
page
;
await
page
.
goto
(
"https://github.com/browserbase"
)
;
// Use act() to execute individual actions
await
page
.
act
(
"click on the stagehand repo"
)
;
// Use Computer Use agents for larger actions
const
agent
=
stagehand
.
agent
(
{
provider
:
"openai"
,
model
:
"computer-use-preview"
,
}
)
;
await
agent
.
execute
(
"Get to the latest PR"
)
;
// Use extract() to read data from the page
const
{
author
,
title
}
=
await
page
.
extract
(
{
instruction
:
"extract the author and title of the PR"
,
schema
:
z
.
object
(
{
author
:
z
.
string
(
)
.
describe
(
"The username of the PR author"
)
,
title
:
z
.
string
(
)
.
describe
(
"The title of the PR"
)
,
}
)
,
}
)
;
Documentation
Visit
docs.stagehand.dev
to view the full documentation.
Getting Started
Start with Stagehand with one line of code, or check out our
Quickstart Guide
for more information:
npx create-browser-app
Watch Anirudh demo create-browser-app to create a Stagehand project!
Build and Run from Source
git clone https://github.com/browserbase/stagehand.git
cd
stagehand
pnpm install
pnpm playwright install
pnpm run build
pnpm run example
#
run the blank script at ./examples/example.ts
pnpm run example 2048
#
run the 2048 example at ./examples/2048.ts
pnpm run evals -man
#
see evaluation suite options
Stagehand is best when you have an API key for an LLM provider and Browserbase credentials. To add these to your project, run:
cp .env.example .env
nano .env
#
Edit the .env file to add API keys
Contributing
Note
We highly value contributions to Stagehand! For questions or support, please join our
Slack community
.
At a high level, we're focused on improving reliability, speed, and cost in that order of priority. If you're interested in contributing, we strongly recommend reaching out to
Miguel Gonzalez
or
Paul Klein
in our
Slack community
before starting to ensure that your contribution aligns with our goals.
For more information, please see our
Contributing Guide
.
Acknowledgements
This project heavily relies on
Playwright
as a resilient backbone to automate the web. It also would not be possible without the awesome techniques and discoveries made by
tarsier
,
gemini-zod
, and
fuji-web
.
We'd like to thank the following people for their major contributions to Stagehand:
Paul Klein
Anirudh Kamath
Sean McGuire
Miguel Gonzalez
Sameel Arif
Filip Michalsky
Jeremy Press
Navid Pour
License
Licensed under the MIT License.
Copyright 2025 Browserbase, Inc.
- 今日の獲得スター数: 366
- 累積スター数: 17,891

### References
- https://github.com/browserbase/stagehand

## BeehiveInnovations/zen-mcp-server

### Executive Summary
- The power of Claude Code / GeminiCLI / CodexCLI + [Gemini / OpenAI / OpenRouter / Azure / Grok / Ollama / Custom Model / All Of The Above] working as one.
- ---
- Zen MCP: Many Workflows. One Context.
Zen_CLink_web.mp4
👉
Watch more examples
Your CLI + Multiple Models = Your AI Dev Team
Use the 🤖 CLI you love:
Claude Code
·
Gemini CLI
·
Codex CLI
·
Qwen Code CLI
·
Cursor
·
and more
With multiple models within a single prompt:
Gemini · OpenAI · Anthropic · Grok · Azure · Ollama · OpenRouter · DIAL · On-Device Model
🆕 Now with CLI-to-CLI Bridge
The new
clink
(CLI + Link) tool connects external AI CLIs directly into your workflow:
Connect external CLIs
like
Gemini CLI
,
Codex CLI
, and
Claude Code
directly into your workflow
CLI Subagents
- Launch isolated CLI instances from
within
your current CLI! Claude Code can spawn Codex subagents, Codex can spawn Gemini CLI subagents, etc. Offload heavy tasks (code reviews, bug hunting) to fresh contexts while your main session's context window remains unpolluted. Each subagent returns only final results.
Context Isolation
- Run separate investigations without polluting your primary workspace
Role Specialization
- Spawn
planner
,
codereviewer
, or custom role agents with specialized system prompts
Full CLI Capabilities
- Web search, file inspection, MCP tool access, latest documentation lookups
Seamless Continuity
- Sub-CLIs participate as first-class members with full conversation context between tools
#
Codex spawns Codex subagent for isolated code review in fresh context
clink with codex codereviewer to audit auth module
for
security issues
#
Subagent reviews in isolation, returns final report without cluttering your context as codex reads each file and walks the directory structure
#
Consensus from different AI models → Implementation handoff with full context preservation between tools
Use consensus with gpt-5 and gemini-pro to decide: dark mode or offline support next
Continue with clink gemini - implement the recommended feature
#
Gemini receives full debate context and starts coding immediately
👉
Learn more about clink
Why Zen MCP?
Why rely on one AI model when you can orchestrate them all?
A Model Context Protocol server that supercharges tools like
Claude Code
,
Codex CLI
, and IDE clients such
as
Cursor
or the
Claude Dev VS Code extension
.
Zen MCP connects your favorite AI tool
to multiple AI models
for enhanced code analysis, problem-solving, and collaborative development.
True AI Collaboration with Conversation Continuity
Zen supports
conversation threading
so your CLI can
discuss ideas with multiple AI models, exchange reasoning, get second opinions, and even run collaborative debates between models
to help you reach deeper insights and better solutions.
Your CLI always stays in control but gets perspectives from the best AI for each subtask. Context carries forward seamlessly across tools and models, enabling complex workflows like: code reviews with multiple models → automated planning → implementation → pre-commit validation.
You're in control.
Your CLI of choice orchestrates the AI team, but you decide the workflow. Craft powerful prompts that bring in Gemini Pro, GPT 5, Flash, or local offline models exactly when needed.
Reasons to Use Zen MCP
A typical workflow with Claude Code as an example:
Multi-Model Orchestration
- Claude coordinates with Gemini Pro, O3, GPT-5, and 50+ other models to get the best analysis for each task
Context Revival Magic
- Even after Claude's context resets, continue conversations seamlessly by having other models "remind" Claude of the discussion
Guided Workflows
- Enforces systematic investigation phases that prevent rushed analysis and ensure thorough code examination
Extended Context Windows
- Break Claude's limits by delegating to Gemini (1M tokens) or O3 (200K tokens) for massive codebases
True Conversation Continuity
- Full context flows across tools and models - Gemini remembers what O3 said 10 steps ago
Model-Specific Strengths
- Extended thinking with Gemini Pro, blazing speed with Flash, strong reasoning with O3, privacy with local Ollama
Professional Code Reviews
- Multi-pass analysis with severity levels, actionable feedback, and consensus from multiple AI experts
Smart Debugging Assistant
- Systematic root cause analysis with hypothesis tracking and confidence levels
Automatic Model Selection
- Claude intelligently picks the right model for each subtask (or you can specify)
Vision Capabilities
- Analyze screenshots, diagrams, and visual content with vision-enabled models
Local Model Support
- Run Llama, Mistral, or other models locally for complete privacy and zero API costs
Bypass MCP Token Limits
- Automatically works around MCP's 25K limit for large prompts and responses
The Killer Feature:
When Claude's context resets, just ask to "continue with O3" - the other model's response magically revives Claude's understanding without re-ingesting documents!
Example: Multi-Model Code Review Workflow
Perform a codereview using gemini pro and o3 and use planner to generate a detailed plan, implement the fixes and do a final precommit check by continuing from the previous codereview
This triggers a
codereview
workflow where Claude walks the code, looking for all kinds of issues
After multiple passes, collects relevant code and makes note of issues along the way
Maintains a
confidence
level between
exploring
,
low
,
medium
,
high
and
certain
to track how confidently it's been able to find and identify issues
Generates a detailed list of critical -> low issues
Shares the relevant files, findings, etc with
Gemini Pro
to perform a deep dive for a second
codereview
Comes back with a response and next does the same with o3, adding to the prompt if a new discovery comes to light
When done, Claude takes in all the feedback and combines a single list of all critical -> low issues, including good patterns in your code. The final list includes new findings or revisions in case Claude misunderstood or missed something crucial and one of the other models pointed this out
It then uses the
planner
workflow to break the work down into simpler steps if a major refactor is required
Claude then performs the actual work of fixing highlighted issues
When done, Claude returns to Gemini Pro for a
precommit
review
All within a single conversation thread! Gemini Pro in step 11
knows
what was recommended by O3 in step 7! Taking that context
and review into consideration to aid with its final pre-commit review.
Think of it as Claude Code
for
Claude Code.
This MCP isn't magic. It's just
super-glue
.
Remember:
Claude stays in full control — but
YOU
call the shots.
Zen is designed to have Claude engage other models only when needed — and to follow through with meaningful back-and-forth.
You're
the one who crafts the powerful prompt that makes Claude bring in Gemini, Flash, O3 — or fly solo.
You're the guide. The prompter. The puppeteer.
You are the AI -
Actually Intelligent
.
Recommended AI Stack
For Claude Code Users
For best results when using
Claude Code
:
Sonnet 4.5
- All agentic work and orchestration
Gemini 2.5 Pro
OR
GPT-5-Pro
- Deep thinking, additional code reviews, debugging and validations, pre-commit analysis
For Codex Users
For best results when using
Codex CLI
:
GPT-5 Codex Medium
- All agentic work and orchestration
Gemini 2.5 Pro
OR
GPT-5-Pro
- Deep thinking, additional code reviews, debugging and validations, pre-commit analysis
Quick Start (5 minutes)
Prerequisites:
Python 3.10+, Git,
uv installed
1. Get API Keys
(choose one or more):
OpenRouter
- Access multiple models with one API
Gemini
- Google's latest models
OpenAI
- O3, GPT-5 series
Azure OpenAI
- Enterprise deployments of GPT-4o, GPT-4.1, GPT-5 family
X.AI
- Grok models
DIAL
- Vendor-agnostic model access
Ollama
- Local models (free)
2. Install
(choose one):
Option A: Clone and Automatic Setup
(recommended)
git clone https://github.com/BeehiveInnovations/zen-mcp-server.git
cd
zen-mcp-server
#
Handles everything: setup, config, API keys from system environment.
#
Auto-configures Claude Desktop, Claude Code, Gemini CLI, Codex CLI, Qwen CLI
#
Enable / disable additional settings in .env
./run-server.sh
Option B: Instant Setup with
uvx
// Add to ~/.claude/settings.json or .mcp.json
// Don't forget to add your API keys under env
{
"mcpServers"
: {
"zen"
: {
"command"
:
"
bash
"
,
"args"
: [
"
-c
"
,
"
for p in $(which uvx 2>/dev/null) $HOME/.local/bin/uvx /opt/homebrew/bin/uvx /usr/local/bin/uvx uvx; do [ -x
\"
$p
\"
] && exec
\"
$p
\"
--from git+https://github.com/BeehiveInnovations/zen-mcp-server.git zen-mcp-server; done; echo 'uvx not found' >&2; exit 1
"
],
"env"
: {
"PATH"
:
"
/usr/local/bin:/usr/bin:/bin:/opt/homebrew/bin:~/.local/bin
"
,
"GEMINI_API_KEY"
:
"
your-key-here
"
,
"DISABLED_TOOLS"
:
"
analyze,refactor,testgen,secaudit,docgen,tracer
"
,
"DEFAULT_MODEL"
:
"
auto
"
}
    }
  }
}
3. Start Using!
"Use zen to analyze this code for security issues with gemini pro"
"Debug this error with o3 and then get flash to suggest optimizations"
"Plan the migration strategy with zen, get consensus from multiple models"
"clink with cli_name=\"gemini\" role=\"planner\" to draft a phased rollout plan"
👉
Complete Setup Guide
with detailed installation, configuration for Gemini / Codex / Qwen, and troubleshooting
👉
Cursor & VS Code Setup
for IDE integration instructions
📺
Watch tools in action
to see real-world examples
Provider Configuration
Zen activates any provider that has credentials in your
.env
. See
.env.example
for deeper customization.
Core Tools
Note:
Each tool comes with its own multi-step workflow, parameters, and descriptions that consume valuable context window space even when not in use. To optimize performance, some tools are disabled by default. See
Tool Configuration
below to enable them.
Collaboration & Planning
(Enabled by default)
clink
- Bridge requests to external AI CLIs (Gemini planner, codereviewer, etc.)
chat
- Brainstorm ideas, get second opinions, validate approaches. With capable models (GPT-5 Pro, Gemini 2.5 Pro), generates complete code / implementation
thinkdeep
- Extended reasoning, edge case analysis, alternative perspectives
planner
- Break down complex projects into structured, actionable plans
consensus
- Get expert opinions from multiple AI models with stance steering
Code Analysis & Quality
debug
- Systematic investigation and root cause analysis
precommit
- Validate changes before committing, prevent regressions
codereview
- Professional reviews with severity levels and actionable feedback
analyze
(disabled by default -
enable
)
- Understand architecture, patterns, dependencies across entire codebases
Development Tools
(Disabled by default -
enable
)
refactor
- Intelligent code refactoring with decomposition focus
testgen
- Comprehensive test generation with edge cases
secaudit
- Security audits with OWASP Top 10 analysis
docgen
- Generate documentation with complexity analysis
Utilities
apilookup
- Forces current-year API/SDK documentation lookups in a sub-process (saves tokens within the current context window), prevents outdated training data responses
challenge
- Prevent "You're absolutely right!" responses with critical analysis
tracer
(disabled by default -
enable
)
- Static analysis prompts for call-flow mapping
👉 Tool Configuration
Default Configuration
To optimize context window usage, only essential tools are enabled by default:
Enabled by default:
chat
,
thinkdeep
,
planner
,
consensus
- Core collaboration tools
codereview
,
precommit
,
debug
- Essential code quality tools
apilookup
- Rapid API/SDK information lookup
challenge
- Critical thinking utility
Disabled by default:
analyze
,
refactor
,
testgen
,
secaudit
,
docgen
,
tracer
Enabling Additional Tools
To enable additional tools, remove them from the
DISABLED_TOOLS
list:
Option 1: Edit your .env file
#
Default configuration (from .env.example)
DISABLED_TOOLS=analyze,refactor,testgen,secaudit,docgen,tracer
#
To enable specific tools, remove them from the list
#
Example: Enable analyze tool
DISABLED_TOOLS=refactor,testgen,secaudit,docgen,tracer
#
To enable ALL tools
DISABLED_TOOLS=
Option 2: Configure in MCP settings
// In ~/.claude/settings.json or .mcp.json
{
"mcpServers"
: {
"zen"
: {
"env"
: {
// Tool configuration
"DISABLED_TOOLS"
:
"
refactor,testgen,secaudit,docgen,tracer
"
,
"DEFAULT_MODEL"
:
"
pro
"
,
"DEFAULT_THINKING_MODE_THINKDEEP"
:
"
high
"
,
// API configuration
"GEMINI_API_KEY"
:
"
your-gemini-key
"
,
"OPENAI_API_KEY"
:
"
your-openai-key
"
,
"OPENROUTER_API_KEY"
:
"
your-openrouter-key
"
,
// Logging and performance
"LOG_LEVEL"
:
"
INFO
"
,
"CONVERSATION_TIMEOUT_HOURS"
:
"
6
"
,
"MAX_CONVERSATION_TURNS"
:
"
50
"
}
    }
  }
}
Option 3: Enable all tools
// Remove or empty the DISABLED_TOOLS to enable everything
{
"mcpServers"
: {
"zen"
: {
"env"
: {
"DISABLED_TOOLS"
:
"
"
}
    }
  }
}
Note:
Essential tools (
version
,
listmodels
) cannot be disabled
After changing tool configuration, restart your Claude session for changes to take effect
Each tool adds to context window usage, so only enable what you need
📺 Watch Tools In Action
Chat Tool
- Collaborative decision making and multi-turn conversations
Picking Redis vs Memcached:
Chat.Redis.or.Memcached_web.webm
Multi-turn conversation with continuation:
Chat.With.Gemini_web.webm
Consensus Tool
- Multi-model debate and decision making
Multi-model consensus debate:
Zen.Debate_web.webm
PreCommit Tool
- Comprehensive change validation
Pre-commit validation workflow:
API Lookup Tool
- Current vs outdated API documentation
Without Zen - outdated APIs:
API_without_zen_web.mp4
With Zen - current APIs:
API_with_zen.mp4
Challenge Tool
- Critical thinking vs reflexive agreement
Without Zen:
With Zen:
Key Features
AI Orchestration
Auto model selection
- Claude picks the right AI for each task
Multi-model workflows
- Chain different models in single conversations
Conversation continuity
- Context preserved across tools and models
Context revival
- Continue conversations even after context resets
Model Support
Multiple providers
- Gemini, OpenAI, Azure, X.AI, OpenRouter, DIAL, Ollama
Latest models
- GPT-5, Gemini 2.5 Pro, O3, Grok-4, local Llama
Thinking modes
- Control reasoning depth vs cost
Vision support
- Analyze images, diagrams, screenshots
Developer Experience
Guided workflows
- Systematic investigation prevents rushed analysis
Smart file handling
- Auto-expand directories, manage token limits
Web search integration
- Access current documentation and best practices
Large prompt support
- Bypass MCP's 25K token limit
Example Workflows
Multi-model Code Review:
"Perform a codereview using gemini pro and o3, then use planner to create a fix strategy"
→ Claude reviews code systematically → Consults Gemini Pro → Gets O3's perspective → Creates unified action plan
Collaborative Debugging:
"Debug this race condition with max thinking mode, then validate the fix with precommit"
→ Deep investigation → Expert analysis → Solution implementation → Pre-commit validation
Architecture Planning:
"Plan our microservices migration, get consensus from pro and o3 on the approach"
→ Structured planning → Multiple expert opinions → Consensus building → Implementation roadmap
👉
Advanced Usage Guide
for complex workflows, model configuration, and power-user features
Quick Links
📖 Documentation
Docs Overview
- High-level map of major guides
Getting Started
- Complete setup guide
Tools Reference
- All tools with examples
Advanced Usage
- Power user features
Configuration
- Environment variables, restrictions
Adding Providers
- Provider-specific setup (OpenAI, Azure, custom gateways)
Model Ranking Guide
- How intelligence scores drive auto-mode suggestions
🔧 Setup & Support
WSL Setup
- Windows users
Troubleshooting
- Common issues
Contributing
- Code standards, PR process
License
Apache 2.0 License - see
LICENSE
file for details.
Acknowledgments
Built with the power of
Multi-Model AI
collaboration 🤝
A
ctual
I
ntelligence by real Humans
MCP (Model Context Protocol)
Codex CLI
Claude Code
Gemini
OpenAI
Azure OpenAI
Star History
- 今日の獲得スター数: 273
- 累積スター数: 8,534

### References
- https://github.com/BeehiveInnovations/zen-mcp-server

## thingsboard/thingsboard

### Executive Summary
- Open-source IoT Platform - Device management, data collection, processing and visualization.
- ---
- Open-source IoT platform for data collection, processing, visualization, and device management.
💡
Get started
• 🌐
Website
• 📚
Documentation
• 📔
Blog
•
▶️
Live demo
• 🔗
LinkedIn
🚀 Installation options
Install ThingsBoard
On-premise
Try
ThingsBoard Cloud
or
Use our Live demo
💡 Getting started with ThingsBoard
Check out our
Getting Started guide
or
watch the video
to learn the basics of ThingsBoard and create your first dashboard! You will learn to:
Connect devices to ThingsBoard
Push data from devices to ThingsBoard
Build real-time dashboards
Create a Customer and assign the dashboard with them.
Define thresholds and trigger alarms
Set up notifications via email, SMS, mobile apps, or integrate with third-party services.
✨ Features
Provision and manage
devices and assets
Provision, monitor and control your IoT entities in secure way using rich server-side APIs. Define relations between your devices, assets, customers or any other entities.
Read more ➜
Collect and visualize
your data
Collect and store telemetry data in scalable and fault-tolerant way. Visualize your data with built-in or custom widgets and flexible dashboards. Share dashboards with your customers.
Read more ➜
SCADA Dashboards
Monitor and control your industrial processes in real time with SCADA. Use SCADA symbols on dashboards to create and manage any workflow, offering full flexibility to design and oversee operations according to your requirements.
Read more ➜
Process and React
Define data processing rule chains. Transform and normalize your device data. Raise alarms on incoming telemetry events, attribute updates, device inactivity and user actions.
Read more ➜
⚙️ Powerful IoT Rule Engine
ThingsBoard allows you to create complex
Rule Chains
to process data from your devices and match your application specific use cases.
Read more about Rule Engine ➜
📦 Real-Time IoT Dashboards
ThingsBoard is a scalable, user-friendly, and device-agnostic IoT platform that speeds up time-to-market with powerful built-in solution templates. It enables data collection and analysis from any devices, saving resources on routine tasks and letting you focus on your solution’s unique aspects. See more our Use Cases
here
.
Smart energy
SCADA swimming pool
Fleet tracking
Smart farming
Smart metering
Check more of our use cases ➜
🫶 Support
To get support, please visit our
GitHub issues page
📄 Licenses
This project is released under
Apache 2.0 License
- 今日の獲得スター数: 265
- 累積スター数: 20,166

### References
- https://github.com/thingsboard/thingsboard

## Zie619/n8n-workflows

### Executive Summary
- all of the workflows of n8n i could find (also from the site itself)
- ---
- ⚡ N8N Workflow Collection & Documentation
A professionally organized collection of
2,057 n8n workflows
with a lightning-fast documentation system that provides instant search, analysis, and browsing capabilities.
⚠️
IMPORTANT NOTICE (Aug 14, 2025):
Repository history has been rewritten due to DMCA compliance. If you have a fork or local clone, please see
Issue 85
for instructions on syncing your copy.
Support My Work
If you'd like to say thanks, consider buying me a coffee—your support helps me keep improving this project!
🚀
NEW: Public Search Interface & High-Performance Documentation
🌐
Browse workflows online
- No installation required!
Or run locally for development with 100x performance improvement:
Option 1: Online Search (Recommended for Users)
🔗 Visit:
zie619.github.io/n8n-workflows
⚡
Instant access
- No setup required
🔍
Search 2,057+ workflows
directly in browser
📱
Mobile-friendly
interface
🏷️
Category filtering
across 15 categories
📥
Direct download
of workflow JSON files
Option 2: Local Development System
#
Install dependencies
pip install -r requirements.txt
#
Start the fast API server
python run.py
#
Open in browser
http://localhost:8000
Features:
⚡
Sub-100ms response times
with SQLite FTS5 search
🔍
Instant full-text search
with advanced filtering
📱
Responsive design
- works perfectly on mobile
🌙
Dark/light themes
with system preference detection
📊
Live statistics
- 365 unique integrations, 29,445 total nodes
🎯
Smart categorization
by trigger type and complexity
🎯
Use case categorization
by service name mapped to categories
📄
On-demand JSON viewing
and download
🔗
Mermaid diagram generation
for workflow visualization
🔄
Real-time workflow naming
with intelligent formatting
Performance Comparison
Metric
Old System
New System
Improvement
File Size
71MB HTML
<100KB
700x smaller
Load Time
10+ seconds
<1 second
10x faster
Search
Client-side only
Full-text with FTS5
Instant
Memory Usage
~2GB RAM
<50MB RAM
40x less
Mobile Support
Poor
Excellent
Fully responsive
📂 Repository Organization
Workflow Collection
2,057 workflows
with meaningful, searchable names
365 unique integrations
across popular platforms
29,445 total nodes
with professional categorization
Quality assurance
- All workflows analyzed and categorized
Advanced Naming System ✨
Our intelligent naming system converts technical filenames into readable titles:
Before
:
2051_Telegram_Webhook_Automation_Webhook.json
After
:
Telegram Webhook Automation
100% meaningful names
with smart capitalization
Automatic integration detection
from node analysis
Use Case Category ✨
The search interface includes a dropdown filter that lets you browse 2,057+ workflows by category.
The system includes an automated categorization feature that organizes workflows by service categories to make them easier to discover and filter.
How Categorization Works
Run the categorization script
python create_categories.py
Service Name Recognition
The script analyzes each workflow JSON filename to identify recognized service names (e.g., "Twilio", "Slack", "Gmail", etc.)
Category Mapping
Each recognized service name is matched to its corresponding category using the definitions in
context/def_categories.json
. For example:
Twilio → Communication & Messaging
Gmail → Communication & Messaging
Airtable → Data Processing & Analysis
Salesforce → CRM & Sales
Search Categories Generation
The script produces a
search_categories.json
file that contains the categorized workflow data
Filter Interface
Users can then filter workflows by category in the search interface, making it easier to find workflows for specific use cases
Available Categories
The categorization system includes the following main categories:
AI Agent Development
Business Process Automation
Cloud Storage & File Management
Communication & Messaging
Creative Content & Video Automation
Creative Design Automation
CRM & Sales
Data Processing & Analysis
E-commerce & Retail
Financial & Accounting
Marketing & Advertising Automation
Project Management
Social Media Management
Technical Infrastructure & DevOps
Web Scraping & Data Extraction
Contribute Categories
You can help expand the categorization by adding more service-to-category mappings (e.g., Twilio → Communication & Messaging) in context/defs_categories.json.
Many workflow JSON files are conveniently named with the service name, often separated by underscores (_).
🛠 Usage Instructions
Option 1: Modern Fast System (Recommended)
#
Clone repository
git clone
<
repo-url
>
cd
n8n-workflows
#
Install Python dependencies
pip install -r requirements.txt
#
Start the documentation server
python run.py
#
Browse workflows at http://localhost:8000
#
- Instant search across 2,057 workflows
#
- Professional responsive interface
#
- Real-time workflow statistics
Option 2: Development Mode
#
Start with auto-reload for development
python run.py --dev
#
Or specify custom host/port
python run.py --host 0.0.0.0 --port 3000
#
Force database reindexing
python run.py --reindex
Import Workflows into n8n
#
Use the Python importer (recommended)
python import_workflows.py
#
Or manually import individual workflows:
#
1. Open your n8n Editor UI
#
2. Click menu (☰) → Import workflow
#
3. Choose any .json file from the workflows/ folder
#
4. Update credentials/webhook URLs before running
📊 Workflow Statistics
Current Collection Stats
Total Workflows
: 2,057 automation workflows
Active Workflows
: 215 (10.5% active rate)
Total Nodes
: 29,528 (avg 14.4 nodes per workflow)
Unique Integrations
: 367 different services and APIs
Database
: SQLite with FTS5 full-text search
Trigger Distribution
Complex
: 832 workflows (40.4%) - Multi-trigger systems
Webhook
: 521 workflows (25.3%) - API-triggered automations
Manual
: 478 workflows (23.2%) - User-initiated workflows
Scheduled
: 226 workflows (11.0%) - Time-based executions
Complexity Analysis
Low (≤5 nodes)
: ~35% - Simple automations
Medium (6-15 nodes)
: ~45% - Standard workflows
High (16+ nodes)
: ~20% - Complex enterprise systems
Popular Integrations
Top services by usage frequency:
Communication
: Telegram, Discord, Slack, WhatsApp
Cloud Storage
: Google Drive, Google Sheets, Dropbox
Databases
: PostgreSQL, MySQL, MongoDB, Airtable
AI/ML
: OpenAI, Anthropic, Hugging Face
Development
: HTTP Request, Webhook, GraphQL
🔍 Advanced Search Features
Smart Search Categories
Our system automatically categorizes workflows into 15 main categories:
Available Categories:
AI Agent Development
: OpenAI, Anthropic, Hugging Face, CalcsLive
Business Process Automation
: Workflow utilities, scheduling, data processing
Cloud Storage & File Management
: Google Drive, Dropbox, OneDrive, Box
Communication & Messaging
: Telegram, Discord, Slack, WhatsApp, Email
Creative Content & Video Automation
: YouTube, Vimeo, content creation
Creative Design Automation
: Canva, Figma, image processing
CRM & Sales
: Salesforce, HubSpot, Pipedrive, customer management
Data Processing & Analysis
: Database operations, analytics, data transformation
E-commerce & Retail
: Shopify, Stripe, PayPal, online stores
Financial & Accounting
: Financial tools, payment processing, accounting
Marketing & Advertising Automation
: Email marketing, campaigns, lead generation
Project Management
: Jira, Trello, Asana, task management
Social Media Management
: LinkedIn, Twitter/X, Facebook, Instagram
Technical Infrastructure & DevOps
: GitHub, deployment, monitoring
Web Scraping & Data Extraction
: HTTP requests, webhooks, data collection
API Usage Examples
#
Search workflows by text
curl
"
http://localhost:8000/api/workflows?q=telegram+automation
"
#
Filter by trigger type and complexity
curl
"
http://localhost:8000/api/workflows?trigger=Webhook&complexity=high
"
#
Find all messaging workflows
curl
"
http://localhost:8000/api/workflows/category/messaging
"
#
Get database statistics
curl
"
http://localhost:8000/api/stats
"
#
Browse available categories
curl
"
http://localhost:8000/api/categories
"
🏗 Technical Architecture
Modern Stack
SQLite Database
- FTS5 full-text search with 365 indexed integrations
FastAPI Backend
- RESTful API with automatic OpenAPI documentation
Responsive Frontend
- Modern HTML5 with embedded CSS/JavaScript
Smart Analysis
- Automatic workflow categorization and naming
Key Features
Change Detection
- MD5 hashing for efficient re-indexing
Background Processing
- Non-blocking workflow analysis
Compressed Responses
- Gzip middleware for optimal speed
Error Handling
- Graceful degradation and comprehensive logging
Mobile Optimization
- Touch-friendly interface design
Database Performance
--
Optimized schema for lightning-fast queries
CREATE
TABLE
workflows
(
    id
INTEGER
PRIMARY KEY
,
    filename
TEXT
UNIQUE,
    name
TEXT
,
    active
BOOLEAN
,
    trigger_type
TEXT
,
    complexity
TEXT
,
    node_count
INTEGER
,
    integrations
TEXT
,
--
JSON array of 365 unique services
description
TEXT
,
    file_hash
TEXT
,
--
MD5 for change detection
analyzed_at
TIMESTAMP
);
--
Full-text search with ranking
CREATE VIRTUAL TABLE workflows_fts USING fts5(
    filename, name, description, integrations, tags,
    content
=
'
workflows
'
, content_rowid
=
'
id
'
);
🔧 Setup & Requirements
System Requirements
Python 3.7+
- For running the documentation system
Modern Browser
- Chrome, Firefox, Safari, Edge
50MB Storage
- For SQLite database and indexes
n8n Instance
- For importing and running workflows
Installation
#
Clone repository
git clone
<
repo-url
>
cd
n8n-workflows
#
Install dependencies
pip install -r requirements.txt
#
Start documentation server
python run.py
#
Access at http://localhost:8000
Development Setup
#
Create virtual environment
python3 -m venv .venv
source
.venv/bin/activate
#
Linux/Mac
#
or .venv\Scripts\activate  # Windows
#
Install dependencies
pip install -r requirements.txt
#
Run with auto-reload for development
python api_server.py --reload
#
Force database reindexing
python workflow_db.py --index --force
📋 Naming Convention
Intelligent Formatting System
Our system automatically converts technical filenames to user-friendly names:
#
Automatic transformations:
2051_Telegram_Webhook_Automation_Webhook.json →
"
Telegram Webhook Automation
"
0250_HTTP_Discord_Import_Scheduled.json →
"
HTTP Discord Import Scheduled
"
0966_OpenAI_Data_Processing_Manual.json →
"
OpenAI Data Processing Manual
"
Technical Format
[ID]_[Service1]_[Service2]_[Purpose]_[Trigger].json
Smart Capitalization Rules
HTTP
→ HTTP (not Http)
API
→ API (not Api)
webhook
→ Webhook
automation
→ Automation
scheduled
→ Scheduled
🚀 API Documentation
Core Endpoints
GET /
- Main workflow browser interface
GET /api/stats
- Database statistics and metrics
GET /api/workflows
- Search with filters and pagination
GET /api/workflows/{filename}
- Detailed workflow information
GET /api/workflows/{filename}/download
- Download workflow JSON
GET /api/workflows/{filename}/diagram
- Generate Mermaid diagram
Advanced Search
GET /api/workflows/category/{category}
- Search by service category
GET /api/categories
- List all available categories
GET /api/integrations
- Get integration statistics
POST /api/reindex
- Trigger background reindexing
Response Examples
// GET /api/stats
{
"total"
:
2053
,
"active"
:
215
,
"inactive"
:
1838
,
"triggers"
: {
"Complex"
:
831
,
"Webhook"
:
519
,
"Manual"
:
477
,
"Scheduled"
:
226
},
"total_nodes"
:
29445
,
"unique_integrations"
:
365
}
🤝 Contributing
🎉 This project solves
Issue #84
- providing online access to workflows without requiring local setup!
Adding New Workflows
Export workflow
as JSON from n8n
Name descriptively
following the established pattern:
[ID]_[Service]_[Purpose]_[Trigger].json
Add to workflows/
directory (create service folder if needed)
Remove sensitive data
(credentials, personal URLs)
Add tags
for better searchability (calculation, automation, etc.)
GitHub Actions automatically
updates the public search interface
Quality Standards
✅ Workflow must be functional and tested
✅ Remove all credentials and sensitive data
✅ Follow naming convention for consistency
✅ Verify compatibility with recent n8n versions
✅ Include meaningful description or comments
✅ Add relevant tags for search optimization
Custom Node Workflows
✅ Include npm package links in descriptions
✅ Document custom node requirements
✅ Add installation instructions
✅ Use descriptive tags (like CalcsLive example)
Reindexing (for local development)
#
Force database reindexing after adding workflows
python run.py --reindex
#
Or update search index only
python scripts/generate_search_index.py
⚠️
Important Notes
Security & Privacy
Review before use
- All workflows shared as-is for educational purposes
Update credentials
- Replace API keys, tokens, and webhooks
Test safely
- Verify in development environment first
Check permissions
- Ensure proper access rights for integrations
Compatibility
n8n Version
- Compatible with n8n 1.0+ (most workflows)
Community Nodes
- Some workflows may require additional node installations
API Changes
- External services may have updated their APIs since creation
Dependencies
- Verify required integrations before importing
📚 Resources & References
Workflow Sources
This comprehensive collection includes workflows from:
Official n8n.io
- Documentation and community examples
GitHub repositories
- Open source community contributions
Blog posts & tutorials
- Real-world automation patterns
User submissions
- Tested and verified workflows
Enterprise use cases
- Business process automations
Learn More
n8n Documentation
- Official documentation
n8n Community
- Community forum and support
Workflow Templates
- Official template library
Integration Docs
- Service-specific guides
🏆 Project Achievements
Repository Transformation
2,053 workflows
professionally organized and named
365 unique integrations
automatically detected and categorized
100% meaningful names
(improved from basic filename patterns)
Zero data loss
during intelligent renaming process
Advanced search
with 15 service categories
Performance Revolution
Sub-100ms search
with SQLite FTS5 full-text indexing
Instant filtering
across 29,445 workflow nodes
Mobile-optimized
responsive design for all devices
Real-time statistics
with live database queries
Professional interface
with modern UX principles
System Reliability
Robust error handling
with graceful degradation
Change detection
for efficient database updates
Background processing
for non-blocking operations
Comprehensive logging
for debugging and monitoring
Production-ready
with proper middleware and security
This repository represents the most comprehensive and well-organized collection of n8n workflows available, featuring cutting-edge search technology and professional documentation that makes workflow discovery and usage a delightful experience.
🎯 Perfect for
: Developers, automation engineers, business analysts, and anyone looking to streamline their workflows with proven n8n automations.
中文
- 今日の獲得スター数: 240
- 累積スター数: 35,687

### References
- https://github.com/Zie619/n8n-workflows

## MODSetter/SurfSense

### Executive Summary
- Open Source Alternative to NotebookLM / Perplexity, connected to external sources such as Search Engines, Slack, Linear, Jira, ClickUp, Confluence, Notion, YouTube, GitHub, Discord and more. Join our discord: https://discord.gg/ejRNvftDp9
- ---
- SurfSense
While tools like NotebookLM and Perplexity are impressive and highly effective for conducting research on any topic/query, SurfSense elevates this capability by integrating with your personal knowledge base. It is a highly customizable AI research agent, connected to external sources such as Search Engines (Tavily, LinkUp), Slack, Linear, Jira, ClickUp, Confluence, Gmail, Notion, YouTube, GitHub, Discord, Airtable, Google Calendar, Luma and more to come.
Video
temp_demo_v7.mp4
Podcast Sample
elon_vs_trump_podcast.mp4
Key Features
💡
Idea
:
Have your own highly customizable private NotebookLM and Perplexity integrated with external sources.
📁
Multiple File Format Uploading Support
Save content from your own personal files
(Documents, images, videos and supports
50+ file extensions
)
to your own personal knowledge base .
🔍
Powerful Search
Quickly research or find anything in your saved content .
💬
Chat with your Saved Content
Interact in Natural Language and get cited answers.
📄
Cited Answers
Get Cited answers just like Perplexity.
🔔
Privacy & Local LLM Support
Works Flawlessly with Ollama local LLMs.
🏠
Self Hostable
Open source and easy to deploy locally.
🎙️ Podcasts
Blazingly fast podcast generation agent. (Creates a 3-minute podcast in under 20 seconds.)
Convert your chat conversations into engaging audio content
Support for local TTS providers (Kokoro TTS)
Support for multiple TTS providers (OpenAI, Azure, Google Vertex AI)
📊
Advanced RAG Techniques
Supports 100+ LLM's
Supports 6000+ Embedding Models.
Supports all major Rerankers (Pinecode, Cohere, Flashrank etc)
Uses Hierarchical Indices (2 tiered RAG setup).
Utilizes Hybrid Search (Semantic + Full Text Search combined with Reciprocal Rank Fusion).
RAG as a Service API Backend.
ℹ️
External Sources
Search Engines (Tavily, LinkUp)
Slack
Linear
Jira
ClickUp
Confluence
Notion
Gmail
Youtube Videos
GitHub
Discord
Airtable
Google Calendar
Luma
and more to come.....
📄
Supported File Extensions
Note
: File format support depends on your ETL service configuration. LlamaCloud supports 50+ formats, Unstructured supports 34+ core formats, and Docling (core formats, local processing, privacy-focused, no API key).
Documents & Text
LlamaCloud
:
.pdf
,
.doc
,
.docx
,
.docm
,
.dot
,
.dotm
,
.rtf
,
.txt
,
.xml
,
.epub
,
.odt
,
.wpd
,
.pages
,
.key
,
.numbers
,
.602
,
.abw
,
.cgm
,
.cwk
,
.hwp
,
.lwp
,
.mw
,
.mcw
,
.pbd
,
.sda
,
.sdd
,
.sdp
,
.sdw
,
.sgl
,
.sti
,
.sxi
,
.sxw
,
.stw
,
.sxg
,
.uof
,
.uop
,
.uot
,
.vor
,
.wps
,
.zabw
Unstructured
:
.doc
,
.docx
,
.odt
,
.rtf
,
.pdf
,
.xml
,
.txt
,
.md
,
.markdown
,
.rst
,
.html
,
.org
,
.epub
Docling
:
.pdf
,
.docx
,
.html
,
.htm
,
.xhtml
,
.adoc
,
.asciidoc
Presentations
LlamaCloud
:
.ppt
,
.pptx
,
.pptm
,
.pot
,
.potm
,
.potx
,
.odp
,
.key
Unstructured
:
.ppt
,
.pptx
Docling
:
.pptx
Spreadsheets & Data
LlamaCloud
:
.xlsx
,
.xls
,
.xlsm
,
.xlsb
,
.xlw
,
.csv
,
.tsv
,
.ods
,
.fods
,
.numbers
,
.dbf
,
.123
,
.dif
,
.sylk
,
.slk
,
.prn
,
.et
,
.uos1
,
.uos2
,
.wk1
,
.wk2
,
.wk3
,
.wk4
,
.wks
,
.wq1
,
.wq2
,
.wb1
,
.wb2
,
.wb3
,
.qpw
,
.xlr
,
.eth
Unstructured
:
.xls
,
.xlsx
,
.csv
,
.tsv
Docling
:
.xlsx
,
.csv
Images
LlamaCloud
:
.jpg
,
.jpeg
,
.png
,
.gif
,
.bmp
,
.svg
,
.tiff
,
.webp
,
.html
,
.htm
,
.web
Unstructured
:
.jpg
,
.jpeg
,
.png
,
.bmp
,
.tiff
,
.heic
Docling
:
.jpg
,
.jpeg
,
.png
,
.bmp
,
.tiff
,
.tif
,
.webp
Audio & Video
(Always Supported)
.mp3
,
.mpga
,
.m4a
,
.wav
,
.mp4
,
.mpeg
,
.webm
Email & Communication
Unstructured
:
.eml
,
.msg
,
.p7s
🔖 Cross Browser Extension
The SurfSense extension can be used to save any webpage you like.
Its main usecase is to save any webpages protected beyond authentication.
FEATURE REQUESTS AND FUTURE
SurfSense is actively being developed.
While it's not yet production-ready, you can help us speed up the process.
Join the
SurfSense Discord
and help shape the future of SurfSense!
🚀 Roadmap
Stay up to date with our development progress and upcoming features!
Check out our public roadmap and contribute your ideas or feedback:
View the Roadmap:
SurfSense Roadmap on GitHub Projects
How to get started?
Installation Options
SurfSense provides two installation methods:
Docker Installation
- The easiest way to get SurfSense up and running with all dependencies containerized.
Includes pgAdmin for database management through a web UI
Supports environment variable customization via
.env
file
Flexible deployment options (full stack or core services only)
No need to manually edit configuration files between environments
See
Docker Setup Guide
for detailed instructions
For deployment scenarios and options, see
Deployment Guide
Manual Installation (Recommended)
- For users who prefer more control over their setup or need to customize their deployment.
Both installation guides include detailed OS-specific instructions for Windows, macOS, and Linux.
Before installation, make sure to complete the
prerequisite setup steps
including:
PGVector setup
File Processing ETL Service
(choose one):
Unstructured.io API key (supports 34+ formats)
LlamaIndex API key (enhanced parsing, supports 50+ formats)
Docling (local processing, no API key required, supports PDF, Office docs, images, HTML, CSV)
Other required API keys
Screenshots
Research Agent
Search Spaces
Manage Documents
Podcast Agent
Agent Chat
Browser Extension
Tech Stack
BackEnd
FastAPI
: Modern, fast web framework for building APIs with Python
PostgreSQL with pgvector
: Database with vector search capabilities for similarity searches
SQLAlchemy
: SQL toolkit and ORM (Object-Relational Mapping) for database interactions
Alembic
: A database migrations tool for SQLAlchemy.
FastAPI Users
: Authentication and user management with JWT and OAuth support
LangGraph
: Framework for developing AI-agents.
LangChain
: Framework for developing AI-powered applications.
LLM Integration
: Integration with LLM models through LiteLLM
Rerankers
: Advanced result ranking for improved search relevance
Hybrid Search
: Combines vector similarity and full-text search for optimal results using Reciprocal Rank Fusion (RRF)
Vector Embeddings
: Document and text embeddings for semantic search
pgvector
: PostgreSQL extension for efficient vector similarity operations
Chonkie
: Advanced document chunking and embedding library
Uses
AutoEmbeddings
for flexible embedding model selection
LateChunker
for optimized document chunking based on embedding model's max sequence length
FrontEnd
Next.js 15.2.3
: React framework featuring App Router, server components, automatic code-splitting, and optimized rendering.
React 19.0.0
: JavaScript library for building user interfaces.
TypeScript
: Static type-checking for JavaScript, enhancing code quality and developer experience.
Vercel AI SDK Kit UI Stream Protocol
: To create scalable chat UI.
Tailwind CSS 4.x
: Utility-first CSS framework for building custom UI designs.
Shadcn
: Headless components library.
Lucide React
: Icon set implemented as React components.
Framer Motion
: Animation library for React.
Sonner
: Toast notification library.
Geist
: Font family from Vercel.
React Hook Form
: Form state management and validation.
Zod
: TypeScript-first schema validation with static type inference.
@hookform/resolvers
: Resolvers for using validation libraries with React Hook Form.
@tanstack/react-table
: Headless UI for building powerful tables & datagrids.
DevOps
Docker
: Container platform for consistent deployment across environments
Docker Compose
: Tool for defining and running multi-container Docker applications
pgAdmin
: Web-based PostgreSQL administration tool included in Docker setup
Extension
Manifest v3 on Plasmo
Future Work
Add More Connectors.
Patch minor bugs.
Document Podcasts
Contribute
Contributions are very welcome! A contribution can be as small as a ⭐ or even finding and creating issues.
Fine-tuning the Backend is always desired.
For detailed contribution guidelines, please see our
CONTRIBUTING.md
file.
Star History
- 今日の獲得スター数: 236
- 累積スター数: 8,894

### References
- https://github.com/MODSetter/SurfSense

## timelinize/timelinize

### Executive Summary
- Store your data from all your accounts and devices in a single cohesive timeline on your own computer
- ---
- Organize your photos & videos, chats & messages, location history, social media content, contacts, and more into a single cohesive timeline on your own computer where you can keep them alive forever.
Timelinize lets you import your data from practically anywhere: your computer, phone, online accounts, GPS-enabled radios, various apps and programs, contact lists, cameras, and more.
Join our Discord
to discuss!
Note
I am looking for a better name for this project. If you have an idea for a good name that is short, relevant, unique, and available,
I'd love to hear it!
Screenshots
These were captured using a dev repository of mine filled with a subset of my real data, so I've run Timelinize in obfuscation mode: images and videos are blurred (except profile pictures---need to fix that); names, identifiers, and locations around sensitive areas are all randomized, and text has been replaced with random words so that the string is about the same length.
(I hope to make a video tour soon.)
Please remember this is an early alpha preview, and the software is very much evolving and improving. And you can help!
WIP dashboard.
Very
WIP. The bubble chart is particularly interesting as it shows you what kinds of data are most common at which times of day throughout the years.
The classic timeline view is a combination of all data grouped by types and time segments for reconstructing a day or other custom time period.
Viewing an item shows all the information about it, regardless of type: text, photo, live photo, video, location, etc.
I had to make a custom file picker since browser APIs are too limiting. This is how you'll import most of your data into your timeline, but this flow is being revised soon.
The large map view is capable of 3D exploration, showing your memories right where they happened with a color-coded path that represents time.
Because Timelinize is entity-aware and supports multiple data sources, it can show data on a map even if it doesn't have geolocation information. That's what the gray dots or pins represent. In this example, a text message was received while at church, even though it doesn't have any geolocation info associated with it directly.
Timelinize treats entities (people, pets/animals, organizations, etc.) as first-class data points which you can filter and organize.
Timelinize will automatically recognize the same entity across data sources with enough information, but if it isn't possible automatically, you can manually merge entities with a click.
Conversations are aggregated across data sources that have messaging capabilities. They become emergent from the database by querying relationships between items and entities.
In this conversation view, you can see messages exchanged with this person across both Facebook and SMS/text message are displayed together. Reactions are also supported.
A gallery displays photos and videos, but not just those in your photo library: it includes pictures and memes sent via messages, photos and videos uploaded to social media, and any other photos/videos in your data. You can always filter to drill down.
How it works
Obtain your data.
This usually involves exporting your data from apps, online accounts, or devices. For example, requesting an archive from Google Takeout. (Apple iCloud, Facebook, Twitter/X, Strava, Instagram, etc. all offer similar functionality for GDPR compliance.) Do this early/soon, because some services take days to provide your data.
Import your data using Timelinize. You don't need to extract or decompress .tar or .zip archives; Timelinize will attempt to recognize your data in its original format and folder structure. All the data you import is indexed in a SQLite database and stored on disk organized by date -- no obfuscation or proprietary formats; you can simply browse your files if you wish.
Explore and organize! Timelinize has a UI that portrays data using various projections and filters. It can recall moments from your past and help you view your life more comprehensively. (It's a great living family history tool.)
Repeat steps 1-3 as often as desired. Timelinize will skip any existing data that is the same and only import new content. You could do this every few weeks or months for busy accounts that are most important to you.
Caution
Timelinize is in active development and is still considered unstable. The schema is still changing, necessitating starting over from a clean slate when updating. Always keep your original source data. Expect to delete and recreate your timelines as you upgrade during this alpha development period.
Download and run
Download the
latest release
for your platform.
See the website for
installation instructions
.
Develop
See our
project wiki
for instructions on
compiling from source
.
Command line interface
Timelinize has a symmetric HTTP API and CLI. When an HTTP API endpoint is created in the code, it automatically adds to the command line as well.
Run
timelinize help
(or
go run main.go help
if you're running from source) to view the list of commands, which are also HTTP endpoints. JSON or form inputs are converted to command line args/flags that represent the JSON schema or form fields.
Setup Development Environment
Dev Container setup is provided for easy development using GitHub Codespaces or Visual Studio Code with the DevContainers extension.
Getting started with VSCode
Make sure you have the following installed:
Docker
DevContainers for VSCode
Open this project in VSCode
Go to the
Remote Explorer
on Activity Bar
Click on
New Dev Container (+)
Click on
Open Current Folder in Container
This sets up a docker container with all the dependencies required for building this project. You can get started with contributing quickly.
Motivation and vision
(For roadmap, see
issues tagged
long-term 🔭
.)
The motivation for this project is two-fold. Both press upon me with a sense of urgency, which is why I dedicated some nights and weekends to work on this.
Connecting with my family -- both living and deceased -- is important to me and my close relatives. But I wish we had more insights into the lives of those who came before us. What was important to them? Where did they live / travel / spend their time? What lessons did they learn? How did global and local events -- or heck, even the weather -- affect them? What hardships did they endure? What would they have wanted to remember? What would it be like to talk to them? A lot of this could not be known unless they wrote it all down. But these days, we have that data for ourselves. What better time than right now to start collecting personal histories from all available sources and develop a rich timeline of our life for our family, or even just for our own reference and nostalgia.
Our lives are better-documented than any before us, but the record of our life is more ephemeral than any before us, too. We lose control of our data by relying on centralized, proprietary apps and cloud services which are useful today, and gone tomorrow. I wrote Timelinize because now is the time to liberate my data from corporations who don't own it, yet who have the only copy of it. This reality has made me feel uneasy for years, and it's not going away soon. Timelinize makes it bearable.
Imagine being able to pull up a single screen with your data from any and all of your online accounts and services -- while offline. And there you see so many aspects of your life at a glance: your photos and videos, social media posts, locations on a map and how you got there, emails and letters, documents, health and physical activities, mental and emotional wellness, and maybe even music you listened to, for any given day. You can "zoom out" and get the big picture. Machine learning algorithms could suggest major clusters based on your content to summarize your days, months, or years, and from that, even recommend printing physical memorabilia. It's like a highly-detailed, automated journal, fully in your control, which you can add to in the app: augment it with your own thoughts like a regular journal.
Then cross-reference your own timeline with a global public timeline: see how locations you went to changed over time, or what major news events may have affected you, or what the political/social climate -- or the literal climate -- was like at the time. For example, you may wonder, "Why did the family stay inside so much of the summer one year?" You could then see, "Oh, because it was 110 F (43 C) degrees for two months straight."
Or translate the projection sideways, and instead of looking at time cross-sections, look at cross-sections of your timeline by media type: photos, posts, location, sentiment. Look at plots, charts, graphs, of your physical activity.
Or view projections by space instead of time: view interrelations between items on a map, even items that don't have location data, because the database is entity-aware. So if a person receives a text message and the same person has location information at about the same time from a photo or GPS device, then the text message can appear on a map too, reminding you where you first got the text with the news about your nephew's birth.
And all of this runs on your own computer: no one else has access to it, no one else owns it, but you.
And if everyone had their own timeline, in theory they could be merged into a global supertimeline to become a thorough record of the human race, all without the need for centralizing our data on cloud services that are controlled by greedy corporations.
History
I've been working on this project since about 2013, even before I conceptualized
Caddy
. My initial vision was to create an automated backup of my Picasa albums that I could store on my own hard drive. This project was called Photobak. Picasa eventually became Google Photos, and about the same time I realized I wanted to backup my photos posted to Facebook, Instagram, and Twitter, too. And while I was at it, why not include my Google Location History to augment the location data from the photos. The vision continued to expand as I realized that my family could use this too, so the schema was upgraded to support multiple people/entities as well. This could allow us to merge databases, or timelines, as family members pass, or as they share parts of their timeline around with each other. Timelinize is the mature evolution of the original project that is now designed to be a comprehensive, highly detailed archive of one's life through digital (or
digitized
) content. An authoritative, unified record that is easy to preserve and organize.
License
This project is licensed with AGPL. I chose this license because I do not want others to make proprietary or commercial software using this package. The point of this project is liberation of and control over one's own, personal data, and I want to ensure that this project won't be used in anything that would perpetuate the walled garden dilemma we already face today. Even if the future of this project ever has proprietary source code, I can ensure it will stay aligned with my values and the project's original goals.
- 今日の獲得スター数: 225
- 累積スター数: 2,204

### References
- https://github.com/timelinize/timelinize

## openai/codex

### Executive Summary
- Lightweight coding agent that runs in your terminal
- ---
- npm i -g @openai/codex
or
brew install codex
Codex CLI
is a coding agent from OpenAI that runs locally on your computer.
If you want Codex in your code editor (VS Code, Cursor, Windsurf),
install in your IDE
If you are looking for the
cloud-based agent
from OpenAI,
Codex Web
, go to
chatgpt.com/codex
Quickstart
Installing and running Codex CLI
Install globally with your preferred package manager. If you use npm:
npm install -g @openai/codex
Alternatively, if you use Homebrew:
brew install codex
Then simply run
codex
to get started:
codex
You can also go to the
latest GitHub Release
and download the appropriate binary for your platform.
Each GitHub Release contains many executables, but in practice, you likely want one of these:
macOS
Apple Silicon/arm64:
codex-aarch64-apple-darwin.tar.gz
x86_64 (older Mac hardware):
codex-x86_64-apple-darwin.tar.gz
Linux
x86_64:
codex-x86_64-unknown-linux-musl.tar.gz
arm64:
codex-aarch64-unknown-linux-musl.tar.gz
Each archive contains a single entry with the platform baked into the name (e.g.,
codex-x86_64-unknown-linux-musl
), so you likely want to rename it to
codex
after extracting it.
Using Codex with your ChatGPT plan
Run
codex
and select
Sign in with ChatGPT
. We recommend signing into your ChatGPT account to use Codex as part of your Plus, Pro, Team, Edu, or Enterprise plan.
Learn more about what's included in your ChatGPT plan
.
You can also use Codex with an API key, but this requires
additional setup
. If you previously used an API key for usage-based billing, see the
migration steps
. If you're having trouble with login, please comment on
this issue
.
Model Context Protocol (MCP)
Codex can access MCP servers. To configure them, refer to the
config docs
.
Configuration
Codex CLI supports a rich set of configuration options, with preferences stored in
~/.codex/config.toml
. For full configuration options, see
Configuration
.
Docs & FAQ
Getting started
CLI usage
Running with a prompt as input
Example prompts
Memory with AGENTS.md
Configuration
Sandbox & approvals
Authentication
Auth methods
Login on a "Headless" machine
Automating Codex
GitHub Action
TypeScript SDK
Non-interactive mode (
codex exec
)
Advanced
Tracing / verbose logging
Model Context Protocol (MCP)
Zero data retention (ZDR)
Contributing
Install & build
System Requirements
DotSlash
Build from source
FAQ
Open source fund
License
This repository is licensed under the
Apache-2.0 License
.
- 今日の獲得スター数: 219
- 累積スター数: 46,727

### References
- https://github.com/openai/codex

## google/computer-use-preview

### Executive Summary
- ---
- Computer Use Preview
Quick Start
This section will guide you through setting up and running the Computer Use Preview model. Follow these steps to get started.
1. Installation
Clone the Repository
git clone https://github.com/google/computer-use-preview.git
cd
computer-use-preview
Set up Python Virtual Environment and Install Dependencies
python3 -m venv .venv
source
.venv/bin/activate
pip install -r requirements.txt
Install Playwright and Browser Dependencies
#
Install system dependencies required by Playwright for Chrome
playwright install-deps chrome
#
Install the Chrome browser for Playwright
playwright install chrome
2. Configuration
You can get started using either the Gemini Developer API or Vertex AI.
A. If using the Gemini Developer API:
You need a Gemini API key to use the agent:
export
GEMINI_API_KEY=
"
YOUR_GEMINI_API_KEY
"
Or to add this to your virtual environment:
echo
'
export GEMINI_API_KEY="YOUR_GEMINI_API_KEY"
'
>>
.venv/bin/activate
#
After editing, you'll need to deactivate and reactivate your virtual
#
environment if it's already active:
deactivate
source
.venv/bin/activate
Replace
YOUR_GEMINI_API_KEY
with your actual key.
B. If using the Vertex AI Client:
You need to explicitly use Vertex AI, then provide project and location to use the agent:
export
USE_VERTEXAI=true
export
VERTEXAI_PROJECT=
"
YOUR_PROJECT_ID
"
export
VERTEXAI_LOCATION=
"
YOUR_LOCATION
"
Or to add this to your virtual environment:
echo
'
export USE_VERTEXAI=true
'
>>
.venv/bin/activate
echo
'
export VERTEXAI_PROJECT="your-project-id"
'
>>
.venv/bin/activate
echo
'
export VERTEXAI_LOCATION="your-location"
'
>>
.venv/bin/activate
#
After editing, you'll need to deactivate and reactivate your virtual
#
environment if it's already active:
deactivate
source
.venv/bin/activate
Replace
YOUR_PROJECT_ID
and
YOUR_LOCATION
with your actual project and location.
3. Running the Tool
The primary way to use the tool is via the
main.py
script.
General Command Structure:
python main.py --query
"
Go to Google and type 'Hello World' into the search bar
"
Available Environments:
You can specify a particular environment with the
--env <environment>
flag.  Available options:
playwright
: Runs the browser locally using Playwright.
browserbase
: Connects to a Browserbase instance.
Local Playwright
Runs the agent using a Chrome browser instance controlled locally by Playwright.
python main.py --query=
"
Go to Google and type 'Hello World' into the search bar
"
--env=
"
playwright
"
You can also specify an initial URL for the Playwright environment:
python main.py --query=
"
Go to Google and type 'Hello World' into the search bar
"
--env=
"
playwright
"
--initial_url=
"
https://www.google.com/search?q=latest+AI+news
"
Browserbase
Runs the agent using Browserbase as the browser backend. Ensure the proper Browserbase environment variables are set:
BROWSERBASE_API_KEY
and
BROWSERBASE_PROJECT_ID
.
python main.py --query=
"
Go to Google and type 'Hello World' into the search bar
"
--env=
"
browserbase
"
Agent CLI
The
main.py
script is the command-line interface (CLI) for running the browser agent.
Command-Line Arguments
Argument
Description
Required
Default
Supported Environment(s)
--query
The natural language query for the browser agent to execute.
Yes
N/A
All
--env
The computer use environment to use. Must be one of the following:
playwright
, or
browserbase
No
N/A
All
--initial_url
The initial URL to load when the browser starts.
No
https://www.google.com
All
--highlight_mouse
If specified, the agent will attempt to highlight the mouse cursor's position in the screenshots. This is useful for visual debugging.
No
False (not highlighted)
playwright
Environment Variables
Variable
Description
Required
GEMINI_API_KEY
Your API key for the Gemini model.
Yes
BROWSERBASE_API_KEY
Your API key for Browserbase.
Yes (when using the browserbase environment)
BROWSERBASE_PROJECT_ID
Your Project ID for Browserbase.
Yes (when using the browserbase environment)
- 今日の獲得スター数: 203
- 累積スター数: 688

### References
- https://github.com/google/computer-use-preview

## LukeGus/Termix

### Executive Summary
- Termix is a web-based server management platform with SSH terminal, tunneling, and file editing capabilities.
- ---
- Repo Stats
English |
中文
Achieved on September 1st, 2025
Top Technologies
If you would like, you can support the project here!
Overview
Termix is an open-source, forever-free, self-hosted all-in-one server management platform. It provides a web-based
solution for managing your servers and infrastructure through a single, intuitive interface. Termix offers SSH terminal
access, SSH tunneling capabilities, and remote file management, with many more tools to come.
Features
SSH Terminal Access
- Full-featured terminal with split-screen support (up to 4 panels) and tab system
SSH Tunnel Management
- Create and manage SSH tunnels with automatic reconnection and health monitoring
Remote File Manager
- Manage files directly on remote servers with support for viewing and editing code, images, audio, and video. Upload, download, rename, delete, and move files seamlessly.
SSH Host Manager
- Save, organize, and manage your SSH connections with tags and folders and easily save reusable login info while being able to automate the deploying of SSH keys
Server Stats
- View CPU, memory, and HDD usage on any SSH server
User Authentication
- Secure user management with admin controls and OIDC and 2FA (TOTP) support
Database Encryption
- SQLite database files encrypted at rest with automatic encryption/decryption
Data Export/Import
- Export and import SSH hosts, credentials, and file manager data with incremental sync
Automatic SSL Setup
- Built-in SSL certificate generation and management with HTTPS redirects
Modern UI
- Clean desktop/mobile-friendly interface built with React, Tailwind CSS, and Shadcn
Languages
- Built-in support for English, Chinese, and German
Platform Support
- Available as a web app, desktop application (Windows & Linux), and dedicated mobile app for iOS and Android. macOS and iPadOS support is planned.
Planned Features
See
Projects
for all planned features. If you are looking to contribute, see
Contributing
.
Installation
Supported Devices:
Website (any modern browser like Google, Safari, and Firefox)
Windows (app)
Linux (app)
iOS (app)
Android (app)
iPadOS and macOS are in progress
Visit the Termix
Docs
for more information on how to install Termix on all platforms. Otherwise, view
a sample Docker Compose file here:
services
:
termix
:
image
:
ghcr.io/lukegus/termix:latest
container_name
:
termix
restart
:
unless-stopped
ports
:
      -
"
8080:8080
"
volumes
:
      -
termix-data:/app/data
environment
:
PORT
:
"
8080
"
volumes
:
termix-data
:
driver
:
local
Support
If you need help with Termix, you can join the
Discord
server and visit the support
channel. You can also open an issue or open a pull request on the
GitHub
repo.
Show-off
2025-09-30.23-13-19.mp4
License
Distributed under the Apache License Version 2.0. See LICENSE for more information.
- 今日の獲得スター数: 119
- 累積スター数: 5,131

### References
- https://github.com/LukeGus/Termix

## openai/openai-agents-python

### Executive Summary
- A lightweight, powerful framework for multi-agent workflows
- ---
- OpenAI Agents SDK
The OpenAI Agents SDK is a lightweight yet powerful framework for building multi-agent workflows. It is provider-agnostic, supporting the OpenAI Responses and Chat Completions APIs, as well as 100+ other LLMs.
Note
Looking for the JavaScript/TypeScript version? Check out
Agents SDK JS/TS
.
Core concepts:
Agents
: LLMs configured with instructions, tools, guardrails, and handoffs
Handoffs
: A specialized tool call used by the Agents SDK for transferring control between agents
Guardrails
: Configurable safety checks for input and output validation
Sessions
: Automatic conversation history management across agent runs
Tracing
: Built-in tracking of agent runs, allowing you to view, debug and optimize your workflows
Explore the
examples
directory to see the SDK in action, and read our
documentation
for more details.
Get started
To get started, set up your Python environment (Python 3.9 or newer required), and then install OpenAI Agents SDK package.
venv
python -m venv .venv
source
.venv/bin/activate
#
On Windows: .venv\Scripts\activate
pip install openai-agents
For voice support, install with the optional
voice
group:
pip install 'openai-agents[voice]'
.
For Redis session support, install with the optional
redis
group:
pip install 'openai-agents[redis]'
.
uv
If you're familiar with
uv
, using the tool would be even similar:
uv init
uv add openai-agents
For voice support, install with the optional
voice
group:
uv add 'openai-agents[voice]'
.
For Redis session support, install with the optional
redis
group:
uv add 'openai-agents[redis]'
.
Hello world example
from
agents
import
Agent
,
Runner
agent
=
Agent
(
name
=
"Assistant"
,
instructions
=
"You are a helpful assistant"
)
result
=
Runner
.
run_sync
(
agent
,
"Write a haiku about recursion in programming."
)
print
(
result
.
final_output
)
# Code within the code,
# Functions calling themselves,
# Infinite loop's dance.
(
If running this, ensure you set the
OPENAI_API_KEY
environment variable
)
(
For Jupyter notebook users, see
hello_world_jupyter.ipynb
)
Handoffs example
from
agents
import
Agent
,
Runner
import
asyncio
spanish_agent
=
Agent
(
name
=
"Spanish agent"
,
instructions
=
"You only speak Spanish."
,
)
english_agent
=
Agent
(
name
=
"English agent"
,
instructions
=
"You only speak English"
,
)
triage_agent
=
Agent
(
name
=
"Triage agent"
,
instructions
=
"Handoff to the appropriate agent based on the language of the request."
,
handoffs
=
[
spanish_agent
,
english_agent
],
)
async
def
main
():
result
=
await
Runner
.
run
(
triage_agent
,
input
=
"Hola, ¿cómo estás?"
)
print
(
result
.
final_output
)
# ¡Hola! Estoy bien, gracias por preguntar. ¿Y tú, cómo estás?
if
__name__
==
"__main__"
:
asyncio
.
run
(
main
())
Functions example
import
asyncio
from
agents
import
Agent
,
Runner
,
function_tool
@
function_tool
def
get_weather
(
city
:
str
)
->
str
:
return
f"The weather in
{
city
}
is sunny."
agent
=
Agent
(
name
=
"Hello world"
,
instructions
=
"You are a helpful agent."
,
tools
=
[
get_weather
],
)
async
def
main
():
result
=
await
Runner
.
run
(
agent
,
input
=
"What's the weather in Tokyo?"
)
print
(
result
.
final_output
)
# The weather in Tokyo is sunny.
if
__name__
==
"__main__"
:
asyncio
.
run
(
main
())
The agent loop
When you call
Runner.run()
, we run a loop until we get a final output.
We call the LLM, using the model and settings on the agent, and the message history.
The LLM returns a response, which may include tool calls.
If the response has a final output (see below for more on this), we return it and end the loop.
If the response has a handoff, we set the agent to the new agent and go back to step 1.
We process the tool calls (if any) and append the tool responses messages. Then we go to step 1.
There is a
max_turns
parameter that you can use to limit the number of times the loop executes.
Final output
Final output is the last thing the agent produces in the loop.
If you set an
output_type
on the agent, the final output is when the LLM returns something of that type. We use
structured outputs
for this.
If there's no
output_type
(i.e. plain text responses), then the first LLM response without any tool calls or handoffs is considered as the final output.
As a result, the mental model for the agent loop is:
If the current agent has an
output_type
, the loop runs until the agent produces structured output matching that type.
If the current agent does not have an
output_type
, the loop runs until the current agent produces a message without any tool calls/handoffs.
Common agent patterns
The Agents SDK is designed to be highly flexible, allowing you to model a wide range of LLM workflows including deterministic flows, iterative loops, and more. See examples in
examples/agent_patterns
.
Tracing
The Agents SDK automatically traces your agent runs, making it easy to track and debug the behavior of your agents. Tracing is extensible by design, supporting custom spans and a wide variety of external destinations, including
Logfire
,
AgentOps
,
Braintrust
,
Scorecard
, and
Keywords AI
. For more details about how to customize or disable tracing, see
Tracing
, which also includes a larger list of
external tracing processors
.
Long running agents & human-in-the-loop
You can use the Agents SDK
Temporal
integration to run durable, long-running workflows, including human-in-the-loop tasks. View a demo of Temporal and the Agents SDK working in action to complete long-running tasks
in this video
, and
view docs here
.
Sessions
The Agents SDK provides built-in session memory to automatically maintain conversation history across multiple agent runs, eliminating the need to manually handle
.to_input_list()
between turns.
Quick start
from
agents
import
Agent
,
Runner
,
SQLiteSession
# Create agent
agent
=
Agent
(
name
=
"Assistant"
,
instructions
=
"Reply very concisely."
,
)
# Create a session instance
session
=
SQLiteSession
(
"conversation_123"
)
# First turn
result
=
await
Runner
.
run
(
agent
,
"What city is the Golden Gate Bridge in?"
,
session
=
session
)
print
(
result
.
final_output
)
# "San Francisco"
# Second turn - agent automatically remembers previous context
result
=
await
Runner
.
run
(
agent
,
"What state is it in?"
,
session
=
session
)
print
(
result
.
final_output
)
# "California"
# Also works with synchronous runner
result
=
Runner
.
run_sync
(
agent
,
"What's the population?"
,
session
=
session
)
print
(
result
.
final_output
)
# "Approximately 39 million"
Session options
No memory
(default): No session memory when session parameter is omitted
session: Session = DatabaseSession(...)
: Use a Session instance to manage conversation history
from
agents
import
Agent
,
Runner
,
SQLiteSession
# SQLite - file-based or in-memory database
session
=
SQLiteSession
(
"user_123"
,
"conversations.db"
)
# Redis - for scalable, distributed deployments
# from agents.extensions.memory import RedisSession
# session = RedisSession.from_url("user_123", url="redis://localhost:6379/0")
agent
=
Agent
(
name
=
"Assistant"
)
# Different session IDs maintain separate conversation histories
result1
=
await
Runner
.
run
(
agent
,
"Hello"
,
session
=
session
)
result2
=
await
Runner
.
run
(
agent
,
"Hello"
,
session
=
SQLiteSession
(
"user_456"
,
"conversations.db"
)
)
Custom session implementations
You can implement your own session memory by creating a class that follows the
Session
protocol:
from
agents
.
memory
import
Session
from
typing
import
List
class
MyCustomSession
:
"""Custom session implementation following the Session protocol."""
def
__init__
(
self
,
session_id
:
str
):
self
.
session_id
=
session_id
# Your initialization here
async
def
get_items
(
self
,
limit
:
int
|
None
=
None
)
->
List
[
dict
]:
# Retrieve conversation history for the session
pass
async
def
add_items
(
self
,
items
:
List
[
dict
])
->
None
:
# Store new items for the session
pass
async
def
pop_item
(
self
)
->
dict
|
None
:
# Remove and return the most recent item from the session
pass
async
def
clear_session
(
self
)
->
None
:
# Clear all items for the session
pass
# Use your custom session
agent
=
Agent
(
name
=
"Assistant"
)
result
=
await
Runner
.
run
(
agent
,
"Hello"
,
session
=
MyCustomSession
(
"my_session"
)
)
Development (only needed if you need to edit the SDK/examples)
Ensure you have
uv
installed.
uv --version
Install dependencies
make sync
(After making changes) lint/test
make check # run tests linter and typechecker
Or to run them individually:
make tests  # run tests
make mypy   # run typechecker
make lint   # run linter
make format-check # run style checker
Acknowledgements
We'd like to acknowledge the excellent work of the open-source community, especially:
Pydantic
(data validation) and
PydanticAI
(advanced agent framework)
LiteLLM
(unified interface for 100+ LLMs)
MkDocs
Griffe
uv
and
ruff
We're committed to continuing to build the Agents SDK as an open source framework so others in the community can expand on our approach.
- 今日の獲得スター数: 116
- 累積スター数: 16,004

### References
- https://github.com/openai/openai-agents-python

## openemr/openemr

### Executive Summary
- The most popular open source electronic health records and medical practice management solution.
- ---
- OpenEMR
OpenEMR
is a Free and Open Source electronic health records and medical practice management application. It features fully integrated electronic health records, practice management, scheduling, electronic billing, internationalization, free support, a vibrant community, and a whole lot more. It runs on Windows, Linux, Mac OS X, and many other platforms.
Contributing
OpenEMR is a leader in healthcare open source software and comprises a large and diverse community of software developers, medical providers and educators with a very healthy mix of both volunteers and professionals.
Join us and learn how to start contributing today!
Already comfortable with git? Check out
CONTRIBUTING.md
for quick setup instructions and requirements for contributing to OpenEMR by resolving a bug or adding an awesome feature 😊.
Support
Community and Professional support can be found
here
.
Extensive documentation and forums can be found on the
OpenEMR website
that can help you to become more familiar about the project 📖.
Reporting Issues and Bugs
Report these on the
Issue Tracker
. If you are unsure if it is an issue/bug, then always feel free to use the
Forum
and
Chat
to discuss about the issue 🪲.
Reporting Security Vulnerabilities
Check out
SECURITY.md
API
Check out
API_README.md
Docker
Check out
DOCKER_README.md
FHIR
Check out
FHIR_README.md
For Developers
If using OpenEMR directly from the code repository, then the following commands will build OpenEMR (Node.js version 22.* is required) :
composer install --no-dev
npm install
npm run build
composer dump-autoload -o
Contributors
This project exists thanks to all the people who have contributed.
[Contribute]
.
Sponsors
Thanks to our
ONC Certification Major Sponsors
!
License
GNU GPL
- 今日の獲得スター数: 115
- 累積スター数: 4,282

### References
- https://github.com/openemr/openemr

## DioxusLabs/dioxus

### Executive Summary
- Fullstack app framework for web, desktop, and mobile.
- ---
- Website
|
Examples
|
Guide
|
中文
|
PT-BR
|
日本語
|
Türkçe
|
한국어
✨ Dioxus 0.7 is in alpha - test it out! ✨
Build for web, desktop, and mobile, and more with a single codebase. Zero-config setup, integrated hot-reloading, and signals-based state management. Add backend functionality with Server Functions and bundle with our CLI.
fn
app
(
)
->
Element
{
let
mut
count =
use_signal
(
||
0
)
;
rsx
!
{
h1
{
"High-Five counter: {count}"
}
button
{
onclick
:
move |_| count +=
1
,
"Up high!"
}
button
{
onclick
:
move |_| count -=
1
,
"Down low!"
}
}
}
⭐️ Unique features:
Cross-platform apps in three lines of code (web, desktop, mobile, server, and more)
Ergonomic state management
combines the best of React, Solid, and Svelte
Built-in featureful, type-safe, fullstack web framework
Integrated bundler for deploying to the web, macOS, Linux, and Windows
Subsecond Rust hot-patching and asset hot-reloading
And more!
Take a tour of Dioxus
.
Instant hot-reloading
With one command,
dx serve
and your app is running. Edit your markup, styles, and see changes in milliseconds. Use our experimental
dx serve --hotpatch
to update Rust code in real time.
Build Beautiful Apps
Dioxus apps are styled with HTML and CSS. Use the built-in TailwindCSS support or load your favorite CSS library. Easily call into native code (objective-c, JNI, Web-Sys) for a perfect native touch.
Truly fullstack applications
Dioxus deeply integrates with
axum
to provide powerful fullstack capabilities for both clients and servers. Pick from a wide array of built-in batteries like WebSockets, SSE, Streaming, File Upload/Download, Server-Side-Rendering, Forms, Middleware, and Hot-Reload, or go fully custom and integrate your existing axum backend.
Experimental Native Renderer
Render using web-sys, webview, server-side-rendering, liveview, or even with our experimental WGPU-based renderer. Embed Dioxus in Bevy, WGPU, or even run on embedded Linux!
First-party primitive components
Get started quickly with a complete set of primitives modeled after shadcn/ui and Radix-Primitives.
First-class Android and iOS support
Dioxus is the fastest way to build native mobile apps with Rust. Simply run
dx serve --platform android
and your app is running in an emulator or on device in seconds. Call directly into JNI and Native APIs.
Bundle for web, desktop, and mobile
Simply run
dx bundle
and your app will be built and bundled with maximization optimizations. On the web, take advantage of
.avif
generation,
.wasm
compression, minification
, and more. Build WebApps weighing
less than 50kb
and desktop/mobile apps less than 5mb.
Fantastic documentation
We've put a ton of effort into building clean, readable, and comprehensive documentation. All html elements and listeners are documented with MDN docs, and our Docs runs continuous integration with Dioxus itself to ensure that the docs are always up to date. Check out the
Dioxus website
for guides, references, recipes, and more. Fun fact: we use the Dioxus website as a testbed for new Dioxus features -
check it out!
Modular and Customizable
Build your own renderer, or use a community renderer like
Freya
. Use our modular components like RSX, VirtualDom, Blitz, Taffy, and Subsecond.
Community
Dioxus is a community-driven project, with a very active
Discord
and
GitHub
community. We're always looking for help, and we're happy to answer questions and help you get started.
Our SDK
is community-run and we even have a
GitHub organization
for the best Dioxus crates that receive free upgrades and support.
Full-time core team
Dioxus has grown from a side project to a small team of fulltime engineers. Thanks to the generous support of FutureWei, Satellite.im, the GitHub Accelerator program, we're able to work on Dioxus full-time. Our long term goal is for Dioxus to become self-sustaining by providing paid high-quality enterprise tools. If your company is interested in adopting Dioxus and would like to work with us, please reach out!
Supported Platforms
Web
Render directly to the DOM using WebAssembly
Pre-render with SSR and rehydrate on the client
Simple "hello world" at about 50kb, comparable to React
Built-in dev server and hot reloading for quick iteration
Desktop
Render using Webview or - experimentally - with WGPU or
Freya
(Skia)
Zero-config setup. Simply `cargo run` or `dx serve` to build your app
Full support for native system access without IPC
Supports macOS, Linux, and Windows. Portable <3mb binaries
Mobile
Render using Webview or - experimentally - with WGPU or Skia
Build .ipa and .apk files for iOS and Android
Call directly into Java and Objective-C with minimal overhead
From "hello world" to running on device in seconds
Server-side Rendering
Suspense, hydration, and server-side rendering
Quickly drop in backend functionality with server functions
Extractors, middleware, and routing integrations
Static-site generation and incremental regeneration
Running the examples
The examples in the main branch of this repository target the git version of dioxus and the CLI. If you are looking for examples that work with the latest stable release of dioxus, check out the
0.6 branch
.
The examples in the top level of this repository can be run with:
cargo run --example
<
example
>
However, we encourage you to download the dioxus-cli to test out features like hot-reloading. To install the most recent binary CLI, you can use cargo binstall.
cargo binstall dioxus-cli@0.7.0-rc.1 --force
If this CLI is out-of-date, you can install it directly from git
cargo install --git https://github.com/DioxusLabs/dioxus dioxus-cli --locked
With the CLI, you can also run examples with the web platform. You will need to disable the default desktop feature and enable the web feature with this command:
dx serve --example
<
example
>
--platform web -- --no-default-features
Contributing
Check out the website
section on contributing
.
Report issues on our
issue tracker
.
Join
the discord and ask questions!
License
This project is licensed under either the
MIT license
or the
Apache-2 License
.
Unless you explicitly state otherwise, any contribution intentionally submitted
for inclusion in Dioxus by you, shall be licensed as MIT or Apache-2, without any additional
terms or conditions.
- 今日の獲得スター数: 110
- 累積スター数: 30,962

### References
- https://github.com/DioxusLabs/dioxus

## open-webui/open-webui

### Executive Summary
- User-friendly AI Interface (Supports Ollama, OpenAI API, ...)
- ---
- Open WebUI 👋
Open WebUI is an
extensible
, feature-rich, and user-friendly self-hosted AI platform designed to operate entirely offline.
It supports various LLM runners like
Ollama
and
OpenAI-compatible APIs
, with
built-in inference engine
for RAG, making it a
powerful AI deployment solution
.
Passionate about open-source AI?
Join our team →
Tip
Looking for an
Enterprise Plan
?
–
Speak with Our Sales Team Today!
Get
enhanced capabilities
, including
custom theming and branding
,
Service Level Agreement (SLA) support
,
Long-Term Support (LTS) versions
, and
more!
For more information, be sure to check out our
Open WebUI Documentation
.
Key Features of Open WebUI ⭐
🚀
Effortless Setup
: Install seamlessly using Docker or Kubernetes (kubectl, kustomize or helm) for a hassle-free experience with support for both
:ollama
and
:cuda
tagged images.
🤝
Ollama/OpenAI API Integration
: Effortlessly integrate OpenAI-compatible APIs for versatile conversations alongside Ollama models. Customize the OpenAI API URL to link with
LMStudio, GroqCloud, Mistral, OpenRouter, and more
.
🛡️
Granular Permissions and User Groups
: By allowing administrators to create detailed user roles and permissions, we ensure a secure user environment. This granularity not only enhances security but also allows for customized user experiences, fostering a sense of ownership and responsibility amongst users.
🔄
SCIM 2.0 Support
: Enterprise-grade user and group provisioning through SCIM 2.0 protocol, enabling seamless integration with identity providers like Okta, Azure AD, and Google Workspace for automated user lifecycle management.
📱
Responsive Design
: Enjoy a seamless experience across Desktop PC, Laptop, and Mobile devices.
📱
Progressive Web App (PWA) for Mobile
: Enjoy a native app-like experience on your mobile device with our PWA, providing offline access on localhost and a seamless user interface.
✒️🔢
Full Markdown and LaTeX Support
: Elevate your LLM experience with comprehensive Markdown and LaTeX capabilities for enriched interaction.
🎤📹
Hands-Free Voice/Video Call
: Experience seamless communication with integrated hands-free voice and video call features, allowing for a more dynamic and interactive chat environment.
🛠️
Model Builder
: Easily create Ollama models via the Web UI. Create and add custom characters/agents, customize chat elements, and import models effortlessly through
Open WebUI Community
integration.
🐍
Native Python Function Calling Tool
: Enhance your LLMs with built-in code editor support in the tools workspace. Bring Your Own Function (BYOF) by simply adding your pure Python functions, enabling seamless integration with LLMs.
📚
Local RAG Integration
: Dive into the future of chat interactions with groundbreaking Retrieval Augmented Generation (RAG) support. This feature seamlessly integrates document interactions into your chat experience. You can load documents directly into the chat or add files to your document library, effortlessly accessing them using the
#
command before a query.
🔍
Web Search for RAG
: Perform web searches using providers like
SearXNG
,
Google PSE
,
Brave Search
,
serpstack
,
serper
,
Serply
,
DuckDuckGo
,
TavilySearch
,
SearchApi
and
Bing
and inject the results directly into your chat experience.
🌐
Web Browsing Capability
: Seamlessly integrate websites into your chat experience using the
#
command followed by a URL. This feature allows you to incorporate web content directly into your conversations, enhancing the richness and depth of your interactions.
🎨
Image Generation Integration
: Seamlessly incorporate image generation capabilities using options such as AUTOMATIC1111 API or ComfyUI (local), and OpenAI's DALL-E (external), enriching your chat experience with dynamic visual content.
⚙️
Many Models Conversations
: Effortlessly engage with various models simultaneously, harnessing their unique strengths for optimal responses. Enhance your experience by leveraging a diverse set of models in parallel.
🔐
Role-Based Access Control (RBAC)
: Ensure secure access with restricted permissions; only authorized individuals can access your Ollama, and exclusive model creation/pulling rights are reserved for administrators.
🌐🌍
Multilingual Support
: Experience Open WebUI in your preferred language with our internationalization (i18n) support. Join us in expanding our supported languages! We're actively seeking contributors!
🧩
Pipelines, Open WebUI Plugin Support
: Seamlessly integrate custom logic and Python libraries into Open WebUI using
Pipelines Plugin Framework
. Launch your Pipelines instance, set the OpenAI URL to the Pipelines URL, and explore endless possibilities.
Examples
include
Function Calling
, User
Rate Limiting
to control access,
Usage Monitoring
with tools like Langfuse,
Live Translation with LibreTranslate
for multilingual support,
Toxic Message Filtering
and much more.
🌟
Continuous Updates
: We are committed to improving Open WebUI with regular updates, fixes, and new features.
Want to learn more about Open WebUI's features? Check out our
Open WebUI documentation
for a comprehensive overview!
Sponsors 🙌
Emerald
Tailscale
• Connect self-hosted AI to any device with Tailscale
Warp
• The intelligent terminal for developers
We are incredibly grateful for the generous support of our sponsors. Their contributions help us to maintain and improve our project, ensuring we can continue to deliver quality work to our community. Thank you!
How to Install 🚀
Installation via Python pip 🐍
Open WebUI can be installed using pip, the Python package installer. Before proceeding, ensure you're using
Python 3.11
to avoid compatibility issues.
Install Open WebUI
:
Open your terminal and run the following command to install Open WebUI:
pip install open-webui
Running Open WebUI
:
After installation, you can start Open WebUI by executing:
open-webui serve
This will start the Open WebUI server, which you can access at
http://localhost:8080
Quick Start with Docker 🐳
Note
Please note that for certain Docker environments, additional configurations might be needed. If you encounter any connection issues, our detailed guide on
Open WebUI Documentation
is ready to assist you.
Warning
When using Docker to install Open WebUI, make sure to include the
-v open-webui:/app/backend/data
in your Docker command. This step is crucial as it ensures your database is properly mounted and prevents any loss of data.
Tip
If you wish to utilize Open WebUI with Ollama included or CUDA acceleration, we recommend utilizing our official images tagged with either
:cuda
or
:ollama
. To enable CUDA, you must install the
Nvidia CUDA container toolkit
on your Linux/WSL system.
Installation with Default Configuration
If Ollama is on your computer
, use this command:
docker run -d -p 3000:8080 --add-host=host.docker.internal:host-gateway -v open-webui:/app/backend/data --name open-webui --restart always ghcr.io/open-webui/open-webui:main
If Ollama is on a Different Server
, use this command:
To connect to Ollama on another server, change the
OLLAMA_BASE_URL
to the server's URL:
docker run -d -p 3000:8080 -e OLLAMA_BASE_URL=https://example.com -v open-webui:/app/backend/data --name open-webui --restart always ghcr.io/open-webui/open-webui:main
To run Open WebUI with Nvidia GPU support
, use this command:
docker run -d -p 3000:8080 --gpus all --add-host=host.docker.internal:host-gateway -v open-webui:/app/backend/data --name open-webui --restart always ghcr.io/open-webui/open-webui:cuda
Installation for OpenAI API Usage Only
If you're only using OpenAI API
, use this command:
docker run -d -p 3000:8080 -e OPENAI_API_KEY=your_secret_key -v open-webui:/app/backend/data --name open-webui --restart always ghcr.io/open-webui/open-webui:main
Installing Open WebUI with Bundled Ollama Support
This installation method uses a single container image that bundles Open WebUI with Ollama, allowing for a streamlined setup via a single command. Choose the appropriate command based on your hardware setup:
With GPU Support
:
Utilize GPU resources by running the following command:
docker run -d -p 3000:8080 --gpus=all -v ollama:/root/.ollama -v open-webui:/app/backend/data --name open-webui --restart always ghcr.io/open-webui/open-webui:ollama
For CPU Only
:
If you're not using a GPU, use this command instead:
docker run -d -p 3000:8080 -v ollama:/root/.ollama -v open-webui:/app/backend/data --name open-webui --restart always ghcr.io/open-webui/open-webui:ollama
Both commands facilitate a built-in, hassle-free installation of both Open WebUI and Ollama, ensuring that you can get everything up and running swiftly.
After installation, you can access Open WebUI at
http://localhost:3000
. Enjoy! 😄
Other Installation Methods
We offer various installation alternatives, including non-Docker native installation methods, Docker Compose, Kustomize, and Helm. Visit our
Open WebUI Documentation
or join our
Discord community
for comprehensive guidance.
Look at the
Local Development Guide
for instructions on setting up a local development environment.
Troubleshooting
Encountering connection issues? Our
Open WebUI Documentation
has got you covered. For further assistance and to join our vibrant community, visit the
Open WebUI Discord
.
Open WebUI: Server Connection Error
If you're experiencing connection issues, it’s often due to the WebUI docker container not being able to reach the Ollama server at 127.0.0.1:11434 (host.docker.internal:11434) inside the container . Use the
--network=host
flag in your docker command to resolve this. Note that the port changes from 3000 to 8080, resulting in the link:
http://localhost:8080
.
Example Docker Command
:
docker run -d --network=host -v open-webui:/app/backend/data -e OLLAMA_BASE_URL=http://127.0.0.1:11434 --name open-webui --restart always ghcr.io/open-webui/open-webui:main
Keeping Your Docker Installation Up-to-Date
In case you want to update your local Docker installation to the latest version, you can do it with
Watchtower
:
docker run --rm --volume /var/run/docker.sock:/var/run/docker.sock containrrr/watchtower --run-once open-webui
In the last part of the command, replace
open-webui
with your container name if it is different.
Check our Updating Guide available in our
Open WebUI Documentation
.
Using the Dev Branch 🌙
Warning
The
:dev
branch contains the latest unstable features and changes. Use it at your own risk as it may have bugs or incomplete features.
If you want to try out the latest bleeding-edge features and are okay with occasional instability, you can use the
:dev
tag like this:
docker run -d -p 3000:8080 -v open-webui:/app/backend/data --name open-webui --add-host=host.docker.internal:host-gateway --restart always ghcr.io/open-webui/open-webui:dev
Offline Mode
If you are running Open WebUI in an offline environment, you can set the
HF_HUB_OFFLINE
environment variable to
1
to prevent attempts to download models from the internet.
export
HF_HUB_OFFLINE=1
What's Next? 🌟
Discover upcoming features on our roadmap in the
Open WebUI Documentation
.
License 📜
This project contains code under multiple licenses. The current codebase includes components licensed under the Open WebUI License with an additional requirement to preserve the "Open WebUI" branding, as well as prior contributions under their respective original licenses. For a detailed record of license changes and the applicable terms for each section of the code, please refer to
LICENSE_HISTORY
. For complete and updated licensing details, please see the
LICENSE
and
LICENSE_HISTORY
files.
Support 💬
If you have any questions, suggestions, or need assistance, please open an issue or join our
Open WebUI Discord community
to connect with us! 🤝
Star History
Created by
Timothy Jaeryang Baek
- Let's make Open WebUI even more amazing together! 💪
- 今日の獲得スター数: 106
- 累積スター数: 111,984

### References
- https://github.com/open-webui/open-webui

## 78/xiaozhi-esp32

### Executive Summary
- An MCP-based chatbot | 一个基于MCP的聊天机器人
- ---
- An MCP-based Chatbot
（中文 |
English
|
日本語
）
介绍
👉
人类：给 AI 装摄像头 vs AI：当场发现主人三天没洗头【bilibili】
👉
手工打造你的 AI 女友，新手入门教程【bilibili】
小智 AI 聊天机器人作为一个语音交互入口，利用 Qwen / DeepSeek 等大模型的 AI 能力，通过 MCP 协议实现多端控制。
版本说明
当前 v2 版本与 v1 版本分区表不兼容，所以无法从 v1 版本通过 OTA 升级到 v2 版本。分区表说明参见
partitions/v2/README.md
。
使用 v1 版本的所有硬件，可以通过手动烧录固件来升级到 v2 版本。
v1 的稳定版本为 1.9.2，可以通过
git checkout v1
来切换到 v1 版本，该分支会持续维护到 2026 年 2 月。
已实现功能
Wi-Fi / ML307 Cat.1 4G
离线语音唤醒
ESP-SR
支持两种通信协议（
Websocket
或 MQTT+UDP）
采用 OPUS 音频编解码
基于流式 ASR + LLM + TTS 架构的语音交互
声纹识别，识别当前说话人的身份
3D Speaker
OLED / LCD 显示屏，支持表情显示
电量显示与电源管理
支持多语言（中文、英文、日文）
支持 ESP32-C3、ESP32-S3、ESP32-P4 芯片平台
通过设备端 MCP 实现设备控制（音量、灯光、电机、GPIO 等）
通过云端 MCP 扩展大模型能力（智能家居控制、PC桌面操作、知识搜索、邮件收发等）
自定义唤醒词、字体、表情与聊天背景，支持网页端在线修改 (
自定义Assets生成器
)
硬件
面包板手工制作实践
详见飞书文档教程：
👉
《小智 AI 聊天机器人百科全书》
面包板效果图如下：
支持 70 多个开源硬件（仅展示部分）
立创·实战派 ESP32-S3 开发板
乐鑫 ESP32-S3-BOX3
M5Stack CoreS3
M5Stack AtomS3R + Echo Base
神奇按钮 2.4
微雪电子 ESP32-S3-Touch-AMOLED-1.8
LILYGO T-Circle-S3
虾哥 Mini C3
璀璨·AI 吊坠
无名科技 Nologo-星智-1.54TFT
SenseCAP Watcher
ESP-HI 超低成本机器狗
软件
固件烧录
新手第一次操作建议先不要搭建开发环境，直接使用免开发环境烧录的固件。
固件默认接入
xiaozhi.me
官方服务器，个人用户注册账号可以免费使用 Qwen 实时模型。
👉
新手烧录固件教程
开发环境
Cursor 或 VSCode
安装 ESP-IDF 插件，选择 SDK 版本 5.4 或以上
Linux 比 Windows 更好，编译速度快，也免去驱动问题的困扰
本项目使用 Google C++ 代码风格，提交代码时请确保符合规范
开发者文档
自定义开发板指南
- 学习如何为小智 AI 创建自定义开发板
MCP 协议物联网控制用法说明
- 了解如何通过 MCP 协议控制物联网设备
MCP 协议交互流程
- 设备端 MCP 协议的实现方式
MQTT + UDP 混合通信协议文档
一份详细的 WebSocket 通信协议文档
大模型配置
如果你已经拥有一个小智 AI 聊天机器人设备，并且已接入官方服务器，可以登录
xiaozhi.me
控制台进行配置。
👉
后台操作视频教程（旧版界面）
相关开源项目
在个人电脑上部署服务器，可以参考以下第三方开源的项目：
xinnan-tech/xiaozhi-esp32-server
Python 服务器
joey-zhou/xiaozhi-esp32-server-java
Java 服务器
AnimeAIChat/xiaozhi-server-go
Golang 服务器
使用小智通信协议的第三方客户端项目：
huangjunsen0406/py-xiaozhi
Python 客户端
TOM88812/xiaozhi-android-client
Android 客户端
100askTeam/xiaozhi-linux
百问科技提供的 Linux 客户端
78/xiaozhi-sf32
思澈科技的蓝牙芯片固件
QuecPython/solution-xiaozhiAI
移远提供的 QuecPython 固件
关于项目
这是一个由虾哥开源的 ESP32 项目，以 MIT 许可证发布，允许任何人免费使用，修改或用于商业用途。
我们希望通过这个项目，能够帮助大家了解 AI 硬件开发，将当下飞速发展的大语言模型应用到实际的硬件设备中。
如果你有任何想法或建议，请随时提出 Issues 或加入 QQ 群：1011329060
Star History
- 今日の獲得スター数: 102
- 累積スター数: 19,237

### References
- https://github.com/78/xiaozhi-esp32

## FlowiseAI/Flowise

### Executive Summary
- Build AI Agents, Visually
- ---
- English |
繁體中文
|
简体中文
|
日本語
|
한국어
Build AI Agents, Visually
📚 Table of Contents
⚡ Quick Start
🐳 Docker
👨‍💻 Developers
🌱 Env Variables
📖 Documentation
🌐 Self Host
☁️ Flowise Cloud
🙋 Support
🙌 Contributing
📄 License
⚡Quick Start
Download and Install
NodeJS
>= 18.15.0
Install Flowise
npm install -g flowise
Start Flowise
npx flowise start
Open
http://localhost:3000
🐳 Docker
Docker Compose
Clone the Flowise project
Go to
docker
folder at the root of the project
Copy
.env.example
file, paste it into the same location, and rename to
.env
file
docker compose up -d
Open
http://localhost:3000
You can bring the containers down by
docker compose stop
Docker Image
Build the image locally:
docker build --no-cache -t flowise
.
Run image:
docker run -d --name flowise -p 3000:3000 flowise
Stop image:
docker stop flowise
👨‍💻 Developers
Flowise has 3 different modules in a single mono repository.
server
: Node backend to serve API logics
ui
: React frontend
components
: Third-party nodes integrations
api-documentation
: Auto-generated swagger-ui API docs from express
Prerequisite
Install
PNPM
npm i -g pnpm
Setup
Clone the repository:
git clone https://github.com/FlowiseAI/Flowise.git
Go into repository folder:
cd
Flowise
Install all dependencies of all modules:
pnpm install
Build all the code:
pnpm build
Exit code 134 (JavaScript heap out of memory)
If you get this error when running the above `build` script, try increasing the Node.js heap size and run the script again:
#
macOS / Linux / Git Bash
export
NODE_OPTIONS=
"
--max-old-space-size=4096
"
#
Windows PowerShell
$env
:NODE_OPTIONS=
"
--max-old-space-size=4096
"
#
Windows CMD
set
NODE_OPTIONS=--max-old-space-size=4096
Then run:
pnpm build
Start the app:
pnpm start
You can now access the app on
http://localhost:3000
For development build:
Create
.env
file and specify the
VITE_PORT
(refer to
.env.example
) in
packages/ui
Create
.env
file and specify the
PORT
(refer to
.env.example
) in
packages/server
Run:
pnpm dev
Any code changes will reload the app automatically on
http://localhost:8080
🌱 Env Variables
Flowise supports different environment variables to configure your instance. You can specify the following variables in the
.env
file inside
packages/server
folder. Read
more
📖 Documentation
You can view the Flowise Docs
here
🌐 Self Host
Deploy Flowise self-hosted in your existing infrastructure, we support various
deployments
AWS
Azure
Digital Ocean
GCP
Alibaba Cloud
Others
Railway
Render
HuggingFace Spaces
Elestio
Sealos
RepoCloud
☁️ Flowise Cloud
Get Started with
Flowise Cloud
.
🙋 Support
Feel free to ask any questions, raise problems, and request new features in
Discussion
.
🙌 Contributing
Thanks go to these awesome contributors
See
Contributing Guide
. Reach out to us at
Discord
if you have any questions or issues.
📄 License
Source code in this repository is made available under the
Apache License Version 2.0
.
- 今日の獲得スター数: 98
- 累積スター数: 45,125

### References
- https://github.com/FlowiseAI/Flowise

## PixelGuys/Cubyz

### Executive Summary
- Voxel sandbox game with a large render distance, procedurally generated content and some cool graphical effects.
- ---
- Cubyz
Cubyz is a 3D voxel sandbox game (inspired by Minecraft).
Cubyz has a bunch of interesting/unique features such as:
Level of Detail (→ This enables far view distances.)
3D Chunks (→ There is no height or depth limit.)
Procedural Crafting (→ You can craft anything you want, and the game will figure out what kind of tool you tried to make.)
About
Cubyz is written in
Zig
, a rather small language with some cool features and a focus on readability.
Windows and Linux are supported. Mac is not supported, as it does not have OpenGL 4.3.
Check out the
Discord server
for more information and announcements.
There are also some devlogs on
YouTube
.
History
Until recently (the Zig rewrite was started in August 2022) Cubyz was written in Java. You can still see the code in the
Cubyz-Java
repository and play it using the
Java Launcher
.
// TODO: Move this over to a separate repository
Originally Cubyz was created on August 22, 2018 by
zenith391
and
ZaUserA
. Back then, it was called "Cubz".
However, both of them lost interest at some point, and now Cubyz is maintained by
IntegratedQuantum
.
Run Cubyz
This section is about compiling a dev version, if you just want a precompiled version, go to
releases
The Easy Way (no tools needed)
Download the latest
source code
Extract the zip file
Go into the extraced folder and double click the
run_linux.sh
or
run_windows.bat
depending on your operating system.
Congratulations: You just compiled your first program!
It doesn't work?
If it doesn't work and keeps running for more than 10 minutes without doing anything it can help to kill and restart the process. A few people seem to experience this, and I have not found the cause. It might also help to delete the
zig-cache
folder.
If you see an error message in the terminal, please report it in the
Issues
tab or on the
Discord server
.
Otherwise you can always ask for help on the Discord server. If you are unable to get it compiling on your machine, you can also ask on the Discord server and we may compile a release for you.
Note for Linux Users:
I also had to install a few
-dev
packages for the compilation to work:
sudo apt install libgl-dev libasound2-dev libx11-dev libxcursor-dev libxrandr-dev libxinerama-dev libxext-dev libxi-dev
The Better Way
Install Git
Clone this repository
git clone https://github.com/pixelguys/Cubyz
Run
run_linux.sh
or
run_windows.bat
, if you already have Zig installed on your computer (it must be a compatible version) you can also just use
zig build run
When you want to update your local version you can use
git pull
. This keeps everything in one place, avoiding repeatedly downloading the compiler on every update.
Contributing
Code
Check out the
Contributing Guidelines
Gameplay Additions
Check out the
Game Design Principles
Textures
If you want to add new textures, make sure they fit the style of the game. It's recommended that you have baseline skills in pixel art before attempting to make textures. A great collection of tutorials can be found
here
If any of the following points are ignored, your texture will be rejected:
Resolution is 16 x 16
Lighting direction is top-left for items and blocks.
Keep colour palettes small. Do not use near-duplicate colours, do not use noise, filters, or brushes that create unnecessary amounts of colours. Most blocks can be textured with ~4-6 colours.
Reference other block textures to see how colours & contrast is used. Test your textures ingame alongside other blocks.
Blocks should tile smoothly. Avoid creating seams or repetitive patterns.
Use hue shifting conservatively. Take the material into account when choosing colours.
Items have full, coloured, 1-pixel outlines. It should be shaded so that the side in light (top left) is brighter, while the side in shadow (bottom right) is darker.
Items should have higher contrast than their block counterparts.
Your texture may be edited or replaced to ensure a consistent art style throughout the game.
For further information, ask
careeoki
on
Discord
. She has made a majority of the art for Cubyz.
- 今日の獲得スター数: 89
- 累積スター数: 1,150

### References
- https://github.com/PixelGuys/Cubyz

## chen08209/FlClash

### Executive Summary
- A multi-platform proxy client based on ClashMeta,simple and easy to use, open-source and ad-free.
- ---
- 简体中文
FlClash
A multi-platform proxy client based on ClashMeta, simple and easy to use, open-source and ad-free.
on Desktop:
on Mobile:
Features
✈️
Multi-platform: Android, Windows, macOS and Linux
💻 Adaptive multiple screen sizes, Multiple color themes available
💡 Based on Material You Design,
Surfboard
-like UI
☁️ Supports data sync via WebDAV
✨ Support subscription link, Dark mode
Use
Linux
⚠️
Make sure to install the following dependencies before using them
sudo apt-get install libayatana-appindicator3-dev
 sudo apt-get install libkeybinder-3.0-dev
Android
Support the following actions
com.follow.clash.action.START
 
 com.follow.clash.action.STOP
 
 com.follow.clash.action.TOGGLE
Download
Build
Update submodules
git submodule update --init --recursive
Install
Flutter
and
Golang
environment
Build Application
android
Install
Android SDK
,
Android NDK
Set
ANDROID_NDK
environment variables
Run Build script
dart .
\s
etup.dart android
windows
You need a windows client
Install
Gcc
，
Inno Setup
Run build script
dart .
\s
etup.dart windows --arch
<
arm64
|
amd
64>
linux
You need a linux client
Run build script
dart .
\s
etup.dart linux --arch
<
arm64
|
amd
64>
macOS
You need a macOS client
Run build script
dart .
\s
etup.dart macos --arch
<
arm64
|
amd
64>
Star
The easiest way to support developers is to click on the star (⭐) at the top of the page.
- 今日の獲得スター数: 72
- 累積スター数: 22,984

### References
- https://github.com/chen08209/FlClash

## WECENG/ticket-purchase

### Executive Summary
- 大麦自动抢票，支持人员、城市、日期场次、价格选择
- ---
- 大麦抢票脚本 V1.0
特征
自动无延时抢票
支持人员、城市、日期场次、价格选择
功能介绍
通过selenium打开页面进行登录，模拟用户购票流程自动购票
其流程图如下:
准备工作
1. 配置环境
1.1安装python3环境
Windows
访问Python官方网站：
https://www.python.org/downloads/windows/
下载最新的Python 3.9+版本的安装程序。
运行安装程序。
在安装程序中，确保勾选 "Add Python X.X to PATH" 选项，这将自动将Python添加到系统环境变量中，方便在命令行中使用Python。
完成安装后，你可以在命令提示符或PowerShell中输入
python3
来启动Python解释器。
macOS
你可以使用Homebrew来安装Python 3。
安装Homebrew（如果未安装）：打开终端并运行以下命令：
/bin/bash -c
"
$(
curl -fsSL https://raw.githubusercontent.com/Homebrew/install/HEAD/install.sh
)
"
安装Python 3：运行以下命令来安装Python 3：
brew install python@3
1.2 安装所需要的环境
在命令窗口输入如下指令
pip3 install selenium
1.3 下载google chrome浏览器
下载地址:
https://www.google.cn/intl/zh-CN/chrome/?brand=YTUH&gclid=Cj0KCQjwj5mpBhDJARIsAOVjBdoV_1sBwdqKGHV3rUU1vJmNKZdy5QNzbRT8F5O0-_jq1WHXurE8a7MaAkWrEALw_wcB&gclsrc=aw.ds
2. 修改配置文件
在运行程序之前，需要先修改
config.json
文件。该文件用于指定用户需要抢票的相关信息，包括演唱会的场次、观演的人员、城市、日期、价格等。文件结果如下图所示：
2.1 文件内容说明
index_url
为大麦网的地址，
无需修改
login_url
为大麦网的登录地址，
无需修改
target_url
为用户需要抢的演唱会票的目标地址，
待修改
users
为观演人的姓名，
观演人需要用户在手机大麦APP中先填写好，然后再填入该配置文件中
，
待修改
city
为城市，
如果用户需要抢的演唱会票需要选择城市，请把城市填入此处。如无需选择，则不填
date
为场次日期，
待修改，可多选
price
为票档的价格，
待修改，可多选
if_commit_order
为是否要自动提交订单，
改成 true
if_listen为是否回流监听，
改成true
2.2 示例说明
进入大麦网
https://www.damai.cn/，选择你需要抢票的演唱会。假设如下图所示：
接下来按照下图的标注对配置文件进行修改：
最终
config.json
的文件内容如下：
{
"index_url"
:
"
https://www.damai.cn/
"
,
"login_url"
:
"
https://passport.damai.cn/login?ru=https%3A%2F%2Fwww.damai.cn%2F
"
,
"target_url"
:
"
https://detail.damai.cn/item.htm?spm=a2oeg.home.card_0.ditem_1.591b23e1JQGWHg&id=740680932762
"
,
"users"
: [
"
名字1
"
,
"
名字2
"
],
"city"
:
"
广州
"
,
"date"
:
"
2023-10-28
"
,
"price"
:
"
1039
"
,
"if_listen"
:
true
,
"if_commit_order"
:
true
}
3.运行程序
运行程序开始抢票，进入命令窗口，执行如下命令：
cd
damai
python3 damai.py
大麦app抢票
大麦app抢票脚本需要依赖appium，因此需要现在安装appium server&client环境，步骤如下：
appium server
下载
先安装好node环境（具备npm）node版本号18.0.0
先下载并安装好android sdk，并配置环境变量（appium server运行需依赖android sdk)
下载appium
npm install -g appium
查看appium是否安装成功
appium -v
下载UiAutomator2驱动
npm install appium-uiautomator2-driver
​		可能会遇到如下错误：
➜  xcode git:(master) ✗ npm install appium-uiautomator2-driver

npm ERR! code 1
npm ERR! path /Users/chenweicheng/Documents/xcode/node_modules/appium-uiautomator2-driver/node_modules/appium-chromedriver
npm ERR! command failed
npm ERR! command sh -c node install-npm.js
npm ERR! [11:57:54] Error installing Chromedriver: Request failed with status code 404
npm ERR! [11:57:54] AxiosError: Request failed with status code 404
npm ERR!     at settle (/Users/chenweicheng/Documents/xcode/node_modules/appium-uiautomator2-driver/node_modules/axios/lib/core/settle.js:19:12)
npm ERR!     at IncomingMessage.handleStreamEnd (/Users/chenweicheng/Documents/xcode/node_modules/appium-uiautomator2-driver/node_modules/axios/lib/adapters/http.js:572:11)
npm ERR!     at IncomingMessage.emit (node:events:539:35)
npm ERR!     at endReadableNT (node:internal/streams/readable:1344:12)
npm ERR!     at processTicksAndRejections (node:internal/process/task_queues:82:21)
npm ERR! [11:57:54] Downloading Chromedriver can be skipped by setting the'APPIUM_SKIP_CHROMEDRIVER_INSTALL' environment variable.

npm ERR! A complete log of this run can be found in:
npm ERR!     /Users/chenweicheng/.npm/_logs/2023-10-26T03_57_35_950Z-debug-0.log
​		解决办法（添加环境变量，错误原因是没有找到chrome浏览器驱动，忽略即可）
export
APPIUM_SKIP_CHROMEDRIVER_INSTALL=true
启动
启动appium server并使用uiautomator2驱动
appium --use-plugins uiautomator2
启动成功将出现如下信息：
[Appium] Welcome to Appium v2.2.1 (REV 2176894a5be5da17a362bf3f20678641a78f4b69)
[Appium] Non-default server args:
[Appium] {
[Appium]   usePlugins: [
[Appium]     'uiautomator2'
[Appium]   ]
[Appium] }
[Appium] Attempting to load driver uiautomator2...
[Appium] Requiring driver at /Users/chenweicheng/Documents/xcode/node_modules/appium-uiautomator2-driver
[Appium] Appium REST http interface listener started on http://0.0.0.0:4723
[Appium] You can provide the following URLs in your client code to connect to this server:
[Appium] 	http://127.0.0.1:4723/ (only accessible from the same host)
[Appium] 	http://172.31.102.45:4723/
[Appium] 	http://198.18.0.1:4723/
[Appium] Available drivers:
[Appium]   - uiautomator2@2.32.3 (automationName 'UiAutomator2')
[Appium] No plugins have been installed. Use the "appium plugin" command to install the one(s) you want to use.
其中
[Appium] 	http://127.0.0.1:4723/ (only accessible from the same host) [Appium] 	http://172.31.102.45:4723/ [Appium] 	http://198.18.0.1:4723/
为appium server连接地址
appium client
先下载并安装好python3和pip3
安装
pip3 install appium-python-client
在代码中引入并使用appium
from
appium
import
webdriver
from
appium
.
options
.
common
.
base
import
AppiumOptions
device_app_info
=
AppiumOptions
()
device_app_info
.
set_capability
(
'platformName'
,
'Android'
)
device_app_info
.
set_capability
(
'platformVersion'
,
'10'
)
device_app_info
.
set_capability
(
'deviceName'
,
'YourDeviceName'
)
device_app_info
.
set_capability
(
'appPackage'
,
'cn.damai'
)
device_app_info
.
set_capability
(
'appActivity'
,
'.launcher.splash.SplashMainActivity'
)
device_app_info
.
set_capability
(
'unicodeKeyboard'
,
True
)
device_app_info
.
set_capability
(
'resetKeyboard'
,
True
)
device_app_info
.
set_capability
(
'noReset'
,
True
)
device_app_info
.
set_capability
(
'newCommandTimeout'
,
6000
)
device_app_info
.
set_capability
(
'automationName'
,
'UiAutomator2'
)
# 连接appium server，server地址查看appium启动信息
driver
=
webdriver
.
Remote
(
'http://127.0.0.1:4723'
,
options
=
device_app_info
)
启动脚本程序
cd
damai_appium
python3 damai_appium.py
- 今日の獲得スター数: 70
- 累積スター数: 4,347

### References
- https://github.com/WECENG/ticket-purchase

## zed-industries/zed

### Executive Summary
- Code at the speed of thought – Zed is a high-performance, multiplayer code editor from the creators of Atom and Tree-sitter.
- ---
- Zed
Welcome to Zed, a high-performance, multiplayer code editor from the creators of
Atom
and
Tree-sitter
.
Installation
On macOS and Linux you can
download Zed directly
or
install Zed via your local package manager
.
Other platforms are not yet available:
Windows (
tracking issue
)
Web (
tracking issue
)
Developing Zed
Building Zed for macOS
Building Zed for Linux
Building Zed for Windows
Running Collaboration Locally
Contributing
See
CONTRIBUTING.md
for ways you can contribute to Zed.
Also... we're hiring! Check out our
jobs
page for open roles.
Licensing
License information for third party dependencies must be correctly provided for CI to pass.
We use
cargo-about
to automatically comply with open source licenses. If CI is failing, check the following:
Is it showing a
no license specified
error for a crate you've created? If so, add
publish = false
under
[package]
in your crate's Cargo.toml.
Is the error
failed to satisfy license requirements
for a dependency? If so, first determine what license the project has and whether this system is sufficient to comply with this license's requirements. If you're unsure, ask a lawyer. Once you've verified that this system is acceptable add the license's SPDX identifier to the
accepted
array in
script/licenses/zed-licenses.toml
.
Is
cargo-about
unable to find the license for a dependency? If so, add a clarification field at the end of
script/licenses/zed-licenses.toml
, as specified in the
cargo-about book
.
- 今日の獲得スター数: 68
- 累積スター数: 66,897

### References
- https://github.com/zed-industries/zed

## rustdesk/rustdesk

### Executive Summary
- An open-source remote desktop application designed for self-hosting, as an alternative to TeamViewer.
- ---
- Build
•
Docker
•
Structure
•
Snapshot
[
Українська
] | [
česky
] | [
中文
] | [
Magyar
] | [
Español
] | [
فارسی
] | [
Français
] | [
Deutsch
] | [
Polski
] | [
Indonesian
] | [
Suomi
] | [
മലയാളം
] | [
日本語
] | [
Nederlands
] | [
Italiano
] | [
Русский
] | [
Português (Brasil)
] | [
Esperanto
] | [
한국어
] | [
العربي
] | [
Tiếng Việt
] | [
Dansk
] | [
Ελληνικά
] | [
Türkçe
] | [
Norsk
]
We need your help to translate this README,
RustDesk UI
and
RustDesk Doc
to your native language
Caution
Misuse Disclaimer:
The developers of RustDesk do not condone or support any unethical or illegal use of this software. Misuse, such as unauthorized access, control or invasion of privacy, is strictly against our guidelines. The authors are not responsible for any misuse of the application.
Chat with us:
Discord
|
Twitter
|
Reddit
|
YouTube
Yet another remote desktop solution, written in Rust. Works out of the box with no configuration required. You have full control of your data, with no concerns about security. You can use our rendezvous/relay server,
set up your own
, or
write your own rendezvous/relay server
.
RustDesk welcomes contribution from everyone. See
CONTRIBUTING.md
for help getting started.
FAQ
BINARY DOWNLOAD
NIGHTLY BUILD
Dependencies
Desktop versions use Flutter or Sciter (deprecated) for GUI, this tutorial is for Sciter only, since it is easier and more friendly to start. Check out our
CI
for building Flutter version.
Please download Sciter dynamic library yourself.
Windows
|
Linux
|
macOS
Raw Steps to build
Prepare your Rust development env and C++ build env
Install
vcpkg
, and set
VCPKG_ROOT
env variable correctly
Windows: vcpkg install libvpx:x64-windows-static libyuv:x64-windows-static opus:x64-windows-static aom:x64-windows-static
Linux/macOS: vcpkg install libvpx libyuv opus aom
run
cargo run
Build
How to Build on Linux
Ubuntu 18 (Debian 10)
sudo apt install -y zip g++ gcc git curl wget nasm yasm libgtk-3-dev clang libxcb-randr0-dev libxdo-dev \
        libxfixes-dev libxcb-shape0-dev libxcb-xfixes0-dev libasound2-dev libpulse-dev cmake make \
        libclang-dev ninja-build libgstreamer1.0-dev libgstreamer-plugins-base1.0-dev libpam0g-dev
openSUSE Tumbleweed
sudo zypper install gcc-c++ git curl wget nasm yasm gcc gtk3-devel clang libxcb-devel libXfixes-devel cmake alsa-lib-devel gstreamer-devel gstreamer-plugins-base-devel xdotool-devel pam-devel
Fedora 28 (CentOS 8)
sudo yum -y install gcc-c++ git curl wget nasm yasm gcc gtk3-devel clang libxcb-devel libxdo-devel libXfixes-devel pulseaudio-libs-devel cmake alsa-lib-devel gstreamer1-devel gstreamer1-plugins-base-devel pam-devel
Arch (Manjaro)
sudo pacman -Syu --needed unzip git cmake gcc curl wget yasm nasm zip make pkg-config clang gtk3 xdotool libxcb libxfixes alsa-lib pipewire
Install vcpkg
git clone https://github.com/microsoft/vcpkg
cd
vcpkg
git checkout 2023.04.15
cd
..
vcpkg/bootstrap-vcpkg.sh
export
VCPKG_ROOT=
$HOME
/vcpkg
vcpkg/vcpkg install libvpx libyuv opus aom
Fix libvpx (For Fedora)
cd
vcpkg/buildtrees/libvpx/src
cd
*
./configure
sed -i
'
s/CFLAGS+=-I/CFLAGS+=-fPIC -I/g
'
Makefile
sed -i
'
s/CXXFLAGS+=-I/CXXFLAGS+=-fPIC -I/g
'
Makefile
make
cp libvpx.a
$HOME
/vcpkg/installed/x64-linux/lib/
cd
Build
curl --proto
'
=https
'
--tlsv1.2 -sSf https://sh.rustup.rs
|
sh
source
$HOME
/.cargo/env
git clone --recurse-submodules https://github.com/rustdesk/rustdesk
cd
rustdesk
mkdir -p target/debug
wget https://raw.githubusercontent.com/c-smile/sciter-sdk/master/bin.lnx/x64/libsciter-gtk.so
mv libsciter-gtk.so target/debug
VCPKG_ROOT=
$HOME
/vcpkg cargo run
How to build with Docker
Begin by cloning the repository and building the Docker container:
git clone https://github.com/rustdesk/rustdesk
cd
rustdesk
git submodule update --init --recursive
docker build -t
"
rustdesk-builder
"
.
Then, each time you need to build the application, run the following command:
docker run --rm -it -v
$PWD
:/home/user/rustdesk -v rustdesk-git-cache:/home/user/.cargo/git -v rustdesk-registry-cache:/home/user/.cargo/registry -e PUID=
"
$(
id -u
)
"
-e PGID=
"
$(
id -g
)
"
rustdesk-builder
Note that the first build may take longer before dependencies are cached, subsequent builds will be faster. Additionally, if you need to specify different arguments to the build command, you may do so at the end of the command in the
<OPTIONAL-ARGS>
position. For instance, if you wanted to build an optimized release version, you would run the command above followed by
--release
. The resulting executable will be available in the target folder on your system, and can be run with:
target/debug/rustdesk
Or, if you're running a release executable:
target/release/rustdesk
Please ensure that you run these commands from the root of the RustDesk repository, or the application may not find the required resources. Also note that other cargo subcommands such as
install
or
run
are not currently supported via this method as they would install or run the program inside the container instead of the host.
File Structure
libs/hbb_common
: video codec, config, tcp/udp wrapper, protobuf, fs functions for file transfer, and some other utility functions
libs/scrap
: screen capture
libs/enigo
: platform specific keyboard/mouse control
libs/clipboard
: file copy and paste implementation for Windows, Linux, macOS.
src/ui
: obsolete Sciter UI (deprecated)
src/server
: audio/clipboard/input/video services, and network connections
src/client.rs
: start a peer connection
src/rendezvous_mediator.rs
: Communicate with
rustdesk-server
, wait for remote direct (TCP hole punching) or relayed connection
src/platform
: platform specific code
flutter
: Flutter code for desktop and mobile
flutter/web/js
: JavaScript for Flutter web client
Screenshots
- 今日の獲得スター数: 67
- 累積スター数: 99,567

### References
- https://github.com/rustdesk/rustdesk

## samber/lo

### Executive Summary
- 💥 A Lodash-style Go library based on Go 1.18+ Generics (map, filter, contains, find...)
- ---
- lo - Iterate over slices, maps, channels...
✨
samber/lo
is a Lodash-style Go library based on Go 1.18+ Generics.
A utility library based on Go 1.18+ generics that makes it easier to work with slices, maps, strings, channels, and functions. It provides dozens of handy methods to simplify common coding tasks and improve code readability. It may look like
Lodash
in some aspects.
5 to 10 helpers may overlap with those from the Go standard library, in packages
slices
and
maps
. I feel this library is legitimate and offers many more valuable abstractions.
See also:
samber/do
: A dependency injection toolkit based on Go 1.18+ Generics
samber/mo
: Monads based on Go 1.18+ Generics (Option, Result, Either...)
💖 Support This Project
I’m going all-in on open-source for the coming months.
Help sustain development: Become an
individual sponsor
or join as a
corporate sponsor
.
Why this name?
I wanted a
short name
, similar to "Lodash", and no Go package uses this name.
🚀 Install
go get github.com/samber/lo@v1
This library is v1 and follows SemVer strictly.
No breaking changes will be made to exported APIs before v2.0.0.
This library has no dependencies outside the Go standard library.
💡 Usage
You can import
lo
using:
import
(
"github.com/samber/lo"
lop
"github.com/samber/lo/parallel"
lom
"github.com/samber/lo/mutable"
loi
"github.com/samber/lo/it"
)
Then use one of the helpers below:
names
:=
lo
.
Uniq
([]
string
{
"Samuel"
,
"John"
,
"Samuel"
})
// []string{"Samuel", "John"}
Tips for lazy developers
I cannot recommend it, but in case you are too lazy for repeating
lo.
everywhere, you can import the entire library into the namespace.
import
(
    .
"github.com/samber/lo"
)
I take no responsibility for this junk. 😁 💩
🤠 Spec
GoDoc:
godoc.org/github.com/samber/lo
Documentation:
lo.samber.dev
Supported helpers for slices:
Filter
Map
UniqMap
FilterMap
FlatMap
Reduce
ReduceRight
ForEach
ForEachWhile
Times
Uniq
UniqBy
GroupBy
GroupByMap
Chunk
PartitionBy
Flatten
Interleave
Shuffle
Reverse
Fill
Repeat
RepeatBy
KeyBy
SliceToMap / Associate
FilterSliceToMap
Keyify
Drop
DropRight
DropWhile
DropRightWhile
DropByIndex
Reject
RejectMap
FilterReject
Count
CountBy
CountValues
CountValuesBy
Subset
Slice
Replace
ReplaceAll
Compact
IsSorted
IsSortedByKey
Splice
Cut
CutPrefix
CutSuffix
Trim
TrimLeft
TrimPrefix
TrimRight
TrimSuffix
Supported helpers for maps:
Keys
UniqKeys
HasKey
ValueOr
Values
UniqValues
PickBy
PickByKeys
PickByValues
OmitBy
OmitByKeys
OmitByValues
Entries / ToPairs
FromEntries / FromPairs
Invert
Assign (merge of maps)
ChunkEntries
MapKeys
MapValues
MapEntries
MapToSlice
FilterMapToSlice
FilterKeys
FilterValues
Supported math helpers:
Range / RangeFrom / RangeWithSteps
Clamp
Sum
SumBy
Product
ProductBy
Mean
MeanBy
Mode
Supported helpers for strings:
RandomString
Substring
ChunkString
RuneLength
PascalCase
CamelCase
KebabCase
SnakeCase
Words
Capitalize
Ellipsis
Supported helpers for tuples:
T2 -> T9
Unpack2 -> Unpack9
Zip2 -> Zip9
ZipBy2 -> ZipBy9
Unzip2 -> Unzip9
UnzipBy2 -> UnzipBy9
CrossJoin2 -> CrossJoin2
CrossJoinBy2 -> CrossJoinBy2
Supported helpers for time and duration:
Duration
Duration0 -> Duration10
Supported helpers for channels:
ChannelDispatcher
SliceToChannel
ChannelToSlice
Generator
Buffer
BufferWithContext
BufferWithTimeout
FanIn
FanOut
Supported intersection helpers:
Contains
ContainsBy
Every
EveryBy
Some
SomeBy
None
NoneBy
Intersect
Difference
Union
Without
WithoutBy
WithoutEmpty
WithoutNth
ElementsMatch
ElementsMatchBy
Supported search helpers:
IndexOf
LastIndexOf
HasPrefix
HasSuffix
Find
FindIndexOf
FindLastIndexOf
FindOrElse
FindKey
FindKeyBy
FindUniques
FindUniquesBy
FindDuplicates
FindDuplicatesBy
Min
MinIndex
MinBy
MinIndexBy
Earliest
EarliestBy
Max
MaxIndex
MaxBy
MaxIndexBy
Latest
LatestBy
First
FirstOrEmpty
FirstOr
Last
LastOrEmpty
LastOr
Nth
NthOr
NthOrEmpty
Sample
SampleBy
Samples
SamplesBy
Conditional helpers:
Ternary
TernaryF
If / ElseIf / Else
Switch / Case / Default
Type manipulation helpers:
IsNil
IsNotNil
ToPtr
Nil
EmptyableToPtr
FromPtr
FromPtrOr
ToSlicePtr
FromSlicePtr
FromSlicePtrOr
ToAnySlice
FromAnySlice
Empty
IsEmpty
IsNotEmpty
Coalesce
CoalesceOrEmpty
CoalesceSlice
CoalesceSliceOrEmpty
CoalesceMap
CoalesceMapOrEmpty
Function helpers:
Partial
Partial2 -> Partial5
Concurrency helpers:
Attempt
AttemptWhile
AttemptWithDelay
AttemptWhileWithDelay
Debounce
DebounceBy
Throttle
ThrottleWithCount
ThrottleBy
ThrottleByWithCount
Synchronize
Async
Async{0->6}
Transaction
WaitFor
WaitForWithContext
Error handling:
Validate
Must
Try
Try1 -> Try6
TryOr
TryOr1 -> TryOr6
TryCatch
TryWithErrorValue
TryCatchWithErrorValue
ErrorsAs
Assert
Assertf
Constraints:
Clonable
Filter
Iterates over a collection and returns a slice of all the elements the predicate function returns
true
for.
even
:=
lo
.
Filter
([]
int
{
1
,
2
,
3
,
4
},
func
(
x
int
,
index
int
)
bool
{
return
x
%
2
==
0
})
// []int{2, 4}
[
play
]
Mutable: like
lo.Filter()
, but the slice is updated in place.
import
lom
"github.com/samber/lo/mutable"
list
:=
[]
int
{
1
,
2
,
3
,
4
}
newList
:=
lom
.
Filter
(
list
,
func
(
x
int
)
bool
{
return
x
%
2
==
0
})
list
// []int{2, 4, 3, 4}
newList
// []int{2, 4}
Map
Manipulates a slice of one type and transforms it into a slice of another type:
import
"github.com/samber/lo"
lo
.
Map
([]
int64
{
1
,
2
,
3
,
4
},
func
(
x
int64
,
index
int
)
string
{
return
strconv
.
FormatInt
(
x
,
10
)
})
// []string{"1", "2", "3", "4"}
[
play
]
Parallel processing: like
lo.Map()
, but the mapper function is called in a goroutine. Results are returned in the same order.
import
lop
"github.com/samber/lo/parallel"
lop
.
Map
([]
int64
{
1
,
2
,
3
,
4
},
func
(
x
int64
,
_
int
)
string
{
return
strconv
.
FormatInt
(
x
,
10
)
})
// []string{"1", "2", "3", "4"}
[
play
]
Mutable: like
lo.Map()
, but the slice is updated in place.
import
lom
"github.com/samber/lo/mutable"
list
:=
[]
int
{
1
,
2
,
3
,
4
}
lom
.
Map
(
list
,
func
(
x
int
)
int
{
return
x
*
2
})
// []int{2, 4, 6, 8}
[
play
]
UniqMap
Manipulates a slice and transforms it to a slice of another type with unique values.
type
User
struct
{
Name
string
Age
int
}
users
:=
[]
User
{{
Name
:
"Alex"
,
Age
:
10
}, {
Name
:
"Alex"
,
Age
:
12
}, {
Name
:
"Bob"
,
Age
:
11
}, {
Name
:
"Alice"
,
Age
:
20
}}
names
:=
lo
.
UniqMap
(
users
,
func
(
u
User
,
index
int
)
string
{
return
u
.
Name
})
// []string{"Alex", "Bob", "Alice"}
[
play
]
FilterMap
Returns a slice obtained after both filtering and mapping using the given callback function.
The callback function should return two values: the result of the mapping operation and whether the result element should be included or not.
matching
:=
lo
.
FilterMap
([]
string
{
"cpu"
,
"gpu"
,
"mouse"
,
"keyboard"
},
func
(
x
string
,
_
int
) (
string
,
bool
) {
if
strings
.
HasSuffix
(
x
,
"pu"
) {
return
"xpu"
,
true
}
return
""
,
false
})
// []string{"xpu", "xpu"}
[
play
]
FlatMap
Manipulates a slice and transforms and flattens it to a slice of another type. The transform function can either return a slice or a
nil
, and in the
nil
case no value is added to the final slice.
lo
.
FlatMap
([]
int64
{
0
,
1
,
2
},
func
(
x
int64
,
_
int
) []
string
{
return
[]
string
{
strconv
.
FormatInt
(
x
,
10
),
strconv
.
FormatInt
(
x
,
10
),
    }
})
// []string{"0", "0", "1", "1", "2", "2"}
[
play
]
Reduce
Reduces a collection to a single value. The value is calculated by accumulating the result of running each element in the collection through an accumulator function. Each successive invocation is supplied with the return value returned by the previous call.
sum
:=
lo
.
Reduce
([]
int
{
1
,
2
,
3
,
4
},
func
(
agg
int
,
item
int
,
_
int
)
int
{
return
agg
+
item
},
0
)
// 10
[
play
]
ReduceRight
Like
lo.Reduce
except that it iterates over elements of collection from right to left.
result
:=
lo
.
ReduceRight
([][]
int
{{
0
,
1
}, {
2
,
3
}, {
4
,
5
}},
func
(
agg
[]
int
,
item
[]
int
,
_
int
) []
int
{
return
append
(
agg
,
item
...
)
}, []
int
{})
// []int{4, 5, 2, 3, 0, 1}
[
play
]
ForEach
Iterates over elements of a collection and invokes the function over each element.
import
"github.com/samber/lo"
lo
.
ForEach
([]
string
{
"hello"
,
"world"
},
func
(
x
string
,
_
int
) {
println
(
x
)
})
// prints "hello\nworld\n"
[
play
]
Parallel processing: like
lo.ForEach()
, but the callback is called as a goroutine.
import
lop
"github.com/samber/lo/parallel"
lop
.
ForEach
([]
string
{
"hello"
,
"world"
},
func
(
x
string
,
_
int
) {
println
(
x
)
})
// prints "hello\nworld\n" or "world\nhello\n"
ForEachWhile
Iterates over collection elements and invokes iteratee for each element collection return value decide to continue or break, like do while().
list
:=
[]
int64
{
1
,
2
,
-
42
,
4
}
lo
.
ForEachWhile
(
list
,
func
(
x
int64
,
_
int
)
bool
{
if
x
<
0
{
return
false
}
fmt
.
Println
(
x
)
return
true
})
// 1
// 2
[
play
]
Times
Times invokes the iteratee n times, returning a slice of the results of each invocation. The iteratee is invoked with index as argument.
import
"github.com/samber/lo"
lo
.
Times
(
3
,
func
(
i
int
)
string
{
return
strconv
.
FormatInt
(
int64
(
i
),
10
)
})
// []string{"0", "1", "2"}
[
play
]
Parallel processing: like
lo.Times()
, but callback is called in goroutine.
import
lop
"github.com/samber/lo/parallel"
lop
.
Times
(
3
,
func
(
i
int
)
string
{
return
strconv
.
FormatInt
(
int64
(
i
),
10
)
})
// []string{"0", "1", "2"}
Uniq
Returns a duplicate-free version of a slice, in which only the first occurrence of each element is kept. The order of result values is determined by the order they occur in the slice.
uniqValues
:=
lo
.
Uniq
([]
int
{
1
,
2
,
2
,
1
})
// []int{1, 2}
[
play
]
UniqBy
Returns a duplicate-free version of a slice, in which only the first occurrence of each element is kept. The order of result values is determined by the order they occur in the slice. It accepts
iteratee
which is invoked for each element in the slice to generate the criterion by which uniqueness is computed.
uniqValues
:=
lo
.
UniqBy
([]
int
{
0
,
1
,
2
,
3
,
4
,
5
},
func
(
i
int
)
int
{
return
i
%
3
})
// []int{0, 1, 2}
[
play
]
GroupBy
Returns an object composed of keys generated from the results of running each element of collection through iteratee.
import
lo
"github.com/samber/lo"
groups
:=
lo
.
GroupBy
([]
int
{
0
,
1
,
2
,
3
,
4
,
5
},
func
(
i
int
)
int
{
return
i
%
3
})
// map[int][]int{0: []int{0, 3}, 1: []int{1, 4}, 2: []int{2, 5}}
[
play
]
Parallel processing: like
lo.GroupBy()
, but callback is called in goroutine.
import
lop
"github.com/samber/lo/parallel"
lop
.
GroupBy
([]
int
{
0
,
1
,
2
,
3
,
4
,
5
},
func
(
i
int
)
int
{
return
i
%
3
})
// map[int][]int{0: []int{0, 3}, 1: []int{1, 4}, 2: []int{2, 5}}
GroupByMap
Returns an object composed of keys generated from the results of running each element of collection through iteratee.
import
lo
"github.com/samber/lo"
groups
:=
lo
.
GroupByMap
([]
int
{
0
,
1
,
2
,
3
,
4
,
5
},
func
(
i
int
) (
int
,
int
) {
return
i
%
3
,
i
*
2
})
// map[int][]int{0: []int{0, 6}, 1: []int{2, 8}, 2: []int{4, 10}}
[
play
]
Chunk
Returns a slice of elements split into groups of length size. If the slice can't be split evenly, the final chunk will be the remaining elements.
lo
.
Chunk
([]
int
{
0
,
1
,
2
,
3
,
4
,
5
},
2
)
// [][]int{{0, 1}, {2, 3}, {4, 5}}
lo
.
Chunk
([]
int
{
0
,
1
,
2
,
3
,
4
,
5
,
6
},
2
)
// [][]int{{0, 1}, {2, 3}, {4, 5}, {6}}
lo
.
Chunk
([]
int
{},
2
)
// [][]int{}
lo
.
Chunk
([]
int
{
0
},
2
)
// [][]int{{0}}
[
play
]
PartitionBy
Returns a slice of elements split into groups. The order of grouped values is determined by the order they occur in collection. The grouping is generated from the results of running each element of collection through iteratee.
import
lo
"github.com/samber/lo"
partitions
:=
lo
.
PartitionBy
([]
int
{
-
2
,
-
1
,
0
,
1
,
2
,
3
,
4
,
5
},
func
(
x
int
)
string
{
if
x
<
0
{
return
"negative"
}
else
if
x
%
2
==
0
{
return
"even"
}
return
"odd"
})
// [][]int{{-2, -1}, {0, 2, 4}, {1, 3, 5}}
[
play
]
Parallel processing: like
lo.PartitionBy()
, but callback is called in goroutine. Results are returned in the same order.
import
lop
"github.com/samber/lo/parallel"
partitions
:=
lop
.
PartitionBy
([]
int
{
-
2
,
-
1
,
0
,
1
,
2
,
3
,
4
,
5
},
func
(
x
int
)
string
{
if
x
<
0
{
return
"negative"
}
else
if
x
%
2
==
0
{
return
"even"
}
return
"odd"
})
// [][]int{{-2, -1}, {0, 2, 4}, {1, 3, 5}}
Flatten
Returns a slice a single level deep.
flat
:=
lo
.
Flatten
([][]
int
{{
0
,
1
}, {
2
,
3
,
4
,
5
}})
// []int{0, 1, 2, 3, 4, 5}
[
play
]
Interleave
Round-robin alternating input slices and sequentially appending value at index into result.
interleaved
:=
lo
.
Interleave
([]
int
{
1
,
4
,
7
}, []
int
{
2
,
5
,
8
}, []
int
{
3
,
6
,
9
})
// []int{1, 2, 3, 4, 5, 6, 7, 8, 9}
interleaved
:=
lo
.
Interleave
([]
int
{
1
}, []
int
{
2
,
5
,
8
}, []
int
{
3
,
6
}, []
int
{
4
,
7
,
9
,
10
})
// []int{1, 2, 3, 4, 5, 6, 7, 8, 9, 10}
[
play
]
Shuffle
Returns a slice of shuffled values. Uses the Fisher-Yates shuffle algorithm.
⚠️
This helper is
mutable
.
import
lom
"github.com/samber/lo/mutable"
list
:=
[]
int
{
0
,
1
,
2
,
3
,
4
,
5
}
lom
.
Shuffle
(
list
)
list
// []int{1, 4, 0, 3, 5, 2}
[
play
]
Reverse
Reverses a slice so that the first element becomes the last, the second element becomes the second to last, and so on.
⚠️
This helper is
mutable
.
import
lom
"github.com/samber/lo/mutable"
list
:=
[]
int
{
0
,
1
,
2
,
3
,
4
,
5
}
lom
.
Reverse
(
list
)
list
// []int{5, 4, 3, 2, 1, 0}
[
play
]
Fill
Fills elements of a slice with
initial
value.
type
foo
struct
{
bar
string
}
func
(
f
foo
)
Clone
()
foo
{
return
foo
{
f
.
bar
}
}
initializedSlice
:=
lo
.
Fill
([]
foo
{
foo
{
"a"
},
foo
{
"a"
}},
foo
{
"b"
})
// []foo{foo{"b"}, foo{"b"}}
[
play
]
Repeat
Builds a slice with N copies of initial value.
type
foo
struct
{
bar
string
}
func
(
f
foo
)
Clone
()
foo
{
return
foo
{
f
.
bar
}
}
slice
:=
lo
.
Repeat
(
2
,
foo
{
"a"
})
// []foo{foo{"a"}, foo{"a"}}
[
play
]
RepeatBy
Builds a slice with values returned by N calls of callback.
slice
:=
lo
.
RepeatBy
(
0
,
func
(
i
int
)
string
{
return
strconv
.
FormatInt
(
int64
(
math
.
Pow
(
float64
(
i
),
2
)),
10
)
})
// []string{}
slice
:=
lo
.
RepeatBy
(
5
,
func
(
i
int
)
string
{
return
strconv
.
FormatInt
(
int64
(
math
.
Pow
(
float64
(
i
),
2
)),
10
)
})
// []string{"0", "1", "4", "9", "16"}
[
play
]
KeyBy
Transforms a slice or a slice of structs to a map based on a pivot callback.
m
:=
lo
.
KeyBy
([]
string
{
"a"
,
"aa"
,
"aaa"
},
func
(
str
string
)
int
{
return
len
(
str
)
})
// map[int]string{1: "a", 2: "aa", 3: "aaa"}
type
Character
struct
{
dir
string
code
int
}
characters
:=
[]
Character
{
    {
dir
:
"left"
,
code
:
97
},
    {
dir
:
"right"
,
code
:
100
},
}
result
:=
lo
.
KeyBy
(
characters
,
func
(
char
Character
)
string
{
return
string
(
rune
(
char
.
code
))
})
//map[a:{dir:left code:97} d:{dir:right code:100}]
[
play
]
SliceToMap (alias: Associate)
Returns a map containing key-value pairs provided by transform function applied to elements of the given slice.
If any of two pairs have the same key the last one gets added to the map.
The order of keys in returned map is not specified and is not guaranteed to be the same from the original slice.
in
:=
[]
*
foo
{{
baz
:
"apple"
,
bar
:
1
}, {
baz
:
"banana"
,
bar
:
2
}}
aMap
:=
lo
.
SliceToMap
(
in
,
func
(
f
*
foo
) (
string
,
int
) {
return
f
.
baz
,
f
.
bar
})
// map[string][int]{ "apple":1, "banana":2 }
[
play
]
FilterSliceToMap
Returns a map containing key-value pairs provided by transform function applied to elements of the given slice.
If any of two pairs have the same key the last one gets added to the map.
The order of keys in returned map is not specified and is not guaranteed to be the same from the original slice.
The third return value of the transform function is a boolean that indicates whether the key-value pair should be included in the map.
list
:=
[]
string
{
"a"
,
"aa"
,
"aaa"
}
result
:=
lo
.
FilterSliceToMap
(
list
,
func
(
str
string
) (
string
,
int
,
bool
) {
return
str
,
len
(
str
),
len
(
str
)
>
1
})
// map[string][int]{"aa":2 "aaa":3}
[
play
]
Keyify
Returns a map with each unique element of the slice as a key.
set
:=
lo
.
Keyify
([]
int
{
1
,
1
,
2
,
3
,
4
})
// map[int]struct{}{1:{}, 2:{}, 3:{}, 4:{}}
[
play
]
Drop
Drops n elements from the beginning of a slice.
l
:=
lo
.
Drop
([]
int
{
0
,
1
,
2
,
3
,
4
,
5
},
2
)
// []int{2, 3, 4, 5}
[
play
]
DropRight
Drops n elements from the end of a slice.
l
:=
lo
.
DropRight
([]
int
{
0
,
1
,
2
,
3
,
4
,
5
},
2
)
// []int{0, 1, 2, 3}
[
play
]
DropWhile
Drop elements from the beginning of a slice while the predicate returns true.
l
:=
lo
.
DropWhile
([]
string
{
"a"
,
"aa"
,
"aaa"
,
"aa"
,
"aa"
},
func
(
val
string
)
bool
{
return
len
(
val
)
<=
2
})
// []string{"aaa", "aa", "aa"}
[
play
]
DropRightWhile
Drop elements from the end of a slice while the predicate returns true.
l
:=
lo
.
DropRightWhile
([]
string
{
"a"
,
"aa"
,
"aaa"
,
"aa"
,
"aa"
},
func
(
val
string
)
bool
{
return
len
(
val
)
<=
2
})
// []string{"a", "aa", "aaa"}
[
play
]
DropByIndex
Drops elements from a slice by the index. A negative index will drop elements from the end of the slice.
l
:=
lo
.
DropByIndex
([]
int
{
0
,
1
,
2
,
3
,
4
,
5
},
2
,
4
,
-
1
)
// []int{0, 1, 3}
[
play
]
Reject
The opposite of Filter, this method returns the elements of collection that predicate does not return true for.
odd
:=
lo
.
Reject
([]
int
{
1
,
2
,
3
,
4
},
func
(
x
int
,
_
int
)
bool
{
return
x
%
2
==
0
})
// []int{1, 3}
[
play
]
RejectMap
The opposite of FilterMap, this method returns a slice obtained after both filtering and mapping using the given callback function.
The callback function should return two values:
the result of the mapping operation and
whether the result element should be included or not.
items
:=
lo
.
RejectMap
([]
int
{
1
,
2
,
3
,
4
},
func
(
x
int
,
_
int
) (
int
,
bool
) {
return
x
*
10
,
x
%
2
==
0
})
// []int{10, 30}
FilterReject
Mixes Filter and Reject, this method returns two slices, one for the elements of collection that predicate returns true for and one for the elements that predicate does not return true for.
kept
,
rejected
:=
lo
.
FilterReject
([]
int
{
1
,
2
,
3
,
4
},
func
(
x
int
,
_
int
)
bool
{
return
x
%
2
==
0
})
// []int{2, 4}
// []int{1, 3}
Count
Counts the number of elements in the collection that equal value.
count
:=
lo
.
Count
([]
int
{
1
,
5
,
1
},
1
)
// 2
[
play
]
CountBy
Counts the number of elements in the collection for which predicate is true.
count
:=
lo
.
CountBy
([]
int
{
1
,
5
,
1
},
func
(
i
int
)
bool
{
return
i
<
4
})
// 2
[
play
]
CountValues
Counts the number of each element in the collection.
lo
.
CountValues
([]
int
{})
// map[int]int{}
lo
.
CountValues
([]
int
{
1
,
2
})
// map[int]int{1: 1, 2: 1}
lo
.
CountValues
([]
int
{
1
,
2
,
2
})
// map[int]int{1: 1, 2: 2}
lo
.
CountValues
([]
string
{
"foo"
,
"bar"
,
""
})
// map[string]int{"": 1, "foo": 1, "bar": 1}
lo
.
CountValues
([]
string
{
"foo"
,
"bar"
,
"bar"
})
// map[string]int{"foo": 1, "bar": 2}
[
play
]
CountValuesBy
Counts the number of each element in the collection. It is equivalent to chaining lo.Map and lo.CountValues.
isEven
:=
func
(
v
int
)
bool
{
return
v
%
2
==
0
}
lo
.
CountValuesBy
([]
int
{},
isEven
)
// map[bool]int{}
lo
.
CountValuesBy
([]
int
{
1
,
2
},
isEven
)
// map[bool]int{false: 1, true: 1}
lo
.
CountValuesBy
([]
int
{
1
,
2
,
2
},
isEven
)
// map[bool]int{false: 1, true: 2}
length
:=
func
(
v
string
)
int
{
return
len
(
v
)
}
lo
.
CountValuesBy
([]
string
{
"foo"
,
"bar"
,
""
},
length
)
// map[int]int{0: 1, 3: 2}
lo
.
CountValuesBy
([]
string
{
"foo"
,
"bar"
,
"bar"
},
length
)
// map[int]int{3: 3}
[
play
]
Subset
Returns a copy of a slice from
offset
up to
length
elements. Like
slice[start:start+length]
, but does not panic on overflow.
in
:=
[]
int
{
0
,
1
,
2
,
3
,
4
}
sub
:=
lo
.
Subset
(
in
,
2
,
3
)
// []int{2, 3, 4}
sub
:=
lo
.
Subset
(
in
,
-
4
,
3
)
// []int{1, 2, 3}
sub
:=
lo
.
Subset
(
in
,
-
2
,
math
.
MaxUint
)
// []int{3, 4}
[
play
]
Slice
Returns a copy of a slice from
start
up to, but not including
end
. Like
slice[start:end]
, but does not panic on overflow.
in
:=
[]
int
{
0
,
1
,
2
,
3
,
4
}
slice
:=
lo
.
Slice
(
in
,
0
,
5
)
// []int{0, 1, 2, 3, 4}
slice
:=
lo
.
Slice
(
in
,
2
,
3
)
// []int{2}
slice
:=
lo
.
Slice
(
in
,
2
,
6
)
// []int{2, 3, 4}
slice
:=
lo
.
Slice
(
in
,
4
,
3
)
// []int{}
[
play
]
Replace
Returns a copy of the slice with the first n non-overlapping instances of old replaced by new.
in
:=
[]
int
{
0
,
1
,
0
,
1
,
2
,
3
,
0
}
slice
:=
lo
.
Replace
(
in
,
0
,
42
,
1
)
// []int{42, 1, 0, 1, 2, 3, 0}
slice
:=
lo
.
Replace
(
in
,
-
1
,
42
,
1
)
// []int{0, 1, 0, 1, 2, 3, 0}
slice
:=
lo
.
Replace
(
in
,
0
,
42
,
2
)
// []int{42, 1, 42, 1, 2, 3, 0}
slice
:=
lo
.
Replace
(
in
,
0
,
42
,
-
1
)
// []int{42, 1, 42, 1, 2, 3, 42}
[
play
]
ReplaceAll
Returns a copy of the slice with all non-overlapping instances of old replaced by new.
in
:=
[]
int
{
0
,
1
,
0
,
1
,
2
,
3
,
0
}
slice
:=
lo
.
ReplaceAll
(
in
,
0
,
42
)
// []int{42, 1, 42, 1, 2, 3, 42}
slice
:=
lo
.
ReplaceAll
(
in
,
-
1
,
42
)
// []int{0, 1, 0, 1, 2, 3, 0}
[
play
]
Compact
Returns a slice of all non-zero elements.
in
:=
[]
string
{
""
,
"foo"
,
""
,
"bar"
,
""
}
slice
:=
lo
.
Compact
(
in
)
// []string{"foo", "bar"}
[
play
]
IsSorted
Checks if a slice is sorted.
slice
:=
lo
.
IsSorted
([]
int
{
0
,
1
,
2
,
3
,
4
,
5
,
6
,
7
,
8
,
9
})
// true
[
play
]
IsSortedByKey
Checks if a slice is sorted by iteratee.
slice
:=
lo
.
IsSortedByKey
([]
string
{
"a"
,
"bb"
,
"ccc"
},
func
(
s
string
)
int
{
return
len
(
s
)
})
// true
[
play
]
Splice
Splice inserts multiple elements at index i. A negative index counts back from the end of the slice. The helper is protected against overflow errors.
result
:=
lo
.
Splice
([]
string
{
"a"
,
"b"
},
1
,
"1"
,
"2"
)
// []string{"a", "1", "2", "b"}
// negative
result
=
lo
.
Splice
([]
string
{
"a"
,
"b"
},
-
1
,
"1"
,
"2"
)
// []string{"a", "1", "2", "b"}
// overflow
result
=
lo
.
Splice
([]
string
{
"a"
,
"b"
},
42
,
"1"
,
"2"
)
// []string{"a", "b", "1", "2"}
[
play
]
Cut
Slices collection around the first instance of separator, returning the part of collection before and after separator. The found result reports whether separator appears in collection. If separator does not appear in s, cut returns collection, empty slice of []T, false.
actualLeft
,
actualRight
,
result
=
lo
.
Cut
([]
string
{
"a"
,
"b"
,
"c"
,
"d"
,
"e"
,
"f"
,
"g"
}, []
string
{
"b"
,
"c"
,
"d"
})
// actualLeft: []string{"a"}
// actualRight: []string{"e", "f", "g"}
// result: true
result
=
lo
.
Cut
([]
string
{
"a"
,
"b"
,
"c"
,
"d"
,
"e"
,
"f"
,
"g"
}, []
string
{
"z"
})
// actualLeft: []string{"a", "b", "c", "d", "e", "f", "g"}
// actualRight: []string{}
// result: false
result
=
lo
.
Cut
([]
string
{
"a"
,
"b"
,
"c"
,
"d"
,
"e"
,
"f"
,
"g"
}, []
string
{
"a"
,
"b"
})
// actualLeft: []string{}
// actualRight: []string{"c", "d", "e", "f", "g"}
// result: true
[
play
]
CutPrefix
Returns collection without the provided leading prefix []T and reports whether it found the prefix. If s doesn't start with prefix, CutPrefix returns collection, false. If prefix is the empty []T, CutPrefix returns collection, true.
actualRight
,
result
=
lo
.
CutPrefix
([]
string
{
"a"
,
"b"
,
"c"
,
"d"
,
"e"
,
"f"
,
"g"
}, []
string
{
"a"
,
"b"
,
"c"
})
// actualRight: []string{"d", "e", "f", "g"}
// result: true
result
=
lo
.
CutPrefix
([]
string
{
"a"
,
"b"
,
"c"
,
"d"
,
"e"
,
"f"
,
"g"
}, []
string
{
"b"
})
// actualRight: []string{"a", "b", "c", "d", "e", "f", "g"}
// result: false
result
=
lo
.
CutPrefix
([]
string
{
"a"
,
"b"
,
"c"
,
"d"
,
"e"
,
"f"
,
"g"
}, []
string
{})
// actualRight: []string{"a", "b", "c", "d", "e", "f", "g"}
// result: true
[
play
]
CutSuffix
Returns collection without the provided ending suffix []T and reports whether it found the suffix. If it doesn't end with suffix, CutSuffix returns collection, false. If suffix is the empty []T, CutSuffix returns collection, true.
actualLeft
,
result
=
lo
.
CutSuffix
([]
string
{
"a"
,
"b"
,
"c"
,
"d"
,
"e"
,
"f"
,
"g"
}, []
string
{
"f"
,
"g"
})
// actualLeft: []string{"a", "b", "c", "d", "e"}
// result: true
actualLeft
,
result
=
lo
.
CutSuffix
([]
string
{
"a"
,
"b"
,
"c"
,
"d"
,
"e"
,
"f"
,
"g"
}, []
string
{
"b"
})
// actualLeft: []string{"a", "b", "c", "d", "e", "f", "g"}
// result: false
actualLeft
,
result
=
lo
.
CutSuffix
([]
string
{
"a"
,
"b"
,
"c"
,
"d"
,
"e"
,
"f"
,
"g"
}, []
string
{})
// actualLeft: []string{"a", "b", "c", "d", "e", "f", "g"}
// result: true
[
play
]
Trim
Removes all the leading and trailing cutset from the collection.
result
:=
lo
.
Trim
([]
int
{
0
,
1
,
2
,
0
,
3
,
0
}, []
int
{
1
,
0
})
// []int{2, 0, 3}
result
:=
lo
.
Trim
([]
string
{
"hello"
,
"world"
,
" "
}, []
string
{
" "
,
""
})
// []string{"hello", "world"}
[
play
]
TrimLeft
Removes all the leading cutset from the collection.
result
:=
lo
.
TrimLeft
([]
int
{
0
,
1
,
2
,
0
,
3
,
0
}, []
int
{
1
,
0
})
// []int{2, 0, 3, 0}
result
:=
lo
.
TrimLeft
([]
string
{
"hello"
,
"world"
,
" "
}, []
string
{
" "
,
""
})
// []string{"hello", "world", " "}
[
play
]
TrimPrefix
Removes all the leading prefix from the collection.
result
:=
lo
.
TrimPrefix
([]
int
{
1
,
2
,
1
,
2
,
3
,
1
,
2
,
4
}, []
int
{
1
,
2
})
// []int{3, 1, 2, 4}
result
:=
lo
.
TrimPrefix
([]
string
{
"hello"
,
"world"
,
"hello"
,
"test"
}, []
string
{
"hello"
})
// []string{"world", "hello", "test"}
[
play
]
TrimRight
Removes all the trailing cutset from the collection.
result
:=
lo
.
TrimRight
([]
int
{
0
,
1
,
2
,
0
,
3
,
0
}, []
int
{
0
,
3
})
// []int{0, 1, 2}
result
:=
lo
.
TrimRight
([]
string
{
"hello"
,
"world"
,
"  "
}, []
string
{
" "
,
""
})
// []string{"hello", "world", ""}
[
play
]
TrimSuffix
Removes all the trailing suffix from the collection.
result
:=
lo
.
TrimSuffix
([]
int
{
1
,
2
,
3
,
1
,
2
,
4
,
2
,
4
,
2
,
4
}, []
int
{
2
,
4
})
// []int{1, 2, 3, 1}
result
:=
lo
.
TrimSuffix
([]
string
{
"hello"
,
"world"
,
"hello"
,
"test"
}, []
string
{
"test"
})
// []string{"hello", "world", "hello"}
[
play
]
Keys
Creates a slice of the map keys.
Use the UniqKeys variant to deduplicate common keys.
keys
:=
lo
.
Keys
(
map
[
string
]
int
{
"foo"
:
1
,
"bar"
:
2
})
// []string{"foo", "bar"}
keys
:=
lo
.
Keys
(
map
[
string
]
int
{
"foo"
:
1
,
"bar"
:
2
},
map
[
string
]
int
{
"baz"
:
3
})
// []string{"foo", "bar", "baz"}
keys
:=
lo
.
Keys
(
map
[
string
]
int
{
"foo"
:
1
,
"bar"
:
2
},
map
[
string
]
int
{
"bar"
:
3
})
// []string{"foo", "bar", "bar"}
[
play
]
UniqKeys
Creates a slice of unique map keys.
keys
:=
lo
.
UniqKeys
(
map
[
string
]
int
{
"foo"
:
1
,
"bar"
:
2
},
map
[
string
]
int
{
"baz"
:
3
})
// []string{"foo", "bar", "baz"}
keys
:=
lo
.
UniqKeys
(
map
[
string
]
int
{
"foo"
:
1
,
"bar"
:
2
},
map
[
string
]
int
{
"bar"
:
3
})
// []string{"foo", "bar"}
[
play
]
HasKey
Returns whether the given key exists.
exists
:=
lo
.
HasKey
(
map
[
string
]
int
{
"foo"
:
1
,
"bar"
:
2
},
"foo"
)
// true
exists
:=
lo
.
HasKey
(
map
[
string
]
int
{
"foo"
:
1
,
"bar"
:
2
},
"baz"
)
// false
[
play
]
Values
Creates a slice of the map values.
Use the UniqValues variant to deduplicate common values.
values
:=
lo
.
Values
(
map
[
string
]
int
{
"foo"
:
1
,
"bar"
:
2
})
// []int{1, 2}
values
:=
lo
.
Values
(
map
[
string
]
int
{
"foo"
:
1
,
"bar"
:
2
},
map
[
string
]
int
{
"baz"
:
3
})
// []int{1, 2, 3}
values
:=
lo
.
Values
(
map
[
string
]
int
{
"foo"
:
1
,
"bar"
:
2
},
map
[
string
]
int
{
"bar"
:
2
})
// []int{1, 2, 2}
[
play
]
UniqValues
Creates a slice of unique map values.
values
:=
lo
.
UniqValues
(
map
[
string
]
int
{
"foo"
:
1
,
"bar"
:
2
})
// []int{1, 2}
values
:=
lo
.
UniqValues
(
map
[
string
]
int
{
"foo"
:
1
,
"bar"
:
2
},
map
[
string
]
int
{
"baz"
:
3
})
// []int{1, 2, 3}
values
:=
lo
.
UniqValues
(
map
[
string
]
int
{
"foo"
:
1
,
"bar"
:
2
},
map
[
string
]
int
{
"bar"
:
2
})
// []int{1, 2}
[
play
]
ValueOr
Returns the value of the given key or the fallback value if the key is not present.
value
:=
lo
.
ValueOr
(
map
[
string
]
int
{
"foo"
:
1
,
"bar"
:
2
},
"foo"
,
42
)
// 1
value
:=
lo
.
ValueOr
(
map
[
string
]
int
{
"foo"
:
1
,
"bar"
:
2
},
"baz"
,
42
)
// 42
[
play
]
PickBy
Returns same map type filtered by given predicate.
m
:=
lo
.
PickBy
(
map
[
string
]
int
{
"foo"
:
1
,
"bar"
:
2
,
"baz"
:
3
},
func
(
key
string
,
value
int
)
bool
{
return
value
%
2
==
1
})
// map[string]int{"foo": 1, "baz": 3}
[
play
]
PickByKeys
Returns same map type filtered by given keys.
m
:=
lo
.
PickByKeys
(
map
[
string
]
int
{
"foo"
:
1
,
"bar"
:
2
,
"baz"
:
3
}, []
string
{
"foo"
,
"baz"
})
// map[string]int{"foo": 1, "baz": 3}
[
play
]
PickByValues
Returns same map type filtered by given values.
m
:=
lo
.
PickByValues
(
map
[
string
]
int
{
"foo"
:
1
,
"bar"
:
2
,
"baz"
:
3
}, []
int
{
1
,
3
})
// map[string]int{"foo": 1, "baz": 3}
[
play
]
OmitBy
Returns same map type filtered by given predicate.
m
:=
lo
.
OmitBy
(
map
[
string
]
int
{
"foo"
:
1
,
"bar"
:
2
,
"baz"
:
3
},
func
(
key
string
,
value
int
)
bool
{
return
value
%
2
==
1
})
// map[string]int{"bar": 2}
[
play
]
OmitByKeys
Returns same map type filtered by given keys.
m
:=
lo
.
OmitByKeys
(
map
[
string
]
int
{
"foo"
:
1
,
"bar"
:
2
,
"baz"
:
3
}, []
string
{
"foo"
,
"baz"
})
// map[string]int{"bar": 2}
[
play
]
OmitByValues
Returns same map type filtered by given values.
m
:=
lo
.
OmitByValues
(
map
[
string
]
int
{
"foo"
:
1
,
"bar"
:
2
,
"baz"
:
3
}, []
int
{
1
,
3
})
// map[string]int{"bar": 2}
[
play
]
Entries (alias: ToPairs)
Transforms a map into a slice of key/value pairs.
entries
:=
lo
.
Entries
(
map
[
string
]
int
{
"foo"
:
1
,
"bar"
:
2
})
// []lo.Entry[string, int]{
//     {
//         Key: "foo",
//         Value: 1,
//     },
//     {
//         Key: "bar",
//         Value: 2,
//     },
// }
[
play
]
FromEntries (alias: FromPairs)
Transforms a slice of key/value pairs into a map.
m
:=
lo
.
FromEntries
([]lo.
Entry
[
string
,
int
]{
    {
Key
:
"foo"
,
Value
:
1
,
    },
    {
Key
:
"bar"
,
Value
:
2
,
    },
})
// map[string]int{"foo": 1, "bar": 2}
[
play
]
Invert
Creates a map composed of the inverted keys and values. If map contains duplicate values, subsequent values overwrite property assignments of previous values.
m1
:=
lo
.
Invert
(
map
[
string
]
int
{
"a"
:
1
,
"b"
:
2
})
// map[int]string{1: "a", 2: "b"}
m2
:=
lo
.
Invert
(
map
[
string
]
int
{
"a"
:
1
,
"b"
:
2
,
"c"
:
1
})
// map[int]string{1: "c", 2: "b"}
[
play
]
Assign
Merges multiple maps from left to right.
mergedMaps
:=
lo
.
Assign
(
map
[
string
]
int
{
"a"
:
1
,
"b"
:
2
},
map
[
string
]
int
{
"b"
:
3
,
"c"
:
4
},
)
// map[string]int{"a": 1, "b": 3, "c": 4}
[
play
]
ChunkEntries
Splits a map into a slice of elements in groups of length equal to its size. If the map cannot be split evenly, the final chunk will contain the remaining elements.
maps
:=
lo
.
ChunkEntries
(
map
[
string
]
int
{
"a"
:
1
,
"b"
:
2
,
"c"
:
3
,
"d"
:
4
,
"e"
:
5
,
    },
3
,
)
// []map[string]int{
//    {"a": 1, "b": 2, "c": 3},
//    {"d": 4, "e": 5},
// }
[
play
]
MapKeys
Manipulates map keys and transforms it to a map of another type.
m2
:=
lo
.
MapKeys
(
map
[
int
]
int
{
1
:
1
,
2
:
2
,
3
:
3
,
4
:
4
},
func
(
_
int
,
v
int
)
string
{
return
strconv
.
FormatInt
(
int64
(
v
),
10
)
})
// map[string]int{"1": 1, "2": 2, "3": 3, "4": 4}
[
play
]
MapValues
Manipulates map values and transforms it to a map of another type.
m1
:=
map
[
int
]
int64
{
1
:
1
,
2
:
2
,
3
:
3
}
m2
:=
lo
.
MapValues
(
m1
,
func
(
x
int64
,
_
int
)
string
{
return
strconv
.
FormatInt
(
x
,
10
)
})
// map[int]string{1: "1", 2: "2", 3: "3"}
[
play
]
MapEntries
Manipulates map entries and transforms it to a map of another type.
in
:=
map
[
string
]
int
{
"foo"
:
1
,
"bar"
:
2
}
out
:=
lo
.
MapEntries
(
in
,
func
(
k
string
,
v
int
) (
int
,
string
) {
return
v
,
k
})
// map[int]string{1: "foo", 2: "bar"}
[
play
]
MapToSlice
Transforms a map into a slice based on specified iteratee.
m
:=
map
[
int
]
int64
{
1
:
4
,
2
:
5
,
3
:
6
}
s
:=
lo
.
MapToSlice
(
m
,
func
(
k
int
,
v
int64
)
string
{
return
fmt
.
Sprintf
(
"%d_%d"
,
k
,
v
)
})
// []string{"1_4", "2_5", "3_6"}
[
play
]
FilterMapToSlice
Transforms a map into a slice based on specified iteratee. The iteratee returns a value and a boolean. If the boolean is true, the value is added to the result slice.
If the boolean is false, the value is not added to the result slice. The order of the keys in the input map is not specified and the order of the keys in the output slice is not guaranteed.
kv
:=
map
[
int
]
int64
{
1
:
1
,
2
:
2
,
3
:
3
,
4
:
4
}
result
:=
lo
.
FilterMapToSlice
(
kv
,
func
(
k
int
,
v
int64
) (
string
,
bool
) {
return
fmt
.
Sprintf
(
"%d_%d"
,
k
,
v
),
k
%
2
==
0
})
// []{"2_2", "4_4"}
FilterKeys
Transforms a map into a slice based on predicate returns true for specific elements. It is a mix of
lo.Filter()
and
lo.Keys()
.
kv
:=
map
[
int
]
string
{
1
:
"foo"
,
2
:
"bar"
,
3
:
"baz"
}
result
:=
FilterKeys
(
kv
,
func
(
k
int
,
v
string
)
bool
{
return
v
==
"foo"
})
// [1]
[
play
]
FilterValues
Transforms a map into a slice based on predicate returns true for specific elements. It is a mix of
lo.Filter()
and
lo.Values()
.
kv
:=
map
[
int
]
string
{
1
:
"foo"
,
2
:
"bar"
,
3
:
"baz"
}
result
:=
FilterValues
(
kv
,
func
(
k
int
,
v
string
)
bool
{
return
v
==
"foo"
})
// ["foo"]
[
play
]
Range / RangeFrom / RangeWithSteps
Creates a slice of numbers (positive and/or negative) progressing from start up to, but not including end.
result
:=
lo
.
Range
(
4
)
// [0, 1, 2, 3]
result
:=
lo
.
Range
(
-
4
)
// [0, -1, -2, -3]
result
:=
lo
.
RangeFrom
(
1
,
5
)
// [1, 2, 3, 4, 5]
result
:=
lo
.
RangeFrom
[
float64
](
1.0
,
5
)
// [1.0, 2.0, 3.0, 4.0, 5.0]
result
:=
lo
.
RangeWithSteps
(
0
,
20
,
5
)
// [0, 5, 10, 15]
result
:=
lo
.
RangeWithSteps
[
float32
](
-
1.0
,
-
4.0
,
-
1.0
)
// [-1.0, -2.0, -3.0]
result
:=
lo
.
RangeWithSteps
(
1
,
4
,
-
1
)
// []
result
:=
lo
.
Range
(
0
)
// []
[
play
]
Clamp
Clamps number within the inclusive lower and upper bounds.
r1
:=
lo
.
Clamp
(
0
,
-
10
,
10
)
// 0
r2
:=
lo
.
Clamp
(
-
42
,
-
10
,
10
)
// -10
r3
:=
lo
.
Clamp
(
42
,
-
10
,
10
)
// 10
[
play
]
Sum
Sums the values in a collection.
If collection is empty 0 is returned.
list
:=
[]
int
{
1
,
2
,
3
,
4
,
5
}
sum
:=
lo
.
Sum
(
list
)
// 15
[
play
]
SumBy
Summarizes the values in a collection using the given return value from the iteration function.
If collection is empty 0 is returned.
strings
:=
[]
string
{
"foo"
,
"bar"
}
sum
:=
lo
.
SumBy
(
strings
,
func
(
item
string
)
int
{
return
len
(
item
)
})
// 6
Product
Calculates the product of the values in a collection.
If collection is empty 0 is returned.
list
:=
[]
int
{
1
,
2
,
3
,
4
,
5
}
product
:=
lo
.
Product
(
list
)
// 120
[
play
]
ProductBy
Calculates the product of the values in a collection using the given return value from the iteration function.
If collection is empty 0 is returned.
strings
:=
[]
string
{
"foo"
,
"bar"
}
product
:=
lo
.
ProductBy
(
strings
,
func
(
item
string
)
int
{
return
len
(
item
)
})
// 9
[
play
]
Mean
Calculates the mean of a collection of numbers.
If collection is empty 0 is returned.
mean
:=
lo
.
Mean
([]
int
{
2
,
3
,
4
,
5
})
// 3
mean
:=
lo
.
Mean
([]
float64
{
2
,
3
,
4
,
5
})
// 3.5
mean
:=
lo
.
Mean
([]
float64
{})
// 0
MeanBy
Calculates the mean of a collection of numbers using the given return value from the iteration function.
If collection is empty 0 is returned.
list
:=
[]
string
{
"aa"
,
"bbb"
,
"cccc"
,
"ddddd"
}
mapper
:=
func
(
item
string
)
float64
{
return
float64
(
len
(
item
))
}
mean
:=
lo
.
MeanBy
(
list
,
mapper
)
// 3.5
mean
:=
lo
.
MeanBy
([]
float64
{},
mapper
)
// 0
[
play
]
Mode
Calculates the mode (most frequent value) of a collection of numbers.
If multiple values have the same highest frequency, then multiple values are returned.
If the collection is empty, the zero value of
T[]
is returned.
mode
:=
lo
.
Mode
([]
int
{
2
,
2
,
3
,
4
})
// [2]
mode
:=
lo
.
Mode
([]
float64
{
2
,
2
,
3
,
3
})
// [2, 3]
mode
:=
lo
.
Mode
([]
float64
{})
// []
mode
:=
lo
.
Mode
([]
int
{
1
,
2
,
3
,
4
,
5
,
6
,
7
,
8
,
9
})
// [1, 2, 3, 4, 5, 6, 7, 8, 9]
RandomString
Returns a random string of the specified length and made of the specified charset.
str
:=
lo
.
RandomString
(
5
,
lo
.
LettersCharset
)
// example: "eIGbt"
[
play
]
Substring
Return part of a string.
sub
:=
lo
.
Substring
(
"hello"
,
2
,
3
)
// "llo"
sub
:=
lo
.
Substring
(
"hello"
,
-
4
,
3
)
// "ell"
sub
:=
lo
.
Substring
(
"hello"
,
-
2
,
math
.
MaxUint
)
// "lo"
[
play
]
ChunkString
Returns a slice of strings split into groups of length size. If the string can't be split evenly, the final chunk will be the remaining characters.
lo
.
ChunkString
(
"123456"
,
2
)
// []string{"12", "34", "56"}
lo
.
ChunkString
(
"1234567"
,
2
)
// []string{"12", "34", "56", "7"}
lo
.
ChunkString
(
""
,
2
)
// []string{""}
lo
.
ChunkString
(
"1"
,
2
)
// []string{"1"}
[
play
]
RuneLength
An alias to utf8.RuneCountInString which returns the number of runes in string.
sub
:=
lo
.
RuneLength
(
"hellô"
)
// 5
sub
:=
len
(
"hellô"
)
// 6
[
play
]
PascalCase
Converts string to pascal case.
str
:=
lo
.
PascalCase
(
"hello_world"
)
// HelloWorld
[
play
]
CamelCase
Converts string to camel case.
str
:=
lo
.
CamelCase
(
"hello_world"
)
// helloWorld
[
play
]
KebabCase
Converts string to kebab case.
str
:=
lo
.
KebabCase
(
"helloWorld"
)
// hello-world
[
play
]
SnakeCase
Converts string to snake case.
str
:=
lo
.
SnakeCase
(
"HelloWorld"
)
// hello_world
[
play
]
Words
Splits string into a slice of its words.
str
:=
lo
.
Words
(
"helloWorld"
)
// []string{"hello", "world"}
[
play
]
Capitalize
Converts the first character of string to upper case and the remaining to lower case.
str
:=
lo
.
Capitalize
(
"heLLO"
)
// Hello
[
play
]
Ellipsis
Trims and truncates a string to a specified length in
bytes
and appends an ellipsis if truncated. If the string contains non-ASCII characters (which may occupy multiple bytes in UTF-8), truncating by byte length may split a character in the middle, potentially resulting in garbled output.
str
:=
lo
.
Ellipsis
(
"  Lorem Ipsum  "
,
5
)
// Lo...
str
:=
lo
.
Ellipsis
(
"Lorem Ipsum"
,
100
)
// Lorem Ipsum
str
:=
lo
.
Ellipsis
(
"Lorem Ipsum"
,
3
)
// ...
[
play
]
T2 -> T9
Creates a tuple from a list of values.
tuple1
:=
lo
.
T2
(
"x"
,
1
)
// Tuple2[string, int]{A: "x", B: 1}
func
example
() (
string
,
int
) {
return
"y"
,
2
}
tuple2
:=
lo
.
T2
(
example
())
// Tuple2[string, int]{A: "y", B: 2}
[
play
]
Unpack2 -> Unpack9
Returns values contained in a tuple.
r1
,
r2
:=
lo
.
Unpack2
(lo.
Tuple2
[
string
,
int
]{
"a"
,
1
})
// "a", 1
Unpack is also available as a method of TupleX.
tuple2
:=
lo
.
T2
(
"a"
,
1
)
a
,
b
:=
tuple2
.
Unpack
()
// "a", 1
[
play
]
Zip2 -> Zip9
Zip creates a slice of grouped elements, the first of which contains the first elements of the given slices, the second of which contains the second elements of the given slices, and so on.
When collections are different sizes, the Tuple attributes are filled with zero value.
tuples
:=
lo
.
Zip2
([]
string
{
"a"
,
"b"
}, []
int
{
1
,
2
})
// []Tuple2[string, int]{{A: "a", B: 1}, {A: "b", B: 2}}
[
play
]
ZipBy2 -> ZipBy9
ZipBy creates a slice of transformed elements, the first of which contains the first elements of the given slices, the second of which contains the second elements of the given slices, and so on.
When collections are different sizes, the Tuple attributes are filled with zero value.
items
:=
lo
.
ZipBy2
([]
string
{
"a"
,
"b"
}, []
int
{
1
,
2
},
func
(
a
string
,
b
int
)
string
{
return
fmt
.
Sprintf
(
"%s-%d"
,
a
,
b
)
})
// []string{"a-1", "b-2"}
Unzip2 -> Unzip9
Unzip accepts a slice of grouped elements and creates a slice regrouping the elements to their pre-zip configuration.
a
,
b
:=
lo
.
Unzip2
([]
Tuple2
[
string
,
int
]{{
A
:
"a"
,
B
:
1
}, {
A
:
"b"
,
B
:
2
}})
// []string{"a", "b"}
// []int{1, 2}
[
play
]
UnzipBy2 -> UnzipBy9
UnzipBy2 iterates over a collection and creates a slice regrouping the elements to their pre-zip configuration.
a
,
b
:=
lo
.
UnzipBy2
([]
string
{
"hello"
,
"john"
,
"doe"
},
func
(
str
string
) (
string
,
int
) {
return
str
,
len
(
str
)
})
// []string{"hello", "john", "doe"}
// []int{5, 4, 3}
CrossJoin2 -> CrossJoin9
Combines every item from one list with every item from others. It is the cartesian product of lists received as arguments. Returns an empty list if a list is empty.
result
:=
lo
.
CrossJoin2
([]
string
{
"hello"
,
"john"
,
"doe"
}, []
int
{
1
,
2
})
// lo.Tuple2{"hello", 1}
// lo.Tuple2{"hello", 2}
// lo.Tuple2{"john", 1}
// lo.Tuple2{"john", 2}
// lo.Tuple2{"doe", 1}
// lo.Tuple2{"doe", 2}
CrossJoinBy2 -> CrossJoinBy9
Combines every item from one list with every item from others. It is the cartesian product of lists received as arguments. The project function is used to create the output values. Returns an empty list if a list is empty.
result
:=
lo
.
CrossJoinBy2
([]
string
{
"hello"
,
"john"
,
"doe"
}, []
int
{
1
,
2
},
func
(
a
A
,
b
B
)
string
{
return
fmt
.
Sprintf
(
"%s - %d"
,
a
,
b
)
})
// "hello - 1"
// "hello - 2"
// "john - 1"
// "john - 2"
// "doe - 1"
// "doe - 2"
Duration
Returns the time taken to execute a function.
duration
:=
lo
.
Duration
(
func
() {
// very long job
})
// 3s
[
play
]
Duration0 -> Duration10
Returns the time taken to execute a function.
duration
:=
lo
.
Duration0
(
func
() {
// very long job
})
// 3s
err
,
duration
:=
lo
.
Duration1
(
func
()
error
{
// very long job
return
errors
.
New
(
"an error"
)
})
// an error
// 3s
str
,
nbr
,
err
,
duration
:=
lo
.
Duration3
(
func
() (
string
,
int
,
error
) {
// very long job
return
"hello"
,
42
,
nil
})
// hello
// 42
// nil
// 3s
ChannelDispatcher
Distributes messages from input channels into N child channels. Close events are propagated to children.
Underlying channels can have a fixed buffer capacity or be unbuffered when cap is 0.
ch
:=
make
(
chan
int
,
42
)
for
i
:=
0
;
i
<=
10
;
i
++
{
ch
<-
i
}
children
:=
lo
.
ChannelDispatcher
(
ch
,
5
,
10
,
DispatchingStrategyRoundRobin
[
int
])
// []<-chan int{...}
consumer
:=
func
(
c
<-
chan
int
) {
for
{
msg
,
ok
:=
<-
c
if
!
ok
{
println
(
"closed"
)
break
}
println
(
msg
)
    }
}
for
i
:=
range
children
{
go
consumer
(
children
[
i
])
}
[
play
]
Many distributions strategies are available:
lo.DispatchingStrategyRoundRobin
: Distributes messages in a rotating sequential manner.
lo.DispatchingStrategyRandom
: Distributes messages in a random manner.
lo.DispatchingStrategyWeightedRandom
: Distributes messages in a weighted manner.
lo.DispatchingStrategyFirst
: Distributes messages in the first non-full channel.
lo.DispatchingStrategyLeast
: Distributes messages in the emptiest channel.
lo.DispatchingStrategyMost
: Distributes to the fullest channel.
Some strategies bring fallback, in order to favor non-blocking behaviors. See implementations.
For custom strategies, just implement the
lo.DispatchingStrategy
prototype:
type
DispatchingStrategy
[
T
any
]
func
(
message
T
,
messageIndex
uint64
,
channels
[]
<-
chan
T
)
int
Eg:
type
Message
struct
{
TenantID
uuid.
UUID
}
func
hash
(
id
uuid.
UUID
)
int
{
h
:=
fnv
.
New32a
()
h
.
Write
([]
byte
(
id
.
String
()))
return
int
(
h
.
Sum32
())
}
// Routes messages per TenantID.
customStrategy
:=
func
(
message
string
,
messageIndex
uint64
,
channels
[]
<-
chan
string
)
int
{
destination
:=
hash
(
message
)
%
len
(
channels
)
// check if channel is full
if
len
(
channels
[
destination
])
<
cap
(
channels
[
destination
]) {
return
destination
}
// fallback when child channel is full
return
utils
.
DispatchingStrategyRoundRobin
(
message
,
uint64
(
destination
),
channels
)
}
children
:=
lo
.
ChannelDispatcher
(
ch
,
5
,
10
,
customStrategy
)
...
SliceToChannel
Returns a read-only channel of collection elements. Channel is closed after last element. Channel capacity can be customized.
list
:=
[]
int
{
1
,
2
,
3
,
4
,
5
}
for
v
:=
range
lo
.
SliceToChannel
(
2
,
list
) {
println
(
v
)
}
// prints 1, then 2, then 3, then 4, then 5
[
play
]
ChannelToSlice
Returns a slice built from channel items. Blocks until channel closes.
list
:=
[]
int
{
1
,
2
,
3
,
4
,
5
}
ch
:=
lo
.
SliceToChannel
(
2
,
list
)
items
:=
ChannelToSlice
(
ch
)
// []int{1, 2, 3, 4, 5}
Generator
Implements the generator design pattern. Channel is closed after last element. Channel capacity can be customized.
generator
:=
func
(
yield
func
(
int
)) {
yield
(
1
)
yield
(
2
)
yield
(
3
)
}
for
v
:=
range
lo
.
Generator
(
2
,
generator
) {
println
(
v
)
}
// prints 1, then 2, then 3
Buffer
Creates a slice of n elements from a channel. Returns the slice, the slice length, the read time and the channel status (opened/closed).
ch
:=
lo
.
SliceToChannel
(
2
, []
int
{
1
,
2
,
3
,
4
,
5
})
items1
,
length1
,
duration1
,
ok1
:=
lo
.
Buffer
(
ch
,
3
)
// []int{1, 2, 3}, 3, 0s, true
items2
,
length2
,
duration2
,
ok2
:=
lo
.
Buffer
(
ch
,
3
)
// []int{4, 5}, 2, 0s, false
Example: RabbitMQ consumer 👇
ch
:=
readFromQueue
()
for
{
// read 1k items
items
,
length
,
_
,
ok
:=
lo
.
Buffer
(
ch
,
1000
)
// do batching stuff
if
!
ok
{
break
}
}
BufferWithContext
Creates a slice of n elements from a channel, with timeout. Returns the slice, the slice length, the read time and the channel status (opened/closed).
ctx
,
cancel
:=
context
.
WithCancel
(
context
.
TODO
())
go
func
() {
ch
<-
0
time
.
Sleep
(
10
*
time
.
Millisecond
)
ch
<-
1
time
.
Sleep
(
10
*
time
.
Millisecond
)
ch
<-
2
time
.
Sleep
(
10
*
time
.
Millisecond
)
ch
<-
3
time
.
Sleep
(
10
*
time
.
Millisecond
)
ch
<-
4
time
.
Sleep
(
10
*
time
.
Millisecond
)
cancel
()
}()
items1
,
length1
,
duration1
,
ok1
:=
lo
.
BufferWithContext
(
ctx
,
ch
,
3
)
// []int{0, 1, 2}, 3, 20ms, true
items2
,
length2
,
duration2
,
ok2
:=
lo
.
BufferWithContext
(
ctx
,
ch
,
3
)
// []int{3, 4}, 2, 30ms, false
BufferWithTimeout
Creates a slice of n elements from a channel, with timeout. Returns the slice, the slice length, the read time and the channel status (opened/closed).
generator
:=
func
(
yield
func
(
int
)) {
for
i
:=
0
;
i
<
5
;
i
++
{
yield
(
i
)
time
.
Sleep
(
35
*
time
.
Millisecond
)
    }
}
ch
:=
lo
.
Generator
(
0
,
generator
)
items1
,
length1
,
duration1
,
ok1
:=
lo
.
BufferWithTimeout
(
ch
,
3
,
100
*
time
.
Millisecond
)
// []int{1, 2}, 2, 100ms, true
items2
,
length2
,
duration2
,
ok2
:=
lo
.
BufferWithTimeout
(
ch
,
3
,
100
*
time
.
Millisecond
)
// []int{3, 4, 5}, 3, 75ms, true
items3
,
length3
,
duration2
,
ok3
:=
lo
.
BufferWithTimeout
(
ch
,
3
,
100
*
time
.
Millisecond
)
// []int{}, 0, 10ms, false
Example: RabbitMQ consumer 👇
ch
:=
readFromQueue
()
for
{
// read 1k items
// wait up to 1 second
items
,
length
,
_
,
ok
:=
lo
.
BufferWithTimeout
(
ch
,
1000
,
1
*
time
.
Second
)
// do batching stuff
if
!
ok
{
break
}
}
Example: Multithreaded RabbitMQ consumer 👇
ch
:=
readFromQueue
()
// 5 workers
// prefetch 1k messages per worker
children
:=
lo
.
ChannelDispatcher
(
ch
,
5
,
1000
,
lo
.
DispatchingStrategyFirst
[
int
])
consumer
:=
func
(
c
<-
chan
int
) {
for
{
// read 1k items
// wait up to 1 second
items
,
length
,
_
,
ok
:=
lo
.
BufferWithTimeout
(
ch
,
1000
,
1
*
time
.
Second
)
// do batching stuff
if
!
ok
{
break
}
    }
}
for
i
:=
range
children
{
go
consumer
(
children
[
i
])
}
FanIn
Merge messages from multiple input channels into a single buffered channel. Output messages have no priority. When all upstream channels reach EOF, downstream channel closes.
stream1
:=
make
(
chan
int
,
42
)
stream2
:=
make
(
chan
int
,
42
)
stream3
:=
make
(
chan
int
,
42
)
all
:=
lo
.
FanIn
(
100
,
stream1
,
stream2
,
stream3
)
// <-chan int
FanOut
Broadcasts all the upstream messages to multiple downstream channels. When upstream channel reaches EOF, downstream channels close. If any downstream channels is full, broadcasting is paused.
stream
:=
make
(
chan
int
,
42
)
all
:=
lo
.
FanOut
(
5
,
100
,
stream
)
// [5]<-chan int
Contains
Returns true if an element is present in a collection.
present
:=
lo
.
Contains
([]
int
{
0
,
1
,
2
,
3
,
4
,
5
},
5
)
// true
[
play
]
ContainsBy
Returns true if the predicate function returns
true
.
present
:=
lo
.
ContainsBy
([]
int
{
0
,
1
,
2
,
3
,
4
,
5
},
func
(
x
int
)
bool
{
return
x
==
3
})
// true
Every
Returns true if all elements of a subset are contained in a collection or if the subset is empty.
ok
:=
lo
.
Every
([]
int
{
0
,
1
,
2
,
3
,
4
,
5
}, []
int
{
0
,
2
})
// true
ok
:=
lo
.
Every
([]
int
{
0
,
1
,
2
,
3
,
4
,
5
}, []
int
{
0
,
6
})
// false
EveryBy
Returns true if the predicate returns true for all elements in the collection or if the collection is empty.
b
:=
EveryBy
([]
int
{
1
,
2
,
3
,
4
},
func
(
x
int
)
bool
{
return
x
<
5
})
// true
[
play
]
Some
Returns true if at least 1 element of a subset is contained in a collection.
If the subset is empty Some returns false.
ok
:=
lo
.
Some
([]
int
{
0
,
1
,
2
,
3
,
4
,
5
}, []
int
{
0
,
6
})
// true
[
play
]
ok := lo.Some([]int{0, 1, 2, 3, 4, 5}, []int{-1, 6})
// false
### SomeBy

Returns true if the predicate returns true for any of the elements in the collection.
If the collection is empty SomeBy returns false.

```go
b := SomeBy([]int{1, 2, 3, 4}, func(x int) bool {
    return x < 3
})
// true
None
Returns true if no element of a subset is contained in a collection or if the subset is empty.
b
:=
None
([]
int
{
0
,
1
,
2
,
3
,
4
,
5
}, []
int
{
0
,
2
})
// false
b
:=
None
([]
int
{
0
,
1
,
2
,
3
,
4
,
5
}, []
int
{
-
1
,
6
})
// true
[
play
]
NoneBy
Returns true if the predicate returns true for none of the elements in the collection or if the collection is empty.
b
:=
NoneBy
([]
int
{
1
,
2
,
3
,
4
},
func
(
x
int
)
bool
{
return
x
<
0
})
// true
[
play
]
Intersect
Returns the intersection between two collections.
result1
:=
lo
.
Intersect
([]
int
{
0
,
1
,
2
,
3
,
4
,
5
}, []
int
{
0
,
2
})
// []int{0, 2}
result2
:=
lo
.
Intersect
([]
int
{
0
,
1
,
2
,
3
,
4
,
5
}, []
int
{
0
,
6
})
// []int{0}
result3
:=
lo
.
Intersect
([]
int
{
0
,
1
,
2
,
3
,
4
,
5
}, []
int
{
-
1
,
6
})
// []int{}
Difference
Returns the difference between two collections.
The first value is the collection of elements absent from list2.
The second value is the collection of elements absent from list1.
left
,
right
:=
lo
.
Difference
([]
int
{
0
,
1
,
2
,
3
,
4
,
5
}, []
int
{
0
,
2
,
6
})
// []int{1, 3, 4, 5}, []int{6}
left
,
right
:=
lo
.
Difference
([]
int
{
0
,
1
,
2
,
3
,
4
,
5
}, []
int
{
0
,
1
,
2
,
3
,
4
,
5
})
// []int{}, []int{}
[
play
]
Union
Returns all distinct elements from given collections. Result will not change the order of elements relatively.
union
:=
lo
.
Union
([]
int
{
0
,
1
,
2
,
3
,
4
,
5
}, []
int
{
0
,
2
}, []
int
{
0
,
10
})
// []int{0, 1, 2, 3, 4, 5, 10}
Without
Returns a slice excluding all given values.
subset
:=
lo
.
Without
([]
int
{
0
,
2
,
10
},
2
)
// []int{0, 10}
subset
:=
lo
.
Without
([]
int
{
0
,
2
,
10
},
0
,
1
,
2
,
3
,
4
,
5
)
// []int{10}
WithoutBy
Filters a slice by excluding elements whose extracted keys match any in the exclude list.
Returns a new slice containing only the elements whose keys are not in the exclude list.
type
struct
User
{
ID
int
Name
string
}
// original users
users
:=
[]
User
{
    {
ID
:
1
,
Name
:
"Alice"
},
    {
ID
:
2
,
Name
:
"Bob"
},
    {
ID
:
3
,
Name
:
"Charlie"
},
}
// extract function to get the user ID
getID
:=
func
(
user
User
)
int
{
return
user
.
ID
}
// exclude users with IDs 2 and 3
excludedIDs
:=
[]
int
{
2
,
3
}
// filtering users
filteredUsers
:=
lo
.
WithoutBy
(
users
,
getID
,
excludedIDs
...
)
// []User[{ID: 1, Name: "Alice"}]
WithoutEmpty
Returns a slice excluding zero values.
subset
:=
lo
.
WithoutEmpty
([]
int
{
0
,
2
,
10
})
// []int{2, 10}
WithoutNth
Returns a slice excluding the nth value.
subset
:=
lo
.
WithoutNth
([]
int
{
-
2
,
-
1
,
0
,
1
,
2
},
3
,
-
42
,
1
)
// []int{-2, 0, 2}
ElementsMatch
Returns true if lists contain the same set of elements (including empty set).
If there are duplicate elements, the number of occurrences in each list should match.
The order of elements is not checked.
b
:=
lo
.
ElementsMatch
([]
int
{
1
,
1
,
2
}, []
int
{
2
,
1
,
1
})
// true
ElementsMatchBy
Returns true if lists contain the same set of elements' keys (including empty set).
If there are duplicate keys, the number of occurrences in each list should match.
The order of elements is not checked.
b
:=
lo
.
ElementsMatchBy
(
    []
someType
{
a
,
b
},
    []
someType
{
b
,
a
},
func
(
item
someType
)
string
{
return
item
.
ID
() },
)
// true
IndexOf
Returns the index at which the first occurrence of a value is found in a slice or -1 if the value cannot be found.
found
:=
lo
.
IndexOf
([]
int
{
0
,
1
,
2
,
1
,
2
,
3
},
2
)
// 2
notFound
:=
lo
.
IndexOf
([]
int
{
0
,
1
,
2
,
1
,
2
,
3
},
6
)
// -1
[
play
]
LastIndexOf
Returns the index at which the last occurrence of a value is found in a slice or -1 if the value cannot be found.
found
:=
lo
.
LastIndexOf
([]
int
{
0
,
1
,
2
,
1
,
2
,
3
},
2
)
// 4
notFound
:=
lo
.
LastIndexOf
([]
int
{
0
,
1
,
2
,
1
,
2
,
3
},
6
)
// -1
HasPrefix
Returns true if the collection has the prefix.
ok
:=
lo
.
HasPrefix
([]
int
{
1
,
2
,
3
,
4
}, []
int
{
42
})
// false
ok
:=
lo
.
HasPrefix
([]
int
{
1
,
2
,
3
,
4
}, []
int
{
1
,
2
})
// true
[
play
]
HasSuffix
Returns true if the collection has the suffix.
ok
:=
lo
.
HasSuffix
([]
int
{
1
,
2
,
3
,
4
}, []
int
{
42
})
// false
ok
:=
lo
.
HasSuffix
([]
int
{
1
,
2
,
3
,
4
}, []
int
{
3
,
4
})
// true
[
play
]
Find
Searches for an element in a slice based on a predicate. Returns element and true if element was found.
str
,
ok
:=
lo
.
Find
([]
string
{
"a"
,
"b"
,
"c"
,
"d"
},
func
(
i
string
)
bool
{
return
i
==
"b"
})
// "b", true
str
,
ok
:=
lo
.
Find
([]
string
{
"foobar"
},
func
(
i
string
)
bool
{
return
i
==
"b"
})
// "", false
[
play
]
FindIndexOf
FindIndexOf searches for an element in a slice based on a predicate and returns the index and true. Returns -1 and false if the element is not found.
str
,
index
,
ok
:=
lo
.
FindIndexOf
([]
string
{
"a"
,
"b"
,
"a"
,
"b"
},
func
(
i
string
)
bool
{
return
i
==
"b"
})
// "b", 1, true
str
,
index
,
ok
:=
lo
.
FindIndexOf
([]
string
{
"foobar"
},
func
(
i
string
)
bool
{
return
i
==
"b"
})
// "", -1, false
[
play
]
FindLastIndexOf
FindLastIndexOf searches for the last element in a slice based on a predicate and returns the index and true. Returns -1 and false if the element is not found.
str
,
index
,
ok
:=
lo
.
FindLastIndexOf
([]
string
{
"a"
,
"b"
,
"a"
,
"b"
},
func
(
i
string
)
bool
{
return
i
==
"b"
})
// "b", 4, true
str
,
index
,
ok
:=
lo
.
FindLastIndexOf
([]
string
{
"foobar"
},
func
(
i
string
)
bool
{
return
i
==
"b"
})
// "", -1, false
[
play
]
FindOrElse
Searches for an element in a slice based on a predicate. Returns the element if found or a given fallback value otherwise.
str
:=
lo
.
FindOrElse
([]
string
{
"a"
,
"b"
,
"c"
,
"d"
},
"x"
,
func
(
i
string
)
bool
{
return
i
==
"b"
})
// "b"
str
:=
lo
.
FindOrElse
([]
string
{
"foobar"
},
"x"
,
func
(
i
string
)
bool
{
return
i
==
"b"
})
// "x"
FindKey
Returns the key of the first value matching.
result1
,
ok1
:=
lo
.
FindKey
(
map
[
string
]
int
{
"foo"
:
1
,
"bar"
:
2
,
"baz"
:
3
},
2
)
// "bar", true
result2
,
ok2
:=
lo
.
FindKey
(
map
[
string
]
int
{
"foo"
:
1
,
"bar"
:
2
,
"baz"
:
3
},
42
)
// "", false
type
test
struct
{
foobar
string
}
result3
,
ok3
:=
lo
.
FindKey
(
map
[
string
]
test
{
"foo"
:
test
{
"foo"
},
"bar"
:
test
{
"bar"
},
"baz"
:
test
{
"baz"
}},
test
{
"foo"
})
// "foo", true
FindKeyBy
Returns the key of the first element predicate returns true for.
result1
,
ok1
:=
lo
.
FindKeyBy
(
map
[
string
]
int
{
"foo"
:
1
,
"bar"
:
2
,
"baz"
:
3
},
func
(
k
string
,
v
int
)
bool
{
return
k
==
"foo"
})
// "foo", true
result2
,
ok2
:=
lo
.
FindKeyBy
(
map
[
string
]
int
{
"foo"
:
1
,
"bar"
:
2
,
"baz"
:
3
},
func
(
k
string
,
v
int
)
bool
{
return
false
})
// "", false
FindUniques
Returns a slice with all the elements that appear in the collection only once. The order of result values is determined by the order they occur in the slice.
uniqueValues
:=
lo
.
FindUniques
([]
int
{
1
,
2
,
2
,
1
,
2
,
3
})
// []int{3}
FindUniquesBy
Returns a slice with all the elements that appear in the collection only once. The order of result values is determined by the order they occur in the slice. It accepts
iteratee
which is invoked for each element in the slice to generate the criterion by which uniqueness is computed.
uniqueValues
:=
lo
.
FindUniquesBy
([]
int
{
3
,
4
,
5
,
6
,
7
},
func
(
i
int
)
int
{
return
i
%
3
})
// []int{5}
FindDuplicates
Returns a slice with the first occurrence of each duplicated element in the collection. The order of result values is determined by the order they occur in the slice.
duplicatedValues
:=
lo
.
FindDuplicates
([]
int
{
1
,
2
,
2
,
1
,
2
,
3
})
// []int{1, 2}
FindDuplicatesBy
Returns a slice with the first occurrence of each duplicated element in the collection. The order of result values is determined by the order they occur in the slice. It accepts
iteratee
which is invoked for each element in the slice to generate the criterion by which uniqueness is computed.
duplicatedValues
:=
lo
.
FindDuplicatesBy
([]
int
{
3
,
4
,
5
,
6
,
7
},
func
(
i
int
)
int
{
return
i
%
3
})
// []int{3, 4}
Min
Search the minimum value of a collection.
Returns zero value when the collection is empty.
min
:=
lo
.
Min
([]
int
{
1
,
2
,
3
})
// 1
min
:=
lo
.
Min
([]
int
{})
// 0
min
:=
lo
.
Min
([]time.
Duration
{
time
.
Second
,
time
.
Hour
})
// 1s
[
play
]
MinIndex
Search the minimum value of a collection and the index of the minimum value.
Returns (zero value, -1) when the collection is empty.
min
,
index
:=
lo
.
MinIndex
([]
int
{
1
,
2
,
3
})
// 1, 0
min
,
index
:=
lo
.
MinIndex
([]
int
{})
// 0, -1
min
,
index
:=
lo
.
MinIndex
([]time.
Duration
{
time
.
Second
,
time
.
Hour
})
// 1s, 0
MinBy
Search the minimum value of a collection using the given comparison function.
If several values of the collection are equal to the smallest value, returns the first such value.
Returns zero value when the collection is empty.
min
:=
lo
.
MinBy
([]
string
{
"s1"
,
"string2"
,
"s3"
},
func
(
item
string
,
min
string
)
bool
{
return
len
(
item
)
<
len
(
min
)
})
// "s1"
min
:=
lo
.
MinBy
([]
string
{},
func
(
item
string
,
min
string
)
bool
{
return
len
(
item
)
<
len
(
min
)
})
// ""
MinIndexBy
Search the minimum value of a collection using the given comparison function and the index of the minimum value.
If several values of the collection are equal to the smallest value, returns the first such value.
Returns (zero value, -1) when the collection is empty.
min
,
index
:=
lo
.
MinIndexBy
([]
string
{
"s1"
,
"string2"
,
"s3"
},
func
(
item
string
,
min
string
)
bool
{
return
len
(
item
)
<
len
(
min
)
})
// "s1", 0
min
,
index
:=
lo
.
MinIndexBy
([]
string
{},
func
(
item
string
,
min
string
)
bool
{
return
len
(
item
)
<
len
(
min
)
})
// "", -1
Earliest
Search the minimum time.Time of a collection.
Returns zero value when the collection is empty.
earliest
:=
lo
.
Earliest
(
time
.
Now
(), time.
Time
{})
// 0001-01-01 00:00:00 +0000 UTC
EarliestBy
Search the minimum time.Time of a collection using the given iteratee function.
Returns zero value when the collection is empty.
type
foo
struct
{
bar
time.
Time
}
earliest
:=
lo
.
EarliestBy
([]
foo
{{
time
.
Now
()}, {}},
func
(
i
foo
) time.
Time
{
return
i
.
bar
})
// {bar:{2023-04-01 01:02:03 +0000 UTC}}
Max
Search the maximum value of a collection.
Returns zero value when the collection is empty.
max
:=
lo
.
Max
([]
int
{
1
,
2
,
3
})
// 3
max
:=
lo
.
Max
([]
int
{})
// 0
max
:=
lo
.
Max
([]time.
Duration
{
time
.
Second
,
time
.
Hour
})
// 1h
MaxIndex
Search the maximum value of a collection and the index of the maximum value.
Returns (zero value, -1) when the collection is empty.
max
,
index
:=
lo
.
MaxIndex
([]
int
{
1
,
2
,
3
})
// 3, 2
max
,
index
:=
lo
.
MaxIndex
([]
int
{})
// 0, -1
max
,
index
:=
lo
.
MaxIndex
([]time.
Duration
{
time
.
Second
,
time
.
Hour
})
// 1h, 1
MaxBy
Search the maximum value of a collection using the given comparison function.
If several values of the collection are equal to the greatest value, returns the first such value.
Returns zero value when the collection is empty.
max
:=
lo
.
MaxBy
([]
string
{
"string1"
,
"s2"
,
"string3"
},
func
(
item
string
,
max
string
)
bool
{
return
len
(
item
)
>
len
(
max
)
})
// "string1"
max
:=
lo
.
MaxBy
([]
string
{},
func
(
item
string
,
max
string
)
bool
{
return
len
(
item
)
>
len
(
max
)
})
// ""
MaxIndexBy
Search the maximum value of a collection using the given comparison function and the index of the maximum value.
If several values of the collection are equal to the greatest value, returns the first such value.
Returns (zero value, -1) when the collection is empty.
max
,
index
:=
lo
.
MaxIndexBy
([]
string
{
"string1"
,
"s2"
,
"string3"
},
func
(
item
string
,
max
string
)
bool
{
return
len
(
item
)
>
len
(
max
)
})
// "string1", 0
max
,
index
:=
lo
.
MaxIndexBy
([]
string
{},
func
(
item
string
,
max
string
)
bool
{
return
len
(
item
)
>
len
(
max
)
})
// "", -1
Latest
Search the maximum time.Time of a collection.
Returns zero value when the collection is empty.
latest
:=
lo
.
Latest
(
time
.
Now
(), time.
Time
{})
// 2023-04-01 01:02:03 +0000 UTC
LatestBy
Search the maximum time.Time of a collection using the given iteratee function.
Returns zero value when the collection is empty.
type
foo
struct
{
bar
time.
Time
}
latest
:=
lo
.
LatestBy
([]
foo
{{
time
.
Now
()}, {}},
func
(
i
foo
) time.
Time
{
return
i
.
bar
})
// {bar:{2023-04-01 01:02:03 +0000 UTC}}
First
Returns the first element of a collection and check for availability of the first element.
first
,
ok
:=
lo
.
First
([]
int
{
1
,
2
,
3
})
// 1, true
first
,
ok
:=
lo
.
First
([]
int
{})
// 0, false
FirstOrEmpty
Returns the first element of a collection or zero value if empty.
first
:=
lo
.
FirstOrEmpty
([]
int
{
1
,
2
,
3
})
// 1
first
:=
lo
.
FirstOrEmpty
([]
int
{})
// 0
FirstOr
Returns the first element of a collection or the fallback value if empty.
first
:=
lo
.
FirstOr
([]
int
{
1
,
2
,
3
},
245
)
// 1
first
:=
lo
.
FirstOr
([]
int
{},
31
)
// 31
Last
Returns the last element of a collection or error if empty.
last
,
ok
:=
lo
.
Last
([]
int
{
1
,
2
,
3
})
// 3
// true
last
,
ok
:=
lo
.
Last
([]
int
{})
// 0
// false
LastOrEmpty
Returns the last element of a collection or zero value if empty.
last
:=
lo
.
LastOrEmpty
([]
int
{
1
,
2
,
3
})
// 3
last
:=
lo
.
LastOrEmpty
([]
int
{})
// 0
LastOr
Returns the last element of a collection or the fallback value if empty.
last
:=
lo
.
LastOr
([]
int
{
1
,
2
,
3
},
245
)
// 3
last
:=
lo
.
LastOr
([]
int
{},
31
)
// 31
Nth
Returns the element at index
nth
of collection. If
nth
is negative, the nth element from the end is returned. An error is returned when nth is out of slice bounds.
nth
,
err
:=
lo
.
Nth
([]
int
{
0
,
1
,
2
,
3
},
2
)
// 2
nth
,
err
:=
lo
.
Nth
([]
int
{
0
,
1
,
2
,
3
},
-
2
)
// 2
NthOr
Returns the element at index
nth
of the collection. If
nth
is negative, it returns the
nth
element from the end. If
nth
is out of slice bounds, it returns the provided fallback value
nth
:=
lo
.
NthOr
([]
int
{
10
,
20
,
30
,
40
,
50
},
2
,
-
1
)
// 30
nth
:=
lo
.
NthOr
([]
int
{
10
,
20
,
30
,
40
,
50
},
-
1
,
-
1
)
// 50
nth
:=
lo
.
NthOr
([]
int
{
10
,
20
,
30
,
40
,
50
},
5
,
-
1
)
// -1 (fallback value)
NthOrEmpty
Returns the element at index
nth
of the collection. If
nth
is negative, it returns the
nth
element from the end. If
nth
is out of slice bounds, it returns the zero value for the element type (e.g., 0 for integers, "" for strings, etc).
nth
:=
lo
.
NthOrEmpty
([]
int
{
10
,
20
,
30
,
40
,
50
},
2
)
// 30
nth
:=
lo
.
NthOrEmpty
([]
int
{
10
,
20
,
30
,
40
,
50
},
-
1
)
// 50
nth
:=
lo
.
NthOrEmpty
([]
int
{
10
,
20
,
30
,
40
,
50
},
5
)
// 0 (zero value for int)
nth
:=
lo
.
NthOrEmpty
([]
string
{
"apple"
,
"banana"
,
"cherry"
},
2
)
// "cherry"
nth
:=
lo
.
NthOrEmpty
([]
string
{
"apple"
,
"banana"
,
"cherry"
},
5
)
// "" (zero value for string)
Sample
Returns a random item from collection.
lo
.
Sample
([]
string
{
"a"
,
"b"
,
"c"
})
// a random string from []string{"a", "b", "c"}
lo
.
Sample
([]
string
{})
// ""
[
play
]
SampleBy
Returns a random item from collection, using a given random integer generator.
import
"math/rand"
r
:=
rand
.
New
(
rand
.
NewSource
(
42
))
lo
.
SampleBy
([]
string
{
"a"
,
"b"
,
"c"
},
r
.
Intn
)
// a random string from []string{"a", "b", "c"}, using a seeded random generator
lo
.
SampleBy
([]
string
{},
r
.
Intn
)
// ""
Samples
Returns N random unique items from collection.
lo
.
Samples
([]
string
{
"a"
,
"b"
,
"c"
},
3
)
// []string{"a", "b", "c"} in random order
SamplesBy
Returns N random unique items from collection, using a given random integer generator.
r
:=
rand
.
New
(
rand
.
NewSource
(
42
))
lo
.
SamplesBy
([]
string
{
"a"
,
"b"
,
"c"
},
3
,
r
.
Intn
)
// []string{"a", "b", "c"} in random order, using a seeded random generator
Ternary
A single line if/else statement.
result
:=
lo
.
Ternary
(
true
,
"a"
,
"b"
)
// "a"
result
:=
lo
.
Ternary
(
false
,
"a"
,
"b"
)
// "b"
Take care to avoid dereferencing potentially nil pointers in your A/B expressions, because they are both evaluated. See TernaryF to avoid this problem.
[
play
]
TernaryF
A single line if/else statement whose options are functions.
result
:=
lo
.
TernaryF
(
true
,
func
()
string
{
return
"a"
},
func
()
string
{
return
"b"
})
// "a"
result
:=
lo
.
TernaryF
(
false
,
func
()
string
{
return
"a"
},
func
()
string
{
return
"b"
})
// "b"
Useful to avoid nil-pointer dereferencing in initializations, or avoid running unnecessary code
var
s
*
string
someStr
:=
TernaryF
(
s
==
nil
,
func
()
string
{
return
uuid
.
New
().
String
() },
func
()
string
{
return
*
s
})
// ef782193-c30c-4e2e-a7ae-f8ab5e125e02
[
play
]
If / ElseIf / Else
result
:=
lo
.
If
(
true
,
1
).
ElseIf
(
false
,
2
).
Else
(
3
)
// 1
result
:=
lo
.
If
(
false
,
1
).
ElseIf
(
true
,
2
).
Else
(
3
)
// 2
result
:=
lo
.
If
(
false
,
1
).
ElseIf
(
false
,
2
).
Else
(
3
)
// 3
Using callbacks:
result
:=
lo
.
IfF
(
true
,
func
()
int
{
return
1
}).
ElseIfF
(
false
,
func
()
int
{
return
2
}).
ElseF
(
func
()
int
{
return
3
})
// 1
Mixed:
result
:=
lo
.
IfF
(
true
,
func
()
int
{
return
1
}).
Else
(
42
)
// 1
[
play
]
Switch / Case / Default
result
:=
lo
.
Switch
(
1
).
Case
(
1
,
"1"
).
Case
(
2
,
"2"
).
Default
(
"3"
)
// "1"
result
:=
lo
.
Switch
(
2
).
Case
(
1
,
"1"
).
Case
(
2
,
"2"
).
Default
(
"3"
)
// "2"
result
:=
lo
.
Switch
(
42
).
Case
(
1
,
"1"
).
Case
(
2
,
"2"
).
Default
(
"3"
)
// "3"
Using callbacks:
result
:=
lo
.
Switch
(
1
).
CaseF
(
1
,
func
()
string
{
return
"1"
}).
CaseF
(
2
,
func
()
string
{
return
"2"
}).
DefaultF
(
func
()
string
{
return
"3"
})
// "1"
Mixed:
result
:=
lo
.
Switch
(
1
).
CaseF
(
1
,
func
()
string
{
return
"1"
}).
Default
(
"42"
)
// "1"
[
play
]
IsNil
Checks if a value is nil or if it's a reference type with a nil underlying value.
var
x
int
lo
.
IsNil
(
x
)
// false
var
k
struct
{}
lo
.
IsNil
(
k
)
// false
var
i
*
int
lo
.
IsNil
(
i
)
// true
var
ifaceWithNilValue
any
=
(
*
string
)(
nil
)
lo
.
IsNil
(
ifaceWithNilValue
)
// true
ifaceWithNilValue
==
nil
// false
IsNotNil
Checks if a value is not nil or if it's not a reference type with a nil underlying value.
var
x
int
lo
.
IsNotNil
(
x
)
// true
var
k
struct
{}
lo
.
IsNotNil
(
k
)
// true
var
i
*
int
lo
.
IsNotNil
(
i
)
// false
var
ifaceWithNilValue
any
=
(
*
string
)(
nil
)
lo
.
IsNotNil
(
ifaceWithNilValue
)
// false
ifaceWithNilValue
==
nil
// true
ToPtr
Returns a pointer copy of the value.
ptr
:=
lo
.
ToPtr
(
"hello world"
)
// *string{"hello world"}
[
play
]
Nil
Returns a nil pointer of type.
ptr
:=
lo
.
Nil
[
float64
]()
// nil
EmptyableToPtr
Returns a pointer copy of value if it's nonzero.
Otherwise, returns nil pointer.
ptr
:=
lo
.
EmptyableToPtr
(
nil
)
// nil
ptr
:=
lo
.
EmptyableToPtr
(
""
)
// nil
ptr
:=
lo
.
EmptyableToPtr
([]
int
{})
// *[]int{}
ptr
:=
lo
.
EmptyableToPtr
(
"hello world"
)
// *string{"hello world"}
FromPtr
Returns the pointer value or empty.
str
:=
"hello world"
value
:=
lo
.
FromPtr
(
&
str
)
// "hello world"
value
:=
lo
.
FromPtr
(
nil
)
// ""
FromPtrOr
Returns the pointer value or the fallback value.
str
:=
"hello world"
value
:=
lo
.
FromPtrOr
(
&
str
,
"empty"
)
// "hello world"
value
:=
lo
.
FromPtrOr
(
nil
,
"empty"
)
// "empty"
ToSlicePtr
Returns a slice of pointers to each value.
ptr
:=
lo
.
ToSlicePtr
([]
string
{
"hello"
,
"world"
})
// []*string{"hello", "world"}
FromSlicePtr
Returns a slice with the pointer values.
Returns a zero value in case of a nil pointer element.
str1
:=
"hello"
str2
:=
"world"
ptr
:=
lo.
FromSlicePtr
[
string
]([]
*
string
{
&
str1
,
&
str2
,
nil
})
// []string{"hello", "world", ""}
ptr
:=
lo
.
Compact
(
    lo.
FromSlicePtr
[
string
]([]
*
string
{
&
str1
,
&
str2
,
nil
}),
)
// []string{"hello", "world"}
FromSlicePtrOr
Returns a slice with the pointer values or the fallback value.
str1
:=
"hello"
str2
:=
"world"
ptr
:=
lo
.
FromSlicePtrOr
([]
*
string
{
&
str1
,
nil
,
&
str2
},
"fallback value"
)
// []string{"hello", "fallback value", "world"}
[
play
]
ToAnySlice
Returns a slice with all elements mapped to
any
type.
elements
:=
lo
.
ToAnySlice
([]
int
{
1
,
5
,
1
})
// []any{1, 5, 1}
FromAnySlice
Returns a slice with all elements mapped to a type. Returns false in case of type conversion failure.
elements
,
ok
:=
lo
.
FromAnySlice
([]
any
{
"foobar"
,
42
})
// []string{}, false
elements
,
ok
:=
lo
.
FromAnySlice
([]
any
{
"foobar"
,
"42"
})
// []string{"foobar", "42"}, true
Empty
Returns the
zero value
.
lo
.
Empty
[
int
]()
// 0
lo
.
Empty
[
string
]()
// ""
lo
.
Empty
[
bool
]()
// false
IsEmpty
Returns true if argument is a zero value.
lo
.
IsEmpty
(
0
)
// true
lo
.
IsEmpty
(
42
)
// false
lo
.
IsEmpty
(
""
)
// true
lo
.
IsEmpty
(
"foobar"
)
// false
type
test
struct
{
foobar
string
}
lo
.
IsEmpty
(
test
{
foobar
:
""
})
// true
lo
.
IsEmpty
(
test
{
foobar
:
"foobar"
})
// false
IsNotEmpty
Returns true if argument is a zero value.
lo
.
IsNotEmpty
(
0
)
// false
lo
.
IsNotEmpty
(
42
)
// true
lo
.
IsNotEmpty
(
""
)
// false
lo
.
IsNotEmpty
(
"foobar"
)
// true
type
test
struct
{
foobar
string
}
lo
.
IsNotEmpty
(
test
{
foobar
:
""
})
// false
lo
.
IsNotEmpty
(
test
{
foobar
:
"foobar"
})
// true
Coalesce
Returns the first non-empty arguments. Arguments must be comparable.
result
,
ok
:=
lo
.
Coalesce
(
0
,
1
,
2
,
3
)
// 1 true
result
,
ok
:=
lo
.
Coalesce
(
""
)
// "" false
var
nilStr
*
string
str
:=
"foobar"
result
,
ok
:=
lo
.
Coalesce
(
nil
,
nilStr
,
&
str
)
// &"foobar" true
CoalesceOrEmpty
Returns the first non-empty arguments. Arguments must be comparable.
result
:=
lo
.
CoalesceOrEmpty
(
0
,
1
,
2
,
3
)
// 1
result
:=
lo
.
CoalesceOrEmpty
(
""
)
// ""
var
nilStr
*
string
str
:=
"foobar"
result
:=
lo
.
CoalesceOrEmpty
(
nil
,
nilStr
,
&
str
)
// &"foobar"
CoalesceSlice
Returns the first non-zero slice.
result
,
ok
:=
lo
.
CoalesceSlice
([]
int
{
1
,
2
,
3
}, []
int
{
4
,
5
,
6
})
// [1, 2, 3]
// true
result
,
ok
:=
lo
.
CoalesceSlice
(
nil
, []
int
{})
// []
// true
result
,
ok
:=
lo
.
CoalesceSlice
([]
int
(
nil
))
// []
// false
CoalesceSliceOrEmpty
Returns the first non-zero slice.
result
:=
lo
.
CoalesceSliceOrEmpty
([]
int
{
1
,
2
,
3
}, []
int
{
4
,
5
,
6
})
// [1, 2, 3]
result
:=
lo
.
CoalesceSliceOrEmpty
(
nil
, []
int
{})
// []
CoalesceMap
Returns the first non-zero map.
result
,
ok
:=
lo
.
CoalesceMap
(
map
[
string
]
int
{
"1"
:
1
,
"2"
:
2
,
"3"
:
3
},
map
[
string
]
int
{
"4"
:
4
,
"5"
:
5
,
"6"
:
6
})
// {"1": 1, "2": 2, "3": 3}
// true
result
,
ok
:=
lo
.
CoalesceMap
(
nil
,
map
[
string
]
int
{})
// {}
// true
result
,
ok
:=
lo
.
CoalesceMap
(
map
[
string
]
int
(
nil
))
// {}
// false
CoalesceMapOrEmpty
Returns the first non-zero map.
result
:=
lo
.
CoalesceMapOrEmpty
(
map
[
string
]
int
{
"1"
:
1
,
"2"
:
2
,
"3"
:
3
},
map
[
string
]
int
{
"4"
:
4
,
"5"
:
5
,
"6"
:
6
})
// {"1": 1, "2": 2, "3": 3}
result
:=
lo
.
CoalesceMapOrEmpty
(
nil
,
map
[
string
]
int
{})
// {}
Partial
Returns new function that, when called, has its first argument set to the provided value.
add
:=
func
(
x
,
y
int
)
int
{
return
x
+
y
}
f
:=
lo
.
Partial
(
add
,
5
)
f
(
10
)
// 15
f
(
42
)
// 47
[
play
]
Partial2 -> Partial5
Returns new function that, when called, has its first argument set to the provided value.
add
:=
func
(
x
,
y
,
z
int
)
int
{
return
x
+
y
+
z
}
f
:=
lo
.
Partial2
(
add
,
42
)
f
(
10
,
5
)
// 57
f
(
42
,
-
4
)
// 80
[
play
]
Attempt
Invokes a function N times until it returns valid output. Returns either the caught error or nil.
When the first argument is less than
1
, the function runs until a successful response is returned.
iter
,
err
:=
lo
.
Attempt
(
42
,
func
(
i
int
)
error
{
if
i
==
5
{
return
nil
}
return
errors
.
New
(
"failed"
)
})
// 6
// nil
iter
,
err
:=
lo
.
Attempt
(
2
,
func
(
i
int
)
error
{
if
i
==
5
{
return
nil
}
return
errors
.
New
(
"failed"
)
})
// 2
// error "failed"
iter
,
err
:=
lo
.
Attempt
(
0
,
func
(
i
int
)
error
{
if
i
<
42
{
return
errors
.
New
(
"failed"
)
    }
return
nil
})
// 43
// nil
For more advanced retry strategies (delay, exponential backoff...), please take a look at
cenkalti/backoff
.
[
play
]
AttemptWithDelay
Invokes a function N times until it returns valid output, with a pause between each call. Returns either the caught error or nil.
When the first argument is less than
1
, the function runs until a successful response is returned.
iter
,
duration
,
err
:=
lo
.
AttemptWithDelay
(
5
,
2
*
time
.
Second
,
func
(
i
int
,
duration
time.
Duration
)
error
{
if
i
==
2
{
return
nil
}
return
errors
.
New
(
"failed"
)
})
// 3
// ~ 4 seconds
// nil
For more advanced retry strategies (delay, exponential backoff...), please take a look at
cenkalti/backoff
.
[
play
]
AttemptWhile
Invokes a function N times until it returns valid output. Returns either the caught error or nil, along with a bool value to determine whether the function should be invoked again. It will terminate the invoke immediately if the second return value is false.
When the first argument is less than
1
, the function runs until a successful response is returned.
count1
,
err1
:=
lo
.
AttemptWhile
(
5
,
func
(
i
int
) (
error
,
bool
) {
err
:=
doMockedHTTPRequest
(
i
)
if
err
!=
nil
{
if
errors
.
Is
(
err
,
ErrBadRequest
) {
// let's assume ErrBadRequest is a critical error that needs to terminate the invoke
return
err
,
false
// flag the second return value as false to terminate the invoke
}
return
err
,
true
}
return
nil
,
false
})
For more advanced retry strategies (delay, exponential backoff...), please take a look at
cenkalti/backoff
.
[
play
]
AttemptWhileWithDelay
Invokes a function N times until it returns valid output, with a pause between each call. Returns either the caught error or nil, along with a bool value to determine whether the function should be invoked again. It will terminate the invoke immediately if the second return value is false.
When the first argument is less than
1
, the function runs until a successful response is returned.
count1
,
time1
,
err1
:=
lo
.
AttemptWhileWithDelay
(
5
,
time
.
Millisecond
,
func
(
i
int
,
d
time.
Duration
) (
error
,
bool
) {
err
:=
doMockedHTTPRequest
(
i
)
if
err
!=
nil
{
if
errors
.
Is
(
err
,
ErrBadRequest
) {
// let's assume ErrBadRequest is a critical error that needs to terminate the invoke
return
err
,
false
// flag the second return value as false to terminate the invoke
}
return
err
,
true
}
return
nil
,
false
})
For more advanced retry strategies (delay, exponential backoff...), please take a look at
cenkalti/backoff
.
[
play
]
Debounce
NewDebounce
creates a debounced instance that delays invoking functions given until after wait milliseconds have elapsed, until
cancel
is called.
f
:=
func
() {
println
(
"Called once after 100ms when debounce stopped invoking!"
)
}
debounce
,
cancel
:=
lo
.
NewDebounce
(
100
*
time
.
Millisecond
,
f
)
for
j
:=
0
;
j
<
10
;
j
++
{
debounce
()
}
time
.
Sleep
(
1
*
time
.
Second
)
cancel
()
[
play
]
DebounceBy
NewDebounceBy
creates a debounced instance for each distinct key, that delays invoking functions given until after wait milliseconds have elapsed, until
cancel
is called.
f
:=
func
(
key
string
,
count
int
) {
println
(
key
+
": Called once after 100ms when debounce stopped invoking!"
)
}
debounce
,
cancel
:=
lo
.
NewDebounceBy
(
100
*
time
.
Millisecond
,
f
)
for
j
:=
0
;
j
<
10
;
j
++
{
debounce
(
"first key"
)
debounce
(
"second key"
)
}
time
.
Sleep
(
1
*
time
.
Second
)
cancel
(
"first key"
)
cancel
(
"second key"
)
[
play
]
Throttle
Creates a throttled instance that invokes given functions only once in every interval.
This returns 2 functions, First one is throttled function and Second one is a function to reset interval.
f
:=
func
() {
println
(
"Called once in every 100ms"
)
}
throttle
,
reset
:=
lo
.
NewThrottle
(
100
*
time
.
Millisecond
,
f
)
for
j
:=
0
;
j
<
10
;
j
++
{
throttle
()
time
.
Sleep
(
30
*
time
.
Millisecond
)
}
reset
()
throttle
()
NewThrottleWithCount
is NewThrottle with count limit, throttled function will be invoked count times in every interval.
f
:=
func
() {
println
(
"Called three times in every 100ms"
)
}
throttle
,
reset
:=
lo
.
NewThrottleWithCount
(
100
*
time
.
Millisecond
,
f
)
for
j
:=
0
;
j
<
10
;
j
++
{
throttle
()
time
.
Sleep
(
30
*
time
.
Millisecond
)
}
reset
()
throttle
()
NewThrottleBy
and
NewThrottleByWithCount
are NewThrottle with sharding key, throttled function will be invoked count times in every interval.
f
:=
func
(
key
string
) {
println
(
key
,
"Called three times in every 100ms"
)
}
throttle
,
reset
:=
lo
.
NewThrottleByWithCount
(
100
*
time
.
Millisecond
,
f
)
for
j
:=
0
;
j
<
10
;
j
++
{
throttle
(
"foo"
)
time
.
Sleep
(
30
*
time
.
Millisecond
)
}
reset
()
throttle
()
Synchronize
Wraps the underlying callback in a mutex. It receives an optional mutex.
s
:=
lo
.
Synchronize
()
for
i
:=
0
;
i
<
10
;
i
++
{
go
s
.
Do
(
func
() {
println
(
"will be called sequentially"
)
    })
}
It is equivalent to:
mu
:=
sync.
Mutex
{}
func
foobar
() {
mu
.
Lock
()
defer
mu
.
Unlock
()
// ...
}
Async
Executes a function in a goroutine and returns the result in a channel.
ch
:=
lo
.
Async
(
func
()
error
{
time
.
Sleep
(
10
*
time
.
Second
);
return
nil
})
// chan error (nil)
Async{0->6}
Executes a function in a goroutine and returns the result in a channel.
For functions with multiple return values, the results will be returned as a tuple inside the channel.
For functions without return, struct{} will be returned in the channel.
ch
:=
lo
.
Async0
(
func
() {
time
.
Sleep
(
10
*
time
.
Second
) })
// chan struct{}
ch
:=
lo
.
Async1
(
func
()
int
{
time
.
Sleep
(
10
*
time
.
Second
);
return
42
})
// chan int (42)
ch
:=
lo
.
Async2
(
func
() (
int
,
string
) {
time
.
Sleep
(
10
*
time
.
Second
);
return
42
,
"Hello"
})
// chan lo.Tuple2[int, string] ({42, "Hello"})
Transaction
Implements a Saga pattern.
transaction
:=
NewTransaction
().
Then
(
func
(
state
int
) (
int
,
error
) {
fmt
.
Println
(
"step 1"
)
return
state
+
10
,
nil
},
func
(
state
int
)
int
{
fmt
.
Println
(
"rollback 1"
)
return
state
-
10
},
    ).
Then
(
func
(
state
int
) (
int
,
error
) {
fmt
.
Println
(
"step 2"
)
return
state
+
15
,
nil
},
func
(
state
int
)
int
{
fmt
.
Println
(
"rollback 2"
)
return
state
-
15
},
    ).
Then
(
func
(
state
int
) (
int
,
error
) {
fmt
.
Println
(
"step 3"
)
if
true
{
return
state
,
errors
.
New
(
"error"
)
            }
return
state
+
42
,
nil
},
func
(
state
int
)
int
{
fmt
.
Println
(
"rollback 3"
)
return
state
-
42
},
    )
_
,
_
=
transaction
.
Process
(
-
5
)
// Output:
// step 1
// step 2
// step 3
// rollback 2
// rollback 1
WaitFor
Runs periodically until a condition is validated.
alwaysTrue
:=
func
(
i
int
)
bool
{
return
true
}
alwaysFalse
:=
func
(
i
int
)
bool
{
return
false
}
laterTrue
:=
func
(
i
int
)
bool
{
return
i
>
5
}
iterations
,
duration
,
ok
:=
lo
.
WaitFor
(
alwaysTrue
,
10
*
time
.
Millisecond
,
2
*
time
.
Millisecond
)
// 1
// 1ms
// true
iterations
,
duration
,
ok
:=
lo
.
WaitFor
(
alwaysFalse
,
10
*
time
.
Millisecond
,
time
.
Millisecond
)
// 10
// 10ms
// false
iterations
,
duration
,
ok
:=
lo
.
WaitFor
(
laterTrue
,
10
*
time
.
Millisecond
,
time
.
Millisecond
)
// 7
// 7ms
// true
iterations
,
duration
,
ok
:=
lo
.
WaitFor
(
laterTrue
,
10
*
time
.
Millisecond
,
5
*
time
.
Millisecond
)
// 2
// 10ms
// false
[
play
]
WaitForWithContext
Runs periodically until a condition is validated or context is invalid.
The condition receives also the context, so it can invalidate the process in the condition checker
ctx
:=
context
.
Background
()
alwaysTrue
:=
func
(
_
context.
Context
,
i
int
)
bool
{
return
true
}
alwaysFalse
:=
func
(
_
context.
Context
,
i
int
)
bool
{
return
false
}
laterTrue
:=
func
(
_
context.
Context
,
i
int
)
bool
{
return
i
>=
5
}
iterations
,
duration
,
ok
:=
lo
.
WaitForWithContext
(
ctx
,
alwaysTrue
,
10
*
time
.
Millisecond
,
2
*
time
.
Millisecond
)
// 1
// 1ms
// true
iterations
,
duration
,
ok
:=
lo
.
WaitForWithContext
(
ctx
,
alwaysFalse
,
10
*
time
.
Millisecond
,
time
.
Millisecond
)
// 10
// 10ms
// false
iterations
,
duration
,
ok
:=
lo
.
WaitForWithContext
(
ctx
,
laterTrue
,
10
*
time
.
Millisecond
,
time
.
Millisecond
)
// 5
// 5ms
// true
iterations
,
duration
,
ok
:=
lo
.
WaitForWithContext
(
ctx
,
laterTrue
,
10
*
time
.
Millisecond
,
5
*
time
.
Millisecond
)
// 2
// 10ms
// false
expiringCtx
,
cancel
:=
context
.
WithTimeout
(
ctx
,
5
*
time
.
Millisecond
)
iterations
,
duration
,
ok
:=
lo
.
WaitForWithContext
(
expiringCtx
,
alwaysFalse
,
100
*
time
.
Millisecond
,
time
.
Millisecond
)
// 5
// 5.1ms
// false
[
play
]
Validate
Helper function that creates an error when a condition is not met.
slice
:=
[]
string
{
"a"
}
val
:=
lo
.
Validate
(
len
(
slice
)
==
0
,
"Slice should be empty but contains %v"
,
slice
)
// error("Slice should be empty but contains [a]")
slice
:=
[]
string
{}
val
:=
lo
.
Validate
(
len
(
slice
)
==
0
,
"Slice should be empty but contains %v"
,
slice
)
// nil
[
play
]
Must
Wraps a function call and panics if second argument is
error
or
false
, returns the value otherwise.
val
:=
lo
.
Must
(
time
.
Parse
(
"2006-01-02"
,
"2022-01-15"
))
// 2022-01-15
val
:=
lo
.
Must
(
time
.
Parse
(
"2006-01-02"
,
"bad-value"
))
// panics
[
play
]
Must{0->6}
Must* has the same behavior as Must but returns multiple values.
func
example0
() (
error
)
func
example1
() (
int
,
error
)
func
example2
() (
int
,
string
,
error
)
func
example3
() (
int
,
string
, time.
Date
,
error
)
func
example4
() (
int
,
string
, time.
Date
,
bool
,
error
)
func
example5
() (
int
,
string
, time.
Date
,
bool
,
float64
,
error
)
func
example6
() (
int
,
string
, time.
Date
,
bool
,
float64
,
byte
,
error
)
lo
.
Must0
(
example0
())
val1
:=
lo
.
Must1
(
example1
())
// alias to Must
val1
,
val2
:=
lo
.
Must2
(
example2
())
val1
,
val2
,
val3
:=
lo
.
Must3
(
example3
())
val1
,
val2
,
val3
,
val4
:=
lo
.
Must4
(
example4
())
val1
,
val2
,
val3
,
val4
,
val5
:=
lo
.
Must5
(
example5
())
val1
,
val2
,
val3
,
val4
,
val5
,
val6
:=
lo
.
Must6
(
example6
())
You can wrap functions like
func (...) (..., ok bool)
.
// math.Signbit(float64) bool
lo
.
Must0
(
math
.
Signbit
(
v
))
// bytes.Cut([]byte,[]byte) ([]byte, []byte, bool)
before
,
after
:=
lo
.
Must2
(
bytes
.
Cut
(
s
,
sep
))
You can give context to the panic message by adding some printf-like arguments.
val
,
ok
:=
lo
.
Find
(
myString
,
func
(
i
string
)
bool
{
return
i
==
requiredChar
})
lo
.
Must0
(
ok
,
"'%s' must always contain '%s'"
,
myString
,
requiredChar
)
list
:=
[]
int
{
0
,
1
,
2
}
item
:=
5
lo
.
Must0
(
lo
.
Contains
(
list
,
item
),
"'%s' must always contain '%s'"
,
list
,
item
)
...
[
play
]
Try
Calls the function and returns false in case of error and panic.
ok
:=
lo
.
Try
(
func
()
error
{
panic
(
"error"
)
return
nil
})
// false
ok
:=
lo
.
Try
(
func
()
error
{
return
nil
})
// true
ok
:=
lo
.
Try
(
func
()
error
{
return
errors
.
New
(
"error"
)
})
// false
[
play
]
Try{0->6}
The same behavior as
Try
, but the callback returns 2 variables.
ok
:=
lo
.
Try2
(
func
() (
string
,
error
) {
panic
(
"error"
)
return
""
,
nil
})
// false
[
play
]
TryOr
Calls the function and return a default value in case of error and on panic.
str
,
ok
:=
lo
.
TryOr
(
func
() (
string
,
error
) {
panic
(
"error"
)
return
"hello"
,
nil
},
"world"
)
// world
// false
str
,
ok
:=
lo
.
TryOr
(
func
()
error
{
return
"hello"
,
nil
},
"world"
)
// hello
// true
str
,
ok
:=
lo
.
TryOr
(
func
()
error
{
return
"hello"
,
errors
.
New
(
"error"
)
},
"world"
)
// world
// false
[
play
]
TryOr{0->6}
The same behavior as
TryOr
, but the callback returns
X
variables.
str
,
nbr
,
ok
:=
lo
.
TryOr2
(
func
() (
string
,
int
,
error
) {
panic
(
"error"
)
return
"hello"
,
42
,
nil
},
"world"
,
21
)
// world
// 21
// false
[
play
]
TryWithErrorValue
The same behavior as
Try
, but also returns the value passed to panic.
err
,
ok
:=
lo
.
TryWithErrorValue
(
func
()
error
{
panic
(
"error"
)
return
nil
})
// "error", false
[
play
]
TryCatch
The same behavior as
Try
, but calls the catch function in case of error.
caught
:=
false
ok
:=
lo
.
TryCatch
(
func
()
error
{
panic
(
"error"
)
return
nil
},
func
() {
caught
=
true
})
// false
// caught == true
[
play
]
TryCatchWithErrorValue
The same behavior as
TryWithErrorValue
, but calls the catch function in case of error.
caught
:=
false
ok
:=
lo
.
TryCatchWithErrorValue
(
func
()
error
{
panic
(
"error"
)
return
nil
},
func
(
val
any
) {
caught
=
val
==
"error"
})
// false
// caught == true
[
play
]
ErrorsAs
A shortcut for:
err
:=
doSomething
()
var
rateLimitErr
*
RateLimitError
if
ok
:=
errors
.
As
(
err
,
&
rateLimitErr
);
ok
{
// retry later
}
single line
lo
helper:
err
:=
doSomething
()
if
rateLimitErr
,
ok
:=
lo.
ErrorsAs
[
*
RateLimitError
](
err
);
ok
{
// retry later
}
[
play
]
Assert
Does nothing when the condition is
true
, otherwise it panics with an optional message.
Think twice before using it, given that
Go intentionally omits assertions from its standard library
.
age
:=
getUserAge
()
lo
.
Assert
(
age
>=
15
)
age
:=
getUserAge
()
lo
.
Assert
(
age
>=
15
,
"user age must be >= 15"
)
[
play
]
Assertf
Like
Assert
, but with
fmt.Printf
-like formatting.
Think twice before using it, given that
Go intentionally omits assertions from its standard library
.
age
:=
getUserAge
()
lo
.
Assertf
(
age
>=
15
,
"user age must be >= 15, got %d"
,
age
)
[
play
]
🛩 Benchmark
We executed a simple benchmark with a dead-simple
lo.Map
loop:
See the full implementation
here
.
_
=
lo
.
Map
[
int64
](
arr
,
func
(
x
int64
,
i
int
)
string
{
return
strconv
.
FormatInt
(
x
,
10
)
})
Result:
Here is a comparison between
lo.Map
,
lop.Map
,
go-funk
library and a simple Go
for
loop.
$ go
test
-benchmem -bench ./...
goos: linux
goarch: amd64
pkg: github.com/samber/lo
cpu: Intel(R) Core(TM) i5-7267U CPU @ 3.10GHz
cpu: Intel(R) Core(TM) i7 CPU         920  @ 2.67GHz
BenchmarkMap/lo.Map-8         	       8	 132728237 ns/op	39998945 B/op	 1000002 allocs/op
BenchmarkMap/lop.Map-8        	       2	 503947830 ns/op	119999956 B/op	 3000007 allocs/op
BenchmarkMap/reflect-8        	       2	 826400560 ns/op	170326512 B/op	 4000042 allocs/op
BenchmarkMap/for-8            	       9	 126252954 ns/op	39998674 B/op	 1000001 allocs/op
PASS
ok  	github.com/samber/lo	6.657s
lo.Map
is way faster (x7) than
go-funk
, a reflection-based Map implementation.
lo.Map
has the same allocation profile as
for
.
lo.Map
is 4% slower than
for
.
lop.Map
is slower than
lo.Map
because it implies more memory allocation and locks.
lop.Map
is useful for long-running callbacks, such as i/o bound processing.
for
beats other implementations for memory and CPU.
🤝 Contributing
Ping me on Twitter
@samuelberthe
(DMs, mentions, whatever :))
Fork the
project
Fix
open issues
or request new features
Don't hesitate ;)
Helper naming: helpers must be self-explanatory and respect standards (other languages, libraries...). Feel free to suggest many names in your contributions.
#
Install some dev dependencies
make tools
#
Run tests
make
test
#
or
make watch-test
👤 Contributors
💫 Show your support
Give a ⭐️ if this project helped you!
📝 License
Copyright © 2022
Samuel Berthe
.
This project is under
MIT
license.
- 今日の獲得スター数: 64
- 累積スター数: 20,337

### References
- https://github.com/samber/lo

## aaPanel/BillionMail

### Executive Summary
- BillionMail gives you open-source MailServer, NewsLetter, Email Marketing — fully self-hosted, dev-friendly, and free from monthly fees. Join the discord: https://discord.gg/asfXzBUhZr
- ---
- BillionMail 📧
An Open-Source MailServer, NewsLetter, Email Marketing Solution for Smarter Campaigns
English |
简体中文
|
日本語
|
Türkçe
What is BillionMail?
BillionMail is a
future open-source Mail server, Email marketing platform
designed to help businesses and individuals manage their email campaigns with ease. Whether you're sending newsletters, promotional emails, or transactional messages, this tool will provide
full control
over your email marketing efforts. With features like
advanced analytics
, and
customer management
, you'll be able to create, send, and track emails like a pro.
Just 3 steps to send a billion emails!
Billion emails. Any business. Guaranteed.
Step 1️⃣ Install BillionMail:
✅ It takes
only 8️⃣ minutes
from installation to
✅ successful email sending
cd
/opt
&&
git clone https://github.com/aaPanel/BillionMail
&&
cd
BillionMail
&&
bash install.sh
Step 2️⃣: Connect Your Domain
Add the sending domain
Verify DNS records
Auto-enable free SSL
Step 3️⃣: Build Your Campaign
Write or paste your email
Choose list & tags
Set send time or send now
Watch on Youtube
Other installation methods
One-click installation on aaPanel
👉
https://www.aapanel.com/new/download.html
(Log in to ✅aaPanel --> 🐳Docker --> 1️⃣OneClick install)
Docker
cd
/opt
&&
git clone https://github.com/aaPanel/BillionMail
&&
cd
BillionMail
&&
cp env_init .env
&&
docker compose up -d
||
docker-compose up -d
Management script
Management help
bm help
View Login default info
bm default
Show domain DNS record
bm show-record
Update BillionMail
bm update
Live Demo
BillionMail Demo:
https://demo.billionmail.com/billionmail
Username:
billionmail
Password:
billionmail
WebMail
BillionMail has integrated
RoundCube
, you can access WebMail via
/roundcube/
.
Why BillionMail?
Most email marketing platforms are either
expensive
,
closed-source
, or
lack essential features
. BillionMail aims to be different:
✅
Fully Open-Source
– No hidden costs, no vendor lock-in.
📊
Advanced Analytics
– Track email delivery, open rates, click-through rates, and more.
📧
Unlimited Sending
– No restrictions on the number of emails you can send.
🎨
Customizable Templates
– Custom professional marketing templates for reuse.
🔒
Privacy-First
– Your data stays with you, no third-party tracking.
🚀
Self-Hosted
– Run it on your own server for complete control.
How You Can Help 🌟
BillionMail is a
community-driven project
, and we need your support to get started! Here's how you can help:
Star This Repository
: Show your interest by starring this repo.
Spread the Word
: Share BillionMail with your network—developers, marketers, and open-source enthusiasts.
Share Feedback
: Let us know what features you'd like to see in BillionMail by opening an issue or joining the discussion.
Contribute
: Once development begins, we'll welcome contributions from the community. Stay tuned for updates!
📧
BillionMail – The Future of Open-Source Email Marketing.
Issues
If you encounter any issues or have feature requests, please
open an issue
. Be sure to include:
A clear description of the problem or request.
Steps to reproduce the issue (if applicable).
Screenshots or error logs (if applicable).
Install Now:
✅It takes
only 8 minutes
from installation to
successful email sending
cd
/opt
&&
git clone https://github.com/aaPanel/BillionMail
&&
cd
BillionMail
&&
bash install.sh
Install with Docker:
(Please install Docker and docker-compose-plugin manually, and modify .env file)
cd
/opt
&&
git clone https://github.com/aaPanel/BillionMail
&&
cd
BillionMail
&&
cp env_init .env
&&
docker compose up -d
||
docker-compose up -d
Star History
License
BillionMail is licensed under the
AGPLv3 License
. This means you can:
✅ Use the software for free.
✅ Modify and distribute the code.
✅ Use it privately without restrictions.
See the
LICENSE
file for more details.
- 今日の獲得スター数: 54
- 累積スター数: 11,553

### References
- https://github.com/aaPanel/BillionMail

## ruvnet/claude-flow

### Executive Summary
- 🌊 The leading agent orchestration platform for Claude. Deploy intelligent multi-agent swarms, coordinate autonomous workflows, and build conversational AI systems. Features enterprise-grade architecture, distributed swarm intelligence, RAG integration, and native Claude Code support via MCP protocol. Ranked #1 in agent-based frameworks.
- ---
- 🌊 Claude-Flow v2.5.0 Alpha 140: AI Orchestration Platform
🌟
Overview
Claude-Flow v2 Alpha
is an enterprise-grade AI orchestration platform that reimagines how developers build with AI. By combining
hive-mind swarm intelligence
,
neural pattern recognition
, and
87 advanced MCP tools
, Claude-Flow enables unprecedented AI-powered development workflows.
🎯
Key Features
🐝 Hive-Mind Intelligence
: Queen-led AI coordination with specialized worker agents
🧠 Neural Networks
: 27+ cognitive models with WASM SIMD acceleration
🔧 87 MCP Tools
: Comprehensive toolkit for swarm orchestration, memory, and automation
🔄 Dynamic Agent Architecture (DAA)
: Self-organizing agents with fault tolerance
💾 SQLite Memory System
: Persistent
.swarm/memory.db
with 12 specialized tables
🪝 Advanced Hooks System
: Automated workflows with pre/post operation hooks
📊 GitHub Integration
: 6 specialized modes for repository management
🌐 Flow Nexus Cloud Platform
: E2B sandboxes, AI swarms, challenges, and marketplace integration
🎯 PreToolUse Modification Hooks
: NEW - Claude Code v2.0.10+ intelligent input modification (safety, organization, optimization)
🔥
Revolutionary AI Coordination
: Build faster, smarter, and more efficiently with AI-powered development orchestration
🎯
NEW: PreToolUse Modification Hooks Plugin
(v2.5.0-alpha.140)
First Claude Code plugin with intelligent tool input modification
- automatically enhances commands and files before execution.
Key Features:
🛡️
Safety
: Auto-adds
-i
to
rm
commands, detects sensitive keywords
📁
Organization
: Auto-routes files (tests→
/tests/
, src→
/src/
)
⚡
Productivity
: Alias expansion (
ll
→
ls -lah
), conventional commits
Quick Start:
Option 1: Direct Plugin Installation
(Recommended)
#
In Claude Code, run:
/plugin ruvnet/claude-flow
Option 2: Via NPM
npx claude-flow@alpha init --force
#
Auto-configures .claude-plugin/hooks/hooks.json
Examples:
rm test.txt          → rm -i test.txt
#
Safety
test.js             → src/test.js
#
Organization
git commit -m
"
fix
"
→ [fix] fix + co-author
#
Commits
📚
Docs
:
HOOKS-V2-MODIFICATION.md
|
Plugin
:
.claude-plugin/
|
Composable
with
agent-booster
🌐
Flow Nexus Cloud Platform
NEW
: Claude-Flow v2.0.0 now includes
Flow Nexus integration
- a cloud-powered AI development platform featuring:
E2B Sandboxes
: Secure isolated environments for Node.js, Python, React, Next.js
AI Swarms
: Deploy multi-agent systems in cloud infrastructure
Neural Training
: Distributed machine learning with custom model deployment
Challenges & Marketplace
: Coding challenges with rUv credit rewards and template marketplace
Workflow Automation
: Event-driven automation with message queue processing
📚
Complete documentation
: Visit
flow-nexus.ruv.io
for comprehensive guides, tutorials, and API reference. Also see issue #
#732
⚡
Try v2.0.0 Alpha in 4 Commands
📋
Prerequisites
Node.js 18+
(LTS recommended)
npm 9+
or equivalent package manager
Windows users
: See
Windows Installation Guide
for special instructions
⚠️
IMPORTANT
: Claude Code must be installed first:
#
1. Install Claude Code globally
npm install -g @anthropic-ai/claude-code
#
2. (Optional) Skip permissions check for faster setup
#
Only use if you understand the security implications
claude --dangerously-skip-permissions
💡
Windows Note
: If you encounter SQLite errors, Claude Flow will automatically use in-memory storage. For persistent storage options, see our
Windows guide
.
🎯
Instant Alpha Testing
Method 1: Plugin Installation
(Easiest - includes PreToolUse hooks!)
#
In Claude Code:
/plugin ruvnet/claude-flow
Method 2: NPM Installation
(For MCP server + CLI)
#
1. Initialize Claude Flow with enhanced MCP setup (auto-configures permissions!)
npx claude-flow@alpha init --force
#
2. Explore all revolutionary capabilities
npx claude-flow@alpha --help
#
3a. Quick AI coordination (recommended for most tasks)
npx claude-flow@alpha swarm
"
build me a REST API
"
--claude
#
3b. OR launch the full hive-mind system (for complex projects)
npx claude-flow@alpha hive-mind wizard
npx claude-flow@alpha hive-mind spawn
"
build enterprise system
"
--claude
🚀
Quick Start with Flow Nexus
#
1. Initialize Flow Nexus only (minimal setup)
npx claude-flow init --flow-nexus
#
2. Register and login (use MCP tools in Claude Code)
mcp__flow-nexus__user_register({ email:
"
your@email.com
"
, password:
"
secure
"
})
mcp__flow-nexus__user_login({ email:
"
your@email.com
"
, password:
"
secure
"
})
#
3. Deploy your first cloud swarm
mcp__flow-nexus__swarm_init({ topology:
"
mesh
"
, maxAgents: 5 })
mcp__flow-nexus__sandbox_create({ template:
"
node
"
, name:
"
api-dev
"
})
🤔
Swarm vs Hive-Mind: Which to Use?
Feature
swarm
Command
hive-mind
Command
Best For
Quick tasks, single objectives
Complex projects, persistent sessions
Setup
Instant - no configuration needed
Interactive wizard setup
Session
Temporary coordination
Persistent with resume capability
Memory
Task-scoped
Project-wide with SQLite storage
Agents
Auto-spawned for task
Manual control with specializations
Use When
"Build X", "Fix Y", "Analyze Z"
Multi-feature projects, team coordination
Quick Rule:
Start with
swarm
for most tasks. Use
hive-mind
when you need persistent sessions or complex multi-agent coordination.
🎯
Typical Workflows - Your "Happy Path" Guide
New to Claude-Flow? Start Here!
Confused about
.hive-mind
and
.swarm
directories? Not sure when to create new hives? Here are the most common workflow patterns:
🚀 Pattern 1: Single Feature Development
#
Initialize once per feature/task
npx claude-flow@alpha init --force
npx claude-flow@alpha hive-mind spawn
"
Implement user authentication
"
--claude
#
Continue working on SAME feature (reuse existing hive)
npx claude-flow@alpha hive-mind status
npx claude-flow@alpha memory query
"
authentication
"
--recent
npx claude-flow@alpha swarm
"
Add password reset functionality
"
--continue-session
🏗️ Pattern 2: Multi-Feature Project
#
Project-level initialization (once per project)
npx claude-flow@alpha init --force --project-name
"
my-app
"
#
Feature 1: Authentication (new hive)
npx claude-flow@alpha hive-mind spawn
"
auth-system
"
--namespace auth --claude
#
Feature 2: User management (separate hive)
npx claude-flow@alpha hive-mind spawn
"
user-management
"
--namespace users --claude
#
Resume Feature 1 later (use session ID from spawn output)
npx claude-flow@alpha hive-mind resume session-xxxxx-xxxxx
🔍 Pattern 3: Research & Analysis
#
Start research session
npx claude-flow@alpha hive-mind spawn
"
Research microservices patterns
"
--agents researcher,analyst --claude
#
Continue research in SAME session
npx claude-flow@alpha memory stats
#
See what's been learned
npx claude-flow@alpha swarm
"
Deep dive into API gateway patterns
"
--continue-session
🤔 When Should I Create a New Hive?
Situation
Action
Command
Same objective/feature
Continue existing hive
npx claude-flow@alpha hive-mind resume <session-id>
New feature in same project
Create new hive with namespace
npx claude-flow@alpha hive-mind spawn "new-feature" --namespace feature-name
Completely different project
New directory + init
mkdir new-project && cd new-project && npx claude-flow@alpha init
Experimenting/testing
Temporary hive
npx claude-flow@alpha hive-mind spawn "experiment" --temp
📁 Understanding "Empty" Directories
Don't panic if directories seem empty!
Claude-Flow uses SQLite databases that may not show files in directory listings:
#
Check what's actually stored (even if directories look empty)
npx claude-flow@alpha memory stats
#
See memory data
npx claude-flow@alpha memory list
#
List all namespaces
npx claude-flow@alpha hive-mind status
#
See active hives
#
Your project structure after initialization:
#
.hive-mind/     <- Contains config.json + SQLite session data
#
.swarm/         <- Contains memory.db (SQLite database)
#
memory/         <- Agent-specific memories (created when agents spawn)
#
coordination/   <- Active workflow files (created during tasks)
🔄 Continuing Previous Work
#
See what you were working on
npx claude-flow@alpha hive-mind status
npx claude-flow@alpha memory query --recent --limit 5
#
List all sessions to find the one you want
npx claude-flow@alpha hive-mind sessions
#
Resume specific session by ID
npx claude-flow@alpha hive-mind resume session-xxxxx-xxxxx
🪝
Advanced Hooks System
Automated Workflow Enhancement
Claude-Flow v2.0.0 introduces a powerful hooks system that automates coordination and enhances every operation:
#
Hooks automatically trigger on operations
npx claude-flow@alpha init --force
#
Auto-configures MCP servers & hooks
Available Hooks
Pre-Operation Hooks
pre-task
: Auto-assigns agents based on task complexity
pre-search
: Caches searches for improved performance
pre-edit
: Validates files and prepares resources
pre-command
: Security validation before execution
Post-Operation Hooks
post-edit
: Auto-formats code using language-specific tools
post-task
: Trains neural patterns from successful operations
post-command
: Updates memory with operation context
notification
: Real-time progress updates
Session Hooks
session-start
: Restores previous context automatically
session-end
: Generates summaries and persists state
session-restore
: Loads memory from previous sessions
Hook Configuration
// .claude/settings.json (auto-configured)
{
"hooks"
: {
"preEditHook"
: {
"command"
:
"
npx
"
,
"args"
: [
"
claude-flow
"
,
"
hooks
"
,
"
pre-edit
"
,
"
--file
"
,
"
${file}
"
,
"
--auto-assign-agents
"
,
"
true
"
],
"alwaysRun"
:
false
},
"postEditHook"
: {
"command"
:
"
npx
"
,
"args"
: [
"
claude-flow
"
,
"
hooks
"
,
"
post-edit
"
,
"
--file
"
,
"
${file}
"
,
"
--format
"
,
"
true
"
],
"alwaysRun"
:
true
},
"sessionEndHook"
: {
"command"
:
"
npx
"
,
"args"
: [
"
claude-flow
"
,
"
hooks
"
,
"
session-end
"
,
"
--generate-summary
"
,
"
true
"
],
"alwaysRun"
:
true
}
  }
}
📚
Complete Documentation
For detailed information about all features, advanced usage, and comprehensive guides, visit our
GitHub Wiki
:
🤖
Core Features
Neural Module
- SAFLA self-learning systems with 4-tier memory architecture
Goal Module
- GOAP intelligent planning with A* pathfinding
Agent System Overview
- Complete catalog of all 64 agents
Hive-Mind Intelligence
- Queen-led AI coordination patterns
⚡
Advanced Topics
Memory System
- SQLite-based persistent memory
MCP Tools Reference
- Complete guide to all 87 tools
GitHub Integration
- Repository management automation
Performance Benchmarking
- Optimization strategies
📋
Configuration & Templates
CLAUDE.md Templates
- Project-specific configurations
SPARC Methodology
- Test-driven development patterns
Development Patterns
- Best practices
🛠️
Setup & Troubleshooting
Installation Guide
- Detailed setup instructions
Windows Installation
- Windows-specific setup
Troubleshooting
- Common issues and solutions
Non-Interactive Mode
- CI/CD automation
🤝
Community & Support
GitHub Issues
:
Report bugs or request features
Discord
:
Join the Agentics Foundation community
Wiki
:
Comprehensive documentation
Examples
:
Real-world usage patterns
📊
Performance & Stats
84.8% SWE-Bench solve rate
- Industry-leading problem-solving capability
32.3% token reduction
- Efficient context management
2.8-4.4x speed improvement
- Parallel coordination strategies
64 specialized agents
- Complete development ecosystem
87 MCP tools
- Comprehensive automation toolkit
📊 Targets (Month 12)
5K+ GitHub stars, 50K npm downloads/month
$25K MRR, 15 enterprise customers
90%+ error prevention, 30+ min saved/dev/week
Star History
Built with ❤️ by
rUv
| Powered by Revolutionary AI
v2.5.0-alpha.140 - The Future of AI Orchestration with PreToolUse Modification Hooks
- 今日の獲得スター数: 54
- 累積スター数: 8,772

### References
- https://github.com/ruvnet/claude-flow

## google/langextract

### Executive Summary
- A Python library for extracting structured information from unstructured text using LLMs with precise source grounding and interactive visualization.
- ---
- LangExtract
Table of Contents
Introduction
Why LangExtract?
Quick Start
Installation
API Key Setup for Cloud Models
Adding Custom Model Providers
Using OpenAI Models
Using Local LLMs with Ollama
More Examples
Romeo and Juliet
Full Text Extraction
Medication Extraction
Radiology Report Structuring: RadExtract
Community Providers
Contributing
Testing
Disclaimer
Introduction
LangExtract is a Python library that uses LLMs to extract structured information from unstructured text documents based on user-defined instructions. It processes materials such as clinical notes or reports, identifying and organizing key details while ensuring the extracted data corresponds to the source text.
Why LangExtract?
Precise Source Grounding:
Maps every extraction to its exact location in the source text, enabling visual highlighting for easy traceability and verification.
Reliable Structured Outputs:
Enforces a consistent output schema based on your few-shot examples, leveraging controlled generation in supported models like Gemini to guarantee robust, structured results.
Optimized for Long Documents:
Overcomes the "needle-in-a-haystack" challenge of large document extraction by using an optimized strategy of text chunking, parallel processing, and multiple passes for higher recall.
Interactive Visualization:
Instantly generates a self-contained, interactive HTML file to visualize and review thousands of extracted entities in their original context.
Flexible LLM Support:
Supports your preferred models, from cloud-based LLMs like the Google Gemini family to local open-source models via the built-in Ollama interface.
Adaptable to Any Domain:
Define extraction tasks for any domain using just a few examples. LangExtract adapts to your needs without requiring any model fine-tuning.
Leverages LLM World Knowledge:
Utilize precise prompt wording and few-shot examples to influence how the extraction task may utilize LLM knowledge. The accuracy of any inferred information and its adherence to the task specification are contingent upon the selected LLM, the complexity of the task, the clarity of the prompt instructions, and the nature of the prompt examples.
Quick Start
Note:
Using cloud-hosted models like Gemini requires an API key. See the
API Key Setup
section for instructions on how to get and configure your key.
Extract structured information with just a few lines of code.
1. Define Your Extraction Task
First, create a prompt that clearly describes what you want to extract. Then, provide a high-quality example to guide the model.
import
langextract
as
lx
import
textwrap
# 1. Define the prompt and extraction rules
prompt
=
textwrap
.
dedent
(
"""
\
Extract characters, emotions, and relationships in order of appearance.
Use exact text for extractions. Do not paraphrase or overlap entities.
Provide meaningful attributes for each entity to add context."""
)
# 2. Provide a high-quality example to guide the model
examples
=
[
lx
.
data
.
ExampleData
(
text
=
"ROMEO. But soft! What light through yonder window breaks? It is the east, and Juliet is the sun."
,
extractions
=
[
lx
.
data
.
Extraction
(
extraction_class
=
"character"
,
extraction_text
=
"ROMEO"
,
attributes
=
{
"emotional_state"
:
"wonder"
}
            ),
lx
.
data
.
Extraction
(
extraction_class
=
"emotion"
,
extraction_text
=
"But soft!"
,
attributes
=
{
"feeling"
:
"gentle awe"
}
            ),
lx
.
data
.
Extraction
(
extraction_class
=
"relationship"
,
extraction_text
=
"Juliet is the sun"
,
attributes
=
{
"type"
:
"metaphor"
}
            ),
        ]
    )
]
2. Run the Extraction
Provide your input text and the prompt materials to the
lx.extract
function.
# The input text to be processed
input_text
=
"Lady Juliet gazed longingly at the stars, her heart aching for Romeo"
# Run the extraction
result
=
lx
.
extract
(
text_or_documents
=
input_text
,
prompt_description
=
prompt
,
examples
=
examples
,
model_id
=
"gemini-2.5-flash"
,
)
Model Selection
:
gemini-2.5-flash
is the recommended default, offering an excellent balance of speed, cost, and quality. For highly complex tasks requiring deeper reasoning,
gemini-2.5-pro
may provide superior results. For large-scale or production use, a Tier 2 Gemini quota is suggested to increase throughput and avoid rate limits. See the
rate-limit documentation
for details.
Model Lifecycle
: Note that Gemini models have a lifecycle with defined retirement dates. Users should consult the
official model version documentation
to stay informed about the latest stable and legacy versions.
3. Visualize the Results
The extractions can be saved to a
.jsonl
file, a popular format for working with language model data. LangExtract can then generate an interactive HTML visualization from this file to review the entities in context.
# Save the results to a JSONL file
lx
.
io
.
save_annotated_documents
([
result
],
output_name
=
"extraction_results.jsonl"
,
output_dir
=
"."
)
# Generate the visualization from the file
html_content
=
lx
.
visualize
(
"extraction_results.jsonl"
)
with
open
(
"visualization.html"
,
"w"
)
as
f
:
if
hasattr
(
html_content
,
'data'
):
f
.
write
(
html_content
.
data
)
# For Jupyter/Colab
else
:
f
.
write
(
html_content
)
This creates an animated and interactive HTML file:
Note on LLM Knowledge Utilization:
This example demonstrates extractions that stay close to the text evidence - extracting "longing" for Lady Juliet's emotional state and identifying "yearning" from "gazed longingly at the stars." The task could be modified to generate attributes that draw more heavily from the LLM's world knowledge (e.g., adding
"identity": "Capulet family daughter"
or
"literary_context": "tragic heroine"
). The balance between text-evidence and knowledge-inference is controlled by your prompt instructions and example attributes.
Scaling to Longer Documents
For larger texts, you can process entire documents directly from URLs with parallel processing and enhanced sensitivity:
# Process Romeo & Juliet directly from Project Gutenberg
result
=
lx
.
extract
(
text_or_documents
=
"https://www.gutenberg.org/files/1513/1513-0.txt"
,
prompt_description
=
prompt
,
examples
=
examples
,
model_id
=
"gemini-2.5-flash"
,
extraction_passes
=
3
,
# Improves recall through multiple passes
max_workers
=
20
,
# Parallel processing for speed
max_char_buffer
=
1000
# Smaller contexts for better accuracy
)
This approach can extract hundreds of entities from full novels while maintaining high accuracy. The interactive visualization seamlessly handles large result sets, making it easy to explore hundreds of entities from the output JSONL file.
See the full
Romeo and Juliet
extraction example →
for detailed results and performance insights.
Installation
From PyPI
pip install langextract
Recommended for most users. For isolated environments, consider using a virtual environment:
python -m venv langextract_env
source
langextract_env/bin/activate
#
On Windows: langextract_env\Scripts\activate
pip install langextract
From Source
LangExtract uses modern Python packaging with
pyproject.toml
for dependency management:
Installing with
-e
puts the package in development mode, allowing you to modify the code without reinstalling.
git clone https://github.com/google/langextract.git
cd
langextract
#
For basic installation:
pip install -e
.
#
For development (includes linting tools):
pip install -e
"
.[dev]
"
#
For testing (includes pytest):
pip install -e
"
.[test]
"
Docker
docker build -t langextract
.
docker run --rm -e LANGEXTRACT_API_KEY=
"
your-api-key
"
langextract python your_script.py
API Key Setup for Cloud Models
When using LangExtract with cloud-hosted models (like Gemini or OpenAI), you'll need to
set up an API key. On-device models don't require an API key. For developers
using local LLMs, LangExtract offers built-in support for Ollama and can be
extended to other third-party APIs by updating the inference endpoints.
API Key Sources
Get API keys from:
AI Studio
for Gemini models
Vertex AI
for enterprise use
OpenAI Platform
for OpenAI models
Setting up API key in your environment
Option 1: Environment Variable
export
LANGEXTRACT_API_KEY=
"
your-api-key-here
"
Option 2: .env File (Recommended)
Add your API key to a
.env
file:
#
Add API key to .env file
cat
>>
.env
<<
'
EOF
'
LANGEXTRACT_API_KEY=your-api-key-here
EOF
#
Keep your API key secure
echo
'
.env
'
>>
.gitignore
In your Python code:
import
langextract
as
lx
result
=
lx
.
extract
(
text_or_documents
=
input_text
,
prompt_description
=
"Extract information..."
,
examples
=
[...],
model_id
=
"gemini-2.5-flash"
)
Option 3: Direct API Key (Not Recommended for Production)
You can also provide the API key directly in your code, though this is not recommended for production use:
result
=
lx
.
extract
(
text_or_documents
=
input_text
,
prompt_description
=
"Extract information..."
,
examples
=
[...],
model_id
=
"gemini-2.5-flash"
,
api_key
=
"your-api-key-here"
# Only use this for testing/development
)
Option 4: Vertex AI (Service Accounts)
Use
Vertex AI
for authentication with service accounts:
result
=
lx
.
extract
(
text_or_documents
=
input_text
,
prompt_description
=
"Extract information..."
,
examples
=
[...],
model_id
=
"gemini-2.5-flash"
,
language_model_params
=
{
"vertexai"
:
True
,
"project"
:
"your-project-id"
,
"location"
:
"global"
# or regional endpoint
}
)
Adding Custom Model Providers
LangExtract supports custom LLM providers via a lightweight plugin system. You can add support for new models without changing core code.
Add new model support independently of the core library
Distribute your provider as a separate Python package
Keep custom dependencies isolated
Override or extend built-in providers via priority-based resolution
See the detailed guide in
Provider System Documentation
to learn how to:
Register a provider with
@registry.register(...)
Publish an entry point for discovery
Optionally provide a schema with
get_schema_class()
for structured output
Integrate with the factory via
create_model(...)
Using OpenAI Models
LangExtract supports OpenAI models (requires optional dependency:
pip install langextract[openai]
):
import
langextract
as
lx
result
=
lx
.
extract
(
text_or_documents
=
input_text
,
prompt_description
=
prompt
,
examples
=
examples
,
model_id
=
"gpt-4o"
,
# Automatically selects OpenAI provider
api_key
=
os
.
environ
.
get
(
'OPENAI_API_KEY'
),
fence_output
=
True
,
use_schema_constraints
=
False
)
Note: OpenAI models require
fence_output=True
and
use_schema_constraints=False
because LangExtract doesn't implement schema constraints for OpenAI yet.
Using Local LLMs with Ollama
LangExtract supports local inference using Ollama, allowing you to run models without API keys:
import
langextract
as
lx
result
=
lx
.
extract
(
text_or_documents
=
input_text
,
prompt_description
=
prompt
,
examples
=
examples
,
model_id
=
"gemma2:2b"
,
# Automatically selects Ollama provider
model_url
=
"http://localhost:11434"
,
fence_output
=
False
,
use_schema_constraints
=
False
)
Quick setup:
Install Ollama from
ollama.com
, run
ollama pull gemma2:2b
, then
ollama serve
.
For detailed installation, Docker setup, and examples, see
examples/ollama/
.
More Examples
Additional examples of LangExtract in action:
Romeo and Juliet
Full Text Extraction
LangExtract can process complete documents directly from URLs. This example demonstrates extraction from the full text of
Romeo and Juliet
from Project Gutenberg (147,843 characters), showing parallel processing, sequential extraction passes, and performance optimization for long document processing.
View
Romeo and Juliet
Full Text Example →
Medication Extraction
Disclaimer:
This demonstration is for illustrative purposes of LangExtract's baseline capability only. It does not represent a finished or approved product, is not intended to diagnose or suggest treatment of any disease or condition, and should not be used for medical advice.
LangExtract excels at extracting structured medical information from clinical text. These examples demonstrate both basic entity recognition (medication names, dosages, routes) and relationship extraction (connecting medications to their attributes), showing LangExtract's effectiveness for healthcare applications.
View Medication Examples →
Radiology Report Structuring: RadExtract
Explore RadExtract, a live interactive demo on HuggingFace Spaces that shows how LangExtract can automatically structure radiology reports. Try it directly in your browser with no setup required.
View RadExtract Demo →
Community Providers
Extend LangExtract with custom model providers! Check out our
Community Provider Plugins
registry to discover providers created by the community or add your own.
For detailed instructions on creating a provider plugin, see the
Custom Provider Plugin Example
.
Contributing
Contributions are welcome! See
CONTRIBUTING.md
to get started
with development, testing, and pull requests. You must sign a
Contributor License Agreement
before submitting patches.
Testing
To run tests locally from the source:
#
Clone the repository
git clone https://github.com/google/langextract.git
cd
langextract
#
Install with test dependencies
pip install -e
"
.[test]
"
#
Run all tests
pytest tests
Or reproduce the full CI matrix locally with tox:
tox
#
runs pylint + pytest on Python 3.10 and 3.11
Ollama Integration Testing
If you have Ollama installed locally, you can run integration tests:
#
Test Ollama integration (requires Ollama running with gemma2:2b model)
tox -e ollama-integration
This test will automatically detect if Ollama is available and run real inference tests.
Development
Code Formatting
This project uses automated formatting tools to maintain consistent code style:
#
Auto-format all code
./autoformat.sh
#
Or run formatters separately
isort langextract tests --profile google --line-length 80
pyink langextract tests --config pyproject.toml
Pre-commit Hooks
For automatic formatting checks:
pre-commit install
#
One-time setup
pre-commit run --all-files
#
Manual run
Linting
Run linting before submitting PRs:
pylint --rcfile=.pylintrc langextract tests
See
CONTRIBUTING.md
for full development guidelines.
Disclaimer
This is not an officially supported Google product. If you use
LangExtract in production or publications, please cite accordingly and
acknowledge usage. Use is subject to the
Apache 2.0 License
.
For health-related applications, use of LangExtract is also subject to the
Health AI Developer Foundations Terms of Use
.
Happy Extracting!
- 今日の獲得スター数: 52
- 累積スター数: 16,257

### References
- https://github.com/google/langextract

## vercel/ai

### Executive Summary
- The AI Toolkit for TypeScript. From the creators of Next.js, the AI SDK is a free open-source library for building AI-powered applications and agents
- ---
- AI SDK
The
AI SDK
is a TypeScript toolkit designed to help you build AI-powered applications and agents using popular frameworks like Next.js, React, Svelte, Vue and runtimes like Node.js.
To learn more about how to use the AI SDK, check out our
API Reference
and
Documentation
.
Installation
You will need Node.js 18+ and npm (or another package manager) installed on your local development machine.
npm install ai
Unified Provider Architecture
The AI SDK provides a
unified API
to interact with model providers like
OpenAI
,
Anthropic
,
Google
, and
more
.
npm install @ai-sdk/openai @ai-sdk/anthropic @ai-sdk/google
Alternatively you can use the
Vercel AI Gateway
.
Usage
Generating Text
import
{
generateText
}
from
'ai'
;
const
{
text
}
=
await
generateText
(
{
model
:
'openai/gpt-5'
,
// use Vercel AI Gateway
prompt
:
'What is an agent?'
,
}
)
;
import
{
generateText
}
from
'ai'
;
import
{
openai
}
from
'@ai-sdk/openai'
;
const
{
text
}
=
await
generateText
(
{
model
:
openai
(
'gpt-5'
)
,
// use OpenAI Responses API
prompt
:
'What is an agent?'
,
}
)
;
Generating Structured Data
import
{
generateObject
}
from
'ai'
;
import
{
z
}
from
'zod'
;
const
{
object
}
=
await
generateObject
(
{
model
:
'openai/gpt-4.1'
,
schema
:
z
.
object
(
{
recipe
:
z
.
object
(
{
name
:
z
.
string
(
)
,
ingredients
:
z
.
array
(
z
.
object
(
{
name
:
z
.
string
(
)
,
amount
:
z
.
string
(
)
}
)
)
,
steps
:
z
.
array
(
z
.
string
(
)
)
,
}
)
,
}
)
,
prompt
:
'Generate a lasagna recipe.'
,
}
)
;
Agents
import
{
Agent
}
from
'ai'
;
const
sandboxAgent
=
new
Agent
(
{
model
:
'openai/gpt-5-codex'
,
system
:
'You are an agent with access to a shell environment.'
,
tools
:
{
local_shell
:
openai
.
tools
.
localShell
(
{
execute
:
async
(
{
action
}
)
=>
{
const
[
cmd
,
...
args
]
=
action
.
command
;
const
sandbox
=
await
getSandbox
(
)
;
// Vercel Sandbox
const
command
=
await
sandbox
.
runCommand
(
{
cmd
,
args
}
)
;
return
{
output
:
await
command
.
stdout
(
)
}
;
}
,
}
)
,
}
,
}
)
;
UI Integration
The
AI SDK UI
module provides a set of hooks that help you build chatbots and generative user interfaces. These hooks are framework agnostic, so they can be used in Next.js, React, Svelte, and Vue.
You need to install the package for your framework, e.g.:
npm install @ai-sdk/react
Agent @/agent/image-generation-agent.ts
import
{
openai
}
from
'@ai-sdk/openai'
;
import
{
Agent
,
InferAgentUIMessage
}
from
'ai'
;
export
const
imageGenerationAgent
=
new
Agent
(
{
model
:
openai
(
'gpt-5'
)
,
tools
:
{
image_generation
:
openai
.
tools
.
imageGeneration
(
{
partialImages
:
3
,
}
)
,
}
,
}
)
;
export
type
ImageGenerationAgentMessage
=
InferAgentUIMessage
<
typeof
imageGenerationAgent
>
;
Route (Next.js App Router) @/app/api/chat/route.ts
import
{
imageGenerationAgent
}
from
'@/agent/image-generation-agent'
;
import
{
validateUIMessages
}
from
'ai'
;
export
async
function
POST
(
req
:
Request
)
{
const
{
messages
}
=
await
req
.
json
(
)
;
return
imageGenerationAgent
.
respond
(
{
messages
:
await
validateUIMessages
(
{
messages
}
)
,
}
)
;
}
UI Component for Tool @/component/image-generation-view.tsx
import
{
openai
}
from
'@ai-sdk/openai'
;
import
{
UIToolInvocation
}
from
'ai'
;
export
default
function
ImageGenerationView
(
{
invocation
,
}
:
{
invocation
:
UIToolInvocation
<
ReturnType
<
typeof
openai
.
tools
.
imageGeneration
>
>
;
}
)
{
switch
(
invocation
.
state
)
{
case
'input-available'
:
return
<
div
>
Generating image...
</
div
>
;
case
'output-available'
:
return
<
img
src
=
{
`data:image/png;base64,
${
invocation
.
output
.
result
}
`
}
/>
;
}
}
Page @/app/page.tsx
'use client'
;
import
{
ImageGenerationAgentMessage
}
from
'@/agent/image-generation-agent'
;
import
ImageGenerationView
from
'@/component/image-generation-view'
;
import
{
useChat
}
from
'@ai-sdk/react'
;
export
default
function
Page
(
)
{
const
{
messages
,
status
,
sendMessage
}
=
useChat
<
ImageGenerationAgentMessage
>
(
)
;
const
[
input
,
setInput
]
=
useState
(
''
)
;
const
handleSubmit
=
e
=>
{
e
.
preventDefault
(
)
;
sendMessage
(
{
text
:
input
}
)
;
setInput
(
''
)
;
}
;
return
(
<
div
>
{
messages
.
map
(
message
=>
(
<
div
key
=
{
message
.
id
}
>
<
strong
>
{
`
${
message
.
role
}
: `
}
</
strong
>
{
message
.
parts
.
map
(
(
part
,
index
)
=>
{
switch
(
part
.
type
)
{
case
'text'
:
return
<
div
key
=
{
index
}
>
{
part
.
text
}
</
div
>
;
case
'tool-image_generation'
:
return
<
ImageGenerationView
key
=
{
index
}
invocation
=
{
part
}
/>
;
}
}
)
}
</
div
>
)
)
}
<
form
onSubmit
=
{
handleSubmit
}
>
<
input
value
=
{
input
}
onChange
=
{
e
=>
setInput
(
e
.
target
.
value
)
}
disabled
=
{
status
!==
'ready'
}
/>
</
form
>
</
div
>
)
;
}
Templates
We've built
templates
that include AI SDK integrations for different use cases, providers, and frameworks. You can use these templates to get started with your AI-powered application.
Community
The AI SDK community can be found on
GitHub Discussions
where you can ask questions, voice ideas, and share your projects with other people.
Contributing
Contributions to the AI SDK are welcome and highly appreciated. However, before you jump right into it, we would like you to review our
Contribution Guidelines
to make sure you have smooth experience contributing to AI SDK.
Authors
This library is created by
Vercel
and
Next.js
team members, with contributions from the
Open Source Community
.
- 今日の獲得スター数: 51
- 累積スター数: 18,328

### References
- https://github.com/vercel/ai

## sapientinc/HRM

### Executive Summary
- Hierarchical Reasoning Model Official Release
- ---
- Hierarchical Reasoning Model
Reasoning, the process of devising and executing complex goal-oriented action sequences, remains a critical challenge in AI.
Current large language models (LLMs) primarily employ Chain-of-Thought (CoT) techniques, which suffer from brittle task decomposition, extensive data requirements, and high latency. Inspired by the hierarchical and multi-timescale processing in the human brain, we propose the Hierarchical Reasoning Model (HRM), a novel recurrent architecture that attains significant computational depth while maintaining both training stability and efficiency.
HRM executes sequential reasoning tasks in a single forward pass without explicit supervision of the intermediate process, through two interdependent recurrent modules: a high-level module responsible for slow, abstract planning, and a low-level module handling rapid, detailed computations. With only 27 million parameters, HRM achieves exceptional performance on complex reasoning tasks using only 1000 training samples. The model operates without pre-training or CoT data, yet achieves nearly perfect performance on challenging tasks including complex Sudoku puzzles and optimal path finding in large mazes.
Furthermore, HRM outperforms much larger models with significantly longer context windows on the Abstraction and Reasoning Corpus (ARC), a key benchmark for measuring artificial general intelligence capabilities.
These results underscore HRM’s potential as a transformative advancement toward universal computation and general-purpose reasoning systems.
Join our Discord Community:
https://discord.gg/sapient
Quick Start Guide 🚀
Prerequisites ⚙️
Ensure PyTorch and CUDA are installed. The repo needs CUDA extensions to be built. If not present, run the following commands:
#
Install CUDA 12.6
CUDA_URL=https://developer.download.nvidia.com/compute/cuda/12.6.3/local_installers/cuda_12.6.3_560.35.05_linux.run

wget -q --show-progress --progress=bar:force:noscroll -O cuda_installer.run
$CUDA_URL
sudo sh cuda_installer.run --silent --toolkit --override
export
CUDA_HOME=/usr/local/cuda-12.6
#
Install PyTorch with CUDA 12.6
PYTORCH_INDEX_URL=https://download.pytorch.org/whl/cu126

pip3 install torch torchvision torchaudio --index-url
$PYTORCH_INDEX_URL
#
Additional packages for building extensions
pip3 install packaging ninja wheel setuptools setuptools-scm
Then install FlashAttention. For Hopper GPUs, install FlashAttention 3
git clone git@github.com:Dao-AILab/flash-attention.git
cd
flash-attention/hopper
python setup.py install
For Ampere or earlier GPUs, install FlashAttention 2
pip3 install flash-attn
Install Python Dependencies 🐍
pip install -r requirements.txt
W&B Integration 📈
This project uses
Weights & Biases
for experiment tracking and metric visualization. Ensure you're logged in:
wandb login
Run Experiments
Quick Demo: Sudoku Solver 💻🗲
Train a master-level Sudoku AI capable of solving extremely difficult puzzles on a modern laptop GPU. 🧩
#
Download and build Sudoku dataset
python dataset/build_sudoku_dataset.py --output-dir data/sudoku-extreme-1k-aug-1000  --subsample-size 1000 --num-aug 1000
#
Start training (single GPU, smaller batch size)
OMP_NUM_THREADS=8 python pretrain.py data_path=data/sudoku-extreme-1k-aug-1000 epochs=20000 eval_interval=2000 global_batch_size=384 lr=7e-5 puzzle_emb_lr=7e-5 weight_decay=1.0 puzzle_emb_weight_decay=1.0
Runtime: ~10 hours on a RTX 4070 laptop GPU
Trained Checkpoints 🚧
ARC-AGI-2
Sudoku 9x9 Extreme (1000 examples)
Maze 30x30 Hard (1000 examples)
To use the checkpoints, see Evaluation section below.
Full-scale Experiments 🔵
Experiments below assume an 8-GPU setup.
Dataset Preparation
#
Initialize submodules
git submodule update --init --recursive
#
ARC-1
python dataset/build_arc_dataset.py
#
ARC offical + ConceptARC, 960 examples
#
ARC-2
python dataset/build_arc_dataset.py --dataset-dirs dataset/raw-data/ARC-AGI-2/data --output-dir data/arc-2-aug-1000
#
ARC-2 official, 1120 examples
#
Sudoku-Extreme
python dataset/build_sudoku_dataset.py
#
Full version
python dataset/build_sudoku_dataset.py --output-dir data/sudoku-extreme-1k-aug-1000  --subsample-size 1000 --num-aug 1000
#
1000 examples
#
Maze
python dataset/build_maze_dataset.py
#
1000 examples
Dataset Visualization
Explore the puzzles visually:
Open
puzzle_visualizer.html
in your browser.
Upload the generated dataset folder located in
data/...
.
Launch experiments
Small-sample (1K)
ARC-1:
OMP_NUM_THREADS=8 torchrun --nproc-per-node 8 pretrain.py
Runtime:
~24 hours
ARC-2:
OMP_NUM_THREADS=8 torchrun --nproc-per-node 8 pretrain.py data_path=data/arc-2-aug-1000
Runtime:
~24 hours (checkpoint after 8 hours is often sufficient)
Sudoku Extreme (1k):
OMP_NUM_THREADS=8 torchrun --nproc-per-node 8 pretrain.py data_path=data/sudoku-extreme-1k-aug-1000 epochs=20000 eval_interval=2000 lr=1e-4 puzzle_emb_lr=1e-4 weight_decay=1.0 puzzle_emb_weight_decay=1.0
Runtime:
~10 minutes
Maze 30x30 Hard (1k):
OMP_NUM_THREADS=8 torchrun --nproc-per-node 8 pretrain.py data_path=data/maze-30x30-hard-1k epochs=20000 eval_interval=2000 lr=1e-4 puzzle_emb_lr=1e-4 weight_decay=1.0 puzzle_emb_weight_decay=1.0
Runtime:
~1 hour
Full Sudoku-Hard
OMP_NUM_THREADS=8 torchrun --nproc-per-node 8 pretrain.py data_path=data/sudoku-hard-full epochs=100 eval_interval=10 lr_min_ratio=0.1 global_batch_size=2304 lr=3e-4 puzzle_emb_lr=3e-4 weight_decay=0.1 puzzle_emb_weight_decay=0.1 arch.loss.loss_type=softmax_cross_entropy arch.L_cycles=8 arch.halt_max_steps=8 arch.pos_encodings=learned
Runtime:
~2 hours
Evaluation
Evaluate your trained models:
Check
eval/exact_accuracy
in W&B.
For ARC-AGI, follow these additional steps:
OMP_NUM_THREADS=8 torchrun --nproc-per-node 8 evaluate.py checkpoint=
<
CHECKPOINT_PATH
>
Then use the provided
arc_eval.ipynb
notebook to finalize and inspect your results.
Notes
Small-sample learning typically exhibits accuracy variance of around ±2 points.
For Sudoku-Extreme (1,000-example dataset), late-stage overfitting may cause numerical instability during training and Q-learning. It is advisable to use early stopping once the training accuracy approaches 100%.
Citation 📜
@misc
{
wang2025hierarchicalreasoningmodel
,
title
=
{
Hierarchical Reasoning Model
}
,
author
=
{
Guan Wang and Jin Li and Yuhao Sun and Xing Chen and Changling Liu and Yue Wu and Meng Lu and Sen Song and Yasin Abbasi Yadkori
}
,
year
=
{
2025
}
,
eprint
=
{
2506.21734
}
,
archivePrefix
=
{
arXiv
}
,
primaryClass
=
{
cs.AI
}
,
url
=
{
https://arxiv.org/abs/2506.21734
}
, 
}
- 今日の獲得スター数: 51
- 累積スター数: 10,867

### References
- https://github.com/sapientinc/HRM

## BerriAI/litellm

### Executive Summary
- Python SDK, Proxy Server (LLM Gateway) to call 100+ LLM APIs in OpenAI format - [Bedrock, Azure, OpenAI, VertexAI, Cohere, Anthropic, Sagemaker, HuggingFace, Replicate, Groq]
- ---
- 🚅 LiteLLM
Call all LLM APIs using the OpenAI format [Bedrock, Huggingface, VertexAI, TogetherAI, Azure, OpenAI, Groq etc.]
LiteLLM Proxy Server (LLM Gateway)
|
Hosted Proxy (Preview)
|
Enterprise Tier
LiteLLM manages:
Translate inputs to provider's
completion
,
embedding
, and
image_generation
endpoints
Consistent output
, text responses will always be available at
['choices'][0]['message']['content']
Retry/fallback logic across multiple deployments (e.g. Azure/OpenAI) -
Router
Set Budgets & Rate limits per project, api key, model
LiteLLM Proxy Server (LLM Gateway)
Jump to LiteLLM Proxy (LLM Gateway) Docs
Jump to Supported LLM Providers
🚨
Stable Release:
Use docker images with the
-stable
tag. These have undergone 12 hour load tests, before being published.
More information about the release cycle here
Support for more providers. Missing a provider or LLM Platform, raise a
feature request
.
Usage (
Docs
)
Important
LiteLLM v1.0.0 now requires
openai>=1.0.0
. Migration guide
here
LiteLLM v1.40.14+ now requires
pydantic>=2.0.0
. No changes required.
pip install litellm
from
litellm
import
completion
import
os
## set ENV variables
os
.
environ
[
"OPENAI_API_KEY"
]
=
"your-openai-key"
os
.
environ
[
"ANTHROPIC_API_KEY"
]
=
"your-anthropic-key"
messages
=
[{
"content"
:
"Hello, how are you?"
,
"role"
:
"user"
}]
# openai call
response
=
completion
(
model
=
"openai/gpt-4o"
,
messages
=
messages
)
# anthropic call
response
=
completion
(
model
=
"anthropic/claude-sonnet-4-20250514"
,
messages
=
messages
)
print
(
response
)
Response (OpenAI Format)
{
"id"
:
"
chatcmpl-1214900a-6cdd-4148-b663-b5e2f642b4de
"
,
"created"
:
1751494488
,
"model"
:
"
claude-sonnet-4-20250514
"
,
"object"
:
"
chat.completion
"
,
"system_fingerprint"
:
null
,
"choices"
: [
        {
"finish_reason"
:
"
stop
"
,
"index"
:
0
,
"message"
: {
"content"
:
"
Hello! I'm doing well, thank you for asking. I'm here and ready to help with whatever you'd like to discuss or work on. How are you doing today?
"
,
"role"
:
"
assistant
"
,
"tool_calls"
:
null
,
"function_call"
:
null
}
        }
    ],
"usage"
: {
"completion_tokens"
:
39
,
"prompt_tokens"
:
13
,
"total_tokens"
:
52
,
"completion_tokens_details"
:
null
,
"prompt_tokens_details"
: {
"audio_tokens"
:
null
,
"cached_tokens"
:
0
},
"cache_creation_input_tokens"
:
0
,
"cache_read_input_tokens"
:
0
}
}
Call any model supported by a provider, with
model=<provider_name>/<model_name>
. There might be provider-specific details here, so refer to
provider docs for more information
Async (
Docs
)
from
litellm
import
acompletion
import
asyncio
async
def
test_get_response
():
user_message
=
"Hello, how are you?"
messages
=
[{
"content"
:
user_message
,
"role"
:
"user"
}]
response
=
await
acompletion
(
model
=
"openai/gpt-4o"
,
messages
=
messages
)
return
response
response
=
asyncio
.
run
(
test_get_response
())
print
(
response
)
Streaming (
Docs
)
liteLLM supports streaming the model response back, pass
stream=True
to get a streaming iterator in response.
Streaming is supported for all models (Bedrock, Huggingface, TogetherAI, Azure, OpenAI, etc.)
from
litellm
import
completion
response
=
completion
(
model
=
"openai/gpt-4o"
,
messages
=
messages
,
stream
=
True
)
for
part
in
response
:
print
(
part
.
choices
[
0
].
delta
.
content
or
""
)
# claude sonnet 4
response
=
completion
(
'anthropic/claude-sonnet-4-20250514'
,
messages
,
stream
=
True
)
for
part
in
response
:
print
(
part
)
Response chunk (OpenAI Format)
{
"id"
:
"
chatcmpl-fe575c37-5004-4926-ae5e-bfbc31f356ca
"
,
"created"
:
1751494808
,
"model"
:
"
claude-sonnet-4-20250514
"
,
"object"
:
"
chat.completion.chunk
"
,
"system_fingerprint"
:
null
,
"choices"
: [
        {
"finish_reason"
:
null
,
"index"
:
0
,
"delta"
: {
"provider_specific_fields"
:
null
,
"content"
:
"
Hello
"
,
"role"
:
"
assistant
"
,
"function_call"
:
null
,
"tool_calls"
:
null
,
"audio"
:
null
},
"logprobs"
:
null
}
    ],
"provider_specific_fields"
:
null
,
"stream_options"
:
null
,
"citations"
:
null
}
Logging Observability (
Docs
)
LiteLLM exposes pre defined callbacks to send data to Lunary, MLflow, Langfuse, DynamoDB, s3 Buckets, Helicone, Promptlayer, Traceloop, Athina, Slack
from
litellm
import
completion
## set env variables for logging tools (when using MLflow, no API key set up is required)
os
.
environ
[
"LUNARY_PUBLIC_KEY"
]
=
"your-lunary-public-key"
os
.
environ
[
"HELICONE_API_KEY"
]
=
"your-helicone-auth-key"
os
.
environ
[
"LANGFUSE_PUBLIC_KEY"
]
=
""
os
.
environ
[
"LANGFUSE_SECRET_KEY"
]
=
""
os
.
environ
[
"ATHINA_API_KEY"
]
=
"your-athina-api-key"
os
.
environ
[
"OPENAI_API_KEY"
]
=
"your-openai-key"
# set callbacks
litellm
.
success_callback
=
[
"lunary"
,
"mlflow"
,
"langfuse"
,
"athina"
,
"helicone"
]
# log input/output to lunary, langfuse, supabase, athina, helicone etc
#openai call
response
=
completion
(
model
=
"openai/gpt-4o"
,
messages
=
[{
"role"
:
"user"
,
"content"
:
"Hi 👋 - i'm openai"
}])
LiteLLM Proxy Server (LLM Gateway) - (
Docs
)
Track spend + Load Balance across multiple projects
Hosted Proxy (Preview)
The proxy provides:
Hooks for auth
Hooks for logging
Cost tracking
Rate Limiting
📖 Proxy Endpoints -
Swagger Docs
Quick Start Proxy - CLI
pip install
'
litellm[proxy]
'
Step 1: Start litellm proxy
$ litellm --model huggingface/bigcode/starcoder
#
INFO: Proxy running on http://0.0.0.0:4000
Step 2: Make ChatCompletions Request to Proxy
Important
💡
Use LiteLLM Proxy with Langchain (Python, JS), OpenAI SDK (Python, JS) Anthropic SDK, Mistral SDK, LlamaIndex, Instructor, Curl
import
openai
# openai v1.0.0+
client
=
openai
.
OpenAI
(
api_key
=
"anything"
,
base_url
=
"http://0.0.0.0:4000"
)
# set proxy to base_url
# request sent to model set on litellm proxy, `litellm --model`
response
=
client
.
chat
.
completions
.
create
(
model
=
"gpt-3.5-turbo"
,
messages
=
[
    {
"role"
:
"user"
,
"content"
:
"this is a test request, write a short poem"
}
])
print
(
response
)
Proxy Key Management (
Docs
)
Connect the proxy with a Postgres DB to create proxy keys
#
Get the code
git clone https://github.com/BerriAI/litellm
#
Go to folder
cd
litellm
#
Add the master key - you can change this after setup
echo
'
LITELLM_MASTER_KEY="sk-1234"
'
>
.env
#
Add the litellm salt key - you cannot change this after adding a model
#
It is used to encrypt / decrypt your LLM API Key credentials
#
We recommend - https://1password.com/password-generator/
#
password generator to get a random hash for litellm salt key
echo
'
LITELLM_SALT_KEY="sk-1234"
'
>>
.env
source
.env
#
Start
docker compose up
UI on
/ui
on your proxy server
Set budgets and rate limits across multiple projects
POST /key/generate
Request
curl
'
http://0.0.0.0:4000/key/generate
'
\
--header
'
Authorization: Bearer sk-1234
'
\
--header
'
Content-Type: application/json
'
\
--data-raw
'
{"models": ["gpt-3.5-turbo", "gpt-4", "claude-2"], "duration": "20m","metadata": {"user": "ishaan@berri.ai", "team": "core-infra"}}
'
Expected Response
{
"
key
"
:
"
sk-kdEXbIqZRwEeEiHwdg7sFA
"
,
#
Bearer token
"
expires
"
:
"
2023-11-19T01:38:25.838000+00:00
"
#
datetime object
}
Supported Providers (
Docs
)
Provider
Completion
Streaming
Async Completion
Async Streaming
Async Embedding
Async Image Generation
openai
✅
✅
✅
✅
✅
✅
Meta - Llama API
✅
✅
✅
✅
azure
✅
✅
✅
✅
✅
✅
AI/ML API
✅
✅
✅
✅
✅
✅
aws - sagemaker
✅
✅
✅
✅
✅
aws - bedrock
✅
✅
✅
✅
✅
google - vertex_ai
✅
✅
✅
✅
✅
✅
google - palm
✅
✅
✅
✅
google AI Studio - gemini
✅
✅
✅
✅
mistral ai api
✅
✅
✅
✅
✅
cloudflare AI Workers
✅
✅
✅
✅
CompactifAI
✅
✅
✅
✅
cohere
✅
✅
✅
✅
✅
anthropic
✅
✅
✅
✅
empower
✅
✅
✅
✅
huggingface
✅
✅
✅
✅
✅
replicate
✅
✅
✅
✅
together_ai
✅
✅
✅
✅
openrouter
✅
✅
✅
✅
ai21
✅
✅
✅
✅
baseten
✅
✅
✅
✅
vllm
✅
✅
✅
✅
nlp_cloud
✅
✅
✅
✅
aleph alpha
✅
✅
✅
✅
petals
✅
✅
✅
✅
ollama
✅
✅
✅
✅
✅
deepinfra
✅
✅
✅
✅
perplexity-ai
✅
✅
✅
✅
Groq AI
✅
✅
✅
✅
Deepseek
✅
✅
✅
✅
anyscale
✅
✅
✅
✅
IBM - watsonx.ai
✅
✅
✅
✅
✅
voyage ai
✅
xinference [Xorbits Inference]
✅
FriendliAI
✅
✅
✅
✅
Galadriel
✅
✅
✅
✅
GradientAI
✅
✅
Novita AI
✅
✅
✅
✅
Featherless AI
✅
✅
✅
✅
Nebius AI Studio
✅
✅
✅
✅
✅
Heroku
✅
✅
OVHCloud AI Endpoints
✅
✅
Read the Docs
Run in Developer mode
Services
Setup .env file in root
Run dependant services
docker-compose up db prometheus
Backend
(In root) create virtual environment
python -m venv .venv
Activate virtual environment
source .venv/bin/activate
Install dependencies
pip install -e ".[all]"
Start proxy backend
python litellm/proxy_cli.py
Frontend
Navigate to
ui/litellm-dashboard
Install dependencies
npm install
Run
npm run dev
to start the dashboard
Enterprise
For companies that need better security, user management and professional support
Talk to founders
This covers:
✅
Features under the
LiteLLM Commercial License
:
✅
Feature Prioritization
✅
Custom Integrations
✅
Professional Support - Dedicated discord + slack
✅
Custom SLAs
✅
Secure access with Single Sign-On
Contributing
We welcome contributions to LiteLLM! Whether you're fixing bugs, adding features, or improving documentation, we appreciate your help.
Quick Start for Contributors
This requires poetry to be installed.
git clone https://github.com/BerriAI/litellm.git
cd
litellm
make install-dev
#
Install development dependencies
make format
#
Format your code
make lint
#
Run all linting checks
make test-unit
#
Run unit tests
make format-check
#
Check formatting only
For detailed contributing guidelines, see
CONTRIBUTING.md
.
Code Quality / Linting
LiteLLM follows the
Google Python Style Guide
.
Our automated checks include:
Black
for code formatting
Ruff
for linting and code quality
MyPy
for type checking
Circular import detection
Import safety checks
All these checks must pass before your PR can be merged.
Support / talk with founders
Schedule Demo 👋
Community Discord 💭
Community Slack 💭
Our numbers 📞 +1 (770) 8783-106 / ‭+1 (412) 618-6238‬
Our emails ✉️
ishaan@berri.ai
/
krrish@berri.ai
Why did we build this
Need for simplicity
: Our code started to get extremely complicated managing & translating calls between Azure, OpenAI and Cohere.
Contributors
- 今日の獲得スター数: 42
- 累積スター数: 29,706

### References
- https://github.com/BerriAI/litellm

## astral-sh/ruff

### Executive Summary
- An extremely fast Python linter and code formatter, written in Rust.
- ---
- Ruff
Docs
|
Playground
An extremely fast Python linter and code formatter, written in Rust.
Linting the CPython codebase from scratch.
⚡️ 10-100x faster than existing linters (like Flake8) and formatters (like Black)
🐍 Installable via
pip
🛠️
pyproject.toml
support
🤝 Python 3.13 compatibility
⚖️ Drop-in parity with
Flake8
, isort, and
Black
📦 Built-in caching, to avoid re-analyzing unchanged files
🔧 Fix support, for automatic error correction (e.g., automatically remove unused imports)
📏 Over
800 built-in rules
, with native re-implementations
of popular Flake8 plugins, like flake8-bugbear
⌨️ First-party
editor integrations
for
VS Code
and
more
🌎 Monorepo-friendly, with
hierarchical and cascading configuration
Ruff aims to be orders of magnitude faster than alternative tools while integrating more
functionality behind a single, common interface.
Ruff can be used to replace
Flake8
(plus dozens of plugins),
Black
,
isort
,
pydocstyle
,
pyupgrade
,
autoflake
, and more, all while executing tens or hundreds of
times faster than any individual tool.
Ruff is extremely actively developed and used in major open-source projects like:
Apache Airflow
Apache Superset
FastAPI
Hugging Face
Pandas
SciPy
...and
many more
.
Ruff is backed by
Astral
. Read the
launch post
,
or the original
project announcement
.
Testimonials
Sebastián Ramírez
, creator
of
FastAPI
:
Ruff is so fast that sometimes I add an intentional bug in the code just to confirm it's actually
running and checking the code.
Nick Schrock
, founder of
Elementl
,
co-creator of
GraphQL
:
Why is Ruff a gamechanger? Primarily because it is nearly 1000x faster. Literally. Not a typo. On
our largest module (dagster itself, 250k LOC) pylint takes about 2.5 minutes, parallelized across 4
cores on my M1. Running ruff against our
entire
codebase takes .4 seconds.
Bryan Van de Ven
, co-creator
of
Bokeh
, original author
of
Conda
:
Ruff is ~150-200x faster than flake8 on my machine, scanning the whole repo takes ~0.2s instead of
~20s. This is an enormous quality of life improvement for local dev. It's fast enough that I added
it as an actual commit hook, which is terrific.
Timothy Crosley
,
creator of
isort
:
Just switched my first project to Ruff. Only one downside so far: it's so fast I couldn't believe
it was working till I intentionally introduced some errors.
Tim Abbott
, lead
developer of
Zulip
:
This is just ridiculously fast...
ruff
is amazing.
Table of Contents
For more, see the
documentation
.
Getting Started
Configuration
Rules
Contributing
Support
Acknowledgements
Who's Using Ruff?
License
Getting Started
For more, see the
documentation
.
Installation
Ruff is available as
ruff
on PyPI.
Invoke Ruff directly with
uvx
:
uvx ruff check
#
Lint all files in the current directory.
uvx ruff format
#
Format all files in the current directory.
Or install Ruff with
uv
(recommended),
pip
, or
pipx
:
#
With uv.
uv tool install ruff@latest
#
Install Ruff globally.
uv add --dev ruff
#
Or add Ruff to your project.
#
With pip.
pip install ruff
#
With pipx.
pipx install ruff
Starting with version
0.5.0
, Ruff can be installed with our standalone installers:
#
On macOS and Linux.
curl -LsSf https://astral.sh/ruff/install.sh
|
sh
#
On Windows.
powershell -c
"
irm https://astral.sh/ruff/install.ps1 | iex
"
#
For a specific version.
curl -LsSf https://astral.sh/ruff/0.14.0/install.sh
|
sh
powershell -c
"
irm https://astral.sh/ruff/0.14.0/install.ps1 | iex
"
You can also install Ruff via
Homebrew
,
Conda
,
and with
a variety of other package managers
.
Usage
To run Ruff as a linter, try any of the following:
ruff check
#
Lint all files in the current directory (and any subdirectories).
ruff check path/to/code/
#
Lint all files in `/path/to/code` (and any subdirectories).
ruff check path/to/code/
*
.py
#
Lint all `.py` files in `/path/to/code`.
ruff check path/to/code/to/file.py
#
Lint `file.py`.
ruff check @arguments.txt
#
Lint using an input file, treating its contents as newline-delimited command-line arguments.
Or, to run Ruff as a formatter:
ruff format
#
Format all files in the current directory (and any subdirectories).
ruff format path/to/code/
#
Format all files in `/path/to/code` (and any subdirectories).
ruff format path/to/code/
*
.py
#
Format all `.py` files in `/path/to/code`.
ruff format path/to/code/to/file.py
#
Format `file.py`.
ruff format @arguments.txt
#
Format using an input file, treating its contents as newline-delimited command-line arguments.
Ruff can also be used as a
pre-commit
hook via
ruff-pre-commit
:
-
repo
:
https://github.com/astral-sh/ruff-pre-commit
#
Ruff version.
rev
:
v0.14.0
hooks
:
#
Run the linter.
-
id
:
ruff-check
args
:
[ --fix ]
#
Run the formatter.
-
id
:
ruff-format
Ruff can also be used as a
VS Code extension
or with
various other editors
.
Ruff can also be used as a
GitHub Action
via
ruff-action
:
name
:
Ruff
on
:
[ push, pull_request ]
jobs
:
ruff
:
runs-on
:
ubuntu-latest
steps
:
      -
uses
:
actions/checkout@v4
-
uses
:
astral-sh/ruff-action@v3
Configuration
Ruff can be configured through a
pyproject.toml
,
ruff.toml
, or
.ruff.toml
file (see:
Configuration
, or
Settings
for a complete list of all configuration options).
If left unspecified, Ruff's default configuration is equivalent to the following
ruff.toml
file:
#
Exclude a variety of commonly ignored directories.
exclude
= [
"
.bzr
"
,
"
.direnv
"
,
"
.eggs
"
,
"
.git
"
,
"
.git-rewrite
"
,
"
.hg
"
,
"
.ipynb_checkpoints
"
,
"
.mypy_cache
"
,
"
.nox
"
,
"
.pants.d
"
,
"
.pyenv
"
,
"
.pytest_cache
"
,
"
.pytype
"
,
"
.ruff_cache
"
,
"
.svn
"
,
"
.tox
"
,
"
.venv
"
,
"
.vscode
"
,
"
__pypackages__
"
,
"
_build
"
,
"
buck-out
"
,
"
build
"
,
"
dist
"
,
"
node_modules
"
,
"
site-packages
"
,
"
venv
"
,
]
#
Same as Black.
line-length
=
88
indent-width
=
4
#
Assume Python 3.9
target-version
=
"
py39
"
[
lint
]
#
Enable Pyflakes (`F`) and a subset of the pycodestyle (`E`) codes by default.
select
= [
"
E4
"
,
"
E7
"
,
"
E9
"
,
"
F
"
]
ignore
= []
#
Allow fix for all enabled rules (when `--fix`) is provided.
fixable
= [
"
ALL
"
]
unfixable
= []
#
Allow unused variables when underscore-prefixed.
dummy-variable-rgx
=
"
^(_+|(_+[a-zA-Z0-9_]*[a-zA-Z0-9]+?))$
"
[
format
]
#
Like Black, use double quotes for strings.
quote-style
=
"
double
"
#
Like Black, indent with spaces, rather than tabs.
indent-style
=
"
space
"
#
Like Black, respect magic trailing commas.
skip-magic-trailing-comma
=
false
#
Like Black, automatically detect the appropriate line ending.
line-ending
=
"
auto
"
Note that, in a
pyproject.toml
, each section header should be prefixed with
tool.ruff
. For
example,
[lint]
should be replaced with
[tool.ruff.lint]
.
Some configuration options can be provided via dedicated command-line arguments, such as those
related to rule enablement and disablement, file discovery, and logging level:
ruff check --select F401 --select F403 --quiet
The remaining configuration options can be provided through a catch-all
--config
argument:
ruff check --config
"
lint.per-file-ignores = {'some_file.py' = ['F841']}
"
To opt in to the latest lint rules, formatter style changes, interface updates, and more, enable
preview mode
by setting
preview = true
in your configuration
file or passing
--preview
on the command line. Preview mode enables a collection of unstable
features that may change prior to stabilization.
See
ruff help
for more on Ruff's top-level commands, or
ruff help check
and
ruff help format
for more on the linting and formatting commands, respectively.
Rules
Ruff supports over 800 lint rules
, many of which are inspired by popular tools like Flake8,
isort, pyupgrade, and others. Regardless of the rule's origin, Ruff re-implements every rule in
Rust as a first-party feature.
By default, Ruff enables Flake8's
F
rules, along with a subset of the
E
rules, omitting any
stylistic rules that overlap with the use of a formatter, like
ruff format
or
Black
.
If you're just getting started with Ruff,
the default rule set is a great place to start
: it
catches a wide variety of common errors (like unused imports) with zero configuration.
Beyond the defaults, Ruff re-implements some of the most popular Flake8 plugins and related code
quality tools, including:
autoflake
eradicate
flake8-2020
flake8-annotations
flake8-async
flake8-bandit
(
#1646
)
flake8-blind-except
flake8-boolean-trap
flake8-bugbear
flake8-builtins
flake8-commas
flake8-comprehensions
flake8-copyright
flake8-datetimez
flake8-debugger
flake8-django
flake8-docstrings
flake8-eradicate
flake8-errmsg
flake8-executable
flake8-future-annotations
flake8-gettext
flake8-implicit-str-concat
flake8-import-conventions
flake8-logging
flake8-logging-format
flake8-no-pep420
flake8-pie
flake8-print
flake8-pyi
flake8-pytest-style
flake8-quotes
flake8-raise
flake8-return
flake8-self
flake8-simplify
flake8-slots
flake8-super
flake8-tidy-imports
flake8-todos
flake8-type-checking
flake8-use-pathlib
flynt
(
#2102
)
isort
mccabe
pandas-vet
pep8-naming
pydocstyle
pygrep-hooks
pylint-airflow
pyupgrade
tryceratops
yesqa
For a complete enumeration of the supported rules, see
Rules
.
Contributing
Contributions are welcome and highly appreciated. To get started, check out the
contributing guidelines
.
You can also join us on
Discord
.
Support
Having trouble? Check out the existing issues on
GitHub
,
or feel free to
open a new one
.
You can also ask for help on
Discord
.
Acknowledgements
Ruff's linter draws on both the APIs and implementation details of many other
tools in the Python ecosystem, especially
Flake8
,
Pyflakes
,
pycodestyle
,
pydocstyle
,
pyupgrade
, and
isort
.
In some cases, Ruff includes a "direct" Rust port of the corresponding tool.
We're grateful to the maintainers of these tools for their work, and for all
the value they've provided to the Python community.
Ruff's formatter is built on a fork of Rome's
rome_formatter
,
and again draws on both API and implementation details from
Rome
,
Prettier
, and
Black
.
Ruff's import resolver is based on the import resolution algorithm from
Pyright
.
Ruff is also influenced by a number of tools outside the Python ecosystem, like
Clippy
and
ESLint
.
Ruff is the beneficiary of a large number of
contributors
.
Ruff is released under the MIT license.
Who's Using Ruff?
Ruff is used by a number of major open-source projects and companies, including:
Albumentations
Amazon (
AWS SAM
)
Anki
Anthropic (
Python SDK
)
Apache Airflow
AstraZeneca (
Magnus
)
Babel
Benchling (
Refac
)
Bokeh
Capital One (
datacompy
)
CrowdCent (
NumerBlox
)
Cryptography (PyCA)
CERN (
Indico
)
DVC
Dagger
Dagster
Databricks (
MLflow
)
Dify
FastAPI
Godot
Gradio
Great Expectations
HTTPX
Hatch
Home Assistant
Hugging Face (
Transformers
,
Datasets
,
Diffusers
)
IBM (
Qiskit
)
ING Bank (
popmon
,
probatus
)
Ibis
ivy
JAX
Jupyter
Kraken Tech
LangChain
Litestar
LlamaIndex
Matrix (
Synapse
)
MegaLinter
Meltano (
Meltano CLI
,
Singer SDK
)
Microsoft (
Semantic Kernel
,
ONNX Runtime
,
LightGBM
)
Modern Treasury (
Python SDK
)
Mozilla (
Firefox
)
Mypy
Nautobot
Netflix (
Dispatch
)
Neon
Nokia
NoneBot
NumPyro
ONNX
OpenBB
Open Wine Components
PDM
PaddlePaddle
Pandas
Pillow
Poetry
Polars
PostHog
Prefect (
Python SDK
,
Marvin
)
PyInstaller
PyMC
PyMC-Marketing
pytest
PyTorch
Pydantic
Pylint
PyVista
Reflex
River
Rippling
Robyn
Saleor
Scale AI (
Launch SDK
)
SciPy
Snowflake (
SnowCLI
)
Sphinx
Stable Baselines3
Starlette
Streamlit
The Algorithms
Vega-Altair
Weblate
WordPress (
Openverse
)
ZenML
Zulip
build (PyPA)
cibuildwheel (PyPA)
delta-rs
featuretools
meson-python
nox
pip
Show Your Support
If you're using Ruff, consider adding the Ruff badge to your project's
README.md
:
[
![
Ruff
]
(
https://img.shields.io/endpoint?url=https://raw.githubusercontent.com/astral-sh/ruff/main/assets/badge/v2.json
)]
(
https://github.com/astral-sh/ruff
)
...or
README.rst
:
..
image
::
https://img.shields.io/endpoint?url=https://raw.githubusercontent.com/astral-sh/ruff/main/assets/badge/v2.json
:target:
https://github.com/astral-sh/ruff
:alt:
Ruff
...or, as HTML:
<
a
href
="
https://github.com/astral-sh/ruff
"
>
<
img
src
="
https://img.shields.io/endpoint?url=https://raw.githubusercontent.com/astral-sh/ruff/main/assets/badge/v2.json
"
alt
="
Ruff
"
style
="
max-width:100%;
"
>
</
a
>
License
This repository is licensed under the
MIT License
- 今日の獲得スター数: 41
- 累積スター数: 42,956

### References
- https://github.com/astral-sh/ruff

## JannisX11/blockbench

### Executive Summary
- Blockbench - A low poly 3D model editor
- ---
- Blockbench
Blockbench is a free and open source model editor for low-poly models with pixel art textures.
Models can be exported into standardized formats, to be shared, rendered, 3D-printed, or used in game engines. There are also multiple dedicated formats for Minecraft Java and Bedrock Edition with format-specific features.
Blockbench features a modern and beginner friendly interface, but also offers lots of customization and advanced features for experienced 3D artists. Plugins can extend the functionality of the program even further.
Website and download:
blockbench.net
Contribution
Check out the
Contribution Guidelines
.
Launching Blockbench
To launch Blockbench from source, you can clone the repository, navigate to the correct branch and launch the program in development mode using the instructions below. If you just want to use the latest version, please download the app from the website.
Install
NodeJS
.
Then install all dependencies via
npm install
Bundle the code via
npm run bundle
Finally, launch Blockbench using
npm run dev
Plugins
Blockbench supports Javascript-based plugins. Learn more about creating plugins on
https://www.blockbench.net/wiki/docs/plugin
.
License
The Blockbench source-code is licensed under the GPL license version 3. See
LICENSE.MD
.
Modifications to the source code can be made under the terms of that license.
Blockbench plugins (external scripts) and themes (theme files to customize the design) that interact with the Blockbench API are an exception. Plugins and themes can be created and/or published as open source, proprietary or paid software.
All assets created with Blockbench (models, textures, animations, screenshots etc.) are your own!
- 今日の獲得スター数: 41
- 累積スター数: 4,413

### References
- https://github.com/JannisX11/blockbench

## jgraph/drawio-desktop

### Executive Summary
- Official electron build of draw.io
- ---
- About
drawio-desktop
is a diagramming desktop app based on
Electron
that wraps the
core draw.io editor
.
Download built binaries from the
releases section
.
Can I use this app for free?
Yes, under the apache 2.0 license. If you don't change the code and accept it is provided "as-is", you can use it for any purpose.
Security
draw.io Desktop is designed to be completely isolated from the Internet, apart from the update process. This checks github.com at startup for a newer version and downloads it from an AWS S3 bucket owned by Github. All JavaScript files are self-contained, the Content Security Policy forbids running remotely loaded JavaScript.
No diagram data is ever sent externally, nor do we send any analytics about app usage externally. There is a Content Security Policy in place on the web part of the interface to ensure external transmission cannot happen, even by accident.
Security and isolating the app are the primarily objectives of draw.io desktop. If you ask for anything that involves external connections enabled in the app by default, the answer will be no.
Support
Support is provided on a reasonable business constraints basis, but without anything contractually binding. All support is provided via this repo. There is no private ticketing support for non-paying users.
Purchasing draw.io for Confluence or Jira does not entitle you to commercial support for draw.io desktop.
Developing
draw.io
is a git submodule of
drawio-desktop
. To get both you need to clone recursively:
git clone --recursive https://github.com/jgraph/drawio-desktop.git
To run this:
npm install
(in the root directory of this repo)
[internal use only] export DRAWIO_ENV=dev if you want to develop/debug in dev mode.
npm start
in the root directory of this repo
runs the app. For debugging, use
npm start --enable-logging
.
Note: If a symlink is used to refer to drawio repo (instead of the submodule), then symlink the
node_modules
directory inside
drawio/src/main/webapp
also.
To release:
Update the draw.io sub-module and push the change. Add version tag before pushing to origin.
Wait for the builds to complete (
https://travis-ci.org/jgraph/drawio-desktop
and
https://ci.appveyor.com/project/davidjgraph/drawio-desktop
)
Go to
https://github.com/jgraph/drawio-desktop/releases
, edit the preview release.
Download the windows exe and windows portable, sign them using
signtool sign /a /tr http://rfc3161timestamp.globalsign.com/advanced /td SHA256 c:/path/to/your/file.exe
Re-upload signed file as
draw.io-windows-installer-x.y.z.exe
and
draw.io-windows-no-installer-x.y.z.exe
Add release notes
Publish release
Note
: In Windows release, when using both x64 and is32 as arch, the result is one big file with both archs. This is why we split them.
Local Storage and Session Storage is stored in the AppData folder:
macOS:
~/Library/Application Support/draw.io
Windows:
C:\Users\<USER-NAME>\AppData\Roaming\draw.io\
Not open-contribution
draw.io is closed to contributions (unless a maintainer permits it, which is extremely rare).
The level of complexity of this project means that even simple changes
can break a
lot
of other moving parts. The amount of testing required
is far more than it first seems. If we were to receive a PR, we'd have
to basically throw it away and write it how we want it to be implemented.
We are grateful for community involvement, bug reports, & feature requests. We do
not wish to come off as anything but welcoming, however, we've
made the decision to keep this project closed to contributions for
the long term viability of the project.
- 今日の獲得スター数: 38
- 累積スター数: 57,185

### References
- https://github.com/jgraph/drawio-desktop

## linshenkx/prompt-optimizer

### Executive Summary
- 一款提示词优化器，助力于编写高质量的提示词
- ---
- Prompt Optimizer (提示词优化器) 🚀
English
|
中文
在线体验
|
快速开始
|
常见问题
|
Chrome插件
|
💖赞助支持
开发文档
|
Vercel部署指南
|
MCP部署使用说明
|
DeepWiki文档
|
ZRead文档
📖 项目简介
Prompt Optimizer是一个强大的AI提示词优化工具，帮助你编写更好的AI提示词，提升AI输出质量。支持Web应用、桌面应用、Chrome插件和Docker部署四种使用方式。
🎥 功能演示
1. 角色扮演对话：激发小模型潜力
在追求成本效益的生产或注重隐私的本地化场景中，结构化的提示词能让小模型稳定地进入角色，提供沉浸式、高一致性的角色扮演体验，有效激发其潜力。
2. 知识图谱提取：保障生产环境的稳定性
在需要程序化处理的生产环境中，高质量的提示词能显著降低对模型智能程度的要求，使得更经济的小模型也能稳定输出可靠的指定格式。本工具旨在辅助开发者快速达到此目的，从而加速开发、保障稳定，实现降本增效。
3. 诗歌写作：辅助创意探索与需求定制
当面对一个强大的AI，我们的目标不只是得到一个“好”答案，而是得到一个“我们想要的”独特答案。本工具能帮助用户将一个模糊的灵感（如“写首诗”）细化为具体的需求（关于什么主题、何种意象、何种情感），辅助您探索、发掘并精确表达自己的创意，与AI共创独一无二的作品。
✨ 核心特性
🎯
智能优化
：一键优化提示词，支持多轮迭代改进，提升AI回复准确度
📝
双模式优化
：支持系统提示词优化和用户提示词优化，满足不同使用场景
🔄
对比测试
：支持原始提示词和优化后提示词的实时对比，直观展示优化效果
🤖
多模型集成
：支持OpenAI、Gemini、DeepSeek、智谱AI、SiliconFlow等主流AI模型
🖼️
图像生成
：支持文生图（T2I）和图生图（I2I），集成Gemini、Seedream等图像模型
📊
高级测试模式
：上下文变量管理、多轮会话测试、工具调用（Function Calling）支持
🔒
安全架构
：纯客户端处理，数据直接与AI服务商交互，不经过中间服务器
📱
多端支持
：同时提供Web应用、桌面应用、Chrome插件和Docker部署四种使用方式
🔐
访问控制
：支持密码保护功能，保障部署安全
🧩
MCP协议支持
：支持Model Context Protocol (MCP) 协议，可与Claude Desktop等MCP兼容应用集成
🚀 高级功能
图像生成模式
🖼️
文生图（T2I）
：通过文本提示词生成图像
🎨
图生图（I2I）
：基于本地图片进行图像变换和优化
🔌
多模型支持
：集成Gemini、Seedream等主流图像生成模型
⚙️
模型参数
：支持各模型特有参数配置（如尺寸、风格等）
📥
预览与下载
：实时预览生成结果，支持下载保存
高级测试模式
📊
上下文变量管理
：自定义变量、批量替换、变量预览
💬
多轮会话测试
：模拟真实对话场景，测试提示词在多轮交互中的表现
🛠️
工具调用支持
：Function Calling集成，支持OpenAI和Gemini工具调用
🎯
灵活调试
：更强大的提示词测试和调试能力
详细使用说明请查看
图像模式文档
快速开始
1. 使用在线版本（推荐）
直接访问：
https://prompt.always200.com
项目是纯前端项目，所有数据只存储在浏览器本地，不会上传至任何服务器，因此直接使用在线版本也是安全可靠的
2. Vercel部署
方式1：一键部署到自己的Vercel(方便，但后续无法自动更新)：
方式2: Fork项目后在Vercel中导入（推荐，但需参考部署文档进行手动设置）：
先Fork项目到自己的GitHub
然后在Vercel中导入该项目
可跟踪源项目更新，便于同步最新功能和修复
配置环境变量：
ACCESS_PASSWORD
：设置访问密码，启用访问限制
VITE_OPENAI_API_KEY
等：配置各AI服务商的API密钥
更多详细的部署步骤和注意事项，请查看：
Vercel部署指南
3. 下载桌面应用
从
GitHub Releases
下载最新版本。我们为各平台提供
安装程序
和
压缩包
两种格式。
安装程序 (推荐)
: 如
*.exe
,
*.dmg
,
*.AppImage
等。
强烈推荐使用此方式，因为它支持自动更新
。
压缩包
: 如
*.zip
。解压即用，但无法自动更新。
桌面应用核心优势
:
✅
无跨域限制
：作为原生桌面应用，它能彻底摆脱浏览器跨域（CORS）问题的困扰。这意味着您可以直接连接任何AI服务提供商的API，包括本地部署的Ollama或有严格安全策略的商业API，获得最完整、最稳定的功能体验。
✅
自动更新
：通过安装程序（如
.exe
,
.dmg
）安装的版本，能够自动检查并更新到最新版。
✅
独立运行
：无需依赖浏览器，提供更快的响应和更佳的性能。
4. 安装Chrome插件
从Chrome商店安装（由于审批较慢，可能不是最新的）：
Chrome商店地址
点击图标即可打开提示词优化器
5. Docker部署
点击查看 Docker 部署命令
#
运行容器（默认配置）
docker run -d -p 8081:80 --restart unless-stopped --name prompt-optimizer linshen/prompt-optimizer
#
运行容器（配置API密钥和访问密码）
docker run -d -p 8081:80 \
  -e VITE_OPENAI_API_KEY=your_key \
  -e ACCESS_USERNAME=your_username
\
#
可选，默认为"admin"
-e ACCESS_PASSWORD=your_password
\
#
设置访问密码
--restart unless-stopped \
  --name prompt-optimizer \
  linshen/prompt-optimizer
国内镜像
: 如果Docker Hub访问较慢，可以将上述命令中的
linshen/prompt-optimizer
替换为
registry.cn-guangzhou.aliyuncs.com/prompt-optimizer/prompt-optimizer
6. Docker Compose部署
点击查看 Docker Compose 部署步骤
#
1. 克隆仓库
git clone https://github.com/linshenkx/prompt-optimizer.git
cd
prompt-optimizer
#
2. 可选：创建.env文件配置API密钥和访问认证
cp env.local.example .env
#
编辑 .env 文件，填入实际的 API 密钥和配置
#
3. 启动服务
docker compose up -d
#
4. 查看日志
docker compose logs -f
#
5. 访问服务
Web 界面：http://localhost:8081
MCP 服务器：http://localhost:8081/mcp
你还可以直接编辑docker-compose.yml文件，自定义配置：
点击查看 docker-compose.yml 示例
services
:
prompt-optimizer
:
#
使用Docker Hub镜像
image
:
linshen/prompt-optimizer:latest
#
或使用阿里云镜像（国内用户推荐）
#
image: registry.cn-guangzhou.aliyuncs.com/prompt-optimizer/prompt-optimizer:latest
container_name
:
prompt-optimizer
restart
:
unless-stopped
ports
:
      -
"
8081:80
"
#
Web应用端口（包含MCP服务器，通过/mcp路径访问）
environment
:
#
API密钥配置
-
VITE_OPENAI_API_KEY=your_openai_key
-
VITE_GEMINI_API_KEY=your_gemini_key
#
访问控制（可选）
-
ACCESS_USERNAME=admin
-
ACCESS_PASSWORD=your_password
7. MCP Server 使用说明
点击查看 MCP Server 使用说明
Prompt Optimizer 现在支持 Model Context Protocol (MCP) 协议，可以与 Claude Desktop 等支持 MCP 的 AI 应用集成。
当通过 Docker 运行时，MCP Server 会自动启动，并可通过
http://ip:port/mcp
访问。
环境变量配置
MCP Server 需要配置 API 密钥才能正常工作。主要的 MCP 专属配置：
#
MCP 服务器配置
MCP_DEFAULT_MODEL_PROVIDER=openai
#
可选值：openai, gemini, deepseek, siliconflow, zhipu, custom
MCP_LOG_LEVEL=info
#
日志级别
Docker 环境下使用 MCP
在 Docker 环境中，MCP Server 会与 Web 应用一起运行，您可以通过 Web 应用的相同端口访问 MCP 服务，路径为
/mcp
。
例如，如果您将容器的 80 端口映射到主机的 8081 端口：
docker run -d -p 8081:80 \
  -e VITE_OPENAI_API_KEY=your-openai-key \
  -e MCP_DEFAULT_MODEL_PROVIDER=openai \
  --name prompt-optimizer \
  linshen/prompt-optimizer
那么 MCP Server 将可以通过
http://localhost:8081/mcp
访问。
Claude Desktop 集成示例
要在 Claude Desktop 中使用 Prompt Optimizer，您需要在 Claude Desktop 的配置文件中添加服务配置。
找到 Claude Desktop 的配置目录：
Windows:
%APPDATA%\Claude\services
macOS:
~/Library/Application Support/Claude/services
Linux:
~/.config/Claude/services
编辑或创建
services.json
文件，添加以下内容：
{
"services"
: [
    {
"name"
:
"
Prompt Optimizer
"
,
"url"
:
"
http://localhost:8081/mcp
"
}
  ]
}
请确保将
localhost:8081
替换为您实际部署 Prompt Optimizer 的地址和端口。
可用工具
optimize-user-prompt
: 优化用户提示词以提高 LLM 性能
optimize-system-prompt
: 优化系统提示词以提高 LLM 性能
iterate-prompt
: 对已经成熟/完善的提示词进行定向迭代优化
更多详细信息，请查看
MCP 服务器用户指南
。
⚙️ API密钥配置
点击查看API密钥配置方法
方式一：通过界面配置（推荐）
点击界面右上角的"⚙️设置"按钮
选择"模型管理"选项卡
点击需要配置的模型（如OpenAI、Gemini、DeepSeek等）
在弹出的配置框中输入对应的API密钥
点击"保存"即可
支持的模型：OpenAI、Gemini、DeepSeek、Zhipu智谱、SiliconFlow、自定义API（OpenAI兼容接口）
除了API密钥，您还可以在模型配置界面为每个模型单独设置高级LLM参数。这些参数通过一个名为
llmParams
的字段进行配置，它允许您以键值对的形式指定LLM SDK支持的任何参数，从而更精细地控制模型行为。
高级LLM参数配置示例：
OpenAI/兼容API
:
{"temperature": 0.7, "max_tokens": 4096, "timeout": 60000}
Gemini
:
{"temperature": 0.8, "maxOutputTokens": 2048, "topP": 0.95}
DeepSeek
:
{"temperature": 0.5, "top_p": 0.9, "frequency_penalty": 0.1}
有关
llmParams
的更详细说明和配置指南，请参阅
LLM参数配置指南
。
方式二：通过环境变量配置
Docker部署时通过
-e
参数配置环境变量：
-e VITE_OPENAI_API_KEY=your_key
-e VITE_GEMINI_API_KEY=your_key
-e VITE_DEEPSEEK_API_KEY=your_key
-e VITE_ZHIPU_API_KEY=your_key
-e VITE_SILICONFLOW_API_KEY=your_key
#
多自定义模型配置（支持无限数量）
-e VITE_CUSTOM_API_KEY_ollama=dummy_key
-e VITE_CUSTOM_API_BASE_URL_ollama=http://localhost:11434/v1
-e VITE_CUSTOM_API_MODEL_ollama=qwen2.5:7b
📖
详细配置指南
: 查看
多自定义模型配置文档
了解完整的配置方法和高级用法
本地开发
详细文档可查看
开发文档
点击查看本地开发命令
#
1. 克隆项目
git clone https://github.com/linshenkx/prompt-optimizer.git
cd
prompt-optimizer
#
2. 安装依赖
pnpm install
#
3. 启动开发服务
pnpm dev
#
主开发命令：构建core/ui并运行web应用
pnpm dev:web
#
仅运行web应用
pnpm dev:fresh
#
完整重置并重新启动开发环境
🗺️ 开发路线
基础功能开发
Web应用发布
Chrome插件发布
国际化支持
支持系统提示词优化和用户提示词优化
桌面应用发布
MCP服务发布
高级模式：变量管理、上下文测试、工具调用
图像生成：文生图（T2I）和图生图（I2I）支持
支持工作区/项目管理
支持提示词收藏和模板管理
详细的项目状态可查看
项目状态文档
📖 相关文档
文档索引
- 所有文档的索引
技术开发指南
- 技术栈和开发规范
LLM参数配置指南
- 高级LLM参数配置详细说明
项目结构
- 详细的项目结构说明
项目状态
- 当前进度和计划
产品需求
- 产品需求文档
Vercel部署指南
- Vercel部署详细说明
Star History
常见问题
点击查看常见问题解答
API连接问题
Q1: 为什么配置好API密钥后仍然无法连接到模型服务？
A
: 大多数连接失败是由
跨域问题
（CORS）导致的。由于本项目是纯前端应用，浏览器出于安全考虑会阻止直接访问不同源的API服务。模型服务如未正确配置CORS策略，会拒绝来自浏览器的直接请求。
Q2: 如何解决本地Ollama的连接问题？
A
: Ollama完全支持OpenAI标准接口，只需配置正确的跨域策略：
设置环境变量
OLLAMA_ORIGINS=*
允许任意来源的请求
如仍有问题，设置
OLLAMA_HOST=0.0.0.0:11434
监听任意IP地址
Q3: 如何解决商业API（如Nvidia的DS API、字节跳动的火山API）的跨域问题？
A
: 这些平台通常有严格的跨域限制，推荐以下解决方案：
使用桌面版应用
（最推荐）
桌面应用作为原生应用，完全没有跨域限制
可以直接连接任何API服务，包括本地部署的模型
提供最完整、最稳定的功能体验
从
GitHub Releases
下载
使用自部署的API中转服务
（专业方案）
部署如OneAPI、NewAPI等开源API聚合/代理工具
在设置中配置为自定义API端点
请求流向：浏览器→中转服务→模型服务提供商
完全控制安全策略和访问权限
注意
：Web版（包括在线版、Vercel部署、Docker部署）都是纯前端应用，都会受到浏览器CORS限制。只有桌面版或使用API中转服务才能解决跨域问题。
Q4: 我已正确配置本地模型（如Ollama）的跨域策略，为什么使用在线版依然无法连接？
A
: 这是由浏览器的
混合内容（Mixed Content）安全策略
导致的。出于安全考虑，浏览器会阻止安全的HTTPS页面（如在线版）向不安全的HTTP地址（如您的本地Ollama服务）发送请求。
解决方案
：
为了绕过此限制，您需要让应用和API处于同一种协议下（例如，都是HTTP）。推荐以下方式：
使用桌面版
：桌面应用没有浏览器限制，是连接本地模型最稳定可靠的方式
使用Docker部署（HTTP）
：通过
http://localhost:8081
访问，与本地Ollama都是HTTP
使用Chrome插件
：插件在某些情况下也可以绕过部分安全限制
🤝 参与贡献
点击查看贡献指南
Fork 本仓库
创建特性分支 (
git checkout -b feature/AmazingFeature
)
提交更改 (
git commit -m '添加某个特性'
)
推送到分支 (
git push origin feature/AmazingFeature
)
提交 Pull Request
提示：使用cursor工具开发时，建议在提交前:
使用"code_review"规则进行代码审查
按照审查报告格式检查:
变更的整体一致性
代码质量和实现方式
测试覆盖情况
文档完善程度
根据审查结果进行优化后再提交
👏 贡献者名单
感谢所有为项目做出贡献的开发者！
📄 开源协议
本项目采用
MIT
协议开源。
如果这个项目对你有帮助，请考虑给它一个 Star ⭐️
👥 联系我们
提交 Issue
发起 Pull Request
加入讨论组
- 今日の獲得スター数: 36
- 累積スター数: 15,876

### References
- https://github.com/linshenkx/prompt-optimizer

## keycloak/keycloak

### Executive Summary
- Open Source Identity and Access Management For Modern Applications and Services
- ---
- Open Source Identity and Access Management
Add authentication to applications and secure services with minimum effort. No need to deal with storing users or authenticating users.
Keycloak provides user federation, strong authentication, user management, fine-grained authorization, and more.
Help and Documentation
Documentation
User Mailing List
- Mailing list for help and general questions about Keycloak
Join
#keycloak
for general questions, or
#keycloak-dev
on Slack for design and development discussions, by creating an account at
https://slack.cncf.io/
.
Reporting Security Vulnerabilities
If you have found a security vulnerability, please look at the
instructions on how to properly report it
.
Reporting an issue
If you believe you have discovered a defect in Keycloak, please open
an issue
.
Please remember to provide a good summary, description as well as steps to reproduce the issue.
Getting started
To run Keycloak, download the distribution from our
website
. Unzip and run:
bin/kc.[sh|bat] start-dev
Alternatively, you can use the Docker image by running:
docker run quay.io/keycloak/keycloak start-dev
For more details refer to the
Keycloak Documentation
.
Building from Source
To build from source, refer to the
building and working with the code base
guide.
Testing
To run tests, refer to the
running tests
guide.
Writing Tests
To write tests, refer to the
writing tests
guide.
Contributing
Before contributing to Keycloak, please read our
contributing guidelines
. Participation in the Keycloak project is governed by the
CNCF Code of Conduct
.
Joining a
community meeting
is a great way to get involved and help shape the future of Keycloak.
Other Keycloak Projects
Keycloak
- Keycloak Server and Java adapters
Keycloak QuickStarts
- QuickStarts for getting started with Keycloak
Keycloak Node.js Connect
- Node.js adapter for Keycloak
License
Apache License, Version 2.0
- 今日の獲得スター数: 34
- 累積スター数: 30,042

### References
- https://github.com/keycloak/keycloak

## qaiu/netdisk-fast-download

### Executive Summary
- 各类网盘直链解析服务, 已支持蓝奏云/蓝奏优享/小飞机盘/123云盘/移动联通/天翼云等. 支持文件夹分享解析. 体验地址: https://lz.qaiu.top http://www.722shop.top:6401
- ---
- netdisk-fast-download 网盘分享链接云解析服务
QQ群：1017480890
netdisk-fast-download网盘直链云解析(nfd云解析)能把网盘分享下载链接转化为直链，支持多款云盘，已支持蓝奏云/蓝奏云优享/奶牛快传/移动云云空间/小飞机盘/亿方云/123云盘/Cloudreve等，支持加密分享，以及部分网盘文件夹分享。
快速开始
命令行下载分享文件：
curl -LOJ
"
https://lz.qaiu.top/parser?url=https://share.feijipan.com/s/nQOaNRPW&pwd=1234
"
或者使用wget:
wget -O bilibili.mp4
"
https://lz.qaiu.top/parser?url=https://share.feijipan.com/s/nQOaNRPW&pwd=1234
"
或者使用浏览器
直接访问
:
### 调用演示站下载：
https://lz.qaiu.top/parser?url=https://share.feijipan.com/s/nQOaNRPW&pwd=1234  
### 调用演示站预览：
https://nfd-parser.github.io/nfd-preview/preview.html?src=https%3A%2F%2Flz.qaiu.top%2Fparser%3Furl%3Dhttps%3A%2F%2Fshare.feijipan.com%2Fs%2FnQOaNRPW&name=bilibili.mp4&ext=mp4
预览地址
预览地址1
预览地址2
天翼云盘大文件解析限时开放
main分支依赖JDK17, 提供了JDK11分支
main-jdk11
0.1.8及以上版本json接口格式有调整 参考json返回数据格式示例
小飞机解析有IP限制，多数云服务商的大陆IP会被拦截（可以自行配置代理），和本程序无关
注意: 请不要过度依赖lz.qaiu.top预览地址服务，建议本地搭建或者云服务器自行搭建。解析次数过多IP会被部分网盘厂商限制，不推荐做公共解析。
网盘支持情况:
20230905 奶牛云直链做了防盗链，需加入请求头：Referer:
https://cowtransfer.com/
20230824 123云盘解析大文件(>100MB)失效，需要登录
20230722 UC网盘解析失效，需要登录
网盘名称-网盘标识:
蓝奏云-lz
蓝奏云优享-iz
奶牛快传-cow
移动云云空间-ec
小飞机网盘-fj
亿方云-fc
123云盘-ye
115网盘(失效)-p115
118网盘(已停服)-p118
文叔叔-ws
联想乐云-le
QQ邮箱云盘-qqw
QQ闪传-qqsc
城通网盘-ct
网易云音乐分享链接-mnes
酷狗音乐分享链接-mkgs
酷我音乐分享链接-mkws
QQ音乐分享链接-mqqs
咪咕音乐分享链接(开发中)
Cloudreve自建网盘-ce
微雨云存储-pvvy
超星云盘(需要referer: https://pan-yz.chaoxing.com)-pcx
Google云盘-pgd
Onedrive-pod
Dropbox-pdp
iCloud-pic
仅专属版提供
移动云盘-p139
联通云盘-pwo
天翼云盘-p189
API接口说明
your_host指的是您的域名或者IP，实际使用时替换为实际域名或者IP，端口默认6400，可以使用nginx代理来做域名访问。
解析方式分为两种类型直接跳转下载文件和获取下载链接,
每一种都提供了两种接口形式:
通用接口parser?url=
和
网盘标志/分享key拼接的短地址（标志短链）
，所有规则参考示例。
通用接口:
/parser?url=分享链接&pwd=密码
没有分享密码去掉&pwd参数;
标志短链:
/d/网盘标识/分享key@密码
没有分享密码去掉@密码;
直链JSON:
/json/网盘标识/分享key@密码
和
/json/parser?url=分享链接&pwd=密码
网盘标识参考上面网盘支持情况
当带有分享密码时需要加上密码参数(pwd)
移动云云空间,小飞机网盘的加密分享的密码可以忽略
移动云空间分享key取分享链接中的data参数,比如
&data=xxx
的参数就是xxx
API规则:
建议使用UrlEncode编码分享链接
解析并自动302跳转
http://your_host/parser?url=分享链接&pwd=xxx
http://your_host/parser?url=UrlEncode(分享链接)&pwd=xxx
http://your_host/d/网盘标识/分享key@分享密码
获取解析后的直链--JSON格式
http://your_host/json/parser?url=分享链接&pwd=xxx
http://your_host/json/网盘标识/分享key@分享密码
文件夹解析v0.1.8fixed3新增
http://your_host/json/getFileList?url=分享链接&pwd=xxx
json接口说明
1. 文件解析：/json/parser?url=分享链接&pwd=xxx
json返回数据格式示例:
shareKey
:    全局分享key
directLink
:  下载链接
cacheHit
:    是否为缓存链接
expires
:     缓存到期时间
{
"code"
:
200
,
"msg"
:
"
success
"
,
"success"
:
true
,
"count"
:
0
,
"data"
: {
"shareKey"
:
"
lz:xxx
"
,
"directLink"
:
"
下载直链
"
,
"cacheHit"
:
true
,
"expires"
:
"
2024-09-18 01:48:02
"
,
"expiration"
:
1726638482825
},
"timestamp"
:
1726637151902
}
2. 分享链接详情接口 /v2/linkInfo?url=分享链接
{
"code"
:
200
,
"msg"
:
"
success
"
,
"success"
:
true
,
"count"
:
0
,
"data"
: {
"downLink"
:
"
https://lz.qaiu.top/d/fj/xx
"
,
"apiLink"
:
"
https://lz.qaiu.top/json/fj/xx
"
,
"cacheHitTotal"
:
5
,
"parserTotal"
:
2
,
"sumTotal"
:
7
,
"shareLinkInfo"
: {
"shareKey"
:
"
xx
"
,
"panName"
:
"
小飞机网盘
"
,
"type"
:
"
fj
"
,
"sharePassword"
:
"
"
,
"shareUrl"
:
"
https://share.feijipan.com/s/xx
"
,
"standardUrl"
:
"
https://www.feijix.com/s/xx
"
,
"otherParam"
: {
"UA"
:
"
Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/131.0.0.0 Safari/537.36 Edg/131.0.0.0
"
},
"cacheKey"
:
"
fj:xx
"
}
    },
"timestamp"
:
1736489219402
}
3. 文件夹解析(仅支持蓝奏云/蓝奏优享/小飞机网盘)
/v2/getFileList?url=分享链接&pwd=分享密码
{
"code"
:
200
,
"msg"
:
"
success
"
,
"success"
:
true
,
"data"
: [
    {
"fileName"
:
"
xxx
"
,
"fileId"
:
"
xxx
"
,
"fileIcon"
:
null
,
"size"
:
999
,
"sizeStr"
:
"
999 M
"
,
"fileType"
:
"
file/folder
"
,
"filePath"
:
null
,
"createTime"
:
"
17 小时前
"
,
"updateTime"
:
null
,
"createBy"
:
null
,
"description"
:
null
,
"downloadCount"
:
"
下载次数
"
,
"panType"
:
"
lz
"
,
"parserUrl"
:
"
下载链接/文件夹链接
"
,
"extParameters"
:
null
}
  ]
}
4. 解析次数统计接口 /v2/statisticsInfo
{
"code"
:
200
,
"msg"
:
"
success
"
,
"success"
:
true
,
"count"
:
0
,
"data"
: {
"parserTotal"
:
320508
,
"cacheTotal"
:
5957910
,
"total"
:
6278418
},
"timestamp"
:
1736489378770
}
IDEA HttpClient示例:
# 解析并重定向到直链
### 蓝奏云普通分享
# @no-redirect
GET http://127.0.0.1:6400/parser?url=https://lanzoux.com/ia2cntg
### 奶牛快传普通分享
# @no-redirect
GET http://127.0.0.1:6400/parser?url=https://cowtransfer.com/s/9a644fe3e3a748
### 360亿方云加密分享
# @no-redirect
GET http://127.0.0.1:6400/parser?url=https://v2.fangcloud.com/sharing/e5079007dc31226096628870c7&pwd=QAIU

# Rest请求自动302跳转(只提供共享文件Id):
### 蓝奏云普通分享
# @no-redirect
GET http://127.0.0.1:6400/lz/ia2cntg
### 奶牛快传普通分享
# @no-redirect
GET http://127.0.0.1:6400/cow/9a644fe3e3a748
### 360亿方云加密分享
GET http://127.0.0.1:6400/json/fc/e5079007dc31226096628870c7@QAIU


# 解析返回json直链
### 蓝奏云普通分享
GET http://127.0.0.1:6400/json/lz/ia2cntg
### 奶牛快传普通分享
GET http://127.0.0.1:6400/json/cow/9a644fe3e3a748
### 360亿方云加密分享
GET http://127.0.0.1:6400/json/fc/e5079007dc31226096628870c7@QAIU
网盘对比
网盘名称
免登陆下载分享
加密分享
初始网盘空间
单文件大小限制
蓝奏云
√
√
不限空间
100M
奶牛快传
√
X
10G
不限大小
移动云云空间(个人版)
√
√(密码可忽略)
5G(个人)
不限大小
小飞机网盘
√
√(密码可忽略)
10G
不限大小
360亿方云
√
√(密码可忽略)
100G(须实名)
不限大小
123云盘
√
√
2T
100G（>100M需要登录）
文叔叔
√
√
10G
5GB
夸克网盘
x
√
10G
不限大小
UC网盘
x
√
10G
不限大小
打包部署
JDK下载（lz.qaiu.top提供直链云解析服务）
阿里jdk17(Dragonwell17-windows-x86)
阿里jdk17(Dragonwell17-linux-x86)
阿里jdk17(Dragonwell17-linux-aarch64)
解析有效性测试-移动云云空间-阿里jdk17-linux-x86
开发和打包
#
环境要求: Jdk17 + maven;
mvn clean
mvn package
打包好的文件位于 web-service/target/netdisk-fast-download-bin.zip
Linux服务部署
Docker 部署（Main分支）
海外服务器Docker部署
#
创建目录
mkdir -p netdisk-fast-download
cd
netdisk-fast-download
#
拉取镜像
docker pull ghcr.io/qaiu/netdisk-fast-download:latest
#
复制配置文件（或下载仓库web-service\src\main\resources）
docker create --name netdisk-fast-download ghcr.io/qaiu/netdisk-fast-download:latest
docker cp netdisk-fast-download:/app/resources ./resources
docker rm netdisk-fast-download
#
启动容器
docker run -d -it --name netdisk-fast-download -p 6401:6401 --restart unless-stopped -e TZ=Asia/Shanghai -v ./resources:/app/resources -v ./db:/app/db -v ./logs:/app/logs ghcr.io/qaiu/netdisk-fast-download:latest
#
反代6401端口
#
升级容器
docker run --rm -v /var/run/docker.sock:/var/run/docker.sock containrrr/watchtower --cleanup --run-once netdisk-fast-download
国内Docker部署
#
创建目录
mkdir -p netdisk-fast-download
cd
netdisk-fast-download
#
拉取镜像
docker pull ghcr.nju.edu.cn/qaiu/netdisk-fast-download:latest
#
复制配置文件（或下载仓库web-service\src\main\resources）
docker create --name netdisk-fast-download ghcr.nju.edu.cn/qaiu/netdisk-fast-download:latest
docker cp netdisk-fast-download:/app/resources ./resources
docker rm netdisk-fast-download
#
启动容器
docker run -d -it --name netdisk-fast-download -p 6401:6401 --restart unless-stopped -e TZ=Asia/Shanghai -v ./resources:/app/resources -v ./db:/app/db -v ./logs:/app/logs ghcr.nju.edu.cn/qaiu/netdisk-fast-download:latest
#
反代6401端口
#
升级容器
docker run --rm -v /var/run/docker.sock:/var/run/docker.sock containrrr/watchtower --cleanup --run-once netdisk-fast-download
宝塔部署指引 ->
点击进入宝塔部署教程
Linux命令行部署
注意: netdisk-fast-download.service中的ExecStart的路径改为实际路径
cd
~
wget -O netdisk-fast-download.zip https://github.com/qaiu/netdisk-fast-download/releases/download/v0.1.9b7/netdisk-fast-download-bin.zip
unzip netdisk-fast-download-bin.zip
cd
netdisk-fast-download
bash service-install.sh
服务相关命令:
查看服务状态
systemctl status netdisk-fast-download.service
启动服务
systemctl start netdisk-fast-download.service
重启服务
systemctl restart netdisk-fast-download.service
停止服务
systemctl stop netdisk-fast-download.service
开机启动服务
systemctl enable netdisk-fast-download.service
停止开机启动
systemctl disable netdisk-fast-download.service
Windows服务部署
下载并解压releases版本netdisk-fast-download-bin.zip
进入netdisk-fast-download下的bin目录
使用管理员权限运行nfd-service-install.bat
如果不想使用服务运行可以直接运行run.bat
注意: 如果jdk环境变量的java版本不是17请修改nfd-service-template.xml中的java命令的路径改为实际路径
相关配置说明
resources目录下包含服务端配置文件 配置文件自带说明，具体请查看配置文件内容，
app-dev.yml 可以配置解析服务相关信息， 包括端口，域名，缓存时长等
server-proxy.yml 可以配置代理服务运行的相关信息， 包括前端反向代理端口，路径等
ip代理配置说明
有时候解析量很大，IP容易被ban，这时候可以使用其他服务器搭建nfd-proxy代理服务。
修改配置文件：
app-dev.yml
proxy
:
  -
panTypes
:
pgd,pdb,pod
#
网盘标识
type
:
http
#
支持http/socks4/socks5
host
:
127.0.0.1
#
代理IP
port
:
7890
#
端口
username
:
#
用户名
password
:
#
密码
nfd-proxy搭建http代理服务器
参考
https://github.com/nfd-parser/nfd-proxy
0.1.9 开发计划
目录解析(专属版)
带cookie/token参数解析大文件(专属版)
技术栈:
Jdk17+Vert.x4
Core模块集成Vert.x实现类似spring的注解式路由API
Star History
免责声明
用户在使用本项目时，应自行承担风险，并确保其行为符合当地法律法规及网盘服务提供商的使用条款。
开发者不对用户因使用本项目而导致的任何后果负责，包括但不限于数据丢失、隐私泄露、账号封禁或其他任何形式的损害。
支持该项目
开源不易，用爱发电，本项目长期维护如果觉得有帮助, 可以请作者喝杯咖啡, 感谢支持
关于专属版
99元, 提供对小飞机,蓝奏优享大文件解析的支持, 提供天翼云盘,移动云盘,联通云盘的解析支持
199元, 包含部署服务和首页定制, 需提供宝塔环境
可以提供功能定制开发, 加v价格详谈:
qq: 197575894
wechat: imcoding_
- 今日の獲得スター数: 32
- 累積スター数: 2,248

### References
- https://github.com/qaiu/netdisk-fast-download

## helix-editor/helix

### Executive Summary
- A post-modern modal text editor.
- ---
- A
Kakoune
/
Neovim
inspired editor, written in Rust.
The editing model is very heavily based on Kakoune; during development I found
myself agreeing with most of Kakoune's design decisions.
For more information, see the
website
or
documentation
.
All shortcuts/keymaps can be found
in the documentation on the website
.
Troubleshooting
Features
Vim-like modal editing
Multiple selections
Built-in language server support
Smart, incremental syntax highlighting and code editing via tree-sitter
Although it's primarily a terminal-based editor, I am interested in exploring
a custom renderer (similar to Emacs) using wgpu or skulpin.
Note: Only certain languages have indentation definitions at the moment. Check
runtime/queries/<lang>/
for
indents.scm
.
Installation
Installation documentation
.
Contributing
Contributing guidelines can be found
here
.
Getting help
Your question might already be answered on the
FAQ
.
Discuss the project on the community
Matrix Space
(make sure to join
#helix-editor:matrix.org
if you're on a client that doesn't support Matrix Spaces yet).
Credits
Thanks to
@jakenvac
for designing the logo!
- 今日の獲得スター数: 31
- 累積スター数: 40,220

### References
- https://github.com/helix-editor/helix

## Ranchero-Software/NetNewsWire

### Executive Summary
- RSS reader for macOS and iOS.
- ---
- NetNewsWire
NetNewsWire is a free and open-source feed reader for macOS and iOS.
It supports
RSS
,
Atom
,
JSON Feed
, and
RSS-in-JSON
formats.
More info:
https://netnewswire.com/
You can
report bugs and make feature requests
here on GitHub. You can also
read change notes
for current and previous releases.
Here’s
How to Support NetNewsWire
. Spoiler: don’t send money. :)
(NetNewsWire’s Help menu has these links, so you don’t have to remember to come back to this page.)
Community
Join the Slack group
to talk with other NetNewsWire users — and to help out, if you’d like to, by testing, coding, writing, providing feedback, or just helping us think things through. Everybody is welcome and encouraged to join.
Every community member is expected to abide by the
code of conduct
which is included in the
Contributing
page.
Pull Requests
See the
Contributing
page for our process. It’s pretty straightforward.
Building
You can build and test NetNewsWire without a paid developer account.
git clone https://github.com/Ranchero-Software/NetNewsWire.git
You can locally override the Xcode settings for code signing
by creating a
DeveloperSettings.xcconfig
file locally at the appropriate path.
This allows for a pristine project with code signing set up with the appropriate
developer ID and certificates, and for developer to be able to have local settings
without needing to check in anything into source control.
You can do this in one of two ways: using the included
setup.sh
script or by creating the folder structure and file manually.
Using
setup.sh
Open Terminal and
cd
into the NetNewsWire directory.
Run this command to ensure you have execution rights for the script:
chmod +x setup.sh
Execute the script with the following command:
./setup.sh
and complete the answers.
Manually
Make a directory
SharedXcodeSettings
next to where you have this repository.
The directory structure is:
directory/
  SharedXcodeSettings/
    DeveloperSettings.xcconfig
  NetNewsWire/
    NetNewsWire.xcodeproj
Example:
If your NetNewsWire Xcode project file is at:
/Users/name/projects/NetNewsWire/NetNewsWire.xcodeproj
Create your
DeveloperSettings.xcconfig
file at
/Users/name/projects/SharedXcodeSettings/DeveloperSettings.xcconfig
Then create a plain text file in it:
SharedXcodeSettings/DeveloperSettings.xcconfig
and
give it the contents:
CODE_SIGN_IDENTITY = Mac Developer
DEVELOPMENT_TEAM = <Your Team ID>
CODE_SIGN_STYLE = Automatic
ORGANIZATION_IDENTIFIER = <Your Domain Name Reversed>
DEVELOPER_ENTITLEMENTS = -dev
PROVISIONING_PROFILE_SPECIFIER =
Set
DEVELOPMENT_TEAM
to your Apple supplied development team.  You can use Keychain
Access to
find your development team ID
.
Set
ORGANIZATION_IDENTIFIER
to a reversed domain name that you control or have made up.
Note that
PROVISIONING_PROFILE_SPECIFIER
should not have a value associated with it.
You can now open the
NetNewsWire.xccodeproj
in Xcode.
Now you should be able to build without code signing errors and without modifying
the NetNewsWire Xcode project.  This is a special build of NetNewsWire with some
functionality disabled.  This is because we have API keys that can't be stored in the
repository or shared between developers.  Certain account types, like iCloud and Feedly, aren't
enabled and the Reader View isn't enabled because of this.
If you have any problems, we will help you out in Slack (
see above
).
- 今日の獲得スター数: 30
- 累積スター数: 9,152

### References
- https://github.com/Ranchero-Software/NetNewsWire
