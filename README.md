# 🔬 AI Agent Framework Pulse Tracker

[![Daily Update](https://github.com/PurpleHaze2320/ai-agent-pulse/actions/workflows/track.yml/badge.svg)](https://github.com/PurpleHaze2320/ai-agent-pulse/actions/workflows/track.yml)
[![Frameworks Tracked](https://img.shields.io/badge/frameworks-19-blue)](https://github.com/PurpleHaze2320/ai-agent-pulse)
[![License: MIT](https://img.shields.io/badge/License-MIT-green.svg)](https://opensource.org/licenses/MIT)
[![GitHub stars](https://img.shields.io/github/stars/PurpleHaze2320/ai-agent-pulse?style=social)](https://github.com/PurpleHaze2320/ai-agent-pulse/stargazers)

> Automated daily tracking of the AI agent framework ecosystem's health, momentum, and trends.
> Last updated: **2026-04-15 07:58 UTC** | Tracking **19** frameworks

## How It Works

This bot runs daily via GitHub Actions and collects metrics from the GitHub API for the most important
AI agent frameworks. It computes a **Pulse Score** (0-100) based on six weighted signals: star velocity,
release freshness, issue health, commit activity, community size, and fork engagement. The result is
a living dashboard that shows which frameworks are gaining momentum and which are losing steam.

## 🏆 Pulse Leaderboard

| Rank | Framework | Pulse | Stars | ⭐ 7d | Commits (4w) | Last Release | Category |
|------|-----------|-------|-------|-------|--------------|--------------|----------|
| 1 | [Agno](https://github.com/agno-agi/agno) | 🟢 **74.6** | 39.4k | 🚀 +202 | 110 | today | `multi-agent` |
| 2 | [Mastra](https://github.com/mastra-ai/mastra) | 🟢 **74.3** | 23.0k | 🚀 +228 | 698 | 6 days ago | `typescript` |
| 3 | [CrewAI](https://github.com/crewAIInc/crewAI) | 🟢 **70.5** | 48.9k | 🚀 +614 | 0 | today | `multi-agent` |
| 4 | [BrowserUse](https://github.com/browser-use/browser-use) | 🟡 **69.4** | 87.9k | 🚀 +1426 | 0 | 13 days ago | `web-agent` |
| 5 | [LangGraph](https://github.com/langchain-ai/langgraph) | 🟡 **69.3** | 29.3k | 🚀 +635 | 0 | today | `orchestration` |
| 6 | [Claude Agent SDK](https://github.com/anthropics/claude-code) | 🟡 **64.6** | 114.2k | 🚀 +3320 | 0 | today | `orchestration` |
| 7 | [LlamaIndex](https://github.com/run-llama/llama_index) | 🟡 **58.2** | 48.6k | 🚀 +213 | 0 | 11 days ago | `data-agent` |
| 8 | [PydanticAI](https://github.com/pydantic/pydantic-ai) | 🟡 **53.7** | 16.4k | 🚀 +201 | 0 | today | `structured` |
| 9 | [Google ADK](https://github.com/google/adk-python) | 🟡 **51.6** | 19.0k | 🚀 +181 | 0 | 1 day ago | `orchestration` |
| 10 | [OpenAI Agents SDK](https://github.com/openai/openai-agents-python) | 🟡 **51.2** | 20.8k | 🚀 +141 | 0 | 6 days ago | `orchestration` |
| 11 | [Semantic Kernel](https://github.com/microsoft/semantic-kernel) | 🟡 **49.6** | 27.7k | 📈 +40 | 0 | 7 days ago | `enterprise` |
| 12 | [Haystack](https://github.com/deepset-ai/haystack) | 🟡 **48.1** | 24.8k | 📈 +74 | 0 | 13 days ago | `pipeline` |
| 13 | [AG2](https://github.com/ag2ai/ag2) | 🟡 **46.8** | 4.4k | 📈 +27 | 0 | 10 days ago | `multi-agent` |
| 14 | [AutoGen](https://github.com/microsoft/autogen) | 🟡 **46.4** | 57.1k | 🚀 +290 | 0 | 6 mo ago | `multi-agent` |
| 15 | [DSPy](https://github.com/stanfordnlp/dspy) | 🟡 **46.1** | 33.7k | 🚀 +178 | 0 | 2 mo ago | `optimization` |
| 16 | [Letta](https://github.com/letta-ai/letta) | 🟡 **45.5** | 22.1k | 🚀 +125 | 0 | 14 days ago | `memory` |
| 17 | [Composio](https://github.com/ComposioHQ/composio) | 🟡 **45.0** | 27.8k | 🚀 +107 | 0 | today | `tooling` |
| 18 | [Smolagents](https://github.com/huggingface/smolagents) | 🟠 **37.3** | 26.6k | 🚀 +130 | 0 | 2 mo ago | `lightweight` |
| 19 | [Swarm](https://github.com/openai/swarm) | 🔴 **9.4** | 21.3k | 📈 +32 | 0 | — | `experimental` |

## 📂 By Category

- `data-agent`: **LlamaIndex** (58.2)
- `enterprise`: **Semantic Kernel** (49.6)
- `experimental`: **Swarm** (9.4)
- `lightweight`: **Smolagents** (37.3)
- `memory`: **Letta** (45.5)
- `multi-agent`: **Agno** (74.6), **CrewAI** (70.5), **AG2** (46.8), **AutoGen** (46.4)
- `optimization`: **DSPy** (46.1)
- `orchestration`: **LangGraph** (69.3), **Claude Agent SDK** (64.6), **Google ADK** (51.6), **OpenAI Agents SDK** (51.2)
- `pipeline`: **Haystack** (48.1)
- `structured`: **PydanticAI** (53.7)
- `tooling`: **Composio** (45.0)
- `typescript`: **Mastra** (74.3)
- `web-agent`: **BrowserUse** (69.4)

## 🔍 Top 5 — Score Breakdown

| Framework | Star Velocity | Release Freshness | Issue Health | Commit Activity | Community | Fork Ratio |
|-----------|:---:|:---:|:---:|:---:|:---:|:---:|
| **Agno** | 33.6 | 100.0 | 84.5 | 100 | 82.2 | 53.3 |
| **Mastra** | 38.5 | 98.0 | 94.0 | 100 | 76.4 | 32.9 |
| **CrewAI** | 100 | 100.0 | 95.6 | 0.0 | 57.0 | 54.6 |
| **BrowserUse** | 100 | 95.7 | 97.1 | 0.0 | 61.4 | 46.0 |
| **LangGraph** | 100 | 100.0 | 79.9 | 0.0 | 54.4 | 68.5 |

## 💡 Key Insights

- **Hottest framework**: Agno with a Pulse Score of 74.6
- **Fastest growing**: Claude Agent SDK gained +3320 stars this week
- **Most active development**: Mastra with 698 commits in the last 4 weeks
- **Stale releases**: Swarm haven't released in a while

## 📦 Recent Releases

- **Composio** [`@composio/cli@0.2.25-beta.211`](https://github.com/ComposioHQ/composio/releases/tag/@composio/cli@0.2.25-beta.211) — today *(pre-release)*
- **Claude Agent SDK** [`v2.1.109`](https://github.com/anthropics/claude-code/releases/tag/v2.1.109) — today
- **Agno** [`v2.5.17`](https://github.com/agno-agi/agno/releases/tag/v2.5.17) — today
- **PydanticAI** [`v1.82.0`](https://github.com/pydantic/pydantic-ai/releases/tag/v1.82.0) — today
- **CrewAI** [`1.14.2a4`](https://github.com/crewAIInc/crewAI/releases/tag/1.14.2a4) — today *(pre-release)*
- **LangGraph** [`1.1.7a2`](https://github.com/langchain-ai/langgraph/releases/tag/1.1.7a2) — today
- **Google ADK** [`v1.30.0`](https://github.com/google/adk-python/releases/tag/v1.30.0) — 1 day ago
- **OpenAI Agents SDK** [`v0.13.6`](https://github.com/openai/openai-agents-python/releases/tag/v0.13.6) — 6 days ago
- **Mastra** [`@mastra/core@1.24.0`](https://github.com/mastra-ai/mastra/releases/tag/@mastra/core@1.24.0) — 6 days ago
- **Semantic Kernel** [`python-1.41.2`](https://github.com/microsoft/semantic-kernel/releases/tag/python-1.41.2) — 7 days ago

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

*Powered by GitHub Actions • Data refreshed daily • Last run: 2026-04-15 07:58 UTC*