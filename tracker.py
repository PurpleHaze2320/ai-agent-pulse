"""
AI Agent Framework Pulse Tracker
Collects GitHub metrics for AI agent frameworks and computes health/momentum scores.
"""

import json
import os
import sys
import time
from datetime import datetime, timezone, timedelta
from pathlib import Path

import requests
import yaml


DATA_DIR = Path(__file__).parent / "data"
CONFIG_PATH = Path(__file__).parent / "config.yaml"

GITHUB_API = "https://api.github.com"
HEADERS = {"Accept": "application/vnd.github+json"}


def load_config():
    with open(CONFIG_PATH) as f:
        return yaml.safe_load(f)


def gh_get(endpoint: str, params: dict = None) -> dict | list | None:
    """Make a GitHub API request with optional token auth and rate-limit handling."""
    token = os.environ.get("GITHUB_TOKEN", "")
    headers = {**HEADERS}
    if token:
        headers["Authorization"] = f"Bearer {token}"

    url = f"{GITHUB_API}{endpoint}" if endpoint.startswith("/") else endpoint
    resp = requests.get(url, headers=headers, params=params, timeout=30)

    if resp.status_code == 403 and "rate limit" in resp.text.lower():
        reset = int(resp.headers.get("X-RateLimit-Reset", time.time() + 60))
        wait = max(reset - int(time.time()), 1)
        print(f"  ⏳ Rate limited. Waiting {wait}s...")
        time.sleep(min(wait, 120))
        return gh_get(endpoint, params)

    if resp.status_code == 404:
        return None

    resp.raise_for_status()
    return resp.json()


def fetch_repo_info(owner_repo: str) -> dict | None:
    """Fetch basic repository information."""
    data = gh_get(f"/repos/{owner_repo}")
    if not data:
        return None
    return {
        "stars": data.get("stargazers_count", 0),
        "forks": data.get("forks_count", 0),
        "open_issues": data.get("open_issues_count", 0),
        "watchers": data.get("subscribers_count", 0),
        "language": data.get("language", "Unknown"),
        "license": (data.get("license") or {}).get("spdx_id", "Unknown"),
        "created_at": data.get("created_at", ""),
        "pushed_at": data.get("pushed_at", ""),
        "description": data.get("description", ""),
        "archived": data.get("archived", False),
        "default_branch": data.get("default_branch", "main"),
    }


def fetch_releases(owner_repo: str, limit: int = 5) -> list[dict]:
    """Fetch recent releases."""
    data = gh_get(f"/repos/{owner_repo}/releases", {"per_page": limit})
    if not data:
        return []
    releases = []
    for r in data:
        releases.append({
            "tag": r.get("tag_name", ""),
            "name": r.get("name", ""),
            "published_at": r.get("published_at", ""),
            "prerelease": r.get("prerelease", False),
        })
    return releases


def fetch_commit_activity(owner_repo: str) -> dict:
    """Fetch commit activity for the last year (weekly buckets)."""
    data = gh_get(f"/repos/{owner_repo}/stats/commit_activity")
    if not data or not isinstance(data, list):
        return {"total_last_4w": 0, "total_last_12w": 0, "weekly": []}

    recent_4w = sum(w.get("total", 0) for w in data[-4:])
    recent_12w = sum(w.get("total", 0) for w in data[-12:])
    weekly = [{"week": w.get("week", 0), "total": w.get("total", 0)} for w in data[-12:]]

    return {"total_last_4w": recent_4w, "total_last_12w": recent_12w, "weekly": weekly}


def fetch_contributors_count(owner_repo: str) -> int:
    """Fetch approximate contributor count using pagination trick."""
    token = os.environ.get("GITHUB_TOKEN", "")
    headers = {**HEADERS}
    if token:
        headers["Authorization"] = f"Bearer {token}"

    resp = requests.get(
        f"{GITHUB_API}/repos/{owner_repo}/contributors",
        headers=headers,
        params={"per_page": 1, "anon": "false"},
        timeout=30,
    )
    if resp.status_code != 200:
        return 0

    # GitHub returns the total count in the Link header's last page
    link = resp.headers.get("Link", "")
    if 'rel="last"' in link:
        import re
        match = re.search(r'page=(\d+)>; rel="last"', link)
        if match:
            return int(match.group(1))
    return len(resp.json()) if resp.json() else 0


