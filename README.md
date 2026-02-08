# GetAJob

AI-powered job search skill for Claude and OpenClaw.

Feel free to security audit the repo and install scripts before installing.

Support the project: [Donate a coffee](https://buymeacoffee.com/hackeroos)

## Project Structure

```
getajob-site/
├── public/                    # Deploy this folder
│   ├── index.html            # Landing page
│   ├── claude/
│   │   ├── install.sh        # Claude installer script
│   │   ├── get-a-job-claude.zip
│   │   └── skill/            # Claude skill files
│   │       ├── SKILL.md
│   │       ├── scripts/
│   │       └── references/
│   └── openclaw/
│       ├── install.sh        # OpenClaw installer script
│       ├── get-a-job-openclaw.zip
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
