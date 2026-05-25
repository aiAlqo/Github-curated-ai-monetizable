import argparse
import csv
import os
import sys
from datetime import date
from pathlib import Path

import requests
from dotenv import load_dotenv

load_dotenv()

CSV_PATH = Path(__file__).parent / "repos.csv"
README_PATH = Path(__file__).parent / "README.md"
GH_API_BASE = "https://api.github.com/repos"
GH_HEADERS = {
    "Accept": "application/vnd.github+json",
    "X-GitHub-Api-Version": "2022-11-28",
}


def load_repos(csv_path: str) -> list[dict]:
    with open(csv_path, newline="", encoding="utf-8") as fh:
        reader = csv.DictReader(fh)
        return [row for row in reader if row["include"].strip().lower() == "yes"]


def format_stars(n: int) -> str:
    if n >= 1000:
        return f"{n / 1000:.1f}k"
    return str(n)


def build_headers(token: str | None) -> dict:
    if not token:
        return {}
    return {"Authorization": f"Bearer {token}"}


def fetch_repo_data(owner_repo: str, auth_headers: dict) -> dict | None:
    url = f"{GH_API_BASE}/{owner_repo}"
    resp = requests.get(url, headers={**GH_HEADERS, **auth_headers})
    if resp.status_code == 404:
        print(f"WARNING: {owner_repo} not found (404) — skipping.", file=sys.stderr)
        return None
    if resp.status_code == 429:
        print("Rate limit hit. Add a GITHUB_TOKEN to .env to increase the limit to 5,000 req/hr.")
        return None
    resp.raise_for_status()
    data = resp.json()
    return {"stars": data["stargazers_count"], "html_url": data["html_url"]}


def build_readme(repos: list[dict]) -> str:
    today = date.today().isoformat()
    count = len(repos)
    lines = [
        "# Open Source AI Tools to Make Money\n",
        f"> Last updated: {today} · {count} projects · [How to refresh](#refresh)\n",
        "",
        "A curated, auto-ranked list of open-source AI projects you can build a business on.",
        "Ranked by GitHub stars. Updated weekly via GitHub Actions — free to run, free to host.",
        "",
        "| # | Project | ⭐ Stars | Category | How to Make Money |",
        "|---|---------|---------|----------|-------------------|",
    ]
    for i, r in enumerate(repos):
        name = r["repo"].split("/")[1]
        row = (
            f"| {i + 1} "
            f"| [{name}]({r['html_url']}) "
            f"| {format_stars(r['stars'])} "
            f"| {r['category']} "
            f"| {r['monetization_idea']} |"
        )
        lines.append(row)

    lines += [
        "",
        "---",
        "",
        "## Refresh",
        "",
        "Run this once locally to regenerate the README with fresh star counts:",
        "",
        "```bash",
        "pip install -r requirements.txt",
        "cp .env.example .env   # paste your GitHub token (free — needs no scopes)",
        "python refresh.py",
        "```",
        "",
        "**Add a repo:**",
        "```bash",
        'python refresh.py --add owner/repo "Category" "How you would monetize it."',
        "```",
        "",
        "**Skip a repo:**",
        "```bash",
        "python refresh.py --skip owner/repo",
        "```",
        "",
        "Or just edit `repos.csv` directly — set `include` to `yes` or `no`.",
        "",
        "## Deployment (free)",
        "",
        "This README is refreshed automatically every Monday at 08:00 UTC by a GitHub Actions",
        "workflow (`.github/workflows/refresh.yml`). It uses the built-in `GITHUB_TOKEN` — no",
        "secrets to configure.",
        "",
        "To publish as a website: **Settings → Pages → Branch: main / folder: / (root)**.",
        "GitHub Pages is free for public repos.",
    ]
    return "\n".join(lines) + "\n"


def cmd_add(csv_path: str, repo: str, category: str, idea: str) -> None:
    with open(csv_path, "a", newline="", encoding="utf-8") as fh:
        writer = csv.DictWriter(
            fh, fieldnames=["repo", "include", "category", "monetization_idea"]
        )
        writer.writerow(
            {"repo": repo, "include": "yes", "category": category, "monetization_idea": idea}
        )
    print(f"Added {repo} to {csv_path}.")


def cmd_skip(csv_path: str, repo: str) -> None:
    with open(csv_path, newline="", encoding="utf-8") as fh:
        rows = list(csv.DictReader(fh))
    if not any(r["repo"] == repo for r in rows):
        print(f"WARNING: {repo} not found in CSV.")
        return
    for row in rows:
        if row["repo"] == repo:
            row["include"] = "no"
    with open(csv_path, "w", newline="", encoding="utf-8") as fh:
        writer = csv.DictWriter(
            fh, fieldnames=["repo", "include", "category", "monetization_idea"]
        )
        writer.writeheader()
        writer.writerows(rows)
    print(f"Set {repo} to include=no.")


def main() -> None:
    parser = argparse.ArgumentParser(
        description="Refresh the AI monetization README from GitHub star counts."
    )
    parser.add_argument(
        "--add",
        nargs=3,
        metavar=("REPO", "CATEGORY", "IDEA"),
        help='Add a repo: --add owner/repo "Category" "Monetization idea."',
    )
    parser.add_argument(
        "--skip",
        metavar="REPO",
        help="Exclude a repo from the list: --skip owner/repo",
    )
    args = parser.parse_args()

    csv_path = str(CSV_PATH)

    if args.add:
        cmd_add(csv_path, args.add[0], args.add[1], args.add[2])
        return

    if args.skip:
        cmd_skip(csv_path, args.skip)
        return

    token = os.getenv("GITHUB_TOKEN")
    if not token:
        print(
            "WARNING: GITHUB_TOKEN not set — using unauthenticated API (60 req/hr limit).\n"
            "Copy .env.example to .env and add a token to increase this to 5,000 req/hr."
        )
    auth_headers = build_headers(token)

    repos = load_repos(csv_path)
    enriched = []
    for row in repos:
        data = fetch_repo_data(row["repo"], auth_headers)
        if data is None:
            continue
        enriched.append({**row, **data})

    enriched.sort(key=lambda r: r["stars"], reverse=True)
    readme = build_readme(enriched)
    README_PATH.write_text(readme, encoding="utf-8")
    print(f"README.md written — {len(enriched)} projects ranked by stars.")


if __name__ == "__main__":
    main()
