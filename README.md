# 🔬 AI Agent Framework Pulse Tracker

[![Daily Update](https://github.com/PurpleHaze2320/ai-agent-pulse/actions/workflows/track.yml/badge.svg)](https://github.com/PurpleHaze2320/ai-agent-pulse/actions/workflows/track.yml)
[![Frameworks Tracked](https://img.shields.io/badge/frameworks-19-blue)](https://github.com/PurpleHaze2320/ai-agent-pulse)
[![License: MIT](https://img.shields.io/badge/License-MIT-green.svg)](https://opensource.org/licenses/MIT)
[![GitHub stars](https://img.shields.io/github/stars/PurpleHaze2320/ai-agent-pulse?style=social)](https://github.com/PurpleHaze2320/ai-agent-pulse/stargazers)

> Automated daily tracking of the AI agent framework ecosystem's health, momentum, and trends.
> Last updated: **2026-10-25 11:02 UTC** | Tracking **19** frameworks

## How It Works

This bot runs daily via GitHub Actions and collects metrics from the GitHub API for the most important
AI agent frameworks. It computes a **Pulse Score** (0-100) based on six weighted signals: star velocity,
release freshness, issue health, commit activity, community size, and fork engagement. The result is
a living dashboard that shows which frameworks are gaining momentum and which are losing steam.

## 🏆 Pulse Leaderboard

| Rank | Framework | Pulse | Stars | ⭐ 7d | Commits (4w) | Last Release | Category |
|------|-----------|-------|-------|-------|--------------|--------------|----------|
| 1 | [BrowserUse](https://github.com/browser-use/browser-use) | 🟢 **89.4** | 119.1k | 🚀 +711 | 112 | 9 days ago | `web-agent` |
| 2 | [LangGraph](https://github.com/langchain-ai/langgraph) | 🟢 **83.5** | 43.9k | 🚀 +426 | 91 | 1 day ago | `orchestration` |
| 3 | [CrewAI](https://github.com/crewAIInc/crewAI) | 🟢 **79.0** | 60.1k | 🚀 +257 | 121 | 1 day ago | `multi-agent` |
| 4 | [Mastra](https://github.com/mastra-ai/mastra) | 🟢 **76.9** | 29.1k | 🚀 +186 | 1931 | 3 days ago | `typescript` |
| 5 | [Google ADK](https://github.com/google/adk-python) | 🟢 **75.2** | 22.0k | 🚀 +101 | 406 | 1 day ago | `orchestration` |
| 6 | [PydanticAI](https://github.com/pydantic/pydantic-ai) | 🟢 **73.4** | 20.9k | 🚀 +158 | 832 | 19 days ago | `structured` |
| 7 | [Claude Agent SDK](https://github.com/anthropics/claude-code) | 🟢 **73.4** | 153.3k | 🚀 +1136 | 38 | 1 day ago | `orchestration` |
| 8 | [Haystack](https://github.com/deepset-ai/haystack) | 🟢 **71.9** | 26.8k | 📈 +72 | 202 | 3 days ago | `pipeline` |
| 9 | [Agno](https://github.com/agno-agi/agno) | 🟢 **70.6** | 42.9k | 📈 +95 | 138 | 1 day ago | `multi-agent` |
| 10 | [OpenAI Agents SDK](https://github.com/openai/openai-agents-python) | 🟡 **68.3** | 30.3k | 🚀 +160 | 59 | 10 days ago | `orchestration` |
| 11 | [Composio](https://github.com/ComposioHQ/composio) | 🟡 **68.2** | 30.7k | 🚀 +121 | 294 | 1 day ago | `tooling` |
| 12 | [AG2](https://github.com/ag2ai/ag2) | 🟡 **66.7** | 5.0k | ↗️ +20 | 84 | 3 days ago | `multi-agent` |
| 13 | [LlamaIndex](https://github.com/run-llama/llama_index) | 🟡 **55.0** | 52.7k | 🚀 +109 | 9 | 1 mo ago | `data-agent` |
| 14 | [Semantic Kernel](https://github.com/microsoft/semantic-kernel) | 🟡 **54.2** | 28.7k | 📈 +28 | 23 | 18 days ago | `enterprise` |
| 15 | [DSPy](https://github.com/stanfordnlp/dspy) | 🟡 **48.2** | 38.8k | 📈 +100 | 0 | 12 days ago | `optimization` |
| 16 | [Letta](https://github.com/letta-ai/letta) | 🟠 **35.4** | 25.3k | 📈 +76 | 1 | 5 mo ago | `memory` |
| 17 | [Smolagents](https://github.com/huggingface/smolagents) | 🟠 **33.8** | 30.0k | 🚀 +131 | 1 | 4 mo ago | `lightweight` |
| 18 | [AutoGen](https://github.com/microsoft/autogen) | 🟠 **32.3** | 61.6k | 📈 +97 | 1 | 1y ago | `multi-agent` |
| 19 | [Swarm](https://github.com/openai/swarm) | 🔴 **9.2** | 22.1k | ↗️ +17 | 0 | — | `experimental` |

## 📂 By Category

- `data-agent`: **LlamaIndex** (55.0)
- `enterprise`: **Semantic Kernel** (54.2)
- `experimental`: **Swarm** (9.2)
- `lightweight`: **Smolagents** (33.8)
- `memory`: **Letta** (35.4)
- `multi-agent`: **CrewAI** (79.0), **Agno** (70.6), **AG2** (66.7), **AutoGen** (32.3)
- `optimization`: **DSPy** (48.2)
- `orchestration`: **LangGraph** (83.5), **Google ADK** (75.2), **Claude Agent SDK** (73.4), **OpenAI Agents SDK** (68.3)
- `pipeline`: **Haystack** (71.9)
- `structured`: **PydanticAI** (73.4)
- `tooling`: **Composio** (68.2)
- `typescript`: **Mastra** (76.9)
- `web-agent`: **BrowserUse** (89.4)

## 🔍 Top 5 — Score Breakdown

| Framework | Star Velocity | Release Freshness | Issue Health | Commit Activity | Community | Fork Ratio |
|-----------|:---:|:---:|:---:|:---:|:---:|:---:|
| **BrowserUse** | 100 | 97.0 | 89.3 | 100 | 72.0 | 44.4 |
| **LangGraph** | 83.7 | 99.7 | 79.0 | 91.0 | 57.0 | 68.7 |
| **CrewAI** | 52.1 | 99.7 | 86.2 | 100 | 71.6 | 59.1 |
| **Mastra** | 37.1 | 99.0 | 95.1 | 100 | 93.6 | 41.8 |
| **Google ADK** | 19.6 | 99.7 | 94.1 | 100 | 85.8 | 77.1 |

## 💡 Key Insights

- **Hottest framework**: BrowserUse with a Pulse Score of 89.4
- **Fastest growing**: Claude Agent SDK gained +1136 stars this week
- **Most active development**: Mastra with 1931 commits in the last 4 weeks
- **Stale releases**: AutoGen, Swarm haven't released in a while

## 📦 Recent Releases

- **CrewAI** [`1.15.30`](https://github.com/crewAIInc/crewAI/releases/tag/1.15.30) — 1 day ago
- **LangGraph** [`1.2.17`](https://github.com/langchain-ai/langgraph/releases/tag/1.2.17) — 1 day ago
- **Claude Agent SDK** [`v2.1.310`](https://github.com/anthropics/claude-code/releases/tag/v2.1.310) — 1 day ago
- **Composio** [`@composio/cli@0.5.1-beta.500`](https://github.com/ComposioHQ/composio/releases/tag/@composio/cli@0.5.1-beta.500) — 1 day ago *(pre-release)*
- **Google ADK** [`v2.13.0`](https://github.com/google/adk-python/releases/tag/v2.13.0) — 1 day ago
- **Agno** [`v3.1.10`](https://github.com/agno-agi/agno/releases/tag/v3.1.10) — 1 day ago
- **AG2** [`v1.2.1`](https://github.com/ag2ai/ag2/releases/tag/v1.2.1) — 3 days ago
- **Haystack** [`v3.4.1`](https://github.com/deepset-ai/haystack/releases/tag/v3.4.1) — 3 days ago
- **Mastra** [`@mastra/core@1.79.0`](https://github.com/mastra-ai/mastra/releases/tag/@mastra/core@1.79.0) — 3 days ago
- **BrowserUse** [`0.13.13`](https://github.com/browser-use/browser-use/releases/tag/0.13.13) — 9 days ago

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

*Powered by GitHub Actions • Data refreshed daily • Last run: 2026-10-25 11:02 UTC*