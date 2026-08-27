# 🔬 AI Agent Framework Pulse Tracker

[![Daily Update](https://github.com/PurpleHaze2320/ai-agent-pulse/actions/workflows/track.yml/badge.svg)](https://github.com/PurpleHaze2320/ai-agent-pulse/actions/workflows/track.yml)
[![Frameworks Tracked](https://img.shields.io/badge/frameworks-19-blue)](https://github.com/PurpleHaze2320/ai-agent-pulse)
[![License: MIT](https://img.shields.io/badge/License-MIT-green.svg)](https://opensource.org/licenses/MIT)
[![GitHub stars](https://img.shields.io/github/stars/PurpleHaze2320/ai-agent-pulse?style=social)](https://github.com/PurpleHaze2320/ai-agent-pulse/stargazers)

> Automated daily tracking of the AI agent framework ecosystem's health, momentum, and trends.
> Last updated: **2026-08-27 17:30 UTC** | Tracking **19** frameworks

## How It Works

This bot runs daily via GitHub Actions and collects metrics from the GitHub API for the most important
AI agent frameworks. It computes a **Pulse Score** (0-100) based on six weighted signals: star velocity,
release freshness, issue health, commit activity, community size, and fork engagement. The result is
a living dashboard that shows which frameworks are gaining momentum and which are losing steam.

## 🏆 Pulse Leaderboard

| Rank | Framework | Pulse | Stars | ⭐ 7d | Commits (4w) | Last Release | Category |
|------|-----------|-------|-------|-------|--------------|--------------|----------|
| 1 | [BrowserUse](https://github.com/browser-use/browser-use) | 🟢 **89.4** | 111.4k | 🚀 +1612 | 121 | 10 days ago | `web-agent` |
| 2 | [CrewAI](https://github.com/crewAIInc/crewAI) | 🟢 **81.0** | 57.7k | 🚀 +323 | 93 | 7 days ago | `multi-agent` |
| 3 | [OpenAI Agents SDK](https://github.com/openai/openai-agents-python) | 🟢 **79.0** | 29.0k | 🚀 +232 | 334 | 8 days ago | `orchestration` |
| 4 | [Mastra](https://github.com/mastra-ai/mastra) | 🟢 **78.0** | 27.5k | 🚀 +204 | 1690 | 1 day ago | `typescript` |
| 5 | [Google ADK](https://github.com/google/adk-python) | 🟢 **74.5** | 21.3k | 🚀 +109 | 442 | today | `orchestration` |
| 6 | [LangGraph](https://github.com/langchain-ai/langgraph) | 🟢 **73.7** | 40.6k | 🚀 +491 | 33 | 7 days ago | `orchestration` |
| 7 | [Haystack](https://github.com/deepset-ai/haystack) | 🟢 **71.4** | 26.3k | 📈 +77 | 183 | 3 days ago | `pipeline` |
| 8 | [Claude Agent SDK](https://github.com/anthropics/claude-code) | 🟢 **70.0** | 143.2k | 🚀 +1116 | 25 | today | `orchestration` |
| 9 | [DSPy](https://github.com/stanfordnlp/dspy) | 🟡 **67.5** | 37.6k | 🚀 +183 | 66 | 5 days ago | `optimization` |
| 10 | [Agno](https://github.com/agno-agi/agno) | 🟡 **65.1** | 41.9k | 🚀 +143 | 62 | 1 day ago | `multi-agent` |
| 11 | [LlamaIndex](https://github.com/run-llama/llama_index) | 🟡 **64.2** | 51.9k | 🚀 +142 | 33 | 7 days ago | `data-agent` |
| 12 | [AG2](https://github.com/ag2ai/ag2) | 🟡 **59.4** | 4.9k | ↗️ +12 | 52 | 12 days ago | `multi-agent` |
| 13 | [Semantic Kernel](https://github.com/microsoft/semantic-kernel) | 🟡 **54.2** | 28.5k | 📈 +39 | 18 | 9 days ago | `enterprise` |
| 14 | [PydanticAI](https://github.com/pydantic/pydantic-ai) | 🟡 **54.1** | 19.5k | 🚀 +127 | 0 | today | `structured` |
| 15 | [Composio](https://github.com/ComposioHQ/composio) | 🟡 **48.4** | 29.9k | 🚀 +118 | 0 | 1 day ago | `tooling` |
| 16 | [Letta](https://github.com/letta-ai/letta) | 🟡 **42.7** | 24.5k | 🚀 +156 | 3 | 3 mo ago | `memory` |
| 17 | [Smolagents](https://github.com/huggingface/smolagents) | 🟠 **38.2** | 29.0k | 🚀 +126 | 2 | 3 mo ago | `lightweight` |
| 18 | [AutoGen](https://github.com/microsoft/autogen) | 🟠 **33.8** | 60.7k | 🚀 +122 | 0 | 11 mo ago | `multi-agent` |
| 19 | [Swarm](https://github.com/openai/swarm) | 🔴 **9.5** | 21.9k | ↗️ +20 | 0 | — | `experimental` |

## 📂 By Category

- `data-agent`: **LlamaIndex** (64.2)
- `enterprise`: **Semantic Kernel** (54.2)
- `experimental`: **Swarm** (9.5)
- `lightweight`: **Smolagents** (38.2)
- `memory`: **Letta** (42.7)
- `multi-agent`: **CrewAI** (81.0), **Agno** (65.1), **AG2** (59.4), **AutoGen** (33.8)
- `optimization`: **DSPy** (67.5)
- `orchestration`: **OpenAI Agents SDK** (79.0), **Google ADK** (74.5), **LangGraph** (73.7), **Claude Agent SDK** (70.0)
- `pipeline`: **Haystack** (71.4)
- `structured`: **PydanticAI** (54.1)
- `tooling`: **Composio** (48.4)
- `typescript`: **Mastra** (78.0)
- `web-agent`: **BrowserUse** (89.4)

## 🔍 Top 5 — Score Breakdown

| Framework | Star Velocity | Release Freshness | Issue Health | Commit Activity | Community | Fork Ratio |
|-----------|:---:|:---:|:---:|:---:|:---:|:---:|
| **BrowserUse** | 100 | 96.7 | 93.1 | 100 | 67.2 | 43.9 |
| **CrewAI** | 66.5 | 97.7 | 96.4 | 93.0 | 60.2 | 57.3 |
| **OpenAI Agents SDK** | 44.1 | 97.3 | 98.9 | 100 | 72.6 | 63.6 |
| **Mastra** | 41.9 | 99.7 | 95.8 | 100 | 93.0 | 39.2 |
| **Google ADK** | 21.1 | 100.0 | 90.5 | 100 | 83.6 | 73.2 |

## 💡 Key Insights

- **Hottest framework**: BrowserUse with a Pulse Score of 89.4
- **Fastest growing**: BrowserUse gained +1612 stars this week
- **Most active development**: Mastra with 1690 commits in the last 4 weeks
- **Stale releases**: AutoGen, Swarm haven't released in a while

## 📦 Recent Releases

- **PydanticAI** [`v2.35.1`](https://github.com/pydantic/pydantic-ai/releases/tag/v2.35.1) — today
- **Google ADK** [`v2.8.0`](https://github.com/google/adk-python/releases/tag/v2.8.0) — today
- **Claude Agent SDK** [`v2.1.247`](https://github.com/anthropics/claude-code/releases/tag/v2.1.247) — today
- **Mastra** [`@mastra/core@1.62.0`](https://github.com/mastra-ai/mastra/releases/tag/@mastra/core@1.62.0) — 1 day ago
- **Agno** [`v3.0.1`](https://github.com/agno-agi/agno/releases/tag/v3.0.1) — 1 day ago
- **Composio** [`@composio/cli@0.4.1-beta.369`](https://github.com/ComposioHQ/composio/releases/tag/@composio/cli@0.4.1-beta.369) — 1 day ago *(pre-release)*
- **Haystack** [`v3.1.0`](https://github.com/deepset-ai/haystack/releases/tag/v3.1.0) — 3 days ago
- **DSPy** [`3.3.1`](https://github.com/stanfordnlp/dspy/releases/tag/3.3.1) — 5 days ago
- **CrewAI** [`1.15.17`](https://github.com/crewAIInc/crewAI/releases/tag/1.15.17) — 7 days ago
- **LlamaIndex** [`v0.14.24`](https://github.com/run-llama/llama_index/releases/tag/v0.14.24) — 7 days ago

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

*Powered by GitHub Actions • Data refreshed daily • Last run: 2026-08-27 17:30 UTC*