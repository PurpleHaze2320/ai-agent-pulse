# 🔬 AI Agent Framework Pulse Tracker

[![Daily Update](https://github.com/PurpleHaze2320/ai-agent-pulse/actions/workflows/track.yml/badge.svg)](https://github.com/PurpleHaze2320/ai-agent-pulse/actions/workflows/track.yml)
[![Frameworks Tracked](https://img.shields.io/badge/frameworks-19-blue)](https://github.com/PurpleHaze2320/ai-agent-pulse)
[![License: MIT](https://img.shields.io/badge/License-MIT-green.svg)](https://opensource.org/licenses/MIT)
[![GitHub stars](https://img.shields.io/github/stars/PurpleHaze2320/ai-agent-pulse?style=social)](https://github.com/PurpleHaze2320/ai-agent-pulse/stargazers)

> Automated daily tracking of the AI agent framework ecosystem's health, momentum, and trends.
> Last updated: **2026-05-18 10:15 UTC** | Tracking **19** frameworks

## How It Works

This bot runs daily via GitHub Actions and collects metrics from the GitHub API for the most important
AI agent frameworks. It computes a **Pulse Score** (0-100) based on six weighted signals: star velocity,
release freshness, issue health, commit activity, community size, and fork engagement. The result is
a living dashboard that shows which frameworks are gaining momentum and which are losing steam.

## 🏆 Pulse Leaderboard

| Rank | Framework | Pulse | Stars | ⭐ 7d | Commits (4w) | Last Release | Category |
|------|-----------|-------|-------|-------|--------------|--------------|----------|
| 1 | [Mastra](https://github.com/mastra-ai/mastra) | 🟢 **77.0** | 24.0k | 🚀 +215 | 850 | 2 days ago | `typescript` |
| 2 | [CrewAI](https://github.com/crewAIInc/crewAI) | 🟢 **71.1** | 51.6k | 🚀 +497 | 0 | 2 days ago | `multi-agent` |
| 3 | [OpenAI Agents SDK](https://github.com/openai/openai-agents-python) | 🟢 **70.6** | 26.4k | 🚀 +250 | 0 | 6 days ago | `orchestration` |
| 4 | [LangGraph](https://github.com/langchain-ai/langgraph) | 🟡 **68.4** | 32.3k | 🚀 +583 | 0 | 6 days ago | `orchestration` |
| 5 | [BrowserUse](https://github.com/browser-use/browser-use) | 🟡 **67.2** | 94.4k | 🚀 +1070 | 0 | 1 mo ago | `web-agent` |
| 6 | [Claude Agent SDK](https://github.com/anthropics/claude-code) | 🟡 **64.7** | 124.5k | 🚀 +2113 | 0 | 2 days ago | `orchestration` |
| 7 | [LlamaIndex](https://github.com/run-llama/llama_index) | 🟡 **58.3** | 49.5k | 🚀 +153 | 0 | 3 days ago | `data-agent` |
| 8 | [PydanticAI](https://github.com/pydantic/pydantic-ai) | 🟡 **53.2** | 17.1k | 🚀 +132 | 0 | 2 days ago | `structured` |
| 9 | [Agno](https://github.com/agno-agi/agno) | 🟡 **52.3** | 40.2k | 🚀 +113 | 0 | 2 days ago | `multi-agent` |
| 10 | [Haystack](https://github.com/deepset-ai/haystack) | 🟡 **51.4** | 25.3k | 🚀 +122 | 0 | 5 days ago | `pipeline` |
| 11 | [DSPy](https://github.com/stanfordnlp/dspy) | 🟡 **51.3** | 34.5k | 🚀 +164 | 0 | 12 days ago | `optimization` |
| 12 | [Semantic Kernel](https://github.com/microsoft/semantic-kernel) | 🟡 **51.1** | 27.9k | 📈 +46 | 0 | 4 days ago | `enterprise` |
| 13 | [Google ADK](https://github.com/google/adk-python) | 🟡 **50.3** | 19.7k | 🚀 +115 | 0 | 9 days ago | `orchestration` |
| 14 | [Letta](https://github.com/letta-ai/letta) | 🟡 **49.4** | 22.8k | 🚀 +159 | 0 | 3 days ago | `memory` |
| 15 | [Composio](https://github.com/ComposioHQ/composio) | 🟡 **49.1** | 28.3k | 🚀 +154 | 0 | 1 day ago | `tooling` |
| 16 | [AG2](https://github.com/ag2ai/ag2) | 🟡 **49.0** | 4.6k | 📈 +39 | 0 | 5 days ago | `multi-agent` |
| 17 | [Smolagents](https://github.com/huggingface/smolagents) | 🟡 **45.3** | 27.4k | 🚀 +144 | 0 | 3 days ago | `lightweight` |
| 18 | [AutoGen](https://github.com/microsoft/autogen) | 🟡 **43.5** | 58.1k | 🚀 +224 | 0 | 7 mo ago | `multi-agent` |
| 19 | [Swarm](https://github.com/openai/swarm) | 🔴 **9.0** | 21.5k | 📈 +25 | 0 | — | `experimental` |

## 📂 By Category

- `data-agent`: **LlamaIndex** (58.3)
- `enterprise`: **Semantic Kernel** (51.1)
- `experimental`: **Swarm** (9.0)
- `lightweight`: **Smolagents** (45.3)
- `memory`: **Letta** (49.4)
- `multi-agent`: **CrewAI** (71.1), **Agno** (52.3), **AG2** (49.0), **AutoGen** (43.5)
- `optimization`: **DSPy** (51.3)
- `orchestration`: **OpenAI Agents SDK** (70.6), **LangGraph** (68.4), **Claude Agent SDK** (64.7), **Google ADK** (50.3)
- `pipeline`: **Haystack** (51.4)
- `structured`: **PydanticAI** (53.2)
- `tooling`: **Composio** (49.1)
- `typescript`: **Mastra** (77.0)
- `web-agent`: **BrowserUse** (67.2)

## 🔍 Top 5 — Score Breakdown

| Framework | Star Velocity | Release Freshness | Issue Health | Commit Activity | Community | Fork Ratio |
|-----------|:---:|:---:|:---:|:---:|:---:|:---:|
| **Mastra** | 43.1 | 99.3 | 94.6 | 100 | 87.2 | 34.8 |
| **CrewAI** | 100 | 99.3 | 98.2 | 0.0 | 59.2 | 55.3 |
| **OpenAI Agents SDK** | 100 | 98.0 | 96.4 | 0.0 | 54.4 | 61.3 |
| **LangGraph** | 100 | 98.0 | 77.0 | 0.0 | 54.6 | 67.8 |
| **BrowserUse** | 100 | 84.7 | 96.2 | 0.0 | 62.8 | 45.2 |

## 💡 Key Insights

- **Hottest framework**: Mastra with a Pulse Score of 77.0
- **Fastest growing**: Claude Agent SDK gained +2113 stars this week
- **Most active development**: Mastra with 850 commits in the last 4 weeks
- **Stale releases**: Swarm haven't released in a while

## 📦 Recent Releases

- **Composio** [`@composio/cli@0.2.31-beta.253`](https://github.com/ComposioHQ/composio/releases/tag/@composio/cli@0.2.31-beta.253) — 1 day ago *(pre-release)*
- **Mastra** [`@mastra/core@1.34.0`](https://github.com/mastra-ai/mastra/releases/tag/@mastra/core@1.34.0) — 2 days ago
- **Claude Agent SDK** [`v2.1.143`](https://github.com/anthropics/claude-code/releases/tag/v2.1.143) — 2 days ago
- **PydanticAI** [`v1.97.0`](https://github.com/pydantic/pydantic-ai/releases/tag/v1.97.0) — 2 days ago
- **CrewAI** [`1.14.5a6`](https://github.com/crewAIInc/crewAI/releases/tag/1.14.5a6) — 2 days ago *(pre-release)*
- **Agno** [`v2.6.7`](https://github.com/agno-agi/agno/releases/tag/v2.6.7) — 2 days ago
- **LlamaIndex** [`v0.14.22`](https://github.com/run-llama/llama_index/releases/tag/v0.14.22) — 3 days ago
- **Letta** [`0.16.8`](https://github.com/letta-ai/letta/releases/tag/0.16.8) — 3 days ago
- **Smolagents** [`v1.25.0`](https://github.com/huggingface/smolagents/releases/tag/v1.25.0) — 3 days ago
- **Semantic Kernel** [`python-1.42.0`](https://github.com/microsoft/semantic-kernel/releases/tag/python-1.42.0) — 4 days ago

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

*Powered by GitHub Actions • Data refreshed daily • Last run: 2026-05-18 10:15 UTC*