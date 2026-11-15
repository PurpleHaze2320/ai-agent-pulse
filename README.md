# 🔬 AI Agent Framework Pulse Tracker

[![Daily Update](https://github.com/PurpleHaze2320/ai-agent-pulse/actions/workflows/track.yml/badge.svg)](https://github.com/PurpleHaze2320/ai-agent-pulse/actions/workflows/track.yml)
[![Frameworks Tracked](https://img.shields.io/badge/frameworks-19-blue)](https://github.com/PurpleHaze2320/ai-agent-pulse)
[![License: MIT](https://img.shields.io/badge/License-MIT-green.svg)](https://opensource.org/licenses/MIT)
[![GitHub stars](https://img.shields.io/github/stars/PurpleHaze2320/ai-agent-pulse?style=social)](https://github.com/PurpleHaze2320/ai-agent-pulse/stargazers)

> Automated daily tracking of the AI agent framework ecosystem's health, momentum, and trends.
> Last updated: **2026-11-15 13:44 UTC** | Tracking **19** frameworks

## How It Works

This bot runs daily via GitHub Actions and collects metrics from the GitHub API for the most important
AI agent frameworks. It computes a **Pulse Score** (0-100) based on six weighted signals: star velocity,
release freshness, issue health, commit activity, community size, and fork engagement. The result is
a living dashboard that shows which frameworks are gaining momentum and which are losing steam.

## 🏆 Pulse Leaderboard

| Rank | Framework | Pulse | Stars | ⭐ 7d | Commits (4w) | Last Release | Category |
|------|-----------|-------|-------|-------|--------------|--------------|----------|
| 1 | [BrowserUse](https://github.com/browser-use/browser-use) | 🟢 **90.2** | 121.1k | 🚀 +774 | 1132 | 1 day ago | `web-agent` |
| 2 | [LangGraph](https://github.com/langchain-ai/langgraph) | 🟢 **82.7** | 45.0k | 🚀 +343 | 100 | 1 day ago | `orchestration` |
| 3 | [Claude Agent SDK](https://github.com/anthropics/claude-code) | 🟢 **80.8** | 155.7k | 🚀 +794 | 78 | 1 day ago | `orchestration` |
| 4 | [CrewAI](https://github.com/crewAIInc/crewAI) | 🟢 **80.6** | 60.9k | 🚀 +300 | 156 | 2 days ago | `multi-agent` |
| 5 | [Google ADK](https://github.com/google/adk-python) | 🟢 **74.6** | 22.2k | 📈 +85 | 309 | 2 days ago | `orchestration` |
| 6 | [Mastra](https://github.com/mastra-ai/mastra) | 🟢 **74.5** | 29.5k | 🚀 +126 | 1895 | 1 day ago | `typescript` |
| 7 | [Haystack](https://github.com/deepset-ai/haystack) | 🟢 **71.9** | 27.0k | 📈 +68 | 199 | 5 days ago | `pipeline` |
| 8 | [PydanticAI](https://github.com/pydantic/pydantic-ai) | 🟢 **70.5** | 21.2k | 🚀 +135 | 903 | 1 mo ago | `structured` |
| 9 | [Agno](https://github.com/agno-agi/agno) | 🟢 **70.2** | 43.2k | 📈 +93 | 110 | 2 days ago | `multi-agent` |
| 10 | [OpenAI Agents SDK](https://github.com/openai/openai-agents-python) | 🟡 **68.5** | 30.7k | 🚀 +136 | 63 | 7 days ago | `orchestration` |
| 11 | [Composio](https://github.com/ComposioHQ/composio) | 🟡 **67.9** | 31.1k | 🚀 +103 | 219 | 1 day ago | `tooling` |
| 12 | [Semantic Kernel](https://github.com/microsoft/semantic-kernel) | 🟡 **67.4** | 28.8k | 📈 +23 | 82 | 8 days ago | `enterprise` |
| 13 | [DSPy](https://github.com/stanfordnlp/dspy) | 🟡 **63.9** | 39.1k | 🚀 +101 | 76 | 4 days ago | `optimization` |
| 14 | [LlamaIndex](https://github.com/run-llama/llama_index) | 🟡 **55.4** | 52.9k | 📈 +64 | 8 | 1 day ago | `data-agent` |
| 15 | [AG2](https://github.com/ag2ai/ag2) | 🟡 **50.0** | 5.1k | ↗️ +15 | 0 | 4 days ago | `multi-agent` |
| 16 | [Letta](https://github.com/letta-ai/letta) | 🟠 **33.0** | 25.4k | 📈 +63 | 0 | 6 mo ago | `memory` |
| 17 | [Smolagents](https://github.com/huggingface/smolagents) | 🟠 **32.6** | 30.4k | 🚀 +112 | 7 | 5 mo ago | `lightweight` |
| 18 | [AutoGen](https://github.com/microsoft/autogen) | 🟠 **32.5** | 61.8k | 📈 +97 | 2 | 1y ago | `multi-agent` |
| 19 | [Swarm](https://github.com/openai/swarm) | 🔴 **9.5** | 22.1k | 📈 +25 | 0 | — | `experimental` |

## 📂 By Category

- `data-agent`: **LlamaIndex** (55.4)
- `enterprise`: **Semantic Kernel** (67.4)
- `experimental`: **Swarm** (9.5)
- `lightweight`: **Smolagents** (32.6)
- `memory`: **Letta** (33.0)
- `multi-agent`: **CrewAI** (80.6), **Agno** (70.2), **AG2** (50.0), **AutoGen** (32.5)
- `optimization`: **DSPy** (63.9)
- `orchestration`: **LangGraph** (82.7), **Claude Agent SDK** (80.8), **Google ADK** (74.6), **OpenAI Agents SDK** (68.5)
- `pipeline`: **Haystack** (71.9)
- `structured`: **PydanticAI** (70.5)
- `tooling`: **Composio** (67.9)
- `typescript`: **Mastra** (74.5)
- `web-agent`: **BrowserUse** (90.2)

## 🔍 Top 5 — Score Breakdown

| Framework | Star Velocity | Release Freshness | Issue Health | Commit Activity | Community | Fork Ratio |
|-----------|:---:|:---:|:---:|:---:|:---:|:---:|
| **BrowserUse** | 100 | 99.7 | 90.3 | 100 | 72.4 | 44.7 |
| **LangGraph** | 72.5 | 99.7 | 79.9 | 100 | 57.6 | 69.0 |
| **Claude Agent SDK** | 100 | 99.7 | 84.8 | 78.0 | 11.2 | 64.2 |
| **CrewAI** | 59.7 | 99.3 | 82.8 | 100 | 73.8 | 60.3 |
| **Google ADK** | 17.1 | 99.3 | 93.4 | 100 | 86.0 | 78.5 |

## 💡 Key Insights

- **Hottest framework**: BrowserUse with a Pulse Score of 90.2
- **Fastest growing**: Claude Agent SDK gained +794 stars this week
- **Most active development**: Mastra with 1895 commits in the last 4 weeks
- **Stale releases**: AutoGen, Swarm haven't released in a while

## 📦 Recent Releases

- **BrowserUse** [`1.0.5`](https://github.com/browser-use/browser-use/releases/tag/1.0.5) — 1 day ago
- **LangGraph** [`1.2.22`](https://github.com/langchain-ai/langgraph/releases/tag/1.2.22) — 1 day ago
- **LlamaIndex** [`v0.14.26`](https://github.com/run-llama/llama_index/releases/tag/v0.14.26) — 1 day ago
- **Claude Agent SDK** [`v2.1.325`](https://github.com/anthropics/claude-code/releases/tag/v2.1.325) — 1 day ago
- **Composio** [`@composio/cli@0.6.1`](https://github.com/ComposioHQ/composio/releases/tag/@composio/cli@0.6.1) — 1 day ago
- **Mastra** [`@mastra/core@1.83.0`](https://github.com/mastra-ai/mastra/releases/tag/@mastra/core@1.83.0) — 1 day ago
- **Google ADK** [`v2.14.1`](https://github.com/google/adk-python/releases/tag/v2.14.1) — 2 days ago
- **CrewAI** [`1.15.41`](https://github.com/crewAIInc/crewAI/releases/tag/1.15.41) — 2 days ago
- **Agno** [`v3.2.0`](https://github.com/agno-agi/agno/releases/tag/v3.2.0) — 2 days ago
- **AG2** [`v.1.3.1`](https://github.com/ag2ai/ag2/releases/tag/v.1.3.1) — 4 days ago

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

*Powered by GitHub Actions • Data refreshed daily • Last run: 2026-11-15 13:44 UTC*