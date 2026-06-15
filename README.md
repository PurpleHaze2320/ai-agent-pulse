# 🔬 AI Agent Framework Pulse Tracker

[![Daily Update](https://github.com/PurpleHaze2320/ai-agent-pulse/actions/workflows/track.yml/badge.svg)](https://github.com/PurpleHaze2320/ai-agent-pulse/actions/workflows/track.yml)
[![Frameworks Tracked](https://img.shields.io/badge/frameworks-19-blue)](https://github.com/PurpleHaze2320/ai-agent-pulse)
[![License: MIT](https://img.shields.io/badge/License-MIT-green.svg)](https://opensource.org/licenses/MIT)
[![GitHub stars](https://img.shields.io/github/stars/PurpleHaze2320/ai-agent-pulse?style=social)](https://github.com/PurpleHaze2320/ai-agent-pulse/stargazers)

> Automated daily tracking of the AI agent framework ecosystem's health, momentum, and trends.
> Last updated: **2026-06-15 12:27 UTC** | Tracking **19** frameworks

## How It Works

This bot runs daily via GitHub Actions and collects metrics from the GitHub API for the most important
AI agent frameworks. It computes a **Pulse Score** (0-100) based on six weighted signals: star velocity,
release freshness, issue health, commit activity, community size, and fork engagement. The result is
a living dashboard that shows which frameworks are gaining momentum and which are losing steam.

## 🏆 Pulse Leaderboard

| Rank | Framework | Pulse | Stars | ⭐ 7d | Commits (4w) | Last Release | Category |
|------|-----------|-------|-------|-------|--------------|--------------|----------|
| 1 | [BrowserUse](https://github.com/browser-use/browser-use) | 🟢 **90.0** | 98.9k | 🚀 +1193 | 408 | 2 days ago | `web-agent` |
| 2 | [CrewAI](https://github.com/crewAIInc/crewAI) | 🟢 **89.5** | 53.6k | 🚀 +549 | 93 | 3 days ago | `multi-agent` |
| 3 | [LangGraph](https://github.com/langchain-ai/langgraph) | 🟢 **81.5** | 34.8k | 🚀 +656 | 66 | 2 days ago | `orchestration` |
| 4 | [Mastra](https://github.com/mastra-ai/mastra) | 🟢 **78.8** | 25.1k | 🚀 +214 | 733 | 2 days ago | `typescript` |
| 5 | [Agno](https://github.com/agno-agi/agno) | 🟢 **70.8** | 40.7k | 🚀 +108 | 93 | 2 days ago | `multi-agent` |
| 6 | [Claude Agent SDK](https://github.com/anthropics/claude-code) | 🟢 **70.5** | 132.5k | 🚀 +1491 | 25 | 2 days ago | `orchestration` |
| 7 | [Haystack](https://github.com/deepset-ai/haystack) | 🟢 **70.1** | 25.6k | 📈 +78 | 118 | 5 days ago | `pipeline` |
| 8 | [PydanticAI](https://github.com/pydantic/pydantic-ai) | 🟡 **68.4** | 17.8k | 🚀 +152 | 70 | 4 days ago | `structured` |
| 9 | [LlamaIndex](https://github.com/run-llama/llama_index) | 🟡 **60.5** | 50.1k | 🚀 +150 | 23 | 1 mo ago | `data-agent` |
| 10 | [OpenAI Agents SDK](https://github.com/openai/openai-agents-python) | 🟡 **59.7** | 27.2k | 🚀 +176 | 23 | 4 days ago | `orchestration` |
| 11 | [AG2](https://github.com/ag2ai/ag2) | 🟡 **59.7** | 4.7k | 📈 +30 | 54 | 2 days ago | `multi-agent` |
| 12 | [DSPy](https://github.com/stanfordnlp/dspy) | 🟡 **56.5** | 35.0k | 🚀 +131 | 36 | 18 days ago | `optimization` |
| 13 | [Composio](https://github.com/ComposioHQ/composio) | 🟡 **52.1** | 28.8k | 📈 +93 | 27 | today | `tooling` |
| 14 | [Semantic Kernel](https://github.com/microsoft/semantic-kernel) | 🟡 **51.8** | 28.1k | 📈 +47 | 5 | 11 days ago | `enterprise` |
| 15 | [Google ADK](https://github.com/google/adk-python) | 🟡 **50.1** | 20.1k | 📈 +96 | 0 | 5 days ago | `orchestration` |
| 16 | [Letta](https://github.com/letta-ai/letta) | 🟡 **46.3** | 23.3k | 🚀 +125 | 0 | 1 mo ago | `memory` |
| 17 | [Smolagents](https://github.com/huggingface/smolagents) | 🟡 **43.7** | 27.9k | 🚀 +116 | 4 | 17 days ago | `lightweight` |
| 18 | [AutoGen](https://github.com/microsoft/autogen) | 🟡 **40.4** | 59.0k | 🚀 +199 | 0 | 8 mo ago | `multi-agent` |
| 19 | [Swarm](https://github.com/openai/swarm) | 🔴 **9.6** | 21.6k | 📈 +40 | 0 | — | `experimental` |

## 📂 By Category

- `data-agent`: **LlamaIndex** (60.5)
- `enterprise`: **Semantic Kernel** (51.8)
- `experimental`: **Swarm** (9.6)
- `lightweight`: **Smolagents** (43.7)
- `memory`: **Letta** (46.3)
- `multi-agent`: **CrewAI** (89.5), **Agno** (70.8), **AG2** (59.7), **AutoGen** (40.4)
- `optimization`: **DSPy** (56.5)
- `orchestration`: **LangGraph** (81.5), **Claude Agent SDK** (70.5), **OpenAI Agents SDK** (59.7), **Google ADK** (50.1)
- `pipeline`: **Haystack** (70.1)
- `structured`: **PydanticAI** (68.4)
- `tooling`: **Composio** (52.1)
- `typescript`: **Mastra** (78.8)
- `web-agent`: **BrowserUse** (90.0)

## 🔍 Top 5 — Score Breakdown

| Framework | Star Velocity | Release Freshness | Issue Health | Commit Activity | Community | Fork Ratio |
|-----------|:---:|:---:|:---:|:---:|:---:|:---:|
| **BrowserUse** | 100 | 99.3 | 95.7 | 100 | 63.0 | 44.6 |
| **CrewAI** | 100 | 99.0 | 96.9 | 93.0 | 59.4 | 56.0 |
| **LangGraph** | 100 | 99.3 | 74.9 | 66.0 | 55.0 | 67.1 |
| **Mastra** | 47.4 | 99.3 | 95.2 | 100 | 92.0 | 35.7 |
| **Agno** | 23.3 | 99.3 | 81.3 | 93.0 | 89.0 | 54.4 |

## 💡 Key Insights

- **Hottest framework**: BrowserUse with a Pulse Score of 90.0
- **Fastest growing**: Claude Agent SDK gained +1491 stars this week
- **Most active development**: Mastra with 733 commits in the last 4 weeks
- **Stale releases**: Swarm haven't released in a while

## 📦 Recent Releases

- **Composio** [`@composio/cli@0.2.32-beta.263`](https://github.com/ComposioHQ/composio/releases/tag/@composio/cli@0.2.32-beta.263) — today *(pre-release)*
- **Claude Agent SDK** [`v2.1.177`](https://github.com/anthropics/claude-code/releases/tag/v2.1.177) — 2 days ago
- **BrowserUse** [`0.13.2`](https://github.com/browser-use/browser-use/releases/tag/0.13.2) — 2 days ago
- **AG2** [`v0.13.4`](https://github.com/ag2ai/ag2/releases/tag/v0.13.4) — 2 days ago
- **LangGraph** [`1.2.5`](https://github.com/langchain-ai/langgraph/releases/tag/1.2.5) — 2 days ago
- **Agno** [`v2.6.14`](https://github.com/agno-agi/agno/releases/tag/v2.6.14) — 2 days ago
- **Mastra** [`@mastra/core@1.42.0`](https://github.com/mastra-ai/mastra/releases/tag/@mastra/core@1.42.0) — 2 days ago
- **CrewAI** [`1.14.7`](https://github.com/crewAIInc/crewAI/releases/tag/1.14.7) — 3 days ago
- **OpenAI Agents SDK** [`v0.17.5`](https://github.com/openai/openai-agents-python/releases/tag/v0.17.5) — 4 days ago
- **PydanticAI** [`v2.0.0b7`](https://github.com/pydantic/pydantic-ai/releases/tag/v2.0.0b7) — 4 days ago *(pre-release)*

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

*Powered by GitHub Actions • Data refreshed daily • Last run: 2026-06-15 12:27 UTC*