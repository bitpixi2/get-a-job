#!/usr/bin/env python3
"""Add or update a dream company in Dream_Companies.csv."""

import csv
import os
import sys
import json


FIELDNAMES = [
    "company", "industry", "why", "careers_url", "jobs_email",
    "contact_name", "contact_linkedin", "recent_news",
    "direction", "last_updated", "status"
]


def load_all(csv_path):
    """Load all dream companies."""
    rows = []
    if os.path.exists(csv_path):
        with open(csv_path, "r") as f:
            reader = csv.DictReader(f)
            for row in reader:
                rows.append(row)
    return rows


def save_all(csv_path, rows):
    """Rewrite the full CSV."""
    with open(csv_path, "w", newline="") as f:
        writer = csv.DictWriter(f, fieldnames=FIELDNAMES)
        writer.writeheader()
        for row in rows:
            writer.writerow({k: row.get(k, "") for k in FIELDNAMES})


def upsert_company(csv_path, company_dict):
    """Add or update a dream company. Updates if company name matches."""
    rows = load_all(csv_path)
    name = company_dict.get("company", "").lower().strip()
    
    updated = False
    for i, row in enumerate(rows):
        if row.get("company", "").lower().strip() == name:
            # Update existing — merge non-empty fields
            for k in FIELDNAMES:
                if company_dict.get(k):
                    rows[i][k] = company_dict[k]
            updated = True
            print(f"🔄 Updated: {company_dict.get('company')}")
            break
    
    if not updated:
        row = {k: company_dict.get(k, "") for k in FIELDNAMES}
        if not row.get("status"):
            row["status"] = "watching"
        rows.append(row)
        print(f"✅ Added: {company_dict.get('company')}")
    
    save_all(csv_path, rows)


def upsert_batch(csv_path, companies_json_str):
    """Add/update multiple companies from a JSON array string."""
    companies = json.loads(companies_json_str)
    for company in companies:
        upsert_company(csv_path, company)


if __name__ == "__main__":
    if len(sys.argv) < 3:
        print("Usage: python update_dream_company.py <csv_path> '<json_array>'")
        sys.exit(1)
    
    upsert_batch(sys.argv[1], sys.argv[2])
