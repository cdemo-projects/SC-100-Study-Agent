# 🛡️ SC-100 Study Agent

A VS Code Copilot agent for preparing for the **SC-100: Microsoft Cybersecurity Architect** certification exam.

## 🎯 What It Does

This agent helps you study for SC-100 by combining AI-powered teaching with live Microsoft documentation lookups. It adapts to how you learn through an optional interview, and teaches you how to navigate Microsoft Learn efficiently during the actual exam.

### 📚 Study Modes

| Mode | Trigger | Description |
|------|---------|-------------|
| **Teach** | Ask about any concept | Explains concepts with MS Learn references and search guidance |
| **Quiz** | "quiz me" / "test me" | Scenario-based questions matching the exam's architect-level style |
| **Study Plan** | "build a study plan" | Week-by-week schedule based on your exam date and available time |
| **Skill Gaps Tracker** | "show my skill gaps" | Gap analysis from quiz history, ranked by domain weight |
| **Practice Question Review** | "explain this question" | Breaks down why each answer is right or wrong |
| **MS Learn Navigation** | "help me search" | Teaches exact search terms and URL patterns for exam day |

### 🧠 Learning Profile

On your first interaction, the agent offers a short interview (2-3 minutes) to understand how you learn best. Your preferences are saved to `LEARNING_PROFILE.md` so every future session is tailored to you. This is optional but recommended.

### 🔍 Source Transparency

Every answer cites its source. You can ask "show me your sources" at any time to see exactly what the agent is grounded on. No mystery, no guessing.

## 📋 SC-100 Exam Domains (April 2026)

| Domain | Weight |
|--------|--------|
| Design solutions that align with security best practices and priorities | 20-25% |
| Design security operations, identity, and compliance capabilities | 25-30% |
| Design security solutions for infrastructure | 25-30% |
| Design security solutions for applications and data | 20-25% |

Passing score: **700**

## ✅ Prerequisites

