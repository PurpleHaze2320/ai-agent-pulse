# 🔬 AI Agent Framework Pulse Tracker

[![Daily Update](https://github.com/PurpleHaze2320/ai-agent-pulse/actions/workflows/track.yml/badge.svg)](https://github.com/PurpleHaze2320/ai-agent-pulse/actions/workflows/track.yml)
[![Frameworks Tracked](https://img.shields.io/badge/frameworks-14-blue)](https://github.com/PurpleHaze2320/ai-agent-pulse)
[![License: MIT](https://img.shields.io/badge/License-MIT-green.svg)](https://opensource.org/licenses/MIT)
[![GitHub stars](https://img.shields.io/github/stars/PurpleHaze2320/ai-agent-pulse?style=social)](https://github.com/PurpleHaze2320/ai-agent-pulse/stargazers)

> Automated daily tracking of the AI agent framework ecosystem's health, momentum, and trends.
> Last updated: **2026-05-23 08:26 UTC** | Tracking **14** frameworks

## How It Works

This bot runs daily via GitHub Actions and collects metrics from the GitHub API for the most important
AI agent frameworks. It computes a **Pulse Score** (0-100) based on six weighted signals: star velocity,
release freshness, issue health, commit activity, community size, and fork engagement. The result is
a living dashboard that shows which frameworks are gaining momentum and which are losing steam.

## 🏆 Pulse Leaderboard

| Rank | Framework | Pulse | Stars | ⭐ 7d | Commits (4w) | Last Release | Category |
|------|-----------|-------|-------|-------|--------------|--------------|----------|
| 1 | [Mastra](https://github.com/mastra-ai/mastra) | 🟢 **80.1** | 24.2k | 🚀 +293 | 1055 | 4 days ago | `typescript` |
| 2 | [CrewAI](https://github.com/crewAIInc/crewAI) | 🟢 **71.1** | 52.0k | 🚀 +499 | 0 | 1 day ago | `multi-agent` |
| 3 | [BrowserUse](https://github.com/browser-use/browser-use) | 🟡 **69.9** | 95.2k | 🚀 +1054 | 0 | 4 days ago | `web-agent` |
| 4 | [LangGraph](https://github.com/langchain-ai/langgraph) | 🟡 **68.8** | 32.7k | 🚀 +588 | 0 | today | `orchestration` |
| 5 | [Claude Agent SDK](https://github.com/anthropics/claude-code) | 🟡 **64.9** | 125.9k | 🚀 +1879 | 0 | today | `orchestration` |
| 6 | [Agno](https://github.com/agno-agi/agno) | 🟡 **54.3** | 40.3k | 🚀 +161 | 0 | 1 day ago | `multi-agent` |
| 7 | [PydanticAI](https://github.com/pydantic/pydantic-ai) | 🟡 **53.8** | 17.2k | 🚀 +139 | 0 | today | `structured` |
| 8 | [Semantic Kernel](https://github.com/microsoft/semantic-kernel) | 🟡 **50.8** | 28.0k | 📈 +49 | 0 | 9 days ago | `enterprise` |
| 9 | [Haystack](https://github.com/deepset-ai/haystack) | 🟡 **50.5** | 25.3k | 🚀 +104 | 0 | 10 days ago | `pipeline` |
| 10 | [DSPy](https://github.com/stanfordnlp/dspy) | 🟡 **49.8** | 34.6k | 🚀 +138 | 0 | 17 days ago | `optimization` |
| 11 | [Composio](https://github.com/ComposioHQ/composio) | 🟡 **48.3** | 28.4k | 🚀 +133 | 0 | 2 days ago | `tooling` |
| 12 | [Smolagents](https://github.com/huggingface/smolagents) | 🟡 **44.5** | 27.5k | 🚀 +135 | 0 | 8 days ago | `lightweight` |
| 13 | [AutoGen](https://github.com/microsoft/autogen) | 🟡 **43.7** | 58.3k | 🚀 +241 | 0 | 7 mo ago | `multi-agent` |
| 14 | [Swarm](https://github.com/openai/swarm) | 🔴 **9.3** | 21.5k | 📈 +30 | 0 | — | `experimental` |

## 📂 By Category

- `enterprise`: **Semantic Kernel** (50.8)
- `experimental`: **Swarm** (9.3)
- `lightweight`: **Smolagents** (44.5)
- `multi-agent`: **CrewAI** (71.1), **Agno** (54.3), **AutoGen** (43.7)
- `optimization`: **DSPy** (49.8)
- `orchestration`: **LangGraph** (68.8), **Claude Agent SDK** (64.9)
- `pipeline`: **Haystack** (50.5)
- `structured`: **PydanticAI** (53.8)
- `tooling`: **Composio** (48.3)
- `typescript`: **Mastra** (80.1)
- `web-agent`: **BrowserUse** (69.9)

## 🔍 Top 5 — Score Breakdown

| Framework | Star Velocity | Release Freshness | Issue Health | Commit Activity | Community | Fork Ratio |
|-----------|:---:|:---:|:---:|:---:|:---:|:---:|
| **Mastra** | 55.7 | 98.7 | 94.8 | 100 | 87.6 | 34.8 |
| **CrewAI** | 100 | 99.7 | 98.2 | 0.0 | 59.4 | 55.4 |
| **BrowserUse** | 100 | 98.7 | 96.0 | 0.0 | 63.0 | 45.0 |
| **LangGraph** | 100 | 100.0 | 76.9 | 0.0 | 54.8 | 67.6 |
| **Claude Agent SDK** | 100 | 100.0 | 82.0 | 0.0 | 10.0 | 65.7 |

## 💡 Key Insights

- **Hottest framework**: Mastra with a Pulse Score of 80.1
- **Fastest growing**: Claude Agent SDK gained +1879 stars this week
- **Most active development**: Mastra with 1055 commits in the last 4 weeks
- **Stale releases**: Swarm haven't released in a while

## 📦 Recent Releases

- **Claude Agent SDK** [`v2.1.150`](https://github.com/anthropics/claude-code/releases/tag/v2.1.150) — today
- **PydanticAI** [`v2.0.0b3`](https://github.com/pydantic/pydantic-ai/releases/tag/v2.0.0b3) — today *(pre-release)*
- **LangGraph** [`sdk==0.3.15`](https://github.com/langchain-ai/langgraph/releases/tag/sdk==0.3.15) — today
- **Agno** [`v2.6.9`](https://github.com/agno-agi/agno/releases/tag/v2.6.9) — 1 day ago
- **CrewAI** [`1.14.6a1`](https://github.com/crewAIInc/crewAI/releases/tag/1.14.6a1) — 1 day ago *(pre-release)*
- **Composio** [`@composio/cli@0.2.31-beta.256`](https://github.com/ComposioHQ/composio/releases/tag/@composio/cli@0.2.31-beta.256) — 2 days ago *(pre-release)*
- **BrowserUse** [`0.12.7`](https://github.com/browser-use/browser-use/releases/tag/0.12.7) — 4 days ago
- **Mastra** [`@mastra/core@1.35.0`](https://github.com/mastra-ai/mastra/releases/tag/@mastra/core@1.35.0) — 4 days ago
- **Smolagents** [`v1.25.0`](https://github.com/huggingface/smolagents/releases/tag/v1.25.0) — 8 days ago
- **Semantic Kernel** [`python-1.42.0`](https://github.com/microsoft/semantic-kernel/releases/tag/python-1.42.0) — 9 days ago

## 🚀 Running Locally

```bash
# Clone the repo
git clone https://github.com/YOUR_USERNAME/ai-agent-pulse.git
cd ai-agent-pulse

# Install dependencies
pip install -r requirements.txt

# Set your GitHub token (optional but recommended for higher rate limits)
export GITHUB_TOKEN=ghp_your_token_here

# Run the tracker
python tracker.py

# Generate the dashboard
python dashboard.py
```

## 📋 Adding a Framework

Edit `config.yaml` and add a new entry under `frameworks:`

```yaml
- name: MyFramework
  repo: owner/repo-name
  category: multi-agent
  description: A brief description
```

## ⚙️ How the Pulse Score Works

The Pulse Score (0–100) is a weighted composite of six signals:

| Signal | Weight | What It Measures |
|--------|--------|------------------|
| Star Velocity | 25% | 7-day and 30-day star growth rate |
| Release Freshness | 20% | Days since last release |
| Commit Activity | 20% | Commits in the last 4 weeks |
| Issue Health | 15% | Ratio of closed to total issues |
| Community | 10% | Total number of contributors |
| Fork Ratio | 10% | Forks relative to stars (engagement) |

---

*Powered by GitHub Actions • Data refreshed daily • Last run: 2026-05-23 08:26 UTC*