# 🔬 AI Agent Framework Pulse Tracker

[![Daily Update](https://github.com/PurpleHaze2320/ai-agent-pulse/actions/workflows/track.yml/badge.svg)](https://github.com/PurpleHaze2320/ai-agent-pulse/actions/workflows/track.yml)
[![Frameworks Tracked](https://img.shields.io/badge/frameworks-19-blue)](https://github.com/PurpleHaze2320/ai-agent-pulse)
[![License: MIT](https://img.shields.io/badge/License-MIT-green.svg)](https://opensource.org/licenses/MIT)
[![GitHub stars](https://img.shields.io/github/stars/PurpleHaze2320/ai-agent-pulse?style=social)](https://github.com/PurpleHaze2320/ai-agent-pulse/stargazers)

> Automated daily tracking of the AI agent framework ecosystem's health, momentum, and trends.
> Last updated: **2026-04-30 08:30 UTC** | Tracking **19** frameworks

## How It Works

This bot runs daily via GitHub Actions and collects metrics from the GitHub API for the most important
AI agent frameworks. It computes a **Pulse Score** (0-100) based on six weighted signals: star velocity,
release freshness, issue health, commit activity, community size, and fork engagement. The result is
a living dashboard that shows which frameworks are gaining momentum and which are losing steam.

## 🏆 Pulse Leaderboard

| Rank | Framework | Pulse | Stars | ⭐ 7d | Commits (4w) | Last Release | Category |
|------|-----------|-------|-------|-------|--------------|--------------|----------|
| 1 | [Mastra](https://github.com/mastra-ai/mastra) | 🟢 **75.8** | 23.4k | 🚀 +194 | 770 | today | `typescript` |
| 2 | [CrewAI](https://github.com/crewAIInc/crewAI) | 🟢 **70.8** | 50.3k | 🚀 +701 | 0 | today | `multi-agent` |
| 3 | [OpenAI Agents SDK](https://github.com/openai/openai-agents-python) | 🟢 **70.7** | 25.6k | 🚀 +856 | 0 | 1 day ago | `orchestration` |
| 4 | [LangGraph](https://github.com/langchain-ai/langgraph) | 🟡 **69.2** | 30.9k | 🚀 +763 | 0 | today | `orchestration` |
| 5 | [BrowserUse](https://github.com/browser-use/browser-use) | 🟡 **68.5** | 91.3k | 🚀 +1688 | 0 | 28 days ago | `web-agent` |
| 6 | [Claude Agent SDK](https://github.com/anthropics/claude-code) | 🟡 **64.6** | 119.4k | 🚀 +2260 | 0 | 1 day ago | `orchestration` |
| 7 | [LlamaIndex](https://github.com/run-llama/llama_index) | 🟡 **60.2** | 49.1k | 🚀 +218 | 0 | 9 days ago | `data-agent` |
| 8 | [Agno](https://github.com/agno-agi/agno) | 🟡 **55.4** | 39.8k | 🚀 +190 | 0 | 1 day ago | `multi-agent` |
| 9 | [PydanticAI](https://github.com/pydantic/pydantic-ai) | 🟡 **54.9** | 16.7k | 🚀 +183 | 0 | 1 day ago | `structured` |
| 10 | [Google ADK](https://github.com/google/adk-python) | 🟡 **52.1** | 19.4k | 🚀 +157 | 0 | 7 days ago | `orchestration` |
| 11 | [Semantic Kernel](https://github.com/microsoft/semantic-kernel) | 🟡 **51.6** | 27.8k | 📈 +57 | 0 | today | `enterprise` |
| 12 | [DSPy](https://github.com/stanfordnlp/dspy) | 🟡 **51.4** | 34.1k | 🚀 +170 | 0 | 8 days ago | `optimization` |
| 13 | [Haystack](https://github.com/deepset-ai/haystack) | 🟡 **49.2** | 25.0k | 📈 +74 | 0 | 9 days ago | `pipeline` |
| 14 | [AG2](https://github.com/ag2ai/ag2) | 🟡 **48.5** | 4.5k | 📈 +33 | 0 | 5 days ago | `multi-agent` |
| 15 | [Letta](https://github.com/letta-ai/letta) | 🟡 **46.6** | 22.4k | 🚀 +147 | 0 | 29 days ago | `memory` |
| 16 | [AutoGen](https://github.com/microsoft/autogen) | 🟡 **45.4** | 57.6k | 🚀 +240 | 0 | 7 mo ago | `multi-agent` |
| 17 | [Composio](https://github.com/ComposioHQ/composio) | 🟡 **45.1** | 28.0k | 📈 +92 | 0 | 2 days ago | `tooling` |
| 18 | [Smolagents](https://github.com/huggingface/smolagents) | 🟠 **38.7** | 27.0k | 🚀 +161 | 0 | 3 mo ago | `lightweight` |
| 19 | [Swarm](https://github.com/openai/swarm) | 🔴 **9.9** | 21.4k | 📈 +42 | 0 | — | `experimental` |

## 📂 By Category

- `data-agent`: **LlamaIndex** (60.2)
- `enterprise`: **Semantic Kernel** (51.6)
- `experimental`: **Swarm** (9.9)
- `lightweight`: **Smolagents** (38.7)
- `memory`: **Letta** (46.6)
- `multi-agent`: **CrewAI** (70.8), **Agno** (55.4), **AG2** (48.5), **AutoGen** (45.4)
- `optimization`: **DSPy** (51.4)
- `orchestration`: **OpenAI Agents SDK** (70.7), **LangGraph** (69.2), **Claude Agent SDK** (64.6), **Google ADK** (52.1)
- `pipeline`: **Haystack** (49.2)
- `structured`: **PydanticAI** (54.9)
- `tooling`: **Composio** (45.1)
- `typescript`: **Mastra** (75.8)
- `web-agent`: **BrowserUse** (68.5)

## 🔍 Top 5 — Score Breakdown

| Framework | Star Velocity | Release Freshness | Issue Health | Commit Activity | Community | Fork Ratio |
|-----------|:---:|:---:|:---:|:---:|:---:|:---:|
| **Mastra** | 40.1 | 100.0 | 94.4 | 100 | 82.2 | 33.8 |
| **CrewAI** | 100 | 100.0 | 96.5 | 0.0 | 58.0 | 55.1 |
| **OpenAI Agents SDK** | 100 | 99.7 | 96.5 | 0.0 | 52.2 | 61.0 |
| **LangGraph** | 100 | 100.0 | 78.9 | 0.0 | 55.0 | 68.3 |
| **BrowserUse** | 100 | 90.7 | 97.1 | 0.0 | 62.2 | 45.6 |

## 💡 Key Insights

- **Hottest framework**: Mastra with a Pulse Score of 75.8
- **Fastest growing**: Claude Agent SDK gained +2260 stars this week
- **Most active development**: Mastra with 770 commits in the last 4 weeks
- **Stale releases**: Swarm haven't released in a while

## 📦 Recent Releases

- **Mastra** [`@mastra/core@1.29.0`](https://github.com/mastra-ai/mastra/releases/tag/@mastra/core@1.29.0) — today
- **LangGraph** [`prebuilt==1.0.13`](https://github.com/langchain-ai/langgraph/releases/tag/prebuilt==1.0.13) — today
- **CrewAI** [`1.14.4a2`](https://github.com/crewAIInc/crewAI/releases/tag/1.14.4a2) — today *(pre-release)*
- **Semantic Kernel** [`dotnet-1.75.0`](https://github.com/microsoft/semantic-kernel/releases/tag/dotnet-1.75.0) — today
- **PydanticAI** [`v1.88.0`](https://github.com/pydantic/pydantic-ai/releases/tag/v1.88.0) — 1 day ago
- **OpenAI Agents SDK** [`v0.14.8`](https://github.com/openai/openai-agents-python/releases/tag/v0.14.8) — 1 day ago
- **Claude Agent SDK** [`v2.1.123`](https://github.com/anthropics/claude-code/releases/tag/v2.1.123) — 1 day ago
- **Agno** [`v2.6.4`](https://github.com/agno-agi/agno/releases/tag/v2.6.4) — 1 day ago
- **Composio** [`py@0.12.0`](https://github.com/ComposioHQ/composio/releases/tag/py@0.12.0) — 2 days ago
- **AG2** [`v0.12.1`](https://github.com/ag2ai/ag2/releases/tag/v0.12.1) — 5 days ago

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

*Powered by GitHub Actions • Data refreshed daily • Last run: 2026-04-30 08:30 UTC*