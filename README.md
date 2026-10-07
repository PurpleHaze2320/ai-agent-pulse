# 🔬 AI Agent Framework Pulse Tracker

[![Daily Update](https://github.com/PurpleHaze2320/ai-agent-pulse/actions/workflows/track.yml/badge.svg)](https://github.com/PurpleHaze2320/ai-agent-pulse/actions/workflows/track.yml)
[![Frameworks Tracked](https://img.shields.io/badge/frameworks-19-blue)](https://github.com/PurpleHaze2320/ai-agent-pulse)
[![License: MIT](https://img.shields.io/badge/License-MIT-green.svg)](https://opensource.org/licenses/MIT)
[![GitHub stars](https://img.shields.io/github/stars/PurpleHaze2320/ai-agent-pulse?style=social)](https://github.com/PurpleHaze2320/ai-agent-pulse/stargazers)

> Automated daily tracking of the AI agent framework ecosystem's health, momentum, and trends.
> Last updated: **2026-10-07 13:00 UTC** | Tracking **19** frameworks

## How It Works

This bot runs daily via GitHub Actions and collects metrics from the GitHub API for the most important
AI agent frameworks. It computes a **Pulse Score** (0-100) based on six weighted signals: star velocity,
release freshness, issue health, commit activity, community size, and fork engagement. The result is
a living dashboard that shows which frameworks are gaining momentum and which are losing steam.

## 🏆 Pulse Leaderboard

| Rank | Framework | Pulse | Stars | ⭐ 7d | Commits (4w) | Last Release | Category |
|------|-----------|-------|-------|-------|--------------|--------------|----------|
| 1 | [Claude Agent SDK](https://github.com/anthropics/claude-code) | 🟢 **81.5** | 149.7k | 🚀 +1058 | 78 | today | `orchestration` |
| 2 | [BrowserUse](https://github.com/browser-use/browser-use) | 🟢 **81.3** | 117.3k | 🚀 +556 | 56 | today | `web-agent` |
| 3 | [Mastra](https://github.com/mastra-ai/mastra) | 🟢 **76.5** | 28.6k | 🚀 +164 | 1990 | 2 days ago | `typescript` |
| 4 | [OpenAI Agents SDK](https://github.com/openai/openai-agents-python) | 🟢 **74.9** | 29.9k | 📈 +95 | 228 | 4 days ago | `orchestration` |
| 5 | [Agno](https://github.com/agno-agi/agno) | 🟢 **73.8** | 42.6k | 🚀 +199 | 99 | 5 days ago | `multi-agent` |
| 6 | [LangGraph](https://github.com/langchain-ai/langgraph) | 🟢 **72.4** | 42.8k | 🚀 +309 | 65 | today | `orchestration` |
| 7 | [Google ADK](https://github.com/google/adk-python) | 🟢 **72.2** | 21.7k | 📈 +43 | 424 | 5 days ago | `orchestration` |
| 8 | [CrewAI](https://github.com/crewAIInc/crewAI) | 🟢 **71.4** | 59.4k | 🚀 +198 | 71 | 8 days ago | `multi-agent` |
| 9 | [AG2](https://github.com/ag2ai/ag2) | 🟡 **68.4** | 5.0k | ↗️ +13 | 94 | 4 days ago | `multi-agent` |
| 10 | [Composio](https://github.com/ComposioHQ/composio) | 🟡 **67.2** | 30.5k | 📈 +91 | 272 | today | `tooling` |
| 11 | [DSPy](https://github.com/stanfordnlp/dspy) | 🟡 **60.4** | 38.5k | 🚀 +106 | 56 | 12 days ago | `optimization` |
| 12 | [LlamaIndex](https://github.com/run-llama/llama_index) | 🟡 **57.6** | 52.4k | 📈 +60 | 24 | 15 days ago | `data-agent` |
| 13 | [PydanticAI](https://github.com/pydantic/pydantic-ai) | 🟡 **55.2** | 20.5k | 🚀 +184 | 0 | 1 day ago | `structured` |
| 14 | [Semantic Kernel](https://github.com/microsoft/semantic-kernel) | 🟡 **53.8** | 28.6k | ↗️ +15 | 18 | 1 day ago | `enterprise` |
| 15 | [Haystack](https://github.com/deepset-ai/haystack) | 🟡 **50.9** | 26.7k | 📈 +54 | 0 | 6 days ago | `pipeline` |
| 16 | [Letta](https://github.com/letta-ai/letta) | 🟠 **36.8** | 25.1k | 📈 +83 | 0 | 4 mo ago | `memory` |
| 17 | [Smolagents](https://github.com/huggingface/smolagents) | 🟠 **35.6** | 29.7k | 🚀 +117 | 5 | 4 mo ago | `lightweight` |
| 18 | [AutoGen](https://github.com/microsoft/autogen) | 🟠 **30.3** | 61.3k | 📈 +43 | 0 | 1y ago | `multi-agent` |
| 19 | [Swarm](https://github.com/openai/swarm) | 🔴 **9.3** | 22.0k | ↗️ +13 | 0 | — | `experimental` |

## 📂 By Category

- `data-agent`: **LlamaIndex** (57.6)
- `enterprise`: **Semantic Kernel** (53.8)
- `experimental`: **Swarm** (9.3)
- `lightweight`: **Smolagents** (35.6)
- `memory`: **Letta** (36.8)
- `multi-agent`: **Agno** (73.8), **CrewAI** (71.4), **AG2** (68.4), **AutoGen** (30.3)
- `optimization`: **DSPy** (60.4)
- `orchestration`: **Claude Agent SDK** (81.5), **OpenAI Agents SDK** (74.9), **LangGraph** (72.4), **Google ADK** (72.2)
- `pipeline`: **Haystack** (50.9)
- `structured`: **PydanticAI** (55.2)
- `tooling`: **Composio** (67.2)
- `typescript`: **Mastra** (76.5)
- `web-agent`: **BrowserUse** (81.3)

## 🔍 Top 5 — Score Breakdown

| Framework | Star Velocity | Release Freshness | Issue Health | Commit Activity | Community | Fork Ratio |
|-----------|:---:|:---:|:---:|:---:|:---:|:---:|
| **Claude Agent SDK** | 100 | 100.0 | 85.9 | 78.0 | 11.4 | 68.7 |
| **BrowserUse** | 100 | 100.0 | 90.1 | 56.0 | 72.0 | 44.2 |
| **Mastra** | 35.7 | 99.3 | 95.1 | 100 | 93.6 | 40.9 |
| **OpenAI Agents SDK** | 22.8 | 98.7 | 99.6 | 100 | 80.0 | 64.9 |
| **Agno** | 35.6 | 98.3 | 72.4 | 99.0 | 88.0 | 57.4 |

## 💡 Key Insights

- **Hottest framework**: Claude Agent SDK with a Pulse Score of 81.5
- **Fastest growing**: Claude Agent SDK gained +1058 stars this week
- **Most active development**: Mastra with 1990 commits in the last 4 weeks
- **Stale releases**: AutoGen, Swarm haven't released in a while

## 📦 Recent Releases

- **Composio** [`@composio/cli@0.4.3-beta.414`](https://github.com/ComposioHQ/composio/releases/tag/@composio/cli@0.4.3-beta.414) — today *(pre-release)*
- **BrowserUse** [`0.13.11`](https://github.com/browser-use/browser-use/releases/tag/0.13.11) — today
- **Claude Agent SDK** [`v2.1.292`](https://github.com/anthropics/claude-code/releases/tag/v2.1.292) — today
- **LangGraph** [`1.2.14`](https://github.com/langchain-ai/langgraph/releases/tag/1.2.14) — today
- **Semantic Kernel** [`python-1.45.0`](https://github.com/microsoft/semantic-kernel/releases/tag/python-1.45.0) — 1 day ago
- **PydanticAI** [`clai2-bleeding`](https://github.com/pydantic/pydantic-ai/releases/tag/clai2-bleeding) — 1 day ago *(pre-release)*
- **Mastra** [`@mastra/core@1.74.0`](https://github.com/mastra-ai/mastra/releases/tag/@mastra/core@1.74.0) — 2 days ago
- **AG2** [`v1.1.2`](https://github.com/ag2ai/ag2/releases/tag/v1.1.2) — 4 days ago
- **OpenAI Agents SDK** [`v0.23.1`](https://github.com/openai/openai-agents-python/releases/tag/v0.23.1) — 4 days ago
- **Agno** [`v3.1.1`](https://github.com/agno-agi/agno/releases/tag/v3.1.1) — 5 days ago

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

*Powered by GitHub Actions • Data refreshed daily • Last run: 2026-10-07 13:00 UTC*