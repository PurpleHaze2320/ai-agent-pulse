# 🔬 AI Agent Framework Pulse Tracker

[![Daily Update](https://github.com/PurpleHaze2320/ai-agent-pulse/actions/workflows/track.yml/badge.svg)](https://github.com/PurpleHaze2320/ai-agent-pulse/actions/workflows/track.yml)
[![Frameworks Tracked](https://img.shields.io/badge/frameworks-19-blue)](https://github.com/PurpleHaze2320/ai-agent-pulse)
[![License: MIT](https://img.shields.io/badge/License-MIT-green.svg)](https://opensource.org/licenses/MIT)
[![GitHub stars](https://img.shields.io/github/stars/PurpleHaze2320/ai-agent-pulse?style=social)](https://github.com/PurpleHaze2320/ai-agent-pulse/stargazers)

> Automated daily tracking of the AI agent framework ecosystem's health, momentum, and trends.
> Last updated: **2026-07-22 08:36 UTC** | Tracking **19** frameworks

## How It Works

This bot runs daily via GitHub Actions and collects metrics from the GitHub API for the most important
AI agent frameworks. It computes a **Pulse Score** (0-100) based on six weighted signals: star velocity,
release freshness, issue health, commit activity, community size, and fork engagement. The result is
a living dashboard that shows which frameworks are gaining momentum and which are losing steam.

## 🏆 Pulse Leaderboard

| Rank | Framework | Pulse | Stars | ⭐ 7d | Commits (4w) | Last Release | Category |
|------|-----------|-------|-------|-------|--------------|--------------|----------|
| 1 | [BrowserUse](https://github.com/browser-use/browser-use) | 🟢 **84.0** | 106.0k | 🚀 +1210 | 72 | 5 days ago | `web-agent` |
| 2 | [CrewAI](https://github.com/crewAIInc/crewAI) | 🟢 **80.2** | 55.9k | 🚀 +394 | 68 | 1 day ago | `multi-agent` |
| 3 | [Mastra](https://github.com/mastra-ai/mastra) | 🟢 **79.5** | 26.4k | 🚀 +243 | 970 | 6 days ago | `typescript` |
| 4 | [Google ADK](https://github.com/google/adk-python) | 🟢 **77.7** | 20.8k | 🚀 +218 | 281 | today | `orchestration` |
| 5 | [PydanticAI](https://github.com/pydantic/pydantic-ai) | 🟢 **77.2** | 18.7k | 🚀 +191 | 246 | today | `structured` |
| 6 | [OpenAI Agents SDK](https://github.com/openai/openai-agents-python) | 🟢 **75.1** | 28.1k | 🚀 +157 | 119 | 5 days ago | `orchestration` |
| 7 | [Agno](https://github.com/agno-agi/agno) | 🟢 **74.7** | 41.3k | 🚀 +177 | 142 | 1 day ago | `multi-agent` |
| 8 | [LangGraph](https://github.com/langchain-ai/langgraph) | 🟢 **73.0** | 37.8k | 🚀 +497 | 29 | 12 days ago | `orchestration` |
| 9 | [Claude Agent SDK](https://github.com/anthropics/claude-code) | 🟢 **70.5** | 138.6k | 🚀 +715 | 27 | today | `orchestration` |
| 10 | [Composio](https://github.com/ComposioHQ/composio) | 🟡 **66.4** | 29.3k | 📈 +76 | 124 | 1 day ago | `tooling` |
| 11 | [LlamaIndex](https://github.com/run-llama/llama_index) | 🟡 **56.1** | 51.0k | 🚀 +143 | 0 | 27 days ago | `data-agent` |
| 12 | [Semantic Kernel](https://github.com/microsoft/semantic-kernel) | 🟡 **52.7** | 28.3k | 📈 +31 | 13 | 14 days ago | `enterprise` |
| 13 | [Haystack](https://github.com/deepset-ai/haystack) | 🟡 **51.2** | 26.0k | 📈 +80 | 0 | 1 day ago | `pipeline` |
| 14 | [DSPy](https://github.com/stanfordnlp/dspy) | 🟡 **49.3** | 36.3k | 🚀 +156 | 0 | 1 mo ago | `optimization` |
| 15 | [AG2](https://github.com/ag2ai/ag2) | 🟡 **48.7** | 4.8k | ↗️ +13 | 0 | 18 days ago | `multi-agent` |
| 16 | [Letta](https://github.com/letta-ai/letta) | 🟡 **42.9** | 23.9k | 🚀 +108 | 1 | 2 mo ago | `memory` |
| 17 | [Smolagents](https://github.com/huggingface/smolagents) | 🟡 **41.5** | 28.5k | 🚀 +125 | 4 | 1 mo ago | `lightweight` |
| 18 | [AutoGen](https://github.com/microsoft/autogen) | 🟠 **35.7** | 59.9k | 🚀 +151 | 0 | 9 mo ago | `multi-agent` |
| 19 | [Swarm](https://github.com/openai/swarm) | 🔴 **11.2** | 21.9k | 📈 +55 | 0 | — | `experimental` |

## 📂 By Category

- `data-agent`: **LlamaIndex** (56.1)
- `enterprise`: **Semantic Kernel** (52.7)
- `experimental`: **Swarm** (11.2)
- `lightweight`: **Smolagents** (41.5)
- `memory`: **Letta** (42.9)
- `multi-agent`: **CrewAI** (80.2), **Agno** (74.7), **AG2** (48.7), **AutoGen** (35.7)
- `optimization`: **DSPy** (49.3)
- `orchestration`: **Google ADK** (77.7), **OpenAI Agents SDK** (75.1), **LangGraph** (73.0), **Claude Agent SDK** (70.5)
- `pipeline`: **Haystack** (51.2)
- `structured`: **PydanticAI** (77.2)
- `tooling`: **Composio** (66.4)
- `typescript`: **Mastra** (79.5)
- `web-agent`: **BrowserUse** (84.0)

## 🔍 Top 5 — Score Breakdown

| Framework | Star Velocity | Release Freshness | Issue Health | Commit Activity | Community | Fork Ratio |
|-----------|:---:|:---:|:---:|:---:|:---:|:---:|
| **BrowserUse** | 100 | 98.3 | 94.8 | 72.0 | 63.0 | 44.0 |
| **CrewAI** | 82.5 | 99.7 | 96.2 | 68.0 | 59.6 | 56.6 |
| **Mastra** | 50.6 | 98.0 | 94.4 | 100 | 93.0 | 37.7 |
| **Google ADK** | 39.6 | 100.0 | 87.4 | 100 | 75.2 | 71.6 |
| **PydanticAI** | 39.1 | 100.0 | 85.7 | 100 | 94.8 | 51.2 |

## 💡 Key Insights

- **Hottest framework**: BrowserUse with a Pulse Score of 84.0
- **Fastest growing**: BrowserUse gained +1210 stars this week
- **Most active development**: Mastra with 970 commits in the last 4 weeks
- **Stale releases**: AutoGen, Swarm haven't released in a while

## 📦 Recent Releases

- **PydanticAI** [`v2.15.0`](https://github.com/pydantic/pydantic-ai/releases/tag/v2.15.0) — today
- **Google ADK** [`v1.36.2`](https://github.com/google/adk-python/releases/tag/v1.36.2) — today
- **Claude Agent SDK** [`v2.1.217`](https://github.com/anthropics/claude-code/releases/tag/v2.1.217) — today
- **Composio** [`@composio/cli@0.2.33-beta.298`](https://github.com/ComposioHQ/composio/releases/tag/@composio/cli@0.2.33-beta.298) — 1 day ago *(pre-release)*
- **CrewAI** [`1.15.5`](https://github.com/crewAIInc/crewAI/releases/tag/1.15.5) — 1 day ago
- **Agno** [`v2.8.0`](https://github.com/agno-agi/agno/releases/tag/v2.8.0) — 1 day ago
- **Haystack** [`v3.0.0`](https://github.com/deepset-ai/haystack/releases/tag/v3.0.0) — 1 day ago
- **BrowserUse** [`0.13.6`](https://github.com/browser-use/browser-use/releases/tag/0.13.6) — 5 days ago
- **OpenAI Agents SDK** [`v0.18.3`](https://github.com/openai/openai-agents-python/releases/tag/v0.18.3) — 5 days ago
- **Mastra** [`@mastra/core@1.51.0`](https://github.com/mastra-ai/mastra/releases/tag/@mastra/core@1.51.0) — 6 days ago

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

*Powered by GitHub Actions • Data refreshed daily • Last run: 2026-07-22 08:36 UTC*