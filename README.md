# 🔬 AI Agent Framework Pulse Tracker

[![Daily Update](https://github.com/PurpleHaze2320/ai-agent-pulse/actions/workflows/track.yml/badge.svg)](https://github.com/PurpleHaze2320/ai-agent-pulse/actions/workflows/track.yml)
[![Frameworks Tracked](https://img.shields.io/badge/frameworks-19-blue)](https://github.com/PurpleHaze2320/ai-agent-pulse)
[![License: MIT](https://img.shields.io/badge/License-MIT-green.svg)](https://opensource.org/licenses/MIT)
[![GitHub stars](https://img.shields.io/github/stars/PurpleHaze2320/ai-agent-pulse?style=social)](https://github.com/PurpleHaze2320/ai-agent-pulse/stargazers)

> Automated daily tracking of the AI agent framework ecosystem's health, momentum, and trends.
> Last updated: **2026-07-30 08:35 UTC** | Tracking **19** frameworks

## How It Works

This bot runs daily via GitHub Actions and collects metrics from the GitHub API for the most important
AI agent frameworks. It computes a **Pulse Score** (0-100) based on six weighted signals: star velocity,
release freshness, issue health, commit activity, community size, and fork engagement. The result is
a living dashboard that shows which frameworks are gaining momentum and which are losing steam.

## 🏆 Pulse Leaderboard

| Rank | Framework | Pulse | Stars | ⭐ 7d | Commits (4w) | Last Release | Category |
|------|-----------|-------|-------|-------|--------------|--------------|----------|
| 1 | [BrowserUse](https://github.com/browser-use/browser-use) | 🟢 **85.0** | 107.3k | 🚀 +1062 | 76 | 2 days ago | `web-agent` |
| 2 | [CrewAI](https://github.com/crewAIInc/crewAI) | 🟢 **80.3** | 56.4k | 🚀 +369 | 74 | today | `multi-agent` |
| 3 | [Mastra](https://github.com/mastra-ai/mastra) | 🟢 **80.0** | 26.7k | 🚀 +251 | 1106 | 1 day ago | `typescript` |
| 4 | [OpenAI Agents SDK](https://github.com/openai/openai-agents-python) | 🟢 **76.1** | 28.3k | 🚀 +173 | 162 | 1 day ago | `orchestration` |
| 5 | [Google ADK](https://github.com/google/adk-python) | 🟢 **73.3** | 20.9k | 📈 +96 | 325 | 8 days ago | `orchestration` |
| 6 | [Agno](https://github.com/agno-agi/agno) | 🟢 **73.0** | 41.5k | 🚀 +129 | 135 | 2 days ago | `multi-agent` |
| 7 | [LangGraph](https://github.com/langchain-ai/langgraph) | 🟢 **71.7** | 38.5k | 🚀 +576 | 19 | 1 day ago | `orchestration` |
| 8 | [Haystack](https://github.com/deepset-ai/haystack) | 🟢 **70.3** | 26.1k | 📈 +76 | 246 | 9 days ago | `pipeline` |
| 9 | [Claude Agent SDK](https://github.com/anthropics/claude-code) | 🟡 **68.9** | 139.6k | 🚀 +818 | 21 | 5 days ago | `orchestration` |
| 10 | [Composio](https://github.com/ComposioHQ/composio) | 🟡 **67.8** | 29.5k | 🚀 +123 | 144 | 9 days ago | `tooling` |
| 11 | [LlamaIndex](https://github.com/run-llama/llama_index) | 🟡 **60.6** | 51.2k | 🚀 +193 | 17 | 1 mo ago | `data-agent` |
| 12 | [PydanticAI](https://github.com/pydantic/pydantic-ai) | 🟡 **55.2** | 18.9k | 🚀 +141 | 0 | today | `structured` |
| 13 | [Semantic Kernel](https://github.com/microsoft/semantic-kernel) | 🟡 **53.7** | 28.4k | 📈 +40 | 19 | 22 days ago | `enterprise` |
| 14 | [AG2](https://github.com/ag2ai/ag2) | 🟡 **50.4** | 4.8k | 📈 +26 | 0 | 1 day ago | `multi-agent` |
| 15 | [DSPy](https://github.com/stanfordnlp/dspy) | 🟡 **47.6** | 36.5k | 🚀 +144 | 0 | 2 mo ago | `optimization` |
| 16 | [Letta](https://github.com/letta-ai/letta) | 🟡 **41.7** | 24.0k | 📈 +97 | 0 | 2 mo ago | `memory` |
| 17 | [Smolagents](https://github.com/huggingface/smolagents) | 🟠 **39.4** | 28.6k | 📈 +90 | 4 | 2 mo ago | `lightweight` |
| 18 | [AutoGen](https://github.com/microsoft/autogen) | 🟠 **36.4** | 60.1k | 🚀 +185 | 0 | 10 mo ago | `multi-agent` |
| 19 | [Swarm](https://github.com/openai/swarm) | 🔴 **9.3** | 21.9k | ↗️ +8 | 0 | — | `experimental` |

## 📂 By Category

- `data-agent`: **LlamaIndex** (60.6)
- `enterprise`: **Semantic Kernel** (53.7)
- `experimental`: **Swarm** (9.3)
- `lightweight`: **Smolagents** (39.4)
- `memory`: **Letta** (41.7)
- `multi-agent`: **CrewAI** (80.3), **Agno** (73.0), **AG2** (50.4), **AutoGen** (36.4)
- `optimization`: **DSPy** (47.6)
- `orchestration`: **OpenAI Agents SDK** (76.1), **Google ADK** (73.3), **LangGraph** (71.7), **Claude Agent SDK** (68.9)
- `pipeline`: **Haystack** (70.3)
- `structured`: **PydanticAI** (55.2)
- `tooling`: **Composio** (67.8)
- `typescript`: **Mastra** (80.0)
- `web-agent`: **BrowserUse** (85.0)

## 🔍 Top 5 — Score Breakdown

| Framework | Star Velocity | Release Freshness | Issue Health | Commit Activity | Community | Fork Ratio |
|-----------|:---:|:---:|:---:|:---:|:---:|:---:|
| **BrowserUse** | 100 | 99.3 | 94.6 | 76.0 | 63.0 | 44.0 |
| **CrewAI** | 78.0 | 100.0 | 95.8 | 74.0 | 59.6 | 56.9 |
| **Mastra** | 51.9 | 99.7 | 93.6 | 100 | 93.0 | 37.9 |
| **OpenAI Agents SDK** | 35.6 | 99.7 | 98.2 | 100 | 62.8 | 62.2 |
| **Google ADK** | 22.5 | 97.3 | 88.1 | 100 | 77.8 | 72.0 |

## 💡 Key Insights

- **Hottest framework**: BrowserUse with a Pulse Score of 85.0
- **Fastest growing**: BrowserUse gained +1062 stars this week
- **Most active development**: Mastra with 1106 commits in the last 4 weeks
- **Stale releases**: AutoGen, Swarm haven't released in a while

## 📦 Recent Releases

- **CrewAI** [`1.15.9`](https://github.com/crewAIInc/crewAI/releases/tag/1.15.9) — today
- **PydanticAI** [`v2.21.0`](https://github.com/pydantic/pydantic-ai/releases/tag/v2.21.0) — today
- **Mastra** [`@mastra/core@1.53.0`](https://github.com/mastra-ai/mastra/releases/tag/@mastra/core@1.53.0) — 1 day ago
- **OpenAI Agents SDK** [`v0.19.1`](https://github.com/openai/openai-agents-python/releases/tag/v0.19.1) — 1 day ago
- **AG2** [`v1.0.1`](https://github.com/ag2ai/ag2/releases/tag/v1.0.1) — 1 day ago
- **LangGraph** [`1.2.10`](https://github.com/langchain-ai/langgraph/releases/tag/1.2.10) — 1 day ago
- **BrowserUse** [`0.13.7`](https://github.com/browser-use/browser-use/releases/tag/0.13.7) — 2 days ago
- **Agno** [`v2.8.5`](https://github.com/agno-agi/agno/releases/tag/v2.8.5) — 2 days ago
- **Claude Agent SDK** [`v2.1.220`](https://github.com/anthropics/claude-code/releases/tag/v2.1.220) — 5 days ago
- **Google ADK** [`v1.36.2`](https://github.com/google/adk-python/releases/tag/v1.36.2) — 8 days ago

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

*Powered by GitHub Actions • Data refreshed daily • Last run: 2026-07-30 08:35 UTC*