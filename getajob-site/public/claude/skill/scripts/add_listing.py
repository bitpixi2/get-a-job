#!/usr/bin/env python3
"""Append a job listing to Job_Listings.csv with deduplication."""

import csv
import os
import sys
import json


def load_existing(csv_path):
    """Load existing listings for dedup check."""
    existing = set()
    if os.path.exists(csv_path):
        with open(csv_path, "r") as f:
            reader = csv.DictReader(f)
            for row in reader:
                key = (row.get("company", "").lower().strip(), 
                       row.get("role", "").lower().strip())
                existing.add(key)
    return existing


def append_listing(csv_path, listing_dict):
    """Append a single listing if not duplicate. Returns True if added."""
    existing = load_existing(csv_path)
    key = (listing_dict.get("company", "").lower().strip(),
           listing_dict.get("role", "").lower().strip())
    
    if key in existing:
        print(f"⏭️  Duplicate skipped: {listing_dict.get('company')} — {listing_dict.get('role')}")
        return False
    
    fieldnames = [
        "date_found", "company", "role", "type", "location",
        "url", "contact_name", "contact_email", "contact_linkedin",
        "salary_range", "match_score", "notes", "status"
    ]
    
    with open(csv_path, "a", newline="") as f:
        writer = csv.DictWriter(f, fieldnames=fieldnames)
        row = {k: listing_dict.get(k, "") for k in fieldnames}
        if not row.get("status"):
            row["status"] = "new"
        writer.writerow(row)
    
    print(f"✅ Added: {listing_dict.get('company')} — {listing_dict.get('role')}")
    return True


def append_batch(csv_path, listings_json_str):
    """Append multiple listings from a JSON array string."""
    listings = json.loads(listings_json_str)
    added = 0
    skipped = 0
    for listing in listings:
        if append_listing(csv_path, listing):
            added += 1
        else:
            skipped += 1
    print(f"\n📊 Results: {added} added, {skipped} duplicates skipped")


if __name__ == "__main__":
    if len(sys.argv) < 3:
        print("Usage: python add_listing.py <csv_path> '<json_array>'")
        sys.exit(1)
    
    append_batch(sys.argv[1], sys.argv[2])
