#!/usr/bin/env python3
"""
Staleness check for sec-toolkit README.

Extracts every GitHub repo URL from the README, queries the GitHub API for the
last commit date on the default branch, and reports any repo that hasn't had
a commit in over 12 months.

Usage:
    python staleness-check.py README.md

Requires GITHUB_TOKEN in the environment for API rate limits.
"""

import os
import re
import sys
import json
import urllib.request
from datetime import datetime, timedelta

GITHUB_API = "https://api.github.com"
STALE_DAYS = 365


def extract_github_repos(readme_path: str) -> list[str]:
    """Return a list of 'owner/repo' strings from GitHub URLs in the README."""
    with open(readme_path, "r", encoding="utf-8") as f:
        content = f.read()
    # Match https://github.com/owner/repo (and variants with trailing paths)
    pattern = r"https?://github\.com/([A-Za-z0-9_.-]+/[A-Za-z0-9_.-]+)"
    matches = re.findall(pattern, content)
    # Deduplicate and clean up trailing slashes
    seen = set()
    repos = []
    for m in matches:
        repo = m.rstrip("/")
        if repo not in seen:
            seen.add(repo)
            repos.append(repo)
    return repos


def get_last_commit_date(owner_repo: str, token: str | None) -> datetime | None:
    """Return the date of the last commit on the default branch, or None on error."""
    url = f"{GITHUB_API}/repos/{owner_repo}/commits?per_page=1"
    req = urllib.request.Request(url)
    req.add_header("Accept", "application/vnd.github.v3+json")
    req.add_header("User-Agent", "sec-toolkit-staleness-check")
    if token:
        req.add_header("Authorization", f"token {token}")
    try:
        with urllib.request.urlopen(req, timeout=10) as resp:
            data = json.loads(resp.read().decode())
            if not data:
                return None
            date_str = data[0]["commit"]["committer"]["date"]
            return datetime.fromisoformat(date_str.replace("Z", "+00:00"))
    except Exception:
        return None


def main() -> None:
    if len(sys.argv) != 2:
        print("Usage: python staleness-check.py README.md", file=sys.stderr)
        sys.exit(1)

    readme_path = sys.argv[1]
    token = os.environ.get("GITHUB_TOKEN")
    cutoff = datetime.now(datetime.now().astimezone().tzinfo) - timedelta(days=STALE_DAYS)

    repos = extract_github_repos(readme_path)
    stale = []

    for repo in repos:
        last = get_last_commit_date(repo, token)
        if last and last < cutoff:
            stale.append((repo, last.strftime("%Y-%m-%d")))

    if stale:
        print("# Stale tools report")
        print()
        print(f"Tools with no commits in the last {STALE_DAYS} days:")
        print()
        for repo, date in stale:
            print(f"- [{repo}](https://github.com/{repo}) — last commit {date}")
    else:
        print("No stale tools found.")


if __name__ == "__main__":
    main()
