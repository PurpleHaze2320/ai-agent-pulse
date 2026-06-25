# 🔬 AI Agent Framework Pulse Tracker

[![Daily Update](https://github.com/PurpleHaze2320/ai-agent-pulse/actions/workflows/track.yml/badge.svg)](https://github.com/PurpleHaze2320/ai-agent-pulse/actions/workflows/track.yml)
[![Frameworks Tracked](https://img.shields.io/badge/frameworks-19-blue)](https://github.com/PurpleHaze2320/ai-agent-pulse)
[![License: MIT](https://img.shields.io/badge/License-MIT-green.svg)](https://opensource.org/licenses/MIT)
[![GitHub stars](https://img.shields.io/github/stars/PurpleHaze2320/ai-agent-pulse?style=social)](https://github.com/PurpleHaze2320/ai-agent-pulse/stargazers)

> Automated daily tracking of the AI agent framework ecosystem's health, momentum, and trends.
> Last updated: **2026-06-25 09:32 UTC** | Tracking **19** frameworks

## How It Works

This bot runs daily via GitHub Actions and collects metrics from the GitHub API for the most important
AI agent frameworks. It computes a **Pulse Score** (0-100) based on six weighted signals: star velocity,
release freshness, issue health, commit activity, community size, and fork engagement. The result is
a living dashboard that shows which frameworks are gaining momentum and which are losing steam.

## 🏆 Pulse Leaderboard

| Rank | Framework | Pulse | Stars | ⭐ 7d | Commits (4w) | Last Release | Category |
|------|-----------|-------|-------|-------|--------------|--------------|----------|
| 1 | [BrowserUse](https://github.com/browser-use/browser-use) | 🟢 **89.3** | 100.6k | 🚀 +1185 | 409 | 12 days ago | `web-agent` |
| 2 | [Mastra](https://github.com/mastra-ai/mastra) | 🟢 **79.8** | 25.4k | 🚀 +243 | 919 | today | `typescript` |
| 3 | [LangGraph](https://github.com/langchain-ai/langgraph) | 🟢 **78.9** | 35.7k | 🚀 +585 | 55 | 6 days ago | `orchestration` |
| 4 | [PydanticAI](https://github.com/pydantic/pydantic-ai) | 🟢 **73.7** | 18.0k | 🚀 +168 | 92 | 1 day ago | `structured` |
| 5 | [Google ADK](https://github.com/google/adk-python) | 🟢 **72.0** | 20.3k | 🚀 +123 | 289 | 6 days ago | `orchestration` |
| 6 | [Claude Agent SDK](https://github.com/anthropics/claude-code) | 🟢 **71.7** | 134.3k | 🚀 +1132 | 30 | today | `orchestration` |
| 7 | [Agno](https://github.com/agno-agi/agno) | 🟢 **70.6** | 40.8k | 📈 +81 | 98 | 1 day ago | `multi-agent` |
| 8 | [CrewAI](https://github.com/crewAIInc/crewAI) | 🟢 **70.2** | 54.3k | 🚀 +464 | 0 | today | `multi-agent` |
| 9 | [Composio](https://github.com/ComposioHQ/composio) | 🟡 **65.8** | 29.0k | 🚀 +127 | 87 | today | `tooling` |
| 10 | [OpenAI Agents SDK](https://github.com/openai/openai-agents-python) | 🟡 **65.1** | 27.4k | 🚀 +177 | 48 | 1 day ago | `orchestration` |
| 11 | [LlamaIndex](https://github.com/run-llama/llama_index) | 🟡 **60.7** | 50.4k | 🚀 +164 | 11 | today | `data-agent` |
| 12 | [DSPy](https://github.com/stanfordnlp/dspy) | 🟡 **57.4** | 35.4k | 🚀 +264 | 18 | 28 days ago | `optimization` |
| 13 | [Semantic Kernel](https://github.com/microsoft/semantic-kernel) | 🟡 **56.3** | 28.2k | 📈 +37 | 28 | 8 days ago | `enterprise` |
| 14 | [Haystack](https://github.com/deepset-ai/haystack) | 🟡 **51.5** | 25.7k | 🚀 +114 | 0 | 7 days ago | `pipeline` |
| 15 | [AG2](https://github.com/ag2ai/ag2) | 🟡 **47.9** | 4.7k | 📈 +23 | 0 | 12 days ago | `multi-agent` |
| 16 | [Letta](https://github.com/letta-ai/letta) | 🟡 **45.0** | 23.5k | 🚀 +119 | 0 | 1 mo ago | `memory` |
| 17 | [Smolagents](https://github.com/huggingface/smolagents) | 🟡 **41.4** | 28.0k | 📈 +87 | 2 | 27 days ago | `lightweight` |
| 18 | [AutoGen](https://github.com/microsoft/autogen) | 🟠 **38.9** | 59.2k | 🚀 +183 | 0 | 8 mo ago | `multi-agent` |
| 19 | [Swarm](https://github.com/openai/swarm) | 🔴 **10.8** | 21.7k | 📈 +80 | 0 | — | `experimental` |

## 📂 By Category

- `data-agent`: **LlamaIndex** (60.7)
- `enterprise`: **Semantic Kernel** (56.3)
- `experimental`: **Swarm** (10.8)
- `lightweight`: **Smolagents** (41.4)
- `memory`: **Letta** (45.0)
- `multi-agent`: **Agno** (70.6), **CrewAI** (70.2), **AG2** (47.9), **AutoGen** (38.9)
- `optimization`: **DSPy** (57.4)
- `orchestration`: **LangGraph** (78.9), **Google ADK** (72.0), **Claude Agent SDK** (71.7), **OpenAI Agents SDK** (65.1)
- `pipeline`: **Haystack** (51.5)
- `structured`: **PydanticAI** (73.7)
- `tooling`: **Composio** (65.8)
- `typescript`: **Mastra** (79.8)
- `web-agent`: **BrowserUse** (89.3)

## 🔍 Top 5 — Score Breakdown

| Framework | Star Velocity | Release Freshness | Issue Health | Commit Activity | Community | Fork Ratio |
|-----------|:---:|:---:|:---:|:---:|:---:|:---:|
| **BrowserUse** | 100 | 96.0 | 95.4 | 100 | 63.0 | 44.5 |
| **Mastra** | 50.8 | 100.0 | 95.2 | 100 | 92.0 | 35.9 |
| **LangGraph** | 100 | 98.0 | 74.3 | 55.0 | 55.0 | 67.0 |
| **PydanticAI** | 33.8 | 99.7 | 82.7 | 92.0 | 95.4 | 50.1 |
| **Google ADK** | 23.6 | 98.0 | 84.5 | 100 | 67.2 | 71.3 |

## 💡 Key Insights

- **Hottest framework**: BrowserUse with a Pulse Score of 89.3
- **Fastest growing**: BrowserUse gained +1185 stars this week
- **Most active development**: Mastra with 919 commits in the last 4 weeks
- **Stale releases**: Swarm haven't released in a while

## 📦 Recent Releases

- **Composio** [`@composio/vercel@0.10.0`](https://github.com/ComposioHQ/composio/releases/tag/@composio/vercel@0.10.0) — today
- **CrewAI** [`1.14.8a5`](https://github.com/crewAIInc/crewAI/releases/tag/1.14.8a5) — today *(pre-release)*
- **Claude Agent SDK** [`v2.1.191`](https://github.com/anthropics/claude-code/releases/tag/v2.1.191) — today
- **LlamaIndex** [`v0.14.23`](https://github.com/run-llama/llama_index/releases/tag/v0.14.23) — today
- **Mastra** [`@mastra/core@1.46.0`](https://github.com/mastra-ai/mastra/releases/tag/@mastra/core@1.46.0) — today
- **OpenAI Agents SDK** [`v0.17.7`](https://github.com/openai/openai-agents-python/releases/tag/v0.17.7) — 1 day ago
- **PydanticAI** [`v2.0.0`](https://github.com/pydantic/pydantic-ai/releases/tag/v2.0.0) — 1 day ago
- **Agno** [`v2.6.19`](https://github.com/agno-agi/agno/releases/tag/v2.6.19) — 1 day ago
- **LangGraph** [`1.2.6`](https://github.com/langchain-ai/langgraph/releases/tag/1.2.6) — 6 days ago
- **Google ADK** [`v2.3.0`](https://github.com/google/adk-python/releases/tag/v2.3.0) — 6 days ago

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

*Powered by GitHub Actions • Data refreshed daily • Last run: 2026-06-25 09:32 UTC*