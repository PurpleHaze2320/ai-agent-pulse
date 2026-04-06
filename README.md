# 🔬 AI Agent Framework Pulse Tracker

[![Daily Update](https://github.com/PurpleHaze2320/ai-agent-pulse/actions/workflows/track.yml/badge.svg)](https://github.com/PurpleHaze2320/ai-agent-pulse/actions/workflows/track.yml)
[![Frameworks Tracked](https://img.shields.io/badge/frameworks-19-blue)](https://github.com/PurpleHaze2320/ai-agent-pulse)
[![License: MIT](https://img.shields.io/badge/License-MIT-green.svg)](https://opensource.org/licenses/MIT)
[![GitHub stars](https://img.shields.io/github/stars/PurpleHaze2320/ai-agent-pulse?style=social)](https://github.com/PurpleHaze2320/ai-agent-pulse/stargazers)

> Automated daily tracking of the AI agent framework ecosystem's health, momentum, and trends.
> Last updated: **2026-04-06 07:54 UTC** | Tracking **19** frameworks

## How It Works

This bot runs daily via GitHub Actions and collects metrics from the GitHub API for the most important
AI agent frameworks. It computes a **Pulse Score** (0-100) based on six weighted signals: star velocity,
release freshness, issue health, commit activity, community size, and fork engagement. The result is
a living dashboard that shows which frameworks are gaining momentum and which are losing steam.

## 🏆 Pulse Leaderboard

| Rank | Framework | Pulse | Stars | ⭐ 7d | Commits (4w) | Last Release | Category |
|------|-----------|-------|-------|-------|--------------|--------------|----------|
| 1 | [Mastra](https://github.com/mastra-ai/mastra) | 🟡 **69.7** | 22.7k | 🚀 +144 | 654 | 10 days ago | `typescript` |
| 2 | [BrowserUse](https://github.com/browser-use/browser-use) | 🟡 **69.3** | 86.2k | 🚀 +623 | 0 | 3 days ago | `web-agent` |
| 3 | [Claude Agent SDK](https://github.com/anthropics/claude-code) | 🟡 **64.3** | 109.5k | 🚀 +7419 | 0 | 2 days ago | `orchestration` |
| 4 | [CrewAI](https://github.com/crewAIInc/crewAI) | 🟡 **57.6** | 48.1k | 🚀 +318 | 0 | today | `multi-agent` |
| 5 | [LangGraph](https://github.com/langchain-ai/langgraph) | 🟡 **56.9** | 28.5k | 🚀 +327 | 0 | 2 days ago | `orchestration` |
| 6 | [LlamaIndex](https://github.com/run-llama/llama_index) | 🟡 **54.0** | 48.3k | 🚀 +107 | 0 | 2 days ago | `data-agent` |
| 7 | [Agno](https://github.com/agno-agi/agno) | 🟡 **49.6** | 39.2k | 📈 +99 | 0 | 3 days ago | `multi-agent` |
| 8 | [Semantic Kernel](https://github.com/microsoft/semantic-kernel) | 🟡 **49.2** | 27.7k | 📈 +44 | 0 | 12 days ago | `enterprise` |
| 9 | [OpenAI Agents SDK](https://github.com/openai/openai-agents-python) | 🟡 **49.1** | 20.6k | 📈 +95 | 0 | today | `orchestration` |
| 10 | [PydanticAI](https://github.com/pydantic/pydantic-ai) | 🟡 **48.1** | 16.1k | 📈 +95 | 0 | 3 days ago | `structured` |
| 11 | [Haystack](https://github.com/deepset-ai/haystack) | 🟡 **47.2** | 24.7k | 📈 +45 | 0 | 4 days ago | `pipeline` |
| 12 | [AG2](https://github.com/ag2ai/ag2) | 🟡 **47.0** | 4.4k | ↗️ +20 | 0 | 1 day ago | `multi-agent` |
| 13 | [Google ADK](https://github.com/google/adk-python) | 🟡 **46.8** | 18.8k | 📈 +72 | 0 | 3 days ago | `orchestration` |
| 14 | [DSPy](https://github.com/stanfordnlp/dspy) | 🟡 **43.2** | 33.5k | 🚀 +103 | 0 | 1 mo ago | `optimization` |
| 15 | [Letta](https://github.com/letta-ai/letta) | 🟡 **43.2** | 21.9k | 📈 +60 | 0 | 5 days ago | `memory` |
| 16 | [Composio](https://github.com/ComposioHQ/composio) | 🟡 **42.4** | 27.7k | 📈 +47 | 0 | 3 days ago | `tooling` |
| 17 | [AutoGen](https://github.com/microsoft/autogen) | 🟡 **40.9** | 56.7k | 🚀 +154 | 0 | 6 mo ago | `multi-agent` |
| 18 | [Smolagents](https://github.com/huggingface/smolagents) | 🟠 **35.3** | 26.5k | 📈 +71 | 0 | 2 mo ago | `lightweight` |
| 19 | [Swarm](https://github.com/openai/swarm) | 🔴 **8.8** | 21.3k | ↗️ +5 | 0 | — | `experimental` |

## 📂 By Category

- `data-agent`: **LlamaIndex** (54.0)
- `enterprise`: **Semantic Kernel** (49.2)
- `experimental`: **Swarm** (8.8)
- `lightweight`: **Smolagents** (35.3)
- `memory`: **Letta** (43.2)
- `multi-agent`: **CrewAI** (57.6), **Agno** (49.6), **AG2** (47.0), **AutoGen** (40.9)
- `optimization`: **DSPy** (43.2)
- `orchestration`: **Claude Agent SDK** (64.3), **LangGraph** (56.9), **OpenAI Agents SDK** (49.1), **Google ADK** (46.8)
- `pipeline`: **Haystack** (47.2)
- `structured`: **PydanticAI** (48.1)
- `tooling`: **Composio** (42.4)
- `typescript`: **Mastra** (69.7)
- `web-agent`: **BrowserUse** (69.3)

## 🔍 Top 5 — Score Breakdown

| Framework | Star Velocity | Release Freshness | Issue Health | Commit Activity | Community | Fork Ratio |
|-----------|:---:|:---:|:---:|:---:|:---:|:---:|
| **Mastra** | 22.3 | 96.7 | 94.0 | 100 | 74.8 | 32.5 |
| **BrowserUse** | 96.6 | 99.0 | 97.7 | 0.0 | 61.0 | 46.3 |
| **Claude Agent SDK** | 100 | 99.3 | 79.2 | 0.0 | 9.4 | 66.4 |
| **CrewAI** | 49.3 | 100.0 | 94.6 | 0.0 | 56.8 | 54.5 |
| **LangGraph** | 50.7 | 99.3 | 80.7 | 0.0 | 54.4 | 68.4 |

## 💡 Key Insights

- **Hottest framework**: Mastra with a Pulse Score of 69.7
- **Fastest growing**: Claude Agent SDK gained +7419 stars this week
- **Most active development**: Mastra with 654 commits in the last 4 weeks
- **Stale releases**: Swarm haven't released in a while

## 📦 Recent Releases

- **CrewAI** [`1.14.0a2`](https://github.com/crewAIInc/crewAI/releases/tag/1.14.0a2) — today *(pre-release)*
- **OpenAI Agents SDK** [`v0.13.5`](https://github.com/openai/openai-agents-python/releases/tag/v0.13.5) — today
- **AG2** [`v0.11.5`](https://github.com/ag2ai/ag2/releases/tag/v0.11.5) — 1 day ago
- **Claude Agent SDK** [`v2.1.92`](https://github.com/anthropics/claude-code/releases/tag/v2.1.92) — 2 days ago
- **LlamaIndex** [`v0.14.20`](https://github.com/run-llama/llama_index/releases/tag/v0.14.20) — 2 days ago
- **LangGraph** [`1.1.6`](https://github.com/langchain-ai/langgraph/releases/tag/1.1.6) — 2 days ago
- **PydanticAI** [`v1.77.0`](https://github.com/pydantic/pydantic-ai/releases/tag/v1.77.0) — 3 days ago
- **Google ADK** [`v1.28.1`](https://github.com/google/adk-python/releases/tag/v1.28.1) — 3 days ago
- **Agno** [`v2.5.14`](https://github.com/agno-agi/agno/releases/tag/v2.5.14) — 3 days ago
- **Composio** [`@composio/vercel@0.6.8`](https://github.com/ComposioHQ/composio/releases/tag/@composio/vercel@0.6.8) — 3 days ago

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

*Powered by GitHub Actions • Data refreshed daily • Last run: 2026-04-06 07:54 UTC*