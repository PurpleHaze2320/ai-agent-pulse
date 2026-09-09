# 🔬 AI Agent Framework Pulse Tracker

[![Daily Update](https://github.com/PurpleHaze2320/ai-agent-pulse/actions/workflows/track.yml/badge.svg)](https://github.com/PurpleHaze2320/ai-agent-pulse/actions/workflows/track.yml)
[![Frameworks Tracked](https://img.shields.io/badge/frameworks-19-blue)](https://github.com/PurpleHaze2320/ai-agent-pulse)
[![License: MIT](https://img.shields.io/badge/License-MIT-green.svg)](https://opensource.org/licenses/MIT)
[![GitHub stars](https://img.shields.io/github/stars/PurpleHaze2320/ai-agent-pulse?style=social)](https://github.com/PurpleHaze2320/ai-agent-pulse/stargazers)

> Automated daily tracking of the AI agent framework ecosystem's health, momentum, and trends.
> Last updated: **2026-09-09 11:01 UTC** | Tracking **19** frameworks

## How It Works

This bot runs daily via GitHub Actions and collects metrics from the GitHub API for the most important
AI agent frameworks. It computes a **Pulse Score** (0-100) based on six weighted signals: star velocity,
release freshness, issue health, commit activity, community size, and fork engagement. The result is
a living dashboard that shows which frameworks are gaining momentum and which are losing steam.

## 🏆 Pulse Leaderboard

| Rank | Framework | Pulse | Stars | ⭐ 7d | Commits (4w) | Last Release | Category |
|------|-----------|-------|-------|-------|--------------|--------------|----------|
| 1 | [BrowserUse](https://github.com/browser-use/browser-use) | 🟢 **90.1** | 113.9k | 🚀 +1828 | 185 | 5 days ago | `web-agent` |
| 2 | [CrewAI](https://github.com/crewAIInc/crewAI) | 🟢 **79.9** | 58.3k | 🚀 +287 | 92 | 4 days ago | `multi-agent` |
| 3 | [Mastra](https://github.com/mastra-ai/mastra) | 🟢 **77.3** | 27.8k | 🚀 +196 | 1308 | today | `typescript` |
| 4 | [OpenAI Agents SDK](https://github.com/openai/openai-agents-python) | 🟢 **77.1** | 29.3k | 🚀 +158 | 152 | 1 day ago | `orchestration` |
| 5 | [PydanticAI](https://github.com/pydantic/pydantic-ai) | 🟢 **75.0** | 19.8k | 🚀 +159 | 243 | today | `structured` |
| 6 | [Google ADK](https://github.com/google/adk-python) | 🟢 **73.3** | 21.5k | 📈 +89 | 369 | 12 days ago | `orchestration` |
| 7 | [Claude Agent SDK](https://github.com/anthropics/claude-code) | 🟢 **70.7** | 144.5k | 🚀 +762 | 26 | today | `orchestration` |
| 8 | [Agno](https://github.com/agno-agi/agno) | 🟢 **70.4** | 42.1k | 🚀 +102 | 96 | today | `multi-agent` |
| 9 | [LangGraph](https://github.com/langchain-ai/langgraph) | 🟡 **69.4** | 41.3k | 🚀 +398 | 33 | 12 days ago | `orchestration` |
| 10 | [Composio](https://github.com/ComposioHQ/composio) | 🟡 **67.8** | 30.1k | 📈 +96 | 218 | today | `tooling` |
| 11 | [LlamaIndex](https://github.com/run-llama/llama_index) | 🟡 **61.5** | 52.1k | 🚀 +110 | 33 | 20 days ago | `data-agent` |
| 12 | [DSPy](https://github.com/stanfordnlp/dspy) | 🟡 **61.4** | 37.9k | 🚀 +152 | 51 | 18 days ago | `optimization` |
| 13 | [AG2](https://github.com/ag2ai/ag2) | 🟡 **58.5** | 4.9k | ↗️ +17 | 43 | 2 days ago | `multi-agent` |
| 14 | [Semantic Kernel](https://github.com/microsoft/semantic-kernel) | 🟡 **55.0** | 28.5k | 📈 +26 | 23 | 5 days ago | `enterprise` |
| 15 | [Haystack](https://github.com/deepset-ai/haystack) | 🟡 **50.9** | 26.5k | 📈 +57 | 0 | 6 days ago | `pipeline` |
| 16 | [Letta](https://github.com/letta-ai/letta) | 🟡 **40.1** | 24.7k | 🚀 +112 | 1 | 3 mo ago | `memory` |
| 17 | [Smolagents](https://github.com/huggingface/smolagents) | 🟠 **37.7** | 29.3k | 🚀 +135 | 2 | 3 mo ago | `lightweight` |
| 18 | [AutoGen](https://github.com/microsoft/autogen) | 🟠 **34.0** | 60.9k | 🚀 +134 | 0 | 11 mo ago | `multi-agent` |
| 19 | [Swarm](https://github.com/openai/swarm) | 🔴 **9.6** | 22.0k | 📈 +25 | 0 | — | `experimental` |

## 📂 By Category

- `data-agent`: **LlamaIndex** (61.5)
- `enterprise`: **Semantic Kernel** (55.0)
- `experimental`: **Swarm** (9.6)
- `lightweight`: **Smolagents** (37.7)
- `memory`: **Letta** (40.1)
- `multi-agent`: **CrewAI** (79.9), **Agno** (70.4), **AG2** (58.5), **AutoGen** (34.0)
- `optimization`: **DSPy** (61.4)
- `orchestration`: **OpenAI Agents SDK** (77.1), **Google ADK** (73.3), **Claude Agent SDK** (70.7), **LangGraph** (69.4)
- `pipeline`: **Haystack** (50.9)
- `structured`: **PydanticAI** (75.0)
- `tooling`: **Composio** (67.8)
- `typescript`: **Mastra** (77.3)
- `web-agent`: **BrowserUse** (90.1)

## 🔍 Top 5 — Score Breakdown

| Framework | Star Velocity | Release Freshness | Issue Health | Commit Activity | Community | Fork Ratio |
|-----------|:---:|:---:|:---:|:---:|:---:|:---:|
| **BrowserUse** | 100 | 98.3 | 92.5 | 100 | 72.0 | 43.9 |
| **CrewAI** | 61.0 | 98.7 | 95.8 | 92.0 | 63.4 | 57.6 |
| **Mastra** | 38.9 | 100.0 | 95.2 | 100 | 93.0 | 39.4 |
| **OpenAI Agents SDK** | 33.7 | 99.7 | 99.1 | 100 | 74.6 | 63.9 |
| **PydanticAI** | 31.9 | 100.0 | 81.0 | 100 | 95.0 | 54.0 |

## 💡 Key Insights

- **Hottest framework**: BrowserUse with a Pulse Score of 90.1
- **Fastest growing**: BrowserUse gained +1828 stars this week
- **Most active development**: Mastra with 1308 commits in the last 4 weeks
- **Stale releases**: AutoGen, Swarm haven't released in a while

## 📦 Recent Releases

- **Mastra** [`@mastra/core@1.65.0`](https://github.com/mastra-ai/mastra/releases/tag/@mastra/core@1.65.0) — today
- **PydanticAI** [`v2.42.0`](https://github.com/pydantic/pydantic-ai/releases/tag/v2.42.0) — today
- **Claude Agent SDK** [`v2.1.266`](https://github.com/anthropics/claude-code/releases/tag/v2.1.266) — today
- **Agno** [`v3.0.9`](https://github.com/agno-agi/agno/releases/tag/v3.0.9) — today
- **Composio** [`@composio/cli@0.4.2-beta.384`](https://github.com/ComposioHQ/composio/releases/tag/@composio/cli@0.4.2-beta.384) — today *(pre-release)*
- **OpenAI Agents SDK** [`v0.22.1`](https://github.com/openai/openai-agents-python/releases/tag/v0.22.1) — 1 day ago
- **AG2** [`v1.0.4`](https://github.com/ag2ai/ag2/releases/tag/v1.0.4) — 2 days ago
- **CrewAI** [`1.15.20`](https://github.com/crewAIInc/crewAI/releases/tag/1.15.20) — 4 days ago
- **BrowserUse** [`0.13.10`](https://github.com/browser-use/browser-use/releases/tag/0.13.10) — 5 days ago
- **Semantic Kernel** [`dotnet-1.80.1`](https://github.com/microsoft/semantic-kernel/releases/tag/dotnet-1.80.1) — 5 days ago

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

*Powered by GitHub Actions • Data refreshed daily • Last run: 2026-09-09 11:01 UTC*