def fetch_issues_stats(owner_repo: str) -> dict:
    """Fetch open vs closed issue counts."""
    open_data = gh_get(f"/search/issues", {
        "q": f"repo:{owner_repo} is:issue is:open",
        "per_page": 1,
    })
    closed_data = gh_get(f"/search/issues", {
        "q": f"repo:{owner_repo} is:issue is:closed",
        "per_page": 1,
    })

    open_count = open_data.get("total_count", 0) if open_data else 0
    closed_count = closed_data.get("total_count", 0) if closed_data else 0
    total = open_count + closed_count

    return {
        "open": open_count,
        "closed": closed_count,
        "close_ratio": round(closed_count / total, 3) if total > 0 else 0,
    }


def compute_pulse_score(metrics: dict, weights: dict) -> dict:
    """
    Compute a 0-100 Pulse Score based on weighted metrics.
    Returns the score and component breakdowns.
    """
    now = datetime.now(timezone.utc)

    # --- Star velocity (normalized to 0-100) ---
    stars = metrics.get("stars", 0)
    history = metrics.get("_history", {})
    stars_7d_ago = history.get("stars_7d_ago", stars)
    stars_30d_ago = history.get("stars_30d_ago", stars)
    velocity_7d = stars - stars_7d_ago
    velocity_30d = stars - stars_30d_ago
    # Normalize: gaining 500+ stars/week is exceptional (100), 0 is 0
    star_score = min(100, (velocity_7d / 500) * 70 + (velocity_30d / 2000) * 30)
    star_score = max(0, star_score)

    # --- Release freshness (days since last release) ---
    releases = metrics.get("releases", [])
    if releases and releases[0].get("published_at"):
        last_release = datetime.fromisoformat(releases[0]["published_at"].replace("Z", "+00:00"))
        days_since = (now - last_release).days
        release_score = max(0, 100 - (days_since / 3))  # 0 after ~300 days
    else:
        release_score = 0

    # --- Issue health ---
    issue_ratio = metrics.get("issues", {}).get("close_ratio", 0)
    issue_score = issue_ratio * 100

    # --- Commit activity ---
    commits_4w = metrics.get("commit_activity", {}).get("total_last_4w", 0)
    # 100+ commits in 4 weeks is very healthy
    commit_score = min(100, (commits_4w / 100) * 100)

    # --- Community (contributors) ---
    contributors = metrics.get("contributors", 0)
    # 500+ contributors is exceptional
    community_score = min(100, (contributors / 500) * 100)

    # --- Fork ratio ---
    forks = metrics.get("forks", 0)
    if stars > 0:
        fork_ratio = forks / stars
        # 0.15-0.25 is healthy engagement
        fork_score = min(100, (fork_ratio / 0.25) * 100)
    else:
        fork_score = 0

    # Weighted composite
    w = weights
    pulse = (
        star_score * w.get("star_velocity_weight", 0.25)
        + release_score * w.get("release_freshness_weight", 0.20)
        + issue_score * w.get("issue_health_weight", 0.15)
        + commit_score * w.get("commit_activity_weight", 0.20)
        + community_score * w.get("community_weight", 0.10)
        + fork_score * w.get("fork_ratio_weight", 0.10)
    )

    return {
        "pulse_score": round(pulse, 1),
        "components": {
            "star_velocity": round(star_score, 1),
            "release_freshness": round(release_score, 1),
            "issue_health": round(issue_score, 1),
            "commit_activity": round(commit_score, 1),
            "community": round(community_score, 1),
            "fork_ratio": round(fork_score, 1),
        },
        "star_velocity_7d": velocity_7d,
        "star_velocity_30d": velocity_30d,
    }


