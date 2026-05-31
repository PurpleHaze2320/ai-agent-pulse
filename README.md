# 🔬 AI Agent Framework Pulse Tracker

[![Daily Update](https://github.com/PurpleHaze2320/ai-agent-pulse/actions/workflows/track.yml/badge.svg)](https://github.com/PurpleHaze2320/ai-agent-pulse/actions/workflows/track.yml)
[![Frameworks Tracked](https://img.shields.io/badge/frameworks-19-blue)](https://github.com/PurpleHaze2320/ai-agent-pulse)
[![License: MIT](https://img.shields.io/badge/License-MIT-green.svg)](https://opensource.org/licenses/MIT)
[![GitHub stars](https://img.shields.io/github/stars/PurpleHaze2320/ai-agent-pulse?style=social)](https://github.com/PurpleHaze2320/ai-agent-pulse/stargazers)

> Automated daily tracking of the AI agent framework ecosystem's health, momentum, and trends.
> Last updated: **2026-05-31 08:54 UTC** | Tracking **19** frameworks

## How It Works

This bot runs daily via GitHub Actions and collects metrics from the GitHub API for the most important
AI agent frameworks. It computes a **Pulse Score** (0-100) based on six weighted signals: star velocity,
release freshness, issue health, commit activity, community size, and fork engagement. The result is
a living dashboard that shows which frameworks are gaining momentum and which are losing steam.

## 🏆 Pulse Leaderboard

| Rank | Framework | Pulse | Stars | ⭐ 7d | Commits (4w) | Last Release | Category |
|------|-----------|-------|-------|-------|--------------|--------------|----------|
| 1 | [Mastra](https://github.com/mastra-ai/mastra) | 🟢 **82.5** | 24.6k | 🚀 +333 | 732 | 3 days ago | `typescript` |
| 2 | [BrowserUse](https://github.com/browser-use/browser-use) | 🟡 **69.8** | 96.4k | 🚀 +1087 | 0 | 5 days ago | `web-agent` |
| 3 | [CrewAI](https://github.com/crewAIInc/crewAI) | 🟡 **69.4** | 52.5k | 🚀 +441 | 0 | 2 days ago | `multi-agent` |
| 4 | [LangGraph](https://github.com/langchain-ai/langgraph) | 🟡 **68.6** | 33.4k | 🚀 +630 | 0 | 2 days ago | `orchestration` |
| 5 | [Claude Agent SDK](https://github.com/anthropics/claude-code) | 🟡 **65.4** | 128.5k | 🚀 +2457 | 0 | 1 day ago | `orchestration` |
| 6 | [LlamaIndex](https://github.com/run-llama/llama_index) | 🟡 **57.5** | 49.8k | 🚀 +165 | 0 | 16 days ago | `data-agent` |
| 7 | [OpenAI Agents SDK](https://github.com/openai/openai-agents-python) | 🟡 **56.2** | 26.8k | 🚀 +174 | 0 | 4 days ago | `orchestration` |
| 8 | [PydanticAI](https://github.com/pydantic/pydantic-ai) | 🟡 **54.4** | 17.4k | 🚀 +159 | 0 | 2 days ago | `structured` |
| 9 | [Agno](https://github.com/agno-agi/agno) | 🟡 **52.2** | 40.4k | 🚀 +114 | 0 | 9 days ago | `multi-agent` |
| 10 | [Semantic Kernel](https://github.com/microsoft/semantic-kernel) | 🟡 **51.3** | 28.0k | 📈 +48 | 0 | 2 days ago | `enterprise` |
| 11 | [DSPy](https://github.com/stanfordnlp/dspy) | 🟡 **50.5** | 34.7k | 🚀 +134 | 0 | 3 days ago | `optimization` |
| 12 | [Google ADK](https://github.com/google/adk-python) | 🟡 **50.2** | 19.9k | 🚀 +108 | 0 | 8 days ago | `orchestration` |
| 13 | [AG2](https://github.com/ag2ai/ag2) | 🟡 **48.6** | 4.6k | ↗️ +18 | 0 | 2 days ago | `multi-agent` |
| 14 | [Haystack](https://github.com/deepset-ai/haystack) | 🟡 **48.4** | 25.4k | 📈 +59 | 0 | 18 days ago | `pipeline` |
| 15 | [Letta](https://github.com/letta-ai/letta) | 🟡 **47.7** | 23.1k | 🚀 +131 | 0 | 16 days ago | `memory` |
| 16 | [Composio](https://github.com/ComposioHQ/composio) | 🟡 **47.3** | 28.5k | 🚀 +117 | 0 | 10 days ago | `tooling` |
| 17 | [Smolagents](https://github.com/huggingface/smolagents) | 🟡 **44.8** | 27.6k | 🚀 +134 | 0 | 2 days ago | `lightweight` |
| 18 | [AutoGen](https://github.com/microsoft/autogen) | 🟡 **42.3** | 58.6k | 🚀 +219 | 0 | 8 mo ago | `multi-agent` |
| 19 | [Swarm](https://github.com/openai/swarm) | 🔴 **9.2** | 21.6k | 📈 +31 | 0 | — | `experimental` |

## 📂 By Category

- `data-agent`: **LlamaIndex** (57.5)
- `enterprise`: **Semantic Kernel** (51.3)
- `experimental`: **Swarm** (9.2)
- `lightweight`: **Smolagents** (44.8)
- `memory`: **Letta** (47.7)
- `multi-agent`: **CrewAI** (69.4), **Agno** (52.2), **AG2** (48.6), **AutoGen** (42.3)
- `optimization`: **DSPy** (50.5)
- `orchestration`: **LangGraph** (68.6), **Claude Agent SDK** (65.4), **OpenAI Agents SDK** (56.2), **Google ADK** (50.2)
- `pipeline`: **Haystack** (48.4)
- `structured`: **PydanticAI** (54.4)
- `tooling`: **Composio** (47.3)
- `typescript`: **Mastra** (82.5)
- `web-agent`: **BrowserUse** (69.8)

## 🔍 Top 5 — Score Breakdown

| Framework | Star Velocity | Release Freshness | Issue Health | Commit Activity | Community | Fork Ratio |
|-----------|:---:|:---:|:---:|:---:|:---:|:---:|
| **Mastra** | 63.4 | 99.0 | 95.6 | 100 | 90.2 | 35.2 |
| **BrowserUse** | 100 | 98.3 | 95.7 | 0.0 | 63.0 | 44.8 |
| **CrewAI** | 93.3 | 99.3 | 98.0 | 0.0 | 59.4 | 55.7 |
| **LangGraph** | 100 | 99.3 | 76.3 | 0.0 | 55.0 | 67.6 |
| **Claude Agent SDK** | 100 | 99.7 | 86.5 | 0.0 | 10.2 | 65.2 |

## 💡 Key Insights

- **Hottest framework**: Mastra with a Pulse Score of 82.5
- **Fastest growing**: Claude Agent SDK gained +2457 stars this week
- **Most active development**: Mastra with 732 commits in the last 4 weeks
- **Stale releases**: Swarm haven't released in a while

## 📦 Recent Releases

- **Claude Agent SDK** [`v2.1.158`](https://github.com/anthropics/claude-code/releases/tag/v2.1.158) — 1 day ago
- **Smolagents** [`v1.26.0`](https://github.com/huggingface/smolagents/releases/tag/v1.26.0) — 2 days ago
- **PydanticAI** [`v2.0.0b4`](https://github.com/pydantic/pydantic-ai/releases/tag/v2.0.0b4) — 2 days ago *(pre-release)*
- **AG2** [`v0.13.2`](https://github.com/ag2ai/ag2/releases/tag/v0.13.2) — 2 days ago
- **CrewAI** [`1.14.6`](https://github.com/crewAIInc/crewAI/releases/tag/1.14.6) — 2 days ago
- **LangGraph** [`sdk==0.4.0`](https://github.com/langchain-ai/langgraph/releases/tag/sdk==0.4.0) — 2 days ago
- **Semantic Kernel** [`dotnet-1.77.0`](https://github.com/microsoft/semantic-kernel/releases/tag/dotnet-1.77.0) — 2 days ago
- **DSPy** [`3.3.0b1`](https://github.com/stanfordnlp/dspy/releases/tag/3.3.0b1) — 3 days ago *(pre-release)*
- **Mastra** [`@mastra/core@1.37.0`](https://github.com/mastra-ai/mastra/releases/tag/@mastra/core@1.37.0) — 3 days ago
- **OpenAI Agents SDK** [`v0.17.4`](https://github.com/openai/openai-agents-python/releases/tag/v0.17.4) — 4 days ago

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

*Powered by GitHub Actions • Data refreshed daily • Last run: 2026-05-31 08:54 UTC*