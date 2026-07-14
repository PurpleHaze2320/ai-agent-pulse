# 🔬 AI Agent Framework Pulse Tracker

[![Daily Update](https://github.com/PurpleHaze2320/ai-agent-pulse/actions/workflows/track.yml/badge.svg)](https://github.com/PurpleHaze2320/ai-agent-pulse/actions/workflows/track.yml)
[![Frameworks Tracked](https://img.shields.io/badge/frameworks-19-blue)](https://github.com/PurpleHaze2320/ai-agent-pulse)
[![License: MIT](https://img.shields.io/badge/License-MIT-green.svg)](https://opensource.org/licenses/MIT)
[![GitHub stars](https://img.shields.io/github/stars/PurpleHaze2320/ai-agent-pulse?style=social)](https://github.com/PurpleHaze2320/ai-agent-pulse/stargazers)

> Automated daily tracking of the AI agent framework ecosystem's health, momentum, and trends.
> Last updated: **2026-07-14 08:17 UTC** | Tracking **19** frameworks

## How It Works

This bot runs daily via GitHub Actions and collects metrics from the GitHub API for the most important
AI agent frameworks. It computes a **Pulse Score** (0-100) based on six weighted signals: star velocity,
release freshness, issue health, commit activity, community size, and fork engagement. The result is
a living dashboard that shows which frameworks are gaining momentum and which are losing steam.

## 🏆 Pulse Leaderboard

| Rank | Framework | Pulse | Stars | ⭐ 7d | Commits (4w) | Last Release | Category |
|------|-----------|-------|-------|-------|--------------|--------------|----------|
| 1 | [CrewAI](https://github.com/crewAIInc/crewAI) | 🟢 **84.0** | 55.5k | 🚀 +424 | 81 | 6 days ago | `multi-agent` |
| 2 | [BrowserUse](https://github.com/browser-use/browser-use) | 🟢 **84.0** | 104.7k | 🚀 +1415 | 71 | 2 days ago | `web-agent` |
| 3 | [Mastra](https://github.com/mastra-ai/mastra) | 🟢 **80.1** | 26.1k | 🚀 +259 | 983 | 5 days ago | `typescript` |
| 4 | [PydanticAI](https://github.com/pydantic/pydantic-ai) | 🟢 **79.0** | 18.5k | 🚀 +250 | 217 | today | `structured` |
| 5 | [OpenAI Agents SDK](https://github.com/openai/openai-agents-python) | 🟢 **76.3** | 27.9k | 🚀 +191 | 108 | 3 days ago | `orchestration` |
| 6 | [LangGraph](https://github.com/langchain-ai/langgraph) | 🟢 **74.9** | 37.3k | 🚀 +575 | 35 | 4 days ago | `orchestration` |
| 7 | [Google ADK](https://github.com/google/adk-python) | 🟢 **72.2** | 20.6k | 📈 +91 | 291 | 6 days ago | `orchestration` |
| 8 | [Claude Agent SDK](https://github.com/anthropics/claude-code) | 🟡 **69.9** | 137.8k | 🚀 +1147 | 23 | today | `orchestration` |
| 9 | [Composio](https://github.com/ComposioHQ/composio) | 🟡 **67.5** | 29.2k | 🚀 +106 | 126 | today | `tooling` |
| 10 | [LlamaIndex](https://github.com/run-llama/llama_index) | 🟡 **56.1** | 50.8k | 🚀 +129 | 0 | 19 days ago | `data-agent` |
| 11 | [DSPy](https://github.com/stanfordnlp/dspy) | 🟡 **55.6** | 36.1k | 🚀 +209 | 18 | 1 mo ago | `optimization` |
| 12 | [Agno](https://github.com/agno-agi/agno) | 🟡 **52.5** | 41.2k | 🚀 +129 | 0 | 4 days ago | `multi-agent` |
| 13 | [Semantic Kernel](https://github.com/microsoft/semantic-kernel) | 🟡 **50.6** | 28.3k | 📈 +31 | 0 | 6 days ago | `enterprise` |
| 14 | [Haystack](https://github.com/deepset-ai/haystack) | 🟡 **49.6** | 25.9k | 📈 +50 | 0 | 5 days ago | `pipeline` |
| 15 | [AG2](https://github.com/ag2ai/ag2) | 🟡 **49.5** | 4.8k | ↗️ +20 | 0 | 10 days ago | `multi-agent` |
| 16 | [Letta](https://github.com/letta-ai/letta) | 🟡 **42.7** | 23.8k | 📈 +93 | 0 | 2 mo ago | `memory` |
| 17 | [Smolagents](https://github.com/huggingface/smolagents) | 🟡 **41.3** | 28.3k | 🚀 +110 | 4 | 1 mo ago | `lightweight` |
| 18 | [AutoGen](https://github.com/microsoft/autogen) | 🟠 **36.9** | 59.7k | 🚀 +170 | 0 | 9 mo ago | `multi-agent` |
| 19 | [Swarm](https://github.com/openai/swarm) | 🔴 **9.2** | 21.8k | 📈 +25 | 0 | — | `experimental` |

## 📂 By Category

- `data-agent`: **LlamaIndex** (56.1)
- `enterprise`: **Semantic Kernel** (50.6)
- `experimental`: **Swarm** (9.2)
- `lightweight`: **Smolagents** (41.3)
- `memory`: **Letta** (42.7)
- `multi-agent`: **CrewAI** (84.0), **Agno** (52.5), **AG2** (49.5), **AutoGen** (36.9)
- `optimization`: **DSPy** (55.6)
- `orchestration`: **OpenAI Agents SDK** (76.3), **LangGraph** (74.9), **Google ADK** (72.2), **Claude Agent SDK** (69.9)
- `pipeline`: **Haystack** (49.6)
- `structured`: **PydanticAI** (79.0)
- `tooling`: **Composio** (67.5)
- `typescript`: **Mastra** (80.1)
- `web-agent`: **BrowserUse** (84.0)

## 🔍 Top 5 — Score Breakdown

| Framework | Star Velocity | Release Freshness | Issue Health | Commit Activity | Community | Fork Ratio |
|-----------|:---:|:---:|:---:|:---:|:---:|:---:|
| **CrewAI** | 88.8 | 98.0 | 95.8 | 81.0 | 59.6 | 56.4 |
| **BrowserUse** | 100 | 99.3 | 94.8 | 71.0 | 63.0 | 44.1 |
| **Mastra** | 52.8 | 98.3 | 95.0 | 100 | 92.6 | 36.9 |
| **PydanticAI** | 46.4 | 100.0 | 85.4 | 100 | 94.8 | 51.1 |
| **OpenAI Agents SDK** | 38.1 | 99.0 | 98.1 | 100 | 60.4 | 62.0 |

## 💡 Key Insights

- **Hottest framework**: CrewAI with a Pulse Score of 84.0
- **Fastest growing**: BrowserUse gained +1415 stars this week
- **Most active development**: Mastra with 983 commits in the last 4 weeks
- **Stale releases**: AutoGen, Swarm haven't released in a while

## 📦 Recent Releases

- **Claude Agent SDK** [`v2.1.209`](https://github.com/anthropics/claude-code/releases/tag/v2.1.209) — today
- **PydanticAI** [`v2.9.1`](https://github.com/pydantic/pydantic-ai/releases/tag/v2.9.1) — today
- **Composio** [`@composio/cli@0.2.32-beta.287`](https://github.com/ComposioHQ/composio/releases/tag/@composio/cli@0.2.32-beta.287) — today *(pre-release)*
- **BrowserUse** [`0.13.4`](https://github.com/browser-use/browser-use/releases/tag/0.13.4) — 2 days ago
- **OpenAI Agents SDK** [`v0.18.2`](https://github.com/openai/openai-agents-python/releases/tag/v0.18.2) — 3 days ago
- **LangGraph** [`1.2.9`](https://github.com/langchain-ai/langgraph/releases/tag/1.2.9) — 4 days ago
- **Agno** [`v2.7.2`](https://github.com/agno-agi/agno/releases/tag/v2.7.2) — 4 days ago
- **Mastra** [`@mastra/core@1.50.0`](https://github.com/mastra-ai/mastra/releases/tag/@mastra/core@1.50.0) — 5 days ago
- **Haystack** [`v2.31.0`](https://github.com/deepset-ai/haystack/releases/tag/v2.31.0) — 5 days ago
- **CrewAI** [`1.15.2`](https://github.com/crewAIInc/crewAI/releases/tag/1.15.2) — 6 days ago

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

*Powered by GitHub Actions • Data refreshed daily • Last run: 2026-07-14 08:17 UTC*