def load_history() -> dict:
    """Load historical snapshot data."""
    history_file = DATA_DIR / "history.json"
    if history_file.exists():
        with open(history_file) as f:
            return json.load(f)
    return {}


def save_history(history: dict):
    """Save historical snapshot data."""
    DATA_DIR.mkdir(parents=True, exist_ok=True)
    with open(DATA_DIR / "history.json", "w") as f:
        json.dump(history, f, indent=2, default=str)


def get_historical_stars(history: dict, repo: str, days_ago: int) -> int | None:
    """Look up star count from N days ago in history."""
    target = datetime.now(timezone.utc) - timedelta(days=days_ago)
    snapshots = history.get(repo, [])

    closest = None
    closest_diff = float("inf")
    for snap in snapshots:
        snap_date = datetime.fromisoformat(snap["timestamp"])
        diff = abs((snap_date - target).total_seconds())
        if diff < closest_diff:
            closest_diff = diff
            closest = snap

    if closest and closest_diff < 86400 * (days_ago + 2):  # Allow some tolerance
        return closest.get("stars", None)
    return None


def track_all(config: dict) -> dict:
    """Run the full tracking cycle for all configured frameworks."""
    frameworks = config["frameworks"]
    weights = config.get("scoring", {})
    history = load_history()
    now = datetime.now(timezone.utc).isoformat()

    results = {}
    total = len(frameworks)

    for i, fw in enumerate(frameworks, 1):
        name = fw["name"]
        repo = fw["repo"]
        print(f"[{i}/{total}] Tracking {name} ({repo})...")

        try:
            info = fetch_repo_info(repo)
            if not info:
                print(f"  ⚠️  Repo not found: {repo}")
                results[name] = {"error": "repo_not_found", "repo": repo}
                continue

            releases = fetch_releases(repo)
            commit_activity = fetch_commit_activity(repo)
            contributors = fetch_contributors_count(repo)
            issues = fetch_issues_stats(repo)

            metrics = {
                **info,
                "repo": repo,
                "name": name,
                "category": fw.get("category", "unknown"),
                "releases": releases,
                "commit_activity": commit_activity,
                "contributors": contributors,
                "issues": issues,
                "tracked_at": now,
                "_history": {
                    "stars_7d_ago": get_historical_stars(history, repo, 7) or info["stars"],
                    "stars_30d_ago": get_historical_stars(history, repo, 30) or info["stars"],
                },
            }

            score_data = compute_pulse_score(metrics, weights)
            metrics["pulse"] = score_data
            del metrics["_history"]

            results[name] = metrics

            # Append to history
            if repo not in history:
                history[repo] = []
            history[repo].append({
                "timestamp": now,
                "stars": info["stars"],
                "forks": info["forks"],
                "open_issues": info["open_issues"],
                "contributors": contributors,
            })

            # Keep only 90 days of history
            cutoff = (datetime.now(timezone.utc) - timedelta(days=90)).isoformat()
            history[repo] = [s for s in history[repo] if s["timestamp"] >= cutoff]

            print(f"  ✅ {name}: ⭐ {info['stars']:,} | Pulse: {score_data['pulse_score']}")

        except Exception as e:
            print(f"  ❌ Error tracking {name}: {e}")
            results[name] = {"error": str(e), "repo": repo}

        # Be nice to the API
        time.sleep(0.5)

    save_history(history)

    # Save latest snapshot
    DATA_DIR.mkdir(parents=True, exist_ok=True)
    with open(DATA_DIR / "latest.json", "w") as f:
        json.dump(results, f, indent=2, default=str)

    print(f"\n📊 Tracking complete. {len([r for r in results.values() if 'error' not in r])}/{total} frameworks tracked.")
    return results


def main():
    config = load_config()
    results = track_all(config)
    return results


if __name__ == "__main__":
    main()
