# 🔬 AI Agent Framework Pulse Tracker

[![Daily Update](https://github.com/PurpleHaze2320/ai-agent-pulse/actions/workflows/track.yml/badge.svg)](https://github.com/PurpleHaze2320/ai-agent-pulse/actions/workflows/track.yml)
[![Frameworks Tracked](https://img.shields.io/badge/frameworks-19-blue)](https://github.com/PurpleHaze2320/ai-agent-pulse)
[![License: MIT](https://img.shields.io/badge/License-MIT-green.svg)](https://opensource.org/licenses/MIT)
[![GitHub stars](https://img.shields.io/github/stars/PurpleHaze2320/ai-agent-pulse?style=social)](https://github.com/PurpleHaze2320/ai-agent-pulse/stargazers)

> Automated daily tracking of the AI agent framework ecosystem's health, momentum, and trends.
> Last updated: **2026-04-16 07:57 UTC** | Tracking **19** frameworks

## How It Works

This bot runs daily via GitHub Actions and collects metrics from the GitHub API for the most important
AI agent frameworks. It computes a **Pulse Score** (0-100) based on six weighted signals: star velocity,
release freshness, issue health, commit activity, community size, and fork engagement. The result is
a living dashboard that shows which frameworks are gaining momentum and which are losing steam.

## 🏆 Pulse Leaderboard

| Rank | Framework | Pulse | Stars | ⭐ 7d | Commits (4w) | Last Release | Category |
|------|-----------|-------|-------|-------|--------------|--------------|----------|
| 1 | [Mastra](https://github.com/mastra-ai/mastra) | 🟢 **74.4** | 23.0k | 🚀 +227 | 737 | 7 days ago | `typescript` |
| 2 | [CrewAI](https://github.com/crewAIInc/crewAI) | 🟢 **70.6** | 49.0k | 🚀 +591 | 0 | today | `multi-agent` |
| 3 | [BrowserUse](https://github.com/browser-use/browser-use) | 🟡 **69.5** | 88.0k | 🚀 +1413 | 0 | 14 days ago | `web-agent` |
| 4 | [LangGraph](https://github.com/langchain-ai/langgraph) | 🟡 **69.3** | 29.4k | 🚀 +647 | 0 | today | `orchestration` |
| 5 | [Claude Agent SDK](https://github.com/anthropics/claude-code) | 🟡 **64.5** | 114.6k | 🚀 +3228 | 0 | today | `orchestration` |
| 6 | [LlamaIndex](https://github.com/run-llama/llama_index) | 🟡 **57.8** | 48.6k | 🚀 +200 | 0 | 12 days ago | `data-agent` |
| 7 | [OpenAI Agents SDK](https://github.com/openai/openai-agents-python) | 🟡 **54.9** | 20.9k | 🚀 +223 | 0 | today | `orchestration` |
| 8 | [PydanticAI](https://github.com/pydantic/pydantic-ai) | 🟡 **54.5** | 16.4k | 🚀 +216 | 0 | today | `structured` |
| 9 | [Agno](https://github.com/agno-agi/agno) | 🟡 **54.3** | 39.5k | 🚀 +193 | 0 | 1 day ago | `multi-agent` |
| 10 | [Google ADK](https://github.com/google/adk-python) | 🟡 **51.6** | 19.0k | 🚀 +180 | 0 | 2 days ago | `orchestration` |
| 11 | [Semantic Kernel](https://github.com/microsoft/semantic-kernel) | 🟡 **49.6** | 27.7k | 📈 +41 | 0 | 8 days ago | `enterprise` |
| 12 | [Haystack](https://github.com/deepset-ai/haystack) | 🟡 **48.2** | 24.8k | 📈 +77 | 0 | 14 days ago | `pipeline` |
| 13 | [DSPy](https://github.com/stanfordnlp/dspy) | 🟡 **46.8** | 33.7k | 🚀 +196 | 0 | 2 mo ago | `optimization` |
| 14 | [AG2](https://github.com/ag2ai/ag2) | 🟡 **46.7** | 4.4k | 📈 +25 | 0 | 11 days ago | `multi-agent` |
| 15 | [AutoGen](https://github.com/microsoft/autogen) | 🟡 **46.1** | 57.1k | 🚀 +281 | 0 | 6 mo ago | `multi-agent` |
| 16 | [Letta](https://github.com/letta-ai/letta) | 🟡 **46.1** | 22.1k | 🚀 +141 | 0 | 15 days ago | `memory` |
| 17 | [Composio](https://github.com/ComposioHQ/composio) | 🟡 **44.9** | 27.8k | 🚀 +106 | 0 | 1 day ago | `tooling` |
| 18 | [Smolagents](https://github.com/huggingface/smolagents) | 🟠 **37.8** | 26.6k | 🚀 +142 | 0 | 3 mo ago | `lightweight` |
| 19 | [Swarm](https://github.com/openai/swarm) | 🔴 **9.4** | 21.3k | 📈 +30 | 0 | — | `experimental` |

## 📂 By Category

- `data-agent`: **LlamaIndex** (57.8)
- `enterprise`: **Semantic Kernel** (49.6)
- `experimental`: **Swarm** (9.4)
- `lightweight`: **Smolagents** (37.8)
- `memory`: **Letta** (46.1)
- `multi-agent`: **CrewAI** (70.6), **Agno** (54.3), **AG2** (46.7), **AutoGen** (46.1)
- `optimization`: **DSPy** (46.8)
- `orchestration`: **LangGraph** (69.3), **Claude Agent SDK** (64.5), **OpenAI Agents SDK** (54.9), **Google ADK** (51.6)
- `pipeline`: **Haystack** (48.2)
- `structured`: **PydanticAI** (54.5)
- `tooling`: **Composio** (44.9)
- `typescript`: **Mastra** (74.4)
- `web-agent`: **BrowserUse** (69.5)

## 🔍 Top 5 — Score Breakdown

| Framework | Star Velocity | Release Freshness | Issue Health | Commit Activity | Community | Fork Ratio |
|-----------|:---:|:---:|:---:|:---:|:---:|:---:|
| **Mastra** | 38.9 | 97.7 | 94.3 | 100 | 76.6 | 32.9 |
| **CrewAI** | 100 | 100.0 | 95.9 | 0.0 | 57.0 | 54.7 |
| **BrowserUse** | 100 | 95.3 | 97.8 | 0.0 | 61.8 | 46.0 |
| **LangGraph** | 100 | 100.0 | 80.0 | 0.0 | 54.4 | 68.5 |
| **Claude Agent SDK** | 100 | 100.0 | 79.4 | 0.0 | 9.4 | 66.8 |

## 💡 Key Insights

- **Hottest framework**: Mastra with a Pulse Score of 74.4
- **Fastest growing**: Claude Agent SDK gained +3228 stars this week
- **Most active development**: Mastra with 737 commits in the last 4 weeks
- **Stale releases**: Swarm haven't released in a while

## 📦 Recent Releases

- **PydanticAI** [`v1.83.0`](https://github.com/pydantic/pydantic-ai/releases/tag/v1.83.0) — today
- **Claude Agent SDK** [`v2.1.110`](https://github.com/anthropics/claude-code/releases/tag/v2.1.110) — today
- **CrewAI** [`1.14.2rc1`](https://github.com/crewAIInc/crewAI/releases/tag/1.14.2rc1) — today *(pre-release)*
- **LangGraph** [`checkpoint==4.0.2`](https://github.com/langchain-ai/langgraph/releases/tag/checkpoint==4.0.2) — today
- **OpenAI Agents SDK** [`v0.14.1`](https://github.com/openai/openai-agents-python/releases/tag/v0.14.1) — today
- **Composio** [`@composio/cli@0.2.25-beta.211`](https://github.com/ComposioHQ/composio/releases/tag/@composio/cli@0.2.25-beta.211) — 1 day ago *(pre-release)*
- **Agno** [`v2.5.17`](https://github.com/agno-agi/agno/releases/tag/v2.5.17) — 1 day ago
- **Google ADK** [`v1.30.0`](https://github.com/google/adk-python/releases/tag/v1.30.0) — 2 days ago
- **Mastra** [`@mastra/core@1.24.0`](https://github.com/mastra-ai/mastra/releases/tag/@mastra/core@1.24.0) — 7 days ago
- **Semantic Kernel** [`python-1.41.2`](https://github.com/microsoft/semantic-kernel/releases/tag/python-1.41.2) — 8 days ago

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

*Powered by GitHub Actions • Data refreshed daily • Last run: 2026-04-16 07:57 UTC*