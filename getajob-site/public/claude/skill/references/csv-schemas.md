# CSV Schemas

## Job_Listings.csv

Columns:

| Column | Description |
|--------|-------------|
| date_found | ISO date when listing was discovered |
| company | Company name |
| role | Job title |
| type | remote / hybrid / in-person |
| location | City, State/Country (or "Remote") |
| url | Direct link to job posting |
| contact_name | Hiring manager or recruiter name if found |
| contact_email | Contact email if found |
| contact_linkedin | LinkedIn profile URL if found |
| salary_range | Salary range if listed |
| match_score | 1-5 rating of how well it matches user preferences |
| notes | Brief notes on why this is a good match |
| status | new / reviewing / applied / interviewing / rejected / offer |

## Dream_Companies.csv

Columns:

| Column | Description |
|--------|-------------|
| company | Company name |
| industry | Industry or sector |
| why | Why this company is interesting to the user |
| careers_url | Link to careers/jobs page |
| jobs_email | General hiring or jobs@ email if found |
| contact_name | Any known contact at the company |
| contact_linkedin | LinkedIn URL of contact |
| recent_news | 2-3 sentence summary of company activity in past 3 months |
| direction | Brief summary of company trajectory and focus |
| last_updated | ISO date of last news/direction refresh |
| status | watching / reached_out / responded / interviewing |
