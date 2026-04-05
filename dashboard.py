"""
Dashboard Generator for AI Agent Framework Pulse Tracker
Generates a README.md with live metrics, charts (as SVG), and trend data.
"""

import json
import math
from datetime import datetime, timezone
from pathlib import Path

import yaml

DATA_DIR = Path(__file__).parent / "data"
CONFIG_PATH = Path(__file__).parent / "config.yaml"
README_PATH = Path(__file__).parent / "README.md"
CHARTS_DIR = Path(__file__).parent / "charts"


def load_latest() -> dict:
    with open(DATA_DIR / "latest.json") as f:
        return json.load(f)


def load_history() -> dict:
    history_file = DATA_DIR / "history.json"
    if history_file.exists():
        with open(history_file) as f:
            return json.load(f)
    return {}


def load_config() -> dict:
    with open(CONFIG_PATH) as f:
        return yaml.safe_load(f)


def pulse_emoji(score: float) -> str:
    if score >= 70:
        return "🟢"
    elif score >= 40:
        return "🟡"
    elif score >= 20:
        return "🟠"
    return "🔴"


def trend_arrow(velocity_7d: int) -> str:
    if velocity_7d > 100:
        return "🚀"
    elif velocity_7d > 20:
        return "📈"
    elif velocity_7d > 0:
        return "↗️"
    elif velocity_7d == 0:
        return "➡️"
    else:
        return "📉"


def format_number(n: int) -> str:
    if n >= 1_000_000:
        return f"{n / 1_000_000:.1f}M"
    if n >= 1_000:
        return f"{n / 1_000:.1f}k"
    return str(n)


def days_ago_text(iso_date: str) -> str:
    if not iso_date:
        return "N/A"
    try:
        dt = datetime.fromisoformat(iso_date.replace("Z", "+00:00"))
        days = (datetime.now(timezone.utc) - dt).days
        if days == 0:
            return "today"
        if days == 1:
            return "1 day ago"
        if days < 30:
            return f"{days} days ago"
        if days < 365:
            months = days // 30
            return f"{months} mo ago"
        return f"{days // 365}y ago"
    except Exception:
        return "N/A"


def generate_sparkline_svg(data_points: list[int], width: int = 120, height: int = 30, color: str = "#4CAF50") -> str:
    """Generate an inline SVG sparkline."""
    if not data_points or len(data_points) < 2:
        return ""

    min_val = min(data_points)
    max_val = max(data_points)
    val_range = max_val - min_val or 1

    points = []
    step = width / (len(data_points) - 1)
    for i, val in enumerate(data_points):
        x = round(i * step, 1)
        y = round(height - ((val - min_val) / val_range) * (height - 4) - 2, 1)
        points.append(f"{x},{y}")

    polyline = " ".join(points)
    return (
        f'<svg width="{width}" height="{height}" xmlns="http://www.w3.org/2000/svg">'
        f'<polyline points="{polyline}" fill="none" stroke="{color}" stroke-width="2" stroke-linecap="round" stroke-linejoin="round"/>'
        f"</svg>"
    )