- [VS Code](https://code.visualstudio.com/) with [GitHub Copilot](https://marketplace.visualstudio.com/items?itemName=GitHub.copilot) and [GitHub Copilot Chat](https://marketplace.visualstudio.com/items?itemName=GitHub.copilot-chat) extensions installed
- A GitHub Copilot subscription (individual, business, or enterprise)
- Python 3.10+ (only needed for the dashboard and transcript search)
- [Git](https://git-scm.com/) (to clone the repo)

## ⚙️ Setup

### 1. 📥 Clone the Repo

```bash
git clone https://github.com/cdemo-projects/SC-100-Study-Agent.git
cd SC-100-Study-Agent
```

Or download the ZIP from the green **Code** button on GitHub and extract it.

### 2. 📂 Install the Agent

Copy the agent file to your VS Code user prompts folder. This is what makes `@sc100-study` available in Copilot Chat.

**Windows (PowerShell):**
```powershell
# For VS Code
Copy-Item "sc100-study.agent.md" "$env:APPDATA\Code\User\prompts\"

# For VS Code Insiders
Copy-Item "sc100-study.agent.md" "$env:APPDATA\Code - Insiders\User\prompts\"
```

**macOS/Linux:**
```bash
# For VS Code
cp sc100-study.agent.md ~/.config/Code/User/prompts/

# For VS Code Insiders
cp sc100-study.agent.md ~/.config/Code\ -\ Insiders/User/prompts/
```

If the `prompts` folder doesn't exist, create it first.

### 3. 🔌 Set Up MCP Servers

These give the agent live access to Microsoft documentation. Create or edit your MCP config file:
- **Windows:** `%APPDATA%\Code\User\mcp.json` (or `Code - Insiders` for Insiders)
- **macOS/Linux:** `~/.config/Code/User/mcp.json`

```json
{
  "servers": {
    "Microsoft Learn - MCP": {
      "type": "http",
      "url": "https://learn.microsoft.com/api/mcp"
    },
    "context7": {
      "type": "http",
      "url": "https://mcp.context7.com/mcp"
    }
  }
}
```

The **Azure MCP server** is built into VS Code with the [Azure Tools extension pack](https://marketplace.visualstudio.com/items?itemName=ms-vscode.vscode-node-azure-pack).

Restart VS Code after adding the servers.

### 4. � Open the Workspace

**This step is important.** Open the cloned `SC-100-Study-Agent` folder in VS Code as your workspace:

```
File > Open Folder > select the SC-100-Study-Agent folder
```

The agent needs this folder open to:
- 📝 Save your learning profile (`LEARNING_PROFILE.md`)
- 📊 Write quiz scores and progress (`study-progress.json`)
- 🔍 Search video transcripts (`transcripts/`)
- 📚 Grow the question bank (`question-bank.json`)

Without the workspace open, the agent can still teach and quiz you, but it won't be able to save progress or search transcripts.

### 5. 🚀 Start Studying

Open VS Code Copilot Chat and type `@sc100-study` followed by your message. The agent will greet you and offer to build your learning profile.

### 📂 File Map

Here's what each file does so nothing is a mystery:

```
SC-100-Study-Agent/
├── 🤖 sc100-study.agent.md      ← The agent (copy to prompts folder)
├── 📊 dashboard.html             ← Study dashboard (run with serve.py)
├── 🐍 serve.py                   ← Dashboard server (python serve.py)
├── 📈 study-progress.json        ← Your progress data (agent writes this)
├── ❓ question-bank.json          ← Quiz questions (grows with every session)
├── 📄 README.md                   ← You are here
├── 📁 .github/
│   └── ISSUE_TEMPLATE/           ← Bug report & feature request templates
└── 🎥 transcripts/
    ├── john-savill-study-cram.txt        ← John Savill's SC-100 Study Cram
    └── playlist/                          ← 27 SC-100 course videos
        ├── 01-Course-Preview...txt
        ├── 02-Course-Intro...txt
        └── ... (27 timestamped transcripts)
```

## 💡 Usage

### 👋 First Time

When you first message `@sc100-study`, the agent will offer a short learning profile interview. This is optional but recommended. It asks about your background, how you learn, your study habits, and which SC-100 domains feel strongest or with the most gaps. Your answers are saved to `LEARNING_PROFILE.md` so every future session is personalized.

### 💬 Example Commands

| What you say | What happens |
|-------------|--------------|
| "Explain Zero Trust" | Teaches the concept, maps it to Domain 1, gives MS Learn search terms and URL |
| "Quiz me on Domain 2" | Generates scenario-based questions on security ops, identity, and compliance |
| "Quiz me" | Quizzes across all 4 domains |
| "Build a study plan" | Creates a week-by-week schedule based on your exam date and available hours |
| "show my skill gaps" | Analyzes your quiz history and ranks skill gap objectives by impact |
| "Explain this question" + paste a practice question | Breaks down what the question tests, each answer choice, and the MS Learn reference |
| "Help me search for Conditional Access" | Gives exact MS Learn search terms, URL, and navigation path for exam day |
| "Show me your sources" | Lists every source the agent is grounded on |
| "Build my learning profile" | Starts the learning profile interview (if you skipped it earlier) |
| "Test my MCP servers" | Verifies the Microsoft Learn, Context7, and Azure MCP servers are working |

### 📌 Tips

- **Every teaching response** ends with the SC-100 domain it covers, the MS Learn search terms, and a key takeaway
- **Quiz mode** tracks your score and which objectives you miss, so the Skill Gaps Tracker gets smarter over time
- **The study plan** front-loads your skill gap domains and accounts for exam weight (Domains 2 and 3 are 25-30%)
- **MS Learn navigation coaching** is built into every response, not just a separate mode. You're building exam-day search muscle memory as you study

### 6. 📊 Study Dashboard (Optional)

A visual dashboard tracks your progress, quiz scores, skill gaps, and lets you search across all 28 video transcripts.

```bash
cd sc100-study
python serve.py
```

Opens at `http://localhost:8100`. Features:

| Tab | Description |
|-----|-------------|
| **Overview** | Domain progress rings, quick stats, recent quiz results |
| **Skill Gaps Map** | Color-coded heatmap per objective (green/yellow/red/gray) |
| **Quiz History** | Full table of all quiz sessions with scores and missed objectives |
| **Study Plan** | Visual timeline with weekly milestones |
| **Transcripts** | Full-text search across 28 SC-100 video transcripts with timestamps |
| **Bookmarks** | Saved MS Learn pages tagged by domain |
| **Timer** | Session timer and total study time tracker |
| **References** | All grounded sources and key MS Learn landing pages by domain |

## 📖 Grounded Sources

### 🏢 Official Microsoft
- [SC-100 Study Guide](https://learn.microsoft.com/credentials/certifications/resources/study-guides/sc-100)
- [SC-100 Certification Page](https://learn.microsoft.com/credentials/certifications/exams/sc-100/)
- [SC-100 Learning Paths](https://learn.microsoft.com/training/paths/sc-100-design-solutions-best-practices-priorities/)
- [SC-100 Free Practice Assessment](https://learn.microsoft.com/credentials/certifications/exams/sc-100/practice/assessment?assessment-type=practice&assessmentId=87)
- [Microsoft Cybersecurity Reference Architectures (MCRA)](https://learn.microsoft.com/security/cybersecurity-reference-architecture/mcra)
- [Well-Architected Framework - Security Pillar](https://learn.microsoft.com/azure/well-architected/security/)
- [Cloud Adoption Framework - Security](https://learn.microsoft.com/azure/cloud-adoption-framework/secure/)
- [Zero Trust Guidance](https://learn.microsoft.com/security/zero-trust/)
- [Microsoft Security Blog](https://techcommunity.microsoft.com/category/security)
- [Microsoft Docs GitHub](https://github.com/MicrosoftDocs/azure-docs)
- Microsoft Learn MCP Server (live documentation lookups)

### 🗺️ Key MS Learn Landing Pages by Domain

| Domain | Landing Pages |
|--------|---------------|
| **1. Best Practices & Priorities** | [Zero Trust](https://learn.microsoft.com/security/zero-trust/), [CAF Security](https://learn.microsoft.com/azure/cloud-adoption-framework/secure/), [MCRA](https://learn.microsoft.com/security/cybersecurity-reference-architecture/) |
| **2. Security Ops & Identity** | [Sentinel](https://learn.microsoft.com/azure/sentinel/), [Entra](https://learn.microsoft.com/entra/), [Defender XDR](https://learn.microsoft.com/defender-xdr/) |
| **3. Infrastructure Security** | [Defender for Cloud](https://learn.microsoft.com/azure/defender-for-cloud/), [Azure Arc](https://learn.microsoft.com/azure/azure-arc/), [Global Secure Access](https://learn.microsoft.com/entra/global-secure-access/) |
| **4. Apps & Data Security** | [Purview](https://learn.microsoft.com/purview/), [Defender for Cloud Apps](https://learn.microsoft.com/defender-cloud-apps/), [Key Vault](https://learn.microsoft.com/azure/key-vault/) |

### 🎥 YouTube
- [SC-100 Study Playlist (27 videos)](https://www.youtube.com/playlist?list=PLahhVEj9XNTfRZMathQ5fn1akTwV7R3w_)
- [John Savill's SC-100 Study Cram](https://www.youtube.com/watch?v=2Qu5gQjNQh4)

## 💬 Feedback

Found a bug or have an idea to make this better?

- **Report a bug:** [Open a GitHub Issue](https://github.com/cdemo-projects/SC-100-Study-Agent/issues/new?template=bug_report.md)
- **Request a feature:** [Open a GitHub Issue](https://github.com/cdemo-projects/SC-100-Study-Agent/issues/new?template=feature_request.md)
- **General feedback:** Feedback form (coming soon)

The dashboard also has a **Feedback** tab with direct links to all of these.

## 📦 Requirements

- VS Code with GitHub Copilot Chat
- Microsoft Learn MCP server (required)
- Context7 MCP server (recommended)
- Azure Tools extension pack (recommended)

## 📄 License

MIT
