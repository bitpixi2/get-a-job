#!/usr/bin/env python3
"""Initialize the Get a Job folder structure on the user's desktop."""

import csv
import os
import sys

def init_job_search(base_path):
    """Create the full Get a Job directory structure and empty CSV files."""
    
    folders = [
        os.path.join(base_path, "Master"),
        os.path.join(base_path, "Applications"),
        os.path.join(base_path, "Summaries"),
    ]
    
    for folder in folders:
        os.makedirs(folder, exist_ok=True)
    
    # Job Listings CSV
    listings_path = os.path.join(base_path, "Job_Listings.csv")
    if not os.path.exists(listings_path):
        with open(listings_path, "w", newline="") as f:
            writer = csv.writer(f)
            writer.writerow([
                "date_found", "company", "role", "type", "location",
                "url", "contact_name", "contact_email", "contact_linkedin",
                "salary_range", "match_score", "notes", "status"
            ])
        print(f"Created: {listings_path}")
    else:
        print(f"Exists: {listings_path}")
    
    # Dream Companies CSV
    dream_path = os.path.join(base_path, "Dream_Companies.csv")
    if not os.path.exists(dream_path):
        with open(dream_path, "w", newline="") as f:
            writer = csv.writer(f)
            writer.writerow([
                "company", "industry", "why", "careers_url", "jobs_email",
                "contact_name", "contact_linkedin", "recent_news",
                "direction", "last_updated", "status"
            ])
        print(f"Created: {dream_path}")
    else:
        print(f"Exists: {dream_path}")
    
    # Master resume placeholder
    resume_path = os.path.join(base_path, "Master", "resume.md")
    if not os.path.exists(resume_path):
        with open(resume_path, "w") as f:
            f.write("# Resume\n\n[Paste or write your master resume here]\n")
        print(f"Created: {resume_path}")
    
    # Portfolio links placeholder
    portfolio_path = os.path.join(base_path, "Master", "portfolio_links.md")
    if not os.path.exists(portfolio_path):
        with open(portfolio_path, "w") as f:
            f.write("# Portfolio & Reference Links\n\n[Add portfolio URLs, GitHub, personal site, etc.]\n")
        print(f"Created: {portfolio_path}")
    
    # Search config placeholder
    config_path = os.path.join(base_path, "search_config.csv")
    if not os.path.exists(config_path):
        with open(config_path, "w", newline="") as f:
            writer = csv.writer(f)
            writer.writerow(["field", "value"])
            writer.writerow(["roles", ""])
            writer.writerow(["industries", ""])
            writer.writerow(["locations_inperson", ""])
            writer.writerow(["remote_ok", "yes"])
            writer.writerow(["hybrid_ok", "yes"])
            writer.writerow(["location_exception", ""])
            writer.writerow(["salary_min", ""])
            writer.writerow(["keywords", ""])
        print(f"Created: {config_path}")
    
    print(f"\n✅ Get a Job workspace ready at: {base_path}")


if __name__ == "__main__":
    if len(sys.argv) > 1:
        base = sys.argv[1]
    else:
        base = os.path.join(os.path.expanduser("~"), "Desktop", "Get a Job")
    
    init_job_search(base)