def generate_bar_chart_svg(items: list[tuple[str, float]], title: str, width: int = 700, bar_height: int = 28, color: str = "#4CAF50") -> str:
    """Generate an SVG horizontal bar chart."""
    if not items:
        return ""

    padding_left = 160
    padding_right = 60
    padding_top = 40
    bar_gap = 6
    chart_width = width - padding_left - padding_right
    total_height = padding_top + len(items) * (bar_height + bar_gap) + 20

    max_val = max(v for _, v in items) or 1

    svg_parts = [
        f'<svg width="{width}" height="{total_height}" xmlns="http://www.w3.org/2000/svg">',
        f'<style>text {{ font-family: -apple-system, BlinkMacSystemFont, "Segoe UI", Helvetica, Arial, sans-serif; }}</style>',
        f'<text x="{width // 2}" y="24" text-anchor="middle" font-size="14" font-weight="bold" fill="#24292f">{title}</text>',
    ]

    for i, (label, value) in enumerate(items):
        y = padding_top + i * (bar_height + bar_gap)
        bar_w = max(2, (value / max_val) * chart_width)

        # Gradient color based on value
        ratio = value / max_val
        r = int(255 * (1 - ratio) + 76 * ratio)
        g = int(200 * (1 - ratio) + 175 * ratio)
        b = int(200 * (1 - ratio) + 80 * ratio)
        bar_color = f"#{r:02x}{g:02x}{b:02x}"

        svg_parts.append(
            f'<text x="{padding_left - 8}" y="{y + bar_height // 2 + 5}" text-anchor="end" font-size="12" fill="#57606a">{label}</text>'
        )
        svg_parts.append(
            f'<rect x="{padding_left}" y="{y}" width="{bar_w:.1f}" height="{bar_height}" rx="4" fill="{bar_color}" opacity="0.85"/>'
        )
        svg_parts.append(
            f'<text x="{padding_left + bar_w + 6}" y="{y + bar_height // 2 + 5}" font-size="11" fill="#24292f">{value:.1f}</text>'
        )

    svg_parts.append("</svg>")
    return "\n".join(svg_parts)


def generate_star_history_svg(history: dict, frameworks: list[dict], width: int = 700, height: int = 400) -> str:
    """Generate an SVG line chart of star growth over time for top frameworks."""
    colors = [
        "#4CAF50", "#2196F3", "#FF9800", "#E91E63", "#9C27B0",
        "#00BCD4", "#FF5722", "#795548", "#607D8B", "#CDDC39",
    ]

    # Collect data for top frameworks by current stars
    chart_data = []
    for fw in frameworks[:10]:
        repo = fw["repo"]
        snapshots = history.get(repo, [])
        if len(snapshots) >= 2:
            points = [(s["timestamp"], s["stars"]) for s in snapshots]
            points.sort()
            chart_data.append((fw["name"], points))

    if not chart_data:
        return ""

    padding = {"top": 50, "right": 150, "bottom": 40, "left": 70}
    plot_w = width - padding["left"] - padding["right"]
    plot_h = height - padding["top"] - padding["bottom"]

    # Find time and value ranges
    all_times = []
    all_vals = []
    for _, points in chart_data:
        for t, v in points:
            all_times.append(datetime.fromisoformat(t))
            all_vals.append(v)

    if not all_times:
        return ""

    t_min = min(all_times)
    t_max = max(all_times)
    v_min = min(all_vals) * 0.95
    v_max = max(all_vals) * 1.05
    t_range = max((t_max - t_min).total_seconds(), 1)
    v_range = max(v_max - v_min, 1)

    svg_parts = [
        f'<svg width="{width}" height="{height}" xmlns="http://www.w3.org/2000/svg">',
        f'<style>text {{ font-family: -apple-system, BlinkMacSystemFont, "Segoe UI", Helvetica, Arial, sans-serif; }}</style>',
        f'<text x="{width // 2}" y="24" text-anchor="middle" font-size="14" font-weight="bold" fill="#24292f">Star Growth Over Time</text>',
        # Plot area background
        f'<rect x="{padding["left"]}" y="{padding["top"]}" width="{plot_w}" height="{plot_h}" fill="#f6f8fa" rx="4"/>',
    ]

    # Grid lines
    for i in range(5):
        y = padding["top"] + (plot_h / 4) * i
        val = v_max - (v_range / 4) * i
        svg_parts.append(f'<line x1="{padding["left"]}" y1="{y}" x2="{padding["left"] + plot_w}" y2="{y}" stroke="#e1e4e8" stroke-width="1"/>')
        svg_parts.append(f'<text x="{padding["left"] - 8}" y="{y + 4}" text-anchor="end" font-size="10" fill="#57606a">{format_number(int(val))}</text>')

    # Draw lines
    for idx, (name, points) in enumerate(chart_data):
        color = colors[idx % len(colors)]
        path_parts = []
        last_x, last_y = 0, 0
        for j, (t, v) in enumerate(points):
            dt = datetime.fromisoformat(t)
            x = padding["left"] + ((dt - t_min).total_seconds() / t_range) * plot_w
            y = padding["top"] + plot_h - ((v - v_min) / v_range) * plot_h
            if j == 0:
                path_parts.append(f"M{x:.1f},{y:.1f}")
            else:
                path_parts.append(f"L{x:.1f},{y:.1f}")
            last_x, last_y = x, y

        svg_parts.append(f'<path d="{" ".join(path_parts)}" fill="none" stroke="{color}" stroke-width="2" stroke-linecap="round"/>')
        # Legend entry
        legend_y = padding["top"] + 16 + idx * 18
        lx = padding["left"] + plot_w + 12
        svg_parts.append(f'<rect x="{lx}" y="{legend_y - 6}" width="12" height="12" rx="2" fill="{color}"/>')
        svg_parts.append(f'<text x="{lx + 16}" y="{legend_y + 4}" font-size="10" fill="#24292f">{name}</text>')

    svg_parts.append("</svg>")
    return "\n".join(svg_parts)


