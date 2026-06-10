# 🔬 AI Agent Framework Pulse Tracker

[![Daily Update](https://github.com/PurpleHaze2320/ai-agent-pulse/actions/workflows/track.yml/badge.svg)](https://github.com/PurpleHaze2320/ai-agent-pulse/actions/workflows/track.yml)
[![Frameworks Tracked](https://img.shields.io/badge/frameworks-19-blue)](https://github.com/PurpleHaze2320/ai-agent-pulse)
[![License: MIT](https://img.shields.io/badge/License-MIT-green.svg)](https://opensource.org/licenses/MIT)
[![GitHub stars](https://img.shields.io/github/stars/PurpleHaze2320/ai-agent-pulse?style=social)](https://github.com/PurpleHaze2320/ai-agent-pulse/stargazers)

> Automated daily tracking of the AI agent framework ecosystem's health, momentum, and trends.
> Last updated: **2026-06-10 10:12 UTC** | Tracking **19** frameworks

## How It Works

This bot runs daily via GitHub Actions and collects metrics from the GitHub API for the most important
AI agent frameworks. It computes a **Pulse Score** (0-100) based on six weighted signals: star velocity,
release freshness, issue health, commit activity, community size, and fork engagement. The result is
a living dashboard that shows which frameworks are gaining momentum and which are losing steam.

## 🏆 Pulse Leaderboard

| Rank | Framework | Pulse | Stars | ⭐ 7d | Commits (4w) | Last Release | Category |
|------|-----------|-------|-------|-------|--------------|--------------|----------|
| 1 | [CrewAI](https://github.com/crewAIInc/crewAI) | 🟢 **88.0** | 53.2k | 🚀 +455 | 91 | today | `multi-agent` |
| 2 | [LangGraph](https://github.com/langchain-ai/langgraph) | 🟢 **85.5** | 34.3k | 🚀 +605 | 87 | 7 days ago | `orchestration` |
| 3 | [Mastra](https://github.com/mastra-ai/mastra) | 🟢 **78.7** | 24.9k | 🚀 +218 | 828 | 5 days ago | `typescript` |
| 4 | [Agno](https://github.com/agno-agi/agno) | 🟢 **73.0** | 40.6k | 🚀 +131 | 119 | 4 days ago | `multi-agent` |
| 5 | [PydanticAI](https://github.com/pydantic/pydantic-ai) | 🟢 **72.0** | 17.7k | 🚀 +188 | 83 | 5 days ago | `structured` |
| 6 | [Claude Agent SDK](https://github.com/anthropics/claude-code) | 🟢 **72.0** | 131.5k | 🚀 +1702 | 32 | today | `orchestration` |
| 7 | [BrowserUse](https://github.com/browser-use/browser-use) | 🟢 **70.1** | 98.1k | 🚀 +1151 | 0 | today | `web-agent` |
| 8 | [Haystack](https://github.com/deepset-ai/haystack) | 🟢 **70.0** | 25.5k | 📈 +67 | 111 | today | `pipeline` |
| 9 | [LlamaIndex](https://github.com/run-llama/llama_index) | 🟡 **67.8** | 50.1k | 🚀 +186 | 51 | 26 days ago | `data-agent` |
| 10 | [AG2](https://github.com/ag2ai/ag2) | 🟡 **62.8** | 4.7k | 📈 +31 | 70 | 5 days ago | `multi-agent` |
| 11 | [OpenAI Agents SDK](https://github.com/openai/openai-agents-python) | 🟡 **61.5** | 27.1k | 🚀 +184 | 33 | 15 days ago | `orchestration` |
| 12 | [DSPy](https://github.com/stanfordnlp/dspy) | 🟡 **57.3** | 35.0k | 🚀 +152 | 34 | 13 days ago | `optimization` |
| 13 | [Composio](https://github.com/ComposioHQ/composio) | 🟡 **53.4** | 28.7k | 🚀 +112 | 29 | 1 day ago | `tooling` |
| 14 | [Semantic Kernel](https://github.com/microsoft/semantic-kernel) | 🟡 **52.6** | 28.1k | 📈 +49 | 7 | 6 days ago | `enterprise` |
| 15 | [Google ADK](https://github.com/google/adk-python) | 🟡 **49.8** | 20.0k | 📈 +80 | 0 | today | `orchestration` |
| 16 | [Letta](https://github.com/letta-ai/letta) | 🟡 **46.4** | 23.2k | 🚀 +117 | 0 | 26 days ago | `memory` |
| 17 | [Smolagents](https://github.com/huggingface/smolagents) | 🟡 **44.3** | 27.8k | 🚀 +109 | 6 | 12 days ago | `lightweight` |
| 18 | [AutoGen](https://github.com/microsoft/autogen) | 🟡 **40.1** | 58.8k | 🚀 +177 | 0 | 8 mo ago | `multi-agent` |
| 19 | [Swarm](https://github.com/openai/swarm) | 🔴 **10.1** | 21.6k | 📈 +44 | 0 | — | `experimental` |

## 📂 By Category

- `data-agent`: **LlamaIndex** (67.8)
- `enterprise`: **Semantic Kernel** (52.6)
- `experimental`: **Swarm** (10.1)
- `lightweight`: **Smolagents** (44.3)
- `memory`: **Letta** (46.4)
- `multi-agent`: **CrewAI** (88.0), **Agno** (73.0), **AG2** (62.8), **AutoGen** (40.1)
- `optimization`: **DSPy** (57.3)
- `orchestration`: **LangGraph** (85.5), **Claude Agent SDK** (72.0), **OpenAI Agents SDK** (61.5), **Google ADK** (49.8)
- `pipeline`: **Haystack** (70.0)
- `structured`: **PydanticAI** (72.0)
- `tooling`: **Composio** (53.4)
- `typescript`: **Mastra** (78.7)
- `web-agent`: **BrowserUse** (70.1)

## 🔍 Top 5 — Score Breakdown

| Framework | Star Velocity | Release Freshness | Issue Health | Commit Activity | Community | Fork Ratio |
|-----------|:---:|:---:|:---:|:---:|:---:|:---:|
| **CrewAI** | 94.5 | 100.0 | 97.4 | 91.0 | 59.4 | 56.0 |
| **LangGraph** | 100 | 97.7 | 75.8 | 87.0 | 55.0 | 67.2 |
| **Mastra** | 47.8 | 98.3 | 95.6 | 100 | 92.2 | 35.4 |
| **Agno** | 26.8 | 98.7 | 81.8 | 100 | 89.0 | 54.2 |
| **PydanticAI** | 36.6 | 98.3 | 82.5 | 83.0 | 92.6 | 49.8 |

## 💡 Key Insights

- **Hottest framework**: CrewAI with a Pulse Score of 88.0
- **Fastest growing**: Claude Agent SDK gained +1702 stars this week
- **Most active development**: Mastra with 828 commits in the last 4 weeks
- **Stale releases**: Swarm haven't released in a while

## 📦 Recent Releases

- **Google ADK** [`v1.35.0`](https://github.com/google/adk-python/releases/tag/v1.35.0) — today
- **BrowserUse** [`0.13.1`](https://github.com/browser-use/browser-use/releases/tag/0.13.1) — today
- **CrewAI** [`1.14.7a4`](https://github.com/crewAIInc/crewAI/releases/tag/1.14.7a4) — today *(pre-release)*
- **Claude Agent SDK** [`v2.1.170`](https://github.com/anthropics/claude-code/releases/tag/v2.1.170) — today
- **Haystack** [`v2.30.1`](https://github.com/deepset-ai/haystack/releases/tag/v2.30.1) — today
- **Composio** [`@composio/cli@0.2.31`](https://github.com/ComposioHQ/composio/releases/tag/@composio/cli@0.2.31) — 1 day ago
- **Agno** [`v2.6.12`](https://github.com/agno-agi/agno/releases/tag/v2.6.12) — 4 days ago
- **Mastra** [`@mastra/core@1.41.0`](https://github.com/mastra-ai/mastra/releases/tag/@mastra/core@1.41.0) — 5 days ago
- **AG2** [`v0.13.3`](https://github.com/ag2ai/ag2/releases/tag/v0.13.3) — 5 days ago
- **PydanticAI** [`v2.0.0b6`](https://github.com/pydantic/pydantic-ai/releases/tag/v2.0.0b6) — 5 days ago *(pre-release)*

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

*Powered by GitHub Actions • Data refreshed daily • Last run: 2026-06-10 10:12 UTC*