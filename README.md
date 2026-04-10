# 🔬 AI Agent Framework Pulse Tracker

[![Daily Update](https://github.com/PurpleHaze2320/ai-agent-pulse/actions/workflows/track.yml/badge.svg)](https://github.com/PurpleHaze2320/ai-agent-pulse/actions/workflows/track.yml)
[![Frameworks Tracked](https://img.shields.io/badge/frameworks-19-blue)](https://github.com/PurpleHaze2320/ai-agent-pulse)
[![License: MIT](https://img.shields.io/badge/License-MIT-green.svg)](https://opensource.org/licenses/MIT)
[![GitHub stars](https://img.shields.io/github/stars/PurpleHaze2320/ai-agent-pulse?style=social)](https://github.com/PurpleHaze2320/ai-agent-pulse/stargazers)

> Automated daily tracking of the AI agent framework ecosystem's health, momentum, and trends.
> Last updated: **2026-04-10 07:51 UTC** | Tracking **19** frameworks

## How It Works

This bot runs daily via GitHub Actions and collects metrics from the GitHub API for the most important
AI agent frameworks. It computes a **Pulse Score** (0-100) based on six weighted signals: star velocity,
release freshness, issue health, commit activity, community size, and fork engagement. The result is
a living dashboard that shows which frameworks are gaining momentum and which are losing steam.

## 🏆 Pulse Leaderboard

| Rank | Framework | Pulse | Stars | ⭐ 7d | Commits (4w) | Last Release | Category |
|------|-----------|-------|-------|-------|--------------|--------------|----------|
| 1 | [Mastra](https://github.com/mastra-ai/mastra) | 🟢 **74.1** | 22.9k | 🚀 +233 | 805 | 1 day ago | `typescript` |
| 2 | [BrowserUse](https://github.com/browser-use/browser-use) | 🟡 **69.9** | 86.9k | 🚀 +1107 | 0 | 7 days ago | `web-agent` |
| 3 | [CrewAI](https://github.com/crewAIInc/crewAI) | 🟡 **68.8** | 48.5k | 🚀 +598 | 0 | 1 day ago | `multi-agent` |
| 4 | [LangGraph](https://github.com/langchain-ai/langgraph) | 🟡 **66.4** | 28.9k | 🚀 +562 | 0 | 2 days ago | `orchestration` |
| 5 | [Claude Agent SDK](https://github.com/anthropics/claude-code) | 🟡 **64.5** | 111.9k | 🚀 +4753 | 0 | today | `orchestration` |
| 6 | [LlamaIndex](https://github.com/run-llama/llama_index) | 🟡 **58.3** | 48.5k | 🚀 +220 | 0 | 6 days ago | `data-agent` |
| 7 | [Agno](https://github.com/agno-agi/agno) | 🟡 **53.4** | 39.3k | 🚀 +186 | 0 | 1 day ago | `multi-agent` |
| 8 | [PydanticAI](https://github.com/pydantic/pydantic-ai) | 🟡 **51.8** | 16.2k | 🚀 +168 | 0 | today | `structured` |
| 9 | [OpenAI Agents SDK](https://github.com/openai/openai-agents-python) | 🟡 **51.2** | 20.7k | 🚀 +146 | 0 | 1 day ago | `orchestration` |
| 10 | [Semantic Kernel](https://github.com/microsoft/semantic-kernel) | 🟡 **50.1** | 27.7k | 📈 +49 | 0 | 2 days ago | `enterprise` |
| 11 | [Google ADK](https://github.com/google/adk-python) | 🟡 **49.4** | 18.9k | 🚀 +131 | 0 | today | `orchestration` |
| 12 | [Haystack](https://github.com/deepset-ai/haystack) | 🟡 **48.9** | 24.8k | 📈 +94 | 0 | 8 days ago | `pipeline` |
| 13 | [AG2](https://github.com/ag2ai/ag2) | 🟡 **47.2** | 4.4k | 📈 +32 | 0 | 5 days ago | `multi-agent` |
| 14 | [AutoGen](https://github.com/microsoft/autogen) | 🟡 **45.7** | 56.9k | 🚀 +281 | 0 | 6 mo ago | `multi-agent` |
| 15 | [DSPy](https://github.com/stanfordnlp/dspy) | 🟡 **45.6** | 33.6k | 🚀 +167 | 0 | 2 mo ago | `optimization` |
| 16 | [Letta](https://github.com/letta-ai/letta) | 🟡 **44.9** | 22.0k | 🚀 +111 | 0 | 9 days ago | `memory` |
| 17 | [Composio](https://github.com/ComposioHQ/composio) | 🟡 **43.8** | 27.7k | 📈 +81 | 0 | today | `tooling` |
| 18 | [Smolagents](https://github.com/huggingface/smolagents) | 🟠 **36.6** | 26.5k | 🚀 +112 | 0 | 2 mo ago | `lightweight` |
| 19 | [Swarm](https://github.com/openai/swarm) | 🔴 **8.6** | 21.3k | ↗️ +6 | 0 | — | `experimental` |

## 📂 By Category

- `data-agent`: **LlamaIndex** (58.3)
- `enterprise`: **Semantic Kernel** (50.1)
- `experimental`: **Swarm** (8.6)
- `lightweight`: **Smolagents** (36.6)
- `memory`: **Letta** (44.9)
- `multi-agent`: **CrewAI** (68.8), **Agno** (53.4), **AG2** (47.2), **AutoGen** (45.7)
- `optimization`: **DSPy** (45.6)
- `orchestration`: **LangGraph** (66.4), **Claude Agent SDK** (64.5), **OpenAI Agents SDK** (51.2), **Google ADK** (49.4)
- `pipeline`: **Haystack** (48.9)
- `structured`: **PydanticAI** (51.8)
- `tooling`: **Composio** (43.8)
- `typescript`: **Mastra** (74.1)
- `web-agent`: **BrowserUse** (69.9)

## 🔍 Top 5 — Score Breakdown

| Framework | Star Velocity | Release Freshness | Issue Health | Commit Activity | Community | Fork Ratio |
|-----------|:---:|:---:|:---:|:---:|:---:|:---:|
| **Mastra** | 36.9 | 99.7 | 93.9 | 100 | 75.6 | 32.7 |
| **BrowserUse** | 100 | 97.7 | 97.3 | 0.0 | 61.2 | 46.2 |
| **CrewAI** | 94.0 | 99.7 | 94.9 | 0.0 | 56.8 | 54.6 |
| **LangGraph** | 88.9 | 99.3 | 80.1 | 0.0 | 54.2 | 68.4 |
| **Claude Agent SDK** | 100 | 100.0 | 79.2 | 0.0 | 9.4 | 66.7 |

## 💡 Key Insights

- **Hottest framework**: Mastra with a Pulse Score of 74.1
- **Fastest growing**: Claude Agent SDK gained +4753 stars this week
- **Most active development**: Mastra with 805 commits in the last 4 weeks
- **Stale releases**: Swarm haven't released in a while

## 📦 Recent Releases

- **Composio** [`@composio/cli@0.2.21-beta.196`](https://github.com/ComposioHQ/composio/releases/tag/@composio/cli@0.2.21-beta.196) — today *(pre-release)*
- **Claude Agent SDK** [`v2.1.100`](https://github.com/anthropics/claude-code/releases/tag/v2.1.100) — today
- **PydanticAI** [`v1.79.0`](https://github.com/pydantic/pydantic-ai/releases/tag/v1.79.0) — today
- **Google ADK** [`v2.0.0a3`](https://github.com/google/adk-python/releases/tag/v2.0.0a3) — today *(pre-release)*
- **Agno** [`v2.5.15`](https://github.com/agno-agi/agno/releases/tag/v2.5.15) — 1 day ago
- **OpenAI Agents SDK** [`v0.13.6`](https://github.com/openai/openai-agents-python/releases/tag/v0.13.6) — 1 day ago
- **CrewAI** [`1.14.2a1`](https://github.com/crewAIInc/crewAI/releases/tag/1.14.2a1) — 1 day ago *(pre-release)*
- **Mastra** [`@mastra/core@1.24.0`](https://github.com/mastra-ai/mastra/releases/tag/@mastra/core@1.24.0) — 1 day ago
- **Semantic Kernel** [`python-1.41.2`](https://github.com/microsoft/semantic-kernel/releases/tag/python-1.41.2) — 2 days ago
- **LangGraph** [`cli==0.4.21`](https://github.com/langchain-ai/langgraph/releases/tag/cli==0.4.21) — 2 days ago

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

*Powered by GitHub Actions • Data refreshed daily • Last run: 2026-04-10 07:51 UTC*