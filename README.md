# 🔬 AI Agent Framework Pulse Tracker

[![Daily Update](https://github.com/PurpleHaze2320/ai-agent-pulse/actions/workflows/track.yml/badge.svg)](https://github.com/PurpleHaze2320/ai-agent-pulse/actions/workflows/track.yml)
[![Frameworks Tracked](https://img.shields.io/badge/frameworks-19-blue)](https://github.com/PurpleHaze2320/ai-agent-pulse)
[![License: MIT](https://img.shields.io/badge/License-MIT-green.svg)](https://opensource.org/licenses/MIT)
[![GitHub stars](https://img.shields.io/github/stars/PurpleHaze2320/ai-agent-pulse?style=social)](https://github.com/PurpleHaze2320/ai-agent-pulse/stargazers)

> Automated daily tracking of the AI agent framework ecosystem's health, momentum, and trends.
> Last updated: **2026-05-13 08:52 UTC** | Tracking **19** frameworks

## How It Works

This bot runs daily via GitHub Actions and collects metrics from the GitHub API for the most important
AI agent frameworks. It computes a **Pulse Score** (0-100) based on six weighted signals: star velocity,
release freshness, issue health, commit activity, community size, and fork engagement. The result is
a living dashboard that shows which frameworks are gaining momentum and which are losing steam.

## 🏆 Pulse Leaderboard

| Rank | Framework | Pulse | Stars | ⭐ 7d | Commits (4w) | Last Release | Category |
|------|-----------|-------|-------|-------|--------------|--------------|----------|
| 1 | [Mastra](https://github.com/mastra-ai/mastra) | 🟢 **76.3** | 23.8k | 🚀 +199 | 936 | 6 days ago | `typescript` |
| 2 | [CrewAI](https://github.com/crewAIInc/crewAI) | 🟢 **71.3** | 51.3k | 🚀 +520 | 0 | today | `multi-agent` |
| 3 | [OpenAI Agents SDK](https://github.com/openai/openai-agents-python) | 🟢 **70.9** | 26.3k | 🚀 +292 | 0 | 1 day ago | `orchestration` |
| 4 | [LangGraph](https://github.com/langchain-ai/langgraph) | 🟡 **68.9** | 31.9k | 🚀 +541 | 0 | 1 day ago | `orchestration` |
| 5 | [BrowserUse](https://github.com/browser-use/browser-use) | 🟡 **67.5** | 93.7k | 🚀 +1058 | 0 | 1 mo ago | `web-agent` |
| 6 | [Claude Agent SDK](https://github.com/anthropics/claude-code) | 🟡 **64.8** | 123.1k | 🚀 +1941 | 0 | today | `orchestration` |
| 7 | [LlamaIndex](https://github.com/run-llama/llama_index) | 🟡 **58.5** | 49.4k | 🚀 +191 | 0 | 22 days ago | `data-agent` |
| 8 | [PydanticAI](https://github.com/pydantic/pydantic-ai) | 🟡 **54.3** | 17.0k | 🚀 +156 | 0 | today | `structured` |
| 9 | [Agno](https://github.com/agno-agi/agno) | 🟡 **52.9** | 40.1k | 🚀 +131 | 0 | 6 days ago | `multi-agent` |
| 10 | [Haystack](https://github.com/deepset-ai/haystack) | 🟡 **51.3** | 25.2k | 🚀 +109 | 0 | today | `pipeline` |
| 11 | [Google ADK](https://github.com/google/adk-python) | 🟡 **51.3** | 19.6k | 🚀 +123 | 0 | 4 days ago | `orchestration` |
| 12 | [Semantic Kernel](https://github.com/microsoft/semantic-kernel) | 🟡 **51.2** | 27.9k | 📈 +46 | 0 | 1 day ago | `enterprise` |
| 13 | [DSPy](https://github.com/stanfordnlp/dspy) | 🟡 **50.5** | 34.4k | 🚀 +134 | 0 | 7 days ago | `optimization` |
| 14 | [AG2](https://github.com/ag2ai/ag2) | 🟡 **48.6** | 4.5k | ↗️ +19 | 0 | today | `multi-agent` |
| 15 | [Letta](https://github.com/letta-ai/letta) | 🟡 **48.2** | 22.7k | 🚀 +200 | 0 | 1 mo ago | `memory` |
| 16 | [Composio](https://github.com/ComposioHQ/composio) | 🟡 **47.1** | 28.2k | 📈 +97 | 0 | today | `tooling` |
| 17 | [AutoGen](https://github.com/microsoft/autogen) | 🟡 **43.5** | 58.0k | 🚀 +214 | 0 | 7 mo ago | `multi-agent` |
| 18 | [Smolagents](https://github.com/huggingface/smolagents) | 🟠 **37.9** | 27.3k | 🚀 +153 | 0 | 3 mo ago | `lightweight` |
| 19 | [Swarm](https://github.com/openai/swarm) | 🔴 **9.7** | 21.5k | 📈 +42 | 0 | — | `experimental` |

## 📂 By Category

- `data-agent`: **LlamaIndex** (58.5)
- `enterprise`: **Semantic Kernel** (51.2)
- `experimental`: **Swarm** (9.7)
- `lightweight`: **Smolagents** (37.9)
- `memory`: **Letta** (48.2)
- `multi-agent`: **CrewAI** (71.3), **Agno** (52.9), **AG2** (48.6), **AutoGen** (43.5)
- `optimization`: **DSPy** (50.5)
- `orchestration`: **OpenAI Agents SDK** (70.9), **LangGraph** (68.9), **Claude Agent SDK** (64.8), **Google ADK** (51.3)
- `pipeline`: **Haystack** (51.3)
- `structured`: **PydanticAI** (54.3)
- `tooling`: **Composio** (47.1)
- `typescript`: **Mastra** (76.3)
- `web-agent`: **BrowserUse** (67.5)

## 🔍 Top 5 — Score Breakdown

| Framework | Star Velocity | Release Freshness | Issue Health | Commit Activity | Community | Fork Ratio |
|-----------|:---:|:---:|:---:|:---:|:---:|:---:|
| **Mastra** | 41.3 | 98.0 | 94.7 | 100 | 86.8 | 34.7 |
| **CrewAI** | 100 | 100.0 | 98.9 | 0.0 | 59.2 | 55.3 |
| **OpenAI Agents SDK** | 100 | 99.7 | 96.5 | 0.0 | 53.6 | 61.3 |
| **LangGraph** | 100 | 99.7 | 77.8 | 0.0 | 54.6 | 67.9 |
| **BrowserUse** | 100 | 86.3 | 96.3 | 0.0 | 63.0 | 45.3 |

## 💡 Key Insights

- **Hottest framework**: Mastra with a Pulse Score of 76.3
- **Fastest growing**: Claude Agent SDK gained +1941 stars this week
- **Most active development**: Mastra with 936 commits in the last 4 weeks
- **Stale releases**: Swarm haven't released in a while

## 📦 Recent Releases

- **AG2** [`v0.13.0`](https://github.com/ag2ai/ag2/releases/tag/v0.13.0) — today
- **PydanticAI** [`v1.95.0`](https://github.com/pydantic/pydantic-ai/releases/tag/v1.95.0) — today
- **Claude Agent SDK** [`v2.1.140`](https://github.com/anthropics/claude-code/releases/tag/v2.1.140) — today
- **CrewAI** [`1.14.5a5`](https://github.com/crewAIInc/crewAI/releases/tag/1.14.5a5) — today *(pre-release)*
- **Composio** [`@composio/cli@0.2.30-beta.245`](https://github.com/ComposioHQ/composio/releases/tag/@composio/cli@0.2.30-beta.245) — today *(pre-release)*
- **Haystack** [`v2.29.0`](https://github.com/deepset-ai/haystack/releases/tag/v2.29.0) — today
- **LangGraph** [`1.2.0`](https://github.com/langchain-ai/langgraph/releases/tag/1.2.0) — 1 day ago
- **OpenAI Agents SDK** [`v0.17.2`](https://github.com/openai/openai-agents-python/releases/tag/v0.17.2) — 1 day ago
- **Semantic Kernel** [`dotnet-1.76.0`](https://github.com/microsoft/semantic-kernel/releases/tag/dotnet-1.76.0) — 1 day ago
- **Google ADK** [`v1.33.0`](https://github.com/google/adk-python/releases/tag/v1.33.0) — 4 days ago

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

*Powered by GitHub Actions • Data refreshed daily • Last run: 2026-05-13 08:52 UTC*