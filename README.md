# 🔬 AI Agent Framework Pulse Tracker

[![Daily Update](https://github.com/PurpleHaze2320/ai-agent-pulse/actions/workflows/track.yml/badge.svg)](https://github.com/PurpleHaze2320/ai-agent-pulse/actions/workflows/track.yml)
[![Frameworks Tracked](https://img.shields.io/badge/frameworks-19-blue)](https://github.com/PurpleHaze2320/ai-agent-pulse)
[![License: MIT](https://img.shields.io/badge/License-MIT-green.svg)](https://opensource.org/licenses/MIT)
[![GitHub stars](https://img.shields.io/github/stars/PurpleHaze2320/ai-agent-pulse?style=social)](https://github.com/PurpleHaze2320/ai-agent-pulse/stargazers)

> Automated daily tracking of the AI agent framework ecosystem's health, momentum, and trends.
> Last updated: **2026-11-09 15:44 UTC** | Tracking **19** frameworks

## How It Works

This bot runs daily via GitHub Actions and collects metrics from the GitHub API for the most important
AI agent frameworks. It computes a **Pulse Score** (0-100) based on six weighted signals: star velocity,
release freshness, issue health, commit activity, community size, and fork engagement. The result is
a living dashboard that shows which frameworks are gaining momentum and which are losing steam.

## 🏆 Pulse Leaderboard

| Rank | Framework | Pulse | Stars | ⭐ 7d | Commits (4w) | Last Release | Category |
|------|-----------|-------|-------|-------|--------------|--------------|----------|
| 1 | [LangGraph](https://github.com/langchain-ai/langgraph) | 🟢 **83.6** | 44.7k | 🚀 +363 | 100 | 3 days ago | `orchestration` |
| 2 | [CrewAI](https://github.com/crewAIInc/crewAI) | 🟢 **79.4** | 60.7k | 🚀 +266 | 185 | today | `multi-agent` |
| 3 | [Mastra](https://github.com/mastra-ai/mastra) | 🟢 **75.4** | 29.4k | 🚀 +152 | 1850 | 5 days ago | `typescript` |
| 4 | [Google ADK](https://github.com/google/adk-python) | 🟢 **74.5** | 22.2k | 📈 +77 | 355 | 2 days ago | `orchestration` |
| 5 | [Claude Agent SDK](https://github.com/anthropics/claude-code) | 🟢 **71.8** | 155.1k | 🚀 +802 | 33 | 2 days ago | `orchestration` |
| 6 | [BrowserUse](https://github.com/browser-use/browser-use) | 🟢 **71.7** | 120.4k | 🚀 +586 | 12 | 13 days ago | `web-agent` |
| 7 | [Haystack](https://github.com/deepset-ai/haystack) | 🟢 **71.4** | 27.0k | 📈 +47 | 200 | today | `pipeline` |
| 8 | [OpenAI Agents SDK](https://github.com/openai/openai-agents-python) | 🟢 **70.1** | 30.6k | 🚀 +119 | 71 | 1 day ago | `orchestration` |
| 9 | [PydanticAI](https://github.com/pydantic/pydantic-ai) | 🟢 **70.0** | 21.1k | 🚀 +105 | 1066 | 1 mo ago | `structured` |
| 10 | [Agno](https://github.com/agno-agi/agno) | 🟡 **69.9** | 43.1k | 🚀 +103 | 127 | 11 days ago | `multi-agent` |
| 11 | [AG2](https://github.com/ag2ai/ag2) | 🟡 **69.8** | 5.1k | ↗️ +13 | 105 | 5 days ago | `multi-agent` |
| 12 | [Semantic Kernel](https://github.com/microsoft/semantic-kernel) | 🟡 **68.9** | 28.7k | 📈 +24 | 87 | 2 days ago | `enterprise` |
| 13 | [Composio](https://github.com/ComposioHQ/composio) | 🟡 **68.7** | 31.0k | 🚀 +122 | 266 | today | `tooling` |
| 14 | [LlamaIndex](https://github.com/run-llama/llama_index) | 🟡 **51.7** | 52.9k | 📈 +81 | 2 | 1 mo ago | `data-agent` |
| 15 | [DSPy](https://github.com/stanfordnlp/dspy) | 🟡 **47.1** | 39.0k | 📈 +99 | 0 | 27 days ago | `optimization` |
| 16 | [Letta](https://github.com/letta-ai/letta) | 🟠 **34.0** | 25.4k | 📈 +72 | 1 | 5 mo ago | `memory` |
| 17 | [AutoGen](https://github.com/microsoft/autogen) | 🟠 **31.8** | 61.8k | 📈 +81 | 1 | 1y ago | `multi-agent` |
| 18 | [Smolagents](https://github.com/huggingface/smolagents) | 🟠 **30.9** | 30.3k | 📈 +90 | 0 | 5 mo ago | `lightweight` |
| 19 | [Swarm](https://github.com/openai/swarm) | 🔴 **9.4** | 22.1k | 📈 +21 | 0 | — | `experimental` |

## 📂 By Category

- `data-agent`: **LlamaIndex** (51.7)
- `enterprise`: **Semantic Kernel** (68.9)
- `experimental`: **Swarm** (9.4)
- `lightweight`: **Smolagents** (30.9)
- `memory`: **Letta** (34.0)
- `multi-agent`: **CrewAI** (79.4), **Agno** (69.9), **AG2** (69.8), **AutoGen** (31.8)
- `optimization`: **DSPy** (47.1)
- `orchestration`: **LangGraph** (83.6), **Google ADK** (74.5), **Claude Agent SDK** (71.8), **OpenAI Agents SDK** (70.1)
- `pipeline`: **Haystack** (71.4)
- `structured`: **PydanticAI** (70.0)
- `tooling`: **Composio** (68.7)
- `typescript`: **Mastra** (75.4)
- `web-agent`: **BrowserUse** (71.7)

## 🔍 Top 5 — Score Breakdown

| Framework | Star Velocity | Release Freshness | Issue Health | Commit Activity | Community | Fork Ratio |
|-----------|:---:|:---:|:---:|:---:|:---:|:---:|
| **LangGraph** | 76.1 | 99.0 | 80.7 | 100 | 57.4 | 68.9 |
| **CrewAI** | 54.7 | 100.0 | 82.9 | 100 | 72.6 | 60.1 |
| **Mastra** | 32.5 | 98.3 | 93.7 | 100 | 93.2 | 42.0 |
| **Google ADK** | 16.7 | 99.3 | 94.1 | 100 | 85.8 | 78.1 |
| **Claude Agent SDK** | 100 | 99.3 | 84.5 | 33.0 | 11.2 | 65.2 |

## 💡 Key Insights

- **Hottest framework**: LangGraph with a Pulse Score of 83.6
- **Fastest growing**: Claude Agent SDK gained +802 stars this week
- **Most active development**: Mastra with 1850 commits in the last 4 weeks
- **Stale releases**: AutoGen, Swarm haven't released in a while

## 📦 Recent Releases

- **Composio** [`@composio/cli@0.6.1-beta.536`](https://github.com/ComposioHQ/composio/releases/tag/@composio/cli@0.6.1-beta.536) — today *(pre-release)*
- **Haystack** [`v3.5.0-rc1`](https://github.com/deepset-ai/haystack/releases/tag/v3.5.0-rc1) — today *(pre-release)*
- **CrewAI** [`1.15.39`](https://github.com/crewAIInc/crewAI/releases/tag/1.15.39) — today
- **OpenAI Agents SDK** [`v0.24.0-alpha.7`](https://github.com/openai/openai-agents-python/releases/tag/v0.24.0-alpha.7) — 1 day ago *(pre-release)*
- **Semantic Kernel** [`dotnet-1.82.0`](https://github.com/microsoft/semantic-kernel/releases/tag/dotnet-1.82.0) — 2 days ago
- **Google ADK** [`v2.14.0`](https://github.com/google/adk-python/releases/tag/v2.14.0) — 2 days ago
- **Claude Agent SDK** [`v2.1.319`](https://github.com/anthropics/claude-code/releases/tag/v2.1.319) — 2 days ago
- **LangGraph** [`sdk==0.4.14`](https://github.com/langchain-ai/langgraph/releases/tag/sdk==0.4.14) — 3 days ago
- **Mastra** [`@mastra/core@1.82.0`](https://github.com/mastra-ai/mastra/releases/tag/@mastra/core@1.82.0) — 5 days ago
- **AG2** [`v1.3.0`](https://github.com/ag2ai/ag2/releases/tag/v1.3.0) — 5 days ago

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

*Powered by GitHub Actions • Data refreshed daily • Last run: 2026-11-09 15:44 UTC*