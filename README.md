# GetAJob

AI-assisted job search Skill for Claude and OpenClaw. GetAJob helps to speed up your job search, build your dream companies list, hunt for existing listings in your preferences, and drafts your outreach.

Version 2 will introduce automation for online job application forms, Calendly scheduling, inbound call handling, and scheduled email and social media posting. The current release remains intentionally sandboxed for security and simplicity, focusing on momentum rather than full automation.

Support the project: [Buy me a coffee](https://buymeacoffee.com/hackeroos)

## Project Structure

```
getajob-site/
├── public/
│   ├── index.html
│   ├── claude/
│   │   ├── install.sh
│   │   ├── getajob-claude.zip
│   │   └── skill/
│   │       ├── SKILL.md
│   │       ├── scripts/
│   │       └── references/
│   └── openclaw/
│       ├── install.sh
│       ├── getajob-openclaw.zip
│       └── skill/
│           └── SKILL.md
└── README.md
```

## Install

Claude:
```bash
curl -fsSL https://getajob.bitpixi.com/claude/install.sh | bash
```

OpenClaw:
```bash
curl -fsSL https://getajob.bitpixi.com/openclaw/install.sh | bash
```
