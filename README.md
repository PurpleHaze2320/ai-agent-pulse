# 🔬 AI Agent Framework Pulse Tracker

[![Daily Update](https://github.com/PurpleHaze2320/ai-agent-pulse/actions/workflows/track.yml/badge.svg)](https://github.com/PurpleHaze2320/ai-agent-pulse/actions/workflows/track.yml)
[![Frameworks Tracked](https://img.shields.io/badge/frameworks-19-blue)](https://github.com/PurpleHaze2320/ai-agent-pulse)
[![License: MIT](https://img.shields.io/badge/License-MIT-green.svg)](https://opensource.org/licenses/MIT)
[![GitHub stars](https://img.shields.io/github/stars/PurpleHaze2320/ai-agent-pulse?style=social)](https://github.com/PurpleHaze2320/ai-agent-pulse/stargazers)

> Automated daily tracking of the AI agent framework ecosystem's health, momentum, and trends.
> Last updated: **2026-04-13 08:13 UTC** | Tracking **19** frameworks

## How It Works

This bot runs daily via GitHub Actions and collects metrics from the GitHub API for the most important
AI agent frameworks. It computes a **Pulse Score** (0-100) based on six weighted signals: star velocity,
release freshness, issue health, commit activity, community size, and fork engagement. The result is
a living dashboard that shows which frameworks are gaining momentum and which are losing steam.

## 🏆 Pulse Leaderboard

| Rank | Framework | Pulse | Stars | ⭐ 7d | Commits (4w) | Last Release | Category |
|------|-----------|-------|-------|-------|--------------|--------------|----------|
| 1 | [Mastra](https://github.com/mastra-ai/mastra) | 🟢 **73.7** | 22.9k | 🚀 +220 | 609 | 4 days ago | `typescript` |
| 2 | [CrewAI](https://github.com/crewAIInc/crewAI) | 🟢 **70.4** | 48.7k | 🚀 +624 | 0 | 2 days ago | `multi-agent` |
| 3 | [BrowserUse](https://github.com/browser-use/browser-use) | 🟡 **69.6** | 87.5k | 🚀 +1346 | 0 | 11 days ago | `web-agent` |
| 4 | [LangGraph](https://github.com/langchain-ai/langgraph) | 🟡 **68.7** | 29.1k | 🚀 +601 | 0 | 2 days ago | `orchestration` |
| 5 | [Claude Agent SDK](https://github.com/anthropics/claude-code) | 🟡 **64.6** | 113.2k | 🚀 +3657 | 0 | today | `orchestration` |
| 6 | [LlamaIndex](https://github.com/run-llama/llama_index) | 🟡 **58.2** | 48.5k | 🚀 +215 | 0 | 9 days ago | `data-agent` |
| 7 | [Agno](https://github.com/agno-agi/agno) | 🟡 **54.2** | 39.4k | 🚀 +200 | 0 | 2 days ago | `multi-agent` |
| 8 | [PydanticAI](https://github.com/pydantic/pydantic-ai) | 🟡 **53.3** | 16.3k | 🚀 +201 | 0 | 2 days ago | `structured` |
| 9 | [OpenAI Agents SDK](https://github.com/openai/openai-agents-python) | 🟡 **51.4** | 20.7k | 🚀 +149 | 0 | 4 days ago | `orchestration` |
| 10 | [Google ADK](https://github.com/google/adk-python) | 🟡 **50.5** | 18.9k | 🚀 +162 | 0 | 3 days ago | `orchestration` |
| 11 | [Semantic Kernel](https://github.com/microsoft/semantic-kernel) | 🟡 **49.6** | 27.7k | 📈 +39 | 0 | 5 days ago | `enterprise` |
| 12 | [Haystack](https://github.com/deepset-ai/haystack) | 🟡 **49.0** | 24.8k | 📈 +98 | 0 | 11 days ago | `pipeline` |
| 13 | [AG2](https://github.com/ag2ai/ag2) | 🟡 **47.0** | 4.4k | 📈 +28 | 0 | 8 days ago | `multi-agent` |
| 14 | [AutoGen](https://github.com/microsoft/autogen) | 🟡 **46.1** | 57.0k | 🚀 +287 | 0 | 6 mo ago | `multi-agent` |
| 15 | [DSPy](https://github.com/stanfordnlp/dspy) | 🟡 **45.7** | 33.6k | 🚀 +169 | 0 | 2 mo ago | `optimization` |
| 16 | [Letta](https://github.com/letta-ai/letta) | 🟡 **45.3** | 22.0k | 🚀 +120 | 0 | 12 days ago | `memory` |
| 17 | [Composio](https://github.com/ComposioHQ/composio) | 🟡 **44.6** | 27.8k | 🚀 +106 | 0 | 2 days ago | `tooling` |
| 18 | [Smolagents](https://github.com/huggingface/smolagents) | 🟠 **36.7** | 26.6k | 🚀 +114 | 0 | 2 mo ago | `lightweight` |
| 19 | [Swarm](https://github.com/openai/swarm) | 🔴 **9.3** | 21.3k | 📈 +26 | 0 | — | `experimental` |

## 📂 By Category

- `data-agent`: **LlamaIndex** (58.2)
- `enterprise`: **Semantic Kernel** (49.6)
- `experimental`: **Swarm** (9.3)
- `lightweight`: **Smolagents** (36.7)
- `memory`: **Letta** (45.3)
- `multi-agent`: **CrewAI** (70.4), **Agno** (54.2), **AG2** (47.0), **AutoGen** (46.1)
- `optimization`: **DSPy** (45.7)
- `orchestration`: **LangGraph** (68.7), **Claude Agent SDK** (64.6), **OpenAI Agents SDK** (51.4), **Google ADK** (50.5)
- `pipeline`: **Haystack** (49.0)
- `structured`: **PydanticAI** (53.3)
- `tooling`: **Composio** (44.6)
- `typescript`: **Mastra** (73.7)
- `web-agent`: **BrowserUse** (69.6)

## 🔍 Top 5 — Score Breakdown

| Framework | Star Velocity | Release Freshness | Issue Health | Commit Activity | Community | Fork Ratio |
|-----------|:---:|:---:|:---:|:---:|:---:|:---:|
| **Mastra** | 36.3 | 98.7 | 93.6 | 100 | 75.6 | 32.8 |
| **CrewAI** | 100 | 99.3 | 95.6 | 0.0 | 57.0 | 54.6 |
| **BrowserUse** | 100 | 96.3 | 97.3 | 0.0 | 61.2 | 46.0 |
| **LangGraph** | 98.1 | 99.3 | 79.8 | 0.0 | 54.4 | 68.6 |
| **Claude Agent SDK** | 100 | 100.0 | 79.7 | 0.0 | 9.4 | 66.9 |

## 💡 Key Insights

- **Hottest framework**: Mastra with a Pulse Score of 73.7
- **Fastest growing**: Claude Agent SDK gained +3657 stars this week
- **Most active development**: Mastra with 609 commits in the last 4 weeks
- **Stale releases**: Swarm haven't released in a while

## 📦 Recent Releases

- **Claude Agent SDK** [`v2.1.104`](https://github.com/anthropics/claude-code/releases/tag/v2.1.104) — today
- **Composio** [`@composio/cli@0.2.23-beta.199`](https://github.com/ComposioHQ/composio/releases/tag/@composio/cli@0.2.23-beta.199) — 2 days ago *(pre-release)*
- **PydanticAI** [`v1.80.0`](https://github.com/pydantic/pydantic-ai/releases/tag/v1.80.0) — 2 days ago
- **LangGraph** [`1.1.7a1`](https://github.com/langchain-ai/langgraph/releases/tag/1.1.7a1) — 2 days ago
- **Agno** [`v2.5.16`](https://github.com/agno-agi/agno/releases/tag/v2.5.16) — 2 days ago
- **CrewAI** [`1.14.2a2`](https://github.com/crewAIInc/crewAI/releases/tag/1.14.2a2) — 2 days ago *(pre-release)*
- **Google ADK** [`v2.0.0a3`](https://github.com/google/adk-python/releases/tag/v2.0.0a3) — 3 days ago *(pre-release)*
- **OpenAI Agents SDK** [`v0.13.6`](https://github.com/openai/openai-agents-python/releases/tag/v0.13.6) — 4 days ago
- **Mastra** [`@mastra/core@1.24.0`](https://github.com/mastra-ai/mastra/releases/tag/@mastra/core@1.24.0) — 4 days ago
- **Semantic Kernel** [`python-1.41.2`](https://github.com/microsoft/semantic-kernel/releases/tag/python-1.41.2) — 5 days ago

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

*Powered by GitHub Actions • Data refreshed daily • Last run: 2026-04-13 08:13 UTC*