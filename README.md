# 🔬 AI Agent Framework Pulse Tracker

[![Daily Update](https://github.com/PurpleHaze2320/ai-agent-pulse/actions/workflows/track.yml/badge.svg)](https://github.com/PurpleHaze2320/ai-agent-pulse/actions/workflows/track.yml)
[![Frameworks Tracked](https://img.shields.io/badge/frameworks-19-blue)](https://github.com/PurpleHaze2320/ai-agent-pulse)
[![License: MIT](https://img.shields.io/badge/License-MIT-green.svg)](https://opensource.org/licenses/MIT)
[![GitHub stars](https://img.shields.io/github/stars/PurpleHaze2320/ai-agent-pulse?style=social)](https://github.com/PurpleHaze2320/ai-agent-pulse/stargazers)

> Automated daily tracking of the AI agent framework ecosystem's health, momentum, and trends.
> Last updated: **2026-10-02 12:12 UTC** | Tracking **19** frameworks

## How It Works

This bot runs daily via GitHub Actions and collects metrics from the GitHub API for the most important
AI agent frameworks. It computes a **Pulse Score** (0-100) based on six weighted signals: star velocity,
release freshness, issue health, commit activity, community size, and fork engagement. The result is
a living dashboard that shows which frameworks are gaining momentum and which are losing steam.

## 🏆 Pulse Leaderboard

| Rank | Framework | Pulse | Stars | ⭐ 7d | Commits (4w) | Last Release | Category |
|------|-----------|-------|-------|-------|--------------|--------------|----------|
| 1 | [Claude Agent SDK](https://github.com/anthropics/claude-code) | 🟢 **85.8** | 148.9k | 🚀 +909 | 140 | today | `orchestration` |
| 2 | [BrowserUse](https://github.com/browser-use/browser-use) | 🟢 **81.1** | 117.0k | 🚀 +753 | 64 | 28 days ago | `web-agent` |
| 3 | [CrewAI](https://github.com/crewAIInc/crewAI) | 🟢 **80.3** | 59.3k | 🚀 +279 | 98 | 3 days ago | `multi-agent` |
| 4 | [Mastra](https://github.com/mastra-ai/mastra) | 🟢 **76.8** | 28.5k | 🚀 +172 | 2087 | 2 days ago | `typescript` |
| 5 | [OpenAI Agents SDK](https://github.com/openai/openai-agents-python) | 🟢 **75.6** | 29.8k | 🚀 +107 | 241 | today | `orchestration` |
| 6 | [PydanticAI](https://github.com/pydantic/pydantic-ai) | 🟢 **75.4** | 20.4k | 🚀 +189 | 645 | today | `structured` |
| 7 | [Google ADK](https://github.com/google/adk-python) | 🟢 **72.7** | 21.7k | 📈 +52 | 402 | today | `orchestration` |
| 8 | [LangGraph](https://github.com/langchain-ai/langgraph) | 🟢 **70.4** | 42.6k | 🚀 +350 | 51 | 8 days ago | `orchestration` |
| 9 | [Composio](https://github.com/ComposioHQ/composio) | 🟡 **67.2** | 30.4k | 📈 +85 | 332 | today | `tooling` |
| 10 | [AG2](https://github.com/ag2ai/ag2) | 🟡 **64.2** | 5.0k | ↗️ +17 | 72 | 2 days ago | `multi-agent` |
| 11 | [DSPy](https://github.com/stanfordnlp/dspy) | 🟡 **64.1** | 38.5k | 🚀 +197 | 56 | 7 days ago | `optimization` |
| 12 | [LlamaIndex](https://github.com/run-llama/llama_index) | 🟡 **58.7** | 52.4k | 📈 +72 | 25 | 10 days ago | `data-agent` |
| 13 | [Agno](https://github.com/agno-agi/agno) | 🟡 **52.8** | 42.5k | 🚀 +160 | 0 | 1 day ago | `multi-agent` |
| 14 | [Semantic Kernel](https://github.com/microsoft/semantic-kernel) | 🟡 **51.2** | 28.6k | ↗️ +20 | 13 | 28 days ago | `enterprise` |
| 15 | [Haystack](https://github.com/deepset-ai/haystack) | 🟡 **50.9** | 26.6k | 📈 +46 | 0 | 1 day ago | `pipeline` |
| 16 | [Letta](https://github.com/letta-ai/letta) | 🟠 **39.2** | 25.0k | 🚀 +128 | 2 | 4 mo ago | `memory` |
| 17 | [Smolagents](https://github.com/huggingface/smolagents) | 🟠 **37.4** | 29.6k | 🚀 +162 | 4 | 4 mo ago | `lightweight` |
| 18 | [AutoGen](https://github.com/microsoft/autogen) | 🟠 **32.6** | 61.3k | 🚀 +102 | 0 | 1y ago | `multi-agent` |
| 19 | [Swarm](https://github.com/openai/swarm) | 🔴 **9.6** | 22.0k | 📈 +23 | 0 | — | `experimental` |

## 📂 By Category

- `data-agent`: **LlamaIndex** (58.7)
- `enterprise`: **Semantic Kernel** (51.2)
- `experimental`: **Swarm** (9.6)
- `lightweight`: **Smolagents** (37.4)
- `memory`: **Letta** (39.2)
- `multi-agent`: **CrewAI** (80.3), **AG2** (64.2), **Agno** (52.8), **AutoGen** (32.6)
- `optimization`: **DSPy** (64.1)
- `orchestration`: **Claude Agent SDK** (85.8), **OpenAI Agents SDK** (75.6), **Google ADK** (72.7), **LangGraph** (70.4)
- `pipeline`: **Haystack** (50.9)
- `structured`: **PydanticAI** (75.4)
- `tooling`: **Composio** (67.2)
- `typescript`: **Mastra** (76.8)
- `web-agent`: **BrowserUse** (81.1)

## 🔍 Top 5 — Score Breakdown

| Framework | Star Velocity | Release Freshness | Issue Health | Commit Activity | Community | Fork Ratio |
|-----------|:---:|:---:|:---:|:---:|:---:|:---:|
| **Claude Agent SDK** | 100 | 100.0 | 86.2 | 100 | 11.4 | 67.6 |
| **BrowserUse** | 100 | 90.7 | 90.4 | 64.0 | 72.0 | 44.1 |
| **CrewAI** | 58.5 | 99.0 | 91.4 | 98.0 | 67.2 | 58.2 |
| **Mastra** | 37.0 | 99.3 | 95.3 | 100 | 93.4 | 40.8 |
| **OpenAI Agents SDK** | 24.9 | 100.0 | 99.8 | 100 | 79.2 | 65.0 |

## 💡 Key Insights

- **Hottest framework**: Claude Agent SDK with a Pulse Score of 85.8
- **Fastest growing**: Claude Agent SDK gained +909 stars this week
- **Most active development**: Mastra with 2087 commits in the last 4 weeks
- **Stale releases**: AutoGen, Swarm haven't released in a while

## 📦 Recent Releases

- **PydanticAI** [`v2.53.0`](https://github.com/pydantic/pydantic-ai/releases/tag/v2.53.0) — today
- **OpenAI Agents SDK** [`v0.23.0`](https://github.com/openai/openai-agents-python/releases/tag/v0.23.0) — today
- **Google ADK** [`v2.11.0`](https://github.com/google/adk-python/releases/tag/v2.11.0) — today
- **Claude Agent SDK** [`v2.1.287`](https://github.com/anthropics/claude-code/releases/tag/v2.1.287) — today
- **Composio** [`@composio/cli@0.4.3-beta.411`](https://github.com/ComposioHQ/composio/releases/tag/@composio/cli@0.4.3-beta.411) — today *(pre-release)*
- **Haystack** [`v3.3.0`](https://github.com/deepset-ai/haystack/releases/tag/v3.3.0) — 1 day ago
- **Agno** [`v3.1.0`](https://github.com/agno-agi/agno/releases/tag/v3.1.0) — 1 day ago
- **Mastra** [`@mastra/core@1.72.0`](https://github.com/mastra-ai/mastra/releases/tag/@mastra/core@1.72.0) — 2 days ago
- **AG2** [`v1.1.1`](https://github.com/ag2ai/ag2/releases/tag/v1.1.1) — 2 days ago
- **CrewAI** [`1.15.23`](https://github.com/crewAIInc/crewAI/releases/tag/1.15.23) — 3 days ago

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

*Powered by GitHub Actions • Data refreshed daily • Last run: 2026-10-02 12:12 UTC*