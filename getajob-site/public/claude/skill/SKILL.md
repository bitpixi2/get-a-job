---
name: get-a-job
description: >
  End-to-end job search assistant that helps users find, track, and apply to jobs.
  Use this skill when the user wants to: (1) set up a job search with their resume,
  preferences, target roles, industries, and location requirements, (2) scan the web
  for new job listings matching their criteria, (3) maintain a spreadsheet of active
  listings and a separate spreadsheet of dream companies they admire, (4) prepare
  tailored application materials (resume, cover letter, follow-up email) for specific
  companies, (5) get daily or weekly summaries of their job search progress, optionally
  formatted as LinkedIn or X posts. Triggers include phrases like "get a job", "job search",
  "find me jobs", "run a scan", "let's apply to [company]", "update my dream companies",
  "daily summary", "weekly recap", "set up my job search", or any request to find open
  roles, track applications, or prepare application materials.
---

# Get a Job

A structured job search workflow that organizes everything in a `Get a Job` folder on the user's desktop.

## Workspace Structure

```
Get a Job/
├── Master/
│   ├── resume.md          (master resume — the source of truth)
│   └── portfolio_links.md (portfolio URLs, GitHub, site, etc.)
├── search_config.csv      (roles, industries, locations, preferences)
├── Job_Listings.csv       (active openings found via web search)
├── Dream_Companies.csv    (aspirational companies with news + careers info)
├── Applications/
│   └── [CompanyName]/     (one folder per company applied to)
│       ├── resume_tailored.md
│       ├── cover_letter.md
│       └── followup_email.md
└── Summaries/
    ├── daily_YYYY-MM-DD.md
    └── weekly_YYYY-MM-DD.md
```

## Workflows

### 1. Setup — "Set up my job search"

Run on first use or when user wants to reconfigure.

1. Ask for resume (file upload or paste). Save to `Master/resume.md`.
2. Ask for portfolio links or references. Save to `Master/portfolio_links.md`.
3. Ask for target roles, industries, and keywords.
4. Ask for location preferences:
   - In-person locations (city, zip, country)
   - Remote OK? Hybrid OK?
   - Exceptions (e.g., "in-person if within 20 min of [zip], remote otherwise")
5. Ask for optional salary minimum.
6. Run `scripts/init_workspace.py <path>` to create the folder structure.
7. Write preferences to `search_config.csv`.

Keep questions conversational — ask the most important ones first, follow up as needed. Do not overwhelm with all questions at once.

### 2. Scan — "Run a scan" / "Find me jobs"

Batch job search the user triggers whenever they want.

1. Read `search_config.csv` for current preferences.
2. Read `Job_Listings.csv` to know what's already tracked.
3. Use web search to find new listings. See `references/search-strategies.md` for query patterns and source priority.
4. For each result, gather: company, role, type, location, URL, contact info, salary range.
5. Rate match quality 1-5 based on how well it fits user preferences.
6. Use `scripts/add_listing.py` to append new listings (handles deduplication).
7. Present a summary of new findings to the user.
8. Suggest any dream company additions based on interesting companies encountered.

Run multiple varied search queries (different role titles, industries, locations) to ensure broad coverage. Aim for 5-10 searches per scan session.

### 3. Dream Companies — "Update my dream companies"

Maintain a list of companies the user admires, even if they have no open listings.

1. Ask the user to name companies they like, use, or admire. Suggest others in their industries.
2. For each company, use web search to find:
   - Careers page URL
   - Jobs or hiring email
   - Recent news (past 3 months) — summarize in 2-3 sentences
   - Company direction and trajectory — summarize briefly
   - Any known contacts
3. Use `scripts/update_dream_company.py` to add or update entries.
4. Periodically (during scan sessions), refresh `recent_news` and `direction` for existing dream companies.

See `references/csv-schemas.md` for column definitions.

### 4. Apply — "Let's apply to [company]"

When the user is ready to apply to a specific company.

1. Read the master resume from `Master/resume.md`.
2. Read the job listing details from `Job_Listings.csv` or `Dream_Companies.csv`.
3. If needed, web search for more details about the role and company.
4. Create `Applications/[CompanyName]/` folder (underscores for spaces).
5. Generate three files per `references/application-materials.md`:
   - `resume_tailored.md` — master resume reordered and tuned for this role
   - `cover_letter.md` — professional, specific, under 400 words
   - `followup_email.md` — for sending 5-7 days post-application
6. Present the files and walk the user through suggested changes.
7. Update the listing's `status` to `applied` in the relevant CSV.

### 5. Summaries — "Daily summary" / "Weekly recap"

Generate progress reports, optionally formatted for social sharing.

1. Read `Job_Listings.csv` and `Dream_Companies.csv` for current state.
2. Compare against previous summaries in `Summaries/` to identify what's new.
3. Generate summary per `references/summary-templates.md`.
4. If user requests it, append LinkedIn and X post drafts to the summary.
5. Save to `Summaries/daily_YYYY-MM-DD.md` or `Summaries/weekly_YYYY-MM-DD.md`.

Tone: professional, forward-looking, momentum-focused. Never negative or desperate.

## Key Guidelines

- All output files are `.md` or `.csv` — no `.docx` unless explicitly requested.
- Always read the master resume before tailoring; never invent experience.
- Keep cover letters under 400 words, follow-up emails under 100 words.
- When searching, use concise 1-6 word queries for best results.
- Deduplicate listings before adding — the scripts handle this automatically.
- Leave contact fields blank rather than guessing.
- Refresh dream company news during scan sessions to keep info current.
- Respect the user's location preferences including conditional rules.
