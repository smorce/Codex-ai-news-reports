# AI News Report (github-trending)

- Generated at: 2025-10-11T02:07:31Z
- Articles: 47

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
- 今日の獲得スター数: 1,263
- 累積スター数: 9,280

### References
- https://github.com/TibixDev/winboat

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
- 今日の獲得スター数: 956
- 累積スター数: 7,250

### References
- https://github.com/Stremio/stremio-web

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
- 今日の獲得スター数: 441
- 累積スター数: 52,599

### References
- https://github.com/TapXWorld/ChinaTextbook

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
- 今日の獲得スター数: 336
- 累積スター数: 2,387

### References
- https://github.com/timelinize/timelinize

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
- 今日の獲得スター数: 334
- 累積スター数: 9,147

### References
- https://github.com/MODSetter/SurfSense

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
- 今日の獲得スター数: 248
- 累積スター数: 18,145

### References
- https://github.com/browserbase/stagehand

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
- 今日の獲得スター数: 231
- 累積スター数: 99,705

### References
- https://github.com/rustdesk/rustdesk

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
- 今日の獲得スター数: 231
- 累積スター数: 97,333

### References
- https://github.com/shadcn-ui/ui

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
- 今日の獲得スター数: 188
- 累積スター数: 46,874

### References
- https://github.com/openai/codex

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
- 今日の獲得スター数: 186
- 累積スター数: 35,868

### References
- https://github.com/Zie619/n8n-workflows

## davila7/claude-code-templates

