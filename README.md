# 🔬 AI Agent Framework Pulse Tracker

[![Daily Update](https://github.com/PurpleHaze2320/ai-agent-pulse/actions/workflows/track.yml/badge.svg)](https://github.com/PurpleHaze2320/ai-agent-pulse/actions/workflows/track.yml)
[![Frameworks Tracked](https://img.shields.io/badge/frameworks-19-blue)](https://github.com/PurpleHaze2320/ai-agent-pulse)
[![License: MIT](https://img.shields.io/badge/License-MIT-green.svg)](https://opensource.org/licenses/MIT)
[![GitHub stars](https://img.shields.io/github/stars/PurpleHaze2320/ai-agent-pulse?style=social)](https://github.com/PurpleHaze2320/ai-agent-pulse/stargazers)

> Automated daily tracking of the AI agent framework ecosystem's health, momentum, and trends.
> Last updated: **2026-07-27 10:00 UTC** | Tracking **19** frameworks

## How It Works

This bot runs daily via GitHub Actions and collects metrics from the GitHub API for the most important
AI agent frameworks. It computes a **Pulse Score** (0-100) based on six weighted signals: star velocity,
release freshness, issue health, commit activity, community size, and fork engagement. The result is
a living dashboard that shows which frameworks are gaining momentum and which are losing steam.

## 🏆 Pulse Leaderboard

| Rank | Framework | Pulse | Stars | ⭐ 7d | Commits (4w) | Last Release | Category |
|------|-----------|-------|-------|-------|--------------|--------------|----------|
| 1 | [BrowserUse](https://github.com/browser-use/browser-use) | 🟢 **84.2** | 107.0k | 🚀 +1306 | 75 | 10 days ago | `web-agent` |
| 2 | [Mastra](https://github.com/mastra-ai/mastra) | 🟢 **79.5** | 26.6k | 🚀 +255 | 921 | 11 days ago | `typescript` |
| 3 | [CrewAI](https://github.com/crewAIInc/crewAI) | 🟢 **78.6** | 56.2k | 🚀 +382 | 63 | today | `multi-agent` |
| 4 | [PydanticAI](https://github.com/pydantic/pydantic-ai) | 🟢 **76.1** | 18.8k | 🚀 +163 | 185 | 2 days ago | `structured` |
| 5 | [OpenAI Agents SDK](https://github.com/openai/openai-agents-python) | 🟢 **75.9** | 28.2k | 🚀 +170 | 138 | today | `orchestration` |
| 6 | [Google ADK](https://github.com/google/adk-python) | 🟢 **74.3** | 20.9k | 🚀 +128 | 255 | 5 days ago | `orchestration` |
| 7 | [Agno](https://github.com/agno-agi/agno) | 🟢 **73.5** | 41.4k | 🚀 +139 | 131 | today | `multi-agent` |
| 8 | [LangGraph](https://github.com/langchain-ai/langgraph) | 🟢 **70.5** | 38.2k | 🚀 +578 | 18 | 17 days ago | `orchestration` |
| 9 | [Haystack](https://github.com/deepset-ai/haystack) | 🟢 **70.5** | 26.0k | 📈 +77 | 220 | 6 days ago | `pipeline` |
| 10 | [Claude Agent SDK](https://github.com/anthropics/claude-code) | 🟡 **69.1** | 139.3k | 🚀 +850 | 21 | 2 days ago | `orchestration` |
| 11 | [Composio](https://github.com/ComposioHQ/composio) | 🟡 **67.4** | 29.4k | 🚀 +113 | 113 | 6 days ago | `tooling` |
| 12 | [LlamaIndex](https://github.com/run-llama/llama_index) | 🟡 **60.1** | 51.1k | 🚀 +183 | 15 | 1 mo ago | `data-agent` |
| 13 | [Semantic Kernel](https://github.com/microsoft/semantic-kernel) | 🟡 **52.5** | 28.4k | 📈 +41 | 12 | 20 days ago | `enterprise` |
| 14 | [AG2](https://github.com/ag2ai/ag2) | 🟡 **50.2** | 4.8k | ↗️ +19 | 0 | today | `multi-agent` |
| 15 | [DSPy](https://github.com/stanfordnlp/dspy) | 🟡 **49.1** | 36.4k | 🚀 +164 | 0 | 2 mo ago | `optimization` |
| 16 | [Letta](https://github.com/letta-ai/letta) | 🟡 **42.1** | 24.0k | 🚀 +104 | 0 | 2 mo ago | `memory` |
| 17 | [Smolagents](https://github.com/huggingface/smolagents) | 🟡 **40.8** | 28.6k | 🚀 +117 | 4 | 1 mo ago | `lightweight` |
| 18 | [AutoGen](https://github.com/microsoft/autogen) | 🟠 **36.5** | 60.0k | 🚀 +188 | 0 | 10 mo ago | `multi-agent` |
| 19 | [Swarm](https://github.com/openai/swarm) | 🔴 **9.7** | 21.9k | ↗️ +18 | 0 | — | `experimental` |

## 📂 By Category

- `data-agent`: **LlamaIndex** (60.1)
- `enterprise`: **Semantic Kernel** (52.5)
- `experimental`: **Swarm** (9.7)
- `lightweight`: **Smolagents** (40.8)
- `memory`: **Letta** (42.1)
- `multi-agent`: **CrewAI** (78.6), **Agno** (73.5), **AG2** (50.2), **AutoGen** (36.5)
- `optimization`: **DSPy** (49.1)
- `orchestration`: **OpenAI Agents SDK** (75.9), **Google ADK** (74.3), **LangGraph** (70.5), **Claude Agent SDK** (69.1)
- `pipeline`: **Haystack** (70.5)
- `structured`: **PydanticAI** (76.1)
- `tooling`: **Composio** (67.4)
- `typescript`: **Mastra** (79.5)
- `web-agent`: **BrowserUse** (84.2)

## 🔍 Top 5 — Score Breakdown

| Framework | Star Velocity | Release Freshness | Issue Health | Commit Activity | Community | Fork Ratio |
|-----------|:---:|:---:|:---:|:---:|:---:|:---:|
| **BrowserUse** | 100 | 96.7 | 94.7 | 75.0 | 63.0 | 43.9 |
| **Mastra** | 52.4 | 96.3 | 93.9 | 100 | 93.0 | 37.9 |
| **CrewAI** | 80.0 | 100.0 | 96.0 | 63.0 | 59.6 | 56.8 |
| **PydanticAI** | 34.9 | 99.3 | 85.7 | 100 | 94.8 | 51.5 |
| **OpenAI Agents SDK** | 34.9 | 100.0 | 98.1 | 100 | 62.4 | 62.1 |

## 💡 Key Insights

- **Hottest framework**: BrowserUse with a Pulse Score of 84.2
- **Fastest growing**: BrowserUse gained +1306 stars this week
- **Most active development**: Mastra with 921 commits in the last 4 weeks
- **Stale releases**: AutoGen, Swarm haven't released in a while

## 📦 Recent Releases

- **Agno** [`v2.8.5`](https://github.com/agno-agi/agno/releases/tag/v2.8.5) — today
- **OpenAI Agents SDK** [`v0.19.0`](https://github.com/openai/openai-agents-python/releases/tag/v0.19.0) — today
- **AG2** [`v1.0.0`](https://github.com/ag2ai/ag2/releases/tag/v1.0.0) — today
- **CrewAI** [`1.15.7`](https://github.com/crewAIInc/crewAI/releases/tag/1.15.7) — today
- **Claude Agent SDK** [`v2.1.220`](https://github.com/anthropics/claude-code/releases/tag/v2.1.220) — 2 days ago
- **PydanticAI** [`v2.18.0`](https://github.com/pydantic/pydantic-ai/releases/tag/v2.18.0) — 2 days ago
- **Google ADK** [`v1.36.2`](https://github.com/google/adk-python/releases/tag/v1.36.2) — 5 days ago
- **Composio** [`@composio/cli@0.2.33-beta.298`](https://github.com/ComposioHQ/composio/releases/tag/@composio/cli@0.2.33-beta.298) — 6 days ago *(pre-release)*
- **Haystack** [`v3.0.0`](https://github.com/deepset-ai/haystack/releases/tag/v3.0.0) — 6 days ago
- **BrowserUse** [`0.13.6`](https://github.com/browser-use/browser-use/releases/tag/0.13.6) — 10 days ago

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

*Powered by GitHub Actions • Data refreshed daily • Last run: 2026-07-27 10:00 UTC*