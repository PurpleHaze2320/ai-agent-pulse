# 🔬 AI Agent Framework Pulse Tracker

[![Daily Update](https://github.com/PurpleHaze2320/ai-agent-pulse/actions/workflows/track.yml/badge.svg)](https://github.com/PurpleHaze2320/ai-agent-pulse/actions/workflows/track.yml)
[![Frameworks Tracked](https://img.shields.io/badge/frameworks-19-blue)](https://github.com/PurpleHaze2320/ai-agent-pulse)
[![License: MIT](https://img.shields.io/badge/License-MIT-green.svg)](https://opensource.org/licenses/MIT)
[![GitHub stars](https://img.shields.io/github/stars/PurpleHaze2320/ai-agent-pulse?style=social)](https://github.com/PurpleHaze2320/ai-agent-pulse/stargazers)

> Automated daily tracking of the AI agent framework ecosystem's health, momentum, and trends.
> Last updated: **2026-07-10 09:44 UTC** | Tracking **19** frameworks

## How It Works

This bot runs daily via GitHub Actions and collects metrics from the GitHub API for the most important
AI agent frameworks. It computes a **Pulse Score** (0-100) based on six weighted signals: star velocity,
release freshness, issue health, commit activity, community size, and fork engagement. The result is
a living dashboard that shows which frameworks are gaining momentum and which are losing steam.

## 🏆 Pulse Leaderboard

| Rank | Framework | Pulse | Stars | ⭐ 7d | Commits (4w) | Last Release | Category |
|------|-----------|-------|-------|-------|--------------|--------------|----------|
| 1 | [CrewAI](https://github.com/crewAIInc/crewAI) | 🟢 **89.9** | 55.3k | 🚀 +465 | 105 | 2 days ago | `multi-agent` |
| 2 | [BrowserUse](https://github.com/browser-use/browser-use) | 🟢 **83.6** | 104.1k | 🚀 +1723 | 71 | 8 days ago | `web-agent` |
| 3 | [Mastra](https://github.com/mastra-ai/mastra) | 🟢 **79.7** | 26.0k | 🚀 +242 | 1028 | 1 day ago | `typescript` |
| 4 | [LangGraph](https://github.com/langchain-ai/langgraph) | 🟢 **78.2** | 37.0k | 🚀 +575 | 50 | today | `orchestration` |
| 5 | [PydanticAI](https://github.com/pydantic/pydantic-ai) | 🟢 **74.2** | 18.3k | 🚀 +127 | 208 | today | `structured` |
| 6 | [Google ADK](https://github.com/google/adk-python) | 🟢 **73.3** | 20.5k | 🚀 +121 | 347 | 2 days ago | `orchestration` |
| 7 | [OpenAI Agents SDK](https://github.com/openai/openai-agents-python) | 🟢 **73.3** | 27.8k | 🚀 +169 | 89 | today | `orchestration` |
| 8 | [Claude Agent SDK](https://github.com/anthropics/claude-code) | 🟢 **71.2** | 137.2k | 🚀 +1626 | 29 | today | `orchestration` |
| 9 | [LlamaIndex](https://github.com/run-llama/llama_index) | 🟡 **61.9** | 50.8k | 🚀 +140 | 26 | 15 days ago | `data-agent` |
| 10 | [Semantic Kernel](https://github.com/microsoft/semantic-kernel) | 🟡 **59.3** | 28.3k | 📈 +39 | 41 | 3 days ago | `enterprise` |
| 11 | [DSPy](https://github.com/stanfordnlp/dspy) | 🟡 **54.0** | 36.0k | 🚀 +234 | 5 | 1 mo ago | `optimization` |
| 12 | [Agno](https://github.com/agno-agi/agno) | 🟡 **51.7** | 41.1k | 🚀 +104 | 0 | today | `multi-agent` |
| 13 | [AG2](https://github.com/ag2ai/ag2) | 🟡 **50.0** | 4.8k | 📈 +27 | 0 | 6 days ago | `multi-agent` |
| 14 | [Haystack](https://github.com/deepset-ai/haystack) | 🟡 **49.7** | 25.9k | 📈 +43 | 0 | 1 day ago | `pipeline` |
| 15 | [Composio](https://github.com/ComposioHQ/composio) | 🟡 **46.5** | 29.2k | 📈 +82 | 0 | 2 days ago | `tooling` |
| 16 | [Letta](https://github.com/letta-ai/letta) | 🟡 **43.6** | 23.7k | 📈 +97 | 2 | 1 mo ago | `memory` |
| 17 | [Smolagents](https://github.com/huggingface/smolagents) | 🟡 **41.6** | 28.3k | 🚀 +111 | 4 | 1 mo ago | `lightweight` |
| 18 | [AutoGen](https://github.com/microsoft/autogen) | 🟠 **37.1** | 59.6k | 🚀 +167 | 0 | 9 mo ago | `multi-agent` |
| 19 | [Swarm](https://github.com/openai/swarm) | 🔴 **8.9** | 21.8k | ↗️ +17 | 0 | — | `experimental` |

## 📂 By Category

- `data-agent`: **LlamaIndex** (61.9)
- `enterprise`: **Semantic Kernel** (59.3)
- `experimental`: **Swarm** (8.9)
- `lightweight`: **Smolagents** (41.6)
- `memory`: **Letta** (43.6)
- `multi-agent`: **CrewAI** (89.9), **Agno** (51.7), **AG2** (50.0), **AutoGen** (37.1)
- `optimization`: **DSPy** (54.0)
- `orchestration`: **LangGraph** (78.2), **Google ADK** (73.3), **OpenAI Agents SDK** (73.3), **Claude Agent SDK** (71.2)
- `pipeline`: **Haystack** (49.7)
- `structured`: **PydanticAI** (74.2)
- `tooling`: **Composio** (46.5)
- `typescript`: **Mastra** (79.7)
- `web-agent`: **BrowserUse** (83.6)

## 🔍 Top 5 — Score Breakdown

| Framework | Star Velocity | Release Freshness | Issue Health | Commit Activity | Community | Fork Ratio |
|-----------|:---:|:---:|:---:|:---:|:---:|:---:|
| **CrewAI** | 96.4 | 99.3 | 95.7 | 100 | 59.6 | 56.3 |
| **BrowserUse** | 100 | 97.3 | 95.0 | 71.0 | 63.0 | 44.1 |
| **Mastra** | 50.3 | 99.7 | 95.2 | 100 | 92.6 | 36.8 |
| **LangGraph** | 100 | 100.0 | 73.2 | 50.0 | 55.0 | 67.1 |
| **PydanticAI** | 27.3 | 100.0 | 85.4 | 100 | 94.8 | 50.9 |

## 💡 Key Insights

- **Hottest framework**: CrewAI with a Pulse Score of 89.9
- **Fastest growing**: BrowserUse gained +1723 stars this week
- **Most active development**: Mastra with 1028 commits in the last 4 weeks
- **Stale releases**: AutoGen, Swarm haven't released in a while

## 📦 Recent Releases

- **PydanticAI** [`v2.8.0`](https://github.com/pydantic/pydantic-ai/releases/tag/v2.8.0) — today
- **Claude Agent SDK** [`v2.1.206`](https://github.com/anthropics/claude-code/releases/tag/v2.1.206) — today
- **LangGraph** [`1.2.9`](https://github.com/langchain-ai/langgraph/releases/tag/1.2.9) — today
- **OpenAI Agents SDK** [`v0.18.1`](https://github.com/openai/openai-agents-python/releases/tag/v0.18.1) — today
- **Agno** [`v2.7.2`](https://github.com/agno-agi/agno/releases/tag/v2.7.2) — today
- **Mastra** [`@mastra/core@1.50.0`](https://github.com/mastra-ai/mastra/releases/tag/@mastra/core@1.50.0) — 1 day ago
- **Haystack** [`v2.31.0`](https://github.com/deepset-ai/haystack/releases/tag/v2.31.0) — 1 day ago
- **CrewAI** [`1.15.2`](https://github.com/crewAIInc/crewAI/releases/tag/1.15.2) — 2 days ago
- **Google ADK** [`v2.4.0`](https://github.com/google/adk-python/releases/tag/v2.4.0) — 2 days ago
- **Composio** [`@composio/cli@0.2.32-beta.286`](https://github.com/ComposioHQ/composio/releases/tag/@composio/cli@0.2.32-beta.286) — 2 days ago *(pre-release)*

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

*Powered by GitHub Actions • Data refreshed daily • Last run: 2026-07-10 09:44 UTC*