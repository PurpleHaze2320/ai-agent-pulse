# 🔬 AI Agent Framework Pulse Tracker

[![Daily Update](https://github.com/PurpleHaze2320/ai-agent-pulse/actions/workflows/track.yml/badge.svg)](https://github.com/PurpleHaze2320/ai-agent-pulse/actions/workflows/track.yml)
[![Frameworks Tracked](https://img.shields.io/badge/frameworks-19-blue)](https://github.com/PurpleHaze2320/ai-agent-pulse)
[![License: MIT](https://img.shields.io/badge/License-MIT-green.svg)](https://opensource.org/licenses/MIT)
[![GitHub stars](https://img.shields.io/github/stars/PurpleHaze2320/ai-agent-pulse?style=social)](https://github.com/PurpleHaze2320/ai-agent-pulse/stargazers)

> Automated daily tracking of the AI agent framework ecosystem's health, momentum, and trends.
> Last updated: **2026-11-17 15:45 UTC** | Tracking **19** frameworks

## How It Works

This bot runs daily via GitHub Actions and collects metrics from the GitHub API for the most important
AI agent frameworks. It computes a **Pulse Score** (0-100) based on six weighted signals: star velocity,
release freshness, issue health, commit activity, community size, and fork engagement. The result is
a living dashboard that shows which frameworks are gaining momentum and which are losing steam.

## 🏆 Pulse Leaderboard

| Rank | Framework | Pulse | Stars | ⭐ 7d | Commits (4w) | Last Release | Category |
|------|-----------|-------|-------|-------|--------------|--------------|----------|
| 1 | [BrowserUse](https://github.com/browser-use/browser-use) | 🟢 **90.2** | 121.3k | 🚀 +757 | 1152 | 1 day ago | `web-agent` |
| 2 | [LangGraph](https://github.com/langchain-ai/langgraph) | 🟢 **81.7** | 45.1k | 🚀 +319 | 103 | 3 days ago | `orchestration` |
| 3 | [CrewAI](https://github.com/crewAIInc/crewAI) | 🟢 **80.9** | 61.0k | 🚀 +303 | 167 | 4 days ago | `multi-agent` |
| 4 | [Google ADK](https://github.com/google/adk-python) | 🟢 **74.2** | 22.2k | 📈 +76 | 327 | 4 days ago | `orchestration` |
| 5 | [Mastra](https://github.com/mastra-ai/mastra) | 🟢 **73.9** | 29.6k | 🚀 +115 | 2098 | 4 days ago | `typescript` |
| 6 | [PydanticAI](https://github.com/pydantic/pydantic-ai) | 🟢 **73.4** | 21.3k | 🚀 +134 | 989 | today | `structured` |
| 7 | [OpenAI Agents SDK](https://github.com/openai/openai-agents-python) | 🟢 **73.4** | 30.7k | 🚀 +135 | 85 | 1 day ago | `orchestration` |
| 8 | [Haystack](https://github.com/deepset-ai/haystack) | 🟢 **71.0** | 27.0k | 📈 +46 | 220 | 7 days ago | `pipeline` |
| 9 | [AG2](https://github.com/ag2ai/ag2) | 🟢 **70.3** | 5.1k | ↗️ +19 | 107 | 1 day ago | `multi-agent` |
| 10 | [Agno](https://github.com/agno-agi/agno) | 🟡 **69.8** | 43.2k | 📈 +86 | 124 | 4 days ago | `multi-agent` |
| 11 | [Semantic Kernel](https://github.com/microsoft/semantic-kernel) | 🟡 **67.7** | 28.8k | 📈 +33 | 82 | 10 days ago | `enterprise` |
| 12 | [Claude Agent SDK](https://github.com/anthropics/claude-code) | 🟡 **65.2** | 156.0k | 🚀 +829 | 0 | today | `orchestration` |
| 13 | [DSPy](https://github.com/stanfordnlp/dspy) | 🟡 **64.3** | 39.1k | 🚀 +115 | 76 | 6 days ago | `optimization` |
| 14 | [LlamaIndex](https://github.com/run-llama/llama_index) | 🟡 **55.1** | 52.9k | 📈 +59 | 8 | 3 days ago | `data-agent` |
| 15 | [Composio](https://github.com/ComposioHQ/composio) | 🟡 **48.5** | 31.1k | 🚀 +120 | 0 | today | `tooling` |
| 16 | [Smolagents](https://github.com/huggingface/smolagents) | 🟠 **33.5** | 30.4k | 🚀 +105 | 13 | 5 mo ago | `lightweight` |
| 17 | [AutoGen](https://github.com/microsoft/autogen) | 🟠 **33.2** | 61.9k | 🚀 +116 | 2 | 1y ago | `multi-agent` |
| 18 | [Letta](https://github.com/letta-ai/letta) | 🟠 **33.0** | 25.5k | 📈 +66 | 0 | 6 mo ago | `memory` |
| 19 | [Swarm](https://github.com/openai/swarm) | 🔴 **9.6** | 22.1k | 📈 +25 | 0 | — | `experimental` |

## 📂 By Category

- `data-agent`: **LlamaIndex** (55.1)
- `enterprise`: **Semantic Kernel** (67.7)
- `experimental`: **Swarm** (9.6)
- `lightweight`: **Smolagents** (33.5)
- `memory`: **Letta** (33.0)
- `multi-agent`: **CrewAI** (80.9), **AG2** (70.3), **Agno** (69.8), **AutoGen** (33.2)
- `optimization`: **DSPy** (64.3)
- `orchestration`: **LangGraph** (81.7), **Google ADK** (74.2), **OpenAI Agents SDK** (73.4), **Claude Agent SDK** (65.2)
- `pipeline`: **Haystack** (71.0)
- `structured`: **PydanticAI** (73.4)
- `tooling`: **Composio** (48.5)
- `typescript`: **Mastra** (73.9)
- `web-agent`: **BrowserUse** (90.2)

## 🔍 Top 5 — Score Breakdown

| Framework | Star Velocity | Release Freshness | Issue Health | Commit Activity | Community | Fork Ratio |
|-----------|:---:|:---:|:---:|:---:|:---:|:---:|
| **BrowserUse** | 100 | 99.7 | 90.2 | 100 | 72.4 | 44.7 |
| **LangGraph** | 69.2 | 99.0 | 79.9 | 100 | 57.6 | 69.0 |
| **CrewAI** | 60.5 | 98.7 | 83.4 | 100 | 74.8 | 60.4 |
| **Google ADK** | 15.9 | 98.7 | 93.2 | 100 | 86.0 | 78.7 |
| **Mastra** | 26.4 | 98.7 | 93.9 | 100 | 93.2 | 42.1 |

## 💡 Key Insights

- **Hottest framework**: BrowserUse with a Pulse Score of 90.2
- **Fastest growing**: Claude Agent SDK gained +829 stars this week
- **Most active development**: Mastra with 2098 commits in the last 4 weeks
- **Stale releases**: AutoGen, Swarm haven't released in a while

## 📦 Recent Releases

- **Composio** [`@composio/cli@0.6.3-beta.562`](https://github.com/ComposioHQ/composio/releases/tag/@composio/cli@0.6.3-beta.562) — today *(pre-release)*
- **PydanticAI** [`v2.69.0`](https://github.com/pydantic/pydantic-ai/releases/tag/v2.69.0) — today
- **Claude Agent SDK** [`v2.1.326`](https://github.com/anthropics/claude-code/releases/tag/v2.1.326) — today
- **OpenAI Agents SDK** [`v0.24.0-alpha.8`](https://github.com/openai/openai-agents-python/releases/tag/v0.24.0-alpha.8) — 1 day ago *(pre-release)*
- **BrowserUse** [`1.0.6`](https://github.com/browser-use/browser-use/releases/tag/1.0.6) — 1 day ago
- **AG2** [`v1.3.2`](https://github.com/ag2ai/ag2/releases/tag/v1.3.2) — 1 day ago
- **LangGraph** [`1.2.22`](https://github.com/langchain-ai/langgraph/releases/tag/1.2.22) — 3 days ago
- **LlamaIndex** [`v0.14.26`](https://github.com/run-llama/llama_index/releases/tag/v0.14.26) — 3 days ago
- **Mastra** [`@mastra/core@1.83.0`](https://github.com/mastra-ai/mastra/releases/tag/@mastra/core@1.83.0) — 4 days ago
- **Google ADK** [`v2.14.1`](https://github.com/google/adk-python/releases/tag/v2.14.1) — 4 days ago

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

*Powered by GitHub Actions • Data refreshed daily • Last run: 2026-11-17 15:45 UTC*