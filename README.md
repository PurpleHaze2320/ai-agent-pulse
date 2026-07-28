# 🔬 AI Agent Framework Pulse Tracker

[![Daily Update](https://github.com/PurpleHaze2320/ai-agent-pulse/actions/workflows/track.yml/badge.svg)](https://github.com/PurpleHaze2320/ai-agent-pulse/actions/workflows/track.yml)
[![Frameworks Tracked](https://img.shields.io/badge/frameworks-19-blue)](https://github.com/PurpleHaze2320/ai-agent-pulse)
[![License: MIT](https://img.shields.io/badge/License-MIT-green.svg)](https://opensource.org/licenses/MIT)
[![GitHub stars](https://img.shields.io/github/stars/PurpleHaze2320/ai-agent-pulse?style=social)](https://github.com/PurpleHaze2320/ai-agent-pulse/stargazers)

> Automated daily tracking of the AI agent framework ecosystem's health, momentum, and trends.
> Last updated: **2026-07-28 08:42 UTC** | Tracking **19** frameworks

## How It Works

This bot runs daily via GitHub Actions and collects metrics from the GitHub API for the most important
AI agent frameworks. It computes a **Pulse Score** (0-100) based on six weighted signals: star velocity,
release freshness, issue health, commit activity, community size, and fork engagement. The result is
a living dashboard that shows which frameworks are gaining momentum and which are losing steam.

## 🏆 Pulse Leaderboard

| Rank | Framework | Pulse | Stars | ⭐ 7d | Commits (4w) | Last Release | Category |
|------|-----------|-------|-------|-------|--------------|--------------|----------|
| 1 | [BrowserUse](https://github.com/browser-use/browser-use) | 🟢 **85.1** | 107.1k | 🚀 +1240 | 76 | today | `web-agent` |
| 2 | [Mastra](https://github.com/mastra-ai/mastra) | 🟢 **80.0** | 26.6k | 🚀 +248 | 966 | today | `typescript` |
| 3 | [CrewAI](https://github.com/crewAIInc/crewAI) | 🟢 **79.2** | 56.3k | 🚀 +381 | 66 | 1 day ago | `multi-agent` |
| 4 | [PydanticAI](https://github.com/pydantic/pydantic-ai) | 🟢 **76.4** | 18.9k | 🚀 +168 | 195 | today | `structured` |
| 5 | [OpenAI Agents SDK](https://github.com/openai/openai-agents-python) | 🟢 **76.3** | 28.2k | 🚀 +181 | 152 | 1 day ago | `orchestration` |
| 6 | [Agno](https://github.com/agno-agi/agno) | 🟢 **73.7** | 41.5k | 🚀 +144 | 132 | today | `multi-agent` |
| 7 | [Google ADK](https://github.com/google/adk-python) | 🟢 **73.6** | 20.9k | 🚀 +106 | 282 | 6 days ago | `orchestration` |
| 8 | [LangGraph](https://github.com/langchain-ai/langgraph) | 🟢 **70.4** | 38.3k | 🚀 +575 | 18 | 18 days ago | `orchestration` |
| 9 | [Haystack](https://github.com/deepset-ai/haystack) | 🟢 **70.3** | 26.0k | 📈 +73 | 226 | 7 days ago | `pipeline` |
| 10 | [Claude Agent SDK](https://github.com/anthropics/claude-code) | 🟡 **69.0** | 139.4k | 🚀 +861 | 21 | 3 days ago | `orchestration` |
| 11 | [LlamaIndex](https://github.com/run-llama/llama_index) | 🟡 **59.9** | 51.2k | 🚀 +179 | 15 | 1 mo ago | `data-agent` |
| 12 | [AG2](https://github.com/ag2ai/ag2) | 🟡 **58.8** | 4.8k | 📈 +22 | 43 | 1 day ago | `multi-agent` |
| 13 | [Semantic Kernel](https://github.com/microsoft/semantic-kernel) | 🟡 **50.1** | 28.4k | 📈 +43 | 0 | 20 days ago | `enterprise` |
| 14 | [DSPy](https://github.com/stanfordnlp/dspy) | 🟡 **48.4** | 36.4k | 🚀 +155 | 0 | 2 mo ago | `optimization` |
| 15 | [Composio](https://github.com/ComposioHQ/composio) | 🟡 **47.3** | 29.4k | 🚀 +112 | 0 | 7 days ago | `tooling` |
| 16 | [Letta](https://github.com/letta-ai/letta) | 🟡 **41.8** | 24.0k | 📈 +96 | 0 | 2 mo ago | `memory` |
| 17 | [Smolagents](https://github.com/huggingface/smolagents) | 🟡 **40.5** | 28.6k | 🚀 +111 | 4 | 2 mo ago | `lightweight` |
| 18 | [AutoGen](https://github.com/microsoft/autogen) | 🟠 **36.6** | 60.1k | 🚀 +188 | 0 | 10 mo ago | `multi-agent` |
| 19 | [Swarm](https://github.com/openai/swarm) | 🔴 **9.9** | 21.9k | 📈 +23 | 0 | — | `experimental` |

## 📂 By Category

- `data-agent`: **LlamaIndex** (59.9)
- `enterprise`: **Semantic Kernel** (50.1)
- `experimental`: **Swarm** (9.9)
- `lightweight`: **Smolagents** (40.5)
- `memory`: **Letta** (41.8)
- `multi-agent`: **CrewAI** (79.2), **Agno** (73.7), **AG2** (58.8), **AutoGen** (36.6)
- `optimization`: **DSPy** (48.4)
- `orchestration`: **OpenAI Agents SDK** (76.3), **Google ADK** (73.6), **LangGraph** (70.4), **Claude Agent SDK** (69.0)
- `pipeline`: **Haystack** (70.3)
- `structured`: **PydanticAI** (76.4)
- `tooling`: **Composio** (47.3)
- `typescript`: **Mastra** (80.0)
- `web-agent`: **BrowserUse** (85.1)

## 🔍 Top 5 — Score Breakdown

| Framework | Star Velocity | Release Freshness | Issue Health | Commit Activity | Community | Fork Ratio |
|-----------|:---:|:---:|:---:|:---:|:---:|:---:|
| **BrowserUse** | 100 | 100.0 | 94.7 | 76.0 | 63.0 | 44.0 |
| **Mastra** | 51.4 | 100.0 | 93.8 | 100 | 93.0 | 37.9 |
| **CrewAI** | 80.0 | 99.7 | 95.9 | 66.0 | 59.6 | 56.8 |
| **PydanticAI** | 35.8 | 100.0 | 85.5 | 100 | 94.8 | 51.6 |
| **OpenAI Agents SDK** | 36.6 | 99.7 | 98.2 | 100 | 62.8 | 62.1 |

## 💡 Key Insights

- **Hottest framework**: BrowserUse with a Pulse Score of 85.1
- **Fastest growing**: BrowserUse gained +1240 stars this week
- **Most active development**: Mastra with 966 commits in the last 4 weeks
- **Stale releases**: AutoGen, Swarm haven't released in a while

## 📦 Recent Releases

- **PydanticAI** [`v2.19.0`](https://github.com/pydantic/pydantic-ai/releases/tag/v2.19.0) — today
- **BrowserUse** [`0.13.7`](https://github.com/browser-use/browser-use/releases/tag/0.13.7) — today
- **Mastra** [`@mastra/core@1.52.0`](https://github.com/mastra-ai/mastra/releases/tag/@mastra/core@1.52.0) — today
- **Agno** [`v2.8.5`](https://github.com/agno-agi/agno/releases/tag/v2.8.5) — today
- **OpenAI Agents SDK** [`v0.19.0`](https://github.com/openai/openai-agents-python/releases/tag/v0.19.0) — 1 day ago
- **AG2** [`v1.0.0`](https://github.com/ag2ai/ag2/releases/tag/v1.0.0) — 1 day ago
- **CrewAI** [`1.15.7`](https://github.com/crewAIInc/crewAI/releases/tag/1.15.7) — 1 day ago
- **Claude Agent SDK** [`v2.1.220`](https://github.com/anthropics/claude-code/releases/tag/v2.1.220) — 3 days ago
- **Google ADK** [`v1.36.2`](https://github.com/google/adk-python/releases/tag/v1.36.2) — 6 days ago
- **Composio** [`@composio/cli@0.2.33-beta.298`](https://github.com/ComposioHQ/composio/releases/tag/@composio/cli@0.2.33-beta.298) — 7 days ago *(pre-release)*

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

*Powered by GitHub Actions • Data refreshed daily • Last run: 2026-07-28 08:42 UTC*