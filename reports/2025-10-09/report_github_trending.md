# AI News Report (github-trending)

- Generated at: 2025-10-09T02:06:04Z
- Articles: 31

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
- 今日の獲得スター数: 1,799
- 累積スター数: 5,573

### References
- https://github.com/Stremio/stremio-web

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
- 今日の獲得スター数: 612
- 累積スター数: 3,894

### References
- https://github.com/aandrew-me/ytDownloader

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
- 今日の獲得スター数: 366
- 累積スター数: 44,832

### References
- https://github.com/FlowiseAI/Flowise

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
- 今日の獲得スター数: 329
- 累積スター数: 8,339

### References
- https://github.com/BeehiveInnovations/zen-mcp-server

## trycua/cua

### Executive Summary
- Open-source infrastructure for Computer-Use Agents. Sandboxes, SDKs, and benchmarks to train and evaluate AI agents that can control full desktops (macOS, Linux, Windows).
- ---
- We’re hosting the
Computer-Use Agents SOTA Challenge
at
Hack the North
and online!
Track A (On-site @ UWaterloo)
: Reserved for participants accepted to Hack the North. 🏆 Prize:
YC interview guaranteed
.
Track B (Remote)
: Open to everyone worldwide. 🏆 Prize:
Cash award
.
👉 Sign up here:
trycua.com/hackathon
cua
("koo-ah") is Docker for
Computer-Use Agents
- it enables AI agents to control full operating systems in virtual containers and deploy them locally or to the cloud.
vibe-photoshop.mp4
With the Computer SDK, you can:
automate Windows, Linux, and macOS VMs with a consistent,
pyautogui-like API
create & manage VMs
locally
or using
cua cloud
With the Agent SDK, you can:
run computer-use models with a
consistent schema
benchmark on OSWorld-Verified, SheetBench-V2, and more
with a single line of code using HUD
(
Notebook
)
combine UI grounding models with any LLM using
composed agents
use new UI agent models and UI grounding models from the Model Zoo below with just a model string (e.g.,
ComputerAgent(model="openai/computer-use-preview")
)
use API or local inference by changing a prefix (e.g.,
openai/
,
openrouter/
,
ollama/
,
huggingface-local/
,
mlx/
,
etc.
)
CUA Model Zoo 🐨
All-in-one CUAs
UI Grounding Models
UI Planning Models
anthropic/claude-sonnet-4-5-20250929
huggingface-local/xlangai/OpenCUA-{7B,32B}
any all-in-one CUA
openai/computer-use-preview
huggingface-local/HelloKKMe/GTA1-{7B,32B,72B}
any VLM (using liteLLM, requires
tools
parameter)
openrouter/z-ai/glm-4.5v
huggingface-local/Hcompany/Holo1.5-{3B,7B,72B}
any LLM (using liteLLM, requires
moondream3+
prefix )
huggingface-local/OpenGVLab/InternVL3_5-{1B,2B,4B,8B,...}
any all-in-one CUA
huggingface-local/ByteDance-Seed/UI-TARS-1.5-7B
moondream3+{ui planning}
(supports text-only models)
omniparser+{ui planning}
{ui grounding}+{ui planning}
human/human
→
Human-in-the-Loop
Missing a model?
Raise a feature request
or
contribute
!
Quick Start
Get started with a Computer-Use Agent UI
Get started with the Computer-Use Agent CLI
Get started with the Python SDKs
Usage (
Docs
)
pip install cua-agent[all]
from
agent
import
ComputerAgent
agent
=
ComputerAgent
(
model
=
"anthropic/claude-3-5-sonnet-20241022"
,
tools
=
[
computer
],
max_trajectory_budget
=
5.0
)
messages
=
[{
"role"
:
"user"
,
"content"
:
"Take a screenshot and tell me what you see"
}]
async
for
result
in
agent
.
run
(
messages
):
for
item
in
result
[
"output"
]:
if
item
[
"type"
]
==
"message"
:
print
(
item
[
"content"
][
0
][
"text"
])
Output format (OpenAI Agent Responses Format):
{
"output"
: [
# user input
{
"role"
:
"
user
"
,
"content"
:
"
go to trycua on gh
"
},
# first agent turn adds the model output to the history
{
"summary"
: [
            {
"text"
:
"
Searching Firefox for Trycua GitHub
"
,
"type"
:
"
summary_text
"
}
        ],
"type"
:
"
reasoning
"
},
    {
"action"
: {
"text"
:
"
Trycua GitHub
"
,
"type"
:
"
type
"
},
"call_id"
:
"
call_QI6OsYkXxl6Ww1KvyJc4LKKq
"
,
"status"
:
"
completed
"
,
"type"
:
"
computer_call
"
},
# second agent turn adds the computer output to the history
{
"type"
:
"
computer_call_output
"
,
"call_id"
:
"
call_QI6OsYkXxl6Ww1KvyJc4LKKq
"
,
"output"
: {
"type"
:
"
input_image
"
,
"image_url"
:
"
data:image/png;base64,...
"
}
    },
# final agent turn adds the agent output text to the history
{
"type"
:
"
message
"
,
"role"
:
"
assistant
"
,
"content"
: [
          {
"text"
:
"
Success! The Trycua GitHub page has been opened.
"
,
"type"
:
"
output_text
"
}
        ]
    }
  ],
"usage"
: {
"prompt_tokens"
:
150
,
"completion_tokens"
:
75
,
"total_tokens"
:
225
,
"response_cost"
:
0.01
,
  }
}
Computer (
Docs
)
pip install cua-computer[all]
from
computer
import
Computer
async
with
Computer
(
os_type
=
"linux"
,
provider_type
=
"cloud"
,
name
=
"your-container-name"
,
api_key
=
"your-api-key"
)
as
computer
:
# Take screenshot
screenshot
=
await
computer
.
interface
.
screenshot
()
# Click and type
await
computer
.
interface
.
left_click
(
100
,
100
)
await
computer
.
interface
.
type
(
"Hello!"
)
Resources
How to use the MCP Server with Claude Desktop or other MCP clients
- One of the easiest ways to get started with Cua
How to use OpenAI Computer-Use, Anthropic, OmniParser, or UI-TARS for your Computer-Use Agent
How to use Lume CLI for managing desktops
Training Computer-Use Models: Collecting Human Trajectories with Cua (Part 1)
Modules
Module
Description
Installation
Lume
VM management for macOS/Linux using Apple's Virtualization.Framework
curl -fsSL https://raw.githubusercontent.com/trycua/cua/main/libs/lume/scripts/install.sh | bash
Lumier
Docker interface for macOS and Linux VMs
docker pull trycua/lumier:latest
Computer (Python)
Python Interface for controlling virtual machines
pip install "cua-computer[all]"
Computer (Typescript)
Typescript Interface for controlling virtual machines
npm install @trycua/computer
Agent
AI agent framework for automating tasks
pip install "cua-agent[all]"
MCP Server
MCP server for using CUA with Claude Desktop
pip install cua-mcp-server
SOM
Self-of-Mark library for Agent
pip install cua-som
Computer Server
Server component for Computer
pip install cua-computer-server
Core (Python)
Python Core utilities
pip install cua-core
Core (Typescript)
Typescript Core utilities
npm install @trycua/core
Community
Join our
Discord community
to discuss ideas, get assistance, or share your demos!
License
Cua is open-sourced under the MIT License - see the
LICENSE
file for details.
Portions of this project, specifically components adapted from Kasm Technologies Inc., are also licensed under the MIT License. See
libs/kasm/LICENSE
for details.
Microsoft's OmniParser, which is used in this project, is licensed under the Creative Commons Attribution 4.0 International License (CC-BY-4.0). See the
OmniParser LICENSE
for details.
Third-Party Licenses and Optional Components
Some optional extras for this project depend on third-party packages that are licensed under terms different from the MIT License.
The optional "omni" extra (installed via
pip install "cua-agent[omni]"
) installs the
cua-som
module, which includes
ultralytics
and is licensed under the AGPL-3.0.
When you choose to install and use such optional extras, your use, modification, and distribution of those third-party components are governed by their respective licenses (e.g., AGPL-3.0 for
ultralytics
).
Contributing
We welcome contributions to Cua! Please refer to our
Contributing Guidelines
for details.
Trademarks
Apple, macOS, and Apple Silicon are trademarks of Apple Inc.
Ubuntu and Canonical are registered trademarks of Canonical Ltd.
Microsoft is a registered trademark of Microsoft Corporation.
This project is not affiliated with, endorsed by, or sponsored by Apple Inc., Canonical Ltd., Microsoft Corporation, or Kasm Technologies.
Stargazers
Thank you to all our supporters!
- 今日の獲得スター数: 310
- 累積スター数: 10,369

### References
- https://github.com/trycua/cua

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
- 今日の獲得スター数: 304
- 累積スター数: 51,626

### References
- https://github.com/TapXWorld/ChinaTextbook

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
- 今日の獲得スター数: 276
- 累積スター数: 15,755

### References
- https://github.com/openai/openai-agents-python

## Infisical/infisical

### Executive Summary
- Infisical is the open-source platform for secrets management, PKI, and SSH access.
- ---
- The open-source secret management platform
: Sync secrets/configs across your team/infrastructure and prevent secret leaks.
Slack
|
Infisical Cloud
|
Self-Hosting
|
Docs
|
Website
|
Hiring (Remote/SF)
Introduction
Infisical
is the open source secret management platform that teams use to centralize their application configuration and secrets like API keys and database credentials as well as manage their internal PKI.
We're on a mission to make security tooling more accessible to everyone, not just security teams, and that means redesigning the entire developer experience from ground up.
Features
Secrets Management:
Dashboard
: Manage secrets across projects and environments (e.g. development, production, etc.) through a user-friendly interface.
Native Integrations
: Sync secrets to platforms like
GitHub
,
Vercel
,
AWS
, and use tools like
Terraform
,
Ansible
, and more.
Secret versioning
and
Point-in-Time Recovery
: Keep track of every secret and project state; roll back when needed.
Secret Rotation
: Rotate secrets at regular intervals for services like
PostgreSQL
,
MySQL
,
AWS IAM
, and more.
Dynamic Secrets
: Generate ephemeral secrets on-demand for services like
PostgreSQL
,
MySQL
,
RabbitMQ
, and more.
Secret Scanning and Leak Prevention
: Prevent secrets from leaking to git.
Infisical Kubernetes Operator
: Deliver secrets to your Kubernetes workloads and automatically reload deployments.
Infisical Agent
: Inject secrets into applications without modifying any code logic.
Infisical (Internal) PKI:
Private Certificate Authority
: Create CA hierarchies, configure
certificate templates
for policy enforcement, and start issuing X.509 certificates.
Certificate Management
: Manage the certificate lifecycle from
issuance
to
revocation
with support for CRL.
Alerting
: Configure alerting for expiring CA and end-entity certificates.
Infisical PKI Issuer for Kubernetes
: Deliver TLS certificates to your Kubernetes workloads with automatic renewal.
Enrollment over Secure Transport
: Enroll and manage certificates via EST protocol.
Infisical Key Management System (KMS):
Cryptographic Keys
: Centrally manage keys across projects through a user-friendly interface or via the API.
Encrypt and Decrypt Data
: Use symmetric keys to encrypt and decrypt data.
Infisical SSH
Signed SSH Certificates
: Issue ephemeral SSH credentials for secure, short-lived, and centralized access to infrastructure.
General Platform:
Authentication Methods
: Authenticate machine identities with Infisical using a cloud-native or platform agnostic authentication method (
Kubernetes Auth
,
GCP Auth
,
Azure Auth
,
AWS Auth
,
OIDC Auth
,
Universal Auth
).
Access Controls
: Define advanced authorization controls for users and machine identities with
RBAC
,
additional privileges
,
temporary access
,
access requests
,
approval workflows
, and more.
Audit logs
: Track every action taken on the platform.
Self-hosting
: Deploy Infisical on-prem or cloud with ease; keep data on your own infrastructure.
Infisical SDK
: Interact with Infisical via client SDKs (
Node
,
Python
,
Go
,
Ruby
,
Java
,
.NET
)
Infisical CLI
: Interact with Infisical via CLI; useful for injecting secrets into local development and CI/CD pipelines.
Infisical API
: Interact with Infisical via API.
Getting started
Check out the
Quickstart Guides
Use Infisical Cloud
Deploy Infisical on premise
The fastest and most reliable way to
get started with Infisical is signing up
for free to
Infisical Cloud
.
View all
deployment options
Run Infisical locally
To set up and run Infisical locally, make sure you have Git and Docker installed on your system. Then run the command for your system:
Linux/macOS:
git clone https://github.com/Infisical/infisical && cd "$(basename $_ .git)" && cp .env.example .env && docker compose -f docker-compose.prod.yml up
Windows Command Prompt:
git clone https://github.com/Infisical/infisical && cd infisical && copy .env.example .env && docker compose -f docker-compose.prod.yml up
Create an account at
http://localhost:80
Scan and prevent secret leaks
On top managing secrets with Infisical, you can also
scan for over 140+ secret types
in your files, directories and git repositories.
To scan your full git history, run:
infisical scan --verbose
Install pre commit hook to scan each commit before you push to your repository
infisical scan install --pre-commit-hook
Learn about Infisical's code scanning feature
here
Open-source vs. paid
This repo available under the
MIT expat license
, with the exception of the
ee
directory which will contain premium enterprise features requiring a Infisical license.
If you are interested in managed Infisical Cloud of self-hosted Enterprise Offering, take a look at
our website
or
book a meeting with us
.
Security
Please do not file GitHub issues or post on our public forum for security vulnerabilities, as they are public!
Infisical takes security issues very seriously. If you have any concerns about Infisical or believe you have uncovered a vulnerability, please get in touch via the e-mail address
security@infisical.com
. In the message, try to provide a description of the issue and ideally a way of reproducing it. The security team will get back to you as soon as possible.
Note that this security address should be used only for undisclosed vulnerabilities. Please report any security problems to us before disclosing it publicly.
Contributing
Whether it's big or small, we love contributions. Check out our guide to see how to
get started
.
Not sure where to get started? You can:
Join our
Slack
, and ask us any questions there.
We are hiring!
If you're reading this, there is a strong chance you like the products we created.
You might also make a great addition to our team. We're growing fast and would love for you to
join us
.
- 今日の獲得スター数: 266
- 累積スター数: 22,291

### References
- https://github.com/Infisical/infisical

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
- 今日の獲得スター数: 219
- 累積スター数: 4,208

### References
- https://github.com/openemr/openemr

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
- 今日の獲得スター数: 210
- 累積スター数: 46,520

### References
- https://github.com/openai/codex

## dyad-sh/dyad

### Executive Summary
- Free, local, open-source AI app builder ✨ v0 / lovable / Bolt alternative 🌟 Star if you like it!
- ---
- Dyad
Dyad is a local, open-source AI app builder. It's fast, private, and fully under your control — like Lovable, v0, or Bolt, but running right on your machine.
More info at:
http://dyad.sh/
🚀 Features
⚡️
Local
: Fast, private and no lock-in.
🛠
Bring your own keys
: Use your own AI API keys — no vendor lock-in.
🖥️
Cross-platform
: Easy to run on Mac or Windows.
📦 Download
No sign-up required. Just download and go.
👉 Download for your platform
🤝 Community
Join our growing community of AI app builders on
Reddit
:
r/dyadbuilders
- share your projects and get help from the community!
🛠️ Contributing
Dyad
is open-source (Apache 2.0 licensed).
If you're interested in contributing to dyad, please read our
contributing
doc.
- 今日の獲得スター数: 201
- 累積スター数: 15,759

### References
- https://github.com/dyad-sh/dyad

## audacity/audacity

### Executive Summary
- Audio Editor
- ---
- Audacity
Audacity
is an easy-to-use, multi-track audio editor and recorder for Windows, macOS, GNU/Linux and other operating systems. More info can be found on
https://www.audacityteam.org
This repository is currently undergoing major structural change.
We're currently working on Audacity 4, which means an entirely new UI and also refactorings aplenty. As such, the
master
branch is currently not particularly friendly to new contributors. It is still possible to submit patches to Audacity 3.x; make sure you branch off
audacity3
if you choose to do so. Build instructions for 3.x can be found
here
; build instructions for Audacity 4 can be found
here
.
You can stay updated with our efforts on
YouTube
,
Discord
and
our blog
.
License
Audacity is open source software licensed GPLv3. Most code files are GPLv2-or-later, with the notable exceptions being
/au3/lib-src
(which contains third party libraries), as well as VST3-related code. Documentation is licensed CC-by 3.0 unless otherwise noted. Details can be found in the
license file
.
- 今日の獲得スター数: 144
- 累積スター数: 15,192

### References
- https://github.com/audacity/audacity

## is-a-dev/register

### Executive Summary
- Grab your own sweet-looking '.is-a.dev' subdomain.
- ---
- is-a.dev
is-a.dev
is a service that allows developers to get a sweet-looking
.is-a.dev
subdomain for their personal websites.
Announcements & Status Updates
Please join our
Discord server
for announcements, updates & upgrades, and downtime notifications regarding the service.
Not all of these will be posted on GitHub
1
, however they will always be posted in our Discord server.
Register
If you want a visual guide, check out
this blog post
.
Fork
this repository.
Read the documentation
.
If you are applying for NS records please read
this
.
Your pull request will be reviewed and merged.
Keep an eye on it in case changes are needed!
After the pull request is merged, your DNS records should be published with-in a few minutes.
Enjoy your new
.is-a.dev
subdomain! Please consider leaving us a star ⭐️ to help support us!
NS Records
When applying for NS records, please be aware we already support a
wide range of DNS records
, so you likely do not need them.
In your PR, please explain why you need NS records, including examples, to help mitigate potential abuse. Refer to the
FAQ
for guidelines on allowed usage.
Pull requests adding NS records without sufficient reasoning will be closed.
Also see:
Why are NS records restricted?
Report Abuse
If you find any subdomains being used for abusive purposes, please report them by
creating an issue
with the relevant evidence.
We are proud to announce that we are supported by Cloudflare's
Project Alexandria
sponsorship program. We would not be able to operate without their help! 💖
Footnotes
We only post announcements on GitHub in the case of a serious incident, which you'll see at the top of this README.
↩
- 今日の獲得スター数: 124
- 累積スター数: 8,486

### References
- https://github.com/is-a-dev/register

## firefly-iii/firefly-iii

### Executive Summary
- Firefly III: a personal finances manager
- ---
- Firefly III
A free and open source personal finance manager
Explore the documentation
View the demo
·
Report a bug
·
Request a feature
·
Ask questions
About Firefly III
Purpose
Features
Who's it for?
The Firefly III eco-system
Getting Started
Contributing
Support the development of Firefly III
License
Do you need help, or do you want to get in touch?
Acknowledgements
About Firefly III
"Firefly III" is a (self-hosted) manager for your personal finances. It can help you keep track of your expenses and income, so you can spend less and save more. Firefly III supports the use of budgets, categories and tags. Using a bunch of external tools, you can import data. It also has many neat financial reports available.
Firefly III should give you
insight
into and
control
over your finances. Money should be useful, not scary. You should be able to
see
where it is going, to
feel
your expenses and to... wow, I'm going overboard with this aren't I?
But you get the idea: this is your money. These are your expenses. Stop them from controlling you. I built this tool because I started to dislike money. Having money, not having money, paying bills with money, you get the idea. But no more. I want to feel "safe", whatever my balance is. And I hope this tool can help you. I know it helps me.
Purpose
Personal financial management is pretty difficult, and everybody has their own approach to it. Some people make budgets, other people limit their cashflow by throwing away their credit cards, others try to increase their current cashflow. There are tons of ways to save and earn money. Firefly III works on the principle that if you know where your money is going, you can stop it from going there.
By keeping track of your expenses and your income you can budget accordingly and save money. Stop living from paycheck to paycheck but give yourself the financial wiggle room you need.
You can read more about the purpose of Firefly III in the
documentation
.
Features
Firefly III is pretty feature packed. Some important stuff first:
It is completely self-hosted and isolated, and will never contact external servers until you explicitly tell it to.
It features a REST JSON API that covers almost every part of Firefly III.
The most exciting features are:
Create
recurring transactions to manage your money
.
Rule based transaction handling
with the ability to create your own rules.
Then the things that make you go "yeah OK, makes sense".
A
double-entry
bookkeeping system.
Save towards a goal using
piggy banks
.
View
income and expense reports
.
And the things you would hope for but not expect:
2 factor authentication for extra security 🔒.
Supports
any currency you want
.
There is a
Docker image
.
And to organise everything:
Clear views that should show you how you're doing.
Easy navigation through your records.
Lots of charts because we all love them.
Many more features are listed in the
documentation
.
Who's it for?
This application is for people who want to track their finances, keep an eye on their money
without having to upload their financial records to the cloud
. You're a bit tech-savvy, you like open source software and you don't mind tinkering with (self-hosted) servers.
The Firefly III eco-system
Several users have built pretty awesome stuff around the Firefly III API.
Check out these tools in the documentation
.
Getting Started
There are many ways to run Firefly III
There is a
demo site
with an example financial administration already present.
You can
install it on your server
.
You can
run it using Docker
.
You can
deploy via Kubernetes
.
You can
install it using Softaculous
.
You can
install it using AMPPS
.
You can
install it on Cloudron
.
You can
install it on Lando
.
You can
install it on Yunohost
.
Contributing
You can contact me at
james@firefly-iii.org
, you may open an issue in the
main repository
or contact me through
gitter
and
Mastodon
.
Of course, there are some
contributing guidelines
and a
code of conduct
, which I invite you to check out.
I can always use your help
squashing bugs
, thinking about
new features
or
translating Firefly III
into other languages.
Sonarcloud
scans the code of Firefly III. If you want to help improve Firefly III, check out the latest reports and take your pick!
There is also a
security policy
.
Support the development of Firefly III
If you like Firefly III and if it helps you save lots of money, why not send me a dime for every dollar saved! 🥳
OK that was a joke. If you feel Firefly III made your life better, please consider contributing as a sponsor. Please check out my
Patreon
and
GitHub Sponsors
page for more information. You can also
buy me a ☕️ coffee at ko-fi.com
. Thank you for your consideration.
License
This work
is licensed
under the
GNU Affero General Public License v3
.
Do you need help, or do you want to get in touch?
Do you want to contact me? You can email me at
james@firefly-iii.org
or get in touch through one of the following support channels:
GitHub Discussions
for questions and support
Gitter.im
for a good chat and a quick answer
GitHub Issues
for bugs and issues
Mastodon
for news and updates
Acknowledgements
Over time,
many people have contributed to Firefly III
. I'm grateful for their support and code contributions.
The Firefly III logo is made by the excellent Cherie Woo.
- 今日の獲得スター数: 110
- 累積スター数: 20,970

### References
- https://github.com/firefly-iii/firefly-iii

## sharkdp/bat

