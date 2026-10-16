# 🔬 AI Agent Framework Pulse Tracker

[![Daily Update](https://github.com/PurpleHaze2320/ai-agent-pulse/actions/workflows/track.yml/badge.svg)](https://github.com/PurpleHaze2320/ai-agent-pulse/actions/workflows/track.yml)
[![Frameworks Tracked](https://img.shields.io/badge/frameworks-19-blue)](https://github.com/PurpleHaze2320/ai-agent-pulse)
[![License: MIT](https://img.shields.io/badge/License-MIT-green.svg)](https://opensource.org/licenses/MIT)
[![GitHub stars](https://img.shields.io/github/stars/PurpleHaze2320/ai-agent-pulse?style=social)](https://github.com/PurpleHaze2320/ai-agent-pulse/stargazers)

> Automated daily tracking of the AI agent framework ecosystem's health, momentum, and trends.
> Last updated: **2026-10-16 11:04 UTC** | Tracking **19** frameworks

## How It Works

This bot runs daily via GitHub Actions and collects metrics from the GitHub API for the most important
AI agent frameworks. It computes a **Pulse Score** (0-100) based on six weighted signals: star velocity,
release freshness, issue health, commit activity, community size, and fork engagement. The result is
a living dashboard that shows which frameworks are gaining momentum and which are losing steam.

## 🏆 Pulse Leaderboard

| Rank | Framework | Pulse | Stars | ⭐ 7d | Commits (4w) | Last Release | Category |
|------|-----------|-------|-------|-------|--------------|--------------|----------|
| 1 | [BrowserUse](https://github.com/browser-use/browser-use) | 🟢 **87.5** | 118.2k | 🚀 +781 | 87 | today | `web-agent` |
| 2 | [LangGraph](https://github.com/langchain-ai/langgraph) | 🟢 **81.3** | 43.4k | 🚀 +408 | 94 | 1 day ago | `orchestration` |
| 3 | [Claude Agent SDK](https://github.com/anthropics/claude-code) | 🟢 **78.9** | 151.2k | 🚀 +1346 | 64 | today | `orchestration` |
| 4 | [Mastra](https://github.com/mastra-ai/mastra) | 🟢 **77.0** | 28.8k | 🚀 +184 | 2136 | today | `typescript` |
| 5 | [CrewAI](https://github.com/crewAIInc/crewAI) | 🟢 **76.9** | 59.8k | 🚀 +266 | 88 | 2 days ago | `multi-agent` |
| 6 | [OpenAI Agents SDK](https://github.com/openai/openai-agents-python) | 🟢 **76.8** | 30.1k | 🚀 +147 | 223 | 1 day ago | `orchestration` |
| 7 | [PydanticAI](https://github.com/pydantic/pydantic-ai) | 🟢 **74.4** | 20.7k | 🚀 +157 | 840 | today | `structured` |
| 8 | [Haystack](https://github.com/deepset-ai/haystack) | 🟢 **70.8** | 26.7k | 📈 +42 | 285 | 1 day ago | `pipeline` |
| 9 | [AG2](https://github.com/ag2ai/ag2) | 🟡 **69.5** | 5.0k | ↗️ +12 | 120 | 5 days ago | `multi-agent` |
| 10 | [Composio](https://github.com/ComposioHQ/composio) | 🟡 **67.8** | 30.6k | 🚀 +107 | 326 | today | `tooling` |
| 11 | [DSPy](https://github.com/stanfordnlp/dspy) | 🟡 **60.1** | 38.7k | 📈 +88 | 57 | 3 days ago | `optimization` |
| 12 | [LlamaIndex](https://github.com/run-llama/llama_index) | 🟡 **56.7** | 52.5k | 📈 +68 | 22 | 24 days ago | `data-agent` |
| 13 | [Google ADK](https://github.com/google/adk-python) | 🟡 **55.7** | 21.9k | 🚀 +118 | 0 | 2 days ago | `orchestration` |
| 14 | [Semantic Kernel](https://github.com/microsoft/semantic-kernel) | 🟡 **54.9** | 28.7k | 📈 +30 | 23 | 9 days ago | `enterprise` |
| 15 | [Agno](https://github.com/agno-agi/agno) | 🟡 **51.8** | 42.8k | 🚀 +131 | 0 | 3 days ago | `multi-agent` |
| 16 | [Letta](https://github.com/letta-ai/letta) | 🟠 **35.9** | 25.2k | 📈 +77 | 0 | 5 mo ago | `memory` |
| 17 | [Smolagents](https://github.com/huggingface/smolagents) | 🟠 **35.1** | 29.9k | 🚀 +126 | 5 | 4 mo ago | `lightweight` |
| 18 | [AutoGen](https://github.com/microsoft/autogen) | 🟠 **33.1** | 61.4k | 🚀 +121 | 0 | 1y ago | `multi-agent` |
| 19 | [Swarm](https://github.com/openai/swarm) | 🔴 **9.2** | 22.1k | ↗️ +13 | 0 | — | `experimental` |

## 📂 By Category

- `data-agent`: **LlamaIndex** (56.7)
- `enterprise`: **Semantic Kernel** (54.9)
- `experimental`: **Swarm** (9.2)
- `lightweight`: **Smolagents** (35.1)
- `memory`: **Letta** (35.9)
- `multi-agent`: **CrewAI** (76.9), **AG2** (69.5), **Agno** (51.8), **AutoGen** (33.1)
- `optimization`: **DSPy** (60.1)
- `orchestration`: **LangGraph** (81.3), **Claude Agent SDK** (78.9), **OpenAI Agents SDK** (76.8), **Google ADK** (55.7)
- `pipeline`: **Haystack** (70.8)
- `structured`: **PydanticAI** (74.4)
- `tooling`: **Composio** (67.8)
- `typescript`: **Mastra** (77.0)
- `web-agent`: **BrowserUse** (87.5)

## 🔍 Top 5 — Score Breakdown

| Framework | Star Velocity | Release Freshness | Issue Health | Commit Activity | Community | Fork Ratio |
|-----------|:---:|:---:|:---:|:---:|:---:|:---:|
| **BrowserUse** | 100 | 100.0 | 89.6 | 87.0 | 72.0 | 44.4 |
| **LangGraph** | 81.1 | 99.7 | 65.2 | 94.0 | 56.6 | 68.1 |
| **Claude Agent SDK** | 100 | 100.0 | 85.6 | 64.0 | 11.4 | 70.9 |
| **Mastra** | 37.0 | 100.0 | 95.3 | 100 | 93.4 | 41.4 |
| **CrewAI** | 53.9 | 99.3 | 88.3 | 88.0 | 69.0 | 58.6 |

## 💡 Key Insights

- **Hottest framework**: BrowserUse with a Pulse Score of 87.5
- **Fastest growing**: Claude Agent SDK gained +1346 stars this week
- **Most active development**: Mastra with 2136 commits in the last 4 weeks
- **Stale releases**: AutoGen, Swarm haven't released in a while

## 📦 Recent Releases

- **Composio** [`@composio/cli@0.4.6-beta.457`](https://github.com/ComposioHQ/composio/releases/tag/@composio/cli@0.4.6-beta.457) — today *(pre-release)*
- **Mastra** [`@mastra/core@1.78.0`](https://github.com/mastra-ai/mastra/releases/tag/@mastra/core@1.78.0) — today
- **PydanticAI** [`v2.57.0`](https://github.com/pydantic/pydantic-ai/releases/tag/v2.57.0) — today
- **BrowserUse** [`0.13.13`](https://github.com/browser-use/browser-use/releases/tag/0.13.13) — today
- **Claude Agent SDK** [`v2.1.301`](https://github.com/anthropics/claude-code/releases/tag/v2.1.301) — today
- **Haystack** [`v3.4.0`](https://github.com/deepset-ai/haystack/releases/tag/v3.4.0) — 1 day ago
- **LangGraph** [`prebuilt==1.1.1`](https://github.com/langchain-ai/langgraph/releases/tag/prebuilt==1.1.1) — 1 day ago
- **OpenAI Agents SDK** [`v0.24.0`](https://github.com/openai/openai-agents-python/releases/tag/v0.24.0) — 1 day ago
- **CrewAI** [`1.15.28`](https://github.com/crewAIInc/crewAI/releases/tag/1.15.28) — 2 days ago
- **Google ADK** [`v2.12.0`](https://github.com/google/adk-python/releases/tag/v2.12.0) — 2 days ago

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

*Powered by GitHub Actions • Data refreshed daily • Last run: 2026-10-16 11:04 UTC*