def generate_readme(data: dict, history: dict, config: dict) -> str:
    """Generate the full README.md dashboard."""
    now = datetime.now(timezone.utc).strftime("%Y-%m-%d %H:%M UTC")
    frameworks = config["frameworks"]

    # Sort by pulse score
    scored = []
    for fw in frameworks:
        name = fw["name"]
        if name in data and "error" not in data[name]:
            d = data[name]
            scored.append({**d, "config": fw})

    scored.sort(key=lambda x: x.get("pulse", {}).get("pulse_score", 0), reverse=True)

    lines = [
        "# 🔬 AI Agent Framework Pulse Tracker",
        "",
        "[![Daily Update](https://github.com/PurpleHaze2320/ai-agent-pulse/actions/workflows/track.yml/badge.svg)](https://github.com/PurpleHaze2320/ai-agent-pulse/actions/workflows/track.yml)",
        f"[![Frameworks Tracked](https://img.shields.io/badge/frameworks-{len(scored)}-blue)](https://github.com/PurpleHaze2320/ai-agent-pulse)",
        "[![License: MIT](https://img.shields.io/badge/License-MIT-green.svg)](https://opensource.org/licenses/MIT)",
        "[![GitHub stars](https://img.shields.io/github/stars/PurpleHaze2320/ai-agent-pulse?style=social)](https://github.com/PurpleHaze2320/ai-agent-pulse/stargazers)",
        "",
        "> Automated daily tracking of the AI agent framework ecosystem's health, momentum, and trends.",
        f"> Last updated: **{now}** | Tracking **{len(scored)}** frameworks",
        "",
        "## How It Works",
        "",
        "This bot runs daily via GitHub Actions and collects metrics from the GitHub API for the most important",
        "AI agent frameworks. It computes a **Pulse Score** (0-100) based on six weighted signals: star velocity,",
        "release freshness, issue health, commit activity, community size, and fork engagement. The result is",
        "a living dashboard that shows which frameworks are gaining momentum and which are losing steam.",
        "",
    ]

    # --- Leaderboard Table ---
    lines += [
        "## 🏆 Pulse Leaderboard",
        "",
        "| Rank | Framework | Pulse | Stars | ⭐ 7d | Commits (4w) | Last Release | Category |",
        "|------|-----------|-------|-------|-------|--------------|--------------|----------|",
    ]

    for i, fw in enumerate(scored, 1):
        p = fw.get("pulse", {})
        score = p.get("pulse_score", 0)
        emoji = pulse_emoji(score)
        v7 = p.get("star_velocity_7d", 0)
        trend = trend_arrow(v7)
        stars = format_number(fw.get("stars", 0))
        commits = fw.get("commit_activity", {}).get("total_last_4w", 0)
        releases = fw.get("releases", [])
        last_rel = days_ago_text(releases[0]["published_at"]) if releases else "—"
        cat = fw.get("category", "")
        repo = fw.get("repo", "")
        lines.append(
            f"| {i} | [{fw['name']}](https://github.com/{repo}) | {emoji} **{score}** | {stars} | {trend} +{v7} | {commits} | {last_rel} | `{cat}` |"
        )

    lines += [""]

    # --- Category Breakdown ---
    categories = {}
    for fw in scored:
        cat = fw.get("category", "other")
        if cat not in categories:
            categories[cat] = []
        categories[cat].append(fw)

    lines += [
        "## 📂 By Category",
        "",
    ]
    for cat, fws in sorted(categories.items()):
        names = ", ".join(f"**{f['name']}** ({f.get('pulse', {}).get('pulse_score', 0)})" for f in fws)
        lines.append(f"- `{cat}`: {names}")

    lines += [""]

    # --- Score Breakdown for Top 5 ---
    lines += [
        "## 🔍 Top 5 — Score Breakdown",
        "",
        "| Framework | Star Velocity | Release Freshness | Issue Health | Commit Activity | Community | Fork Ratio |",
        "|-----------|:---:|:---:|:---:|:---:|:---:|:---:|",
    ]

    for fw in scored[:5]:
        c = fw.get("pulse", {}).get("components", {})
        lines.append(
            f"| **{fw['name']}** | {c.get('star_velocity', 0)} | {c.get('release_freshness', 0)} | {c.get('issue_health', 0)} | {c.get('commit_activity', 0)} | {c.get('community', 0)} | {c.get('fork_ratio', 0)} |"
        )

    lines += [""]

    # --- Key Insights ---
    lines += ["## 💡 Key Insights", ""]

    if scored:
        top = scored[0]
        lines.append(f"- **Hottest framework**: {top['name']} with a Pulse Score of {top.get('pulse', {}).get('pulse_score', 0)}")

    fastest_growing = max(scored, key=lambda x: x.get("pulse", {}).get("star_velocity_7d", 0))
    if fastest_growing.get("pulse", {}).get("star_velocity_7d", 0) > 0:
        lines.append(f"- **Fastest growing**: {fastest_growing['name']} gained +{fastest_growing['pulse']['star_velocity_7d']} stars this week")

    most_active = max(scored, key=lambda x: x.get("commit_activity", {}).get("total_last_4w", 0))
    lines.append(f"- **Most active development**: {most_active['name']} with {most_active['commit_activity']['total_last_4w']} commits in the last 4 weeks")

    archived = [fw for fw in scored if fw.get("archived")]
    if archived:
        lines.append(f"- **⚠️ Archived**: {', '.join(f['name'] for f in archived)}")

    stale = [fw for fw in scored if fw.get("pulse", {}).get("components", {}).get("release_freshness", 0) < 10]
    if stale:
        lines.append(f"- **Stale releases**: {', '.join(f['name'] for f in stale)} haven't released in a while")

    lines += [""]

    # --- Recent Releases ---
    lines += ["## 📦 Recent Releases", ""]
    release_list = []
    for fw in scored:
        for rel in fw.get("releases", [])[:1]:
            if rel.get("published_at"):
                release_list.append((fw["name"], fw.get("repo", ""), rel))
    release_list.sort(key=lambda x: x[2]["published_at"], reverse=True)

    for name, repo, rel in release_list[:10]:
        tag = rel["tag"]
        date = days_ago_text(rel["published_at"])
        pre = " *(pre-release)*" if rel.get("prerelease") else ""
        lines.append(f"- **{name}** [`{tag}`](https://github.com/{repo}/releases/tag/{tag}) — {date}{pre}")

    lines += [""]

    # --- How to Use ---
    lines += [
        "## 🚀 Running Locally",
        "",
        "```bash",
        "# Clone the repo",
        "git clone https://github.com/YOUR_USERNAME/ai-agent-pulse.git",
        "cd ai-agent-pulse",
        "",
        "# Install dependencies",
        "pip install -r requirements.txt",
        "",
        "# Set your GitHub token (optional but recommended for higher rate limits)",
        "export GITHUB_TOKEN=ghp_your_token_here",
        "",
        "# Run the tracker",
        "python tracker.py",
        "",
        "# Generate the dashboard",
        "python dashboard.py",
        "```",
        "",
        "## 📋 Adding a Framework",
        "",
        "Edit `config.yaml` and add a new entry under `frameworks:`",
        "",
        "```yaml",
        "- name: MyFramework",
        "  repo: owner/repo-name",
        "  category: multi-agent",
        "  description: A brief description",
        "```",
        "",
        "## ⚙️ How the Pulse Score Works",
        "",
        "The Pulse Score (0–100) is a weighted composite of six signals:",
        "",
        "| Signal | Weight | What It Measures |",
        "|--------|--------|------------------|",
        "| Star Velocity | 25% | 7-day and 30-day star growth rate |",
        "| Release Freshness | 20% | Days since last release |",
        "| Commit Activity | 20% | Commits in the last 4 weeks |",
        "| Issue Health | 15% | Ratio of closed to total issues |",
        "| Community | 10% | Total number of contributors |",
        "| Fork Ratio | 10% | Forks relative to stars (engagement) |",
        "",
        "---",
        "",
        f"*Powered by GitHub Actions • Data refreshed daily • Last run: {now}*",
    ]

    return "\n".join(lines)