### Executive Summary
- A cat(1) clone with wings.
- ---
- A
cat(1)
clone with syntax highlighting and Git integration.
Key Features
•
How To Use
•
Installation
•
Customization
•
Project goals, alternatives
[English]
  [
中文
]
  [
日本語
]
  [
한국어
]
  [
Русский
]
Sponsors
A special
thank you
goes to our biggest
sponsors
:
Warp, the intelligent terminal
Available on MacOS, Linux, Windows
Graphite is the AI developer productivity platform helping
teams on GitHub ship higher quality software, faster
Syntax highlighting
bat
supports syntax highlighting for a large number of programming and markup
languages:
Git integration
bat
communicates with
git
to show modifications with respect to the index
(see left side bar):
Show non-printable characters
You can use the
-A
/
--show-all
option to show and highlight non-printable
characters:
Automatic paging
By default,
bat
pipes its own output to a pager (e.g.
less
) if the output is too large for one screen.
If you would rather
bat
work like
cat
all the time (never page output), you can set
--paging=never
as an option, either on the command line or in your configuration file.
If you intend to alias
cat
to
bat
in your shell configuration, you can use
alias cat='bat --paging=never'
to preserve the default behavior.
File concatenation
Even with a pager set, you can still use
bat
to concatenate files 😉.
Whenever
bat
detects a non-interactive terminal (i.e. when you pipe into another process or into a file),
bat
will act as a drop-in replacement for
cat
and fall back to printing the plain file contents, regardless of the
--pager
option's value.
How to use
Display a single file on the terminal
bat README.md
Display multiple files at once
bat src/
*
.rs
Read from stdin, determine the syntax automatically (note, highlighting will
only work if the syntax can be determined from the first line of the file,
usually through a shebang such as
#!/bin/sh
)
curl -s https://sh.rustup.rs
|
bat
Read from stdin, specify the language explicitly
yaml2json .travis.yml
|
json_pp
|
bat -l json
Show and highlight non-printable characters:
bat -A /etc/hosts
Use it as a
cat
replacement:
bat
>
note.md
#
quickly create a new file
bat header.md content.md footer.md
>
document.md

