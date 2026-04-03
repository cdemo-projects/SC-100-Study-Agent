# 📋 Changelog

All notable changes to the SC-100 Study Agent.

## [1.1.0] - 2026-04-03

### ✨ Improved
- Replaced role framing with explicit task + success criteria
- Added "Does NOT Sound Like" anti-pattern section (7 patterns to avoid)
- Added rule enforcement: agent stops and flags if about to break a non-negotiable standard
- Teach mode now asks clarifying questions before broad topics
- First interaction confirms alignment before starting work
- Added reference examples for teaching responses, quiz feedback, and study plans

## [1.0.0] - 2026-04-02

### 🚀 Initial Release
- SC-100 Study Coach agent with 6 study modes (Teach, Quiz, Study Plan, Skill Gaps Tracker, Practice Question Review, MS Learn Navigation Coach)
- Learning profile interview (optional, adapts teaching to how you learn)
- Agent Identity with 9 non-negotiable standards (accuracy, in-line references, no guessing, challenge thinking, welcome pushback, teach the why, architecture decisions, no fluff, expand on demand)
- Full SC-100 exam structure (April 2026, 4 domains, all objectives)
- Question Design Standard (5 question types, 3 difficulty levels, case study mode, grounding in MCP sources)
- MS Learn Search Strategy with exam day tips and landing pages by domain
- Full source transparency with grounded sources list (11 Microsoft sources, 2 YouTube references)
- MCP server setup instructions (Microsoft Learn, Context7, Azure MCP)
- Interactive dashboard with 9 tabs (Overview, Quiz, Skill Gaps Map, Quiz History, Study Plan, Transcripts, Bookmarks, Timer, References, Feedback)
- Dashboard quiz with clickable answers, Mermaid diagram support, product icons, and configurable question count
- Question bank loaded from `question-bank.json` (grows with every study session)
- 28 timestamped video transcripts (27 SC-100 course playlist + John Savill's Study Cram), fully searchable
- Study progress tracking via `study-progress.json`
- GitHub Issue templates (bug report, feature request)
- Feedback tab in dashboard
- MIT License