### Executive Summary
- CLI tool for configuring and monitoring Claude Code
- ---
- Claude Code Templates (aitmpl.com)
Ready-to-use configurations for Anthropic's Claude Code.
A comprehensive collection of AI agents, custom commands, settings, hooks, external integrations (MCPs), and project templates to enhance your development workflow.
Browse & Install Components and Templates
Browse All Templates
- Interactive web interface to explore and install 100+ agents, commands, settings, hooks, and MCPs.
🚀 Quick Installation
#
Install a complete development stack
npx claude-code-templates@latest --agent frontend-developer --command generate-tests --mcp github-integration
#
Browse and install interactively
npx claude-code-templates@latest
#
Install specific components
npx claude-code-templates@latest --agent security-auditor
npx claude-code-templates@latest --command optimize-bundle
npx claude-code-templates@latest --setting mcp-timeouts
npx claude-code-templates@latest --hook pre-commit-validation
npx claude-code-templates@latest --mcp postgresql-integration
What You Get
Component
Description
Examples
🤖 Agents
AI specialists for specific domains
Security auditor, React performance optimizer, database architect
⚡ Commands
Custom slash commands
/generate-tests
,
/optimize-bundle
,
/check-security
🔌 MCPs
External service integrations
GitHub, PostgreSQL, Stripe, AWS, OpenAI
⚙️ Settings
Claude Code configurations
Timeouts, memory settings, output styles
🪝 Hooks
Automation triggers
Pre-commit validation, post-completion actions
📦 Templates
Complete project configurations with CLAUDE.md, .claude/* files and .mcp.json
Framework-specific setups, project best practices
🛠️ Additional Tools
Beyond the template catalog, Claude Code Templates includes powerful development tools:
📊 Claude Code Analytics
Monitor your AI-powered development sessions in real-time with live state detection and performance metrics.
npx claude-code-templates@latest --analytics
💬 Conversation Monitor
Mobile-optimized interface to view Claude responses in real-time with secure remote access.
#
Local access
npx claude-code-templates@latest --chats
#
Secure remote access via Cloudflare Tunnel
npx claude-code-templates@latest --chats --tunnel
🔍 Health Check
Comprehensive diagnostics to ensure your Claude Code installation is optimized.
npx claude-code-templates@latest --health-check
📖 Documentation
📚 docs.aitmpl.com
- Complete guides, examples, and API reference for all components and tools.
Contributing
We welcome contributions!
Browse existing templates
to see what's available, then check our
contributing guidelines
to add your own agents, commands, MCPs, settings, or hooks.
Please read our
Code of Conduct
before contributing.
Attribution
This collection includes components from multiple sources:
Agents Collection:
wshobson/agents Collection
by
wshobson
- Licensed under MIT License (48 agents)
Commands Collection:
awesome-claude-code Commands
by
hesreallyhim
- Licensed under CC0 1.0 Universal (21 commands)
📄 License
This project is licensed under the MIT License - see the
LICENSE
file for details.
🔗 Links
🌐 Browse Templates
:
aitmpl.com
📚 Documentation
:
docs.aitmpl.com
💬 Community
:
GitHub Discussions
🐛 Issues
:
GitHub Issues
⭐ Star History
⭐ Found this useful? Give us a star to support the project!
- 今日の獲得スター数: 186
- 累積スター数: 6,984

### References
- https://github.com/davila7/claude-code-templates

## anthropics/claude-code

### Executive Summary
- Claude Code is an agentic coding tool that lives in your terminal, understands your codebase, and helps you code faster by executing routine tasks, explaining complex code, and handling git workflows - all through natural language commands.
- ---
- Claude Code
Claude Code is an agentic coding tool that lives in your terminal, understands your codebase, and helps you code faster by executing routine tasks, explaining complex code, and handling git workflows -- all through natural language commands. Use it in your terminal, IDE, or tag @claude on Github.
Learn more in the
official documentation
.
Get started
Install Claude Code:
npm install -g @anthropic-ai/claude-code
Navigate to your project directory and run
claude
.
Reporting Bugs
We welcome your feedback. Use the
/bug
command to report issues directly within Claude Code, or file a
GitHub issue
.
Connect on Discord
Join the
Claude Developers Discord
to connect with other developers using Claude Code. Get help, share feedback, and discuss your projects with the community.
Data collection, usage, and retention
When you use Claude Code, we collect feedback, which includes usage data (such as code acceptance or rejections), associated conversation data, and user feedback submitted via the
/bug
command.
How we use your data
See our
data usage policies
.
Privacy safeguards
We have implemented several safeguards to protect your data, including limited retention periods for sensitive information, restricted access to user session data, and clear policies against using feedback for model training.
For full details, please review our
Commercial Terms of Service
and
Privacy Policy
.
- 今日の獲得スター数: 177
- 累積スター数: 36,195

### References
- https://github.com/anthropics/claude-code

## CapSoftware/Cap

### Executive Summary
- Open source Loom alternative. Beautiful, shareable screen recordings.
- ---
- Cap
The open source Loom alternative.
Cap.so »
Downloads for
macOS & Windows
Cap is the open source alternative to Loom. It's a video messaging tool that allows you to record, edit and share videos in seconds.
Self Hosting
Cap Web is available to self-host using Docker or Railway, see our
self-hosting docs
to learn more.
You can also use the button below to deploy Cap Web to Railway:
Cap Desktop can connect to your self-hosted Cap Web instance regardless of if you build it yourself or
download from our website
.
Monorepo App Architecture
We use a combination of Rust, React (Next.js), TypeScript, Tauri, Drizzle (ORM), MySQL, TailwindCSS throughout this Turborepo powered monorepo.
A note about database: The codebase is currently designed to work with MySQL only. MariaDB or other compatible databases might partially work but are not officially supported.
Apps:
desktop
: A
Tauri
(Rust) app, using
SolidStart
on the frontend.
web
: A
Next.js
web app.
Packages:
ui
: A
React
Shared component library.
utils
: A
React
Shared utility library.
tsconfig
: Shared
tsconfig
configurations used throughout the monorepo.
database
: A
React
and
Drizzle ORM
Shared database library.
config
:
eslint
configurations (includes
eslint-config-next
,
eslint-config-prettier
other configs used throughout the monorepo).
License:
Portions of this software are licensed as follows:
All code residing in the
cap-camera*
and
scap-*
families of crates is licensed under the MIT License (see
licenses/LICENSE-MIT
).
All third party components are licensed under the original license provided by the owner of the applicable component
All other content not mentioned above is available under the AGPLv3 license as defined in
LICENSE
Contributing
See
CONTRIBUTING.md
for more information. This guide is a work in progress, and is updated regularly as the app matures.
- 今日の獲得スター数: 136
- 累積スター数: 12,407

### References
- https://github.com/CapSoftware/Cap

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
- 今日の獲得スター数: 110
- 累積スター数: 112,077

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
- 今日の獲得スター数: 107
- 累積スター数: 19,437

### References
- https://github.com/78/xiaozhi-esp32

## evershopcommerce/evershop

### Executive Summary
- 🛍️ Typescript E-commerce Platform
- ---
- EverShop
Documentation
|
Demo
Introduction
EverShop is a modern, TypeScript-first eCommerce platform built with GraphQL and React. Designed for developers, it offers essential commerce features in a modular, fully customizable architecture—perfect for building tailored shopping experiences with confidence and speed.
Installation Using Docker
You can get started with EverShop in minutes by using the Docker image. The Docker image is a great way to get started with EverShop without having to worry about installing dependencies or configuring your environment.
curl -sSL https://raw.githubusercontent.com/evershopcommerce/evershop/main/docker-compose.yml
>
docker-compose.yml
docker-compose up -d
For the full installation guide, please refer to our
Installation guide
.
Documentation
Installation guide
.
Extension development
.
Theme development
.
Demo
Explore our demo store.
Demo user:
Email:
demo@evershop.io
Password: 123456
Support
If you like my work, feel free to:
⭐ this repository. It helps.
about EverShop. Thank you!
Contributing
EverShop is an open-source project. We are committed to a fully transparent development process and appreciate highly any contributions. Whether you are helping us fix bugs, proposing new features, improving our documentation or spreading the word - we would love to have you as part of the EverShop community.
Ask a question about EverShop
You can ask questions, and participate in discussions about EverShop-related topics in the EverShop Discord channel.
Create a bug report
If you see an error message or run into an issue, please
create bug report
. This effort is valued and it will help all EverShop users.
Submit a feature request
If you have an idea, or you're missing a capability that would make development easier and more robust, please
Submit feature request
.
If a similar feature request already exists, don't forget to leave a "+1".
If you add some more information such as your thoughts and vision about the feature, your comments will be embraced warmly :)
Please refer to our
Contribution Guidelines
and
Code of Conduct
.
License
GPL-3.0 License
- 今日の獲得スター数: 99
- 累積スター数: 6,383

### References
- https://github.com/evershopcommerce/evershop

## rizinorg/cutter

### Executive Summary
- Free and Open Source Reverse Engineering Platform powered by rizin
- ---
- Cutter
Cutter is a free and open-source reverse engineering platform powered by
rizin
. It aims at being an advanced and customizable reverse engineering platform while keeping the user experience in mind. Cutter is created by reverse engineers for reverse engineers.
Learn more at
cutter.re
.
Getting Cutter
Download
Cutter release binaries for all major platforms (Linux, macOS, Windows) can be downloaded from
GitHub Releases
.
Linux
: If your distribution provides it, check for
cutter
package in your package manager (or
cutter-re
/
rz-cutter
). If not available there, we have setup repositories in
OBS
for some common distributions. Look at
https://software.opensuse.org/package/cutter-re
and follow the instructions there. Otherwise download the
.AppImage
file from our release, make it executable and run as below or use
AppImageLauncher
.
chmod +x Cutter*.AppImage; ./Cutter*.AppImage
macOS
: Download the
.dmg
file or use
Homebrew Cask
:
brew install --cask cutter
Windows
: Download the
.zip
archive, or use either
Chocolatey
or
Scoop
:
choco install cutter
scoop bucket add extras
followed by
scoop install cutter
Build from sources
To build Cutter from sources, please check the
Building Docs
.
Docker image
To deploy
cutter
using a pre-built
Dockerfile
, it's possible to use the
provided configuration
. The corresponding
README.md
file also contains instructions on how to get started using the docker image with minimal effort.
Documentation
User Guide
Contribution Guidelines
Developers Docs
Plugins
Cutter supports both Python and Native C++ plugins.
Our community has built many plugins and useful scripts for Cutter such as the native integration of
Ghidra decompiler
or the plugin to visualize DynamoRIO code coverage. You can find a list of cutter plugins linked below. Feel free to extend it with your own plugins and scripts for Cutter.
Official & Community Plugins
Plugins Development Guide
Getting Help
Please use the following channels to ask for help from Cutter developers and community:
Telegram:
https://t.me/cutter_re
Mattermost:
https://im.rizin.re
IRC:
#cutter on
https://web.libera.chat/
Twitter:
@cutter_re
- 今日の獲得スター数: 97
- 累積スター数: 17,754

### References
- https://github.com/rizinorg/cutter

## xyflow/xyflow

### Executive Summary
- React Flow | Svelte Flow - Powerful open source libraries for building node-based UIs with React (https://reactflow.dev) or Svelte (https://svelteflow.dev). Ready out-of-the-box and infinitely customizable.
- ---
- Powerful open source libraries for building node-based UIs with React or Svelte. Ready out-of-the-box and infinitely customizable.
React Flow
·
Svelte Flow
·
React Flow Pro
·
Discord
The xyflow mono repo
The xyflow repository is the home of four packages:
React Flow 12
@xyflow/react
packages/react
React Flow 11
reactflow
v11 branch
Svelte Flow
@xyflow/svelte
packages/svelte
Shared helper library
@xyflow/system
packages/system
Commercial usage
Are you using React Flow or Svelte Flow for a personal project?
Great! No sponsorship needed, you can support us by reporting any bugs you find, sending us screenshots of your projects, and starring us on Github 🌟
Are you using React Flow or Svelte Flow at your organization and making money from it?
Awesome! We rely on your support to keep our libraries developed and maintained under an MIT License, just how we like it. For React Flow you can do that on the
React Flow Pro website
and for both of our libraries you can do it through
Github Sponsors
.
Getting started
The best way to get started is to check out the
React Flow
or
Svelte Flow
learn section. However if you want to get a sneak peek of how to install and use the libraries you can see it here:
React Flow
basic usage
Installation
npm install @xyflow/react
Basic usage
import
{
useCallback
}
from
'react'
;
import
{
ReactFlow
,
MiniMap
,
Controls
,
Background
,
useNodesState
,
useEdgesState
,
addEdge
,
}
from
'@xyflow/react'
;
import
'@xyflow/react/dist/style.css'
;
const
initialNodes
=
[
{
id
:
'1'
,
position
:
{
x
:
0
,
y
:
0
}
,
data
:
{
label
:
'1'
}
}
,
{
id
:
'2'
,
position
:
{
x
:
0
,
y
:
100
}
,
data
:
{
label
:
'2'
}
}
,
]
;
const
initialEdges
=
[
{
id
:
'e1-2'
,
source
:
'1'
,
target
:
'2'
}
]
;
function
Flow
(
)
{
const
[
nodes
,
setNodes
,
onNodesChange
]
=
useNodesState
(
initialNodes
)
;
const
[
edges
,
setEdges
,
onEdgesChange
]
=
useEdgesState
(
initialEdges
)
;
const
onConnect
=
useCallback
(
(
params
)
=>
setEdges
(
(
eds
)
=>
addEdge
(
params
,
eds
)
)
,
[
setEdges
]
)
;
return
(
<
ReactFlow
nodes
=
{
nodes
}
edges
=
{
edges
}
onNodesChange
=
{
onNodesChange
}
onEdgesChange
=
{
onEdgesChange
}
onConnect
=
{
onConnect
}
>
<
MiniMap
/>
<
Controls
/>
<
Background
/>
</
ReactFlow
>
)
;
}
export
default
Flow
;
Svelte Flow
basic usage
Installation
npm install @xyflow/svelte
Basic usage
<
script
lang
=
"
ts
"
>
import
{
writable
}
from
'
svelte/store
'
;
import
{
SvelteFlow
,
Controls
,
Background
,
BackgroundVariant
,
MiniMap
,
}
from
'
@xyflow/svelte
'
;
import
'
@xyflow/svelte/dist/style.css
'
const
nodes
=
writable
([
{
id:
'
1
'
,
type:
'
input
'
,
data: { label:
'
Input Node
'
},
position: { x:
0
, y:
0
}
},
{
id:
'
2
'
,
type:
'
custom
'
,
data: { label:
'
Node
'
},
position: { x:
0
, y:
150
}
}
]);
const
edges
=
writable
([
{
id:
'
1-2
'
,
type:
'
default
'
,
source:
'
1
'
,
target:
'
2
'
,
label:
'
Edge Text
'
}
]);
</
script
>

<
SvelteFlow
{
nodes
}
{
edges
}
fitView
on:nodeclick
={(
event
)
=>
console
.
log
(
'
on node click
'
,
event
)}
>
<
Controls
/>
<
Background
variant
={
BackgroundVariant
.
Dots
} />
<
MiniMap
/>
</
SvelteFlow
>
Releases
For releasing packages we are using
changesets
in combination with the
changeset Github action
. The rough idea is:
create PRs for new features, updates and fixes (with a changeset if relevant for changelog)
merge into main
changset creates a PR that bumps all packages based on the changesets
merge changeset PR if you want to release to Github and npm
Built by
xyflow
React Flow and Svelte Flow are maintained by the
xyflow team
. If you need help or want to talk to us about a collaboration, reach out through our
contact form
or by joining our
Discord Server
.
License
React Flow and Svelte Flow are
MIT licensed
.
- 今日の獲得スター数: 92
- 累積スター数: 32,452

### References
- https://github.com/xyflow/xyflow

## rust-lang/rustfmt

### Executive Summary
- Format Rust code
- ---
- rustfmt
A tool for formatting Rust code according to style guidelines.
If you'd like to help out (and you should, it's a fun project!), see
Contributing.md
and our
Code of
Conduct
.
You can use rustfmt in Travis CI builds. We provide a minimal Travis CI
configuration (see
here
).
Quick start
You can run
rustfmt
with Rust 1.24 and above.
On the Stable toolchain
To install:
rustup component add rustfmt
To run on a cargo project in the current working directory:
cargo fmt
On the Nightly toolchain
For the latest and greatest
rustfmt
, nightly is required.
To install:
rustup component add rustfmt --toolchain nightly
To run on a cargo project in the current working directory:
cargo +nightly fmt
Limitations
Rustfmt tries to work on as much Rust code as possible. Sometimes, the code
doesn't even need to compile! In general, we are looking to limit areas of
instability; in particular, post-1.0, the formatting of most code should not
change as Rustfmt improves. However, there are some things that Rustfmt can't
do or can't do well (and thus where formatting might change significantly,
even post-1.0). We would like to reduce the list of limitations over time.
The following list enumerates areas where Rustfmt does not work or where the
stability guarantees do not apply (we don't make a distinction between the two
because in the future Rustfmt might work on code where it currently does not):
a program where any part of the program does not parse (parsing is an early
stage of compilation and in Rust includes macro expansion).
Macro declarations and uses (current status: some macro declarations and uses
are formatted).
Comments, including any AST node with a comment 'inside' (Rustfmt does not
currently attempt to format comments, it does format code with comments inside, but that formatting may change in the future).
Rust code in code blocks in comments.
Any fragment of a program (i.e., stability guarantees only apply to whole
programs, even where fragments of a program can be formatted today).
Code containing non-ascii unicode characters (we believe Rustfmt mostly works
here, but do not have the test coverage or experience to be 100% sure).
Bugs in Rustfmt (like any software, Rustfmt has bugs, we do not consider bug
fixes to break our stability guarantees).
Running
You can run Rustfmt by just typing
rustfmt filename
if you used
cargo install
. This runs rustfmt on the given file, if the file includes out of line
modules, then we reformat those too. So to run on a whole module or crate, you
just need to run on the root file (usually mod.rs or lib.rs). Rustfmt can also
read data from stdin. Alternatively, you can use
cargo fmt
to format all
binary and library targets of your crate.
You can run
rustfmt --help
for information about available arguments.
The easiest way to run rustfmt against a project is with
cargo fmt
.
cargo fmt
works on both
single-crate projects and
cargo workspaces
.
Please see
cargo fmt --help
for usage information.
You can specify the path to your own
rustfmt
binary for cargo to use by setting the
RUSTFMT
environment variable. This was added in v1.4.22, so you must have this version or newer to leverage this feature (
cargo fmt --version
)
Running
rustfmt
directly
To format individual files or arbitrary codes from stdin, the
rustfmt
binary should be used. Some
examples follow:
rustfmt lib.rs main.rs
will format "lib.rs" and "main.rs" in place
rustfmt
will read a code from stdin and write formatting to stdout
echo "fn     main() {}" | rustfmt
would emit "fn main() {}".
For more information, including arguments and emit options, see
rustfmt --help
.
Verifying code is formatted
When running with
--check
, Rustfmt will exit with
0
if Rustfmt would not
make any formatting changes to the input, and
1
if Rustfmt would make changes.
In other modes, Rustfmt will exit with
1
if there was some error during
formatting (for example a parsing or internal error) and
0
if formatting
completed without error (whether or not changes were made).
Running Rustfmt from your editor
Vim
Emacs
Sublime Text 3
Atom
Visual Studio Code
IntelliJ or CLion
Checking style on a CI server
To keep your code base consistently formatted, it can be helpful to fail the CI build
when a pull request contains unformatted code. Using
--check
instructs
rustfmt to exit with an error code if the input is not formatted correctly.
It will also print any found differences. (Older versions of Rustfmt don't
support
--check
, use
--write-mode diff
).
A minimal Travis setup could look like this (requires Rust 1.31.0 or greater):
language
:
rust
before_script
:
-
rustup component add rustfmt
script
:
-
cargo build
-
cargo test
-
cargo fmt --all -- --check
See
this blog post
for more info.
How to build and test
cargo build
to build.
cargo test
to run all tests.
To run rustfmt after this, use
cargo run --bin rustfmt -- filename
. See the
notes above on running rustfmt.
Configuring Rustfmt
Rustfmt is designed to be very configurable. You can create a TOML file called
rustfmt.toml
or
.rustfmt.toml
, place it in the project or any other parent
directory and it will apply the options in that file. See
rustfmt --help=config
for the options which are available, or if you prefer to see
visual style previews,
GitHub page
.
By default, Rustfmt uses a style which conforms to the
Rust style guide
that has been formalized through the
style RFC
process
.
Configuration options are either stable or unstable. Stable options can always
be used, while unstable ones are only available on a nightly toolchain, and opt-in.
See
GitHub page
for details.
Rust's Editions
The
edition
option determines the Rust language edition used for parsing the code. This is important for syntax compatibility but does not directly control formatting behavior (see
Style Editions
).
When running
cargo fmt
, the
edition
is automatically read from the
Cargo.toml
file. However, when running
rustfmt
directly, the
edition
defaults to 2015. For consistent parsing between rustfmt and
cargo fmt
, you should configure the
edition
in your
rustfmt.toml
file:
edition
=
"
2018
"
Style Editions
This option is inferred from the
edition
if not specified.
See
Rust Style Editions
for details on formatting differences between style editions.
rustfmt has a default style edition of
2015
while
cargo fmt
infers the style edition from the
edition
set in
Cargo.toml
. This can lead to inconsistencies between
rustfmt
and
cargo fmt
if the style edition is not explicitly configured.
To ensure consistent formatting, it is recommended to specify the
style_edition
in a
rustfmt.toml
configuration file. For example:
style_edition
=
"
2024
"
Tips
To ensure consistent parsing between
cargo fmt
and
rustfmt
, you should configure the
edition
in your
rustfmt.toml
file.
To ensure consistent formatting between
cargo fmt
and
rustfmt
, you should configure the
style_edition
in your
rustfmt.toml
file.
For things you do not want rustfmt to mangle, use
#[rustfmt::skip]
To prevent rustfmt from formatting a macro or an attribute,
use
#[rustfmt::skip::macros(target_macro_name)]
or
#[rustfmt::skip::attributes(target_attribute_name)]
Example:
#!
[
rustfmt
::
skip
::
attributes
(
custom_attribute
)
]
#
[
custom_attribute
(
formatting
,
here
,
should
,
be
,
Skipped
)
]
#
[
rustfmt
::
skip
::
macros
(
html
)
]
fn
main
(
)
{
let
macro_result1 =
html
!
{
<div>
Hello
</div>
}
.
to_string
(
)
;
When you run rustfmt, place a file named
rustfmt.toml
or
.rustfmt.toml
in
target file directory or its parents to override the default settings of
rustfmt. You can generate a file containing the default configuration with
rustfmt --print-config default rustfmt.toml
and customize as needed.
After successful compilation, a
rustfmt
executable can be found in the
target directory.
If you're having issues compiling Rustfmt (or compile errors when trying to
install), make sure you have the most recent version of Rust installed.
You can change the way rustfmt emits the changes with the --emit flag:
Example:
cargo fmt -- --emit files
Options:
Flag
Description
Nightly Only
files
overwrites output to files
No
stdout
writes output to stdout
No
coverage
displays how much of the input file was processed
Yes
checkstyle
emits in a checkstyle format
Yes
json
emits diffs in a json format
Yes
License
Rustfmt is distributed under the terms of both the MIT license and the
Apache License (Version 2.0).
See
LICENSE-APACHE
and
LICENSE-MIT
for details.
- 今日の獲得スター数: 81
- 累積スター数: 6,583

### References
- https://github.com/rust-lang/rustfmt

## tile-ai/tilelang

### Executive Summary
- Domain-specific language designed to streamline the development of high-performance GPU/CPU/Accelerators kernels
- ---
- Tile Language
Tile Language (
tile-lang
) is a concise domain-specific language designed to streamline the development of high-performance GPU/CPU kernels (e.g., GEMM, Dequant GEMM, FlashAttention, LinearAttention). By employing a Pythonic syntax with an underlying compiler infrastructure on top of
TVM
, tile-lang allows developers to focus on productivity without sacrificing the low-level optimizations necessary for state-of-the-art performance.
Latest News
10/07/2025 🍎: Added Apple Metal Device support, check out
Pull Request #799
for details.
09/29/2025  🎉: Thrilled to announce that ​​AscendC​​ and ​Ascend​NPU IR​​ backends targeting Huawei Ascend chips are now supported!
Check out the preview here:
🔗
link
.
This includes implementations across two branches:
ascendc_pto
and
npuir
.
Feel free to explore and share your feedback!
07/04/2025 🚀: Introduced
T.gemm_sp
for 2:4 sparse tensor core support, check out
Pull Request #526
for details.
06/05/2025 ✨: Added
NVRTC Backend
to significantly reduce compilation time for cute templates!
04/14/2025 🚀: Added high-performance FlashMLA implementation for AMD MI300X, achieving performance parity with hand-optimized assembly kernels of Aiter! See
example_mla_amd
for details.
03/03/2025 🚀: Added high-performance MLA Decoding support using only 80 lines of Python code, achieving performance on par with FlashMLA on H100 (see
example_mla_decode.py
)! We also provide
documentation
explaining how TileLang achieves this.
02/15/2025 ✨: Added WebGPU Codegen support, see
Pull Request #86
!
02/12/2025 ✨: Excited to announce the release of
v0.1.0
!
02/10/2025 🚀: Added debug tools for TileLang—
T.print
for printing variables/buffers (
docs
) and a memory layout plotter (
examples/plot_layout
).
01/20/2025 ✨: We are excited to announce that tile-lang, a dsl for high performance AI workloads, is now open source and available to the public!
Tested Devices
Although tile-lang aims to be portable across a range of Devices, it has been specifically tested and validated on the following devices: for NVIDIA GPUs, this includes the H100 (with Auto TMA/WGMMA support), A100, V100, RTX 4090, RTX 3090, and RTX A6000; for AMD GPUs, it includes the MI250 (with Auto MatrixCore support) and the MI300X (with Async Copy support).
OP Implementation Examples
tile-lang
provides the building blocks to implement a wide variety of operators. Some examples include:
Matrix Multiplication
Dequantization GEMM
Flash Attention
Flash Linear Attention
Flash MLA Decoding
Native Sparse Attention
Within the
examples
directory, you will also find additional complex kernels—such as convolutions, forward/backward passes for FlashAttention, more operators will continuously be added.
Benchmark Summary
TileLang achieves exceptional performance across a variety of computational patterns. Comprehensive benchmark scripts and settings are available at
tilelang-benchmark
. Below are selected results showcasing its capabilities:
MLA Decoding Performance on H100
Flash Attention Performance on H100
Matmul Performance on GPUs (RTX 4090, A100, H100, MI300X)
Dequantize Matmul Performance on A100
Installation
Method 1: Install with Pip
The quickest way to get started is to install the latest release from PyPI:
pip install tilelang
Alternatively, you can install directly from the GitHub repository:
pip install git+https://github.com/tile-ai/tilelang
Or install locally:
#
install required system dependencies
sudo apt-get update
sudo apt-get install -y python3-setuptools gcc libtinfo-dev zlib1g-dev build-essential cmake libedit-dev libxml2-dev

pip install -e
.
-v
#
remove -e option if you don't want to install in editable mode, -v for verbose output
Method 2: Build from Source
We currently provide three ways to install
tile-lang
from source:
Install from Source (using your own TVM installation)
Install from Source (using the bundled TVM submodule)
Install Using the Provided Script
Method 3: Install with Nightly Version
For users who want access to the latest features and improvements before official releases, we provide nightly builds of
tile-lang
.
pip install tilelang -f https://tile-ai.github.io/whl/nightly/cu121/
#
or pip install tilelang --find-links https://tile-ai.github.io/whl/nightly/cu121/
Note:
Nightly builds contain the most recent code changes but may be less stable than official releases. They're ideal for testing new features or if you need a specific bugfix that hasn't been released yet.
Quick Start
In this section, you'll learn how to write and execute a straightforward GEMM (matrix multiplication) kernel using tile-lang, followed by techniques for layout optimizations, pipelining, and L2-cache–friendly swizzling.
GEMM Example with Annotations (Layout, L2 Cache Swizzling, and Pipelining, etc.)
Below is an example that demonstrates more advanced features: layout annotation, parallelized copy, and swizzle for improved L2 cache locality. This snippet shows how to adapt your kernel to maximize performance on complex hardware.
import
tilelang
import
tilelang
.
language
as
T
# @tilelang.jit(target="cuda")
# target currently can be "cuda" or "hip" or "cpu".
# if not specified, it will be inferred from the input tensors during compile time
@
tilelang
.
jit
def
matmul
(
M
,
N
,
K
,
block_M
,
block_N
,
block_K
,
dtype
=
"float16"
,
accum_dtype
=
"float"
):
@
T
.
prim_func
def
matmul_relu_kernel
(
A
:
T
.
Tensor
((
M
,
K
),
dtype
),
B
:
T
.
Tensor
((
K
,
N
),
dtype
),
C
:
T
.
Tensor
((
M
,
N
),
dtype
),
    ):
# Initialize Kernel Context
with
T
.
Kernel
(
T
.
ceildiv
(
N
,
block_N
),
T
.
ceildiv
(
M
,
block_M
),
threads
=
128
)
as
(
bx
,
by
):
A_shared
=
T
.
alloc_shared
((
block_M
,
block_K
),
dtype
)
B_shared
=
T
.
alloc_shared
((
block_K
,
block_N
),
dtype
)
C_local
=
T
.
alloc_fragment
((
block_M
,
block_N
),
accum_dtype
)
# Enable rasterization for better L2 cache locality (Optional)
# T.use_swizzle(panel_size=10, enable=True)
# Clear local accumulation
T
.
clear
(
C_local
)
for
ko
in
T
.
Pipelined
(
T
.
ceildiv
(
K
,
block_K
),
num_stages
=
3
):
# Copy tile of A
# This is a sugar syntax for parallelized copy
T
.
copy
(
A
[
by
*
block_M
,
ko
*
block_K
],
A_shared
)
# Copy tile of B
T
.
copy
(
B
[
ko
*
block_K
,
bx
*
block_N
],
B_shared
)
# Perform a tile-level GEMM on the shared buffers
# Currently we dispatch to the cute/hip on Nvidia/AMD GPUs
T
.
gemm
(
A_shared
,
B_shared
,
C_local
)
# relu
for
i
,
j
in
T
.
Parallel
(
block_M
,
block_N
):
C_local
[
i
,
j
]
=
T
.
max
(
C_local
[
i
,
j
],
0
)
# Copy result back to global memory
T
.
copy
(
C_local
,
C
[
by
*
block_M
,
bx
*
block_N
])
return
matmul_relu_kernel
M
=
1024
# M = T.symbolic("m") if you want to use dynamic shape
N
=
1024
K
=
1024
block_M
=
128
block_N
=
128
block_K
=
32
# 1. Define the kernel (matmul) and compile/lower it into an executable module
matmul_relu_kernel
=
matmul
(
M
,
N
,
K
,
block_M
,
block_N
,
block_K
)
# 3. Test the kernel in Python with PyTorch data
import
torch
# Create random input tensors on the GPU
a
=
torch
.
randn
(
M
,
K
,
device
=
"cuda"
,
dtype
=
torch
.
float16
)
b
=
torch
.
randn
(
K
,
N
,
device
=
"cuda"
,
dtype
=
torch
.
float16
)
c
=
torch
.
empty
(
M
,
N
,
device
=
"cuda"
,
dtype
=
torch
.
float16
)
# Run the kernel through the Profiler
matmul_relu_kernel
(
a
,
b
,
c
)
print
(
c
)
# Reference multiplication using PyTorch
ref_c
=
torch
.
relu
(
a
@
b
)
# Validate correctness
torch
.
testing
.
assert_close
(
c
,
ref_c
,
rtol
=
1e-2
,
atol
=
1e-2
)
print
(
"Kernel output matches PyTorch reference."
)
# 4. Retrieve and inspect the generated CUDA source (optional)
# cuda_source = jit_kernel.get_kernel_source()
# print("Generated CUDA kernel:\n", cuda_source)
# 5.Profile latency with kernel
profiler
=
matmul_relu_kernel
.
get_profiler
(
tensor_supply_type
=
tilelang
.
TensorSupplyType
.
Normal
)
latency
=
profiler
.
do_bench
()
print
(
f"Latency:
{
latency
}
ms"
)
Dive Deep into TileLang Beyond GEMM
In addition to GEMM, we provide a variety of examples to showcase the versatility and power of TileLang, including:
Dequantize GEMM
: Achieve high-performance dequantization by
fine-grained control over per-thread operations
, with many features now adopted as default behaviors in
BitBLAS
, which utilizing magic layout transformation and intrins to accelerate dequantize gemm.
FlashAttention
: Enable cross-operator fusion with simple and intuitive syntax, and we also provide an example of auto tuning.
LinearAttention
: Examples include RetNet and Mamba implementations.
Convolution
: Implementations of Convolution with IM2Col.
Upcoming Features
Check our
tilelang v0.2.0 release plan
for upcoming features.
TileLang has now been used in project
BitBLAS
and
AttentionEngine
.
Join the Discussion
Welcome to join our Discord community for discussions, support, and collaboration!
Acknowledgements
We would like to express our gratitude to the
TVM
community for their invaluable contributions. The initial version of this project was mainly developed by
LeiWang1999
,
chengyupku
and
nox-410
with supervision from Prof.
Zhi Yang
at Peking University. Part of this work was carried out during an internship at Microsoft Research, where Dr. Lingxiao Ma, Dr. Yuqing Xia, Dr. Jilong Xue, and Dr. Fan Yang offered valuable advice and support. We deeply appreciate their mentorship and contributions.
- 今日の獲得スター数: 73
- 累積スター数: 3,425

### References
- https://github.com/tile-ai/tilelang

## vllm-project/vllm

### Executive Summary
- A high-throughput and memory-efficient inference and serving engine for LLMs
- ---
- Easy, fast, and cheap LLM serving for everyone
|
Documentation
|
Blog
|
Paper
|
Twitter/X
|
User Forum
|
Developer Slack
|
Join us at the
PyTorch Conference, October 22-23
and
Ray Summit, November 3-5
in San Francisco for our latest updates on vLLM and to meet the vLLM team! Register now for the largest vLLM community events of the year!
Latest News
🔥
[2025/09] We hosted
vLLM Toronto Meetup
focused on tackling inference at scale and speculative decoding with speakers from NVIDIA and Red Hat! Please find the meetup slides
here
.
[2025/08] We hosted
vLLM Shenzhen Meetup
focusing on the ecosystem around vLLM! Please find the meetup slides
here
.
[2025/08] We hosted
vLLM Singapore Meetup
. We shared V1 updates, disaggregated serving and MLLM speedups with speakers from Embedded LLM, AMD, WekaIO, and A*STAR. Please find the meetup slides
here
.
[2025/08] We hosted
vLLM Shanghai Meetup
focusing on building, developing, and integrating with vLLM! Please find the meetup slides
here
.
[2025/05] vLLM is now a hosted project under PyTorch Foundation! Please find the announcement
here
.
[2025/01] We are excited to announce the alpha release of vLLM V1: A major architectural upgrade with 1.7x speedup! Clean code, optimized execution loop, zero-overhead prefix caching, enhanced multimodal support, and more. Please check out our blog post
here
.
Previous News
[2025/08] We hosted
vLLM Korea Meetup
with Red Hat and Rebellions! We shared the latest advancements in vLLM along with project spotlights from the vLLM Korea community. Please find the meetup slides
here
.
[2025/08] We hosted
vLLM Beijing Meetup
focusing on large-scale LLM deployment! Please find the meetup slides
here
and the recording
here
.
[2025/05] We hosted
NYC vLLM Meetup
! Please find the meetup slides
here
.
[2025/04] We hosted
Asia Developer Day
! Please find the meetup slides from the vLLM team
here
.
[2025/03] We hosted
vLLM x Ollama Inference Night
! Please find the meetup slides from the vLLM team
here
.
[2025/03] We hosted
the first vLLM China Meetup
! Please find the meetup slides from vLLM team
here
.
[2025/03] We hosted
the East Coast vLLM Meetup
! Please find the meetup slides
here
.
[2025/02] We hosted
the ninth vLLM meetup
with Meta! Please find the meetup slides from vLLM team
here
and AMD
here
. The slides from Meta will not be posted.
[2025/01] We hosted
the eighth vLLM meetup
with Google Cloud! Please find the meetup slides from vLLM team
here
, and Google Cloud team
here
.
[2024/12] vLLM joins
pytorch ecosystem
! Easy, Fast, and Cheap LLM Serving for Everyone!
[2024/11] We hosted
the seventh vLLM meetup
with Snowflake! Please find the meetup slides from vLLM team
here
, and Snowflake team
here
.
[2024/10] We have just created a developer slack (
slack.vllm.ai
) focusing on coordinating contributions and discussing features. Please feel free to join us there!
[2024/10] Ray Summit 2024 held a special track for vLLM! Please find the opening talk slides from the vLLM team
here
. Learn more from the
talks
from other vLLM contributors and users!
[2024/09] We hosted
the sixth vLLM meetup
with NVIDIA! Please find the meetup slides
here
.
[2024/07] We hosted
the fifth vLLM meetup
with AWS! Please find the meetup slides
here
.
[2024/07] In partnership with Meta, vLLM officially supports Llama 3.1 with FP8 quantization and pipeline parallelism! Please check out our blog post
here
.
[2024/06] We hosted
the fourth vLLM meetup
with Cloudflare and BentoML! Please find the meetup slides
here
.
[2024/04] We hosted
the third vLLM meetup
with Roblox! Please find the meetup slides
here
.
[2024/01] We hosted
the second vLLM meetup
with IBM! Please find the meetup slides
here
.
[2023/10] We hosted
the first vLLM meetup
with a16z! Please find the meetup slides
here
.
[2023/08] We would like to express our sincere gratitude to
Andreessen Horowitz
(a16z) for providing a generous grant to support the open-source development and research of vLLM.
[2023/06] We officially released vLLM! FastChat-vLLM integration has powered
LMSYS Vicuna and Chatbot Arena
since mid-April. Check out our
blog post
.
About
vLLM is a fast and easy-to-use library for LLM inference and serving.
Originally developed in the
Sky Computing Lab
at UC Berkeley, vLLM has evolved into a community-driven project with contributions from both academia and industry.
vLLM is fast with:
State-of-the-art serving throughput
Efficient management of attention key and value memory with
PagedAttention
Continuous batching of incoming requests
Fast model execution with CUDA/HIP graph
Quantizations:
GPTQ
,
AWQ
,
AutoRound
, INT4, INT8, and FP8
Optimized CUDA kernels, including integration with FlashAttention and FlashInfer
Speculative decoding
Chunked prefill
vLLM is flexible and easy to use with:
Seamless integration with popular Hugging Face models
High-throughput serving with various decoding algorithms, including
parallel sampling
,
beam search
, and more
Tensor, pipeline, data and expert parallelism support for distributed inference
Streaming outputs
OpenAI-compatible API server
Support for NVIDIA GPUs, AMD CPUs and GPUs, Intel CPUs and GPUs, PowerPC CPUs, and TPU. Additionally, support for diverse hardware plugins such as Intel Gaudi, IBM Spyre and Huawei Ascend.
Prefix caching support
Multi-LoRA support
vLLM seamlessly supports most popular open-source models on HuggingFace, including:
Transformer-like LLMs (e.g., Llama)
Mixture-of-Expert LLMs (e.g., Mixtral, Deepseek-V2 and V3)
Embedding Models (e.g., E5-Mistral)
Multi-modal LLMs (e.g., LLaVA)
Find the full list of supported models
here
.
Getting Started
Install vLLM with
pip
or
from source
:
pip install vllm
Visit our
documentation
to learn more.
Installation
Quickstart
List of Supported Models
Contributing
We welcome and value any contributions and collaborations.
Please check out
Contributing to vLLM
for how to get involved.
Sponsors
vLLM is a community project. Our compute resources for development and testing are supported by the following organizations. Thank you for your support!
Cash Donations:
a16z
Dropbox
Sequoia Capital
Skywork AI
ZhenFund
Compute Resources:
Alibaba Cloud
AMD
Anyscale
AWS
Crusoe Cloud
Databricks
DeepInfra
Google Cloud
Intel
Lambda Lab
Nebius
Novita AI
NVIDIA
Replicate
Roblox
RunPod
Trainy
UC Berkeley
UC San Diego
Volcengine
Slack Sponsor: Anyscale
We also have an official fundraising venue through
OpenCollective
. We plan to use the fund to support the development, maintenance, and adoption of vLLM.
Citation
If you use vLLM for your research, please cite our
paper
:
@inproceedings
{
kwon2023efficient
,
title
=
{
Efficient Memory Management for Large Language Model Serving with PagedAttention
}
,
author
=
{
Woosuk Kwon and Zhuohan Li and Siyuan Zhuang and Ying Sheng and Lianmin Zheng and Cody Hao Yu and Joseph E. Gonzalez and Hao Zhang and Ion Stoica
}
,
booktitle
=
{
Proceedings of the ACM SIGOPS 29th Symposium on Operating Systems Principles
}
,
year
=
{
2023
}
}
Contact Us
For technical questions and feature requests, please use GitHub
Issues
For discussing with fellow users, please use the
vLLM Forum
For coordinating contributions and development, please use
Slack
For security disclosures, please use GitHub's
Security Advisories
feature
For collaborations and partnerships, please contact us at
vllm-questions@lists.berkeley.edu
Media Kit
If you wish to use vLLM's logo, please refer to
our media kit repo
- 今日の獲得スター数: 70
- 累積スター数: 59,787

### References
- https://github.com/vllm-project/vllm

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
- 今日の獲得スター数: 65
- 累積スター数: 11,612

### References
- https://github.com/aaPanel/BillionMail

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
Start Adding Memory with your choice of format (Note, Link, File)
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
- 今日の獲得スター数: 62
- 累積スター数: 11,473

### References
- https://github.com/supermemoryai/supermemory

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
- 今日の獲得スター数: 61
- 累積スター数: 23,044

### References
- https://github.com/chen08209/FlClash

## jiji262/douyin-downloader

### Executive Summary
- 抖音批量下载工具，去水印，支持视频、图集、合集、音乐(原声)。免费！免费！免费！
- ---
- 抖音下载器 - 无水印批量下载工具
一个功能强大的抖音内容批量下载工具，支持视频、图集、音乐、直播等多种内容类型的下载。提供两个版本：V1.0（稳定版）和 V2.0（增强版）。
📋 目录
快速开始
版本说明
V1.0 使用指南
V2.0 使用指南
Cookie 配置工具
支持的链接类型
常见问题
更新日志
⚡ 快速开始
环境要求
Python 3.9+
操作系统
：Windows、macOS、Linux
安装步骤
克隆项目
git clone https://github.com/jiji262/douyin-downloader.git
cd
douyin-downloader
安装依赖
pip install -r requirements.txt
配置 Cookie
（首次使用需要）
#
方式1：自动获取（推荐）
python cookie_extractor.py
#
方式2：手动获取
python get_cookies_manual.py
📦 版本说明
V1.0 (DouYinCommand.py) - 稳定版
✅
经过验证
：稳定可靠，经过大量测试
✅
简单易用
：配置文件驱动，使用简单
✅
功能完整
：支持所有内容类型下载
✅
单个视频下载
：完全正常工作
⚠️
需要手动配置
：需要手动获取和配置 Cookie
V2.0 (downloader.py) - 增强版
🚀
自动 Cookie 管理
：支持自动获取和刷新 Cookie
🚀
统一入口
：整合所有功能到单一脚本
🚀
异步架构
：性能更优，支持并发下载
🚀
智能重试
：自动重试和错误恢复
🚀
增量下载
：支持增量更新，避免重复下载
⚠️
单个视频下载
：目前 API 返回空响应（已知问题）
✅
用户主页下载
：完全正常工作
🎯 V1.0 使用指南
配置文件设置
编辑配置文件
cp config.example.yml config.yml
#
编辑 config.yml 文件
配置示例
#
下载链接
link
:
  -
https://v.douyin.com/xxxxx/
#
单个视频
-
https://www.douyin.com/user/xxxxx
#
用户主页
-
https://www.douyin.com/collection/xxxxx
#
合集
#
保存路径
path
:
./Downloaded/
#
Cookie配置（必填）
cookies
:
msToken
:
YOUR_MS_TOKEN_HERE
ttwid
:
YOUR_TTWID_HERE
odin_tt
:
YOUR_ODIN_TT_HERE
passport_csrf_token
:
YOUR_PASSPORT_CSRF_TOKEN_HERE
sid_guard
:
YOUR_SID_GUARD_HERE
#
下载选项
music
:
True
#
下载音乐
cover
:
True
#
下载封面
avatar
:
True
#
下载头像
json
:
True
#
保存JSON数据
#
下载模式
mode
:
  -
post
#
下载发布的作品
#
- like     # 下载喜欢的作品
#
- mix      # 下载合集
#
下载数量（0表示全部）
number
:
post
:
0
#
发布作品数量
like
:
0
#
喜欢作品数量
allmix
:
0
#
合集数量
mix
:
0
#
单个合集内作品数量
#
其他设置
thread
:
5
#
下载线程数
database
:
True
#
使用数据库记录
运行程序
#
使用配置文件运行
python DouYinCommand.py
#
或者使用命令行参数
python DouYinCommand.py --cmd False
使用示例
#
下载单个视频
#
在 config.yml 中设置 link 为单个视频链接
python DouYinCommand.py
#
下载用户主页
#
在 config.yml 中设置 link 为用户主页链接
python DouYinCommand.py
#
下载合集
#
在 config.yml 中设置 link 为合集链接
python DouYinCommand.py
🚀 V2.0 使用指南
命令行使用
#
下载单个视频（需要先配置 Cookie）
python downloader.py -u
"
https://v.douyin.com/xxxxx/
"
#
下载用户主页（推荐）
python downloader.py -u
"
https://www.douyin.com/user/xxxxx
"
#
自动获取 Cookie 并下载
python downloader.py --auto-cookie -u
"
https://www.douyin.com/user/xxxxx
"
#
指定保存路径
python downloader.py -u
"
链接
"
--path
"
./my_videos/
"
#
使用配置文件
python downloader.py --config
配置文件使用
创建配置文件
cp config.example.yml config_simple.yml
配置示例
#
下载链接
link
:
  -
https://www.douyin.com/user/xxxxx
#
保存路径
path
:
./Downloaded/
#
自动 Cookie 管理
auto_cookie
:
true
#
下载选项
music
:
true
cover
:
true
avatar
:
true
json
:
true
#
下载模式
mode
:
  -
post
#
下载数量
number
:
post
:
10
#
增量下载
increase
:
post
:
false
#
数据库
database
:
true
运行程序
python downloader.py --config
命令行参数
python downloader.py [选项] [链接...]

选项：
  -u, --url URL          下载链接
  -p, --path PATH        保存路径
  -c, --config           使用配置文件
  --auto-cookie          自动获取 Cookie
  --cookies COOKIES      手动指定 Cookie
  -h, --help            显示帮助信息
🍪 Cookie 配置工具
1. cookie_extractor.py - 自动获取工具
功能
：使用 Playwright 自动打开浏览器，自动获取 Cookie
使用方式
：
#
安装 Playwright
pip install playwright
playwright install chromium
#
运行自动获取
python cookie_extractor.py
特点
：
✅ 自动打开浏览器
✅ 支持扫码登录
✅ 自动检测登录状态
✅ 自动保存到配置文件
✅ 支持多种登录方式
使用步骤
：
运行
python cookie_extractor.py
选择提取方式（推荐选择1）
在打开的浏览器中完成登录
程序自动提取并保存 Cookie
2. get_cookies_manual.py - 手动获取工具
功能
：通过浏览器开发者工具手动获取 Cookie
使用方式
：
python get_cookies_manual.py
特点
：
✅ 无需安装 Playwright
✅ 详细的操作教程
✅ 支持 Cookie 验证
✅ 自动保存到配置文件
✅ 支持备份和恢复
使用步骤
：
运行
python get_cookies_manual.py
选择"获取新的Cookie"
按照教程在浏览器中获取 Cookie
粘贴 Cookie 内容
程序自动解析并保存
Cookie 获取教程
方法一：浏览器开发者工具
打开浏览器，访问
抖音网页版
登录你的抖音账号
按
F12
打开开发者工具
切换到
Network
标签页
刷新页面，找到任意请求
在请求头中找到
Cookie
字段
复制以下关键 cookie 值：
msToken
ttwid
odin_tt
passport_csrf_token
sid_guard
方法二：使用自动工具
#
推荐使用自动工具
python cookie_extractor.py
📋 支持的链接类型
🎬 视频内容
单个视频分享链接
：
https://v.douyin.com/xxxxx/
单个视频直链
：
https://www.douyin.com/video/xxxxx
图集作品
：
https://www.douyin.com/note/xxxxx
👤 用户内容
用户主页
：
https://www.douyin.com/user/xxxxx
支持下载用户发布的所有作品
支持下载用户喜欢的作品（需要权限）
📚 合集内容
用户合集
：
https://www.douyin.com/collection/xxxxx
音乐合集
：
https://www.douyin.com/music/xxxxx
🔴 直播内容
直播间
：
https://live.douyin.com/xxxxx
🔧 常见问题
Q: 为什么单个视频下载失败？
A
:
V1.0：请检查 Cookie 是否有效，确保包含必要的字段
V2.0：目前已知问题，API 返回空响应，建议使用用户主页下载
Q: Cookie 过期怎么办？
A
:
使用
python cookie_extractor.py
重新获取
或使用
python get_cookies_manual.py
手动获取
Q: 下载速度慢怎么办？
A
:
调整
thread
参数增加并发数
检查网络连接
避免同时下载过多内容
Q: 如何批量下载？
A
:
V1.0：在
config.yml
中添加多个链接
V2.0：使用命令行传入多个链接或使用配置文件
Q: 支持哪些格式？
A
:
视频：MP4 格式（无水印）
图片：JPG 格式
音频：MP3 格式
数据：JSON 格式
📝 更新日志
V2.0 (2025-08)
✅
统一入口
：整合所有功能到
downloader.py
✅
自动 Cookie 管理
：支持自动获取和刷新
✅
异步架构
：性能优化，支持并发下载
✅
智能重试
：自动重试和错误恢复
✅
增量下载
：支持增量更新
✅
用户主页下载
：完全正常工作
⚠️
单个视频下载
：API 返回空响应（已知问题）
V1.0 (2024-12)
✅
稳定可靠
：经过大量测试验证
✅
功能完整
：支持所有内容类型
✅
单个视频下载
：完全正常工作
✅
配置文件驱动
：简单易用
✅
数据库支持
：记录下载历史
⚖️ 法律声明
本项目仅供
学习交流
使用
请遵守相关法律法规和平台服务条款
不得用于商业用途或侵犯他人权益
下载内容请尊重原作者版权
🤝 贡献指南
欢迎提交 Issue 和 Pull Request！
报告问题
使用
Issues
报告 bug
请提供详细的错误信息和复现步骤
功能建议
在 Issues 中提出新功能建议
详细描述功能需求和使用场景
📄 许可证
本项目采用
MIT License
开源许可证。
如果这个项目对你有帮助，请给个 ⭐ Star 支持一下！
🐛 报告问题
•
💡 功能建议
•
📖 查看文档
Made with ❤️ by
jiji262
- 今日の獲得スター数: 60
- 累積スター数: 5,265

### References
- https://github.com/jiji262/douyin-downloader

## wmjordan/PDFPatcher

### Executive Summary
- PDF补丁丁——PDF工具箱，可以编辑书签、剪裁旋转页面、解除限制、提取或合并文档，探查文档结构，提取图片、转成图片等等
- ---
- PDF 补丁丁（PDFPatcher）
感谢您关注 PDF 补丁丁，请在使用软件或源代码前阅读本说明和授权协议。本软件及源代码采用 AGPL＋“
良心授权
”协议——
用户每次使用本软件后如有所获益，应行一善事；如使用源代码开发了新的软件并获得收益，应将收益中不低于千分之一的金额捐赠给社会的弱势群体
。
功能简介
PDF 补丁丁是一个 PDF 处理工具。它具有以下功能：
修改 PDF 文档：修改文档属性、页码编号、页面链接；统一页面尺寸；删除自动打开网页等动作；去除复制及打印限制；设置阅读器初始模式；清理文档隐藏垃圾数据；重新压缩黑白图片；旋转页面。
贴心 PDF 书签编辑器：带有阅读界面（具有便于阅读竖排文档的从右到左阅读方式），可批量修改 PDF 书签属性（颜色、样式、目标页码、缩放比例等），书签可精确定位到页面中间；在书签中执行查找替换（支持正则表达式及 XPath 匹配、可快速选择篇、章、节书签），
自动快速生成文档书签
。
制作 PDF 文件：合并已有 PDF 文件或图片，生成新的 PDF 文件；合并后的 PDF 文档带有原文档的书签，还可挂上新书签（或根据文件名生成），新书签文本和样式可自定义；合并的 PDF 文档可指定统一的页面尺寸，以便打印和阅读。
拆分或合并 PDF 文件，并保留原文件的书签或挂上新的书签。
高速无损导出 PDF 文档的图片。
将 PDF 页面转换为图片。
提取或删除 PDF 文档中指定的页面，调整 PDF 文档的页面顺序。
根据 PDF 文档元数据重命名 PDF 文件名。
调用微软 Office 的图像识别引擎分析 PDF 文档图片中的文字；将图片 PDF 的目录页转换为 PDF 书签。识别结果可写入 PDF 文件。
替换字体：替换文档中使用的字体；嵌入字库到 PDF 文档，消除复制文本时的乱码，使之可在没有字库的设备（如 Kindle 等电子书阅读器）上阅读。
分析文档结构：以树视图显示 PDF 文档结构，可编辑修改 PDF 文档节点，或将 PDF 文档导出成 XML 文件，供 PDF 爱好者分析、调试之用。
永久免费，绝不过期，无广告，无弹出废话对话框，不窥探隐私。
授权协议
《PDF 补丁丁》软件（以下简称本软件）受著作权法及国际条约条款和其它知识产权法及条约的保护。
本软件对于最终用户免费。由于本软件使用了带有 AGPL 条款的第三方开源组件，因此，本软件及其源代码的使用协议也基于 AGPL。另外还带有如下附加条件。在遵守本软件的前提条件下，你可以在遵循本协议的基础上自由的使用和传播它，你一旦安装、复制或使用本软件，则表示您已经同意本协议条款。如果你不同意本协议，请不要安装使用本软件，也不应利用其源代码。
附加条件：
每一个使用本软件的用户，如果本软件帮助了您，每使用本软件后，您应当做 1 件善事。善事无分大小，有心则行。例如：
如果您的父母在身边，你可以为您的父母做一顿美味的饭菜，或者为他们按摩、洗脚；如果他们身处远方，你可以向他们发起通话，问候他们的健康和生活。
在大雨滂沱的时候，如果您有雨伞，可与同路的人共享；在烈日当空的时节，如果您看到环卫工人太阳下工作，您可以为他们买一瓶水送给他们；在拥挤的公共交通工具上，或在公共场合排队等候之际，如果您有座位，可以让给老人、孕妇或提着重物的人就坐。
您可以用您擅长的技能，为身边的人排难解困；您可以将您的知识，分享给其他人，让他们有所获益；您可以向比您困难的人捐资赠物。
如果您觉得这个软件真的好用，请将它的使用方法介绍给别人，让别人也通过使用本软件而得到好处；或者将其它您觉得好用的软件介绍给别人。
如果您无法做到使用本软件后做 1 件善事，请记在心中。在有机会的时候，多行善积德。本用户协议之遵循与否，全在于您的良心。是为“
良心授权
”。
相关定义：
软件：软件是指《PDF 补丁丁》软件以及它的更新、产品手册，以及在线文档等相关载体。
限制：你可以使用本软件的源代码开发应用程序（自由、共享或商用），也可以任意方式分发数量不限的本软件的完整拷贝，但前提是：
① 你分发软件时必须提供本软件的完整版本，未经许可不得对软件乃至它的安装程序做任何修改；
② 你分发软件时不能更改本授权协议；
③ 你如果在商业性宣传活动、产品中附加本软件，应当获得著作权人的书面许可；
④ 你如果利用本软件的源代码编写了其它软件，并且产生了销售收入，应当将该软件销售收入不低于千分之一的金额捐献给社会上的弱势群体。
支持：软件会由于用户的需求而不断更新，著作权人将提供包括用户手册、电子邮件等各种相关信息支持，但软件不确保支持内容和功能不发生变更。
终止：当你不同意或者违背本协议的时候，协议将自动终止，你必须立即删除本软件产品。
版权：本软件及源代码受著作权法及国际条约条款和其它知识产权法及条约的保护。
免责：对于本软件安装、复制、使用中导致的任何损失，本软件及著作权人不负责任。
常用的 PDF 开源组件简介
PDF 文档的规范（ISO 32000-1:2008 《Document management — Portable document format — Part 1:PDF 1.7》）可从网上找到，一般来说，它是 PDF 处理程序开发者的必读文献。
PDF 文档格式中涉及印刷领域的多项技术，并有其独特的文档结构，还使用了多种数据压缩算法。要从零开始编写 PDF 文档的处理程序，对于一般人而言，通常是困难而不太现实的。PDF 补丁丁使用 .NET Framework 开发，主要采用 iText 和 MuPDF 这两个开放源代码的组件库来处理 PDF 文档。
前者是 .NET 组件，与 PDF 主程序具有较好的互操作性，并且在解析、生成和修改 PDF 文档，以及嵌入 TTF 字体子集这些功能上，优胜于后者。
后者采用 C 语言开发并编译，与前者相比，其最大的优点是具有渲染 PDF 文档为位图的功能。MuPDF 编译出来的动态组件库可在作者另一个开放源代码库
SharpMuPDF
下载。PDF 补丁丁通过 P/Invoke 技术调用该组件库的功能。
除了 PDF 开源组件之外，程序还使用了其它优秀开源组件。例如 ObjectListView 这个强大的列表控件、FreeImage 来读取和解码各种类型的点阵图像文件、Cyotek 的 ImageBox 用于显示渲染好的 PDF 文档页面、TabControlExtra 用于构建选项卡式文档界面、HTMLRenderer 用于显示 HTML 网页界面等等。
源代码的结构
App 目录：PDF 补丁丁主程序
Common：一些常用的工具类
Functions：用于呈现软件各类功能的窗体和控件
Lib：程序使用的第三方组件
Model：编辑文档时所用的高级模型（基础数据模型由 iText 和 MuPDF 的类实现）
Options：程序的选项
Processor：处理 PDF 文档的算法（其中 Mupdf 目录里放置了 P/Invoke 调用 MuPDF 的类）
doc 目录：放置程序的使用文档
JBig2 目录：放置 JBIG2 图像的编码和解码库代码
运行环境
Windows 7 以上版本的操作系统。
.NET Framework 4.0 到 4.8 版本。
使用文字识别功能需要安装 Microsoft Office 2003（或 2007）的 Document Imaging 组件（MODI）。
编译程序源代码，建议使用 Visual Studio 2022 或更新版本，并安装“.NET 桌面开发”（用于编译 PDF 补丁丁源代码）和“C++ 桌面开发”（用于编译 JBIG2 编码组件）两个工作负载。可能会遇到项目“面向不再受支持的 .NET Framework”、需要“将目标更新为 .NET Framework 4.8”的问题。简单方法是将目标更新为 .NET Framework 4.8，如不更新目标，请参考
这篇文章介绍的方法
。
联系作者
除第三方组件外，本软件的源代码完全开放：
https://github.com/wmjordan/PDFPatcher
https://gitee.com/wmjordan/pdfpatcher
建议通过开放源代码网站通过提交 issue 的方式提交您的建议或需求。因日常工作繁忙，暂不提供加 QQ 或微信咨询的服务，敬请谅解。
在邮件或消息中，请注明你的版本号，附上截图和附件，详细说明你遇到的问题。
如遇到需要提供附件的情况，请把它搞小一点。一般情况下，最好不要发送超过 10M 的附件。
对于 PDF 文件，可用“提取页面”功能提取有代表性的页面。
对于图片文件，请压缩源文件，或提供有代表性的一两页图片。
- 今日の獲得スター数: 56
- 累積スター数: 10,561

### References
- https://github.com/wmjordan/PDFPatcher

## Mentra-Community/MentraOS

### Executive Summary
- The open-source OS for smart glasses with dozens of apps. Get captions, AI assistant, notifications, translation, and more. Devs now write 1 app that runs on any pair of smart glases.
- ---
- MentraOS
The open source operating system for smart glasses
Website
•
Documentation
•
Developer Console
•
Mentra Store
Supported Smart Glasses
Works with Even Realities G1, Mentra Mach 1, Mentra Live. See
smart glasses compatibility list here
.
Apps on Mentra Store
The Mentra Store already has a ton of useful apps that real users are running everyday. Here are some apps already published by developers on the Mentra Store:
Live Captions
Link
Merge
Notes
Calendar
Dash
Translation
→ Browse All Apps
Write Once, Run on Any Smart Glasses
MentraOS is how developers build smart glasses apps.
We handle the pairing, connection, data streaming, and cross-compatibility, so you can focus on creating amazing apps. Every component is 100% open source (MIT license).
Why Build with MentraOS?
Cross Compatibility
: Your app runs on any pair of smart glasses
Speed
: TypeScript SDK means you're making apps in minutes, not months
Control
: Access smart glasses I/O - displays, microphones, cameras, speakers
Distribution
: Get your app in front of everyone using smart glasses
MentraOS Community
The MentraOS Community is a group of developers, companies, and users dedicated to ensuring the next personal computer is open, cross-compatible, and user-controlled. That's why we're building MentraOS.
To get involved, join the
MentraOS Community Discord server
.
Contact
Have questions or ideas? We'd love to hear from you!
Email
:
team@mentra.glass
Discord
:
Join our community
Twitter
:
Follow @mentralabs
Contributing
MentraOS is made by a community and we welcome PRs. Here's the Contributors Guide:
docs.mentra.glass/contributing
License
MIT License Copyright 2025 MentraOS Community
© 2025 Mentra Labs
- 今日の獲得スター数: 55
- 累積スター数: 1,316

### References
- https://github.com/Mentra-Community/MentraOS

## rustfs/rustfs

### Executive Summary
- 🚀 High-performance distributed object storage for MinIO alternative.
- ---
- RustFS is a high-performance distributed object storage software built using Rust
Getting Started
·
Docs
·
Bug reports
·
Discussions
English |
简体中文
|
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
RustFS is a high-performance distributed object storage software built using Rust, one of the most popular languages worldwide. Along with MinIO, it shares a range of advantages such as simplicity, S3 compatibility, open-source nature, support for data lakes, AI, and big data. Furthermore, it has a better and more user-friendly open-source license in comparison to other storage systems, being constructed under the Apache license. As Rust serves as its foundation, RustFS provides faster speed and safer distributed features for high-performance object storage.
⚠️
RustFS is under rapid development. Do NOT use in production environments!
Features
High Performance
: Built with Rust, ensuring speed and efficiency.
Distributed Architecture
: Scalable and fault-tolerant design for large-scale deployments.
S3 Compatibility
: Seamless integration with existing S3-compatible applications.
Data Lake Support
: Optimized for big data and AI workloads.
Open Source
: Licensed under Apache 2.0, encouraging community contributions and transparency.
User-Friendly
: Designed with simplicity in mind, making it easy to deploy and manage.
RustFS vs MinIO
Stress test server parameters
Type
parameter
Remark
CPU
2 Core
Intel Xeon(Sapphire Rapids) Platinum 8475B , 2.7/3.2 GHz
Memory
4GB
Network
15Gbp
Driver
40GB x 4
IOPS 3800 / Driver
rustfs.mp4
RustFS vs Other object storage
RustFS
Other object storage
Powerful Console
Simple and useless Console
Developed based on Rust language, memory is safer
Developed in Go or C, with potential issues like memory GC/leaks
Does not report logs to third-party countries
Reporting logs to other third countries may violate national security laws
Licensed under Apache, more business-friendly
AGPL V3 License and other License, polluted open source and License traps, infringement of intellectual property rights
Comprehensive S3 support, works with domestic and international cloud providers
Full support for S3, but no local cloud vendor support
Rust-based development, strong support for secure and innovative devices
Poor support for edge gateways and secure innovative devices
Stable commercial prices, free community support
High pricing, with costs up to $250,000 for 1PiB
No risk
Intellectual property risks and risks of prohibited uses
Quickstart
To get started with RustFS, follow these steps:
One-click installation script (Option 1)​​
curl -O  https://rustfs.com/install_rustfs.sh
&&
bash install_rustfs.sh
Docker Quick Start (Option 2)​​
#
create data and logs directories
mkdir -p data logs
#
using latest alpha version
docker run -d -p 9000:9000 -v
$(
pwd
)
/data:/data -v
$(
pwd
)
/logs:/logs rustfs/rustfs:alpha
#
Specific version
docker run -d -p 9000:9000 -v
$(
pwd
)
/data:/data -v
$(
pwd
)
/logs:/logs rustfs/rustfs:1.0.0.alpha.45
For docker installation, you can also run the container with docker compose. With the
docker-compose.yml
file under root directory, running the command:
docker compose --profile observability up -d
NOTE
: You should be better to have a look for
docker-compose.yaml
file. Because, several services contains in the file. Grafan,prometheus,jaeger containers will be launched using docker compose file, which is helpful for rustfs observability. If you want to start redis as well as nginx container, you can specify the corresponding profiles.
Build from Source (Option 3) - Advanced Users
For developers who want to build RustFS Docker images from source with multi-architecture support:
#
Build multi-architecture images locally
./docker-buildx.sh --build-arg RELEASE=latest
#
Build and push to registry
./docker-buildx.sh --push
#
Build specific version
./docker-buildx.sh --release v1.0.0 --push
#
Build for custom registry
./docker-buildx.sh --registry your-registry.com --namespace yourname --push
The
docker-buildx.sh
script supports:
Multi-architecture builds
:
linux/amd64
,
linux/arm64
Automatic version detection
: Uses git tags or commit hashes
Registry flexibility
: Supports Docker Hub, GitHub Container Registry, etc.
Build optimization
: Includes caching and parallel builds
You can also use Make targets for convenience:
make docker-buildx
#
Build locally
make docker-buildx-push
#
Build and push
make docker-buildx-version VERSION=v1.0.0
#
Build specific version
make help-docker
#
Show all Docker-related commands
Access the Console
: Open your web browser and navigate to
http://localhost:9000
to access the RustFS console, default username and password is
rustfsadmin
.
Create a Bucket
: Use the console to create a new bucket for your objects.
Upload Objects
: You can upload files directly through the console or use S3-compatible APIs to interact with your RustFS instance.
NOTE
: If you want to access RustFS instance with
https
, you can refer to
TLS configuration docs
.
Documentation
For detailed documentation, including configuration options, API references, and advanced usage, please visit our
Documentation
.
Getting Help
If you have any questions or need assistance, you can:
Check the
FAQ
for common issues and solutions.
Join our
GitHub Discussions
to ask questions and share your experiences.
Open an issue on our
GitHub Issues
page for bug reports or feature requests.
Links
Documentation
- The manual you should read
Changelog
- What we broke and fixed
GitHub Discussions
- Where the community lives
Contact
Bugs
:
GitHub Issues
Business
:
hello@rustfs.com
Jobs
:
jobs@rustfs.com
General Discussion
:
GitHub Discussions
Contributing
:
CONTRIBUTING.md
Contributors
RustFS is a community-driven project, and we appreciate all contributions. Check out the
Contributors
page to see the amazing people who have helped make RustFS better.
License
Apache 2.0
RustFS
is a trademark of RustFS, Inc. All other trademarks are the property of their respective owners.
- 今日の獲得スター数: 52
- 累積スター数: 8,877

### References
- https://github.com/rustfs/rustfs

## krahets/hello-algo

### Executive Summary
- 《Hello 算法》：动画图解、一键运行的数据结构与算法教程。支持 Python, Java, C++, C, C#, JS, Go, Swift, Rust, Ruby, Kotlin, TS, Dart 代码。简体版和繁体版同步更新，English version in translation
- ---
- 动画图解、一键运行的数据结构与算法教程
简体中文
  ｜
繁體中文
｜
English
关于本书
本项目旨在打造一本开源免费、新手友好的数据结构与算法入门教程。
全书采用动画图解，内容清晰易懂、学习曲线平滑，引导初学者探索数据结构与算法的知识地图。
源代码可一键运行，帮助读者在练习中提升编程技能，了解算法工作原理和数据结构底层实现。
提倡读者互助学习，欢迎大家在评论区提出问题与分享见解，在交流讨论中共同进步。
若本书对您有所帮助，请在页面右上角点个 Star ⭐ 支持一下，谢谢！
推荐语
“一本通俗易懂的数据结构与算法入门书，引导读者手脑并用地学习，强烈推荐算法初学者阅读。”
—— 邓俊辉，清华大学计算机系教授
“如果我当年学数据结构与算法的时候有《Hello 算法》，学起来应该会简单 10 倍！”
—— 李沐，亚马逊资深首席科学家
鸣谢
Warp is built for coding with multiple AI agents.
强烈推荐 Warp 终端，高颜值 + 好用的 AI，体验非常棒！
贡献
本开源书仍在持续更新之中，欢迎您参与本项目，一同为读者提供更优质的学习内容。
内容修正
：请您协助修正或在评论区指出语法错误、内容缺失、文字歧义、无效链接或代码 bug 等问题。
代码转译
：期待您贡献各种语言代码，已支持 Python、Java、C++、Go、JavaScript 等 12 门编程语言。
中译英
：诚邀您加入我们的翻译小组，成员主要来自计算机相关专业、英语专业和英文母语者。
欢迎您提出宝贵意见和建议，如有任何问题请提交 Issues 或微信联系
krahets-jyd
。
感谢本开源书的每一位撰稿人，是他们的无私奉献让这本书变得更好，他们是：
License
The texts, code, images, photos, and videos in this repository are licensed under
CC BY-NC-SA 4.0
.
- 今日の獲得スター数: 51
- 累積スター数: 117,629

### References
- https://github.com/krahets/hello-algo

## coollabsio/coolify

### Executive Summary
- An open-source & self-hostable Heroku / Netlify / Vercel alternative.
- ---
- About the Project
Coolify is an open-source & self-hostable alternative to Heroku / Netlify / Vercel / etc.
It helps you manage your servers, applications, and databases on your own hardware; you only need an SSH connection. You can manage VPS, Bare Metal, Raspberry PIs, and anything else.
Imagine having the ease of a cloud but with your own servers. That is
Coolify
.
No vendor lock-in, which means that all the configurations for your applications/databases/etc are saved to your server. So, if you decide to stop using Coolify (oh nooo), you could still manage your running resources. You lose the automations and all the magic. 🪄️
For more information, take a look at our landing page at
coolify.io
.
Installation
curl -fsSL https://cdn.coollabs.io/coolify/install.sh
|
bash
You can find the installation script source
here
.
Note
Please refer to the
docs
for more information about the installation.
Support
Contact us at
coolify.io/docs/contact
.
Cloud
If you do not want to self-host Coolify, there is a paid cloud version available:
app.coolify.io
For more information & pricing, take a look at our landing page
coolify.io
.
Why should I use the Cloud version?
The recommended way to use Coolify is to have one server for Coolify and one (or more) for the resources you are deploying. A server is around 4-5$/month.
By subscribing to the cloud version, you get the Coolify server for the same price, but with:
High-availability
Free email notifications
Better support
Less maintenance for you
Donations
To stay completely free and open-source, with no feature behind the paywall and evolve the project, we need your help. If you like Coolify, please consider donating to help us fund the project's future development.
coolify.io/sponsorships
Thank you so much!
Big Sponsors
CubePath
- Dedicated Servers & Instant Deploy
GlueOps
- DevOps automation and infrastructure management
Algora
- Open source contribution platform
Ubicloud
- Open source cloud infrastructure platform
LiquidWeb
- Premium managed hosting solutions
Convex
- Open-source reactive database for web app developers
Arcjet
- Advanced web security and performance solutions
SaasyKit
- Complete SaaS starter kit for developers
SupaGuide
- Your comprehensive guide to Supabase
Logto
- The better identity infrastructure for developers
Trieve
- AI-powered search and analytics
Supadata AI
- Scrape YouTube, web, and files. Get AI-ready, clean data
Darweb
- Design. Develop. Deliver. Specialized in 3D CPQ Solutions
Hetzner
- Server, cloud, hosting, and data center solutions
COMIT
- New York Times award–winning contractor
Blacksmith
- Infrastructure automation platform
WZ-IT
- German agency for customised cloud solutions
BC Direct
- Your trusted technology consulting partner
Tigris
- Modern developer data platform
Hostinger
- Web hosting and VPS solutions
QuantCDN
- Enterprise-grade content delivery network
PFGLabs
- Build Real Projects with Golang
JobsCollider
- 30,000+ remote jobs for developers
Juxtdigital
- Digital PR & AI Authority Building Agency
Cloudify.ro
- Cloud hosting solutions
CodeRabbit
- Cut Code Review Time & Bugs in Half
American Cloud
- US-based cloud infrastructure services
MassiveGrid
- Enterprise cloud hosting solutions
Syntax.fm
- Podcast for web developers
Tolgee
- The open source localization platform
CompAI
- Open source compliance automation platform
GoldenVM
- Premium virtual machine hosting solutions
Gozunga
- Seriously Simple Cloud Infrastructure
Macarne
- Best IP Transit & Carrier Ethernet Solutions for Simplified Network Connectivity
Small Sponsors
...and many more at
GitHub Sponsors
Recognitions
Core Maintainers
Andras Bacsai
🏔️ Peak
Repo Activity
Star History
- 今日の獲得スター数: 49
- 累積スター数: 46,176

### References
- https://github.com/coollabsio/coolify

## hyprwm/Hyprland

### Executive Summary
- Hyprland is an independent, highly customizable, dynamic tiling Wayland compositor that doesn't sacrifice on its looks.
- ---
- Hyprland is a 100% independent, dynamic tiling Wayland compositor that doesn't sacrifice on its looks.
It provides the latest Wayland features, is highly customizable, has all the eyecandy, the most powerful plugins,
easy IPC, much more QoL stuff than other compositors and more...
Install
Quick Start
Configure
Contribute
Features
All of the eyecandy: gradient borders, blur, animations, shadows and much more
A lot of customization
100% independent, no wlroots, no libweston, no kwin, no mutter.
Custom bezier curves for the best animations
Powerful plugin support
Built-in plugin manager
Tearing support for better gaming performance
Easily expandable and readable codebase
Fast and active development
Not afraid to provide bleeding-edge features
Config reloaded instantly upon saving
Fully dynamic workspaces
Two built-in layouts and more available as plugins
Global keybinds passed to your apps of choice
Tiling/pseudotiling/floating/fullscreen windows
Special workspaces (scratchpads)
Window groups (tabbed mode)
Powerful window/monitor/layer rules
Socket-based IPC
Native IME and Input Panels Support
and much more...
Gallery
Special Thanks
wlroots
-
For powering Hyprland in the past
tinywl
-
For showing how 2 do stuff
Sway
-
For showing how 2 do stuff the overkill way
Vivarium
-
For showing how 2 do stuff the simple way
dwl
-
For showing how 2 do stuff the hacky way
Wayfire
-
For showing how 2 do some graphics stuff
- 今日の獲得スター数: 49
- 累積スター数: 31,051

### References
- https://github.com/hyprwm/Hyprland

## tangyoha/telegram_media_downloader

### Executive Summary
- 基于Dineshkarthik的项目， 电报视频下载，电报资源下载，跨平台，支持web查看下载进度 ，支持bot下发指令下载，支持下载已经加入的私有群但是限制下载的资源， telegram media download,Download media files from a telegram conversation/chat/channel up to 2GiB per file
- ---
- Telegram Media Downloader
中文
·
Feature request
·
Report a bug
·
Support:
Discussions
&
Telegram Community
Overview
Support two default running
The robot is running, and the command
download
or
forward
is issued from the robot
Download as a one-time download tool
UI
Web page
After running, open a browser and visit
localhost:5000
If it is a remote machine, you need to configure web_host: 0.0.0.0
Robot
Need to configure bot_token, please refer to
Documentation
Support
Category
Support
Language
Python 3.7
and above
Download media types
audio, document, photo, video, video_note, voice
Version release plan
v2.2.0
Installation
For *nix os distributions with
make
availability
git clone https://github.com/tangyoha/telegram_media_downloader.git
cd
telegram_media_downloader
make install
For Windows which doesn't have
make
inbuilt
git clone https://github.com/tangyoha/telegram_media_downloader.git
cd
telegram_media_downloader
pip3 install -r requirements.txt
Docker
For more detailed installation tutorial, please check the wiki
Make sure you have
docker
and
docker-compose
installed
docker pull tangyoha/telegram_media_downloader:latest
mkdir -p
~
/app
&&
mkdir -p
~
/app/log/
&&
cd
~
/app
wget https://raw.githubusercontent.com/tangyoha/telegram_media_downloader/master/docker-compose.yaml -O docker-compose.yaml
wget https://raw.githubusercontent.com/tangyoha/telegram_media_downloader/master/config.yaml -O config.yaml
wget https://raw.githubusercontent.com/tangyoha/telegram_media_downloader/master/data.yaml -O data.yaml
#
vi config.yaml and docker-compose.yaml
vi config.yaml
#
The first time you need to start the foreground
#
enter your phone number and code, then exit(ctrl + c)
docker-compose run --rm telegram_media_downloader
#
After performing the above operations, all subsequent startups will start in the background
docker-compose up -d
#
Upgrade
docker pull tangyoha/telegram_media_downloader:latest
cd
~
/app
docker-compose down
docker-compose up -d
Upgrade installation
cd
telegram_media_downloader
pip3 install -r requirements.txt
Configuration
All the configurations are  passed to the Telegram Media Downloader via
config.yaml
file.
Getting your API Keys:
The very first step requires you to obtain a valid Telegram API key (API id/hash pair):
Visit
https://my.telegram.org/apps
and log in with your Telegram Account.
Fill out the form to register a new Telegram application.
Done! The API key consists of two parts:
api_id
and
api_hash
.
Getting chat id:
1. Using web telegram:
Open
https://web.telegram.org/?legacy=1#/im
Now go to the chat/channel and you will see the URL as something like
https://web.telegram.org/?legacy=1#/im?p=u853521067_2449618633394
here
853521067
is the chat id.
https://web.telegram.org/?legacy=1#/im?p=@somename
here
somename
is the chat id.
https://web.telegram.org/?legacy=1#/im?p=s1301254321_6925449697188775560
here take
1301254321
and add
-100
to the start of the id =>
-1001301254321
.
https://web.telegram.org/?legacy=1#/im?p=c1301254321_6925449697188775560
here take
1301254321
and add
-100
to the start of the id =>
-1001301254321
.
2. Using bot:
Use
@username_to_id_bot
to get the chat_id of
almost any telegram user: send username to the bot or just forward their message to the bot
any chat: send chat username or copy and send its joinchat link to the bot
public or private channel: same as chats, just copy and send to the bot
id of any telegram bot
config.yaml
api_hash
:
your_api_hash
api_id
:
your_api_id
chat
:
-
chat_id
:
telegram_chat_id
last_read_message_id
:
0
download_filter
:
message_date >= 2022-12-01 00:00:00 and message_date <= 2023-01-17 00:00:00
-
chat_id
:
telegram_chat_id_2
last_read_message_id
:
0
#
note we remove ids_to_retry to data.yaml
ids_to_retry
:
[]
media_types
:
-
audio
-
document
-
photo
-
video
-
voice
-
animation
#
gif
file_formats
:
audio
:
  -
all
document
:
  -
pdf
-
epub
video
:
  -
mp4
save_path
:
D:\telegram_media_downloader
file_path_prefix
:
-
chat_title
-
media_datetime
upload_drive
:
#
required
enable_upload_file
:
true
#
required
remote_dir
:
drive:/telegram
#
required
upload_adapter
:
rclone
#
option,when config upload_adapter rclone then this config are required
rclone_path
:
D:\rclone\rclone.exe
#
option
before_upload_file_zip
:
True
#
option
after_upload_file_delete
:
True
hide_file_name
:
true
file_name_prefix
:
-
message_id
-
file_name
file_name_prefix_split
:
'
-
'
max_download_task
:
5
web_host
:
127.0.0.1
web_port
:
5000
language
:
EN
web_login_secret
:
123
allowed_user_ids
:
-
'
me
'
date_format
:
'
%Y_%m
'
enable_download_txt
:
false
api_hash
- The api_hash you got from telegram apps
api_id
- The api_id you got from telegram apps
bot_token
- Your bot token
chat
- Chat list
chat_id
-  The id of the chat/channel you want to download media. Which you get from the above-mentioned steps.
download_filter
- Download filter, see
How to use Filter
last_read_message_id
- If it is the first time you are going to read the channel let it be
0
or if you have already used this script to download media it will have some numbers which are auto-updated after the scripts successful execution. Don't change it.
ids_to_retry
-
Leave it as it is.
This is used by the downloader script to keep track of all skipped downloads so that it can be downloaded during the next execution of the script.
media_types
- Type of media to download, you can update which type of media you want to download it can be one or any of the available types.
file_formats
- File types to download for supported media types which are
audio
,
document
and
video
. Default format is
all
, downloads all files.
save_path
- The root directory where you want to store downloaded files.
file_path_prefix
- Store file subfolders, the order of the list is not fixed, can be randomly combined.
chat_title
- Channel or group title, it will be chat id if not exist title.
media_datetime
- Media date.
media_type
- Media type, also see
media_types
.
upload_drive
- You can upload file to cloud drive.
enable_upload_file
- Enable upload file, default
false
.
remote_dir
- Where you upload, like
drive_id/drive_name
.
upload_adapter
- Upload file adapter, which can be
rclone
,
aligo
. If it is
rclone
, it supports all
rclone
servers that support uploading. If it is
aligo
, it supports uploading
Ali cloud disk
.
rclone_path
- RClone exe path, see
How to use rclone
before_upload_file_zip
- Zip file before upload, default
false
.
after_upload_file_delete
- Delete file after upload success, default
false
.
file_name_prefix
- Custom file name, use the same as
file_path_prefix
message_id
- Message id
file_name
- File name (may be empty)
caption
- The title of the message (may be empty)
file_name_prefix_split
- Custom file name prefix symbol, the default is
-
max_download_task
- The maximum number of task download tasks, the default is 5.
hide_file_name
- Whether to hide the web interface file name, default
false
web_host
- Web host
web_port
- Web port
language
- Application language, the default is English (
EN
), optional
ZH
(Chinese),
RU
,
UA
web_login_secret
- Web page login password, if not configured, no login is required to access the web page
log_level
- see
logging._nameToLevel
.
forward_limit
- Limit the number of forwards per minute, the default is 33, please do not modify this parameter by default.
allowed_user_ids
- Who is allowed to use the robot? The default login account can be used. Please add single quotes to the name with @.
date_format
Support custom configuration of media_datetime format in file_path_prefix.see
python-datetime
enable_download_txt
Enable download txt file, default
false
Execution
python3 media_downloader.py
All downloaded media will be stored at the root of
save_path
.
The specific location reference is as follows:
The complete directory of video download is:
save_path
/
chat_title
/
media_datetime
/
media_type
.
The order of the list is not fixed and can be randomly combined.
If the configuration is empty, all files are saved under
save_path
.
Proxy
socks4, socks5, http
proxies are supported in this project currently. To use it, add the following to the bottom of your
config.yaml
file
proxy
:
scheme
:
socks5
hostname
:
127.0.0.1
port
:
1234
username
:
your_username(delete the line if none)
password
:
your_password(delete the line if none)
If your proxy doesn’t require authorization you can omit username and password. Then the proxy will automatically be enabled.
Contributing
Contributing Guidelines
Read through our
contributing guidelines
to learn about our submission process, coding rules and more.
Want to Help?
Want to file a bug, contribute some code, or improve documentation? Excellent! Read up on our guidelines for
contributing
.
Code of Conduct
Help us keep Telegram Media Downloader open and inclusive. Please read and follow our
Code of Conduct
.
Sponsor
PayPal
- 今日の獲得スター数: 48
- 累積スター数: 4,112

### References
- https://github.com/tangyoha/telegram_media_downloader

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
- 今日の獲得スター数: 47
- 累積スター数: 31,009

### References
- https://github.com/DioxusLabs/dioxus

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
- 今日の獲得スター数: 46
- 累積スター数: 4,482

### References
- https://github.com/WECENG/ticket-purchase

## coze-dev/coze-studio

### Executive Summary
- An AI agent development platform with all-in-one visual tools, simplifying agent creation, debugging, and deployment like never before. Coze your way to AI Agent creation.
- ---
- Coze Studio
•
Feature list
•
Quickstart
•
Developer Guide
English |
中文
What is Coze Studio?
Coze Studio
is an all-in-one AI agent development tool. Providing the latest large models and tools, various development modes and frameworks, Coze Studio offers the most convenient AI agent development environment, from development to deployment.
Provides all core technologies needed for AI agent development
: prompt, RAG, plugin, workflow, enabling developers to focus on creating the core value of AI.
Ready to use for professional AI agent development at the lowest cost
: Coze Studio provides developers with complete app templates and build frameworks, allowing you to quickly construct various AI agents and turn creative ideas into reality.
Coze Studio, derived from the "Coze Development Platform" which has served tens of thousands of enterprises and millions of developers, we have made its core engine completely open. It is a one-stop visual development tool for AI Agents that makes creating, debugging, and deploying AI Agents unprecedentedly simple. Through Coze Studio's visual design and build tools, developers can quickly create and debug agents, apps, and workflows using no-code or low-code approaches, enabling powerful AI app development and more customized business logic. It's an ideal choice for building low-code AI products tailored . Coze Studio aims to lower the threshold for AI agent development and application, encouraging community co-construction and sharing for deeper exploration and practice in the AI field.
The backend of Coze Studio is developed using Golang, the frontend uses React + TypeScript, and the overall architecture is based on microservices and built following domain-driven design (DDD) principles. Provide developers with a high-performance, highly scalable, and easy-to-customize underlying framework to help them address complex business needs.
Feature list
Module
Feature
Model service
Manage the model list, integrate services such as OpenAI and Volcengine
Build agent
* Build, publish, and manage agent
* Support configuring workflows, knowledge bases, and other resources
Build apps
* Create and publish apps
* Build business logic through workflows
Build a workflow
Create, modify, publish, and delete workflows
Develop resources
Support creating and managing the following resources:
* Plugins
* Knowledge bases
* Databases
* Prompts
API and SDK
* Create conversations, initiate chats, and other OpenAPI
* Integrate agents or apps into your own app through Chat SDK
Quickstart
Learn how to obtain and deploy the open-source version of Coze Studio, quickly build projects, and experience Coze Studio's open-source version.
Environment requirements:
Before installing Coze Studio, please ensure that your machine meets the following minimum system requirements: 2 Core、4 GB
Pre-install Docker and Docker Compose, and start the Docker service.
Deployment steps:
Retrieve the source code.
#
Clone code
git clone https://github.com/coze-dev/coze-studio.git
Configure the model.
Copy the template files of the doubao-seed-1.6 model from the template directory and paste them into the configuration file directory.
cd
coze-studio
#
Copy model configuration template
cp backend/conf/model/template/model_template_ark_doubao-seed-1.6.yaml backend/conf/model/ark_doubao-seed-1.6.yaml
Modify the template file in the configuration file directory.
Enter the directory
backend/conf/model
. Open the file
ark_doubao-seed-1.6.yaml
.
Set the fields
id
,
meta.conn_config.api_key
,
meta.conn_config.model
, and save the file.
id
: The model ID in Coze Studio, defined by the developer, must be a non-zero integer and globally unique. Agents or workflows call models based on model IDs. For models that have already been launched, do not modify their IDs; otherwise, it may result in model call failures.
meta.conn_config.api_key
: The API Key for the model service. In this example, it is the API Key for Ark API Key. For more information, see
Get Volcengine Ark API Key
or
Get BytePlus ModelArk API Key
.
meta.conn_config.model
: The Model name for the model service. In this example, it refers to the Model ID or Endpoint ID of Ark. For more information, see
Get Volcengine Ark Model ID
/
Get Volcengine Ark Endpoint ID
or
Get BytePlus ModelArk Model ID
/
Get BytePlus ModelArk Endpoint ID
.
For users in China, you may use Volcengine Ark; for users outside China, you may use BytePlus ModelArk instead.
Deploy and start the service.
When deploying and starting Coze Studio for the first time, it may take a while to retrieve images and build local images. Please be patient. During deployment, you will see the following log information. If you see the message "Container coze-server Started," it means the Coze Studio service has started successfully.
#
Start the service
cd
docker
cp .env.example .env
docker compose up -d
For common startup failure issues,
please refer to the
FAQ
.
After starting the service, you can open Coze Studio by accessing
http://localhost:8888/
through your browser.
Warning
If you want to deploy Coze Studio in a public network environment, it is recommended to assess security risks before you begin, and take corresponding protection measures. Possible security risks include account registration functions, Python execution environments in workflow code nodes, Coze Server listening address configurations, SSRF (Server - Side Request Forgery), and some horizontal privilege escalations in APIs.  For more details, refer to
Quickstart
.
Developer Guide
Project Configuration
:
Model Configuration
: Before deploying the open-source version of Coze Studio, you must configure the model service. Otherwise, you cannot select models when building agents, workflows, and apps.
Plugin Configuration
: To use official plugins from the plugin store, you must first configure the plugins and add the authentication keys for third-party services.
Basic Component Configuration
: Learn how to configure components such as image uploaders to use functions like image uploading in Coze Studio .
API Reference
: The Coze Studio Community Edition API and Chat SDK are authenticated using Personal Access Token, providing APIs for conversations and workflows.
Development Guidelines
:
Project Architecture
: Learn about the technical architecture and core components of the open-source version of Coze Studio.
Code Development and Testing
: Learn how to perform secondary development and testing based on the open-source version of Coze Studio.
Troubleshooting
: Learn how to view container states and system logs.
Using the open-source version of Coze Studio
Regarding how to use Coze Studio, refer to the
Coze Development Platform Official Documentation Center
for more information. Please note that certain features, such as tone customization, are limited to the commercial version. Differences between the open-source and commercial versions can be found in the
Feature List
.
Quick Start
: Quickly build an AI assistant agent with Coze Studio.
Developing Agents
: Learn how to create, build, publish, and manage agents. You can use functions such as knowledge, plugins, etc., to resolve model hallucination and lack of expertise in professional fields. In addition, Coze Studio provides rich memory features that enable agents to generate more accurate responses based on a personal user's historical conversations during interactions.
Develop workflows
: A workflow is a set of executable instructions used to implement business logic or complete specific tasks. It structures data flow and task processing for apps or agents. Coze Studio provides a visual canvas where you can quickly build workflows by dragging and dropping nodes.
Resources such as plugins
: In Coze Studio, workflows, plugins, databases, knowledge bases, and variables are collectively referred to as resources.
API & SDK
: Coze Studio supports
API related to chat and workflows
, and you can also integrate agents or apps with local business systems through
Chat SDK
.
Tutorials for practice
: Learn how to use Coze Studio to implement various AI scenarios, such as building web-based online customer service using Chat SDK.
License
This project uses the Apache 2.0 license. For details, please refer to the
LICENSE
file.
Community contributions
We welcome community contributions. For contribution guidelines, please refer to
CONTRIBUTING
and
Code of conduct
. We look forward to your contributions!
Security and privacy
If you discover potential security issues in the project, or believe you may have found a security issue, please notify the ByteDance security team through our
security center
or
vulnerability reporting email
.
Please
do not
create public GitHub Issues.
Join Community
We are committed to building an open and friendly developer community. All developers interested in AI Agent development are welcome to join us!
🐛 Issue Reports & Feature Requests
To efficiently track and resolve issues while ensuring transparency and collaboration, we recommend participating through:
GitHub Issues
:
Submit bug reports or feature requests
Pull Requests
:
Contribute code or documentation improvements
💬 Technical Discussion & Communication
Join our technical discussion groups to share experiences with other developers and stay updated with the latest project developments:
Feishu Group Chat
Scan the QR code below with Feishu mobile app to join:
Discord Server
Click to join:
Coze Community
Telegram Group
Click to join: Telegram Group
Coze
Acknowledgments
Thank you to all the developers and community members who have contributed to the Coze Studio project. Special thanks:
The
Eino
framework team - providing powerful support for Coze Studio's agent and workflow runtime engines, model abstractions and implementations, and knowledge base indexing and retrieval
The
FlowGram
team - providing a high-quality workflow building engine for Coze Studio's frontend workflow canvas editor
The
Hertz
team - Go HTTP framework with high-performance and strong-extensibility for building micro-services
All users who participated in testing and feedback
- 今日の獲得スター数: 44
- 累積スター数: 17,538

### References
- https://github.com/coze-dev/coze-studio

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
- 今日の獲得スター数: 42
- 累積スター数: 57,217

### References
- https://github.com/jgraph/drawio-desktop

## microsoft/RD-Agent

### Executive Summary
- Research and development (R&D) is crucial for the enhancement of industrial productivity, especially in the AI era, where the core aspects of R&D are mainly focused on data and models. We are committed to automating these high-value generic R&D processes through R&D-Agent, which lets AI drive data-driven AI. 🔗https://aka.ms/RD-Agent-Tech-Report
- ---
- 🖥️ Live Demo
|
🎥 Demo Video
▶️
YouTube
|
📖 Documentation
|
📄 Tech Report
|
📃 Papers
📰 News
🗞️ News
📝 Description
NeurIPS 2025 Acceptance
We are thrilled to announce that our paper
R&D-Agent-Quant
has been accepted to NeurIPS 2025
Technical Report Release
Overall framework description and results on MLE-bench
R&D-Agent-Quant Release
Apply R&D-Agent to quant trading
MLE-Bench Results Released
R&D-Agent currently leads as the
top-performing machine learning engineering agent
on MLE-bench
Support LiteLLM Backend
We now fully support
LiteLLM
as our default backend for integration with multiple LLM providers.
General Data Science Agent
Data Science Agent
Kaggle Scenario release
We release
Kaggle Agent
, try the new features!
Official WeChat group release
We created a WeChat group, welcome to join! (🗪
QR Code
)
Official Discord release
We launch our first chatting channel in Discord (🗪
)
First release
R&D-Agent
is released on GitHub
🏆 The Best Machine Learning Engineering Agent!
MLE-bench
is a comprehensive benchmark evaluating the performance of AI agents on machine learning engineering tasks. Utilizing datasets from 75 Kaggle competitions, MLE-bench provides robust assessments of AI systems' capabilities in real-world ML engineering scenarios.
R&D-Agent currently leads as the top-performing machine learning engineering agent on MLE-bench:
Agent
Low == Lite (%)
Medium (%)
High (%)
All (%)
R&D-Agent o3(R)+GPT-4.1(D)
51.52 ± 6.9
19.3 ± 5.5
26.67 ± 0
30.22 ± 1.5
R&D-Agent o1-preview
48.18 ± 2.49
8.95 ± 2.36
18.67 ± 2.98
22.4 ± 1.1
AIDE o1-preview
34.3 ± 2.4
8.8 ± 1.1
10.0 ± 1.9
16.9 ± 1.1
Notes:
O3(R)+GPT-4.1(D)
: This version is designed to both reduce average time per loop and leverage a cost-effective combination of backend LLMs by seamlessly integrating Research Agent (o3) with Development Agent (GPT-4.1).
AIDE o1-preview
: Represents the previously best public result on MLE-bench as reported in the original MLE-bench paper.
Average and standard deviation results for R&D-Agent o1-preview is based on a independent of 5 seeds and for R&D-Agent o3(R)+GPT-4.1(D) is based on 6 seeds.
According to MLE-Bench, the 75 competitions are categorized into three levels of complexity:
Low==Lite
if we estimate that an experienced ML engineer can produce a sensible solution in under 2 hours, excluding the time taken to train any models;
Medium
if it takes between 2 and 10 hours; and
High
if it takes more than 10 hours.
You can inspect the detailed runs of the above results online.
R&D-Agent o1-preview detailed runs
R&D-Agent o3(R)+GPT-4.1(D) detailed runs
For running R&D-Agent on MLE-bench, refer to
MLE-bench Guide: Running ML Engineering via MLE-bench
🥇 The First Data-Centric Quant Multi-Agent Framework!
R&D-Agent for Quantitative Finance, in short
RD-Agent(Q)
, is the first data-centric, multi-agent framework designed to automate the full-stack research and development of quantitative strategies via coordinated factor-model co-optimization.
Extensive experiments in real stock markets show that, at a cost under $10, RD-Agent(Q) achieves approximately 2× higher ARR than benchmark factor libraries while using over 70% fewer factors. It also surpasses state-of-the-art deep time-series models under smaller resource budgets. Its alternating factor–model optimization further delivers excellent trade-off between predictive accuracy and strategy robustness.
You can learn more details about
RD-Agent(Q)
through the
paper
and reproduce it through the
documentation
.
Data Science Agent Preview
Check out our demo video showcasing the current progress of our Data Science Agent under development:
DS.Agent.Preview.mp4
🌟 Introduction
R&D-Agent aims to automate the most critical and valuable aspects of the industrial R&D process, and we begin with focusing on the data-driven scenarios to streamline the development of models and data.
Methodologically, we have identified a framework with two key components: 'R' for proposing new ideas and 'D' for implementing them.
We believe that the automatic evolution of R&D will lead to solutions of significant industrial value.
R&D is a very general scenario. The advent of R&D-Agent can be your
💰
Automatic Quant Factory
(
🎥Demo Video
|
▶️
YouTube
)
🤖
Data Mining Agent:
Iteratively proposing data & models (
🎥Demo Video 1
|
▶️
YouTube
) (
🎥Demo Video 2
|
▶️
YouTube
)  and implementing them by gaining knowledge from data.
🦾
Research Copilot:
Auto read research papers (
🎥Demo Video
|
▶️
YouTube
) / financial reports (
🎥Demo Video
|
▶️
YouTube
) and implement model structures or building datasets.
🤖
Kaggle Agent:
Auto Model Tuning and Feature Engineering(
🎥Demo Video Coming Soon...
) and implementing them to achieve more in competitions.
...
You can click the links above to view the demo. We're continuously adding more methods and scenarios to the project to enhance your R&D processes and boost productivity.
Additionally, you can take a closer look at the examples in our
🖥️ Live Demo
.
⚡ Quick start
RD-Agent currently only supports Linux.
You can try above demos by running the following command:
🐳 Docker installation.
Users must ensure Docker is installed before attempting most scenarios. Please refer to the
official 🐳Docker page
for installation instructions.
Ensure the current user can run Docker commands
without using sudo
. You can verify this by executing
docker run hello-world
.
🐍 Create a Conda Environment
Create a new conda environment with Python (3.10 and 3.11 are well-tested in our CI):
conda create -n rdagent python=3.10
Activate the environment:
conda activate rdagent
🛠️ Install the R&D-Agent
For Users
You can directly install the R&D-Agent package from PyPI:
pip install rdagent
For Developers
If you want to try the latest version or contribute to RD-Agent, you can install it from the source and follow the development setup:
git clone https://github.com/microsoft/RD-Agent
cd
RD-Agent
make dev
More details can be found in the
development setup
.
💊 Health check
rdagent provides a health check that currently checks two things.
whether the docker installation was successful.
whether the default port used by the
rdagent ui
is occupied.
rdagent health_check --no-check-env
⚙️ Configuration
The demos requires following ability:
ChatCompletion
json_mode
embedding query
You can set your Chat Model and Embedding Model in the following ways:
🔥 Attention
: We now provide experimental support for
DeepSeek
models! You can use DeepSeek's official API for cost-effective and high-performance inference. See the configuration example below for DeepSeek setup.
Using LiteLLM (Default)
: We now support LiteLLM as a backend for integration with multiple LLM providers. You can configure in multiple ways:
Option 1: Unified API base for both models
Configuration Example:
OpenAI
Setup :
cat
<<
EOF
> .env
# Set to any model supported by LiteLLM.
CHAT_MODEL=gpt-4o
EMBEDDING_MODEL=text-embedding-3-small
# Configure unified API base
OPENAI_API_BASE=<your_unified_api_base>
OPENAI_API_KEY=<replace_with_your_openai_api_key>
Configuration Example:
Azure OpenAI
Setup :
Before using this configuration, please confirm in advance that your
Azure OpenAI API key
supports
embedded models
.
cat
<<
EOF
> .env
EMBEDDING_MODEL=azure/<Model deployment supporting embedding>
CHAT_MODEL=azure/<your deployment name>
AZURE_API_KEY=<replace_with_your_openai_api_key>
AZURE_API_BASE=<your_unified_api_base>
AZURE_API_VERSION=<azure api version>
Option 2: Separate API bases for Chat and Embedding models
cat
<<
EOF
> .env
# Set to any model supported by LiteLLM.
# Configure separate API bases for chat and embedding
# CHAT MODEL:
CHAT_MODEL=gpt-4o
OPENAI_API_BASE=<your_chat_api_base>
OPENAI_API_KEY=<replace_with_your_openai_api_key>
# EMBEDDING MODEL:
# TAKE siliconflow as an example, you can use other providers.
# Note: embedding requires litellm_proxy prefix
EMBEDDING_MODEL=litellm_proxy/BAAI/bge-large-en-v1.5
LITELLM_PROXY_API_KEY=<replace_with_your_siliconflow_api_key>
LITELLM_PROXY_API_BASE=https://api.siliconflow.cn/v1
Configuration Example:
DeepSeek
Setup :
Since many users encounter configuration errors when setting up DeepSeek. Here's a complete working example for DeepSeek Setup:
cat
<<
EOF
> .env
# CHAT MODEL: Using DeepSeek Official API
CHAT_MODEL=deepseek/deepseek-chat
DEEPSEEK_API_KEY=<replace_with_your_deepseek_api_key>
# EMBEDDING MODEL: Using SiliconFlow for embedding since deepseek has no embedding model.
# Note: embedding requires litellm_proxy prefix
EMBEDDING_MODEL=litellm_proxy/BAAI/bge-m3
LITELLM_PROXY_API_KEY=<replace_with_your_siliconflow_api_key>
LITELLM_PROXY_API_BASE=https://api.siliconflow.cn/v1
Notice: If you are using reasoning models that include thought processes in their responses (such as <think> tags), you need to set the following environment variable:
REASONING_THINK_RM=True
You can also use a deprecated backend if you only use
OpenAI API
or
Azure OpenAI
directly. For this deprecated setting and more configuration information, please refer to the
documentation
.
If your environment configuration is complete, please execute the following commands to check if your configuration is valid. This step is necessary.
rdagent health_check
🚀 Run the Application
The
🖥️ Live Demo
is implemented by the following commands(each item represents one demo, you can select the one you prefer):
Run the
Automated Quantitative Trading & Iterative Factors Model Joint Evolution
:
Qlib
self-loop factor & model proposal and implementation application
rdagent fin_quant
Run the
Automated Quantitative Trading & Iterative Factors Evolution
:
Qlib
self-loop factor proposal and implementation application
rdagent fin_factor
Run the
Automated Quantitative Trading & Iterative Model Evolution
:
Qlib
self-loop model proposal and implementation application
rdagent fin_model
Run the
Automated Quantitative Trading & Factors Extraction from Financial Reports
:  Run the
Qlib
factor extraction and implementation application based on financial reports
#
1. Generally, you can run this scenario using the following command:
rdagent fin_factor_report --report-folder=
<
Your financial reports folder path
>
#
2. Specifically, you need to prepare some financial reports first. You can follow this concrete example:
wget https://github.com/SunsetWolf/rdagent_resource/releases/download/reports/all_reports.zip
unzip all_reports.zip -d git_ignore_folder/reports
rdagent fin_factor_report --report-folder=git_ignore_folder/reports
Run the
Automated Model Research & Development Copilot
: model extraction and implementation application
#
1. Generally, you can run your own papers/reports with the following command:
rdagent general_model
<
Your paper URL
>
#
2. Specifically, you can do it like this. For more details and additional paper examples, use `rdagent general_model -h`:
rdagent general_model
"
https://arxiv.org/pdf/2210.09789
"
Run the
Automated Medical Prediction Model Evolution
: Medical self-loop model proposal and implementation application
#
Generally, you can run the data science program with the following command:
rdagent data_science --competition
<
your competition name
>
#
Specifically, you need to create a folder for storing competition files (e.g., competition description file, competition datasets, etc.), and configure the path to the folder in your environment. In addition, you need to use chromedriver when you download the competition descriptors, which you can follow for this specific example:
#
1. Download the dataset, extract it to the target folder.
wget https://github.com/SunsetWolf/rdagent_resource/releases/download/ds_data/arf-12-hours-prediction-task.zip
unzip arf-12-hours-prediction-task.zip -d ./git_ignore_folder/ds_data/
#
2. Configure environment variables in the `.env` file
dotenv
set
DS_LOCAL_DATA_PATH
"
$(
pwd
)
/git_ignore_folder/ds_data
"
dotenv
set
DS_CODER_ON_WHOLE_PIPELINE True
dotenv
set
DS_IF_USING_MLE_DATA False
dotenv
set
DS_SAMPLE_DATA_BY_LLM False
dotenv
set
DS_SCEN rdagent.scenarios.data_science.scen.DataScienceScen
#
3. run the application
rdagent data_science --competition arf-12-hours-prediction-task
NOTE:
For more information about the dataset, please refer to the
documentation
.
Run the
Automated Kaggle Model Tuning & Feature Engineering
:  self-loop model proposal and feature engineering implementation application
Using
tabular-playground-series-dec-2021
as an example.
Register and login on the
Kaggle
website.
Configuring the Kaggle API.
(1) Click on the avatar (usually in the top right corner of the page) ->
Settings
->
Create New Token
, A file called
kaggle.json
will be downloaded.
(2) Move
kaggle.json
to
~/.config/kaggle/
(3) Modify the permissions of the kaggle.json file. Reference command:
chmod 600 ~/.config/kaggle/kaggle.json
Join the competition: Click
Join the competition
->
I Understand and Accept
at the bottom of the
competition details page
.
#
Generally, you can run the Kaggle competition program with the following command:
rdagent data_science --competition
<
your competition name
>
#
1. Configure environment variables in the `.env` file
mkdir -p ./git_ignore_folder/ds_data
dotenv
set
DS_LOCAL_DATA_PATH
"
$(
pwd
)
/git_ignore_folder/ds_data
"
dotenv
set
DS_CODER_ON_WHOLE_PIPELINE True
dotenv
set
DS_IF_USING_MLE_DATA True
dotenv
set
DS_SAMPLE_DATA_BY_LLM True
dotenv
set
DS_SCEN rdagent.scenarios.data_science.scen.KaggleScen
#
2. run the application
rdagent data_science --competition tabular-playground-series-dec-2021
🖥️ Monitor the Application Results
You can run the following command for our demo program to see the run logs.
rdagent ui --port 19899 --log-dir
<
your log folder like
"
log/
"
>
--data-science
About the
data_science
parameter: If you want to see the logs of the data science scenario, set the
data_science
parameter to
True
; otherwise set it to
False
.
Although port 19899 is not commonly used, but before you run this demo, you need to check if port 19899 is occupied. If it is, please change it to another port that is not occupied.
You can check if a port is occupied by running the following command.
rdagent health_check --no-check-env --no-check-docker
🏭 Scenarios
We have applied R&D-Agent to multiple valuable data-driven industrial scenarios.
🎯 Goal: Agent for Data-driven R&D
In this project, we are aiming to build an Agent to automate Data-Driven R&D that can
📄 Read real-world material (reports, papers, etc.) and
extract
key formulas, descriptions of interested
features
and
models
, which are the key components of data-driven R&D .
🛠️
Implement
the extracted formulas (e.g., features, factors, and models) in runnable codes.
Due to the limited ability of LLM in implementing at once, build an evolving process for the agent to improve performance by learning from feedback and knowledge.
💡 Propose
new ideas
based on current knowledge and observations.
📈 Scenarios/Demos
In the two key areas of data-driven scenarios, model implementation and data building, our system aims to serve two main roles: 🦾Copilot and 🤖Agent.
The 🦾Copilot follows human instructions to automate repetitive tasks.
The 🤖Agent, being more autonomous, actively proposes ideas for better results in the future.
The supported scenarios are listed below:
Scenario/Target
Model Implementation
Data Building
💹 Finance
🤖
Iteratively Proposing Ideas & Evolving
▶️
YouTube
🤖
Iteratively Proposing Ideas & Evolving
▶️
YouTube
🦾
Auto reports reading & implementation
▶️
YouTube
🩺 Medical
🤖
Iteratively Proposing Ideas & Evolving
▶️
YouTube
-
🏭 General
🦾
Auto paper reading & implementation
▶️
YouTube
🤖 Auto Kaggle Model Tuning
🤖Auto Kaggle feature Engineering
RoadMap
: Currently, we are working hard to add new features to the Kaggle scenario.
Different scenarios vary in entrance and configuration. Please check the detailed setup tutorial in the scenarios documents.
Here is a gallery of
successful explorations
(5 traces showed in
🖥️ Live Demo
). You can download and view the execution trace using
this command
from the documentation.
Please refer to
📖readthedocs_scen
for more details of the scenarios.
⚙️ Framework
Automating the R&D process in data science is a highly valuable yet underexplored area in industry. We propose a framework to push the boundaries of this important research field.
The research questions within this framework can be divided into three main categories:
Research Area
Paper/Work List
Benchmark the R&D abilities
Benchmark
Idea proposal:
Explore new ideas or refine existing ones
Research
Ability to realize ideas:
Implement and execute ideas
Development
We believe that the key to delivering high-quality solutions lies in the ability to evolve R&D capabilities. Agents should learn like human experts, continuously improving their R&D skills.
More documents can be found in the
📖 readthedocs
.
📃 Paper/Work list
Overall Technical Report
R&D-Agent: Automating Data-Driven AI Solution Building Through LLM-Powered Automated Research, Development, and Evolution
@misc
{
yang2024rdagent
,
title
=
{
R\&D-Agent: Automating Data-Driven AI Solution Building Through LLM-Powered Automated Research, Development, and Evolution
}
,
author
=
{
Xu Yang and Xiao Yang and Shikai Fang and Bowen Xian and Yuante Li and Jian Wang and Minrui Xu and Haoran Pan and Xinpeng Hong and Weiqing Liu and Yelong Shen and Weizhu Chen and Jiang Bian
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
2505.14738
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
https://arxiv.org/abs/2505.14738
}
}
📊 Benchmark
Towards Data-Centric Automatic R&D
@misc
{
chen2024datacentric
,
title
=
{
Towards Data-Centric Automatic R&D
}
,
author
=
{
Haotian Chen and Xinjie Shen and Zeqi Ye and Wenjun Feng and Haoxue Wang and Xiao Yang and Xu Yang and Weiqing Liu and Jiang Bian
}
,
year
=
{
2024
}
,
eprint
=
{
2404.11276
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
}
🔍 Research
In a data mining expert's daily research and development process, they propose a hypothesis (e.g., a model structure like RNN can capture patterns in time-series data), design experiments (e.g., finance data contains time-series and we can verify the hypothesis in this scenario), implement the experiment as code (e.g., Pytorch model structure), and then execute the code to get feedback (e.g., metrics, loss curve, etc.). The experts learn from the feedback and improve in the next iteration.
Based on the principles above, we have established a basic method framework that continuously proposes hypotheses, verifies them, and gets feedback from the real-world practice. This is the first scientific research automation framework that supports linking with real-world verification.
For more detail, please refer to our
🖥️ Live Demo page
.
🛠️ Development
Collaborative Evolving Strategy for Automatic Data-Centric Development
@misc
{
yang2024collaborative
,
title
=
{
Collaborative Evolving Strategy for Automatic Data-Centric Development
}
,
author
=
{
Xu Yang and Haotian Chen and Wenjun Feng and Haoxue Wang and Zeqi Ye and Xinjie Shen and Xiao Yang and Shizhao Sun and Weiqing Liu and Jiang Bian
}
,
year
=
{
2024
}
,
eprint
=
{
2407.18690
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
}
Deep Application in Diverse Scenarios
R&D-Agent-Quant: A Multi-Agent Framework for Data-Centric Factors and Model Joint Optimization
@misc
{
li2025rdagentquant
,
title
=
{
R\&D-Agent-Quant: A Multi-Agent Framework for Data-Centric Factors and Model Joint Optimization
}
,
author
=
{
Yuante Li and Xu Yang and Xiao Yang and Minrui Xu and Xisen Wang and Weiqing Liu and Jiang Bian
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
2505.15155
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
}
🤝 Contributing
We welcome contributions and suggestions to improve R&D-Agent. Please refer to the
Contributing Guide
for more details on how to contribute.
Before submitting a pull request, ensure that your code passes the automatic CI checks.
📝 Guidelines
This project welcomes contributions and suggestions.
Contributing to this project is straightforward and rewarding. Whether it's solving an issue, addressing a bug, enhancing documentation, or even correcting a typo, every contribution is valuable and helps improve R&D-Agent.
To get started, you can explore the issues list, or search for
TODO:
comments in the codebase by running the command
grep -r "TODO:"
.
Before we released R&D-Agent as an open-source project on GitHub, it was an internal project within our group. Unfortunately, the internal commit history was not preserved when we removed some confidential code. As a result, some contributions from our group members, including Haotian Chen, Wenjun Feng, Haoxue Wang, Zeqi Ye, Xinjie Shen, and Jinhui Li, were not included in the public commits.
⚖️ Legal disclaimer
The RD-agent is provided “as is”, without warranty of any kind, express or implied, including but not limited to the warranties of merchantability, fitness for a particular purpose and noninfringement. The RD-agent is aimed to facilitate research and development process in the financial industry and not ready-to-use for any financial investment or advice. Users shall independently assess and test the risks of the RD-agent in a specific use scenario, ensure the responsible use of AI technology, including but not limited to developing and integrating risk mitigation measures, and comply with all applicable laws and regulations in all applicable jurisdictions. The RD-agent does not provide financial opinions or reflect the opinions of Microsoft, nor is it designed to replace the role of qualified financial professionals in formulating, assessing, and approving finance products. The inputs and outputs of the RD-agent belong to the users and users shall assume all liability under any theory of liability, whether in contract, torts, regulatory, negligence, products liability, or otherwise, associated with use of the RD-agent and any inputs and outputs thereof.
- 今日の獲得スター数: 42
- 累積スター数: 8,357

### References
- https://github.com/microsoft/RD-Agent

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
- 今日の獲得スター数: 39
- 累積スター数: 4,437

### References
- https://github.com/JannisX11/blockbench

## fatedier/frp

### Executive Summary
- A fast reverse proxy to help you expose a local server behind a NAT or firewall to the internet.
- ---
- frp
README
|
中文文档
Sponsors
frp is an open source project with its ongoing development made possible entirely by the support of our awesome sponsors. If you'd like to join them, please consider
sponsoring frp's development
.
Gold Sponsors
Recall.ai - API for meeting recordings
If you're looking for a meeting recording API, consider checking out
Recall.ai
,
an API that records Zoom, Google Meet, Microsoft Teams, in-person meetings, and more.
Warp, built for collaborating with AI Agents
Available for macOS, Linux and Windows
The complete IDE crafted for professional Go developers
Secure and Elastic Infrastructure for Running Your AI-Generated Code
The sovereign cloud that puts you in control
An open source, self-hosted alternative to public clouds, built for data ownership and privacy
What is frp?
frp is a fast reverse proxy that allows you to expose a local server located behind a NAT or firewall to the Internet. It currently supports
TCP
and
UDP
, as well as
HTTP
and
HTTPS
protocols, enabling requests to be forwarded to internal services via domain name.
frp also offers a P2P connect mode.
Table of Contents
Development Status
About V2
Architecture
Example Usage
Access your computer in a LAN network via SSH
Multiple SSH services sharing the same port
Accessing Internal Web Services with Custom Domains in LAN
Forward DNS query requests
Forward Unix Domain Socket
Expose a simple HTTP file server
Enable HTTPS for a local HTTP(S) service
Expose your service privately
P2P Mode
Features
Configuration Files
Using Environment Variables
Split Configures Into Different Files
Server Dashboard
Client Admin UI
Monitor
Prometheus
Authenticating the Client
Token Authentication
OIDC Authentication
Encryption and Compression
TLS
Hot-Reloading frpc configuration
Get proxy status from client
Only allowing certain ports on the server
Port Reuse
Bandwidth Limit
For Each Proxy
TCP Stream Multiplexing
Support KCP Protocol
Support QUIC Protocol
Connection Pooling
Load balancing
Service Health Check
Rewriting the HTTP Host Header
Setting other HTTP Headers
Get Real IP
HTTP X-Forwarded-For
Proxy Protocol
Require HTTP Basic Auth (Password) for Web Services
Custom Subdomain Names
URL Routing
TCP Port Multiplexing
Connecting to frps via PROXY
Port range mapping
Client Plugins
Server Manage Plugins
SSH Tunnel Gateway
Virtual Network (VirtualNet)
Feature Gates
Available Feature Gates
Enabling Feature Gates
Feature Lifecycle
Related Projects
Contributing
Donation
GitHub Sponsors
PayPal
Development Status
frp is currently under development. You can try the latest release version in the
master
branch, or use the
dev
branch to access the version currently in development.
We are currently working on version 2 and attempting to perform some code refactoring and improvements. However, please note that it will not be compatible with version 1.
We will transition from version 0 to version 1 at the appropriate time and will only accept bug fixes and improvements, rather than big feature requests.
About V2
The complexity and difficulty of the v2 version are much higher than anticipated. I can only work on its development during fragmented time periods, and the constant interruptions disrupt productivity significantly. Given this situation, we will continue to optimize and iterate on the current version until we have more free time to proceed with the major version overhaul.
The concept behind v2 is based on my years of experience and reflection in the cloud-native domain, particularly in K8s and ServiceMesh. Its core is a modernized four-layer and seven-layer proxy, similar to envoy. This proxy itself is highly scalable, not only capable of implementing the functionality of intranet penetration but also applicable to various other domains. Building upon this highly scalable core, we aim to implement all the capabilities of frp v1 while also addressing the functionalities that were previously unachievable or difficult to implement in an elegant manner. Furthermore, we will maintain efficient development and iteration capabilities.
In addition, I envision frp itself becoming a highly extensible system and platform, similar to how we can provide a range of extension capabilities based on K8s. In K8s, we can customize development according to enterprise needs, utilizing features such as CRD, controller mode, webhook, CSI, and CNI. In frp v1, we introduced the concept of server plugins, which implemented some basic extensibility. However, it relies on a simple HTTP protocol and requires users to start independent processes and manage them on their own. This approach is far from flexible and convenient, and real-world demands vary greatly. It is unrealistic to expect a non-profit open-source project maintained by a few individuals to meet everyone's needs.
Finally, we acknowledge that the current design of modules such as configuration management, permission verification, certificate management, and API management is not modern enough. While we may carry out some optimizations in the v1 version, ensuring compatibility remains a challenging issue that requires a considerable amount of effort to address.
We sincerely appreciate your support for frp.
Architecture
Example Usage
To begin, download the latest program for your operating system and architecture from the
Release
page.
Next, place the
frps
binary and server configuration file on Server A, which has a public IP address.
Finally, place the
frpc
binary and client configuration file on Server B, which is located on a LAN that cannot be directly accessed from the public internet.
Some antiviruses improperly mark frpc as malware and delete it. This is due to frp being a networking tool capable of creating reverse proxies. Antiviruses sometimes flag reverse proxies due to their ability to bypass firewall port restrictions. If you are using antivirus, then you may need to whitelist/exclude frpc in your antivirus settings to avoid accidental quarantine/deletion. See
issue 3637
for more details.
Access your computer in a LAN network via SSH
Modify
frps.toml
on server A by setting the
bindPort
for frp clients to connect to:
#
frps.toml
bindPort
=
7000
Start
frps
on server A:
./frps -c ./frps.toml
Modify
frpc.toml
on server B and set the
serverAddr
field to the public IP address of your frps server:
#
frpc.toml
serverAddr
=
"
x.x.x.x
"
serverPort
=
7000
[[
proxies
]]
name
=
"
ssh
"
type
=
"
tcp
"
localIP
=
"
127.0.0.1
"
localPort
=
22
remotePort
=
6000
Note that the
localPort
(listened on the client) and
remotePort
(exposed on the server) are used for traffic going in and out of the frp system, while the
serverPort
is used for communication between frps and frpc.
Start
frpc
on server B:
./frpc -c ./frpc.toml
To access server B from another machine through server A via SSH (assuming the username is
test
), use the following command:
ssh -oPort=6000 test@x.x.x.x
Multiple SSH services sharing the same port
This example implements multiple SSH services exposed through the same port using a proxy of type tcpmux. Similarly, as long as the client supports the HTTP Connect proxy connection method, port reuse can be achieved in this way.
Deploy frps on a machine with a public IP and modify the frps.toml file. Here is a simplified configuration:
bindPort
=
7000
tcpmuxHTTPConnectPort
=
5002
Deploy frpc on the internal machine A with the following configuration:
serverAddr
=
"
x.x.x.x
"
serverPort
=
7000
[[
proxies
]]
name
=
"
ssh1
"
type
=
"
tcpmux
"
multiplexer
=
"
httpconnect
"
customDomains
= [
"
machine-a.example.com
"
]
localIP
=
"
127.0.0.1
"
localPort
=
22
Deploy another frpc on the internal machine B with the following configuration:
serverAddr
=
"
x.x.x.x
"
serverPort
=
7000
[[
proxies
]]
name
=
"
ssh2
"
type
=
"
tcpmux
"
multiplexer
=
"
httpconnect
"
customDomains
= [
"
machine-b.example.com
"
]
localIP
=
"
127.0.0.1
"
localPort
=
22
To access internal machine A using SSH ProxyCommand, assuming the username is "test":
ssh -o 'proxycommand socat - PROXY:x.x.x.x:%h:%p,proxyport=5002' test@machine-a.example.com
To access internal machine B, the only difference is the domain name, assuming the username is "test":
ssh -o 'proxycommand socat - PROXY:x.x.x.x:%h:%p,proxyport=5002' test@machine-b.example.com
Accessing Internal Web Services with Custom Domains in LAN
Sometimes we need to expose a local web service behind a NAT network to others for testing purposes with our own domain name.
Unfortunately, we cannot resolve a domain name to a local IP. However, we can use frp to expose an HTTP(S) service.
Modify
frps.toml
and set the HTTP port for vhost to 8080:
#
frps.toml
bindPort
=
7000
vhostHTTPPort
=
8080
If you want to configure an https proxy, you need to set up the
vhostHTTPSPort
.
Start
frps
:
./frps -c ./frps.toml
Modify
frpc.toml
and set
serverAddr
to the IP address of the remote frps server. Specify the
localPort
of your web service:
#
frpc.toml
serverAddr
=
"
x.x.x.x
"
serverPort
=
7000
[[
proxies
]]
name
=
"
web
"
type
=
"
http
"
localPort
=
80
customDomains
= [
"
www.example.com
"
]
Start
frpc
:
./frpc -c ./frpc.toml
Map the A record of
www.example.com
to either the public IP of the remote frps server or a CNAME record pointing to your original domain.
Visit your local web service using url
http://www.example.com:8080
.
Forward DNS query requests
Modify
frps.toml
:
#
frps.toml
bindPort
=
7000
Start
frps
:
./frps -c ./frps.toml
Modify
frpc.toml
and set
serverAddr
to the IP address of the remote frps server. Forward DNS query requests to the Google Public DNS server
8.8.8.8:53
:
#
frpc.toml
serverAddr
=
"
x.x.x.x
"
serverPort
=
7000
[[
proxies
]]
name
=
"
dns
"
type
=
"
udp
"
localIP
=
"
8.8.8.8
"
localPort
=
53
remotePort
=
6000
Start frpc:
./frpc -c ./frpc.toml
Test DNS resolution using the
dig
command:
dig @x.x.x.x -p 6000 www.google.com
Forward Unix Domain Socket
Expose a Unix domain socket (e.g. the Docker daemon socket) as TCP.
Configure
frps
as above.
Start
frpc
with the following configuration:
#
frpc.toml
serverAddr
=
"
x.x.x.x
"
serverPort
=
7000
[[
proxies
]]
name
=
"
unix_domain_socket
"
type
=
"
tcp
"
remotePort
=
6000
[
proxies
.
plugin
]
type
=
"
unix_domain_socket
"
unixPath
=
"
/var/run/docker.sock
"
Test the configuration by getting the docker version using
curl
:
curl http://x.x.x.x:6000/version
Expose a simple HTTP file server
Expose a simple HTTP file server to access files stored in the LAN from the public Internet.
Configure
frps
as described above, then:
Start
frpc
with the following configuration:
#
frpc.toml
serverAddr
=
"
x.x.x.x
"
serverPort
=
7000
[[
proxies
]]
name
=
"
test_static_file
"
type
=
"
tcp
"
remotePort
=
6000
[
proxies
.
plugin
]
type
=
"
static_file
"
localPath
=
"
/tmp/files
"
stripPrefix
=
"
static
"
httpUser
=
"
abc
"
httpPassword
=
"
abc
"
Visit
http://x.x.x.x:6000/static/
from your browser and specify correct username and password to view files in
/tmp/files
on the
frpc
machine.
Enable HTTPS for a local HTTP(S) service
You may substitute
https2https
for the plugin, and point the
localAddr
to a HTTPS endpoint.
Start
frpc
with the following configuration:
#
frpc.toml
serverAddr
=
"
x.x.x.x
"
serverPort
=
7000
[[
proxies
]]
name
=
"
test_https2http
"
type
=
"
https
"
customDomains
= [
"
test.example.com
"
]

[
proxies
.
plugin
]
type
=
"
https2http
"
localAddr
=
"
127.0.0.1:80
"
crtPath
=
"
./server.crt
"
keyPath
=
"
./server.key
"
hostHeaderRewrite
=
"
127.0.0.1
"
requestHeaders.set.x-from-where
=
"
frp
"
Visit
https://test.example.com
.
Expose your service privately
To mitigate risks associated with exposing certain services directly to the public network, STCP (Secret TCP) mode requires a preshared key to be used for access to the service from other clients.
Configure
frps
same as above.
Start
frpc
on machine B with the following config. This example is for exposing the SSH service (port 22), and note the
secretKey
field for the preshared key, and that the
remotePort
field is removed here:
#
frpc.toml
serverAddr
=
"
x.x.x.x
"
serverPort
=
7000
[[
proxies
]]
name
=
"
secret_ssh
"
type
=
"
stcp
"
secretKey
=
"
abcdefg
"
localIP
=
"
127.0.0.1
"
localPort
=
22
Start another
frpc
(typically on another machine C) with the following config to access the SSH service with a security key (
secretKey
field):
#
frpc.toml
serverAddr
=
"
x.x.x.x
"
serverPort
=
7000
[[
visitors
]]
name
=
"
secret_ssh_visitor
"
type
=
"
stcp
"
serverName
=
"
secret_ssh
"
secretKey
=
"
abcdefg
"
bindAddr
=
"
127.0.0.1
"
bindPort
=
6000
On machine C, connect to SSH on machine B, using this command:
ssh -oPort=6000 127.0.0.1
P2P Mode
xtcp
is designed to transmit large amounts of data directly between clients. A frps server is still needed, as P2P here only refers to the actual data transmission.
Note that it may not work with all types of NAT devices. You might want to fallback to stcp if xtcp doesn't work.
Start
frpc
on machine B, and expose the SSH port. Note that the
remotePort
field is removed:
#
frpc.toml
serverAddr
=
"
x.x.x.x
"
serverPort
=
7000
#
set up a new stun server if the default one is not available.
#
natHoleStunServer = "xxx"
[[
proxies
]]
name
=
"
p2p_ssh
"
type
=
"
xtcp
"
secretKey
=
"
abcdefg
"
localIP
=
"
127.0.0.1
"
localPort
=
22
Start another
frpc
(typically on another machine C) with the configuration to connect to SSH using P2P mode:
#
frpc.toml
serverAddr
=
"
x.x.x.x
"
serverPort
=
7000
#
set up a new stun server if the default one is not available.
#
natHoleStunServer = "xxx"
[[
visitors
]]
name
=
"
p2p_ssh_visitor
"
type
=
"
xtcp
"
serverName
=
"
p2p_ssh
"
secretKey
=
"
abcdefg
"
bindAddr
=
"
127.0.0.1
"
bindPort
=
6000
#
when automatic tunnel persistence is required, set it to true
keepTunnelOpen
=
false
On machine C, connect to SSH on machine B, using this command:
ssh -oPort=6000 127.0.0.1
Features
Configuration Files
Since v0.52.0, we support TOML, YAML, and JSON for configuration. Please note that INI is deprecated and will be removed in future releases. New features will only be available in TOML, YAML, or JSON. Users wanting these new features should switch their configuration format accordingly.
Read the full example configuration files to find out even more features not described here.
Examples use TOML format, but you can still use YAML or JSON.
These configuration files is for reference only. Please do not use this configuration directly to run the program as it may have various issues.
Full configuration file for frps (Server)
Full configuration file for frpc (Client)
Using Environment Variables
Environment variables can be referenced in the configuration file, using Go's standard format:
#
frpc.toml
serverAddr
=
"
{{ .Envs.FRP_SERVER_ADDR }}
"
serverPort
=
7000
[[
proxies
]]
name
=
"
ssh
"
type
=
"
tcp
"
localIP
=
"
127.0.0.1
"
localPort
=
22
remotePort
= {{ .Envs.FRP_SSH_REMOTE_PORT }
}
With the config above, variables can be passed into
frpc
program like this:
export FRP_SERVER_ADDR=x.x.x.x
export FRP_SSH_REMOTE_PORT=6000
./frpc -c ./frpc.toml
frpc
will render configuration file template using OS environment variables. Remember to prefix your reference with
.Envs
.
Split Configures Into Different Files
You can split multiple proxy configs into different files and include them in the main file.
#
frpc.toml
serverAddr
=
"
x.x.x.x
"
serverPort
=
7000
includes
= [
"
./confd/*.toml
"
]
#
./confd/test.toml
[[
proxies
]]
name
=
"
ssh
"
type
=
"
tcp
"
localIP
=
"
127.0.0.1
"
localPort
=
22
remotePort
=
6000
Server Dashboard
Check frp's status and proxies' statistics information by Dashboard.
Configure a port for dashboard to enable this feature:
#
The default value is 127.0.0.1. Change it to 0.0.0.0 when you want to access it from a public network.
webServer.addr
=
"
0.0.0.0
"
webServer.port
=
7500
#
dashboard's username and password are both optional
webServer.user
=
"
admin
"
webServer.password
=
"
admin
"
Then visit
http://[serverAddr]:7500
to see the dashboard, with username and password both being
admin
.
Additionally, you can use HTTPS port by using your domains wildcard or normal SSL certificate:
webServer.port
=
7500
#
dashboard's username and password are both optional
webServer.user
=
"
admin
"
webServer.password
=
"
admin
"
webServer.tls.certFile
=
"
server.crt
"
webServer.tls.keyFile
=
"
server.key
"
Then visit
https://[serverAddr]:7500
to see the dashboard in secure HTTPS connection, with username and password both being
admin
.
Client Admin UI
The Client Admin UI helps you check and manage frpc's configuration.
Configure an address for admin UI to enable this feature:
webServer.addr
=
"
127.0.0.1
"
webServer.port
=
7400
webServer.user
=
"
admin
"
webServer.password
=
"
admin
"
Then visit
http://127.0.0.1:7400
to see admin UI, with username and password both being
admin
.
Monitor
When web server is enabled, frps will save monitor data in cache for 7 days. It will be cleared after process restart.
Prometheus is also supported.
Prometheus
Enable dashboard first, then configure
enablePrometheus = true
in
frps.toml
.
http://{dashboard_addr}/metrics
will provide prometheus monitor data.
Authenticating the Client
There are 2 authentication methods to authenticate frpc with frps.
You can decide which one to use by configuring
auth.method
in
frpc.toml
and
frps.toml
, the default one is token.
Configuring
auth.additionalScopes = ["HeartBeats"]
will use the configured authentication method to add and validate authentication on every heartbeat between frpc and frps.
Configuring
auth.additionalScopes = ["NewWorkConns"]
will do the same for every new work connection between frpc and frps.
Token Authentication
When specifying
auth.method = "token"
in
frpc.toml
and
frps.toml
- token based authentication will be used.
Make sure to specify the same
auth.token
in
frps.toml
and
frpc.toml
for frpc to pass frps validation
Token Source
frp supports reading authentication tokens from external sources using the
tokenSource
configuration. Currently, file-based token source is supported.
File-based token source:
#
frpc.toml
auth.method
=
"
token
"
auth.tokenSource.type
=
"
file
"
auth.tokenSource.file.path
=
"
/path/to/token/file
"
The token will be read from the specified file at startup. This is useful for scenarios where tokens are managed by external systems or need to be kept separate from configuration files for security reasons.
OIDC Authentication
When specifying
auth.method = "oidc"
in
frpc.toml
and
frps.toml
- OIDC based authentication will be used.
OIDC stands for OpenID Connect, and the flow used is called
Client Credentials Grant
.
To use this authentication type - configure
frpc.toml
and
frps.toml
as follows:
#
frps.toml
auth.method
=
"
oidc
"
auth.oidc.issuer
=
"
https://example-oidc-issuer.com/
"
auth.oidc.audience
=
"
https://oidc-audience.com/.default
"
#
frpc.toml
auth.method
=
"
oidc
"
auth.oidc.clientID
=
"
98692467-37de-409a-9fac-bb2585826f18
"
#
Replace with OIDC client ID
auth.oidc.clientSecret
=
"
oidc_secret
"
auth.oidc.audience
=
"
https://oidc-audience.com/.default
"
auth.oidc.tokenEndpointURL
=
"
https://example-oidc-endpoint.com/oauth2/v2.0/token
"
Encryption and Compression
The features are off by default. You can turn on encryption and/or compression:
#
frpc.toml
[[
proxies
]]
name
=
"
ssh
"
type
=
"
tcp
"
localPort
=
22
remotePort
=
6000
transport.useEncryption
=
true
transport.useCompression
=
true
TLS
Since v0.50.0, the default value of
transport.tls.enable
and
transport.tls.disableCustomTLSFirstByte
has been changed to true, and tls is enabled by default.
For port multiplexing, frp sends a first byte
0x17
to dial a TLS connection. This only takes effect when you set
transport.tls.disableCustomTLSFirstByte
to false.
To
enforce
frps
to only accept TLS connections - configure
transport.tls.force = true
in
frps.toml
.
This is optional.
frpc
TLS settings:
transport.tls.enable
=
true
transport.tls.certFile
=
"
certificate.crt
"
transport.tls.keyFile
=
"
certificate.key
"
transport.tls.trustedCaFile
=
"
ca.crt
"
frps
TLS settings:
transport.tls.force
=
true
transport.tls.certFile
=
"
certificate.crt
"
transport.tls.keyFile
=
"
certificate.key
"
transport.tls.trustedCaFile
=
"
ca.crt
"
You will need
a root CA cert
and
at least one SSL/TLS certificate
. It
can
be self-signed or regular (such as Let's Encrypt or another SSL/TLS certificate provider).
If you using
frp
via IP address and not hostname, make sure to set the appropriate IP address in the Subject Alternative Name (SAN) area when generating SSL/TLS Certificates.
Given an example:
Prepare openssl config file. It exists at
/etc/pki/tls/openssl.cnf
in Linux System and
/System/Library/OpenSSL/openssl.cnf
in MacOS, and you can copy it to current path, like
cp /etc/pki/tls/openssl.cnf ./my-openssl.cnf
. If not, you can build it by yourself, like:
cat > my-openssl.cnf << EOF
[ ca ]
default_ca = CA_default
[ CA_default ]
x509_extensions = usr_cert
[ req ]
default_bits        = 2048
default_md          = sha256
default_keyfile     = privkey.pem
distinguished_name  = req_distinguished_name
attributes          = req_attributes
x509_extensions     = v3_ca
string_mask         = utf8only
[ req_distinguished_name ]
[ req_attributes ]
[ usr_cert ]
basicConstraints       = CA:FALSE
nsComment              = "OpenSSL Generated Certificate"
subjectKeyIdentifier   = hash
authorityKeyIdentifier = keyid,issuer
[ v3_ca ]
subjectKeyIdentifier   = hash
authorityKeyIdentifier = keyid:always,issuer
basicConstraints       = CA:true
EOF
build ca certificates:
openssl genrsa -out ca.key 2048
openssl req -x509 -new -nodes -key ca.key -subj "/CN=example.ca.com" -days 5000 -out ca.crt
build frps certificates:
openssl genrsa -out server.key 2048

openssl req -new -sha256 -key server.key \
    -subj "/C=XX/ST=DEFAULT/L=DEFAULT/O=DEFAULT/CN=server.com" \
    -reqexts SAN \
    -config <(cat my-openssl.cnf <(printf "\n[SAN]\nsubjectAltName=DNS:localhost,IP:127.0.0.1,DNS:example.server.com")) \
    -out server.csr

openssl x509 -req -days 365 -sha256 \
	-in server.csr -CA ca.crt -CAkey ca.key -CAcreateserial \
	-extfile <(printf "subjectAltName=DNS:localhost,IP:127.0.0.1,DNS:example.server.com") \
	-out server.crt
build frpc certificates：
openssl genrsa -out client.key 2048
openssl req -new -sha256 -key client.key \
    -subj "/C=XX/ST=DEFAULT/L=DEFAULT/O=DEFAULT/CN=client.com" \
    -reqexts SAN \
    -config <(cat my-openssl.cnf <(printf "\n[SAN]\nsubjectAltName=DNS:client.com,DNS:example.client.com")) \
    -out client.csr

openssl x509 -req -days 365 -sha256 \
    -in client.csr -CA ca.crt -CAkey ca.key -CAcreateserial \
	-extfile <(printf "subjectAltName=DNS:client.com,DNS:example.client.com") \
	-out client.crt
Hot-Reloading frpc configuration
The
webServer
fields are required for enabling HTTP API:
#
frpc.toml
webServer.addr
=
"
127.0.0.1
"
webServer.port
=
7400
Then run command
frpc reload -c ./frpc.toml
and wait for about 10 seconds to let
frpc
create or update or remove proxies.
Note that global client parameters won't be modified except 'start'.
You can run command
frpc verify -c ./frpc.toml
before reloading to check if there are config errors.
Get proxy status from client
Use
frpc status -c ./frpc.toml
to get status of all proxies. The
webServer
fields are required for enabling HTTP API.
Only allowing certain ports on the server
allowPorts
in
frps.toml
is used to avoid abuse of ports:
#
frps.toml
allowPorts
= [
  {
start
=
2000
,
end
=
3000
},
  {
single
=
3001
},
  {
single
=
3003
},
  {
start
=
4000
,
end
=
50000
}
]
Port Reuse
vhostHTTPPort
and
vhostHTTPSPort
in frps can use same port with
bindPort
. frps will detect the connection's protocol and handle it correspondingly.
What you need to pay attention to is that if you want to configure
vhostHTTPSPort
and
bindPort
to the same port, you need to first set
transport.tls.disableCustomTLSFirstByte
to false.
We would like to try to allow multiple proxies bind a same remote port with different protocols in the future.
Bandwidth Limit
For Each Proxy
#
frpc.toml
[[
proxies
]]
name
=
"
ssh
"
type
=
"
tcp
"
localPort
=
22
remotePort
=
6000
transport.bandwidthLimit
=
"
1MB
"
Set
transport.bandwidthLimit
in each proxy's configure to enable this feature. Supported units are
MB
and
KB
.
Set
transport.bandwidthLimitMode
to
client
or
server
to limit bandwidth on the client or server side. Default is
client
.
TCP Stream Multiplexing
frp supports tcp stream multiplexing since v0.10.0 like HTTP2 Multiplexing, in which case all logic connections to the same frpc are multiplexed into the same TCP connection.
You can disable this feature by modify
frps.toml
and
frpc.toml
:
#
frps.toml and frpc.toml, must be same
transport.tcpMux
=
false
Support KCP Protocol
KCP is a fast and reliable protocol that can achieve the transmission effect of a reduction of the average latency by 30% to 40% and reduction of the maximum delay by a factor of three, at the cost of 10% to 20% more bandwidth wasted than TCP.
KCP mode uses UDP as the underlying transport. Using KCP in frp:
Enable KCP in frps:
#
frps.toml
bindPort
=
7000
#
Specify a UDP port for KCP.
kcpBindPort
=
7000
The
kcpBindPort
number can be the same number as
bindPort
, since
bindPort
field specifies a TCP port.
Configure
frpc.toml
to use KCP to connect to frps:
#
frpc.toml
serverAddr
=
"
x.x.x.x
"
#
Same as the 'kcpBindPort' in frps.toml
serverPort
=
7000
transport.protocol
=
"
kcp
"
Support QUIC Protocol
QUIC is a new multiplexed transport built on top of UDP.
Using QUIC in frp:
Enable QUIC in frps:
#
frps.toml
bindPort
=
7000
#
Specify a UDP port for QUIC.
quicBindPort
=
7000
The
quicBindPort
number can be the same number as
bindPort
, since
bindPort
field specifies a TCP port.
Configure
frpc.toml
to use QUIC to connect to frps:
#
frpc.toml
serverAddr
=
"
x.x.x.x
"
#
Same as the 'quicBindPort' in frps.toml
serverPort
=
7000
transport.protocol
=
"
quic
"
Connection Pooling
By default, frps creates a new frpc connection to the backend service upon a user request. With connection pooling, frps keeps a certain number of pre-established connections, reducing the time needed to establish a connection.
This feature is suitable for a large number of short connections.
Configure the limit of pool count each proxy can use in
frps.toml
:
#
frps.toml
transport.maxPoolCount
=
5
Enable and specify the number of connection pool:
#
frpc.toml
transport.poolCount
=
1
Load balancing
Load balancing is supported by
group
.
This feature is only available for types
tcp
,
http
,
tcpmux
now.
#
frpc.toml
[[
proxies
]]
name
=
"
test1
"
type
=
"
tcp
"
localPort
=
8080
remotePort
=
80
loadBalancer.group
=
"
web
"
loadBalancer.groupKey
=
"
123
"
[[
proxies
]]
name
=
"
test2
"
type
=
"
tcp
"
localPort
=
8081
remotePort
=
80
loadBalancer.group
=
"
web
"
loadBalancer.groupKey
=
"
123
"
loadBalancer.groupKey
is used for authentication.
Connections to port 80 will be dispatched to proxies in the same group randomly.
For type
tcp
,
remotePort
in the same group should be the same.
For type
http
,
customDomains
,
subdomain
,
locations
should be the same.
Service Health Check
Health check feature can help you achieve high availability with load balancing.
Add
healthCheck.type = "tcp"
or
healthCheck.type = "http"
to enable health check.
With health check type
tcp
, the service port will be pinged (TCPing):
#
frpc.toml
[[
proxies
]]
name
=
"
test1
"
type
=
"
tcp
"
localPort
=
22
remotePort
=
6000
#
Enable TCP health check
healthCheck.type
=
"
tcp
"
#
TCPing timeout seconds
healthCheck.timeoutSeconds
=
3
#
If health check failed 3 times in a row, the proxy will be removed from frps
healthCheck.maxFailed
=
3
#
A health check every 10 seconds
healthCheck.intervalSeconds
=
10
With health check type
http
, an HTTP request will be sent to the service and an HTTP 2xx OK response is expected:
#
frpc.toml
[[
proxies
]]
name
=
"
web
"
type
=
"
http
"
localIP
=
"
127.0.0.1
"
localPort
=
80
customDomains
= [
"
test.example.com
"
]
#
Enable HTTP health check
healthCheck.type
=
"
http
"
#
frpc will send a GET request to '/status'
#
and expect an HTTP 2xx OK response
healthCheck.path
=
"
/status
"
healthCheck.timeoutSeconds
=
3
healthCheck.maxFailed
=
3
healthCheck.intervalSeconds
=
10
Rewriting the HTTP Host Header
By default frp does not modify the tunneled HTTP requests at all as it's a byte-for-byte copy.
However, speaking of web servers and HTTP requests, your web server might rely on the
Host
HTTP header to determine the website to be accessed. frp can rewrite the
Host
header when forwarding the HTTP requests, with the
hostHeaderRewrite
field:
#
frpc.toml
[[
proxies
]]
name
=
"
web
"
type
=
"
http
"
localPort
=
80
customDomains
= [
"
test.example.com
"
]
hostHeaderRewrite
=
"
dev.example.com
"
The HTTP request will have the
Host
header rewritten to
Host: dev.example.com
when it reaches the actual web server, although the request from the browser probably has
Host: test.example.com
.
Setting other HTTP Headers
Similar to
Host
, You can override other HTTP request and response headers with proxy type
http
.
#
frpc.toml
[[
proxies
]]
name
=
"
web
"
type
=
"
http
"
localPort
=
80
customDomains
= [
"
test.example.com
"
]
hostHeaderRewrite
=
"
dev.example.com
"
requestHeaders.set.x-from-where
=
"
frp
"
responseHeaders.set.foo
=
"
bar
"
In this example, it will set header
x-from-where: frp
in the HTTP request and
foo: bar
in the HTTP response.
Get Real IP
HTTP X-Forwarded-For
This feature is for
http
proxies or proxies with the
https2http
and
https2https
plugins enabled.
You can get user's real IP from HTTP request headers
X-Forwarded-For
.
Proxy Protocol
frp supports Proxy Protocol to send user's real IP to local services.
Here is an example for https service:
#
frpc.toml
[[
proxies
]]
name
=
"
web
"
type
=
"
https
"
localPort
=
443
customDomains
= [
"
test.example.com
"
]
#
now v1 and v2 are supported
transport.proxyProtocolVersion
=
"
v2
"
You can enable Proxy Protocol support in nginx to expose user's real IP in HTTP header
X-Real-IP
, and then read
X-Real-IP
header in your web service for the real IP.
Require HTTP Basic Auth (Password) for Web Services
Anyone who can guess your tunnel URL can access your local web server unless you protect it with a password.
This enforces HTTP Basic Auth on all requests with the username and password specified in frpc's configure file.
It can only be enabled when proxy type is http.
#
frpc.toml
[[
proxies
]]
name
=
"
web
"
type
=
"
http
"
localPort
=
80
customDomains
= [
"
test.example.com
"
]
httpUser
=
"
abc
"
httpPassword
=
"
abc
"
Visit
http://test.example.com
in the browser and now you are prompted to enter the username and password.
Custom Subdomain Names
It is convenient to use
subdomain
configure for http and https types when many people share one frps server.
#
frps.toml
subDomainHost
=
"
frps.com
"
Resolve
*.frps.com
to the frps server's IP. This is usually called a Wildcard DNS record.
#
frpc.toml
[[
proxies
]]
name
=
"
web
"
type
=
"
http
"
localPort
=
80
subdomain
=
"
test
"
Now you can visit your web service on
test.frps.com
.
Note that if
subdomainHost
is not empty,
customDomains
should not be the subdomain of
subdomainHost
.
URL Routing
frp supports forwarding HTTP requests to different backend web services by url routing.
locations
specifies the prefix of URL used for routing. frps first searches for the most specific prefix location given by literal strings regardless of the listed order.
#
frpc.toml
[[
proxies
]]
name
=
"
web01
"
type
=
"
http
"
localPort
=
80
customDomains
= [
"
web.example.com
"
]
locations
= [
"
/
"
]

[[
proxies
]]
name
=
"
web02
"
type
=
"
http
"
localPort
=
81
customDomains
= [
"
web.example.com
"
]
locations
= [
"
/news
"
,
"
/about
"
]
HTTP requests with URL prefix
/news
or
/about
will be forwarded to
web02
and other requests to
web01
.
TCP Port Multiplexing
frp supports receiving TCP sockets directed to different proxies on a single port on frps, similar to
vhostHTTPPort
and
vhostHTTPSPort
.
The only supported TCP port multiplexing method available at the moment is
httpconnect
- HTTP CONNECT tunnel.
When setting
tcpmuxHTTPConnectPort
to anything other than 0 in frps, frps will listen on this port for HTTP CONNECT requests.
The host of the HTTP CONNECT request will be used to match the proxy in frps. Proxy hosts can be configured in frpc by configuring
customDomains
and / or
subdomain
under
tcpmux
proxies, when
multiplexer = "httpconnect"
.
For example:
#
frps.toml
bindPort
=
7000
tcpmuxHTTPConnectPort
=
1337
#
frpc.toml
serverAddr
=
"
x.x.x.x
"
serverPort
=
7000
[[
proxies
]]
name
=
"
proxy1
"
type
=
"
tcpmux
"
multiplexer
=
"
httpconnect
"
customDomains
= [
"
test1
"
]
localPort
=
80
[[
proxies
]]
name
=
"
proxy2
"
type
=
"
tcpmux
"
multiplexer
=
"
httpconnect
"
customDomains
= [
"
test2
"
]
localPort
=
8080
In the above configuration - frps can be contacted on port 1337 with a HTTP CONNECT header such as:
CONNECT test1 HTTP/1.1\r\n\r\n
and the connection will be routed to
proxy1
.
Connecting to frps via PROXY
frpc can connect to frps through proxy if you set OS environment variable
HTTP_PROXY
, or if
transport.proxyURL
is set in frpc.toml file.
It only works when protocol is tcp.
#
frpc.toml
serverAddr
=
"
x.x.x.x
"
serverPort
=
7000
transport.proxyURL
=
"
http://user:pwd@192.168.1.128:8080
"
Port range mapping
Added in v0.56.0
We can use the range syntax of Go template combined with the built-in
parseNumberRangePair
function to achieve port range mapping.
The following example, when run, will create 8 proxies named
test-6000, test-6001 ... test-6007
, each mapping the remote port to the local port.
{{- range $_, $v := parseNumberRangePair "6000-6006,6007" "6000-6006,6007" }}
[[proxies]]
name = "tcp-{{ $v.First }}"
type = "tcp"
localPort = {{ $v.First }}
remotePort = {{ $v.Second }}
{{- end }}
Client Plugins
frpc only forwards requests to local TCP or UDP ports by default.
Plugins are used for providing rich features. There are built-in plugins such as
unix_domain_socket
,
http_proxy
,
socks5
,
static_file
,
http2https
,
https2http
,
https2https
and you can see
example usage
.
Using plugin
http_proxy
:
#
frpc.toml
[[
proxies
]]
name
=
"
http_proxy
"
type
=
"
tcp
"
remotePort
=
6000
[
proxies
.
plugin
]
type
=
"
http_proxy
"
httpUser
=
"
abc
"
httpPassword
=
"
abc
"
httpUser
and
httpPassword
are configuration parameters used in
http_proxy
plugin.
Server Manage Plugins
Read the
document
.
Find more plugins in
gofrp/plugin
.
SSH Tunnel Gateway
added in v0.53.0
frp supports listening to an SSH port on the frps side and achieves TCP protocol proxying through the SSH -R protocol, without relying on frpc.
#
frps.toml
sshTunnelGateway.bindPort
=
2200
When running
./frps -c frps.toml
, a private key file named
.autogen_ssh_key
will be automatically created in the current working directory. This generated private key file will be used by the SSH server in frps.
Executing the command
ssh -R :80:127.0.0.1:8080 v0@{frp address} -p 2200 tcp --proxy_name
"
test-tcp
"
--remote_port 9090
sets up a proxy on frps that forwards the local 8080 service to the port 9090.
frp (via SSH) (Ctrl+C to quit)

User:
ProxyName: test-tcp
Type: tcp
RemoteAddress: :9090
This is equivalent to:
frpc tcp --proxy_name
"
test-tcp
"
--local_ip 127.0.0.1 --local_port 8080 --remote_port 9090
Please refer to this
document
for more information.
Virtual Network (VirtualNet)
Alpha feature added in v0.62.0
The VirtualNet feature enables frp to create and manage virtual network connections between clients and visitors through a TUN interface. This allows for IP-level routing between machines, extending frp beyond simple port forwarding to support full network connectivity.
For detailed information about configuration and usage, please refer to the
VirtualNet documentation
.
Feature Gates
frp supports feature gates to enable or disable experimental features. This allows users to try out new features before they're considered stable.
Available Feature Gates
Name
Stage
Default
Description
VirtualNet
ALPHA
false
Virtual network capabilities for frp
Enabling Feature Gates
To enable an experimental feature, add the feature gate to your configuration:
featureGates
= {
VirtualNet
=
true
}
Feature Lifecycle
Features typically go through three stages:
ALPHA
: Disabled by default, may be unstable
BETA
: May be enabled by default, more stable but still evolving
GA (Generally Available)
: Enabled by default, ready for production use
Related Projects
gofrp/plugin
- A repository for frp plugins that contains a variety of plugins implemented based on the frp extension mechanism, meeting the customization needs of different scenarios.
gofrp/tiny-frpc
- A lightweight version of the frp client (around 3.5MB at minimum) implemented using the ssh protocol, supporting some of the most commonly used features, suitable for devices with limited resources.
Contributing
Interested in getting involved? We would like to help you!
Take a look at our
issues list
and consider sending a Pull Request to
dev branch
.
If you want to add a new feature, please create an issue first to describe the new feature, as well as the implementation approach. Once a proposal is accepted, create an implementation of the new features and submit it as a pull request.
Sorry for my poor English. Improvements for this document are welcome, even some typo fixes.
If you have great ideas, send an email to
fatedier@gmail.com
.
Note: We prefer you to give your advise in
issues
, so others with a same question can search it quickly and we don't need to answer them repeatedly.
Donation
If frp helps you a lot, you can support us by:
GitHub Sponsors
Support us by
Github Sponsors
.
You can have your company's logo placed on README file of this project.
PayPal
Donate money by
PayPal
to my account
fatedier@gmail.com
.
- 今日の獲得スター数: 36
- 累積スター数: 99,464

### References
- https://github.com/fatedier/frp

## NaiboWang/EasySpider

### Executive Summary
- A visual no-code/code-free web crawler/spider易采集：一个可视化浏览器自动化测试/数据采集/爬虫软件，可以无代码图形化的设计和执行爬虫任务。别名：ServiceWrapper面向Web应用的智能化服务封装系统。
- ---
- 易采集/EasySpider: Visual Code-Free Web Crawler
一个
完全免费
（
包括商业使用和二次开发
）的可视化浏览器自动化测试/数据采集/爬虫软件，可以使用图形化界面，无代码可视化的设计和执行任务。只需要在网页上选择自己想要操作的内容并根据提示框操作即可完成任务的设计和执行。同时软件还可以单独以命令行的方式进行执行，从而可以很方便的嵌入到其他系统中。
A
completely free (including for commercial use and secondary development)
visual browser automation test/data collection/crawler software, which can be used to design and execute tasks in a code-free visual way. You only need to select the content you want to operate on the web page and follow the prompts to complete the design and execution of the task. At the same time, the software can also be executed separately in the command line, so that it can be easily embedded into other systems.
下载易采集/Download EasySpider
进入
Releases Page
下载最新版本。如果下载速度慢，可以考虑中国境内下载地址：
中国境内下载地址
。
Refer to the
Releases Page
to download the latest version of EasySpider.
赞助者/Sponsors
亮数据BrightData
是代理市场领导者，覆盖全球的7200万IP，提供真人住宅IP，即时批量采集网络公开数据，成功率亲测有保证。需要性价比高代理IP的可
点击上方图片注册
后联系中文客服，开通后免费试用，
现在有首充多少就送多少的活动
。BrightData可配合EasySpider进行数据采集。
BestProxy
全球独享专属资源池，优选海外195+国家/地区高质量住宅IP，本地ISP原生IP，不限量住宅代理、长效ISP代理、静态数据中心代理、网页爬虫API，城市级精准定位，支持HTTP(S)和SOCKS5协议，低检测风险，全方位代理服务解决方案，助力各种场景业务IP代理需求。$0.66/G起按需付费和长期套餐，适合不同预算需求，24/7多语言支持，联系客服免费试用500M。可与EasySpider工具配合使用，高效采集网络数据。
IPdodo
专注为跨境用户，提供独享/纯净/家宽/原生/双ISP的全球代理IP，不限流量。全球8000万真实住宅IP，覆盖200+国家/地区，99.9%匿名保护，且支持Http/Https/Socks5协议，满足爬虫、数据采集、跨境电商、tk/fb流媒体等业务场景。现在前往IPdodo注册，支持免费试用。
官方网站/Official Website
访问易采集官网：
www.easyspider.cn
Visit the official website of EasySpider:
www.easyspider.net
软件使用示例/Software Usage Example
示例1/Example 1
（右键）选中一个大商品块 -> 软件自动检测到同类型商品块 -> 点击“选中全部”选项 -> 点击“选中子元素”选项 -> 点击“采集数据”选项，即可采集到所有商品的所有信息，并分成不同字段保存。
(Right click) Select a large product block -> The software will automatically detect similar blocks -> Click the 'Select All' option -> Click the 'Select Child Elements' option -> Click the 'Collect Data' option, you can collect the information of all products, and will be saved by sub-field.
示例2/Example 2
（右键）选中一个商品标题，同类型标题会被自动匹配，点击“选中全部”选项 -> 点击“采集数据”选项，即可采集到所有商品的标题信息。
同时，选中全部后如果选择“循环点击每个元素”选项，即可自动打开每个商品的详情页，然后可以再继续设置采集详情页的信息。
(Right Click) Select a product title, the same type of title will be automatically matched, click the 'Select All' option -> Click the 'Collect Data' option, you can collect the title information of all products.
At the same time, if you select the 'Loop-click every element' option after selecting all, you can automatically open the details page of each product, and then can set to collect the information of the details page.
更多特性/More Features
更多特性请翻到页面底部查看。
More features please scroll to the bottom of this page to view.
支持作者/Support Author
易采集EasySpider是一款完全免费且使用中无广告的开源软件，软件开发和维护全靠作者用爱发电，因此您可以选择支持作者让作者有更多的热情和精力维护此软件，或者您使用了此软件进行了盈利，欢迎您通过下面的方式支持作者：
Github Sponsor：直接点击右侧
Sponsor
按钮赞助。
支付宝账号：
naibowang@foxmail.com
，也可以扫描下方二维码。
微信收款：扫描下方二维码。
PayPal账号：naibowang，也可以扫描下方二维码。
You can support the author by clicking the
Sponsor
button at right side or pay via paypal: naibowang.
文档/Documentation
请点此进入
教程文档
，如有英文可暂时翻译一下，或看作者的
硕士毕业论文
（主要看第三章和第五章）。
Ebay样例博客：
https://blog.csdn.net/ihero/article/details/130805504
。
Documentation can be found from
GitHub Wiki
.
视频教程/Video Tutorials
Bilibili/B站视频教程:
EasySpider介绍 - 中国地震台网采集案例
设置页面向下滚动
如何无代码可视化的爬取需要登录才能爬的网站 - 知乎网站案例
循环点击列表中每个链接进入详情页采集详情页内容+设计时动态调试+动态JS
实战采集汽车网文章内容并下载文章内图片
定时执行任务+选中子元素多种模式+将提取值作为变量输入
【重要】自定义条件判断之使用循环项内的JS命令返回值 - 第二弹
流程图执行逻辑解析 - 58同城房源描述采集案例
MacOS系统设计和执行eBay网站爬虫任务教程
如何执行自己写的JS代码和系统代码 （自定义操作）
如何自定义循环和判断条件 - 第一弹
如何对元素和网页截图及命令行执行指南
OCR识别元素内容功能（常用于文字验证码）
如何爬需要输入验证码的网站
如何切换IP池和使用隧道IP - 打开详情页采集案例
如何同时执行多个任务（并行多开）
Python代码运算后的结果作为文本框的输入
实例 - 反人类网站文章采集和代码调试
写入MySQL数据库教程
从源代码编译程序并设计运行和调试任务指南（基于Ubuntu24.04）
Refer to
Youtube Playlist
to see the video tutorials of EasySpider.
样例任务/Sample Tasks
从本项目的
Examples
文件夹中下载样例任务，更名为大于0的数字，导入到EasySpider中的
tasks
文件夹中，然后在EasySpider中打开即可。
Download sample tasks from the
Examples
folder of this project, rename them to numbers greater than 0, import them into the
tasks
folder in EasySpider, and then open them in EasySpider.
声明/Declaration
本软件仅供学习交流使用，
严禁使用软件进行任何违法违规的操作，如爬取不允许爬取的政府/军事机关网站等
。使用本软件所造成的
一切后果由使用者自负
，与作者本人无关，
作者不会承担任何责任
。
This software is for learning and communication only.
It is strictly forbidden to use the software for any illegal operations, such as crawling government/military websites that are not allowed to be crawled.
All consequences caused by the use of this software are
at the user's own risk, and the author is not responsible for any consequences
.
对于政府和军事机关等网站的爬虫操作，
作者将不会进行任何答疑
，以免违反国家相关法律法规和政策。
For the crawler operations of government and military websites,
the author will not answer any questions
in order to avoid violating relevant national laws, regulations and policies.
EasySpider遵循AGPL-3.0协议，
任何个人和企业都可以免费使用软件本身或使用源代码进行二次开发，无需联系作者进行商业（专利）授权
，但需要注意AGPL-3.0协议的相关规则：
EasySpider complies with the AGPL-3.0 agreement.
Any individual or enterprise can use the software for free and use the software source code for secondary development without contacting the author for commercial (patent) authorization.
However, it is necessary to pay attention to the related rules of the AGPL-3.0 agreement:
1. Copyleft（传染性） / Copyleft (Viral Clause)
衍生作品 / Derivative Works
任何基于 AGPL 代码的修改或衍生作品，必须
以相同许可证（AGPL-3.0）发布
。
Any modifications or derivative works based on AGPL code must be
licensed under AGPL-3.0
.
联动范围 / Scope of Copyleft
若 AGPL 代码与其他代码结合（如静态链接、紧密集成），整个作品需遵守 AGPL。
If AGPL code is combined with other code (e.g., static linking), the entire work must comply with AGPL.
2. 网络使用条款 / Network Use Clause
SaaS 触发开源义务 / SaaS Trigger
若软件以服务形式提供（如网站、API），必须向所有用户公开
完整对应源代码
（包括修改后的代码）。
If the software is provided as a service (e.g., website, API), the
full corresponding source code
(including modifications) must be made available to all users.
用户权利 / User Rights
服务的接收者可通过下载或书面请求获取源码。
Service recipients may obtain the source code via download or written request.
3. 源码提供要求 / Source Code Provision
二进制分发 / Binary Distribution
必须附带源码或提供获取渠道（如下载链接）。
Source code must be included or a download link provided.
网络服务场景 / Network Service Scenario
需通过服务界面
显式提供源码链接
，或向用户书面承诺提供源码。
The service interface must
explicitly provide a source code link
or offer a written offer for source code.
4. 专利授权 / Patent Grant
贡献者自动授予用户与软件相关的专利许可，禁止专利诉讼。
Contributors automatically grant users patent rights related to the software, and prohibit patent litigation.
5. 免责声明 / Disclaimer
软件按“原样”提供，作者
不承担任何责任
（无担保条款）。
The software is provided "as is" with
no warranties or liabilities
.
答疑QQ群
群号：
682921940
，建议通过Github提Issue的方式答疑，如果实在有需要才请加QQ群，因为群人数有上限，
QQ群不提供软件下载功能
。
出版物/Publications
This software has been accepted by The Web Conference (WWW) 2023 (中国计算机学会顶级会议，CCF A):
EasySpider: A No-Code Visual System for Crawling the Web
, April 2023.
中国国家知识产权局发明专利，
一种自定义提取流程的服务封装系统
， 2022年5月。
浙江大学硕士论文
，
面向WEB应用的智能化服务封装系统设计与实现
，2020年6月。
编译说明/Compilation Instructions
查看
编译说明
。
Refer to
Compilation Instructions
.
支持特性/Supported Features
中文界面截图
软件界面示例
块和子块及表单定义
已选中和待选择示例
京东商品块选择示例：
京东商品标题自动匹配选择示例
分块选择所有子元素示例
同类型元素自动和手动匹配示例
四种选择方式示例
输入文字示例
循环点击58同城房屋标题以进入详情页采集示例
采集元素文本示例
流程图界面介绍
循环选项示例
循环点击下一页示例
条件分支示例
完整采集流程图示例
完整采集流程图转换为常规流程图示例
服务信息示例
服务调用示例
58 同城房源信息采集服务部分采集结果展示
- 今日の獲得スター数: 36
- 累積スター数: 42,881

### References
- https://github.com/NaiboWang/EasySpider

## katanemo/archgw

### Executive Summary
- The smart edge and AI gateway for agents. Arch is a high-performance proxy server that handles the low-level work in building agents: like applying guardrails, routing prompts to the right agent, and unifying access to LLMs, etc. Natively designed to handle and process prompts, Arch helps you build agents faster.
- ---
- Arch is a modular ai-native edge and AI gateway for agents.
Arch handles the
pesky low-level work
in building agentic apps — like applying guardrails, clarifying vague user input, routing prompts to the right agent, and unifying access to any LLM. It’s a language and framework friendly infrastructure layer designed to help you build and ship agentic apps faster.
Quickstart
•
Demos
•
Route LLMs
•
Build agentic apps with Arch
•
Documentation
•
Contact
About The Latest Release:
[0.3.15]
Preference-aware multi LLM routing for Claude Code 2.0
Overview
AI demos are easy to hack. But once you move past a prototype, you’re stuck building and maintaining low-level plumbing code that slows down real innovation. For example:
Routing & orchestration.
Put routing in code and you’ve got two choices: maintain it yourself or live with a framework’s baked-in logic. Either way, keeping routing consistent means pushing code changes across all your agents, slowing iteration and turning every policy tweak into a refactor instead of a config flip.
Model integration churn.
Frameworks wire LLM integrations directly into code abstractions, making it hard to add or swap models without touching application code — meaning you’ll have to do codewide search/replace every time you want to experiment with a new model or version.
Observability & governance.
Logging, tracing, and guardrails are baked in as tightly coupled features, so bringing in best-of-breed solutions is painful and often requires digging through the guts of a framework.
Prompt engineering overhead
. Input validation, clarifying vague user input, and coercing outputs into the right schema all pile up, turning what should be design work into low-level plumbing work.
Brittle upgrades
. Every change (new model, new guardrail, new trace format) means patching and redeploying application servers. Contrast that with bouncing a central proxy—one upgrade, instantly consistent everywhere.
With Arch, you can move faster by focusing on higher-level objectives in a language and framework agnostic way.
Arch
was built by the contributors of
Envoy Proxy
with the belief that:
Prompts are nuanced and opaque user requests, which require the same capabilities as traditional HTTP requests including secure handling, intelligent routing, robust observability, and integration with backend (API) systems to improve speed and accuracy for common agentic scenarios  – all outside core application logic.*
Core Features
:
🚦 Route to Agents
: Engineered with purpose-built
LLMs
for fast (<100ms) agent routing and hand-off
🔗 Route to LLMs
: Unify access to LLMs with support for
three routing strategies
.
⛨ Guardrails
: Centrally configure and prevent harmful outcomes and ensure safe user interactions
⚡ Tools Use
: For common agentic scenarios let Arch instantly clarify and convert prompts to tools/API calls
🕵 Observability
: W3C compatible request tracing and LLM metrics that instantly plugin with popular tools
🧱 Built on Envoy
: Arch runs alongside app servers as a containerized process, and builds on top of
Envoy's
proven HTTP management and scalability features to handle ingress and egress traffic related to prompts and LLMs.
High-Level Sequence Diagram
:
Jump to our
docs
to learn how you can use Arch to improve the speed, security and personalization of your GenAI apps.
Important
Today, the function calling LLM (Arch-Function) designed for the agentic and RAG scenarios is hosted free of charge in the US-central region. To offer consistent latencies and throughput, and to manage our expenses, we will enable access to the hosted version via developers keys soon, and give you the option to run that LLM locally. For more details see this issue
#258
Contact
To get in touch with us, please join our
discord server
. We will be monitoring that actively and offering support there.
Demos
Sample App: Weather Forecast Agent
- A sample agentic weather forecasting app that highlights core function calling capabilities of Arch.
Sample App: Network Operator Agent
- A simple network device switch operator agent that can retrive device statistics and reboot them.
User Case: Connecting to SaaS APIs
- Connect 3rd party SaaS APIs to your agentic chat experience.
Quickstart
Follow this quickstart guide to use Arch as a router for local or hosted LLMs, including dynamic routing. Later in the section we will see how you can Arch to build highly capable agentic applications, and to provide e2e observability.
Prerequisites
Before you begin, ensure you have the following:
Docker System
(v24)
Docker compose
(v2.29)
Python
(v3.13)
Arch's CLI allows you to manage and interact with the Arch gateway efficiently. To install the CLI, simply run the following command:
Tip
We recommend that developers create a new Python virtual environment to isolate dependencies before installing Arch. This ensures that archgw and its dependencies do not interfere with other packages on your system.
$
python3.12 -m venv venv
$
source
venv/bin/activate
#
On Windows, use: venv\Scripts\activate
$
pip install archgw==0.3.15
Use Arch as a LLM Router
Arch supports three powerful routing strategies for LLMs: model-based routing, alias-based routing, and preference-based routing. Each strategy offers different levels of abstraction and control for managing your LLM infrastructure.
Model-based Routing
Model-based routing allows you to configure specific models with static routing. This is ideal when you need direct control over which models handle specific requests. Arch supports 11+ LLM providers including OpenAI, Anthropic, DeepSeek, Mistral, Groq, and more.
version
:
v0.1.0
listeners
:
egress_traffic
:
address
:
0.0.0.0
port
:
12000
message_format
:
openai
timeout
:
30s
llm_providers
:
  -
model
:
openai/gpt-4o
access_key
:
$OPENAI_API_KEY
default
:
true
-
model
:
anthropic/claude-3-5-sonnet-20241022
access_key
:
$ANTHROPIC_API_KEY
You can then route to specific models using any OpenAI-compatible client:
from
openai
import
OpenAI
client
=
OpenAI
(
base_url
=
"http://127.0.0.1:12000/v1"
,
api_key
=
"test"
)
# Route to specific model
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
"anthropic/claude-3-5-sonnet-20241022"
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
"Explain quantum computing"
}]
)
Alias-based Routing
Alias-based routing lets you create semantic model names that map to underlying providers. This approach decouples your application code from specific model names, making it easy to experiment with different models or handle provider changes.
version
:
v0.1.0
listeners
:
egress_traffic
:
address
:
0.0.0.0
port
:
12000
message_format
:
openai
timeout
:
30s
llm_providers
:
  -
model
:
openai/gpt-4o
access_key
:
$OPENAI_API_KEY
-
model
:
anthropic/claude-3-5-sonnet-20241022
access_key
:
$ANTHROPIC_API_KEY
model_aliases
:
#
Model aliases - friendly names that map to actual model names
fast-model
:
target
:
gpt-4o-mini
reasoning-model
:
target
:
gpt-4o
creative-model
:
target
:
claude-3-5-sonnet-20241022
Use semantic aliases in your application code:
# Your code uses semantic names instead of provider-specific ones
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
"reasoning-model"
,
# Routes to best available reasoning model
messages
=
[{
"role"
:
"user"
,
"content"
:
"Solve this complex problem..."
}]
)
Preference-aligned Routing
Preference-aligned routing provides intelligent, dynamic model selection based on natural language descriptions of tasks and preferences. Instead of hardcoded routing logic, you describe what each model is good at using plain English.
version
:
v0.1.0
listeners
:
egress_traffic
:
address
:
0.0.0.0
port
:
12000
message_format
:
openai
timeout
:
30s
llm_providers
:
  -
model
:
openai/gpt-4o
access_key
:
$OPENAI_API_KEY
routing_preferences
:
      -
name
:
complex_reasoning
description
:
deep analysis, mathematical problem solving, and logical reasoning
-
name
:
creative_writing
description
:
storytelling, creative content, and artistic writing
-
model
:
deepseek/deepseek-coder
access_key
:
$DEEPSEEK_API_KEY
routing_preferences
:
      -
name
:
code_generation
description
:
generating new code, writing functions, and creating scripts
-
name
:
code_review
description
:
analyzing existing code for bugs, improvements, and optimization
Arch uses a lightweight 1.5B autoregressive model to intelligently map user prompts to these preferences, automatically selecting the best model for each request. This approach adapts to intent drift, supports multi-turn conversations, and avoids brittle embedding-based classifiers or manual if/else chains. No retraining required when adding models or updating policies — routing is governed entirely by human-readable rules.
Learn More
: Check our
documentation
for comprehensive provider setup guides and routing strategies. You can learn more about the design, benchmarks, and methodology behind preference-based routing in our paper:
Build Agentic Apps with Arch
In following quickstart we will show you how easy it is to build AI agent with Arch gateway. We will build a currency exchange agent using following simple steps. For this demo we will use
https://api.frankfurter.dev/
to fetch latest price for currencies and assume USD as base currency.
Step 1. Create arch config file
Create
arch_config.yaml
file with following content,
version
:
v0.1.0
listeners
:
ingress_traffic
:
address
:
0.0.0.0
port
:
10000
message_format
:
openai
timeout
:
30s
llm_providers
:
  -
access_key
:
$OPENAI_API_KEY
model
:
openai/gpt-4o
system_prompt
:
|
You are a helpful assistant.
prompt_guards
:
input_guards
:
jailbreak
:
on_exception
:
message
:
Looks like you're curious about my abilities, but I can only provide assistance for currency exchange.
prompt_targets
:
  -
name
:
currency_exchange
description
:
Get currency exchange rate from USD to other currencies
parameters
:
      -
name
:
currency_symbol
description
:
the currency that needs conversion
required
:
true
type
:
str
in_path
:
true
endpoint
:
name
:
frankfurther_api
path
:
/v1/latest?base=USD&symbols={currency_symbol}
system_prompt
:
|
You are a helpful assistant. Show me the currency symbol you want to convert from USD.
-
name
:
get_supported_currencies
description
:
Get list of supported currencies for conversion
endpoint
:
name
:
frankfurther_api
path
:
/v1/currencies
endpoints
:
frankfurther_api
:
endpoint
:
api.frankfurter.dev:443
protocol
:
https
Step 2. Start arch gateway with currency conversion config
$ archgw up arch_config.yaml
2024-12-05 16:56:27,979 - cli.main - INFO - Starting archgw cli version: 0.3.15
2024-12-05 16:56:28,485 - cli.utils - INFO - Schema validation successful
!
2024-12-05 16:56:28,485 - cli.main - INFO - Starting arch model server and arch gateway
2024-12-05 16:56:51,647 - cli.core - INFO - Container is healthy
!
Once the gateway is up you can start interacting with at port 10000 using openai chat completion API.
Some of the sample queries you can ask could be
what is currency rate for gbp?
or
show me list of currencies for conversion
.
Step 3. Interacting with gateway using curl command
Here is a sample curl command you can use to interact,
$ curl --header
'
Content-Type: application/json
'
\
  --data
'
{"messages": [{"role": "user","content": "what is exchange rate for gbp"}], "model": "none"}
'
\
  http://localhost:10000/v1/chat/completions
|
jq
"
.choices[0].message.content
"
"
As of the date provided in your context, December 5, 2024, the exchange rate for GBP (British Pound) from USD (United States Dollar) is 0.78558. This means that 1 USD is equivalent to 0.78558 GBP.
"
And to get list of supported currencies,
$ curl --header
'
Content-Type: application/json
'
\
  --data
'
{"messages": [{"role": "user","content": "show me list of currencies that are supported for conversion"}], "model": "none"}
'
\
  http://localhost:10000/v1/chat/completions
|
jq
"
.choices[0].message.content
"
"
Here is a list of the currencies that are supported for conversion from USD, along with their symbols:\n\n1. AUD - Australian Dollar\n2. BGN - Bulgarian Lev\n3. BRL - Brazilian Real\n4. CAD - Canadian Dollar\n5. CHF - Swiss Franc\n6. CNY - Chinese Renminbi Yuan\n7. CZK - Czech Koruna\n8. DKK - Danish Krone\n9. EUR - Euro\n10. GBP - British Pound\n11. HKD - Hong Kong Dollar\n12. HUF - Hungarian Forint\n13. IDR - Indonesian Rupiah\n14. ILS - Israeli New Sheqel\n15. INR - Indian Rupee\n16. ISK - Icelandic Króna\n17. JPY - Japanese Yen\n18. KRW - South Korean Won\n19. MXN - Mexican Peso\n20. MYR - Malaysian Ringgit\n21. NOK - Norwegian Krone\n22. NZD - New Zealand Dollar\n23. PHP - Philippine Peso\n24. PLN - Polish Złoty\n25. RON - Romanian Leu\n26. SEK - Swedish Krona\n27. SGD - Singapore Dollar\n28. THB - Thai Baht\n29. TRY - Turkish Lira\n30. USD - United States Dollar\n31. ZAR - South African Rand\n\nIf you want to convert USD to any of these currencies, you can select the one you are interested in.
"
Observability
Arch is designed to support best-in class observability by supporting open standards. Please read our
docs
on observability for more details on tracing, metrics, and logs. The screenshot below is from our integration with Signoz (among others)
Debugging
When debugging issues / errors application logs and access logs provide key information to give you more context on whats going on with the system. Arch gateway runs in info log level and following is a typical output you could see in a typical interaction between developer and arch gateway,
$ archgw up --service archgw --foreground
...
[2025-03-26 18:32:01.350][26][info] prompt_gateway: on_http_request_body: sending request to model server
[2025-03-26 18:32:01.851][26][info] prompt_gateway: on_http_call_response: model server response received
[2025-03-26 18:32:01.852][26][info] prompt_gateway: on_http_call_response: dispatching api call to developer endpoint: weather_forecast_service, path: /weather, method: POST
[2025-03-26 18:32:01.882][26][info] prompt_gateway: on_http_call_response: developer api call response received: status code: 200
[2025-03-26 18:32:01.882][26][info] prompt_gateway: on_http_call_response: sending request to upstream llm
[2025-03-26 18:32:01.883][26][info] llm_gateway: on_http_request_body: provider: gpt-4o-mini, model requested: None, model selected: gpt-4o-mini
[2025-03-26 18:32:02.818][26][info] llm_gateway: on_http_response_body: time to first token: 1468ms
[2025-03-26 18:32:04.532][26][info] llm_gateway: on_http_response_body: request latency: 3183ms
...
Log level can be changed to debug to get more details. To enable debug logs edit (supervisord.conf)[arch/supervisord.conf], change the log level
--component-log-level wasm:info
to
--component-log-level wasm:debug
. And after that you need to rebuild docker image and restart the arch gateway using following set of commands,
# make sure you are at the root of the repo
$ archgw build
# go to your service that has arch_config.yaml file and issue following command,
$ archgw up --service archgw --foreground
Contribution
We would love feedback on our
Roadmap
and we welcome contributions to
Arch
!
Whether you're fixing bugs, adding new features, improving documentation, or creating tutorials, your help is much appreciated.
Please visit our
Contribution Guide
for more details
- 今日の獲得スター数: 36
- 累積スター数: 3,928

### References
- https://github.com/katanemo/archgw

## gkd-kit/gkd

### Executive Summary
- 基于无障碍，高级选择器，订阅规则的自定义屏幕点击 Android 应用 | An Android APP with custom screen tapping based on Accessibility, Advanced Selectors, and Subscription Rules
- ---
- gkd
基于
高级选择器
+
订阅规则
+
快照审查
的自定义屏幕点击 Android 应用
通过自定义规则，在指定界面，满足指定条件(如屏幕上存在特定文字)时，点击特定的节点或位置或执行其他操作
快捷操作
帮助你简化一些重复的流程, 如某些软件自动确认电脑登录
跳过流程
某些软件可能在启动时存在一些烦人的流程, 这个软件可以帮助你点击跳过这个流程
免责声明
本项目遵循
GPL-3.0
开源，项目仅供学习交流，禁止用于商业或非法用途
安装
如遇问题请先查看
疑难解答
截图
订阅
GKD
默认不提供规则
，需自行添加本地规则，或者通过订阅链接的方式获取远程规则
也可通过
subscription-template
快速构建自己的远程订阅
第三方订阅列表可在
https://github.com/topics/gkd-subscription
查看
要加入此列表, 需点击仓库主页右上角设置图标后在 Topics 中添加
gkd-subscription
示例图片 - 添加至 Topics (点击展开)
选择器
一个类似 CSS 选择器的选择器, 能联系节点上下文信息, 更容易也更精确找到目标节点
https://gkd.li/guide/selector
@[vid="menu"] < [vid="menu_container"] - [vid="dot_text_layout"] > [text^="广告"]
示例图片 - 选择器路径视图 (点击展开)
捐赠
如果 GKD 对你有用, 可以通过以下链接支持该项目
https://github.com/lisonge/sponsor
或前往
Google Play
给个好评
Star History
- 今日の獲得スター数: 35
- 累積スター数: 31,388

### References
- https://github.com/gkd-kit/gkd

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
- 今日の獲得スター数: 35
- 累積スター数: 30,074

### References
- https://github.com/keycloak/keycloak

## dataease/SQLBot

### Executive Summary
- 🔥 基于大模型和 RAG 的智能问数系统。Text-to-SQL Generation via LLMs using RAG.
- ---
- 基于大模型和 RAG 的智能问数系统
SQLBot 是一款基于大模型和 RAG 的智能问数系统。SQLBot 的优势包括：
开箱即用
: 只需配置大模型和数据源即可开启问数之旅，通过大模型和 RAG 的结合来实现高质量的 text2sql；
易于集成
: 支持快速嵌入到第三方业务系统，也支持被 n8n、MaxKB、Dify、Coze 等 AI 应用开发平台集成调用，让各类应用快速拥有智能问数能力；
安全可控
: 提供基于工作空间的资源隔离机制，能够实现细粒度的数据权限控制。
工作原理
快速开始
安装部署
准备一台 Linux 服务器，安装好
Docker
，执行以下一键安装脚本：
docker run -d \
  --name sqlbot \
  --restart unless-stopped \
  -p 8000:8000 \
  -p 8001:8001 \
  -v ./data/sqlbot/excel:/opt/sqlbot/data/excel \
  -v ./data/sqlbot/file:/opt/sqlbot/data/file \
  -v ./data/sqlbot/images:/opt/sqlbot/images \
  -v ./data/sqlbot/logs:/opt/sqlbot/app/logs \
  -v ./data/postgresql:/var/lib/postgresql/data \
  --privileged=true \
  dataease/sqlbot
你也可以通过
1Panel 应用商店
快速部署 SQLBot。
如果是内网环境，你可以通过
离线安装包方式
部署 SQLBot。
访问方式
在浏览器中打开: http://<你的服务器IP>:8000/
用户名: admin
密码: SQLBot@123456
联系我们
如你有更多问题，可以加入我们的技术交流群与我们交流。
UI 展示
Star History
飞致云旗下的其他明星项目
DataEase
- 人人可用的开源 BI 工具
1Panel
- 现代化、开源的 Linux 服务器运维管理面板
MaxKB
- 强大易用的企业级智能体平台
JumpServer
- 广受欢迎的开源堡垒机
Cordys CRM
- 新一代的开源 AI CRM 系统
Halo
- 强大易用的开源建站工具
MeterSphere
- 新一代的开源持续测试工具
License
本仓库遵循
FIT2CLOUD Open Source License
开源协议，该许可证本质上是 GPLv3，但有一些额外的限制。
你可以基于 SQLBot 的源代码进行二次开发，但是需要遵守以下规定：
不能替换和修改 SQLBot 的 Logo 和版权信息；
二次开发后的衍生作品必须遵守 GPL V3 的开源义务。
如需商业授权，请联系
support@fit2cloud.com
。
- 今日の獲得スター数: 33
- 累積スター数: 3,711

### References
- https://github.com/dataease/SQLBot

## intruder-io/autoswagger

### Executive Summary
- Autoswagger by Intruder - detect API auth weaknesses
- ---
- Autoswagger
by
Intruder
Autoswagger
is a command-line tool designed to discover, parse, and test for unauthenticated endpoints using
Swagger/OpenAPI
documentation. It helps identify potential security issues in unprotected endpoints of APIs, such as PII leaks and common secret exposures.
Please note that this initial release of Autoswagger is by no means complete, and there are some types of specification which the tool does not currently handle. Please feel free to use it as you wish, and extend its detection capabilities or add detection regexes to cover your specific use-case!
Table of Contents
Introduction
Key Features
Installation & Usage
Discovery Phases
Endpoint Testing
PII Detection
Output Examples
Stats & Reporting
Acknowledgments
Introduction
Autoswagger automates the process of finding
OpenAPI/Swagger
specifications, extracting API endpoints, and systematically testing them for
PII
exposure,
secrets
, and large or interesting responses. It leverages
Presidio
for PII recognition and
regex
for sensitive key/token detection.
Key Features
Multiple Discovery Phases
Discovers OpenAPI specs in three ways:
Direct Spec
: If a full URL with a path ending in
.json
,
.yaml
, or
.yml
is provided, parse that file directly.
Swagger UI
: Parse known paths of Swagger UI (e.g.
/swagger-ui.html
), and extract spec from HTML or JavaScript.
Direct Spec by Bruteforce
: Attempt discovery using common OpenAPI schema locations (
/swagger.json
,
/openapi.json
, etc.). Only attempt this if 1. and 2. did not yield a result.
Parallel Endpoint Testing
Multi-threaded concurrent testing of many endpoints, respecting a configurable rate limit (
-rate
).
Brute-Force of Parameter Values
If
-b
or
--brute
is used, try using various data types with a few example values in an attempt to bypass parameter-specific validations.
Presidio PII Detection
Check output for phone numbers, emails, addresses, and names (with context validation to reduce false positives). Also parse CSV rows and naive “key: value” lines.
Secrets Detection
Leverages a set of regex patterns to detect tokens, keys, and debugging artifacts (like environment variables).
Command Line or JSON Output
In default mode, displays results in a table. With
-json
, output a JSON structure.
-product
mode filters output to only show those that contain PII, secrets, or large responses.
Installation & Usage
Clone
or
download
the repository containing Autoswagger.
git clone git@github.com:intruder-io/autoswagger.git
Install dependencies
(e.g., using Python 3.7+):
pip install -r requirements.txt
(It's recommended to use a virtual environment for this:
python3 -m venv venv;source venv/bin/activate
)
Check installation, show help:
python3 autoswagger.py -h
Flags
Flag
Description
urls
List of base URLs or direct spec URLs.
-v, --verbose
Enables verbose logging. Creates a log file under
~/.autoswagger/logs
.
-risk
Includes non-GET methods (POST, PUT, PATCH, DELETE) in testing.
-all
Includes 200 and 404 endpoints in output (excludes 401/403).
-product
Outputs only endpoints with PII or large responses, in JSON format.
-stats
Displays scan statistics (e.g. requests, RPS, hosts with PII).
-rate <N>
Throttles requests to N requests per second. Default is 30. Use 0 to disable rate limiting.
-b, --brute
Enables brute-forcing of parameter values (multiple test combos).
-json
Outputs results in JSON format instead of a Rich table in default mode.
Help
/   | __  __/ /_____  ______      ______ _____ _____ ____  _____
     / /| |/ / / / __/ __ \/ ___/ | /| / / __ `/ __ `/ __ `/ _ \/ ___/
    / ___ / /_/ / /_/ /_/ (__  )| |/ |/ / /_/ / /_/ / /_/ /  __/ /
    /_/  |_\__,_/\__/\____/____/ |__/|__/_\__,_/\__, /\__, /\___/_/
                                              /____//____/
                              https://intruder.io
                          Find unauthenticated endpoints

usage: autoswagger.py [-h] [-v] [-risk] [-all] [-product] [-stats] [-rate RATE] [-b] [-json] [urls ...]

Autoswagger: Detect unauthenticated access control issues via Swagger/OpenAPI documentation.

positional arguments:
  urls           Base URL(s) or spec URL(s) of the target API(s)

options:
  -h, --help     show this help message and exit
  -v, --verbose  Enable verbose output
  -risk          Include non-GET requests in testing
  -all           Include all HTTP status codes in the results, excluding 401 and 403
  -product       Output all endpoints in JSON, flagging those that contain PII or have large responses.
  -stats         Display scan statistics. Included in JSON if -product or -json is used.
  -rate RATE     Set the rate limit in requests per second (default: 30). Use 0 to disable rate limiting.
  -b, --brute    Enable exhaustive testing of parameter values.
  -json          Output results in JSON format in default mode.

Example usage:
  python autoswagger.py https://api.example.com -v
Discovery Phases
Direct Spec
If a provided URL ends with
.json/.yaml/.yml
, Autoswagger
directly
attempts to parse the OpenAPI schema.
Swagger-UI Detection
Tries known UI paths (e.g.,
/swagger-ui.html
).
If found, parses the HTML or local JavaScript files for a
swagger.json
or
openapi.json
.
Can detect embedded configs like
window.swashbuckleConfig
.
Direct Spec by Bruteforce
If no spec is found so far, Autoswagger attempts a list of default endpoints like
/swagger.json
,
/openapi.json
, etc.
Stops when a valid spec is discovered or none are found.
Endpoint Testing
Collect Endpoints
After loading a spec, Autoswagger extracts each path and method under the
paths
key.
HTTP Methods
By default, tests
GET
only.
Use
-risk
to include other methods (
POST
,
PUT
,
PATCH
,
DELETE
).
Parameter Values
Fill path/query parameters with defaults or values to enumerate.
Optionally builds request bodies from the spec’s
requestBody
(OpenAPI 3) or body parameters (Swagger 2).
Rate Limiting & Concurrency
Supports threading with a cap on requests per second (
-rate
).
Each endpoint is tested in a dedicated job.
Response Analysis
Decodes responses, checks for PII, secrets, and large content.
Logs relevant findings.
PII Detection
Presidio-Based Analysis
Searches for phone numbers, emails, addresses, names.
Context-based scanning (e.g., CSV headers, key-value lines).
Secrets & Debug Info
TruffleHog-like regex checks for API keys, tokens, environment variables.
Merges any matches into the PII data structure for final reporting.
Large Response Check
Flags responses with 100+ JSON elements or large XML structures as “interesting.”
Also checks raw size threshold (e.g., >100k bytes).
Output
By default, output is shown in a table.
-json
produces JSON objects, grouping results by endpoint.
-product
filters down to only “interesting” endpoints (PII, large responses and responses with secrets).
Interpreting Results
For most use cases, interpreting results involves looking at the output (endpoints resulting in Status Code 200s), and paying particular attention to endpoints which are marked as 'PII or Secret Detected'. These endpoints are the ones that contain impactful exposures, but they should be manually checked to confirm. You may also wish to look at other 200s that do not contain PII, and determine whether it's intended for these endpoints to be public or not.
Simple GET endpoints can be triaged using command line tools like curl, but we would recommend using your usual API testing suite (tools such as Postman or Burp Suite) to replay requests and read responses to confirm whether an exposure is present.
Stats & Reporting
-stats
appends or prints overall statistics, such as:
Hosts with valid specs
Hosts with PII
Total requests sent, average RPS
Percentage of endpoints responding with 2xx or 4xx
Shown in either a Rich table in default mode or embedded in JSON if
-json
or
-product
is used.
Acknowledgments
Autoswagger is maintained and owned by
Intruder
. It was primarily developed by Cale Anderson
- 今日の獲得スター数: 32
- 累積スター数: 1,473

### References
- https://github.com/intruder-io/autoswagger

## microsoft/edit

### Executive Summary
- We all edit.
- ---
- Edit
A simple editor for simple needs.
This editor pays homage to the classic
MS-DOS Editor
, but with a modern interface and input controls similar to VS Code. The goal is to provide an accessible editor that even users largely unfamiliar with terminals can easily use.
Installation
You can also download binaries from
our Releases page
.
Windows
You can install the latest version with WinGet:
winget install Microsoft.Edit
Build Instructions
Install Rust
Install the nightly toolchain:
rustup install nightly
Alternatively, set the environment variable
RUSTC_BOOTSTRAP=1
Clone the repository
For a release build, run:
cargo build --config .cargo/release.toml --release
Build Configuration
During compilation you can set various environment variables to configure the build. The following table lists the available configuration options:
Environment variable
Description
EDIT_CFG_ICU*
See
ICU library name (SONAME)
for details.
EDIT_CFG_LANGUAGES
A comma-separated list of languages to include in the build. See
i18n/edit.toml
for available languages.
Notes to Package Maintainers
Package Naming
The canonical executable name is "edit" and the alternative name is "msedit".
We're aware of the potential conflict of "edit" with existing commands and recommend alternatively naming packages and executables "msedit".
Names such as "ms-edit" should be avoided.
Assigning an "edit" alias is recommended, if possible.
ICU library name (SONAME)
This project
optionally
depends on the ICU library for its Search and Replace functionality.
By default, the project will look for a SONAME without version suffix:
Windows:
icuuc.dll
macOS:
libicuuc.dylib
UNIX, and other OS:
libicuuc.so
If your installation uses a different SONAME, please set the following environment variable at build time:
EDIT_CFG_ICUUC_SONAME
:
For instance,
libicuuc.so.76
.
EDIT_CFG_ICUI18N_SONAME
:
For instance,
libicui18n.so.76
.
Additionally, this project assumes that the ICU exports are exported without
_
prefix and without version suffix, such as
u_errorName
.
If your installation uses versioned exports, please set:
EDIT_CFG_ICU_CPP_EXPORTS
:
If set to
true
, it'll look for C++ symbols such as
_u_errorName
.
Enabled by default on macOS.
EDIT_CFG_ICU_RENAMING_VERSION
:
If set to a version number, such as
76
, it'll look for symbols such as
u_errorName_76
.
Finally, you can set the following environment variables:
EDIT_CFG_ICU_RENAMING_AUTO_DETECT
:
If set to
true
, the executable will try to detect the
EDIT_CFG_ICU_RENAMING_VERSION
value at runtime.
The way it does this is not officially supported by ICU and as such is not recommended to be relied upon.
Enabled by default on UNIX (excluding macOS) if no other options are set.
To test your settings, run
cargo test
again but with the
--ignored
flag. For instance:
cargo
test
-- --ignored
- 今日の獲得スター数: 31
- 累積スター数: 12,384

### References
- https://github.com/microsoft/edit

## YunaiV/ruoyi-vue-pro

### Executive Summary
- 🔥 官方推荐 🔥 RuoYi-Vue 全新 Pro 版本，优化重构所有功能。基于 Spring Boot + MyBatis Plus + Vue & Element 实现的后台管理系统 + 微信小程序，支持 RBAC 动态权限、数据权限、SaaS 多租户、Flowable 工作流、三方登录、支付、短信、商城、CRM、ERP、AI 大模型等功能。你的 ⭐️ Star ⭐️，是作者生发的动力！
- ---
- 严肃声明：现在、未来都不会有商业版本，所有代码全部开源!！
「我喜欢写代码，乐此不疲」
「我喜欢做开源，以此为乐」
我 🐶 在上海艰苦奋斗，早中晚在 top3 大厂认真搬砖，夜里为开源做贡献。
如果这个项目让你有所收获，记得 Star 关注哦，这对我是非常不错的鼓励与支持。
🐶 新手必读
演示地址【Vue3 + element-plus】：
http://dashboard-vue3.yudao.iocoder.cn
演示地址【Vue3 + vben(ant-design-vue)】：
http://dashboard-vben.yudao.iocoder.cn
演示地址【Vue2 + element-ui】：
http://dashboard.yudao.iocoder.cn
启动文档：
https://doc.iocoder.cn/quick-start/
视频教程：
https://doc.iocoder.cn/video/
🐰 版本说明
版本
JDK 8 + Spring Boot 2.7
JDK 17/21 + Spring Boot 3.2
【完整版】
ruoyi-vue-pro
master
分支
master-jdk17
分支
【精简版】
yudao-boot-mini
master
分支
master-jdk17
分支
【完整版】：包括系统功能、基础设施、会员中心、数据报表、工作流程、商城系统、微信公众号、CRM、ERP 等功能
【精简版】：只包括系统功能、基础设施功能，不包括会员中心、数据报表、工作流程、商城系统、微信公众号、CRM、ERP 等功能
可参考
《迁移文档》
，只需要 5-10 分钟，即可将【完整版】按需迁移到【精简版】
🐯 平台简介
芋道
，以开发者为中心，打造中国第一流的快速开发平台，全部开源，个人与企业可 100% 免费使用。
有任何问题，或者想要的功能，可以在
Issues
中提给艿艿。
😜 给项目点点 Star 吧，这对我们真的很重要！
Java 后端：
master
分支为 JDK 8 + Spring Boot 2.7，
master-jdk17
分支为 JDK 17/21 + Spring Boot 3.2
管理后台的电脑端：Vue3 提供
element-plus
、
vben(ant-design-vue)
两个版本，Vue2 提供
element-ui
版本
管理后台的移动端：采用
uni-app
方案，一份代码多终端适配，同时支持 APP、小程序、H5！
后端采用 Spring Boot 多模块架构、MySQL + MyBatis Plus、Redis + Redisson
数据库可使用 MySQL、Oracle、PostgreSQL、SQL Server、MariaDB、国产达梦 DM、TiDB 等
消息队列可使用 Event、Redis、RabbitMQ、Kafka、RocketMQ 等
权限认证使用 Spring Security & Token & Redis，支持多终端、多种用户的认证系统，支持 SSO 单点登录
支持加载动态权限菜单，按钮级别权限控制，Redis 缓存提升性能
支持 SaaS 多租户，可自定义每个租户的权限，提供透明化的多租户底层封装
工作流使用 Flowable，支持动态表单、在线设计流程、会签 / 或签、多种任务分配方式
高效率开发，使用代码生成器可以一键生成 Java、Vue 前后端代码、SQL 脚本、接口文档，支持单表、树表、主子表
实时通信，采用 Spring WebSocket 实现，内置 Token 身份校验，支持 WebSocket 集群
集成微信小程序、微信公众号、企业微信、钉钉等三方登陆，集成支付宝、微信等支付与退款
集成阿里云、腾讯云等短信渠道，集成 MinIO、阿里云、腾讯云、七牛云等云存储服务
集成报表设计器、大屏设计器，通过拖拽即可生成酷炫的报表与大屏
🐳 项目关系
三个项目的功能对比，可见社区共同整理的
国产开源项目对比
表格。
后端项目
项目
Star
简介
ruoyi-vue-pro
基于 Spring Boot 多模块架构
yudao-cloud
基于 Spring Cloud 微服务架构
Spring-Boot-Labs
系统学习 Spring Boot & Cloud 专栏
前端项目
项目
Star
简介
yudao-ui-admin-vue3
基于 Vue3 + element-plus 实现的管理后台
yudao-ui-admin-vben
基于 Vue3 + vben(ant-design-vue) 实现的管理后台
yudao-mall-uniapp
基于 uni-app 实现的商城小程序
yudao-ui-admin-vue2
基于 Vue2 + element-ui 实现的管理后台
yudao-ui-admin-uniapp
基于 Vue2 + element-ui 实现的管理后台
yudao-ui-go-view
基于 Vue3 + naive-ui 实现的大屏报表
😎 开源协议
为什么推荐使用本项目？
① 本项目采用比 Apache 2.0 更宽松的
MIT License
开源协议，个人与企业可 100% 免费使用，不用保留类作者、Copyright 信息。
② 代码全部开源，不会像其他项目一样，只开源部分代码，让你无法了解整个项目的架构设计。
国产开源项目对比
③ 代码整洁、架构整洁，遵循《阿里巴巴 Java 开发手册》规范，代码注释详细，113770 行 Java 代码，42462 行代码注释。
🤝 项目外包
我们也是接外包滴，如果你有项目想要外包，可以微信联系【
Aix9975
】。
团队包含专业的项目经理、架构师、前端工程师、后端工程师、测试工程师、运维工程师，可以提供全流程的外包服务。
项目可以是商城、SCRM 系统、OA 系统、物流系统、ERP 系统、CMS 系统、HIS 系统、支付系统、IM 聊天、微信公众号、微信小程序等等。
🐼 内置功能
系统内置多种多种业务功能，可以用于快速你的业务系统：
通用模块（必选）：系统功能、基础设施
通用模块（可选）：工作流程、支付系统、数据报表、会员中心
业务系统（按需）：ERP 系统、CRM 系统、商城系统、微信公众号、AI 大模型
友情提示：本项目基于 RuoYi-Vue 修改，
重构优化
后端的代码，
美化
前端的界面。
额外新增的功能，我们使用 🚀 标记。
重新实现的功能，我们使用 ⭐️ 标记。
🙂 所有功能，都通过
单元测试
保证高质量。
系统功能
功能
描述
用户管理
用户是系统操作者，该功能主要完成系统用户配置
⭐️
在线用户
当前系统中活跃用户状态监控，支持手动踢下线
角色管理
角色菜单权限分配、设置角色按机构进行数据范围权限划分
菜单管理
配置系统菜单、操作权限、按钮权限标识等，本地缓存提供性能
部门管理
配置系统组织机构（公司、部门、小组），树结构展现支持数据权限
岗位管理
配置系统用户所属担任职务
🚀
租户管理
配置系统租户，支持 SaaS 场景下的多租户功能
🚀
租户套餐
配置租户套餐，自定每个租户的菜单、操作、按钮的权限
字典管理
对系统中经常使用的一些较为固定的数据进行维护
🚀
短信管理
短信渠道、短息模板、短信日志，对接阿里云、腾讯云等主流短信平台
🚀
邮件管理
邮箱账号、邮件模版、邮件发送日志，支持所有邮件平台
🚀
站内信
系统内的消息通知，提供站内信模版、站内信消息
🚀
操作日志
系统正常操作日志记录和查询，集成 Swagger 生成日志内容
⭐️
登录日志
系统登录日志记录查询，包含登录异常
🚀
错误码管理
系统所有错误码的管理，可在线修改错误提示，无需重启服务
通知公告
系统通知公告信息发布维护
🚀
敏感词
配置系统敏感词，支持标签分组
🚀
应用管理
管理 SSO 单点登录的应用，支持多种 OAuth2 授权方式
🚀
地区管理
展示省份、城市、区镇等城市信息，支持 IP 对应城市
工作流程
基于 Flowable 构建，可支持信创（国产）数据库，满足中国特色流程操作：
BPMN 设计器
钉钉/飞书设计器
历经头部企业生产验证，工作流引擎须标配仿钉钉/飞书 + BPMN 双设计器！！！
前者支持轻量配置简单流程，后者实现复杂场景深度编排
功能列表
功能描述
是否完成
SIMPLE 设计器
仿钉钉/飞书设计器，支持拖拽搭建表单流程，10 分钟快速完成审批流程配置
✅
BPMN 设计器
基于 BPMN 标准开发，适配复杂业务场景，满足多层级审批及流程自动化需求
✅
会签
同一个审批节点设置多个人（如 A、B、C 三人，三人会同时收到待办任务），需全部同意之后，审批才可到下一审批节点
✅
或签
同一个审批节点设置多个人，任意一个人处理后，就能进入下一个节点
✅
依次审批
（顺序会签）同一个审批节点设置多个人（如 A、B、C 三人），三人按顺序依次收到待办，即 A 先审批，A 提交后 B 才能审批，需全部同意之后，审批才可到下一审批节点
✅
抄送
将审批结果通知给抄送人，同一个审批默认排重，不重复抄送给同一人
✅
驳回
（退回）将审批重置发送给某节点，重新审批。可驳回至发起人、上一节点、任意节点
✅
转办
A 转给其 B 审批，B 审批后，进入下一节点
✅
委派
A 转给其 B 审批，B 审批后，转给 A，A 继续审批后进入下一节点
✅
加签
允许当前审批人根据需要，自行增加当前节点的审批人，支持向前、向后加签
✅
减签
（取消加签）在当前审批人操作之前，减少审批人
✅
撤销
（取消流程）流程发起人，可以对流程进行撤销处理
✅
终止
系统管理员，在任意节点终止流程实例
✅
表单权限
支持拖拉拽配置表单，每个审批节点可配置只读、编辑、隐藏权限
✅
超时审批
配置超时审批时间，超时后自动触发审批通过、不通过、驳回等操作
✅
自动提醒
配置提醒时间，到达时间后自动触发短信、邮箱、站内信等通知提醒，支持自定义重复提醒频次
✅
父子流程
主流程设置子流程节点，子流程节点会自动触发子流程。子流程结束后，主流程才会执行（继续往下下执行），支持同步子流程、异步子流程
✅
条件分支
（排它分支）用于在流程中实现决策，即根据条件选择一个分支执行
✅
并行分支
允许将流程分成多条分支，不进行条件判断，所有分支都会执行
✅
包容分支
（条件分支 + 并行分支的结合体）允许基于条件选择多条分支执行，但如果没有任何一个分支满足条件，则可以选择默认分支
✅
路由分支
根据条件选择一个分支执行（重定向到指定配置节点），也可以选择默认分支执行（继续往下执行）
✅
触发节点
执行到该节点，触发 HTTP 请求、HTTP 回调、更新数据、删除数据等
✅
延迟节点
执行到该节点，审批等待一段时间再执行，支持固定时长、固定日期等
✅
拓展设置
流程前置/后置通知，节点（任务）前置、后置通知，流程报表，自动审批去重，自定流程编号、标题、摘要，流程报表等
✅
支付系统
功能
描述
🚀
应用信息
配置商户的应用信息，对接支付宝、微信等多个支付渠道
🚀
支付订单
查看用户发起的支付宝、微信等的【支付】订单
🚀
退款订单
查看用户发起的支付宝、微信等的【退款】订单
🚀
回调通知
查看支付回调业务的【支付】【退款】的通知结果
🚀
接入示例
提供接入支付系统的【支付】【退款】的功能实战
基础设施
功能
描述
🚀
代码生成
前后端代码的生成（Java、Vue、SQL、单元测试），支持 CRUD 下载
🚀
系统接口
基于 Swagger 自动生成相关的 RESTful API 接口文档
🚀
数据库文档
基于 Screw 自动生成数据库文档，支持导出 Word、HTML、MD 格式
表单构建
拖动表单元素生成相应的 HTML 代码，支持导出 JSON、Vue 文件
🚀
配置管理
对系统动态配置常用参数，支持 SpringBoot 加载
⭐️
定时任务
在线（添加、修改、删除)任务调度包含执行结果日志
🚀
文件服务
支持将文件存储到 S3（MinIO、阿里云、腾讯云、七牛云）、本地、FTP、数据库等
🚀
WebSocket
提供 WebSocket 接入示例，支持一对一、一对多发送方式
🚀
API 日志
包括 RESTful API 访问日志、异常日志两部分，方便排查 API 相关的问题
MySQL 监控
监视当前系统数据库连接池状态，可进行分析SQL找出系统性能瓶颈
Redis 监控
监控 Redis 数据库的使用情况，使用的 Redis Key 管理
🚀
消息队列
基于 Redis 实现消息队列，Stream 提供集群消费，Pub/Sub 提供广播消费
🚀
Java 监控
基于 Spring Boot Admin 实现 Java 应用的监控
🚀
链路追踪
接入 SkyWalking 组件，实现链路追踪
🚀
日志中心
接入 SkyWalking 组件，实现日志中心
🚀
服务保障
基于 Redis 实现分布式锁、幂等、限流功能，满足高并发场景
🚀
日志服务
轻量级日志中心，查看远程服务器的日志
🚀
单元测试
基于 JUnit + Mockito 实现单元测试，保证功能的正确性、代码的质量等
数据报表
功能
描述
🚀
报表设计器
支持数据报表、图形报表、打印设计等
🚀
大屏设计器
拖拽生成数据大屏，内置几十种图表组件
微信公众号
功能
描述
🚀
账号管理
配置接入的微信公众号，可支持多个公众号
🚀
数据统计
统计公众号的用户增减、累计用户、消息概况、接口分析等数据
🚀
粉丝管理
查看已关注、取关的粉丝列表，可对粉丝进行同步、打标签等操作
🚀
消息管理
查看粉丝发送的消息列表，可主动回复粉丝消息
🚀
自动回复
自动回复粉丝发送的消息，支持关注回复、消息回复、关键字回复
🚀
标签管理
对公众号的标签进行创建、查询、修改、删除等操作
🚀
菜单管理
自定义公众号的菜单，也可以从公众号同步菜单
🚀
素材管理
管理公众号的图片、语音、视频等素材，支持在线播放语音、视频
🚀
图文草稿箱
新增常用的图文素材到草稿箱，可发布到公众号
🚀
图文发表记录
查看已发布成功的图文素材，支持删除操作
商城系统
演示地址：
https://doc.iocoder.cn/mall-preview/
会员中心
功能
描述
🚀
会员管理
会员是 C 端的消费者，该功能用于会员的搜索与管理
🚀
会员标签
对会员的标签进行创建、查询、修改、删除等操作
🚀
会员等级
对会员的等级、成长值进行管理，可用于订单折扣等会员权益
🚀
会员分组
对会员进行分组，用于用户画像、内容推送等运营手段
🚀
积分签到
回馈给签到、消费等行为的积分，会员可订单抵现、积分兑换等途径消耗
ERP 系统
演示地址：
https://doc.iocoder.cn/erp-preview/
CRM 系统
演示地址：
https://doc.iocoder.cn/crm-preview/
AI 大模型
演示地址：
https://doc.iocoder.cn/ai-preview/
🐨 技术栈
模块
项目
说明
yudao-dependencies
Maven 依赖版本管理
yudao-framework
Java 框架拓展
yudao-server
管理后台 + 用户 APP 的服务端
yudao-module-system
系统功能的 Module 模块
yudao-module-member
会员中心的 Module 模块
yudao-module-infra
基础设施的 Module 模块
yudao-module-bpm
工作流程的 Module 模块
yudao-module-pay
支付系统的 Module 模块
yudao-module-mall
商城系统的 Module 模块
yudao-module-erp
ERP 系统的 Module 模块
yudao-module-crm
CRM 系统的 Module 模块
yudao-module-ai
AI 大模型的 Module 模块
yudao-module-mp
微信公众号的 Module 模块
yudao-module-report
大屏报表 Module 模块
框架
框架
说明
版本
学习指南
Spring Boot
应用开发框架
2.7.18
文档
MySQL
数据库服务器
5.7 / 8.0+
Druid
JDBC 连接池、监控组件
1.2.23
文档
MyBatis Plus
MyBatis 增强工具包
3.5.7
文档
Dynamic Datasource
动态数据源
3.6.1
文档
Redis
key-value 数据库
5.0 / 6.0 /7.0
Redisson
Redis 客户端
3.32.0
文档
Spring MVC
MVC 框架
5.3.24
文档
Spring Security
Spring 安全框架
5.7.11
文档
Hibernate Validator
参数校验组件
6.2.5
文档
Flowable
工作流引擎
6.8.0
文档
Quartz
任务调度组件
2.3.2
文档
Springdoc
Swagger 文档
1.7.0
文档
SkyWalking
分布式应用追踪系统
8.12.0
文档
Spring Boot Admin
Spring Boot 监控平台
2.7.10
文档
Jackson
JSON 工具库
2.13.5
MapStruct
Java Bean 转换
1.6.3
文档
Lombok
消除冗长的 Java 代码
1.18.34
文档
JUnit
Java 单元测试框架
5.8.2
-
Mockito
Java Mock 框架
4.8.0
-
🐷 演示图
系统功能
模块
biu
biu
biu
登录 & 首页
用户 & 应用
租户 & 套餐
-
部门 & 岗位
-
菜单 & 角色
-
审计日志
-
短信
字典 & 敏感词
错误码 & 通知
-
工作流程
模块
biu
biu
biu
流程模型
表单 & 分组
-
我的流程
待办 & 已办
OA 请假
基础设施
模块
biu
biu
biu
代码生成
-
文档
-
文件 & 配置
定时任务
-
API 日志
-
MySQL & Redis
-
监控平台
支付系统
模块
biu
biu
biu
商家 & 应用
支付 & 退款
---
数据报表
模块
biu
biu
biu
报表设计器
大屏设计器
移动端（管理后台）
biu
biu
biu
目前已经实现登录、我的、工作台、编辑资料、头像修改、密码修改、常见问题、关于我们等基础功能。
- 今日の獲得スター数: 30
- 累積スター数: 33,522

### References
- https://github.com/YunaiV/ruoyi-vue-pro