bat -n main.rs
#
show line numbers (only)
bat f - g
#
output 'f', then stdin, then 'g'.
Integration with other tools
fzf
You can use
bat
as a previewer for
fzf
. To do this,
use
bat
's
--color=always
option to force colorized output. You can also use
--line-range
option to restrict the load times for long files:
fzf --preview
"
bat --color=always --style=numbers --line-range=:500 {}
"
For more information, see
fzf
's
README
.
find
or
fd
You can use the
-exec
option of
find
to preview all search results with
bat
:
find … -exec bat {} +
If you happen to use
fd
, you can use the
-X
/
--exec-batch
option to do the same:
fd … -X bat
ripgrep
With
batgrep
,
bat
can be used as the printer for
ripgrep
search results.
batgrep needle src/
tail -f
bat
can be combined with
tail -f
to continuously monitor a given file with syntax highlighting.
tail -f /var/log/pacman.log
|
bat --paging=never -l log
Note that we have to switch off paging in order for this to work. We have also specified the syntax
explicitly (
-l log
), as it can not be auto-detected in this case.
git
You can combine
bat
with
git show
to view an older version of a given file with proper syntax
highlighting:
git show v0.6.0:src/main.rs
|
bat -l rs
git diff
You can combine
bat
with
git diff
to view lines around code changes with proper syntax
highlighting:
batdiff
() {
    git diff --name-only --relative --diff-filter=d -z
|
xargs -0 bat --diff
}
If you prefer to use this as a separate tool, check out
batdiff
in
bat-extras
.
If you are looking for more support for git and diff operations, check out
delta
.
xclip
The line numbers and Git modification markers in the output of
bat
can make it hard to copy
the contents of a file. To prevent this, you can call
bat
with the
-p
/
--plain
option or
simply pipe the output into
xclip
:
bat main.cpp
|
xclip
bat
will detect that the output is being redirected and print the plain file contents.
man
bat
can be used as a colorizing pager for
man
, by setting the
MANPAGER
environment variable:
export
MANPAGER=
"
sh -c 'awk '\''{ gsub(/\x1B\[[0-9;]*m/,
\"\"
,
\$
0); gsub(/.\x08/,
\"\"
,
\$
0); print }'\'' | bat -p -lman'
"
man 2
select
(replace
bat
with
batcat
if you are on Debian or Ubuntu)
If you prefer to have this bundled in a new command, you can also use
batman
.
Warning
This will
not work
out of the box with Mandoc's
man
implementation.
Please either use
batman
, or convert the shell script to a
shebang executable
and point
MANPAGER
to that.
Note that the
Manpage syntax
is developed in this repository and still needs some work.
prettier
/
shfmt
/
rustfmt
The
prettybat
script is a wrapper that will format code and print it with
bat
.
Warp
Highlighting
--help
messages
You can use
bat
to colorize help text:
$ cp --help | bat -plhelp
You can also use a wrapper around this:
#
in your .bashrc/.zshrc/*rc
alias
bathelp=
'
bat --plain --language=help
'
help
() {
"
$@
"
--help
2>&1
|
bathelp
}
Then you can do
$ help cp
or
$ help git commit
.
When you are using
zsh
, you can also use global aliases to override
-h
and
--help
entirely:
alias
-g -- -h=
'
-h 2>&1 | bat --language=help --style=plain
'
alias
-g -- --help=
'
--help 2>&1 | bat --language=help --style=plain
'
For
fish
, you can use abbreviations:
abbr
-a
--position
anywhere --
--help
'
--help | bat -plhelp
'
abbr
-a
--position
anywhere --
-h
'
-h | bat -plhelp
'
This way, you can keep on using
cp --help
, but get colorized help pages.
Be aware that in some cases,
-h
may not be a shorthand of
--help
(for example with
ls
). In cases where you need to use
-h
as a command argument you can prepend
\
to the arguement (eg.
ls \-h
) to escape the aliasing defined above.
Please report any issues with the help syntax in
this repository
.
Installation
On Ubuntu (using
apt
)
... and other Debian-based Linux distributions.
bat
is available on
Ubuntu since 20.04 ("Focal")
and
Debian since August 2021 (Debian 11 - "Bullseye")
.
If your Ubuntu/Debian installation is new enough you can simply run:
sudo apt install bat
Important
: If you install
bat
this way, please note that the executable may be installed as
batcat
instead of
bat
(due to
a name
clash with another package
). You can set up a
bat -> batcat
symlink or alias to prevent any issues that may come up because of this and to be consistent with other distributions:
mkdir -p
~
/.local/bin
ln -s /usr/bin/batcat
~
/.local/bin/bat
an example alias for
batcat
as
bat
:
alias
bat=
"
batcat
"
On Ubuntu (using most recent
.deb
packages)
... and other Debian-based Linux distributions.
If the package has not yet been promoted to your Ubuntu/Debian installation, or you want
the most recent release of
bat
, download the latest
.deb
package from the
release page
and install it via:
sudo dpkg -i bat_0.18.3_amd64.deb
#
adapt version number and architecture
On Alpine Linux
You can install
the
bat
package
from the official sources, provided you have the appropriate repository enabled:
apk add bat
On Arch Linux
You can install
the
bat
package
from the official sources:
pacman -S bat
On Fedora
You can install
the
bat
package
from the official
Fedora Modular
repository.
dnf install bat
On Gentoo Linux
You can install
the
bat
package
from the official sources:
emerge sys-apps/bat
On FreeBSD
You can install a precompiled
bat
package
with pkg:
pkg install bat
or build it on your own from the FreeBSD ports:
cd
/usr/ports/textproc/bat
make install
On OpenBSD
You can install
bat
package using
pkg_add(1)
:
pkg_add bat
Via nix
You can install
bat
using the
nix package manager
:
nix-env -i bat
On openSUSE
You can install
bat
with zypper:
zypper install bat
Via snap package
There is currently no recommended snap package available.
Existing packages may be available, but are not officially supported and may contain
issues
.
On macOS (or Linux) via Homebrew
You can install
bat
with
Homebrew
:
brew install bat
On macOS via MacPorts
Or install
bat
with
MacPorts
:
port install bat
On Windows
There are a few options to install
bat
on Windows. Once you have installed
bat
,
take a look at the
"Using
bat
on Windows"
section.
Prerequisites
You will need to install the
Visual C++ Redistributable
With WinGet
You can install
bat
via
WinGet
:
winget install sharkdp.bat
With Chocolatey
You can install
bat
via
Chocolatey
:
choco install bat
With Scoop
You can install
bat
via
scoop
:
scoop install bat
From prebuilt binaries:
You can download prebuilt binaries from the
Release page
,
You will need to install the
Visual C++ Redistributable
package.
From binaries
Check out the
Release page
for
prebuilt versions of
bat
for many different architectures. Statically-linked
binaries are also available: look for archives with
musl
in the file name.
From source
If you want to build
bat
from source, you need Rust 1.74.0 or
higher. You can then use
cargo
to build everything:
From local source
cargo install --path
.
--locked
Note
The
--path .
above specifies the directory of the source code and NOT where
bat
will be installed.
For more information see the docs for
cargo install
.
From
crates.io
cargo install --locked bat
Note that additional files like the man page or shell completion
files can not be installed automatically in both these ways.
If installing from a local source, they will be generated by
cargo
and should be available in the cargo target folder under
build
.
Furthermore, shell completions are also available by running:
bat --completion
<
shell
>
#
see --help for supported shells
Customization
Highlighting theme
Use
bat --list-themes
to get a list of all available themes for syntax
highlighting. By default,
bat
uses
Monokai Extended
or
Monokai Extended Light
for dark and light themes respectively. To select the
TwoDark
theme, call
bat
with the
--theme=TwoDark
option or set the
BAT_THEME
environment variable to
TwoDark
. Use
export BAT_THEME="TwoDark"
in your shell's startup file to
make the change permanent. Alternatively, use
bat
's
configuration file
.
If you want to preview the different themes on a custom file, you can use
the following command (you need
fzf
for this):
bat --list-themes
|
fzf --preview=
"
bat --theme={} --color=always /path/to/file
"
bat
automatically picks a fitting theme depending on your terminal's background color.
You can use the
--theme-dark
/
--theme-light
options or the
BAT_THEME_DARK
/
BAT_THEME_LIGHT
environment variables
to customize the themes used. This is especially useful if you frequently switch between dark and light mode.
You can also use a custom theme by following the
'Adding new themes' section below
.
8-bit themes
bat
has three themes that always use
8-bit colors
,
even when truecolor support is available:
ansi
looks decent on any terminal. It uses 3-bit colors: black, red, green,
yellow, blue, magenta, cyan, and white.
base16
is designed for
base16
terminal themes. It uses
4-bit colors (3-bit colors plus bright variants) in accordance with the
base16 styling guidelines
.
base16-256
is designed for
tinted-shell
.
It replaces certain bright colors with 8-bit colors from 16 to 21.
Do not
use this simply
because you have a 256-color terminal but are not using tinted-shell.
Although these themes are more restricted, they have three advantages over truecolor themes. They:
Enjoy maximum compatibility. Some terminal utilities do not support more than 3-bit colors.
Adapt to terminal theme changes. Even for already printed output.
Visually harmonize better with other terminal software.
Output style
You can use the
--style
option to control the appearance of
bat
's output.
You can use
--style=numbers,changes
, for example, to show only Git changes
and line numbers but no grid and no file header. Set the
BAT_STYLE
environment
variable to make these changes permanent or use
bat
's
configuration file
.
Tip
If you specify a default style in
bat
's config file, you can change which components
are displayed during a single run of
bat
using the
--style
command-line argument.
By prefixing a component with
+
or
-
, it can be added or removed from the current style.
For example, if your config contains
--style=full,-snip
, you can run bat with
--style=-grid,+snip
to remove the grid and add back the
snip
component.
Or, if you want to override the styles completely, you use
--style=numbers
to
only show the line numbers.
Adding new syntaxes / language definitions
Should you find that a particular syntax is not available within
bat
, you can follow these
instructions to easily add new syntaxes to your current
bat
installation.
bat
uses the excellent
syntect
library for syntax highlighting.
syntect
can read any
Sublime Text
.sublime-syntax
file
and theme.
A good resource for finding Sublime Syntax packages is
Package Control
. Once you found a
syntax:
Create a folder with syntax definition files:
mkdir -p
"
$(
bat --config-dir
)
/syntaxes
"
cd
"
$(
bat --config-dir
)
/syntaxes
"
#
Put new '.sublime-syntax' language definition files
#
in this folder (or its subdirectories), for example:
git clone https://github.com/tellnobody1/sublime-purescript-syntax
Now use the following command to parse these files into a binary cache:
bat cache --build
Finally, use
bat --list-languages
to check if the new languages are available.
If you ever want to go back to the default settings, call:
bat cache --clear
If you think that a specific syntax should be included in
bat
by default, please
consider opening a "syntax request" ticket after reading the policies and
instructions
here
:
Open Syntax Request
.
Adding new themes
This works very similar to how we add new syntax definitions.
Note
Themes are stored in
.tmTheme
files
.
First, create a folder with the new syntax highlighting themes:
mkdir -p
"
$(
bat --config-dir
)
/themes
"
cd
"
$(
bat --config-dir
)
/themes
"
#
Download a theme in '.tmTheme' format, for example:
git clone https://github.com/greggb/sublime-snazzy
#
Update the binary cache
bat cache --build
Finally, use
bat --list-themes
to check if the new themes are available.
Note
bat
uses the name of the
.tmTheme
file for the theme's name.
Adding or changing file type associations
You can add new (or change existing) file name patterns using the
--map-syntax
command line option. The option takes an argument of the form
pattern:syntax
where
pattern
is a glob pattern that is matched against the file name and
the absolute file path. The
syntax
part is the full name of a supported language
(use
bat --list-languages
for an overview).
Note:
You probably want to use this option as
an entry in
bat
's configuration file
for persistence instead of passing it on the command line as a one-off. Generally
you'd just use
-l
if you want to manually specify a language for a file.
Example: To use "INI" syntax highlighting for all files with a
.conf
file extension, use
--map-syntax=
'
*.conf:INI
'
Example: To open all files called
.ignore
(exact match) with the "Git Ignore" syntax, use:
--map-syntax=
'
.ignore:Git Ignore
'
Example: To open all
.conf
files in subfolders of
/etc/apache2
with the "Apache Conf"
syntax, use (this mapping is already built in):
--map-syntax=
'
/etc/apache2/**/*.conf:Apache Conf
'
Using a different pager
bat
uses the pager that is specified in the
PAGER
environment variable. If this variable is not
set,
less
is used by default. You can also use bat's built-in pager with
--pager=builtin
or
by setting the
BAT_PAGER
environment variable to "builtin".
If you want to use a different pager, you can either modify the
PAGER
variable or set the
BAT_PAGER
environment variable to override what is specified in
PAGER
.
Note
If
PAGER
is
more
or
most
,
bat
will silently use
less
instead to ensure support for colors.
If you want to pass command-line arguments to the pager, you can also set them via the
PAGER
/
BAT_PAGER
variables:
export
BAT_PAGER=
"
less -RFK
"
Instead of using environment variables, you can also use
bat
's
configuration file
to configure the pager (
--pager
option).
Using
less
as a pager
When using
less
as a pager,
bat
will automatically pass extra options along to
less
to improve the experience. Specifically,
-R
/
--RAW-CONTROL-CHARS
,
-F
/
--quit-if-one-screen
,
-K
/
--quit-on-intr
and under certain conditions,
-X
/
--no-init
and/or
-S
/
--chop-long-lines
.
Important
These options will not be added if:
The pager is not named
less
.
The
--pager
argument contains any command-line arguments (e.g.
--pager="less -R"
).
The
BAT_PAGER
environment variable contains any command-line arguments (e.g.
export BAT_PAGER="less -R"
)
The
--quit-if-one-screen
option will not be added when:
The
--paging=always
argument is used.
The
BAT_PAGING
environment is set to
always
.
The
-R
option is needed to interpret ANSI colors correctly.
The
-F
option instructs
less
to exit immediately if the output size is smaller than
the vertical size of the terminal. This is convenient for small files because you do not
have to press
q
to quit the pager.
The
-K
option instructs
less
to exit immediately when an interrupt signal is received.
This is useful to ensure that
less
quits together with
bat
on SIGINT.
The
-X
option is needed to fix a bug with the
--quit-if-one-screen
feature in versions
of
less
older than version 530. Unfortunately, it also breaks mouse-wheel support in
less
.
If you want to enable mouse-wheel scrolling on older versions of
less
and do not mind losing
the quit-if-one-screen feature, you can set the pager (via
--pager
or
BAT_PAGER
) to
less -R
.
For
less
530 or newer, it should work out of the box.
The
-S
option is added when
bat
's
-S
/
--chop-long-lines
option is used. This tells
less
to truncate any lines larger than the terminal width.
Indentation
bat
expands tabs to 4 spaces by itself, not relying on the pager. To change this, simply add the
--tabs
argument with the number of spaces you want to be displayed.
Note
: Defining tab stops for the pager (via the
--pager
argument by
bat
, or via the
LESS
environment variable for
less
) won't be taken into account because the pager will already get
expanded spaces instead of tabs. This behaviour is added to avoid indentation issues caused by the
sidebar. Calling
bat
with
--tabs=0
will override it and let tabs be consumed by the pager.
Dark mode
If you make use of the dark mode feature in
macOS
, you might want to configure
bat
to use a different
theme based on the OS theme. The following snippet uses the
default
theme when in the
dark mode
and the
GitHub
theme when in the
light mode
.
alias
cat=
"
bat --theme auto:system --theme-dark default --theme-light GitHub
"
The same dark mode feature is now available in
GNOME
and affects the
org.gnome.desktop.interface color-scheme
setting. The following code converts the above to use said setting.
#
.bashrc
sys_color_scheme_is_dark
() {
    condition=
$(
gsettings get org.gnome.desktop.interface color-scheme
)
condition=
$(
echo
"
$condition
"
|
tr -d
"
[:space:]'
"
)
if
[
$condition
==
"
prefer-dark
"
]
;
then
return
0
else
return
1
fi
}
bat_alias_wrapper
() {
#
get color scheme
sys_color_scheme_is_dark
if
[[
$?
-eq
0 ]]
;
then
#
bat command with dark color scheme
bat --theme=default
"
$@
"
else
#
bat command with light color scheme
bat --theme=GitHub
"
$@
"
fi
}
alias
cat=
'
bat_alias_wrapper
'
Configuration file
bat
can also be customized with a configuration file. The location of the file is dependent
on your operating system. To get the default path for your system, call
bat --config-file
Alternatively, you can use
BAT_CONFIG_PATH
or
BAT_CONFIG_DIR
environment variables to point
bat
to a non-default location of the configuration file or the configuration directory respectively:
export
BAT_CONFIG_PATH=
"
/path/to/bat/bat.conf
"
export
BAT_CONFIG_DIR=
"
/path/to/bat
"
A default configuration file can be created with the
--generate-config-file
option.
bat --generate-config-file
There is also now a systemwide configuration file, which is located under
/etc/bat/config
on
Linux and Mac OS and
C:\ProgramData\bat\config
on windows. If the system wide configuration
file is present, the content of the user configuration will simply be appended to it.
Format
The configuration file is a simple list of command line arguments. Use
bat --help
to see a full list of possible options and values. In addition, you can add comments by prepending a line with the
#
character.
Example configuration file:
#
Set the theme to "TwoDark"
--theme=
"
TwoDark
"
#
Show line numbers, Git modifications and file header (but no grid)
--style=
"
numbers,changes,header
"
#
Use italic text on the terminal (not supported on all terminals)
--italic-text=always
#
Use C++ syntax for Arduino .ino files
--map-syntax
"
*.ino:C++
"
Using
bat
on Windows
bat
mostly works out-of-the-box on Windows, but a few features may need extra configuration.
Prerequisites
You will need to install the
Visual C++ Redistributable
package.
Paging
Windows only includes a very limited pager in the form of
more
. You can download a Windows binary
for
less
from its homepage
or
through
Chocolatey
. To use it, place the binary in a directory in
your
PATH
or
define an environment variable
. The
Chocolatey package
installs
less
automatically.
Colors
Windows 10 natively supports colors in both
conhost.exe
(Command Prompt) and PowerShell since
v1511
, as
well as in newer versions of bash. On earlier versions of Windows, you can use
Cmder
, which includes
ConEmu
.
Note:
Old versions of
less
do not correctly interpret colors on Windows. To fix this, you can add the optional Unix tools to your PATH when installing Git. If you don’t have any other pagers installed, you can disable paging entirely by passing
--paging=never
or by setting
BAT_PAGER
to an empty string.
Cygwin
bat
on Windows does not natively support Cygwin's unix-style paths (
/cygdrive/*
). When passed an absolute cygwin path as an argument,
bat
will encounter the following error:
The system cannot find the path specified. (os error 3)
This can be solved by creating a wrapper or adding the following function to your
.bash_profile
file:
bat
() {
local
index
local
args=(
"
$@
"
)
for
index
in
$(
seq 0
${
#
args[@]}
)
;
do
case
"
${args[index]}
"
in
-
*
)
continue
;;
*
)  [
-e
"
${args[index]}
"
]
&&
args[index]=
"
$(
cygpath --windows
"
${args[index]}
"
)
"
;;
esac
done
command
bat
"
${args[@]}
"
}
Troubleshooting
Garbled output
If an input file contains color codes or other ANSI escape sequences or control characters,
bat
will have problems
performing syntax highlighting and text wrapping, and thus the output can become garbled.
If your version of
bat
supports the
--strip-ansi=auto
option, it can be used to remove such sequences
before syntax highlighting. Alternatively, you may disable both syntax highlighting and wrapping by
passing the
--color=never --wrap=never
options to
bat
.
Note
The
auto
option of
--strip-ansi
avoids removing escape sequences when the syntax is plain text.
Terminals & colors
bat
handles terminals
with
and
without
truecolor support. However, the colors in most syntax
highlighting themes are not optimized for 8-bit colors. It is therefore strongly recommended
that you use a terminal with 24-bit truecolor support (
terminator
,
konsole
,
iTerm2
, ...),
or use one of the basic
8-bit themes
designed for a restricted set of colors.
See
this article
for more details and a full list of
terminals with truecolor support.
Make sure that your truecolor terminal sets the
COLORTERM
variable to either
truecolor
or
24bit
. Otherwise,
bat
will not be able to determine whether or not 24-bit escape sequences
are supported (and fall back to 8-bit colors).
Line numbers and grid are hardly visible
Please try a different theme (see
bat --list-themes
for a list). The
OneHalfDark
and
OneHalfLight
themes provide grid and line colors that are brighter.
File encodings
bat
natively supports UTF-8 as well as UTF-16. For every other file encoding, you may need to
convert to UTF-8 first because the encodings can typically not be auto-detected. You can
iconv
to do so.
Example: if you have a PHP file in Latin-1 (ISO-8859-1) encoding, you can call:
iconv -f ISO-8859-1 -t UTF-8 my-file.php
|
bat
Note: you might have to use the
-l
/
--language
option if the syntax can not be auto-detected
by
bat
.
Development
#
Recursive clone to retrieve all submodules
git clone --recursive https://github.com/sharkdp/bat
#
Build (debug version)
cd
bat
cargo build --bins
#
Run unit tests and integration tests
cargo
test
#
Install (release version)
cargo install --path
.
--locked
#
Build a bat binary with modified syntaxes and themes
bash assets/create.sh
cargo install --path
.
--locked --force
If you want to build an application that uses
bat
's pretty-printing
features as a library, check out the
the API documentation
.
Note that you have to use either
regex-onig
or
regex-fancy
as a feature
when you depend on
bat
as a library.
Contributing
Take a look at the
CONTRIBUTING.md
guide.
Maintainers
sharkdp
eth-p
keith-hall
Enselic
Security vulnerabilities
See
SECURITY.md
.
Project goals and alternatives
bat
tries to achieve the following goals:
Provide beautiful, advanced syntax highlighting
Integrate with Git to show file modifications
Be a drop-in replacement for (POSIX)
cat
Offer a user-friendly command-line interface
There are a lot of alternatives, if you are looking for similar programs. See
this document
for a comparison.
License
Copyright (c) 2018-2025
bat-developers
.
bat
is made available under the terms of either the MIT License or the Apache License 2.0, at your option.
See the
LICENSE-APACHE
and
LICENSE-MIT
files for license details.
- 今日の獲得スター数: 97
- 累積スター数: 54,887

### References
- https://github.com/sharkdp/bat

## shadcn-ui/ui

### Executive Summary
- A set of beautifully-designed, accessible components and a code distribution platform. Works with your favorite frameworks. Open Source. Open Code.
- ---
- shadcn/ui
Accessible and customizable components that you can copy and paste into your apps. Free. Open Source.
Use this to build your own component library
.
Documentation
Visit
http://ui.shadcn.com/docs
to view the documentation.
Contributing
Please read the
contributing guide
.
License
Licensed under the
MIT license
.
- 今日の獲得スター数: 91
- 累積スター数: 96,851

### References
- https://github.com/shadcn-ui/ui

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
- 今日の獲得スター数: 88
- 累積スター数: 8,601

### References
- https://github.com/MODSetter/SurfSense

## jdx/mise

### Executive Summary
- dev tools, env vars, task runner
- ---
- mise-en-place
The front-end to your dev env
Getting Started
•
Documentation
•
Dev Tools
•
Environments
•
Tasks
What is it?
Like
asdf
(or
nvm
or
pyenv
but for any language) it manages
dev tools
like node, python, cmake, terraform, and
hundreds more
.
Like
direnv
it manages
environment variables
for different project directories.
Like
make
it manages
tasks
used to build and test projects.
Demo
The following demo shows how to install and use
mise
to manage multiple versions of
node
on the same system.
Note that calling
which node
gives us a real path to node, not a shim.
It also shows that you can use
mise
to install and many other tools such as
jq
,
terraform
, or
go
.
See
demo transcript
.
Quickstart
Install mise
See
Getting started
for more options.
$
curl https://mise.run
|
sh
$
~
/.local/bin/mise --version
2025.10.6 macos-arm64 (a1b2d3e 2025-10-08)
Hook mise into your shell (pick the right one for your shell):
#
note this assumes mise is located at
~
/.local/bin/mise
#
which is what https://mise.run does by default
echo 'eval "$(~/.local/bin/mise activate bash)"' >> ~/.bashrc
echo 'eval "$(~/.local/bin/mise activate zsh)"' >> ~/.zshrc
echo '~/.local/bin/mise activate fish | source' >> ~/.config/fish/config.fish
echo '~/.local/bin/mise activate pwsh | Out-String | Invoke-Expression' >> ~/.config/powershell/Microsoft.PowerShell_profile.ps1
Execute commands with specific tools
$
mise
exec
node@22 -- node -v
mise node@22.x.x ✓ installed
v22.x.x
Install tools
$
mise use --global node@22 go@1
$
node -v
v22.x.x
$
go version
go version go1.x.x macos/arm64
See
dev tools
for more examples.
Manage environment variables
#
mise.toml
[
env
]
SOME_VAR
=
"
foo
"
$
mise
set
SOME_VAR=bar
$
echo
$SOME_VAR
bar
Note that
mise
can also
load
.env
files
.
Run tasks
#
mise.toml
[
tasks
.
build
]
description
=
"
build the project
"
run
=
"
echo building...
"
$
mise run build
building...
See
tasks
for more information.
Example mise project
Here is a combined example to give you an idea of how you can use mise to manage your a project's tools, environment, and tasks.
#
mise.toml
[
tools
]
terraform
=
"
1
"
aws-cli
=
"
2
"
[
env
]
TF_WORKSPACE
=
"
development
"
AWS_REGION
=
"
us-west-2
"
AWS_PROFILE
=
"
dev
"
[
tasks
.
plan
]
description
=
"
Run terraform plan with configured workspace
"
run
=
"""
terraform init
terraform workspace select $TF_WORKSPACE
terraform plan
"""
[
tasks
.
validate
]
description
=
"
Validate AWS credentials and terraform config
"
run
=
"""
aws sts get-caller-identity
terraform validate
"""
[
tasks
.
deploy
]
description
=
"
Deploy infrastructure after validation
"
depends
= [
"
validate
"
,
"
plan
"
]
run
=
"
terraform apply -auto-approve
"
Run it with:
mise install # install tools specified in mise.toml
mise run deploy
Find more examples in the
mise cookbook
.
Full Documentation
See
mise.jdx.dev
GitHub Issues & Discussions
Due to the volume of issue submissions mise received, using GitHub Issues became unsustainable for
the project. Instead, mise uses GitHub Discussions which provide a more community-centric platform
for communication and require less management on the part of the maintainers.
Please note the following discussion categories, which match how issues are often used:
Announcements
Ideas
: for feature requests, etc.
Troubleshooting & Bug Reports
Special Thanks
We're grateful for Cloudflare's support through
Project Alexandria
.
Contributors
- 今日の獲得スター数: 77
- 累積スター数: 20,215

### References
- https://github.com/jdx/mise

## tursodatabase/turso

### Executive Summary
- Turso is an in-process SQL database, compatible with SQLite.
- ---
- Turso Database
An in-process SQL database, compatible with SQLite.
About
Turso Database is an in-process SQL database written in Rust, compatible with SQLite.
⚠️
Warning:
This software is in BETA. It may still contain bugs and unexpected behavior. Use caution with production data and ensure you have backups.
Features and Roadmap
SQLite compatibility
for SQL dialect, file formats, and the C API [see
document
for details]
Change data capture (CDC)
for real-time tracking of database changes.
Multi-language support
for
Go
JavaScript
Java
Python
Rust
WebAssembly
Asynchronous I/O
support on Linux with
io_uring
Cross-platform
support for Linux, macOS, Windows and browsers (through WebAssembly)
Vector support
support including exact search and vector manipulation
Improved schema management
including extended
ALTER
support and faster schema changes.
The database has the following experimental features:
BEGIN CONCURRENT
for improved write throughput using multi-version concurrency control (MVCC).
Encryption at rest
for protecting the data locally.
Incremental computation
using DBSP for incremental view mainatenance and query subscriptions.
The following features are on our current roadmap:
Vector indexing
for fast approximate vector search, similar to
libSQL vector search
.
Getting Started
Please see the
Turso Database Manual
for more information.
💻 Command Line
You can install the latest `turso` release with:
curl --proto
'
=https
'
--tlsv1.2 -LsSf \
  https://github.com/tursodatabase/turso/releases/latest/download/turso_cli-installer.sh
|
sh
Then launch the interactive shell:
$ tursodb
This will start the Turso interactive shell where you can execute SQL statements:
Turso
Enter ".help" for usage hints.
Connected to a transient in-memory database.
Use ".open FILENAME" to reopen on a persistent database
turso> CREATE TABLE users (id INT, username TEXT);
turso> INSERT INTO users VALUES (1, 'alice');
turso> INSERT INTO users VALUES (2, 'bob');
turso> SELECT * FROM users;
1|alice
2|bob
You can also build and run the latest development version with:
cargo run
If you like docker, we got you covered. Simply run this in the root folder:
make docker-cli-build
&&
\
make docker-cli-run
🦀 Rust
cargo add turso
Example usage:
let
db =
Builder
::
new_local
(
"sqlite.db"
)
.
build
(
)
.
await
?
;
let
conn = db
.
connect
(
)
?
;
let
res = conn
.
query
(
"SELECT * FROM users"
,
(
)
)
.
await
?
;
✨ JavaScript
npm i @tursodatabase/database
Example usage:
import
{
connect
}
from
'@tursodatabase/database'
;
const
db
=
await
connect
(
'sqlite.db'
)
;
const
stmt
=
db
.
prepare
(
'SELECT * FROM users'
)
;
const
users
=
stmt
.
all
(
)
;
console
.
log
(
users
)
;
🐍 Python
uv pip install pyturso
Example usage:
import
turso
con
=
turso
.
connect
(
"sqlite.db"
)
cur
=
con
.
cursor
()
res
=
cur
.
execute
(
"SELECT * FROM users"
)
print
(
res
.
fetchone
())
🦫 Go
go get github.com/tursodatabase/turso-go
go install github.com/tursodatabase/turso-go
Example usage:
import
(
"database/sql"
_
"github.com/tursodatabase/turso-go"
)
conn
,
_
=
sql
.
Open
(
"turso"
,
"sqlite.db"
)
defer
conn
.
Close
()
stmt
,
_
:=
conn
.
Prepare
(
"select * from users"
)
defer
stmt
.
Close
()
rows
,
_
=
stmt
.
Query
()
for
rows
.
Next
() {
var
id
int
var
username
string
_
:=
rows
.
Scan
(
&
id
,
&
username
)
fmt
.
Printf
(
"User: ID: %d, Username: %s
\n
"
,
id
,
username
)
}
☕️ Java
We integrated Turso Database into JDBC. For detailed instructions on how to use Turso Database with java, please refer to
the
README.md under bindings/java
.
🤖 MCP Server Mode
The Turso CLI includes a built-in
Model Context Protocol (MCP)
server that allows AI assistants to interact with your databases.
Start the MCP server with:
tursodb your_database.db --mcp
Configuration
Add Turso to your MCP client configuration:
{
"mcpServers"
: {
"turso"
: {
"command"
:
"
/path/to/.turso/tursodb
"
,
"args"
: [
"
/path/to/your/database.db
"
,
"
--mcp
"
]
    }
  }
}
Available Tools
The MCP server provides nine tools for database interaction:
open_database
- Open a new database
current_database
- Describe the current database
list_tables
- List all tables in the database
describe_table
- Describe the structure of a specific table
execute_query
- Execute read-only SELECT queries
insert_data
- Insert new data into tables
update_data
- Update existing data in tables
delete_data
- Delete data from tables
schema_change
- Execute schema modification statements (CREATE TABLE, ALTER TABLE, DROP TABLE)
Once connected, you can ask your AI assistant:
"Show me all tables in the database"
"What's the schema for the users table?"
"Find all posts with more than 100 upvotes"
"Insert a new user with name 'Alice' and email '
alice@example.com
'"
MCP Clients
Claude Code
If you're using
Claude Code
, you can easily connect to your Turso MCP server using the built-in MCP management commands:
Quick Setup
Add the MCP server
to Claude Code:
claude mcp add my-database -- tursodb ./path/to/your/database.db --mcp
Restart Claude Code
to activate the connection
Start querying
your database through natural language!
Command Breakdown
claude mcp add my-database -- tursodb ./path/to/your/database.db --mcp
#
↑            ↑       ↑                           ↑
#
|            |       |                           |
#
Name         |       Database path               MCP flag
#
Separator
my-database
- Choose any name for your MCP server
--
- Required separator between Claude options and your command
tursodb
- The Turso database CLI
./path/to/your/database.db
- Path to your SQLite database file
--mcp
- Enables MCP server mode
Example Usage
#
For a local project database
cd
/your/project
claude mcp add my-project-db -- tursodb ./data/app.db --mcp
#
For an absolute path
claude mcp add analytics-db -- tursodb /Users/you/databases/analytics.db --mcp
#
For a specific project (local scope)
claude mcp add project-db --local -- tursodb ./database.db --mcp
Managing MCP Servers
#
List all configured MCP servers
claude mcp list
#
Get details about a specific server
claude mcp get my-database
#
Remove an MCP server
claude mcp remove my-database
Claude Desktop
For Claude Desktop, add the configuration to your
claude_desktop_config.json
file:
{
"mcpServers"
: {
"turso"
: {
"command"
:
"
/path/to/.turso/tursodb
"
,
"args"
: [
"
./path/to/your/database.db.db
"
,
"
--mcp
"
]
    }
  }
}
Cursor
For Cursor, configure MCP in your settings:
Open Cursor settings
Navigate to Extensions → MCP
Add a new server with:
Name
:
turso
Command
:
/path/to/.turso/tursodb
Args
:
["./path/to/your/database.db.db", "--mcp"]
Alternatively, you can add it to your Cursor configuration file directly.
Direct JSON-RPC Usage
The MCP server runs as a single process that handles multiple JSON-RPC requests over stdin/stdout. Here's how to interact with it directly:
Example with In-Memory Database
cat
<<
'
EOF
' | tursodb --mcp
{"jsonrpc": "2.0", "id": 1, "method": "initialize", "params": {"protocolVersion": "2024-11-05", "capabilities": {}, "clientInfo": {"name": "client", "version": "1.0"}}}
{"jsonrpc": "2.0", "id": 2, "method": "tools/call", "params": {"name": "schema_change", "arguments": {"query": "CREATE TABLE users (id INTEGER, name TEXT, email TEXT)"}}}
{"jsonrpc": "2.0", "id": 3, "method": "tools/call", "params": {"name": "list_tables", "arguments": {}}}
{"jsonrpc": "2.0", "id": 4, "method": "tools/call", "params": {"name": "insert_data", "arguments": {"query": "INSERT INTO users VALUES (1, 'Alice', 'alice@example.com')"}}}
{"jsonrpc": "2.0", "id": 5, "method": "tools/call", "params": {"name": "execute_query", "arguments": {"query": "SELECT * FROM users"}}}
EOF
Example with Existing Database
#
Working with an existing database file
cat
<<
'
EOF
' | tursodb mydb.db --mcp
{"jsonrpc": "2.0", "id": 1, "method": "initialize", "params": {"protocolVersion": "2024-11-05", "capabilities": {}, "clientInfo": {"name": "client", "version": "1.0"}}}
{"jsonrpc": "2.0", "id": 2, "method": "tools/call", "params": {"name": "list_tables", "arguments": {}}}
EOF
Contributing
We'd love to have you contribute to Turso Database! Please check out the
contribution guide
to get started.
Found a data corruption bug? Get up to $1,000.00
SQLite is loved because it is the most reliable database in the world. The next evolution of SQLite has
to match or surpass this level of reliability. Turso is built with
Deterministic Simulation Testing
from the ground up, and is also tested by
Antithesis
.
Even during Alpha, if you find a bug that leads to a data corruption and demonstrate
how our simulator failed to catch it, you can get up to $1,000.00. As the project matures we will
increase the size of the prize, and the scope of the bugs.
More details
here
.
You can see an example of an awarded case on
#2049
.
Turso core staff are not eligible.
FAQ
Is Turso Database ready for production use?
Turso Database is currently under heavy development and is
not
ready for production use.
How is Turso Database different from Turso's libSQL?
Turso Database is a project to build the next evolution of SQLite in Rust, with a strong open contribution focus and features like native async support, vector search, and more. The libSQL project is also an attempt to evolve SQLite in a similar direction, but through a fork rather than a rewrite.
Rewriting SQLite in Rust started as an unassuming experiment, and due to its incredible success, replaces libSQL as our intended direction. At this point, libSQL is production ready, Turso Database is not - although it is evolving rapidly. More details
here
.
Publications
Pekka Enberg, Sasu Tarkoma, Jon Crowcroft Ashwin Rao (2024). Serverless Runtime / Database Co-Design With Asynchronous I/O. In
EdgeSys ‘24
.
[PDF]
Pekka Enberg, Sasu Tarkoma, and Ashwin Rao (2023). Towards Database and Serverless Runtime Co-Design. In
CoNEXT-SW ’23
. [
PDF
] [
Slides
]
License
This project is licensed under the
MIT license
.
Contribution
Unless you explicitly state otherwise, any contribution intentionally submitted
for inclusion in Turso Database by you, shall be licensed as MIT, without any additional
terms or conditions.
Partners
Thanks to all the partners of Turso!
Contributors
Thanks to all the contributors to Turso Database!
- 今日の獲得スター数: 70
- 累積スター数: 14,012

### References
- https://github.com/tursodatabase/turso

## simular-ai/Agent-S

### Executive Summary
- Agent S: an open agentic framework that uses computers like a human
- ---
- Agent S:
  Use Computer Like a Human
🌐
[S3 blog]
📄
[S3 Paper]
🎥
[S3 Video]
🌐
[S2 blog]
📄
[S2 Paper (COLM 2025)]
🎥
[S2 Video]
🌐
[S1 blog]
📄
[S1 Paper (ICLR 2025)]
🎥
[S1 Video]
Deutsch
|
Español
|
français
|
日本語
|
한국어
|
Português
|
Русский
|
中文
Skip the setup? Try Agent S in
Simular Cloud
🥳 Updates
2025/10/02
: Released Agent S3 and its
technical paper
, setting a new SOTA of
69.9%
on OSWorld (approaching 72% human performance), with strong generalizability on WindowsAgentArena and AndroidWorld! It is also simpler, faster, and more flexible.
2025/08/01
: Agent S2.5 is released (gui-agents v0.2.5): simpler, better, and faster! New SOTA on
OSWorld-Verified
!
2025/07/07
: The
Agent S2 paper
is accepted to COLM 2025! See you in Montreal!
2025/04/27
: The Agent S paper won the Best Paper Award 🏆 at ICLR 2025 Agentic AI for Science Workshop!
2025/04/01
: Released the
Agent S2 paper
with new SOTA results on OSWorld, WindowsAgentArena, and AndroidWorld!
2025/03/12
: Released Agent S2 along with v0.2.0 of
gui-agents
, the new state-of-the-art for computer use agents (CUA), outperforming OpenAI's CUA/Operator and Anthropic's Claude 3.7 Sonnet Computer-Use!
2025/01/22
: The
Agent S paper
is accepted to ICLR 2025!
2025/01/21
: Released v0.1.2 of
gui-agents
library, with support for Linux and Windows!
2024/12/05
: Released v0.1.0 of
gui-agents
library, allowing you to use Agent-S for Mac, OSWorld, and WindowsAgentArena with ease!
2024/10/10
: Released the
Agent S paper
and codebase!
Table of Contents
💡 Introduction
🎯 Current Results
🛠️ Installation & Setup
🚀 Usage
🤝 Acknowledgements
💬 Citation
💡 Introduction
Welcome to
Agent S
, an open-source framework designed to enable autonomous interaction with computers through Agent-Computer Interface. Our mission is to build intelligent GUI agents that can learn from past experiences and perform complex tasks autonomously on your computer.
Whether you're interested in AI, automation, or contributing to cutting-edge agent-based systems, we're excited to have you here!
🎯 Current Results
On OSWorld, Agent S3 alone reaches 62.6% in the 100-step setting, already exceeding the previous state of the art of 61.4% (Claude Sonnet 4.5). With the addition of Behavior Best-of-N, performance climbs even higher to 69.9%, bringing computer-use agents to within just a few points of human-level accuracy (72%).
Agent S3 also demonstrates strong zero-shot generalization. On WindowsAgentArena, accuracy rises from 50.2% using only Agent S3 to 56.6% by selecting from 3 rollouts. Similarly on AndroidWorld, performance improves from 68.1% to 71.6%
🛠️ Installation & Setup
Prerequisites
Single Monitor
: Our agent is designed for single monitor screens
Security
: The agent runs Python code to control your computer - use with care
Supported Platforms
: Linux, Mac, and Windows
Installation
To install Agent S3 without cloning the repository, run
pip install gui-agents
If you would like to test Agent S3 while making changes, clone the repository and install using
pip install -e .
Don't forget to also
brew install tesseract
! Pytesseract requires this extra installation to work.
API Configuration
Option 1: Environment Variables
Add to your
.bashrc
(Linux) or
.zshrc
(MacOS):
export
OPENAI_API_KEY=
<
YOUR_API_KEY
>
export
ANTHROPIC_API_KEY=
<
YOUR_ANTHROPIC_API_KEY
>
export
HF_TOKEN=
<
YOUR_HF_TOKEN
>
Option 2: Python Script
import
os
os
.
environ
[
"OPENAI_API_KEY"
]
=
"<YOUR_API_KEY>"
Supported Models
We support Azure OpenAI, Anthropic, Gemini, Open Router, and vLLM inference. See
models.md
for details.
Grounding Models (Required)
For optimal performance, we recommend
UI-TARS-1.5-7B
hosted on Hugging Face Inference Endpoints or another provider. See
Hugging Face Inference Endpoints
for setup instructions.
🚀 Usage
⚡️
Recommended Setup:
For the best configuration, we recommend using
OpenAI gpt-5-2025-08-07
as the main model, paired with
UI-TARS-1.5-7B
for grounding.
CLI
Note, this is running Agent S3, our improved agent, without bBoN.
Run Agent S3 with the required parameters:
agent_s \
    --provider openai \
    --model gpt-5-2025-08-07 \
    --ground_provider huggingface \
    --ground_url http://localhost:8080 \
    --ground_model ui-tars-1.5-7b \
    --grounding_width 1920 \
    --grounding_height 1080
Local Coding Environment (Optional)
For tasks that require code execution (e.g., data processing, file manipulation, system automation), you can enable the local coding environment:
agent_s \
    --provider openai \
    --model gpt-5-2025-08-07 \
    --ground_provider huggingface \
    --ground_url http://localhost:8080 \
    --ground_model ui-tars-1.5-7b \
    --grounding_width 1920 \
    --grounding_height 1080 \
    --enable_local_env
⚠️
WARNING
: The local coding environment executes arbitrary Python and Bash code locally on your machine. Only use this feature in trusted environments and with trusted inputs.
Required Parameters
--provider
: Main generation model provider (e.g., openai, anthropic, etc.) - Default: "openai"
--model
: Main generation model name (e.g., gpt-5-2025-08-07) - Default: "gpt-5-2025-08-07"
--ground_provider
: The provider for the grounding model -
Required
--ground_url
: The URL of the grounding model -
Required
--ground_model
: The model name for the grounding model -
Required
--grounding_width
: Width of the output coordinate resolution from the grounding model -
Required
--grounding_height
: Height of the output coordinate resolution from the grounding model -
Required
Optional Parameters
--model_temperature
: The temperature to fix all model calls to (necessary to set to 1.0 for models like o3 but can be left blank for other models)
Grounding Model Dimensions
The grounding width and height should match the output coordinate resolution of your grounding model:
UI-TARS-1.5-7B
: Use
--grounding_width 1920 --grounding_height 1080
UI-TARS-72B
: Use
--grounding_width 1000 --grounding_height 1000
Optional Parameters
--model_url
: Custom API URL for main generation model - Default: ""
--model_api_key
: API key for main generation model - Default: ""
--ground_api_key
: API key for grounding model endpoint - Default: ""
--max_trajectory_length
: Maximum number of image turns to keep in trajectory - Default: 8
--enable_reflection
: Enable reflection agent to assist the worker agent - Default: True
--enable_local_env
: Enable local coding environment for code execution (WARNING: Executes arbitrary code locally) - Default: False
Local Coding Environment Details
The local coding environment enables Agent S3 to execute Python and Bash code directly on your machine. This is particularly useful for:
Data Processing
: Manipulating spreadsheets, CSV files, or databases
File Operations
: Bulk file processing, content extraction, or file organization
System Automation
: Configuration changes, system setup, or automation scripts
Code Development
: Writing, editing, or executing code files
Text Processing
: Document manipulation, content editing, or formatting
When enabled, the agent can use the
call_code_agent
action to execute code blocks for tasks that can be completed through programming rather than GUI interaction.
Requirements:
Python
: The same Python interpreter used to run Agent S3 (automatically detected)
Bash
: Available at
/bin/bash
(standard on macOS and Linux)
System Permissions
: The agent runs with the same permissions as the user executing it
Security Considerations:
The local environment executes arbitrary code with the same permissions as the user running the agent
Only enable this feature in trusted environments
Be cautious when the agent generates code for system-level operations
Consider running in a sandboxed environment for untrusted tasks
Bash scripts are executed with a 30-second timeout to prevent hanging processes
gui_agents
SDK
First, we import the necessary modules.
AgentS3
is the main agent class for Agent S3.
OSWorldACI
is our grounding agent that translates agent actions into executable python code.
import
pyautogui
import
io
from
gui_agents
.
s3
.
agents
.
agent_s
import
AgentS3
from
gui_agents
.
s3
.
agents
.
grounding
import
OSWorldACI
from
gui_agents
.
s3
.
utils
.
local_env
import
LocalEnv
# Optional: for local coding environment
# Load in your API keys.
from
dotenv
import
load_dotenv
load_dotenv
()
current_platform
=
"linux"
# "darwin", "windows"
Next, we define our engine parameters.
engine_params
is used for the main agent, and
engine_params_for_grounding
is for grounding. For
engine_params_for_grounding
, we support custom endpoints like HuggingFace TGI, vLLM, and Open Router.
engine_params
=
{
"engine_type"
:
provider
,
"model"
:
model
,
"base_url"
:
model_url
,
# Optional
"api_key"
:
model_api_key
,
# Optional
"temperature"
:
model_temperature
# Optional
}
# Load the grounding engine from a custom endpoint
ground_provider
=
"<your_ground_provider>"
ground_url
=
"<your_ground_url>"
ground_model
=
"<your_ground_model>"
ground_api_key
=
"<your_ground_api_key>"
# Set grounding dimensions based on your model's output coordinate resolution
# UI-TARS-1.5-7B: grounding_width=1920, grounding_height=1080
# UI-TARS-72B: grounding_width=1000, grounding_height=1000
grounding_width
=
1920
# Width of output coordinate resolution
grounding_height
=
1080
# Height of output coordinate resolution
engine_params_for_grounding
=
{
"engine_type"
:
ground_provider
,
"model"
:
ground_model
,
"base_url"
:
ground_url
,
"api_key"
:
ground_api_key
,
# Optional
"grounding_width"
:
grounding_width
,
"grounding_height"
:
grounding_height
,
}
Then, we define our grounding agent and Agent S3.
# Optional: Enable local coding environment
enable_local_env
=
False
# Set to True to enable local code execution
local_env
=
LocalEnv
()
if
enable_local_env
else
None
grounding_agent
=
OSWorldACI
(
env
=
local_env
,
# Pass local_env for code execution capability
platform
=
current_platform
,
engine_params_for_generation
=
engine_params
,
engine_params_for_grounding
=
engine_params_for_grounding
,
width
=
1920
,
# Optional: screen width
height
=
1080
# Optional: screen height
)
agent
=
AgentS3
(
engine_params
,
grounding_agent
,
platform
=
current_platform
,
max_trajectory_length
=
8
,
# Optional: maximum image turns to keep
enable_reflection
=
True
# Optional: enable reflection agent
)
Finally, let's query the agent!
# Get screenshot.
screenshot
=
pyautogui
.
screenshot
()
buffered
=
io
.
BytesIO
()
screenshot
.
save
(
buffered
,
format
=
"PNG"
)
screenshot_bytes
=
buffered
.
getvalue
()
obs
=
{
"screenshot"
:
screenshot_bytes
,
}
instruction
=
"Close VS Code"
info
,
action
=
agent
.
predict
(
instruction
=
instruction
,
observation
=
obs
)
exec
(
action
[
0
])
Refer to
gui_agents/s3/cli_app.py
for more details on how the inference loop works.
OSWorld
To deploy Agent S3 in OSWorld, follow the
OSWorld Deployment instructions
.
💬 Citations
If you find this codebase useful, please cite:
@misc{Agent-S3,
      title={The Unreasonable Effectiveness of Scaling Agents for Computer Use}, 
      author={Gonzalo Gonzalez-Pumariega and Vincent Tu and Chih-Lun Lee and Jiachen Yang and Ang Li and Xin Eric Wang},
      year={2025},
      eprint={2510.02250},
      archivePrefix={arXiv},
      primaryClass={cs.AI},
      url={https://arxiv.org/abs/2510.02250}, 
}

@misc{Agent-S2,
      title={Agent S2: A Compositional Generalist-Specialist Framework for Computer Use Agents}, 
      author={Saaket Agashe and Kyle Wong and Vincent Tu and Jiachen Yang and Ang Li and Xin Eric Wang},
      year={2025},
      eprint={2504.00906},
      archivePrefix={arXiv},
      primaryClass={cs.AI},
      url={https://arxiv.org/abs/2504.00906}, 
}

@inproceedings{Agent-S,
    title={{Agent S: An Open Agentic Framework that Uses Computers Like a Human}},
    author={Saaket Agashe and Jiuzhou Han and Shuyu Gan and Jiachen Yang and Ang Li and Xin Eric Wang},
    booktitle={International Conference on Learning Representations (ICLR)},
    year={2025},
    url={https://arxiv.org/abs/2410.08164}
}
Star History
- 今日の獲得スター数: 70
- 累積スター数: 6,928

### References
- https://github.com/simular-ai/Agent-S

## open-ani/animeko

### Executive Summary
- 集找番、追番、看番的一站式弹幕追番平台，云收藏同步 (Bangumi)，离线缓存，BitTorrent，弹幕云过滤。100% Kotlin/Compose Multiplatform
- ---
- 正式版
测试版
讨论群
Animeko 支持云同步观看记录 (
Bangumi
)、多视频数据源、缓存、弹幕、以及更多功能，提供尽可能简单且舒适的追番体验。
Animeko 曾用名 Ani，现在也简称 Ani。
立即下载
play.mp4
主要功能
浏览来自
Bangumi
的番剧信息以及社区评价
丰富的检索方式：新番时间表、标签搜索
由 Bangumi 和 Animeko 服务端共同提供的精确新番时间表
云同步追番进度
省心的追番进度管理，看完视频自动更新进度
打开 APP 立即继续观看，无需回想上次看到了哪
聚合数据源
聚合视频数据源，全自动选择
还支持 BitTorrent、Jellyfin、Emby、以及自定义源
聚合全网弹幕源（
弹弹play
），以及 Animeko 自己的
弹幕服务
离线缓存
所有数据源都能缓存
精美界面
适配平板和大屏设备
更多个性设置
下载
Animeko 支持所有主流平台：Android、iOS、Windows、macOS、Linux。
稳定版本: 每两周更新, 功能稳定
下载稳定版本
通常建议使用稳定版本. 如果你愿意参与测试并拥有一定的对 bug 的处理能力, 也欢迎使用测试版本更快体验新功能.
具体版本类型可查看下方.
测试版本: 每两天更新, 体验最新功能
下载测试版本
点击查看具体版本类型
Animeko 采用语义化版本号, 简单来说就是
4.x.y
的格式. 有以下几种版本类型:
稳定版本:
新特性发布
: 当
x
更新时, 会有新特性的发布. 通常为 2 周一次.
Bug 修复
: 当
y
更新时, 只会有针对前个版本的重要的 bug 修复. 这些 Bug 修复版本穿插在新特性更新的间隔中,
时间不固定.
在稳定版本的发布周期之间, 会发布测试版本:
Alpha 测试版
: 所有重大新功能都会首先发布到
alpha
测试通道, 客户端内可使用 "每日构建"
接收更新. 这些新功能非常不稳定, 适合热情的先锋测试员!
Beta 测试版
: 在功能经过 alpha 测试修复重大问题后, 会进入
beta
测试通道,
在客户端内名称为 "测试版". 此版本仍然不稳定, 是一个平衡新功能和稳定性的选择
技术总览
如果你是开发者，我们总是欢迎你提交 PR 参与开发！
以下几点可以给你一个技术上的大概了解。
Kotlin 多平台
架构；
使用新一代响应式 UI 框架
Compose Multiplatform
构建
UI；
内置专为 Animeko 打造的“基于
libtorrent
的 BitTorrent 引擎，优化边下边播的体验；
高性能弹幕引擎，公益弹幕服务器 + 网络弹幕源；
适配多平台的
视频播放器
，Android 底层为
ExoPlayer
，PC 底层为
VLC
；
多类型数据源适配，内置
动漫花园
、
Mikan
，拥有强大的自定义数据源编辑器和自动数据源选择器。
参与开发
欢迎你提交 PR 参与开发，
有关项目技术细节请参考
CONTRIBUTING
。
FAQ
资源来源是什么?
全部视频数据都来自网络, Animeko 本身不存储任何视频数据。
Animeko 支持两大数据源类型：BT 和在线。BT 源即为公共 BitTorrent P2P 网络，
每个在 BT
网络上的人都可分享自己拥有的资源供他人下载。在线源即为其他视频资源网站分享的内容。Animeko
本身并不提供任何视频资源。
本着互助精神，使用 BT 源时 Animeko 会自动做种 (分享数据)。
BT 指纹为
-AL4123-
，其中
4123
为版本号
4.12.3
；UA 为类似
ani_libtorrent/4.12.3
。
弹幕来源是什么?
Animeko 拥有自己的公益弹幕服务器，在 Animeko 应用内发送的弹幕将会发送到弹幕服务器上。每条弹幕都会以
Bangumi
用户名绑定以防滥用（并考虑未来增加举报和屏蔽功能）。
Animeko 还会从
弹弹play
获取关联弹幕，弹弹play还会从其他弹幕平台例如哔哩哔哩港澳台和巴哈姆特获取弹幕。
番剧每集可拥有几十到几千条不等的弹幕量。
- 今日の獲得スター数: 68
- 累積スター数: 11,874

### References
- https://github.com/open-ani/animeko

## LadybirdBrowser/ladybird

### Executive Summary
- Truly independent web browser
- ---
- Ladybird
Ladybird
is a truly independent web browser, using a novel engine based on web standards.
Important
Ladybird is in a pre-alpha state, and only suitable for use by developers
Features
We aim to build a complete, usable browser for the modern web.
Ladybird uses a multi-process architecture with a main UI process, several WebContent renderer processes,
an ImageDecoder process, and a RequestServer process.
Image decoding and network connections are done out of process to be more robust against malicious content.
Each tab has its own renderer process, which is sandboxed from the rest of the system.
At the moment, many core library support components are inherited from SerenityOS:
LibWeb: Web rendering engine
LibJS: JavaScript engine
LibWasm: WebAssembly implementation
LibCrypto/LibTLS: Cryptography primitives and Transport Layer Security
LibHTTP: HTTP/1.1 client
LibGfx: 2D Graphics Library, Image Decoding and Rendering
LibUnicode: Unicode and locale support
LibMedia: Audio and video playback
LibCore: Event loop, OS abstraction layer
LibIPC: Inter-process communication
How do I build and run this?
See
build instructions
for information on how to build Ladybird.
Ladybird runs on Linux, macOS, Windows (with WSL2), and many other *Nixes.
How do I read the documentation?
Code-related documentation can be found in the
documentation
folder.
Get in touch and participate!
Join
our Discord server
to participate in development discussion.
Please read
Getting started contributing
if you plan to contribute to Ladybird for the first time.
Before opening an issue, please see the
issue policy
and the
detailed issue-reporting guidelines
.
The full contribution guidelines can be found in
CONTRIBUTING.md
.
License
Ladybird is licensed under a 2-clause BSD license.
- 今日の獲得スター数: 61
- 累積スター数: 49,502

### References
- https://github.com/LadybirdBrowser/ladybird

## EFForg/rayhunter

### Executive Summary
- Rust tool to detect cell site simulators on an orbic mobile hotspot
- ---
- Rayhunter
Rayhunter is a project for detecting IMSI catchers, also known as cell-site simulators or stingrays. It was first designed to run on a cheap mobile hotspot called the Orbic RC400L, but thanks to community efforts can
support some other devices as well
.
It's also designed to be as easy to install and use as possible, regardless of your level of technical skills, and to minimize false positives.
→  Check out the
installation guide
to get started.
→ To learn more about the aim of the project, and about IMSI catchers in general, please check out our
introductory blog post
.
→ For discussion, help, or to join the mattermost channel and get involved with the project and community check out the
many ways listed here
!
→ To learn more about the project in general check out the
Rayhunter Book
.
LEGAL DISCLAIMER:
Use this program at your own risk. We believe running this program does not currently violate any laws or regulations in the United States. However, we are not responsible for civil or criminal liability resulting from the use of this software. If you are located outside of the US please consult with an attorney in your country to help you assess the legal risks of running this program.
Good Hunting!
- 今日の獲得スター数: 54
- 累積スター数: 3,053

### References
- https://github.com/EFForg/rayhunter

## ggml-org/llama.cpp

### Executive Summary
- LLM inference in C/C++
- ---
- llama.cpp
Manifesto
/
ggml
/
ops
LLM inference in C/C++
Recent API changes
Changelog for
libllama
API
Changelog for
llama-server
REST API
Hot topics
guide : running gpt-oss with llama.cpp
[FEEDBACK] Better packaging for llama.cpp to support downstream consumers 🤗
Support for the
gpt-oss
model with native MXFP4 format has been added |
PR
|
Collaboration with NVIDIA
|
Comment
Hot PRs:
All
|
Open
Multimodal support arrived in
llama-server
:
#12898
|
documentation
VS Code extension for FIM completions:
https://github.com/ggml-org/llama.vscode
Vim/Neovim plugin for FIM completions:
https://github.com/ggml-org/llama.vim
Introducing GGUF-my-LoRA
#10123
Hugging Face Inference Endpoints now support GGUF out of the box!
#9669
Hugging Face GGUF editor:
discussion
|
tool
Quick start
Getting started with llama.cpp is straightforward. Here are several ways to install it on your machine:
Install
llama.cpp
using
brew, nix or winget
Run with Docker - see our
Docker documentation
Download pre-built binaries from the
releases page
Build from source by cloning this repository - check out
our build guide
Once installed, you'll need a model to work with. Head to the
Obtaining and quantizing models
section to learn more.
Example command:
#
Use a local model file
llama-cli -m my_model.gguf
#
Or download and run a model directly from Hugging Face
llama-cli -hf ggml-org/gemma-3-1b-it-GGUF
#
Launch OpenAI-compatible API server
llama-server -hf ggml-org/gemma-3-1b-it-GGUF
Description
The main goal of
llama.cpp
is to enable LLM inference with minimal setup and state-of-the-art performance on a wide
range of hardware - locally and in the cloud.
Plain C/C++ implementation without any dependencies
Apple silicon is a first-class citizen - optimized via ARM NEON, Accelerate and Metal frameworks
AVX, AVX2, AVX512 and AMX support for x86 architectures
1.5-bit, 2-bit, 3-bit, 4-bit, 5-bit, 6-bit, and 8-bit integer quantization for faster inference and reduced memory use
Custom CUDA kernels for running LLMs on NVIDIA GPUs (support for AMD GPUs via HIP and Moore Threads GPUs via MUSA)
Vulkan and SYCL backend support
CPU+GPU hybrid inference to partially accelerate models larger than the total VRAM capacity
The
llama.cpp
project is the main playground for developing new features for the
ggml
library.
Models
Typically finetunes of the base models below are supported as well.
Instructions for adding support for new models:
HOWTO-add-model.md
Text-only
LLaMA 🦙
LLaMA 2 🦙🦙
LLaMA 3 🦙🦙🦙
Mistral 7B
Mixtral MoE
DBRX
Falcon
Chinese LLaMA / Alpaca
and
Chinese LLaMA-2 / Alpaca-2
Vigogne (French)
BERT
Koala
Baichuan 1 & 2
+
derivations
Aquila 1 & 2
Starcoder models
Refact
MPT
Bloom
Yi models
StableLM models
Deepseek models
Qwen models
PLaMo-13B
Phi models
PhiMoE
GPT-2
Orion 14B
InternLM2
CodeShell
Gemma
Mamba
Grok-1
Xverse
Command-R models
SEA-LION
GritLM-7B
+
GritLM-8x7B
OLMo
OLMo 2
OLMoE
Granite models
GPT-NeoX
+
Pythia
Snowflake-Arctic MoE
Smaug
Poro 34B
Bitnet b1.58 models
Flan T5
Open Elm models
ChatGLM3-6b
+
ChatGLM4-9b
+
GLMEdge-1.5b
+
GLMEdge-4b
GLM-4-0414
SmolLM
EXAONE-3.0-7.8B-Instruct
FalconMamba Models
Jais
Bielik-11B-v2.3
RWKV-6
QRWKV-6
GigaChat-20B-A3B
Trillion-7B-preview
Ling models
LFM2 models
Hunyuan models
Multimodal
LLaVA 1.5 models
,
LLaVA 1.6 models
BakLLaVA
Obsidian
ShareGPT4V
MobileVLM 1.7B/3B models
Yi-VL
Mini CPM
Moondream
Bunny
GLM-EDGE
Qwen2-VL
LFM2-VL
Bindings
Python:
ddh0/easy-llama
Python:
abetlen/llama-cpp-python
Go:
go-skynet/go-llama.cpp
Node.js:
withcatai/node-llama-cpp
JS/TS (llama.cpp server client):
lgrammel/modelfusion
JS/TS (Programmable Prompt Engine CLI):
offline-ai/cli
JavaScript/Wasm (works in browser):
tangledgroup/llama-cpp-wasm
Typescript/Wasm (nicer API, available on npm):
ngxson/wllama
Ruby:
yoshoku/llama_cpp.rb
Rust (more features):
edgenai/llama_cpp-rs
Rust (nicer API):
mdrokz/rust-llama.cpp
Rust (more direct bindings):
utilityai/llama-cpp-rs
Rust (automated build from crates.io):
ShelbyJenkins/llm_client
C#/.NET:
SciSharp/LLamaSharp
C#/VB.NET (more features - community license):
LM-Kit.NET
Scala 3:
donderom/llm4s
Clojure:
phronmophobic/llama.clj
React Native:
mybigday/llama.rn
Java:
kherud/java-llama.cpp
Java:
QuasarByte/llama-cpp-jna
Zig:
deins/llama.cpp.zig
Flutter/Dart:
netdur/llama_cpp_dart
Flutter:
xuegao-tzx/Fllama
PHP (API bindings and features built on top of llama.cpp):
distantmagic/resonance
(more info)
Guile Scheme:
guile_llama_cpp
Swift
srgtuszy/llama-cpp-swift
Swift
ShenghaiWang/SwiftLlama
Delphi
Embarcadero/llama-cpp-delphi
UIs
(to have a project listed here, it should clearly state that it depends on
llama.cpp
)
AI Sublime Text plugin
(MIT)
cztomsik/ava
(MIT)
Dot
(GPL)
eva
(MIT)
iohub/collama
(Apache-2.0)
janhq/jan
(AGPL)
johnbean393/Sidekick
(MIT)
KanTV
(Apache-2.0)
KodiBot
(GPL)
llama.vim
(MIT)
LARS
(AGPL)
Llama Assistant
(GPL)
LLMFarm
(MIT)
LLMUnity
(MIT)
LMStudio
(proprietary)
LocalAI
(MIT)
LostRuins/koboldcpp
(AGPL)
MindMac
(proprietary)
MindWorkAI/AI-Studio
(FSL-1.1-MIT)
Mobile-Artificial-Intelligence/maid
(MIT)
Mozilla-Ocho/llamafile
(Apache-2.0)
nat/openplayground
(MIT)
nomic-ai/gpt4all
(MIT)
ollama/ollama
(MIT)
oobabooga/text-generation-webui
(AGPL)
PocketPal AI
(MIT)
psugihara/FreeChat
(MIT)
ptsochantaris/emeltal
(MIT)
pythops/tenere
(AGPL)
ramalama
(MIT)
semperai/amica
(MIT)
withcatai/catai
(MIT)
Autopen
(GPL)
Tools
akx/ggify
– download PyTorch models from HuggingFace Hub and convert them to GGML
akx/ollama-dl
– download models from the Ollama library to be used directly with llama.cpp
crashr/gppm
– launch llama.cpp instances utilizing NVIDIA Tesla P40 or P100 GPUs with reduced idle power consumption
gpustack/gguf-parser
- review/check the GGUF file and estimate the memory usage
Styled Lines
(proprietary licensed, async wrapper of inference part for game development in Unity3d with pre-built Mobile and Web platform wrappers and a model example)
Infrastructure
Paddler
- Open-source LLMOps platform for hosting and scaling AI in your own infrastructure
GPUStack
- Manage GPU clusters for running LLMs
llama_cpp_canister
- llama.cpp as a smart contract on the Internet Computer, using WebAssembly
llama-swap
- transparent proxy that adds automatic model switching with llama-server
Kalavai
- Crowdsource end to end LLM deployment at any scale
llmaz
- ☸️ Easy, advanced inference platform for large language models on Kubernetes.
Games
Lucy's Labyrinth
- A simple maze game where agents controlled by an AI model will try to trick you.
Supported backends
Backend
Target devices
Metal
Apple Silicon
BLAS
All
BLIS
All
SYCL
Intel and Nvidia GPU
MUSA
Moore Threads GPU
CUDA
Nvidia GPU
HIP
AMD GPU
Vulkan
GPU
CANN
Ascend NPU
OpenCL
Adreno GPU
IBM zDNN
IBM Z & LinuxONE
WebGPU [In Progress]
All
RPC
All
Obtaining and quantizing models
The
Hugging Face
platform hosts a
number of LLMs
compatible with
llama.cpp
:
Trending
LLaMA
You can either manually download the GGUF file or directly use any
llama.cpp
-compatible models from
Hugging Face
or other model hosting sites, such as
ModelScope
, by using this CLI argument:
-hf <user>/<model>[:quant]
. For example:
llama-cli -hf ggml-org/gemma-3-1b-it-GGUF
By default, the CLI would download from Hugging Face, you can switch to other options with the environment variable
MODEL_ENDPOINT
. For example, you may opt to downloading model checkpoints from ModelScope or other model sharing communities by setting the environment variable, e.g.
MODEL_ENDPOINT=https://www.modelscope.cn/
.
After downloading a model, use the CLI tools to run it locally - see below.
llama.cpp
requires the model to be stored in the
GGUF
file format. Models in other data formats can be converted to GGUF using the
convert_*.py
Python scripts in this repo.
The Hugging Face platform provides a variety of online tools for converting, quantizing and hosting models with
llama.cpp
:
Use the
GGUF-my-repo space
to convert to GGUF format and quantize model weights to smaller sizes
Use the
GGUF-my-LoRA space
to convert LoRA adapters to GGUF format (more info:
#10123
)
Use the
GGUF-editor space
to edit GGUF meta data in the browser (more info:
#9268
)
Use the
Inference Endpoints
to directly host
llama.cpp
in the cloud (more info:
#9669
)
To learn more about model quantization,
read this documentation
llama-cli
A CLI tool for accessing and experimenting with most of
llama.cpp
's functionality.
Run in conversation mode
Models with a built-in chat template will automatically activate conversation mode. If this doesn't occur, you can manually enable it by adding
-cnv
and specifying a suitable chat template with
--chat-template NAME
llama-cli -m model.gguf
#
> hi, who are you?
#
Hi there! I'm your helpful assistant! I'm an AI-powered chatbot designed to assist and provide information to users like you. I'm here to help answer your questions, provide guidance, and offer support on a wide range of topics. I'm a friendly and knowledgeable AI, and I'm always happy to help with anything you need. What's on your mind, and how can I assist you today?
#
#
> what is 1+1?
#
Easy peasy! The answer to 1+1 is... 2!
Run in conversation mode with custom chat template
#
use the "chatml" template (use -h to see the list of supported templates)
llama-cli -m model.gguf -cnv --chat-template chatml
#
use a custom template
llama-cli -m model.gguf -cnv --in-prefix
'
User:
'
--reverse-prompt
'
User:
'
Run simple text completion
To disable conversation mode explicitly, use
-no-cnv
llama-cli -m model.gguf -p
"
I believe the meaning of life is
"
-n 128 -no-cnv
#
I believe the meaning of life is to find your own truth and to live in accordance with it. For me, this means being true to myself and following my passions, even if they don't align with societal expectations. I think that's what I love about yoga – it's not just a physical practice, but a spiritual one too. It's about connecting with yourself, listening to your inner voice, and honoring your own unique journey.
Constrain the output with a custom grammar
llama-cli -m model.gguf -n 256 --grammar-file grammars/json.gbnf -p
'
Request: schedule a call at 8pm; Command:
'
#
{"appointmentTime": "8pm", "appointmentDetails": "schedule a a call"}
The
grammars/
folder contains a handful of sample grammars. To write your own, check out the
GBNF Guide
.
For authoring more complex JSON grammars, check out
https://grammar.intrinsiclabs.ai/
llama-server
A lightweight,
OpenAI API
compatible, HTTP server for serving LLMs.
Start a local HTTP server with default configuration on port 8080
llama-server -m model.gguf --port 8080
#
Basic web UI can be accessed via browser: http://localhost:8080
#
Chat completion endpoint: http://localhost:8080/v1/chat/completions
Support multiple-users and parallel decoding
#
up to 4 concurrent requests, each with 4096 max context
llama-server -m model.gguf -c 16384 -np 4
Enable speculative decoding
#
the draft.gguf model should be a small variant of the target model.gguf
llama-server -m model.gguf -md draft.gguf
Serve an embedding model
#
use the /embedding endpoint
llama-server -m model.gguf --embedding --pooling cls -ub 8192
Serve a reranking model
#
use the /reranking endpoint
llama-server -m model.gguf --reranking
Constrain all outputs with a grammar
#
custom grammar
llama-server -m model.gguf --grammar-file grammar.gbnf
#
JSON
llama-server -m model.gguf --grammar-file grammars/json.gbnf
llama-perplexity
A tool for measuring the
perplexity
1
(and other quality metrics) of a model over a given text.
Measure the perplexity over a text file
llama-perplexity -m model.gguf -f file.txt
#
[1]15.2701,[2]5.4007,[3]5.3073,[4]6.2965,[5]5.8940,[6]5.6096,[7]5.7942,[8]4.9297, ...
#
Final estimate: PPL = 5.4007 +/- 0.67339
Measure KL divergence
#
TODO
llama-bench
Benchmark the performance of the inference for various parameters.
Run default benchmark
llama-bench -m model.gguf
#
Output:
#
| model               |       size |     params | backend    | threads |          test |                  t/s |
#
| ------------------- | ---------: | ---------: | ---------- | ------: | ------------: | -------------------: |
#
| qwen2 1.5B Q4_0     | 885.97 MiB |     1.54 B | Metal,BLAS |      16 |         pp512 |      5765.41 ± 20.55 |
#
| qwen2 1.5B Q4_0     | 885.97 MiB |     1.54 B | Metal,BLAS |      16 |         tg128 |        197.71 ± 0.81 |
#
#
build: 3e0ba0e60 (4229)
llama-run
A comprehensive example for running
llama.cpp
models. Useful for inferencing. Used with RamaLama
2
.
Run a model with a specific prompt (by default it's pulled from Ollama registry)
llama-run granite-code
llama-simple
A minimal example for implementing apps with
llama.cpp
. Useful for developers.
Basic text completion
llama-simple -m model.gguf
#
Hello my name is Kaitlyn and I am a 16 year old girl. I am a junior in high school and I am currently taking a class called "The Art of
Contributing
Contributors can open PRs
Collaborators will be invited based on contributions
Maintainers can push to branches in the
llama.cpp
repo and merge PRs into the
master
branch
Any help with managing issues, PRs and projects is very appreciated!
See
good first issues
for tasks suitable for first contributions
Read the
CONTRIBUTING.md
for more information
Make sure to read this:
Inference at the edge
A bit of backstory for those who are interested:
Changelog podcast
Other documentation
main (cli)
server
GBNF grammars
Development documentation
How to build
Running on Docker
Build on Android
Performance troubleshooting
GGML tips & tricks
Seminal papers and background on the models
If your issue is with model generation quality, then please at least scan the following links and papers to understand the limitations of LLaMA models. This is especially important when choosing an appropriate model size and appreciating both the significant and subtle differences between LLaMA models and ChatGPT:
LLaMA:
Introducing LLaMA: A foundational, 65-billion-parameter large language model
LLaMA: Open and Efficient Foundation Language Models
GPT-3
Language Models are Few-Shot Learners
GPT-3.5 / InstructGPT / ChatGPT:
Aligning language models to follow instructions
Training language models to follow instructions with human feedback
XCFramework
The XCFramework is a precompiled version of the library for iOS, visionOS, tvOS,
and macOS. It can be used in Swift projects without the need to compile the
library from source. For example:
// swift-tools-version: 5.10
// The swift-tools-version declares the minimum version of Swift required to build this package.
import
PackageDescription
let
package
=
Package
(
name
:
"
MyLlamaPackage
"
,
targets
:
[
.
executableTarget
(
name
:
"
MyLlamaPackage
"
,
dependencies
:
[
"
LlamaFramework
"
]
)
,
.
binaryTarget
(
name
:
"
LlamaFramework
"
,
url
:
"
https://github.com/ggml-org/llama.cpp/releases/download/b5046/llama-b5046-xcframework.zip
"
,
checksum
:
"
c19be78b5f00d8d29a25da41042cb7afa094cbf6280a225abe614b03b20029ab
"
)
]
)
The above example is using an intermediate build
b5046
of the library. This can be modified
to use a different version by changing the URL and checksum.
Completions
Command-line completion is available for some environments.
Bash Completion
$ build/bin/llama-cli --completion-bash
>
~
/.llama-completion.bash
$
source
~
/.llama-completion.bash
Optionally this can be added to your
.bashrc
or
.bash_profile
to load it
automatically. For example:
$
echo
"
source ~/.llama-completion.bash
"
>>
~
/.bashrc
Dependencies
yhirose/cpp-httplib
- Single-header HTTP server, used by
llama-server
- MIT license
stb-image
- Single-header image format decoder, used by multimodal subsystem - Public domain
nlohmann/json
- Single-header JSON library, used by various tools/examples - MIT License
minja
- Minimal Jinja parser in C++, used by various tools/examples - MIT License
linenoise.cpp
- C++ library that provides readline-like line editing capabilities, used by
llama-run
- BSD 2-Clause License
curl
- Client-side URL transfer library, used by various tools/examples -
CURL License
miniaudio.h
- Single-header audio format decoder, used by multimodal subsystem - Public domain
Footnotes
https://huggingface.co/docs/transformers/perplexity
↩
RamaLama
↩
- 今日の獲得スター数: 49
- 累積スター数: 87,367

### References
- https://github.com/ggml-org/llama.cpp

## supermemoryai/supermemory

### Executive Summary
- Memory engine and app that is extremely fast, scalable. The Memory API for the AI era.
- ---
- Features
Core Functionality
Add Memories from Any Content
: Easily add memories from URLs, PDFs, and plain text—just paste, upload, or link.
Chat with Your Memories
: Converse with your stored content using natural language chat.
Supermemory MCP Integration
: Seamlessly connect with all major AI tools (Claude, Cursor, etc.) via Supermemory MCP.
How do i use this?
Go to
app.supermemory.ai
and sign into with your account
Start Adding Memory with your choose of format (Note, Link, File)
You can also Connect to your favourite services (Notion, Google Drive, OneDrive)
Once Memories are added, you can chat with Supermemory by clicking on "Open Chat" and retrieve info from your saved memories
Add MCP to your AI Tools (by clicking on "Connect to your AI" and select the AI tool you are trying to integrate)
Support
Have questions or feedback? We're here to help:
Email:
dhravya@supermemory.com
Documentation:
docs.supermemory.ai
Contributing
We welcome contributions from developers of all skill levels! Whether you're fixing bugs, adding features, or improving documentation, your help makes supermemory better for everyone.
Quick Start for Contributors
Fork and clone
the repository
Install dependencies
with
bun install
Set up your environment
by copying
.env.example
to
.env.local
Start developing
with
bun run dev
For detailed guidelines, development setup, coding standards, and the complete contribution workflow, please see our
Contributing Guide
.
Ways to Contribute
🐛
Bug fixes
- Help us squash those pesky issues
✨
New features
- Add functionality that users will love
🎨
UI/UX improvements
- Make the interface more intuitive
⚡
Performance optimizations
- Help us make supermemory faster
Check out our
Issues
page for
good first issue
and
help wanted
labels to get started!
Updates & Roadmap
Stay up to date with the latest improvements:
Changelog
X
.
- 今日の獲得スター数: 47
- 累積スター数: 11,152

### References
- https://github.com/supermemoryai/supermemory

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
- 今日の獲得スター数: 46
- 累積スター数: 17,563

### References
- https://github.com/browserbase/stagehand

## oracle/graal

### Executive Summary
- GraalVM compiles applications into native executables that start instantly, scale fast, and use fewer compute resources 🚀
- ---
- GraalVM is a high-performance JDK distribution that compiles your Java applications ahead of time into standalone binaries. These binaries start instantly, provide peak performance with no warmup, and use fewer resources.
You can use GraalVM just like any other Java Development Kit in your IDE.
The project website at
https://www.graalvm.org/
describes how to
get started
, how to
stay connected
, and how to
contribute
.
Documentation
Please refer to the
GraalVM website for documentation
.
You can find most of the documentation sources in the
docs/
directory in the same hierarchy as displayed on the website.
Additional documentation including developer instructions for individual components can be found in corresponding
docs/
sub-directories.
The documentation for the Truffle framework, for example, is in
truffle/docs/
.
This also applies to languages, tools, and other components maintained in
related repositories
.
Get Support
Open a
GitHub issue
for bug reports, questions, or requests for enhancements.
Join the
GraalVM Slack
to connect with the community and the GraalVM team.
Report a security vulnerability according to the
Reporting Vulnerabilities guide
.
Repository Structure
This source repository is the main repository for GraalVM and includes the following components:
Directory
Description
.devcontainer/
Configuration files for GitHub dev containers.
.github/
Configuration files for GitHub issues, workflows, ….
compiler/
Graal compiler
, a modern, versatile compiler written in Java.
espresso/
Espresso
, a meta-circular Java bytecode interpreter for the GraalVM.
regex/
TRegex, a regular expression engine for other GraalVM languages.
sdk/
GraalVM SDK
, long-term supported APIs of GraalVM.
substratevm/
Framework for ahead-of-time (AOT) compilation with
Native Image
.
sulong/
Sulong
, an engine for running LLVM bitcode on GraalVM.
tools/
Tools for GraalVM languages implemented with the instrumentation framework.
truffle/
GraalVM's
language implementation framework
for creating languages and tools.
visualizer/
Ideal Graph Visualizer (IGV)
, a tool for analyzing Graal compiler graphs.
vm/
Components for building GraalVM distributions.
wasm/
GraalWasm
, an engine for running WebAssembly programs on GraalVM.
Related Repositories
GraalVM provides additional languages, tools, and other components developed in related repositories. These are:
Name
Description
FastR
Implementation of the R language.
GraalJS
Implementation of JavaScript and Node.js.
GraalPy
Implementation of the Python language.
Native Build Tools
Build tool plugins for GraalVM Native Image.
SimpleLanguage
A simple example language built with the Truffle framework.
SimpleTool
A simple example tool built with the Truffle framework.
TruffleRuby
Implementation of the Ruby language.
Examples and Tutorials
Explore practical examples, deep-dive workshops, and language-specific demos for working with GraalVM.
Name
Description
GraalVM Demos
Example applications highlighting GraalVM key features and best practices.
GraalVM Workshops and Tutorials
Workshops and tutorials to help you learn and apply GraalVM tools and capabilities.
Graal Languages - Demos and Guides
Demo applications and guides for GraalJS, GraalPy, GraalWasm, and other Graal Languages.
License
GraalVM Community Edition is open source and distributed under
version 2 of the GNU General Public License with the “Classpath” Exception
, which are the same terms as for Java. The licenses of the individual GraalVM components are generally derivative of the license of a particular language (see the table below).
Component(s)
License
Espresso
,
Ideal Graph Visualizer
GPL 2
GraalVM Compiler
,
SubstrateVM
,
Tools
,
VM
GPL 2 with Classpath Exception
GraalVM SDK
,
GraalWasm
,
Truffle Framework
,
TRegex
Universal Permissive License
Sulong
3-clause BSD
- 今日の獲得スター数: 45
- 累積スター数: 21,200

### References
- https://github.com/oracle/graal

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
wget -O netdisk-fast-download.zip  https://github.com/qaiu/netdisk-fast-download/releases/download/0.1.8-release-fixed2/netdisk-fast-download-bin-fixed2.zip
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
99元, 提供对小飞机,蓝奏优享大文件解析的支持, 提供天翼云盘,移动云盘,联调云盘的解析支持
199元, 包含部署服务和首页定制, 需提供宝塔环境
可以提供功能定制开发, 加v价格详谈:
qq: 197575894
wechat: imcoding_
- 今日の獲得スター数: 41
- 累積スター数: 2,220

### References
- https://github.com/qaiu/netdisk-fast-download

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
- 今日の獲得スター数: 37
- 累積スター数: 30,886

### References
- https://github.com/DioxusLabs/dioxus

## modelcontextprotocol/python-sdk

### Executive Summary
- The official Python SDK for Model Context Protocol servers and clients
- ---
- MCP Python SDK
Python implementation of the Model Context Protocol (MCP)
Table of Contents
MCP Python SDK
Overview
Installation
Adding MCP to your python project
Running the standalone MCP development tools
Quickstart
What is MCP?
Core Concepts
Server
Resources
Tools
Structured Output
Prompts
Images
Context
Getting Context in Functions
Context Properties and Methods
Completions
Elicitation
Sampling
Logging and Notifications
Authentication
FastMCP Properties
Session Properties and Methods
Request Context Properties
Running Your Server
Development Mode
Claude Desktop Integration
Direct Execution
Streamable HTTP Transport
CORS Configuration for Browser-Based Clients
Mounting to an Existing ASGI Server
StreamableHTTP servers
Basic mounting
Host-based routing
Multiple servers with path configuration
Path configuration at initialization
SSE servers
Advanced Usage
Low-Level Server
Structured Output Support
Pagination (Advanced)
Writing MCP Clients
Client Display Utilities
OAuth Authentication for Clients
Parsing Tool Results
MCP Primitives
Server Capabilities
Documentation
Contributing
License
Overview
The Model Context Protocol allows applications to provide context for LLMs in a standardized way, separating the concerns of providing context from the actual LLM interaction. This Python SDK implements the full MCP specification, making it easy to:
Build MCP clients that can connect to any MCP server
Create MCP servers that expose resources, prompts and tools
Use standard transports like stdio, SSE, and Streamable HTTP
Handle all MCP protocol messages and lifecycle events
Installation
Adding MCP to your python project
We recommend using
uv
to manage your Python projects.
If you haven't created a uv-managed project yet, create one:
uv init mcp-server-demo
cd
mcp-server-demo
Then add MCP to your project dependencies:
uv add
"
mcp[cli]
"
Alternatively, for projects using pip for dependencies:
pip install
"
mcp[cli]
"
Running the standalone MCP development tools
To run the mcp command with uv:
uv run mcp
Quickstart
Let's create a simple MCP server that exposes a calculator tool and some data:
"""
FastMCP quickstart example.
cd to the `examples/snippets/clients` directory and run:
uv run server fastmcp_quickstart stdio
"""
from
mcp
.
server
.
fastmcp
import
FastMCP
# Create an MCP server
mcp
=
FastMCP
(
"Demo"
)
# Add an addition tool
@
mcp
.
tool
()
def
add
(
a
:
int
,
b
:
int
)
->
int
:
"""Add two numbers"""
return
a
+
b
# Add a dynamic greeting resource
@
mcp
.
resource
(
"greeting://{name}"
)
def
get_greeting
(
name
:
str
)
->
str
:
"""Get a personalized greeting"""
return
f"Hello,
{
name
}
!"
# Add a prompt
@
mcp
.
prompt
()
def
greet_user
(
name
:
str
,
style
:
str
=
"friendly"
)
->
str
:
"""Generate a greeting prompt"""
styles
=
{
"friendly"
:
"Please write a warm, friendly greeting"
,
"formal"
:
"Please write a formal, professional greeting"
,
"casual"
:
"Please write a casual, relaxed greeting"
,
    }
return
f"
{
styles
.
get
(
style
,
styles
[
'friendly'
])
}
for someone named
{
name
}
."
Full example:
examples/snippets/servers/fastmcp_quickstart.py
You can install this server in
Claude Desktop
and interact with it right away by running:
uv run mcp install server.py
Alternatively, you can test it with the MCP Inspector:
uv run mcp dev server.py
What is MCP?
The
Model Context Protocol (MCP)
lets you build servers that expose data and functionality to LLM applications in a secure, standardized way. Think of it like a web API, but specifically designed for LLM interactions. MCP servers can:
Expose data through
Resources
(think of these sort of like GET endpoints; they are used to load information into the LLM's context)
Provide functionality through
Tools
(sort of like POST endpoints; they are used to execute code or otherwise produce a side effect)
Define interaction patterns through
Prompts
(reusable templates for LLM interactions)
And more!
Core Concepts
Server
The FastMCP server is your core interface to the MCP protocol. It handles connection management, protocol compliance, and message routing:
"""Example showing lifespan support for startup/shutdown with strong typing."""
from
collections
.
abc
import
AsyncIterator
from
contextlib
import
asynccontextmanager
from
dataclasses
import
dataclass
from
mcp
.
server
.
fastmcp
import
Context
,
FastMCP
from
mcp
.
server
.
session
import
ServerSession
# Mock database class for example
class
Database
:
"""Mock database class for example."""
@
classmethod
async
def
connect
(
cls
)
->
"Database"
:
"""Connect to database."""
return
cls
()
async
def
disconnect
(
self
)
->
None
:
"""Disconnect from database."""
pass
def
query
(
self
)
->
str
:
"""Execute a query."""
return
"Query result"
@
dataclass
class
AppContext
:
"""Application context with typed dependencies."""
db
:
Database
@
asynccontextmanager
async
def
app_lifespan
(
server
:
FastMCP
)
->
AsyncIterator
[
AppContext
]:
"""Manage application lifecycle with type-safe context."""
# Initialize on startup
db
=
await
Database
.
connect
()
try
:
yield
AppContext
(
db
=
db
)
finally
:
# Cleanup on shutdown
await
db
.
disconnect
()
# Pass lifespan to server
mcp
=
FastMCP
(
"My App"
,
lifespan
=
app_lifespan
)
# Access type-safe lifespan context in tools
@
mcp
.
tool
()
def
query_db
(
ctx
:
Context
[
ServerSession
,
AppContext
])
->
str
:
"""Tool that uses initialized resources."""
db
=
ctx
.
request_context
.
lifespan_context
.
db
return
db
.
query
()
Full example:
examples/snippets/servers/lifespan_example.py
Resources
Resources are how you expose data to LLMs. They're similar to GET endpoints in a REST API - they provide data but shouldn't perform significant computation or have side effects:
from
mcp
.
server
.
fastmcp
import
FastMCP
mcp
=
FastMCP
(
name
=
"Resource Example"
)
@
mcp
.
resource
(
"file://documents/{name}"
)
def
read_document
(
name
:
str
)
->
str
:
"""Read a document by name."""
# This would normally read from disk
return
f"Content of
{
name
}
"
@
mcp
.
resource
(
"config://settings"
)
def
get_settings
()
->
str
:
"""Get application settings."""
return
"""{
"theme": "dark",
"language": "en",
"debug": false
}"""
Full example:
examples/snippets/servers/basic_resource.py
Tools
Tools let LLMs take actions through your server. Unlike resources, tools are expected to perform computation and have side effects:
from
mcp
.
server
.
fastmcp
import
FastMCP
mcp
=
FastMCP
(
name
=
"Tool Example"
)
@
mcp
.
tool
()
def
sum
(
a
:
int
,
b
:
int
)
->
int
:
"""Add two numbers together."""
return
a
+
b
@
mcp
.
tool
()
def
get_weather
(
city
:
str
,
unit
:
str
=
"celsius"
)
->
str
:
"""Get weather for a city."""
# This would normally call a weather API
return
f"Weather in
{
city
}
: 22degrees
{
unit
[
0
].
upper
()
}
"
Full example:
examples/snippets/servers/basic_tool.py
Tools can optionally receive a Context object by including a parameter with the
Context
type annotation. This context is automatically injected by the FastMCP framework and provides access to MCP capabilities:
from
mcp
.
server
.
fastmcp
import
Context
,
FastMCP
from
mcp
.
server
.
session
import
ServerSession
mcp
=
FastMCP
(
name
=
"Progress Example"
)
@
mcp
.
tool
()
async
def
long_running_task
(
task_name
:
str
,
ctx
:
Context
[
ServerSession
,
None
],
steps
:
int
=
5
)
->
str
:
"""Execute a task with progress updates."""
await
ctx
.
info
(
f"Starting:
{
task_name
}
"
)
for
i
in
range
(
steps
):
progress
=
(
i
+
1
)
/
steps
await
ctx
.
report_progress
(
progress
=
progress
,
total
=
1.0
,
message
=
f"Step
{
i
+
1
}
/
{
steps
}
"
,
        )
await
ctx
.
debug
(
f"Completed step
{
i
+
1
}
"
)
return
f"Task '
{
task_name
}
' completed"
Full example:
examples/snippets/servers/tool_progress.py
Structured Output
Tools will return structured results by default, if their return type
annotation is compatible. Otherwise, they will return unstructured results.
Structured output supports these return types:
Pydantic models (BaseModel subclasses)
TypedDicts
Dataclasses and other classes with type hints
dict[str, T]
(where T is any JSON-serializable type)
Primitive types (str, int, float, bool, bytes, None) - wrapped in
{"result": value}
Generic types (list, tuple, Union, Optional, etc.) - wrapped in
{"result": value}
Classes without type hints cannot be serialized for structured output. Only
classes with properly annotated attributes will be converted to Pydantic models
for schema generation and validation.
Structured results are automatically validated against the output schema
generated from the annotation. This ensures the tool returns well-typed,
validated data that clients can easily process.
Note:
For backward compatibility, unstructured results are also
returned. Unstructured results are provided for backward compatibility
with previous versions of the MCP specification, and are quirks-compatible
with previous versions of FastMCP in the current version of the SDK.
Note:
In cases where a tool function's return type annotation
causes the tool to be classified as structured
and this is undesirable
,
the  classification can be suppressed by passing
structured_output=False
to the
@tool
decorator.
"""Example showing structured output with tools."""
from
typing
import
TypedDict
from
pydantic
import
BaseModel
,
Field
from
mcp
.
server
.
fastmcp
import
FastMCP
mcp
=
FastMCP
(
"Structured Output Example"
)
# Using Pydantic models for rich structured data
class
WeatherData
(
BaseModel
):
"""Weather information structure."""
temperature
:
float
=
Field
(
description
=
"Temperature in Celsius"
)
humidity
:
float
=
Field
(
description
=
"Humidity percentage"
)
condition
:
str
wind_speed
:
float
@
mcp
.
tool
()
def
get_weather
(
city
:
str
)
->
WeatherData
:
"""Get weather for a city - returns structured data."""
# Simulated weather data
return
WeatherData
(
temperature
=
22.5
,
humidity
=
45.0
,
condition
=
"sunny"
,
wind_speed
=
5.2
,
    )
# Using TypedDict for simpler structures
class
LocationInfo
(
TypedDict
):
latitude
:
float
longitude
:
float
name
:
str
@
mcp
.
tool
()
def
get_location
(
address
:
str
)
->
LocationInfo
:
"""Get location coordinates"""
return
LocationInfo
(
latitude
=
51.5074
,
longitude
=
-
0.1278
,
name
=
"London, UK"
)
# Using dict[str, Any] for flexible schemas
@
mcp
.
tool
()
def
get_statistics
(
data_type
:
str
)
->
dict
[
str
,
float
]:
"""Get various statistics"""
return
{
"mean"
:
42.5
,
"median"
:
40.0
,
"std_dev"
:
5.2
}
# Ordinary classes with type hints work for structured output
class
UserProfile
:
name
:
str
age
:
int
email
:
str
|
None
=
None
def
__init__
(
self
,
name
:
str
,
age
:
int
,
email
:
str
|
None
=
None
):
self
.
name
=
name
self
.
age
=
age
self
.
email
=
email
@
mcp
.
tool
()
def
get_user
(
user_id
:
str
)
->
UserProfile
:
"""Get user profile - returns structured data"""
return
UserProfile
(
name
=
"Alice"
,
age
=
30
,
email
=
"alice@example.com"
)
# Classes WITHOUT type hints cannot be used for structured output
class
UntypedConfig
:
def
__init__
(
self
,
setting1
,
setting2
):
# type: ignore[reportMissingParameterType]
self
.
setting1
=
setting1
self
.
setting2
=
setting2
@
mcp
.
tool
()
def
get_config
()
->
UntypedConfig
:
"""This returns unstructured output - no schema generated"""
return
UntypedConfig
(
"value1"
,
"value2"
)
# Lists and other types are wrapped automatically
@
mcp
.
tool
()
def
list_cities
()
->
list
[
str
]:
"""Get a list of cities"""
return
[
"London"
,
"Paris"
,
"Tokyo"
]
# Returns: {"result": ["London", "Paris", "Tokyo"]}
@
mcp
.
tool
()
def
get_temperature
(
city
:
str
)
->
float
:
"""Get temperature as a simple float"""
return
22.5
# Returns: {"result": 22.5}
Full example:
examples/snippets/servers/structured_output.py
Prompts
Prompts are reusable templates that help LLMs interact with your server effectively:
from
mcp
.
server
.
fastmcp
import
FastMCP
from
mcp
.
server
.
fastmcp
.
prompts
import
base
mcp
=
FastMCP
(
name
=
"Prompt Example"
)
@
mcp
.
prompt
(
title
=
"Code Review"
)
def
review_code
(
code
:
str
)
->
str
:
return
f"Please review this code:
\n
\n
{
code
}
"
@
mcp
.
prompt
(
title
=
"Debug Assistant"
)
def
debug_error
(
error
:
str
)
->
list
[
base
.
Message
]:
return
[
base
.
UserMessage
(
"I'm seeing this error:"
),
base
.
UserMessage
(
error
),
base
.
AssistantMessage
(
"I'll help debug that. What have you tried so far?"
),
    ]
Full example:
examples/snippets/servers/basic_prompt.py
Icons
MCP servers can provide icons for UI display. Icons can be added to the server implementation, tools, resources, and prompts:
from
mcp
.
server
.
fastmcp
import
FastMCP
,
Icon
# Create an icon from a file path or URL
icon
=
Icon
(
src
=
"icon.png"
,
mimeType
=
"image/png"
,
sizes
=
"64x64"
)
# Add icons to server
mcp
=
FastMCP
(
"My Server"
,
website_url
=
"https://example.com"
,
icons
=
[
icon
]
)
# Add icons to tools, resources, and prompts
@
mcp
.
tool
(
icons
=
[
icon
])
def
my_tool
():
"""Tool with an icon."""
return
"result"
@
mcp
.
resource
(
"demo://resource"
,
icons
=
[
icon
])
def
my_resource
():
"""Resource with an icon."""
return
"content"
Full example:
examples/fastmcp/icons_demo.py
Images
FastMCP provides an
Image
class that automatically handles image data:
"""Example showing image handling with FastMCP."""
from
PIL
import
Image
as
PILImage
from
mcp
.
server
.
fastmcp
import
FastMCP
,
Image
mcp
=
FastMCP
(
"Image Example"
)
@
mcp
.
tool
()
def
create_thumbnail
(
image_path
:
str
)
->
Image
:
"""Create a thumbnail from an image"""
img
=
PILImage
.
open
(
image_path
)
img
.
thumbnail
((
100
,
100
))
return
Image
(
data
=
img
.
tobytes
(),
format
=
"png"
)
Full example:
examples/snippets/servers/images.py
Context
The Context object is automatically injected into tool and resource functions that request it via type hints. It provides access to MCP capabilities like logging, progress reporting, resource reading, user interaction, and request metadata.
Getting Context in Functions
To use context in a tool or resource function, add a parameter with the
Context
type annotation:
from
mcp
.
server
.
fastmcp
import
Context
,
FastMCP
mcp
=
FastMCP
(
name
=
"Context Example"
)
@
mcp
.
tool
()
async
def
my_tool
(
x
:
int
,
ctx
:
Context
)
->
str
:
"""Tool that uses context capabilities."""
# The context parameter can have any name as long as it's type-annotated
return
await
process_with_context
(
x
,
ctx
)
Context Properties and Methods
The Context object provides the following capabilities:
ctx.request_id
- Unique ID for the current request
ctx.client_id
- Client ID if available
ctx.fastmcp
- Access to the FastMCP server instance (see
FastMCP Properties
)
ctx.session
- Access to the underlying session for advanced communication (see
Session Properties and Methods
)
ctx.request_context
- Access to request-specific data and lifespan resources (see
Request Context Properties
)
await ctx.debug(message)
- Send debug log message
await ctx.info(message)
- Send info log message
await ctx.warning(message)
- Send warning log message
await ctx.error(message)
- Send error log message
await ctx.log(level, message, logger_name=None)
- Send log with custom level
await ctx.report_progress(progress, total=None, message=None)
- Report operation progress
await ctx.read_resource(uri)
- Read a resource by URI
await ctx.elicit(message, schema)
- Request additional information from user with validation
from
mcp
.
server
.
fastmcp
import
Context
,
FastMCP
from
mcp
.
server
.
session
import
ServerSession
mcp
=
FastMCP
(
name
=
"Progress Example"
)
@
mcp
.
tool
()
async
def
long_running_task
(
task_name
:
str
,
ctx
:
Context
[
ServerSession
,
None
],
steps
:
int
=
5
)
->
str
:
"""Execute a task with progress updates."""
await
ctx
.
info
(
f"Starting:
{
task_name
}
"
)
for
i
in
range
(
steps
):
progress
=
(
i
+
1
)
/
steps
await
ctx
.
report_progress
(
progress
=
progress
,
total
=
1.0
,
message
=
f"Step
{
i
+
1
}
/
{
steps
}
"
,
        )
await
ctx
.
debug
(
f"Completed step
{
i
+
1
}
"
)
return
f"Task '
{
task_name
}
' completed"
Full example:
examples/snippets/servers/tool_progress.py
Completions
MCP supports providing completion suggestions for prompt arguments and resource template parameters. With the context parameter, servers can provide completions based on previously resolved values:
Client usage:
"""
cd to the `examples/snippets` directory and run:
uv run completion-client
"""
import
asyncio
import
os
from
mcp
import
ClientSession
,
StdioServerParameters
from
mcp
.
client
.
stdio
import
stdio_client
from
mcp
.
types
import
PromptReference
,
ResourceTemplateReference
# Create server parameters for stdio connection
server_params
=
StdioServerParameters
(
command
=
"uv"
,
# Using uv to run the server
args
=
[
"run"
,
"server"
,
"completion"
,
"stdio"
],
# Server with completion support
env
=
{
"UV_INDEX"
:
os
.
environ
.
get
(
"UV_INDEX"
,
""
)},
)
async
def
run
():
"""Run the completion client example."""
async
with
stdio_client
(
server_params
)
as
(
read
,
write
):
async
with
ClientSession
(
read
,
write
)
as
session
:
# Initialize the connection
await
session
.
initialize
()
# List available resource templates
templates
=
await
session
.
list_resource_templates
()
print
(
"Available resource templates:"
)
for
template
in
templates
.
resourceTemplates
:
print
(
f"  -
{
template
.
uriTemplate
}
"
)
# List available prompts
prompts
=
await
session
.
list_prompts
()
print
(
"
\n
Available prompts:"
)
for
prompt
in
prompts
.
prompts
:
print
(
f"  -
{
prompt
.
name
}
"
)
# Complete resource template arguments
if
templates
.
resourceTemplates
:
template
=
templates
.
resourceTemplates
[
0
]
print
(
f"
\n
Completing arguments for resource template:
{
template
.
uriTemplate
}
"
)
# Complete without context
result
=
await
session
.
complete
(
ref
=
ResourceTemplateReference
(
type
=
"ref/resource"
,
uri
=
template
.
uriTemplate
),
argument
=
{
"name"
:
"owner"
,
"value"
:
"model"
},
                )
print
(
f"Completions for 'owner' starting with 'model':
{
result
.
completion
.
values
}
"
)
# Complete with context - repo suggestions based on owner
result
=
await
session
.
complete
(
ref
=
ResourceTemplateReference
(
type
=
"ref/resource"
,
uri
=
template
.
uriTemplate
),
argument
=
{
"name"
:
"repo"
,
"value"
:
""
},
context_arguments
=
{
"owner"
:
"modelcontextprotocol"
},
                )
print
(
f"Completions for 'repo' with owner='modelcontextprotocol':
{
result
.
completion
.
values
}
"
)
# Complete prompt arguments
if
prompts
.
prompts
:
prompt_name
=
prompts
.
prompts
[
0
].
name
print
(
f"
\n
Completing arguments for prompt:
{
prompt_name
}
"
)
result
=
await
session
.
complete
(
ref
=
PromptReference
(
type
=
"ref/prompt"
,
name
=
prompt_name
),
argument
=
{
"name"
:
"style"
,
"value"
:
""
},
                )
print
(
f"Completions for 'style' argument:
{
result
.
completion
.
values
}
"
)
def
main
():
"""Entry point for the completion client."""
asyncio
.
run
(
run
())
if
__name__
==
"__main__"
:
main
()
Full example:
examples/snippets/clients/completion_client.py
Elicitation
Request additional information from users. This example shows an Elicitation during a Tool Call:
from
pydantic
import
BaseModel
,
Field
from
mcp
.
server
.
fastmcp
import
Context
,
FastMCP
from
mcp
.
server
.
session
import
ServerSession
mcp
=
FastMCP
(
name
=
"Elicitation Example"
)
class
BookingPreferences
(
BaseModel
):
"""Schema for collecting user preferences."""
checkAlternative
:
bool
=
Field
(
description
=
"Would you like to check another date?"
)
alternativeDate
:
str
=
Field
(
default
=
"2024-12-26"
,
description
=
"Alternative date (YYYY-MM-DD)"
,
    )
@
mcp
.
tool
()
async
def
book_table
(
date
:
str
,
time
:
str
,
party_size
:
int
,
ctx
:
Context
[
ServerSession
,
None
])
->
str
:
"""Book a table with date availability check."""
# Check if date is available
if
date
==
"2024-12-25"
:
# Date unavailable - ask user for alternative
result
=
await
ctx
.
elicit
(
message
=
(
f"No tables available for
{
party_size
}
on
{
date
}
. Would you like to try another date?"
),
schema
=
BookingPreferences
,
        )
if
result
.
action
==
"accept"
and
result
.
data
:
if
result
.
data
.
checkAlternative
:
return
f"[SUCCESS] Booked for
{
result
.
data
.
alternativeDate
}
"
return
"[CANCELLED] No booking made"
return
"[CANCELLED] Booking cancelled"
# Date available
return
f"[SUCCESS] Booked for
{
date
}
at
{
time
}
"
Full example:
examples/snippets/servers/elicitation.py
Elicitation schemas support default values for all field types. Default values are automatically included in the JSON schema sent to clients, allowing them to pre-populate forms.
The
elicit()
method returns an
ElicitationResult
with:
action
: "accept", "decline", or "cancel"
data
: The validated response (only when accepted)
validation_error
: Any validation error message
Sampling
Tools can interact with LLMs through sampling (generating text):
from
mcp
.
server
.
fastmcp
import
Context
,
FastMCP
from
mcp
.
server
.
session
import
ServerSession
from
mcp
.
types
import
SamplingMessage
,
TextContent
mcp
=
FastMCP
(
name
=
"Sampling Example"
)
@
mcp
.
tool
()
async
def
generate_poem
(
topic
:
str
,
ctx
:
Context
[
ServerSession
,
None
])
->
str
:
"""Generate a poem using LLM sampling."""
prompt
=
f"Write a short poem about
{
topic
}
"
result
=
await
ctx
.
session
.
create_message
(
messages
=
[
SamplingMessage
(
role
=
"user"
,
content
=
TextContent
(
type
=
"text"
,
text
=
prompt
),
            )
        ],
max_tokens
=
100
,
    )
if
result
.
content
.
type
==
"text"
:
return
result
.
content
.
text
return
str
(
result
.
content
)
Full example:
examples/snippets/servers/sampling.py
Logging and Notifications
Tools can send logs and notifications through the context:
from
mcp
.
server
.
fastmcp
import
Context
,
FastMCP
from
mcp
.
server
.
session
import
ServerSession
mcp
=
FastMCP
(
name
=
"Notifications Example"
)
@
mcp
.
tool
()
async
def
process_data
(
data
:
str
,
ctx
:
Context
[
ServerSession
,
None
])
->
str
:
"""Process data with logging."""
# Different log levels
await
ctx
.
debug
(
f"Debug: Processing '
{
data
}
'"
)
await
ctx
.
info
(
"Info: Starting processing"
)
await
ctx
.
warning
(
"Warning: This is experimental"
)
await
ctx
.
error
(
"Error: (This is just a demo)"
)
# Notify about resource changes
await
ctx
.
session
.
send_resource_list_changed
()
return
f"Processed:
{
data
}
"
Full example:
examples/snippets/servers/notifications.py
Authentication
Authentication can be used by servers that want to expose tools accessing protected resources.
mcp.server.auth
implements OAuth 2.1 resource server functionality, where MCP servers act as Resource Servers (RS) that validate tokens issued by separate Authorization Servers (AS). This follows the
MCP authorization specification
and implements RFC 9728 (Protected Resource Metadata) for AS discovery.
MCP servers can use authentication by providing an implementation of the
TokenVerifier
protocol:
"""
Run from the repository root:
uv run examples/snippets/servers/oauth_server.py
"""
from
pydantic
import
AnyHttpUrl
from
mcp
.
server
.
auth
.
provider
import
AccessToken
,
TokenVerifier
from
mcp
.
server
.
auth
.
settings
import
AuthSettings
from
mcp
.
server
.
fastmcp
import
FastMCP
class
SimpleTokenVerifier
(
TokenVerifier
):
"""Simple token verifier for demonstration."""
async
def
verify_token
(
self
,
token
:
str
)
->
AccessToken
|
None
:
pass
# This is where you would implement actual token validation
# Create FastMCP instance as a Resource Server
mcp
=
FastMCP
(
"Weather Service"
,
# Token verifier for authentication
token_verifier
=
SimpleTokenVerifier
(),
# Auth settings for RFC 9728 Protected Resource Metadata
auth
=
AuthSettings
(
issuer_url
=
AnyHttpUrl
(
"https://auth.example.com"
),
# Authorization Server URL
resource_server_url
=
AnyHttpUrl
(
"http://localhost:3001"
),
# This server's URL
required_scopes
=
[
"user"
],
    ),
)
@
mcp
.
tool
()
async
def
get_weather
(
city
:
str
=
"London"
)
->
dict
[
str
,
str
]:
"""Get weather data for a city"""
return
{
"city"
:
city
,
"temperature"
:
"22"
,
"condition"
:
"Partly cloudy"
,
"humidity"
:
"65%"
,
    }
if
__name__
==
"__main__"
:
mcp
.
run
(
transport
=
"streamable-http"
)
Full example:
examples/snippets/servers/oauth_server.py
For a complete example with separate Authorization Server and Resource Server implementations, see
examples/servers/simple-auth/
.
Architecture:
Authorization Server (AS)
: Handles OAuth flows, user authentication, and token issuance
Resource Server (RS)
: Your MCP server that validates tokens and serves protected resources
Client
: Discovers AS through RFC 9728, obtains tokens, and uses them with the MCP server
See
TokenVerifier
for more details on implementing token validation.
FastMCP Properties
The FastMCP server instance accessible via
ctx.fastmcp
provides access to server configuration and metadata:
ctx.fastmcp.name
- The server's name as defined during initialization
ctx.fastmcp.instructions
- Server instructions/description provided to clients
ctx.fastmcp.website_url
- Optional website URL for the server
ctx.fastmcp.icons
- Optional list of icons for UI display
ctx.fastmcp.settings
- Complete server configuration object containing:
debug
- Debug mode flag
log_level
- Current logging level
host
and
port
- Server network configuration
mount_path
,
sse_path
,
streamable_http_path
- Transport paths
stateless_http
- Whether the server operates in stateless mode
And other configuration options
@
mcp
.
tool
()
def
server_info
(
ctx
:
Context
)
->
dict
:
"""Get information about the current server."""
return
{
"name"
:
ctx
.
fastmcp
.
name
,
"instructions"
:
ctx
.
fastmcp
.
instructions
,
"debug_mode"
:
ctx
.
fastmcp
.
settings
.
debug
,
"log_level"
:
ctx
.
fastmcp
.
settings
.
log_level
,
"host"
:
ctx
.
fastmcp
.
settings
.
host
,
"port"
:
ctx
.
fastmcp
.
settings
.
port
,
    }
Session Properties and Methods
The session object accessible via
ctx.session
provides advanced control over client communication:
ctx.session.client_params
- Client initialization parameters and declared capabilities
await ctx.session.send_log_message(level, data, logger)
- Send log messages with full control
await ctx.session.create_message(messages, max_tokens)
- Request LLM sampling/completion
await ctx.session.send_progress_notification(token, progress, total, message)
- Direct progress updates
await ctx.session.send_resource_updated(uri)
- Notify clients that a specific resource changed
await ctx.session.send_resource_list_changed()
- Notify clients that the resource list changed
await ctx.session.send_tool_list_changed()
- Notify clients that the tool list changed
await ctx.session.send_prompt_list_changed()
- Notify clients that the prompt list changed
@
mcp
.
tool
()
async
def
notify_data_update
(
resource_uri
:
str
,
ctx
:
Context
)
->
str
:
"""Update data and notify clients of the change."""
# Perform data update logic here
# Notify clients that this specific resource changed
await
ctx
.
session
.
send_resource_updated
(
AnyUrl
(
resource_uri
))
# If this affects the overall resource list, notify about that too
await
ctx
.
session
.
send_resource_list_changed
()
return
f"Updated
{
resource_uri
}
and notified clients"
Request Context Properties
The request context accessible via
ctx.request_context
contains request-specific information and resources:
ctx.request_context.lifespan_context
- Access to resources initialized during server startup
Database connections, configuration objects, shared services
Type-safe access to resources defined in your server's lifespan function
ctx.request_context.meta
- Request metadata from the client including:
progressToken
- Token for progress notifications
Other client-provided metadata
ctx.request_context.request
- The original MCP request object for advanced processing
ctx.request_context.request_id
- Unique identifier for this request
# Example with typed lifespan context
@
dataclass
class
AppContext
:
db
:
Database
config
:
AppConfig
@
mcp
.
tool
()
def
query_with_config
(
query
:
str
,
ctx
:
Context
)
->
str
:
"""Execute a query using shared database and configuration."""
# Access typed lifespan context
app_ctx
:
AppContext
=
ctx
.
request_context
.
lifespan_context
# Use shared resources
connection
=
app_ctx
.
db
settings
=
app_ctx
.
config
# Execute query with configuration
result
=
connection
.
execute
(
query
,
timeout
=
settings
.
query_timeout
)
return
str
(
result
)
Full lifespan example:
examples/snippets/servers/lifespan_example.py
Running Your Server
Development Mode
The fastest way to test and debug your server is with the MCP Inspector:
uv run mcp dev server.py
#
Add dependencies
uv run mcp dev server.py --with pandas --with numpy
#
Mount local code
uv run mcp dev server.py --with-editable
.
Claude Desktop Integration
Once your server is ready, install it in Claude Desktop:
uv run mcp install server.py
#
Custom name
uv run mcp install server.py --name
"
My Analytics Server
"
#
Environment variables
uv run mcp install server.py -v API_KEY=abc123 -v DB_URL=postgres://...
uv run mcp install server.py -f .env
Direct Execution
For advanced scenarios like custom deployments:
"""Example showing direct execution of an MCP server.
This is the simplest way to run an MCP server directly.
cd to the `examples/snippets` directory and run:
uv run direct-execution-server
or
python servers/direct_execution.py
"""
from
mcp
.
server
.
fastmcp
import
FastMCP
mcp
=
FastMCP
(
"My App"
)
@
mcp
.
tool
()
def
hello
(
name
:
str
=
"World"
)
->
str
:
"""Say hello to someone."""
return
f"Hello,
{
name
}
!"
def
main
():
"""Entry point for the direct execution server."""
mcp
.
run
()
if
__name__
==
"__main__"
:
main
()
Full example:
examples/snippets/servers/direct_execution.py
Run it with:
python servers/direct_execution.py
#
or
uv run mcp run servers/direct_execution.py
Note that
uv run mcp run
or
uv run mcp dev
only supports server using FastMCP and not the low-level server variant.
Streamable HTTP Transport
Note
: Streamable HTTP transport is superseding SSE transport for production deployments.
"""
Run from the repository root:
uv run examples/snippets/servers/streamable_config.py
"""
from
mcp
.
server
.
fastmcp
import
FastMCP
# Stateful server (maintains session state)
mcp
=
FastMCP
(
"StatefulServer"
)
# Other configuration options:
# Stateless server (no session persistence)
# mcp = FastMCP("StatelessServer", stateless_http=True)
# Stateless server (no session persistence, no sse stream with supported client)
# mcp = FastMCP("StatelessServer", stateless_http=True, json_response=True)
# Add a simple tool to demonstrate the server
@
mcp
.
tool
()
def
greet
(
name
:
str
=
"World"
)
->
str
:
"""Greet someone by name."""
return
f"Hello,
{
name
}
!"
# Run server with streamable_http transport
if
__name__
==
"__main__"
:
mcp
.
run
(
transport
=
"streamable-http"
)
Full example:
examples/snippets/servers/streamable_config.py
You can mount multiple FastMCP servers in a Starlette application:
"""
Run from the repository root:
uvicorn examples.snippets.servers.streamable_starlette_mount:app --reload
"""
import
contextlib
from
starlette
.
applications
import
Starlette
from
starlette
.
routing
import
Mount
from
mcp
.
server
.
fastmcp
import
FastMCP
# Create the Echo server
echo_mcp
=
FastMCP
(
name
=
"EchoServer"
,
stateless_http
=
True
)
@
echo_mcp
.
tool
()
def
echo
(
message
:
str
)
->
str
:
"""A simple echo tool"""
return
f"Echo:
{
message
}
"
# Create the Math server
math_mcp
=
FastMCP
(
name
=
"MathServer"
,
stateless_http
=
True
)
@
math_mcp
.
tool
()
def
add_two
(
n
:
int
)
->
int
:
"""Tool to add two to the input"""
return
n
+
2
# Create a combined lifespan to manage both session managers
@
contextlib
.
asynccontextmanager
async
def
lifespan
(
app
:
Starlette
):
async
with
contextlib
.
AsyncExitStack
()
as
stack
:
await
stack
.
enter_async_context
(
echo_mcp
.
session_manager
.
run
())
await
stack
.
enter_async_context
(
math_mcp
.
session_manager
.
run
())
yield
# Create the Starlette app and mount the MCP servers
app
=
Starlette
(
routes
=
[
Mount
(
"/echo"
,
echo_mcp
.
streamable_http_app
()),
Mount
(
"/math"
,
math_mcp
.
streamable_http_app
()),
    ],
lifespan
=
lifespan
,
)
# Note: Clients connect to http://localhost:8000/echo/mcp and http://localhost:8000/math/mcp
# To mount at the root of each path (e.g., /echo instead of /echo/mcp):
# echo_mcp.settings.streamable_http_path = "/"
# math_mcp.settings.streamable_http_path = "/"
Full example:
examples/snippets/servers/streamable_starlette_mount.py
For low level server with Streamable HTTP implementations, see:
Stateful server:
examples/servers/simple-streamablehttp/
Stateless server:
examples/servers/simple-streamablehttp-stateless/
The streamable HTTP transport supports:
Stateful and stateless operation modes
Resumability with event stores
JSON or SSE response formats
Better scalability for multi-node deployments
CORS Configuration for Browser-Based Clients
If you'd like your server to be accessible by browser-based MCP clients, you'll need to configure CORS headers. The
Mcp-Session-Id
header must be exposed for browser clients to access it:
from
starlette
.
applications
import
Starlette
from
starlette
.
middleware
.
cors
import
CORSMiddleware
# Create your Starlette app first
starlette_app
=
Starlette
(
routes
=
[...])
# Then wrap it with CORS middleware
starlette_app
=
CORSMiddleware
(
starlette_app
,
allow_origins
=
[
"*"
],
# Configure appropriately for production
allow_methods
=
[
"GET"
,
"POST"
,
"DELETE"
],
# MCP streamable HTTP methods
expose_headers
=
[
"Mcp-Session-Id"
],
)
This configuration is necessary because:
The MCP streamable HTTP transport uses the
Mcp-Session-Id
header for session management
Browsers restrict access to response headers unless explicitly exposed via CORS
Without this configuration, browser-based clients won't be able to read the session ID from initialization responses
Mounting to an Existing ASGI Server
By default, SSE servers are mounted at
/sse
and Streamable HTTP servers are mounted at
/mcp
. You can customize these paths using the methods described below.
For more information on mounting applications in Starlette, see the
Starlette documentation
.
StreamableHTTP servers
You can mount the StreamableHTTP server to an existing ASGI server using the
streamable_http_app
method. This allows you to integrate the StreamableHTTP server with other ASGI applications.
Basic mounting
"""
Basic example showing how to mount StreamableHTTP server in Starlette.
Run from the repository root:
uvicorn examples.snippets.servers.streamable_http_basic_mounting:app --reload
"""
from
starlette
.
applications
import
Starlette
from
starlette
.
routing
import
Mount
from
mcp
.
server
.
fastmcp
import
FastMCP
# Create MCP server
mcp
=
FastMCP
(
"My App"
)
@
mcp
.
tool
()
def
hello
()
->
str
:
"""A simple hello tool"""
return
"Hello from MCP!"
# Mount the StreamableHTTP server to the existing ASGI server
app
=
Starlette
(
routes
=
[
Mount
(
"/"
,
app
=
mcp
.
streamable_http_app
()),
    ]
)
Full example:
examples/snippets/servers/streamable_http_basic_mounting.py
Host-based routing
"""
Example showing how to mount StreamableHTTP server using Host-based routing.
Run from the repository root:
uvicorn examples.snippets.servers.streamable_http_host_mounting:app --reload
"""
from
starlette
.
applications
import
Starlette
from
starlette
.
routing
import
Host
from
mcp
.
server
.
fastmcp
import
FastMCP
# Create MCP server
mcp
=
FastMCP
(
"MCP Host App"
)
@
mcp
.
tool
()
def
domain_info
()
->
str
:
"""Get domain-specific information"""
return
"This is served from mcp.acme.corp"
# Mount using Host-based routing
app
=
Starlette
(
routes
=
[
Host
(
"mcp.acme.corp"
,
app
=
mcp
.
streamable_http_app
()),
    ]
)
Full example:
examples/snippets/servers/streamable_http_host_mounting.py
Multiple servers with path configuration
"""
Example showing how to mount multiple StreamableHTTP servers with path configuration.
Run from the repository root:
uvicorn examples.snippets.servers.streamable_http_multiple_servers:app --reload
"""
from
starlette
.
applications
import
Starlette
from
starlette
.
routing
import
Mount
from
mcp
.
server
.
fastmcp
import
FastMCP
# Create multiple MCP servers
api_mcp
=
FastMCP
(
"API Server"
)
chat_mcp
=
FastMCP
(
"Chat Server"
)
@
api_mcp
.
tool
()
def
api_status
()
->
str
:
"""Get API status"""
return
"API is running"
@
chat_mcp
.
tool
()
def
send_message
(
message
:
str
)
->
str
:
"""Send a chat message"""
return
f"Message sent:
{
message
}
"
# Configure servers to mount at the root of each path
# This means endpoints will be at /api and /chat instead of /api/mcp and /chat/mcp
api_mcp
.
settings
.
streamable_http_path
=
"/"
chat_mcp
.
settings
.
streamable_http_path
=
"/"
# Mount the servers
app
=
Starlette
(
routes
=
[
Mount
(
"/api"
,
app
=
api_mcp
.
streamable_http_app
()),
Mount
(
"/chat"
,
app
=
chat_mcp
.
streamable_http_app
()),
    ]
)
Full example:
examples/snippets/servers/streamable_http_multiple_servers.py
Path configuration at initialization
"""
Example showing path configuration during FastMCP initialization.
Run from the repository root:
uvicorn examples.snippets.servers.streamable_http_path_config:app --reload
"""
from
starlette
.
applications
import
Starlette
from
starlette
.
routing
import
Mount
from
mcp
.
server
.
fastmcp
import
FastMCP
# Configure streamable_http_path during initialization
# This server will mount at the root of wherever it's mounted
mcp_at_root
=
FastMCP
(
"My Server"
,
streamable_http_path
=
"/"
)
@
mcp_at_root
.
tool
()
def
process_data
(
data
:
str
)
->
str
:
"""Process some data"""
return
f"Processed:
{
data
}
"
# Mount at /process - endpoints will be at /process instead of /process/mcp
app
=
Starlette
(
routes
=
[
Mount
(
"/process"
,
app
=
mcp_at_root
.
streamable_http_app
()),
    ]
)
Full example:
examples/snippets/servers/streamable_http_path_config.py
SSE servers
Note
: SSE transport is being superseded by
Streamable HTTP transport
.
You can mount the SSE server to an existing ASGI server using the
sse_app
method. This allows you to integrate the SSE server with other ASGI applications.
from
starlette
.
applications
import
Starlette
from
starlette
.
routing
import
Mount
,
Host
from
mcp
.
server
.
fastmcp
import
FastMCP
mcp
=
FastMCP
(
"My App"
)
# Mount the SSE server to the existing ASGI server
app
=
Starlette
(
routes
=
[
Mount
(
'/'
,
app
=
mcp
.
sse_app
()),
    ]
)
# or dynamically mount as host
app
.
router
.
routes
.
append
(
Host
(
'mcp.acme.corp'
,
app
=
mcp
.
sse_app
()))
When mounting multiple MCP servers under different paths, you can configure the mount path in several ways:
from
starlette
.
applications
import
Starlette
from
starlette
.
routing
import
Mount
from
mcp
.
server
.
fastmcp
import
FastMCP
# Create multiple MCP servers
github_mcp
=
FastMCP
(
"GitHub API"
)
browser_mcp
=
FastMCP
(
"Browser"
)
curl_mcp
=
FastMCP
(
"Curl"
)
search_mcp
=
FastMCP
(
"Search"
)
# Method 1: Configure mount paths via settings (recommended for persistent configuration)
github_mcp
.
settings
.
mount_path
=
"/github"
browser_mcp
.
settings
.
mount_path
=
"/browser"
# Method 2: Pass mount path directly to sse_app (preferred for ad-hoc mounting)
# This approach doesn't modify the server's settings permanently
# Create Starlette app with multiple mounted servers
app
=
Starlette
(
routes
=
[
# Using settings-based configuration
Mount
(
"/github"
,
app
=
github_mcp
.
sse_app
()),
Mount
(
"/browser"
,
app
=
browser_mcp
.
sse_app
()),
# Using direct mount path parameter
Mount
(
"/curl"
,
app
=
curl_mcp
.
sse_app
(
"/curl"
)),
Mount
(
"/search"
,
app
=
search_mcp
.
sse_app
(
"/search"
)),
    ]
)
# Method 3: For direct execution, you can also pass the mount path to run()
if
__name__
==
"__main__"
:
search_mcp
.
run
(
transport
=
"sse"
,
mount_path
=
"/search"
)
For more information on mounting applications in Starlette, see the
Starlette documentation
.
Advanced Usage
Low-Level Server
For more control, you can use the low-level server implementation directly. This gives you full access to the protocol and allows you to customize every aspect of your server, including lifecycle management through the lifespan API:
"""
Run from the repository root:
uv run examples/snippets/servers/lowlevel/lifespan.py
"""
from
collections
.
abc
import
AsyncIterator
from
contextlib
import
asynccontextmanager
from
typing
import
Any
import
mcp
.
server
.
stdio
import
mcp
.
types
as
types
from
mcp
.
server
.
lowlevel
import
NotificationOptions
,
Server
from
mcp
.
server
.
models
import
InitializationOptions
# Mock database class for example
class
Database
:
"""Mock database class for example."""
@
classmethod
async
def
connect
(
cls
)
->
"Database"
:
"""Connect to database."""
print
(
"Database connected"
)
return
cls
()
async
def
disconnect
(
self
)
->
None
:
"""Disconnect from database."""
print
(
"Database disconnected"
)
async
def
query
(
self
,
query_str
:
str
)
->
list
[
dict
[
str
,
str
]]:
"""Execute a query."""
# Simulate database query
return
[{
"id"
:
"1"
,
"name"
:
"Example"
,
"query"
:
query_str
}]
@
asynccontextmanager
async
def
server_lifespan
(
_server
:
Server
)
->
AsyncIterator
[
dict
[
str
,
Any
]]:
"""Manage server startup and shutdown lifecycle."""
# Initialize resources on startup
db
=
await
Database
.
connect
()
try
:
yield
{
"db"
:
db
}
finally
:
# Clean up on shutdown
await
db
.
disconnect
()
# Pass lifespan to server
server
=
Server
(
"example-server"
,
lifespan
=
server_lifespan
)
@
server
.
list_tools
()
async
def
handle_list_tools
()
->
list
[
types
.
Tool
]:
"""List available tools."""
return
[
types
.
Tool
(
name
=
"query_db"
,
description
=
"Query the database"
,
inputSchema
=
{
"type"
:
"object"
,
"properties"
: {
"query"
: {
"type"
:
"string"
,
"description"
:
"SQL query to execute"
}},
"required"
: [
"query"
],
            },
        )
    ]
@
server
.
call_tool
()
async
def
query_db
(
name
:
str
,
arguments
:
dict
[
str
,
Any
])
->
list
[
types
.
TextContent
]:
"""Handle database query tool call."""
if
name
!=
"query_db"
:
raise
ValueError
(
f"Unknown tool:
{
name
}
"
)
# Access lifespan context
ctx
=
server
.
request_context
db
=
ctx
.
lifespan_context
[
"db"
]
# Execute query
results
=
await
db
.
query
(
arguments
[
"query"
])
return
[
types
.
TextContent
(
type
=
"text"
,
text
=
f"Query results:
{
results
}
"
)]
async
def
run
():
"""Run the server with lifespan management."""
async
with
mcp
.
server
.
stdio
.
stdio_server
()
as
(
read_stream
,
write_stream
):
await
server
.
run
(
read_stream
,
write_stream
,
InitializationOptions
(
server_name
=
"example-server"
,
server_version
=
"0.1.0"
,
capabilities
=
server
.
get_capabilities
(
notification_options
=
NotificationOptions
(),
experimental_capabilities
=
{},
                ),
            ),
        )
if
__name__
==
"__main__"
:
import
asyncio
asyncio
.
run
(
run
())
Full example:
examples/snippets/servers/lowlevel/lifespan.py
The lifespan API provides:
A way to initialize resources when the server starts and clean them up when it stops
Access to initialized resources through the request context in handlers
Type-safe context passing between lifespan and request handlers
"""
Run from the repository root:
uv run examples/snippets/servers/lowlevel/basic.py
"""
import
asyncio
import
mcp
.
server
.
stdio
import
mcp
.
types
as
types
from
mcp
.
server
.
lowlevel
import
NotificationOptions
,
Server
from
mcp
.
server
.
models
import
InitializationOptions
# Create a server instance
server
=
Server
(
"example-server"
)
@
server
.
list_prompts
()
async
def
handle_list_prompts
()
->
list
[
types
.
Prompt
]:
"""List available prompts."""
return
[
types
.
Prompt
(
name
=
"example-prompt"
,
description
=
"An example prompt template"
,
arguments
=
[
types
.
PromptArgument
(
name
=
"arg1"
,
description
=
"Example argument"
,
required
=
True
)],
        )
    ]
@
server
.
get_prompt
()
async
def
handle_get_prompt
(
name
:
str
,
arguments
:
dict
[
str
,
str
]
|
None
)
->
types
.
GetPromptResult
:
"""Get a specific prompt by name."""
if
name
!=
"example-prompt"
:
raise
ValueError
(
f"Unknown prompt:
{
name
}
"
)
arg1_value
=
(
arguments
or
{}).
get
(
"arg1"
,
"default"
)
return
types
.
GetPromptResult
(
description
=
"Example prompt"
,
messages
=
[
types
.
PromptMessage
(
role
=
"user"
,
content
=
types
.
TextContent
(
type
=
"text"
,
text
=
f"Example prompt text with argument:
{
arg1_value
}
"
),
            )
        ],
    )
async
def
run
():
"""Run the basic low-level server."""
async
with
mcp
.
server
.
stdio
.
stdio_server
()
as
(
read_stream
,
write_stream
):
await
server
.
run
(
read_stream
,
write_stream
,
InitializationOptions
(
server_name
=
"example"
,
server_version
=
"0.1.0"
,
capabilities
=
server
.
get_capabilities
(
notification_options
=
NotificationOptions
(),
experimental_capabilities
=
{},
                ),
            ),
        )
if
__name__
==
"__main__"
:
asyncio
.
run
(
run
())
Full example:
examples/snippets/servers/lowlevel/basic.py
Caution: The
uv run mcp run
and
uv run mcp dev
tool doesn't support low-level server.
Structured Output Support
The low-level server supports structured output for tools, allowing you to return both human-readable content and machine-readable structured data. Tools can define an
outputSchema
to validate their structured output:
"""
Run from the repository root:
uv run examples/snippets/servers/lowlevel/structured_output.py
"""
import
asyncio
from
typing
import
Any
import
mcp
.
server
.
stdio
import
mcp
.
types
as
types
from
mcp
.
server
.
lowlevel
import
NotificationOptions
,
Server
from
mcp
.
server
.
models
import
InitializationOptions
server
=
Server
(
"example-server"
)
@
server
.
list_tools
()
async
def
list_tools
()
->
list
[
types
.
Tool
]:
"""List available tools with structured output schemas."""
return
[
types
.
Tool
(
name
=
"get_weather"
,
description
=
"Get current weather for a city"
,
inputSchema
=
{
"type"
:
"object"
,
"properties"
: {
"city"
: {
"type"
:
"string"
,
"description"
:
"City name"
}},
"required"
: [
"city"
],
            },
outputSchema
=
{
"type"
:
"object"
,
"properties"
: {
"temperature"
: {
"type"
:
"number"
,
"description"
:
"Temperature in Celsius"
},
"condition"
: {
"type"
:
"string"
,
"description"
:
"Weather condition"
},
"humidity"
: {
"type"
:
"number"
,
"description"
:
"Humidity percentage"
},
"city"
: {
"type"
:
"string"
,
"description"
:
"City name"
},
                },
"required"
: [
"temperature"
,
"condition"
,
"humidity"
,
"city"
],
            },
        )
    ]
@
server
.
call_tool
()
async
def
call_tool
(
name
:
str
,
arguments
:
dict
[
str
,
Any
])
->
dict
[
str
,
Any
]:
"""Handle tool calls with structured output."""
if
name
==
"get_weather"
:
city
=
arguments
[
"city"
]
# Simulated weather data - in production, call a weather API
weather_data
=
{
"temperature"
:
22.5
,
"condition"
:
"partly cloudy"
,
"humidity"
:
65
,
"city"
:
city
,
# Include the requested city
}
# low-level server will validate structured output against the tool's
# output schema, and additionally serialize it into a TextContent block
# for backwards compatibility with pre-2025-06-18 clients.
return
weather_data
else
:
raise
ValueError
(
f"Unknown tool:
{
name
}
"
)
async
def
run
():
"""Run the structured output server."""
async
with
mcp
.
server
.
stdio
.
stdio_server
()
as
(
read_stream
,
write_stream
):
await
server
.
run
(
read_stream
,
write_stream
,
InitializationOptions
(
server_name
=
"structured-output-example"
,
server_version
=
"0.1.0"
,
capabilities
=
server
.
get_capabilities
(
notification_options
=
NotificationOptions
(),
experimental_capabilities
=
{},
                ),
            ),
        )
if
__name__
==
"__main__"
:
asyncio
.
run
(
run
())
Full example:
examples/snippets/servers/lowlevel/structured_output.py
Tools can return data in three ways:
Content only
: Return a list of content blocks (default behavior before spec revision 2025-06-18)
Structured data only
: Return a dictionary that will be serialized to JSON (Introduced in spec revision 2025-06-18)
Both
: Return a tuple of (content, structured_data) preferred option to use for backwards compatibility
When an
outputSchema
is defined, the server automatically validates the structured output against the schema. This ensures type safety and helps catch errors early.
Pagination (Advanced)
For servers that need to handle large datasets, the low-level server provides paginated versions of list operations. This is an optional optimization - most servers won't need pagination unless they're dealing with hundreds or thousands of items.
Server-side Implementation
"""
Example of implementing pagination with MCP server decorators.
"""
from
pydantic
import
AnyUrl
import
mcp
.
types
as
types
from
mcp
.
server
.
lowlevel
import
Server
# Initialize the server
server
=
Server
(
"paginated-server"
)
# Sample data to paginate
ITEMS
=
[
f"Item
{
i
}
"
for
i
in
range
(
1
,
101
)]
# 100 items
@
server
.
list_resources
()
async
def
list_resources_paginated
(
request
:
types
.
ListResourcesRequest
)
->
types
.
ListResourcesResult
:
"""List resources with pagination support."""
page_size
=
10
# Extract cursor from request params
cursor
=
request
.
params
.
cursor
if
request
.
params
is
not
None
else
None
# Parse cursor to get offset
start
=
0
if
cursor
is
None
else
int
(
cursor
)
end
=
start
+
page_size
# Get page of resources
page_items
=
[
types
.
Resource
(
uri
=
AnyUrl
(
f"resource://items/
{
item
}
"
),
name
=
item
,
description
=
f"Description for
{
item
}
"
)
for
item
in
ITEMS
[
start
:
end
]
    ]
# Determine next cursor
next_cursor
=
str
(
end
)
if
end
<
len
(
ITEMS
)
else
None
return
types
.
ListResourcesResult
(
resources
=
page_items
,
nextCursor
=
next_cursor
)
Full example:
examples/snippets/servers/pagination_example.py
Client-side Consumption
"""
Example of consuming paginated MCP endpoints from a client.
"""
import
asyncio
from
mcp
.
client
.
session
import
ClientSession
from
mcp
.
client
.
stdio
import
StdioServerParameters
,
stdio_client
from
mcp
.
types
import
Resource
async
def
list_all_resources
()
->
None
:
"""Fetch all resources using pagination."""
async
with
stdio_client
(
StdioServerParameters
(
command
=
"uv"
,
args
=
[
"run"
,
"mcp-simple-pagination"
]))
as
(
read
,
write
,
    ):
async
with
ClientSession
(
read
,
write
)
as
session
:
await
session
.
initialize
()
all_resources
:
list
[
Resource
]
=
[]
cursor
=
None
while
True
:
# Fetch a page of resources
result
=
await
session
.
list_resources
(
cursor
=
cursor
)
all_resources
.
extend
(
result
.
resources
)
print
(
f"Fetched
{
len
(
result
.
resources
)
}
resources"
)
# Check if there are more pages
if
result
.
nextCursor
:
cursor
=
result
.
nextCursor
else
:
break
print
(
f"Total resources:
{
len
(
all_resources
)
}
"
)
if
__name__
==
"__main__"
:
asyncio
.
run
(
list_all_resources
())
Full example:
examples/snippets/clients/pagination_client.py
Key Points
Cursors are opaque strings
- the server defines the format (numeric offsets, timestamps, etc.)
Return
nextCursor=None
when there are no more pages
Backward compatible
- clients that don't support pagination will still work (they'll just get the first page)
Flexible page sizes
- Each endpoint can define its own page size based on data characteristics
See the
simple-pagination example
for a complete implementation.
Writing MCP Clients
The SDK provides a high-level client interface for connecting to MCP servers using various
transports
:
"""
cd to the `examples/snippets/clients` directory and run:
uv run client
"""
import
asyncio
import
os
from
pydantic
import
AnyUrl
from
mcp
import
ClientSession
,
StdioServerParameters
,
types
from
mcp
.
client
.
stdio
import
stdio_client
from
mcp
.
shared
.
context
import
RequestContext
# Create server parameters for stdio connection
server_params
=
StdioServerParameters
(
command
=
"uv"
,
# Using uv to run the server
args
=
[
"run"
,
"server"
,
"fastmcp_quickstart"
,
"stdio"
],
# We're already in snippets dir
env
=
{
"UV_INDEX"
:
os
.
environ
.
get
(
"UV_INDEX"
,
""
)},
)
# Optional: create a sampling callback
async
def
handle_sampling_message
(
context
:
RequestContext
[
ClientSession
,
None
],
params
:
types
.
CreateMessageRequestParams
)
->
types
.
CreateMessageResult
:
print
(
f"Sampling request:
{
params
.
messages
}
"
)
return
types
.
CreateMessageResult
(
role
=
"assistant"
,
content
=
types
.
TextContent
(
type
=
"text"
,
text
=
"Hello, world! from model"
,
        ),
model
=
"gpt-3.5-turbo"
,
stopReason
=
"endTurn"
,
    )
async
def
run
():
async
with
stdio_client
(
server_params
)
as
(
read
,
write
):
async
with
ClientSession
(
read
,
write
,
sampling_callback
=
handle_sampling_message
)
as
session
:
# Initialize the connection
await
session
.
initialize
()
# List available prompts
prompts
=
await
session
.
list_prompts
()
print
(
f"Available prompts:
{
[
p
.
name
for
p
in
prompts
.
prompts
]
}
"
)
# Get a prompt (greet_user prompt from fastmcp_quickstart)
if
prompts
.
prompts
:
prompt
=
await
session
.
get_prompt
(
"greet_user"
,
arguments
=
{
"name"
:
"Alice"
,
"style"
:
"friendly"
})
print
(
f"Prompt result:
{
prompt
.
messages
[
0
].
content
}
"
)
# List available resources
resources
=
await
session
.
list_resources
()
print
(
f"Available resources:
{
[
r
.
uri
for
r
in
resources
.
resources
]
}
"
)
# List available tools
tools
=
await
session
.
list_tools
()
print
(
f"Available tools:
{
[
t
.
name
for
t
in
tools
.
tools
]
}
"
)
# Read a resource (greeting resource from fastmcp_quickstart)
resource_content
=
await
session
.
read_resource
(
AnyUrl
(
"greeting://World"
))
content_block
=
resource_content
.
contents
[
0
]
if
isinstance
(
content_block
,
types
.
TextContent
):
print
(
f"Resource content:
{
content_block
.
text
}
"
)
# Call a tool (add tool from fastmcp_quickstart)
result
=
await
session
.
call_tool
(
"add"
,
arguments
=
{
"a"
:
5
,
"b"
:
3
})
result_unstructured
=
result
.
content
[
0
]
if
isinstance
(
result_unstructured
,
types
.
TextContent
):
print
(
f"Tool result:
{
result_unstructured
.
text
}
"
)
result_structured
=
result
.
structuredContent
print
(
f"Structured tool result:
{
result_structured
}
"
)
def
main
():
"""Entry point for the client script."""
asyncio
.
run
(
run
())
if
__name__
==
"__main__"
:
main
()
Full example:
examples/snippets/clients/stdio_client.py
Clients can also connect using
Streamable HTTP transport
:
"""
Run from the repository root:
uv run examples/snippets/clients/streamable_basic.py
"""
import
asyncio
from
mcp
import
ClientSession
from
mcp
.
client
.
streamable_http
import
streamablehttp_client
async
def
main
():
# Connect to a streamable HTTP server
async
with
streamablehttp_client
(
"http://localhost:8000/mcp"
)
as
(
read_stream
,
write_stream
,
_
,
    ):
# Create a session using the client streams
async
with
ClientSession
(
read_stream
,
write_stream
)
as
session
:
# Initialize the connection
await
session
.
initialize
()
# List available tools
tools
=
await
session
.
list_tools
()
print
(
f"Available tools:
{
[
tool
.
name
for
tool
in
tools
.
tools
]
}
"
)
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
Full example:
examples/snippets/clients/streamable_basic.py
Client Display Utilities
When building MCP clients, the SDK provides utilities to help display human-readable names for tools, resources, and prompts:
"""
cd to the `examples/snippets` directory and run:
uv run display-utilities-client
"""
import
asyncio
import
os
from
mcp
import
ClientSession
,
StdioServerParameters
from
mcp
.
client
.
stdio
import
stdio_client
from
mcp
.
shared
.
metadata_utils
import
get_display_name
# Create server parameters for stdio connection
server_params
=
StdioServerParameters
(
command
=
"uv"
,
# Using uv to run the server
args
=
[
"run"
,
"server"
,
"fastmcp_quickstart"
,
"stdio"
],
env
=
{
"UV_INDEX"
:
os
.
environ
.
get
(
"UV_INDEX"
,
""
)},
)
async
def
display_tools
(
session
:
ClientSession
):
"""Display available tools with human-readable names"""
tools_response
=
await
session
.
list_tools
()
for
tool
in
tools_response
.
tools
:
# get_display_name() returns the title if available, otherwise the name
display_name
=
get_display_name
(
tool
)
print
(
f"Tool:
{
display_name
}
"
)
if
tool
.
description
:
print
(
f"
{
tool
.
description
}
"
)
async
def
display_resources
(
session
:
ClientSession
):
"""Display available resources with human-readable names"""
resources_response
=
await
session
.
list_resources
()
for
resource
in
resources_response
.
resources
:
display_name
=
get_display_name
(
resource
)
print
(
f"Resource:
{
display_name
}
(
{
resource
.
uri
}
)"
)
templates_response
=
await
session
.
list_resource_templates
()
for
template
in
templates_response
.
resourceTemplates
:
display_name
=
get_display_name
(
template
)
print
(
f"Resource Template:
{
display_name
}
"
)
async
def
run
():
"""Run the display utilities example."""
async
with
stdio_client
(
server_params
)
as
(
read
,
write
):
async
with
ClientSession
(
read
,
write
)
as
session
:
# Initialize the connection
await
session
.
initialize
()
print
(
"=== Available Tools ==="
)
await
display_tools
(
session
)
print
(
"
\n
=== Available Resources ==="
)
await
display_resources
(
session
)
def
main
():
"""Entry point for the display utilities client."""
asyncio
.
run
(
run
())
if
__name__
==
"__main__"
:
main
()
Full example:
examples/snippets/clients/display_utilities.py
The
get_display_name()
function implements the proper precedence rules for displaying names:
For tools:
title
>
annotations.title
>
name
For other objects:
title
>
name
This ensures your client UI shows the most user-friendly names that servers provide.
OAuth Authentication for Clients
The SDK includes
authorization support
for connecting to protected MCP servers:
"""
Before running, specify running MCP RS server URL.
To spin up RS server locally, see
examples/servers/simple-auth/README.md
cd to the `examples/snippets` directory and run:
uv run oauth-client
"""
import
asyncio
from
urllib
.
parse
import
parse_qs
,
urlparse
from
pydantic
import
AnyUrl
from
mcp
import
ClientSession
from
mcp
.
client
.
auth
import
OAuthClientProvider
,
TokenStorage
from
mcp
.
client
.
streamable_http
import
streamablehttp_client
from
mcp
.
shared
.
auth
import
OAuthClientInformationFull
,
OAuthClientMetadata
,
OAuthToken
class
InMemoryTokenStorage
(
TokenStorage
):
"""Demo In-memory token storage implementation."""
def
__init__
(
self
):
self
.
tokens
:
OAuthToken
|
None
=
None
self
.
client_info
:
OAuthClientInformationFull
|
None
=
None
async
def
get_tokens
(
self
)
->
OAuthToken
|
None
:
"""Get stored tokens."""
return
self
.
tokens
async
def
set_tokens
(
self
,
tokens
:
OAuthToken
)
->
None
:
"""Store tokens."""
self
.
tokens
=
tokens
async
def
get_client_info
(
self
)
->
OAuthClientInformationFull
|
None
:
"""Get stored client information."""
return
self
.
client_info
async
def
set_client_info
(
self
,
client_info
:
OAuthClientInformationFull
)
->
None
:
"""Store client information."""
self
.
client_info
=
client_info
async
def
handle_redirect
(
auth_url
:
str
)
->
None
:
print
(
f"Visit:
{
auth_url
}
"
)
async
def
handle_callback
()
->
tuple
[
str
,
str
|
None
]:
callback_url
=
input
(
"Paste callback URL: "
)
params
=
parse_qs
(
urlparse
(
callback_url
).
query
)
return
params
[
"code"
][
0
],
params
.
get
(
"state"
, [
None
])[
0
]
async
def
main
():
"""Run the OAuth client example."""
oauth_auth
=
OAuthClientProvider
(
server_url
=
"http://localhost:8001"
,
client_metadata
=
OAuthClientMetadata
(
client_name
=
"Example MCP Client"
,
redirect_uris
=
[
AnyUrl
(
"http://localhost:3000/callback"
)],
grant_types
=
[
"authorization_code"
,
"refresh_token"
],
response_types
=
[
"code"
],
scope
=
"user"
,
        ),
storage
=
InMemoryTokenStorage
(),
redirect_handler
=
handle_redirect
,
callback_handler
=
handle_callback
,
    )
async
with
streamablehttp_client
(
"http://localhost:8001/mcp"
,
auth
=
oauth_auth
)
as
(
read
,
write
,
_
):
async
with
ClientSession
(
read
,
write
)
as
session
:
await
session
.
initialize
()
tools
=
await
session
.
list_tools
()
print
(
f"Available tools:
{
[
tool
.
name
for
tool
in
tools
.
tools
]
}
"
)
resources
=
await
session
.
list_resources
()
print
(
f"Available resources:
{
[
r
.
uri
for
r
in
resources
.
resources
]
}
"
)
def
run
():
asyncio
.
run
(
main
())
if
__name__
==
"__main__"
:
run
()
Full example:
examples/snippets/clients/oauth_client.py
For a complete working example, see
examples/clients/simple-auth-client/
.
Parsing Tool Results
When calling tools through MCP, the
CallToolResult
object contains the tool's response in a structured format. Understanding how to parse this result is essential for properly handling tool outputs.
"""examples/snippets/clients/parsing_tool_results.py"""
import
asyncio
from
mcp
import
ClientSession
,
StdioServerParameters
,
types
from
mcp
.
client
.
stdio
import
stdio_client
async
def
parse_tool_results
():
"""Demonstrates how to parse different types of content in CallToolResult."""
server_params
=
StdioServerParameters
(
command
=
"python"
,
args
=
[
"path/to/mcp_server.py"
]
    )
async
with
stdio_client
(
server_params
)
as
(
read
,
write
):
async
with
ClientSession
(
read
,
write
)
as
session
:
await
session
.
initialize
()
# Example 1: Parsing text content
result
=
await
session
.
call_tool
(
"get_data"
, {
"format"
:
"text"
})
for
content
in
result
.
content
:
if
isinstance
(
content
,
types
.
TextContent
):
print
(
f"Text:
{
content
.
text
}
"
)
# Example 2: Parsing structured content from JSON tools
result
=
await
session
.
call_tool
(
"get_user"
, {
"id"
:
"123"
})
if
hasattr
(
result
,
"structuredContent"
)
and
result
.
structuredContent
:
# Access structured data directly
user_data
=
result
.
structuredContent
print
(
f"User:
{
user_data
.
get
(
'name'
)
}
, Age:
{
user_data
.
get
(
'age'
)
}
"
)
# Example 3: Parsing embedded resources
result
=
await
session
.
call_tool
(
"read_config"
, {})
for
content
in
result
.
content
:
if
isinstance
(
content
,
types
.
EmbeddedResource
):
resource
=
content
.
resource
if
isinstance
(
resource
,
types
.
TextResourceContents
):
print
(
f"Config from
{
resource
.
uri
}
:
{
resource
.
text
}
"
)
elif
isinstance
(
resource
,
types
.
BlobResourceContents
):
print
(
f"Binary data from
{
resource
.
uri
}
"
)
# Example 4: Parsing image content
result
=
await
session
.
call_tool
(
"generate_chart"
, {
"data"
: [
1
,
2
,
3
]})
for
content
in
result
.
content
:
if
isinstance
(
content
,
types
.
ImageContent
):
print
(
f"Image (
{
content
.
mimeType
}
):
{
len
(
content
.
data
)
}
bytes"
)
# Example 5: Handling errors
result
=
await
session
.
call_tool
(
"failing_tool"
, {})
if
result
.
isError
:
print
(
"Tool execution failed!"
)
for
content
in
result
.
content
:
if
isinstance
(
content
,
types
.
TextContent
):
print
(
f"Error:
{
content
.
text
}
"
)
async
def
main
():
await
parse_tool_results
()
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
MCP Primitives
The MCP protocol defines three core primitives that servers can implement:
Primitive
Control
Description
Example Use
Prompts
User-controlled
Interactive templates invoked by user choice
Slash commands, menu options
Resources
Application-controlled
Contextual data managed by the client application
File contents, API responses
Tools
Model-controlled
Functions exposed to the LLM to take actions
API calls, data updates
Server Capabilities
MCP servers declare capabilities during initialization:
Capability
Feature Flag
Description
prompts
listChanged
Prompt template management
resources
subscribe
listChanged
Resource exposure and updates
tools
listChanged
Tool discovery and execution
logging
-
Server logging configuration
completions
-
Argument completion suggestions
Documentation
API Reference
Model Context Protocol documentation
Model Context Protocol specification
Officially supported servers
Contributing
We are passionate about supporting contributors of all levels of experience and would love to see you get involved in the project. See the
contributing guide
to get started.
License
This project is licensed under the MIT License - see the LICENSE file for details.
- 今日の獲得スター数: 32
- 累積スター数: 19,129

### References
- https://github.com/modelcontextprotocol/python-sdk

## openai/openai-agents-js

### Executive Summary
- A lightweight, powerful framework for multi-agent workflows and voice agents
- ---
- OpenAI Agents SDK (JavaScript/TypeScript)
The OpenAI Agents SDK is a lightweight yet powerful framework for building multi-agent workflows in JavaScript/TypeScript. It is provider-agnostic, supporting OpenAI APIs and more.
Note
Looking for the Python version? Check out
Agents SDK Python
.
Core concepts
Agents
: LLMs configured with instructions, tools, guardrails, and handoffs.
Handoffs
: Specialized tool calls for transferring control between agents.
Guardrails
: Configurable safety checks for input and output validation.
Tracing
: Built-in tracking of agent runs, allowing you to view, debug, and optimize your workflows.
Explore the
examples/
directory to see the SDK in action.
Supported Features
Multi-Agent Workflows
: Compose and orchestrate multiple agents in a single workflow.
Tool Integration
: Seamlessly call tools/functions from within agent responses.
Handoffs
: Transfer control between agents dynamically during a run.
Structured Outputs
: Support for both plain text and schema-validated structured outputs.
Streaming Responses
: Stream agent outputs and events in real time.
Tracing & Debugging
: Built-in tracing for visualizing and debugging agent runs.
Guardrails
: Input and output validation for safety and reliability.
Parallelization
: Run agents or tool calls in parallel and aggregate results.
Human-in-the-Loop
: Integrate human approval or intervention into workflows.
Realtime Voice Agents
: Build realtime voice agents using WebRTC or WebSockets
Local MCP Server Support
: Give an Agent access to a locally running MCP server to provide tools
Separate optimized browser package
: Dedicated package meant to run in the browser for Realtime agents.
Broader model support
: Use non-OpenAI models through the Vercel AI SDK adapter
Long running functions
: Suspend an agent loop to execute a long-running function and revive it later
Voice pipeline
: Chain text-based agents using speech-to-text and text-to-speech into a voice agent
Get started
Supported environments
Node.js 22 or later
Deno
Bun
Experimental support:
Cloudflare Workers with
nodejs_compat
enabled
Check out the documentation
for more detailed information.
Installation
npm install @openai/agents zod@3
Hello world example
import
{
Agent
,
run
}
from
'@openai/agents'
;
const
agent
=
new
Agent
(
{
name
:
'Assistant'
,
instructions
:
'You are a helpful assistant'
,
}
)
;
const
result
=
await
run
(
agent
,
'Write a haiku about recursion in programming.'
,
)
;
console
.
log
(
result
.
finalOutput
)
;
// Code within the code,
// Functions calling themselves,
// Infinite loop's dance.
(
If running this, ensure you set the
OPENAI_API_KEY
environment variable
)
Functions example
import
{
z
}
from
'zod'
;
import
{
Agent
,
run
,
tool
}
from
'@openai/agents'
;
const
getWeatherTool
=
tool
(
{
name
:
'get_weather'
,
description
:
'Get the weather for a given city'
,
parameters
:
z
.
object
(
{
city
:
z
.
string
(
)
}
)
,
execute
:
async
(
input
)
=>
{
return
`The weather in
${
input
.
city
}
is sunny`
;
}
,
}
)
;
const
agent
=
new
Agent
(
{
name
:
'Data agent'
,
instructions
:
'You are a data agent'
,
tools
:
[
getWeatherTool
]
,
}
)
;
async
function
main
(
)
{
const
result
=
await
run
(
agent
,
'What is the weather in Tokyo?'
)
;
console
.
log
(
result
.
finalOutput
)
;
}
main
(
)
.
catch
(
console
.
error
)
;
Handoffs example
import
{
z
}
from
'zod'
;
import
{
Agent
,
run
,
tool
}
from
'@openai/agents'
;
const
getWeatherTool
=
tool
(
{
name
:
'get_weather'
,
description
:
'Get the weather for a given city'
,
parameters
:
z
.
object
(
{
city
:
z
.
string
(
)
}
)
,
execute
:
async
(
input
)
=>
{
return
`The weather in
${
input
.
city
}
is sunny`
;
}
,
}
)
;
const
dataAgent
=
new
Agent
(
{
name
:
'Data agent'
,
instructions
:
'You are a data agent'
,
handoffDescription
:
'You know everything about the weather'
,
tools
:
[
getWeatherTool
]
,
}
)
;
// Use Agent.create method to ensure the finalOutput type considers handoffs
const
agent
=
Agent
.
create
(
{
name
:
'Basic test agent'
,
instructions
:
'You are a basic agent'
,
handoffs
:
[
dataAgent
]
,
}
)
;
async
function
main
(
)
{
const
result
=
await
run
(
agent
,
'What is the weather in San Francisco?'
)
;
console
.
log
(
result
.
finalOutput
)
;
}
main
(
)
.
catch
(
console
.
error
)
;
Voice Agent
import
{
z
}
from
'zod'
;
import
{
RealtimeAgent
,
RealtimeSession
,
tool
}
from
'@openai/agents-realtime'
;
const
getWeatherTool
=
tool
(
{
name
:
'get_weather'
,
description
:
'Get the weather for a given city'
,
parameters
:
z
.
object
(
{
city
:
z
.
string
(
)
}
)
,
execute
:
async
(
input
)
=>
{
return
`The weather in
${
input
.
city
}
is sunny`
;
}
,
}
)
;
const
agent
=
new
RealtimeAgent
(
{
name
:
'Data agent'
,
instructions
:
'You are a data agent. When you are asked to check weather, you must use the available tools.'
,
tools
:
[
getWeatherTool
]
,
}
)
;
// Intended to run in the browser
const
{
apiKey
}
=
await
fetch
(
'/path/to/ephemeral/key/generation'
)
.
then
(
(
resp
)
=>
resp
.
json
(
)
,
)
;
// Automatically configures audio input/output — start talking
const
session
=
new
RealtimeSession
(
agent
)
;
await
session
.
connect
(
{
apiKey
}
)
;
Running Complete Examples
The
examples/
directory contains a series of examples to get started:
pnpm examples:basic
- Basic example with handoffs and tool calling
pnpm examples:agents-as-tools
- Using agents as tools for translation
pnpm examples:tools-web-search
- Using the web search tool
pnpm examples:tools-file-search
- Using the file search tool
pnpm examples:deterministic
- Deterministic multi-agent workflow
pnpm examples:parallelization
- Running agents in parallel and picking the best result
pnpm examples:human-in-the-loop
- Human approval for certain tool calls
pnpm examples:streamed
- Streaming agent output and events in real time
pnpm examples:streamed:human-in-the-loop
- Streaming output with human-in-the-loop approval
pnpm examples:routing
- Routing between agents based on language or context
pnpm examples:realtime-demo
- Framework agnostic Voice Agent example
pnpm examples:realtime-next
- Next.js Voice Agent example application
The agent loop
When you call
Runner.run()
, the SDK executes a loop until a final output is produced.
The agent is invoked with the given input, using the model and settings configured on the agent (or globally).
The LLM returns a response, which may include tool calls or handoff requests.
If the response contains a final output (see below), the loop ends and the result is returned.
If the response contains a handoff, the agent is switched to the new agent and the loop continues.
If there are tool calls, the tools are executed, their results are appended to the message history, and the loop continues.
You can control the maximum number of iterations with the
maxTurns
parameter.
Final output
The final output is the last thing the agent produces in the loop.
If the agent has an
outputType
(structured output), the loop ends when the LLM returns a response matching that type.
If there is no
outputType
(plain text), the first LLM response without tool calls or handoffs is considered the final output.
Summary of the agent loop:
If the current agent has an
outputType
, the loop runs until structured output of that type is produced.
If not, the loop runs until a message is produced with no tool calls or handoffs.
Error handling
If the maximum number of turns is exceeded, a
MaxTurnsExceededError
is thrown.
If a guardrail is triggered, a
GuardrailTripwireTriggered
exception is raised.
Documentation
To view the documentation locally:
pnpm docs:dev
Then visit
http://localhost:4321
in your browser.
Development
If you want to contribute or edit the SDK/examples:
Install dependencies
pnpm install
Build the project
pnpm build
&&
pnpm -r build-check
Run tests and linter
pnpm
test
&&
pnpm lint
See
AGENTS.md
and
CONTRIBUTING.md
for the full contributor guide.
Acknowledgements
We'd like to acknowledge the excellent work of the open-source community, especially:
zod
(schema validation)
Starlight
vite
and
vitest
pnpm
Next.js
We're committed to building the Agents SDK as an open source framework so others in the community can expand on our approach.
For more details, see the
documentation
or explore the
examples/
directory.
- 今日の獲得スター数: 31
- 累積スター数: 1,610

### References
- https://github.com/openai/openai-agents-js