def build_charts(data: dict, history: dict, config: dict):
    """Generate SVG chart files."""
    CHARTS_DIR.mkdir(parents=True, exist_ok=True)

    scored = []
    for fw in config["frameworks"]:
        name = fw["name"]
        if name in data and "error" not in data[name]:
            scored.append(data[name])
    scored.sort(key=lambda x: x.get("pulse", {}).get("pulse_score", 0), reverse=True)

    # Pulse score bar chart
    items = [(fw["name"], fw["pulse"]["pulse_score"]) for fw in scored[:15]]
    svg = generate_bar_chart_svg(items, "Pulse Score — Top Frameworks")
    with open(CHARTS_DIR / "pulse_scores.svg", "w") as f:
        f.write(svg)

    # Stars bar chart
    items = [(fw["name"], fw.get("stars", 0)) for fw in sorted(scored, key=lambda x: x.get("stars", 0), reverse=True)[:15]]
    svg = generate_bar_chart_svg(items, "GitHub Stars", color="#2196F3")
    with open(CHARTS_DIR / "stars.svg", "w") as f:
        f.write(svg)

    # Commit activity bar chart
    items = [(fw["name"], fw.get("commit_activity", {}).get("total_last_4w", 0))
             for fw in sorted(scored, key=lambda x: x.get("commit_activity", {}).get("total_last_4w", 0), reverse=True)[:15]]
    svg = generate_bar_chart_svg(items, "Commits (Last 4 Weeks)", color="#FF9800")
    with open(CHARTS_DIR / "commits.svg", "w") as f:
        f.write(svg)

    # Star history line chart
    svg = generate_star_history_svg(history, config["frameworks"])
    if svg:
        with open(CHARTS_DIR / "star_history.svg", "w") as f:
            f.write(svg)

    print(f"📊 Charts saved to {CHARTS_DIR}/")


def main():
    config = load_config()
    data = load_latest()
    history = load_history()

    build_charts(data, history, config)

    readme_content = generate_readme(data, history, config)
    with open(README_PATH, "w") as f:
        f.write(readme_content)

    print(f"✅ Dashboard written to {README_PATH}")


if __name__ == "__main__":
    main()
