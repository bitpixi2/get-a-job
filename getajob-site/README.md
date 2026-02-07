# GetAJob Landing Page

AI-powered job search skill for Claude.ai and OpenClaw.

## Quick Deploy to Vercel

### Option 1: Deploy from GitHub (Recommended)

1. **Create a new GitHub repo** called `getajob` (or any name)

2. **Push this code to GitHub:**
   ```bash
   cd getajob-site
   git init
   git add .
   git commit -m "Initial commit"
   git branch -M main
   git remote add origin https://github.com/YOUR_USERNAME/getajob.git
   git push -u origin main
   ```

3. **Connect to Vercel:**
   - Go to [vercel.com](https://vercel.com)
   - Click "Add New Project"
   - Import your GitHub repo
   - Framework Preset: **Other** (static site)
   - Root Directory: `public`
   - Click Deploy

4. **Add custom domain:**
   - In Vercel dashboard → Settings → Domains
   - Add `getajob.hackeroos.com.au`
   - Add the DNS records Vercel provides to your domain registrar

### Option 2: Deploy via Vercel CLI

```bash
npm i -g vercel
cd getajob-site/public
vercel --prod
```

Then add your custom domain in the Vercel dashboard.

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

## DNS Setup

If your main site (hackeroos.com.au) is on Vercel via Lovable, add these records:

| Type  | Name    | Value                          |
|-------|---------|--------------------------------|
| CNAME | getajob | cname.vercel-dns.com          |

Or use whatever Vercel tells you when you add the domain.

## Install Commands

Once deployed, users can install via:

**Claude.ai:**
```bash
curl -fsSL https://getajob.hackeroos.com.au/claude/install.sh | bash
```

**OpenClaw:**
```bash
curl -fsSL https://getajob.hackeroos.com.au/openclaw/install.sh | bash
```

## Local Development

Just open `public/index.html` in a browser, or use a local server:

```bash
cd public
python3 -m http.server 8000
# Open http://localhost:8000
```

## License

MIT
