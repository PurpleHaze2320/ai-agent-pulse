# 🔬 AI Agent Framework Pulse Tracker

[![Daily Update](https://github.com/PurpleHaze2320/ai-agent-pulse/actions/workflows/track.yml/badge.svg)](https://github.com/PurpleHaze2320/ai-agent-pulse/actions/workflows/track.yml)
[![Frameworks Tracked](https://img.shields.io/badge/frameworks-19-blue)](https://github.com/PurpleHaze2320/ai-agent-pulse)
[![License: MIT](https://img.shields.io/badge/License-MIT-green.svg)](https://opensource.org/licenses/MIT)
[![GitHub stars](https://img.shields.io/github/stars/PurpleHaze2320/ai-agent-pulse?style=social)](https://github.com/PurpleHaze2320/ai-agent-pulse/stargazers)

> Automated daily tracking of the AI agent framework ecosystem's health, momentum, and trends.
> Last updated: **2026-11-19 15:30 UTC** | Tracking **19** frameworks

## How It Works

This bot runs daily via GitHub Actions and collects metrics from the GitHub API for the most important
AI agent frameworks. It computes a **Pulse Score** (0-100) based on six weighted signals: star velocity,
release freshness, issue health, commit activity, community size, and fork engagement. The result is
a living dashboard that shows which frameworks are gaining momentum and which are losing steam.

## 🏆 Pulse Leaderboard

| Rank | Framework | Pulse | Stars | ⭐ 7d | Commits (4w) | Last Release | Category |
|------|-----------|-------|-------|-------|--------------|--------------|----------|
| 1 | [BrowserUse](https://github.com/browser-use/browser-use) | 🟢 **90.0** | 121.5k | 🚀 +660 | 1158 | 3 days ago | `web-agent` |
| 2 | [LangGraph](https://github.com/langchain-ai/langgraph) | 🟢 **81.2** | 45.2k | 🚀 +302 | 108 | today | `orchestration` |
| 3 | [CrewAI](https://github.com/crewAIInc/crewAI) | 🟢 **81.1** | 61.1k | 🚀 +293 | 195 | today | `multi-agent` |
| 4 | [Mastra](https://github.com/mastra-ai/mastra) | 🟢 **76.0** | 29.6k | 🚀 +167 | 2291 | 1 day ago | `typescript` |
| 5 | [OpenAI Agents SDK](https://github.com/openai/openai-agents-python) | 🟢 **74.6** | 30.8k | 🚀 +134 | 92 | 1 day ago | `orchestration` |
| 6 | [Haystack](https://github.com/deepset-ai/haystack) | 🟢 **71.2** | 27.1k | 📈 +54 | 234 | 9 days ago | `pipeline` |
| 7 | [AG2](https://github.com/ag2ai/ag2) | 🟢 **70.1** | 5.1k | ↗️ +16 | 118 | 3 days ago | `multi-agent` |
| 8 | [Composio](https://github.com/ComposioHQ/composio) | 🟡 **69.2** | 31.2k | 🚀 +135 | 302 | today | `tooling` |
| 9 | [Agno](https://github.com/agno-agi/agno) | 🟡 **69.1** | 43.2k | 📈 +63 | 132 | 1 day ago | `multi-agent` |
| 10 | [Semantic Kernel](https://github.com/microsoft/semantic-kernel) | 🟡 **67.6** | 28.8k | 📈 +27 | 83 | 12 days ago | `enterprise` |
| 11 | [Claude Agent SDK](https://github.com/anthropics/claude-code) | 🟡 **65.3** | 156.3k | 🚀 +880 | 0 | today | `orchestration` |
| 12 | [LlamaIndex](https://github.com/run-llama/llama_index) | 🟡 **55.7** | 53.0k | 📈 +81 | 8 | 5 days ago | `data-agent` |
| 13 | [Google ADK](https://github.com/google/adk-python) | 🟡 **54.2** | 22.3k | 📈 +81 | 0 | 6 days ago | `orchestration` |
| 14 | [PydanticAI](https://github.com/pydantic/pydantic-ai) | 🟡 **53.1** | 21.3k | 🚀 +122 | 0 | today | `structured` |
| 15 | [DSPy](https://github.com/stanfordnlp/dspy) | 🟡 **49.0** | 39.1k | 🚀 +116 | 0 | 8 days ago | `optimization` |
| 16 | [AutoGen](https://github.com/microsoft/autogen) | 🟠 **34.5** | 61.9k | 🚀 +150 | 2 | 1y ago | `multi-agent` |
| 17 | [Smolagents](https://github.com/huggingface/smolagents) | 🟠 **34.1** | 30.4k | 🚀 +109 | 16 | 5 mo ago | `lightweight` |
| 18 | [Letta](https://github.com/letta-ai/letta) | 🟠 **32.8** | 25.5k | 📈 +64 | 0 | 6 mo ago | `memory` |
| 19 | [Swarm](https://github.com/openai/swarm) | 🔴 **9.6** | 22.2k | 📈 +25 | 0 | — | `experimental` |

## 📂 By Category

- `data-agent`: **LlamaIndex** (55.7)
- `enterprise`: **Semantic Kernel** (67.6)
- `experimental`: **Swarm** (9.6)
- `lightweight`: **Smolagents** (34.1)
- `memory`: **Letta** (32.8)
- `multi-agent`: **CrewAI** (81.1), **AG2** (70.1), **Agno** (69.1), **AutoGen** (34.5)
- `optimization`: **DSPy** (49.0)
- `orchestration`: **LangGraph** (81.2), **OpenAI Agents SDK** (74.6), **Claude Agent SDK** (65.3), **Google ADK** (54.2)
- `pipeline`: **Haystack** (71.2)
- `structured`: **PydanticAI** (53.1)
- `tooling`: **Composio** (69.2)
- `typescript`: **Mastra** (76.0)
- `web-agent`: **BrowserUse** (90.0)

## 🔍 Top 5 — Score Breakdown

| Framework | Star Velocity | Release Freshness | Issue Health | Commit Activity | Community | Fork Ratio |
|-----------|:---:|:---:|:---:|:---:|:---:|:---:|
| **BrowserUse** | 100 | 99.0 | 90.0 | 100 | 72.2 | 44.7 |
| **LangGraph** | 66.1 | 100.0 | 80.3 | 100 | 57.6 | 69.0 |
| **CrewAI** | 59.0 | 100.0 | 84.5 | 100 | 76.0 | 60.4 |
| **Mastra** | 34.0 | 99.7 | 93.6 | 100 | 93.2 | 42.1 |
| **OpenAI Agents SDK** | 27.8 | 99.7 | 98.2 | 92.0 | 80.2 | 66.0 |

## 💡 Key Insights

- **Hottest framework**: BrowserUse with a Pulse Score of 90.0
- **Fastest growing**: Claude Agent SDK gained +880 stars this week
- **Most active development**: Mastra with 2291 commits in the last 4 weeks
- **Stale releases**: AutoGen, Swarm haven't released in a while

## 📦 Recent Releases

- **Composio** [`@composio/cli@0.6.3-beta.570`](https://github.com/ComposioHQ/composio/releases/tag/@composio/cli@0.6.3-beta.570) — today *(pre-release)*
- **LangGraph** [`1.2.23`](https://github.com/langchain-ai/langgraph/releases/tag/1.2.23) — today
- **CrewAI** [`1.15.43`](https://github.com/crewAIInc/crewAI/releases/tag/1.15.43) — today
- **PydanticAI** [`v2.71.0`](https://github.com/pydantic/pydantic-ai/releases/tag/v2.71.0) — today
- **Claude Agent SDK** [`v2.1.328`](https://github.com/anthropics/claude-code/releases/tag/v2.1.328) — today
- **Mastra** [`@mastra/core@1.84.0`](https://github.com/mastra-ai/mastra/releases/tag/@mastra/core@1.84.0) — 1 day ago
- **OpenAI Agents SDK** [`v0.25.0`](https://github.com/openai/openai-agents-python/releases/tag/v0.25.0) — 1 day ago
- **Agno** [`v3.2.1`](https://github.com/agno-agi/agno/releases/tag/v3.2.1) — 1 day ago
- **BrowserUse** [`1.0.6`](https://github.com/browser-use/browser-use/releases/tag/1.0.6) — 3 days ago
- **AG2** [`v1.3.2`](https://github.com/ag2ai/ag2/releases/tag/v1.3.2) — 3 days ago

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

*Powered by GitHub Actions • Data refreshed daily • Last run: 2026-11-19 15:30 UTC*