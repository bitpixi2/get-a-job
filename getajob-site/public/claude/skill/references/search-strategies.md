# Search Strategies

## Web Search Queries

When scanning for jobs, construct searches combining role + industry + location. Run multiple queries to cover breadth.

**Query patterns (use concise queries, 1-6 words):**

- `[role] jobs [location] 2026`
- `[role] remote hiring`
- `[company] careers [role]`
- `[industry] jobs [location]`
- `hiring [role] [specific skill]`

**For Dream Companies (news and direction):**

- `[company] news [current quarter/year]`
- `[company] latest announcement`
- `[company] hiring plans`
- `[company] careers page`

## Source Priority

Prefer links from these sources when available:

1. Company careers pages directly
2. LinkedIn job postings
3. Indeed, Glassdoor
4. Industry-specific job boards (e.g., Wellfound for startups, Dribbble/Behance for design)
5. Recent news articles mentioning hiring

## Contact Discovery

When searching for contact info for a listing:

1. Check the job posting for a named recruiter or hiring manager
2. Search `[company] [role] recruiter linkedin`
3. Look for team leads in the relevant department on LinkedIn
4. Fall back to generic careers@ or jobs@ email from company website

If no contact found, leave fields blank rather than guessing.

## Location Matching

When user has conditional location preferences (e.g., "in-person if within 20 min of [zip], remote otherwise"):

1. For each listing, determine if the office location is within the user's radius
2. Mark `type` accordingly: in-person listings within radius stay as-is, distant ones only included if they offer remote/hybrid
3. Note location details in the `notes` field

## Deduplication

Before adding a listing to Job_Listings.csv:

1. Check if same company + same role title already exists
2. If duplicate, skip unless the URL is different (could be a re-post)
3. If re-posted, update the existing row's date_found
