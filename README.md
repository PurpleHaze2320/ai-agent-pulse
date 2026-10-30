# 🔬 AI Agent Framework Pulse Tracker

[![Daily Update](https://github.com/PurpleHaze2320/ai-agent-pulse/actions/workflows/track.yml/badge.svg)](https://github.com/PurpleHaze2320/ai-agent-pulse/actions/workflows/track.yml)
[![Frameworks Tracked](https://img.shields.io/badge/frameworks-19-blue)](https://github.com/PurpleHaze2320/ai-agent-pulse)
[![License: MIT](https://img.shields.io/badge/License-MIT-green.svg)](https://opensource.org/licenses/MIT)
[![GitHub stars](https://img.shields.io/github/stars/PurpleHaze2320/ai-agent-pulse?style=social)](https://github.com/PurpleHaze2320/ai-agent-pulse/stargazers)

> Automated daily tracking of the AI agent framework ecosystem's health, momentum, and trends.
> Last updated: **2026-10-30 12:29 UTC** | Tracking **19** frameworks

## How It Works

This bot runs daily via GitHub Actions and collects metrics from the GitHub API for the most important
AI agent frameworks. It computes a **Pulse Score** (0-100) based on six weighted signals: star velocity,
release freshness, issue health, commit activity, community size, and fork engagement. The result is
a living dashboard that shows which frameworks are gaining momentum and which are losing steam.

## 🏆 Pulse Leaderboard

| Rank | Framework | Pulse | Stars | ⭐ 7d | Commits (4w) | Last Release | Category |
|------|-----------|-------|-------|-------|--------------|--------------|----------|
| 1 | [BrowserUse](https://github.com/browser-use/browser-use) | 🟢 **89.8** | 119.6k | 🚀 +617 | 119 | 3 days ago | `web-agent` |
| 2 | [LangGraph](https://github.com/langchain-ai/langgraph) | 🟢 **83.9** | 44.2k | 🚀 +385 | 122 | 3 days ago | `orchestration` |
| 3 | [CrewAI](https://github.com/crewAIInc/crewAI) | 🟢 **79.5** | 60.3k | 🚀 +270 | 186 | 1 day ago | `multi-agent` |
| 4 | [Mastra](https://github.com/mastra-ai/mastra) | 🟢 **76.8** | 29.2k | 🚀 +179 | 2429 | 1 day ago | `typescript` |
| 5 | [Claude Agent SDK](https://github.com/anthropics/claude-code) | 🟢 **75.3** | 153.9k | 🚀 +952 | 48 | today | `orchestration` |
| 6 | [Google ADK](https://github.com/google/adk-python) | 🟢 **74.0** | 22.0k | 📈 +72 | 506 | 6 days ago | `orchestration` |
| 7 | [OpenAI Agents SDK](https://github.com/openai/openai-agents-python) | 🟢 **73.2** | 30.4k | 🚀 +152 | 86 | 15 days ago | `orchestration` |
| 8 | [PydanticAI](https://github.com/pydantic/pydantic-ai) | 🟢 **72.5** | 21.0k | 🚀 +146 | 1163 | 24 days ago | `structured` |
| 9 | [Haystack](https://github.com/deepset-ai/haystack) | 🟢 **71.5** | 26.9k | 📈 +69 | 235 | 8 days ago | `pipeline` |
| 10 | [Agno](https://github.com/agno-agi/agno) | 🟢 **70.7** | 43.0k | 📈 +94 | 175 | today | `multi-agent` |
| 11 | [AG2](https://github.com/ag2ai/ag2) | 🟢 **70.1** | 5.0k | 📈 +22 | 111 | 2 days ago | `multi-agent` |
| 12 | [Composio](https://github.com/ComposioHQ/composio) | 🟡 **68.9** | 30.8k | 🚀 +133 | 360 | 1 day ago | `tooling` |
| 13 | [Semantic Kernel](https://github.com/microsoft/semantic-kernel) | 🟡 **65.4** | 28.7k | 📈 +27 | 70 | 1 day ago | `enterprise` |
| 14 | [DSPy](https://github.com/stanfordnlp/dspy) | 🟡 **62.8** | 38.9k | 🚀 +105 | 74 | 17 days ago | `optimization` |
| 15 | [LlamaIndex](https://github.com/run-llama/llama_index) | 🟡 **54.7** | 52.7k | 🚀 +108 | 9 | 1 mo ago | `data-agent` |
| 16 | [Letta](https://github.com/letta-ai/letta) | 🟠 **34.2** | 25.3k | 📈 +58 | 1 | 5 mo ago | `memory` |
| 17 | [Smolagents](https://github.com/huggingface/smolagents) | 🟠 **33.6** | 30.1k | 🚀 +137 | 1 | 5 mo ago | `lightweight` |
| 18 | [AutoGen](https://github.com/microsoft/autogen) | 🟠 **32.3** | 61.6k | 📈 +94 | 2 | 1y ago | `multi-agent` |
| 19 | [Swarm](https://github.com/openai/swarm) | 🔴 **9.1** | 22.1k | ↗️ +15 | 0 | — | `experimental` |

## 📂 By Category

- `data-agent`: **LlamaIndex** (54.7)
- `enterprise`: **Semantic Kernel** (65.4)
- `experimental`: **Swarm** (9.1)
- `lightweight`: **Smolagents** (33.6)
- `memory`: **Letta** (34.2)
- `multi-agent`: **CrewAI** (79.5), **Agno** (70.7), **AG2** (70.1), **AutoGen** (32.3)
- `optimization`: **DSPy** (62.8)
- `orchestration`: **LangGraph** (83.9), **Claude Agent SDK** (75.3), **Google ADK** (74.0), **OpenAI Agents SDK** (73.2)
- `pipeline`: **Haystack** (71.5)
- `structured`: **PydanticAI** (72.5)
- `tooling`: **Composio** (68.9)
- `typescript`: **Mastra** (76.8)
- `web-agent`: **BrowserUse** (89.8)

## 🔍 Top 5 — Score Breakdown

| Framework | Star Velocity | Release Freshness | Issue Health | Commit Activity | Community | Fork Ratio |
|-----------|:---:|:---:|:---:|:---:|:---:|:---:|
| **BrowserUse** | 100 | 99.0 | 89.0 | 100 | 72.2 | 44.5 |
| **LangGraph** | 78.6 | 99.0 | 78.9 | 100 | 57.4 | 68.8 |
| **CrewAI** | 54.0 | 99.7 | 85.6 | 100 | 72.6 | 59.4 |
| **Mastra** | 36.4 | 99.7 | 94.7 | 100 | 93.4 | 41.9 |
| **Claude Agent SDK** | 100 | 100.0 | 85.0 | 48.0 | 11.4 | 67.8 |

## 💡 Key Insights

- **Hottest framework**: BrowserUse with a Pulse Score of 89.8
- **Fastest growing**: Claude Agent SDK gained +952 stars this week
- **Most active development**: Mastra with 2429 commits in the last 4 weeks
- **Stale releases**: AutoGen, Swarm haven't released in a while

## 📦 Recent Releases

- **Claude Agent SDK** [`v2.1.314`](https://github.com/anthropics/claude-code/releases/tag/v2.1.314) — today
- **Agno** [`v3.1.12`](https://github.com/agno-agi/agno/releases/tag/v3.1.12) — today
- **CrewAI** [`1.15.33`](https://github.com/crewAIInc/crewAI/releases/tag/1.15.33) — 1 day ago
- **Composio** [`@composio/cli@0.5.1-beta.521`](https://github.com/ComposioHQ/composio/releases/tag/@composio/cli@0.5.1-beta.521) — 1 day ago *(pre-release)*
- **Mastra** [`@mastra/core@1.80.0`](https://github.com/mastra-ai/mastra/releases/tag/@mastra/core@1.80.0) — 1 day ago
- **Semantic Kernel** [`python-1.46.0`](https://github.com/microsoft/semantic-kernel/releases/tag/python-1.46.0) — 1 day ago
- **AG2** [`v1.2.2`](https://github.com/ag2ai/ag2/releases/tag/v1.2.2) — 2 days ago
- **BrowserUse** [`0.13.14`](https://github.com/browser-use/browser-use/releases/tag/0.13.14) — 3 days ago
- **LangGraph** [`1.2.18`](https://github.com/langchain-ai/langgraph/releases/tag/1.2.18) — 3 days ago
- **Google ADK** [`v2.13.0`](https://github.com/google/adk-python/releases/tag/v2.13.0) — 6 days ago

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

*Powered by GitHub Actions • Data refreshed daily • Last run: 2026-10-30 12:29 UTC*