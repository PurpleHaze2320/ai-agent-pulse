# 🔬 AI Agent Framework Pulse Tracker

[![Daily Update](https://github.com/PurpleHaze2320/ai-agent-pulse/actions/workflows/track.yml/badge.svg)](https://github.com/PurpleHaze2320/ai-agent-pulse/actions/workflows/track.yml)
[![Frameworks Tracked](https://img.shields.io/badge/frameworks-19-blue)](https://github.com/PurpleHaze2320/ai-agent-pulse)
[![License: MIT](https://img.shields.io/badge/License-MIT-green.svg)](https://opensource.org/licenses/MIT)
[![GitHub stars](https://img.shields.io/github/stars/PurpleHaze2320/ai-agent-pulse?style=social)](https://github.com/PurpleHaze2320/ai-agent-pulse/stargazers)

> Automated daily tracking of the AI agent framework ecosystem's health, momentum, and trends.
> Last updated: **2026-11-07 12:44 UTC** | Tracking **19** frameworks

## How It Works

This bot runs daily via GitHub Actions and collects metrics from the GitHub API for the most important
AI agent frameworks. It computes a **Pulse Score** (0-100) based on six weighted signals: star velocity,
release freshness, issue health, commit activity, community size, and fork engagement. The result is
a living dashboard that shows which frameworks are gaining momentum and which are losing steam.

## 🏆 Pulse Leaderboard

| Rank | Framework | Pulse | Stars | ⭐ 7d | Commits (4w) | Last Release | Category |
|------|-----------|-------|-------|-------|--------------|--------------|----------|
| 1 | [BrowserUse](https://github.com/browser-use/browser-use) | 🟢 **89.4** | 120.2k | 🚀 +611 | 107 | 11 days ago | `web-agent` |
| 2 | [LangGraph](https://github.com/langchain-ai/langgraph) | 🟢 **85.2** | 44.6k | 🚀 +402 | 131 | 1 day ago | `orchestration` |
| 3 | [CrewAI](https://github.com/crewAIInc/crewAI) | 🟢 **79.5** | 60.6k | 🚀 +270 | 199 | today | `multi-agent` |
| 4 | [Mastra](https://github.com/mastra-ai/mastra) | 🟢 **76.1** | 29.4k | 🚀 +168 | 2413 | 3 days ago | `typescript` |
| 5 | [Claude Agent SDK](https://github.com/anthropics/claude-code) | 🟢 **74.8** | 154.9k | 🚀 +843 | 47 | today | `orchestration` |
| 6 | [Google ADK](https://github.com/google/adk-python) | 🟢 **74.7** | 22.1k | 📈 +76 | 512 | today | `orchestration` |
| 7 | [OpenAI Agents SDK](https://github.com/openai/openai-agents-python) | 🟢 **71.9** | 30.5k | 🚀 +138 | 78 | 3 days ago | `orchestration` |
| 8 | [Haystack](https://github.com/deepset-ai/haystack) | 🟢 **71.1** | 26.9k | 📈 +48 | 251 | 4 days ago | `pipeline` |
| 9 | [PydanticAI](https://github.com/pydantic/pydantic-ai) | 🟢 **70.2** | 21.1k | 🚀 +105 | 1269 | 1 mo ago | `structured` |
| 10 | [AG2](https://github.com/ag2ai/ag2) | 🟢 **70.0** | 5.0k | ↗️ +15 | 128 | 3 days ago | `multi-agent` |
| 11 | [Agno](https://github.com/agno-agi/agno) | 🟡 **69.9** | 43.1k | 📈 +98 | 163 | 8 days ago | `multi-agent` |
| 12 | [Semantic Kernel](https://github.com/microsoft/semantic-kernel) | 🟡 **69.5** | 28.7k | ↗️ +19 | 90 | today | `enterprise` |
| 13 | [Composio](https://github.com/ComposioHQ/composio) | 🟡 **68.4** | 31.0k | 🚀 +118 | 397 | 1 day ago | `tooling` |
| 14 | [DSPy](https://github.com/stanfordnlp/dspy) | 🟡 **64.3** | 39.0k | 🚀 +101 | 85 | 25 days ago | `optimization` |
| 15 | [LlamaIndex](https://github.com/run-llama/llama_index) | 🟡 **52.9** | 52.8k | 📈 +80 | 7 | 1 mo ago | `data-agent` |
| 16 | [Letta](https://github.com/letta-ai/letta) | 🟠 **34.1** | 25.4k | 📈 +72 | 1 | 5 mo ago | `memory` |
| 17 | [AutoGen](https://github.com/microsoft/autogen) | 🟠 **32.5** | 61.7k | 📈 +94 | 2 | 1y ago | `multi-agent` |
| 18 | [Smolagents](https://github.com/huggingface/smolagents) | 🟠 **31.3** | 30.2k | 📈 +96 | 0 | 5 mo ago | `lightweight` |
| 19 | [Swarm](https://github.com/openai/swarm) | 🔴 **9.4** | 22.1k | 📈 +21 | 0 | — | `experimental` |

## 📂 By Category

- `data-agent`: **LlamaIndex** (52.9)
- `enterprise`: **Semantic Kernel** (69.5)
- `experimental`: **Swarm** (9.4)
- `lightweight`: **Smolagents** (31.3)
- `memory`: **Letta** (34.1)
- `multi-agent`: **CrewAI** (79.5), **AG2** (70.0), **Agno** (69.9), **AutoGen** (32.5)
- `optimization`: **DSPy** (64.3)
- `orchestration`: **LangGraph** (85.2), **Claude Agent SDK** (74.8), **Google ADK** (74.7), **OpenAI Agents SDK** (71.9)
- `pipeline`: **Haystack** (71.1)
- `structured`: **PydanticAI** (70.2)
- `tooling`: **Composio** (68.4)
- `typescript`: **Mastra** (76.1)
- `web-agent`: **BrowserUse** (89.4)

## 🔍 Top 5 — Score Breakdown

| Framework | Star Velocity | Release Freshness | Issue Health | Commit Activity | Community | Fork Ratio |
|-----------|:---:|:---:|:---:|:---:|:---:|:---:|
| **BrowserUse** | 100 | 96.3 | 89.6 | 100 | 72.2 | 44.6 |
| **LangGraph** | 82.1 | 99.7 | 80.9 | 100 | 57.4 | 68.9 |
| **CrewAI** | 55.1 | 100.0 | 83.2 | 100 | 72.6 | 60.0 |
| **Mastra** | 34.9 | 99.0 | 93.9 | 100 | 93.2 | 41.9 |
| **Claude Agent SDK** | 100 | 100.0 | 84.6 | 47.0 | 11.2 | 66.1 |

## 💡 Key Insights

- **Hottest framework**: BrowserUse with a Pulse Score of 89.4
- **Fastest growing**: Claude Agent SDK gained +843 stars this week
- **Most active development**: Mastra with 2413 commits in the last 4 weeks
- **Stale releases**: AutoGen, Swarm haven't released in a while

## 📦 Recent Releases

- **CrewAI** [`1.15.37`](https://github.com/crewAIInc/crewAI/releases/tag/1.15.37) — today
- **Semantic Kernel** [`dotnet-1.82.0`](https://github.com/microsoft/semantic-kernel/releases/tag/dotnet-1.82.0) — today
- **Google ADK** [`v2.14.0`](https://github.com/google/adk-python/releases/tag/v2.14.0) — today
- **Claude Agent SDK** [`v2.1.319`](https://github.com/anthropics/claude-code/releases/tag/v2.1.319) — today
- **Composio** [`@composio/cli@0.6.1-beta.535`](https://github.com/ComposioHQ/composio/releases/tag/@composio/cli@0.6.1-beta.535) — 1 day ago *(pre-release)*
- **LangGraph** [`sdk==0.4.14`](https://github.com/langchain-ai/langgraph/releases/tag/sdk==0.4.14) — 1 day ago
- **Mastra** [`@mastra/core@1.82.0`](https://github.com/mastra-ai/mastra/releases/tag/@mastra/core@1.82.0) — 3 days ago
- **AG2** [`v1.3.0`](https://github.com/ag2ai/ag2/releases/tag/v1.3.0) — 3 days ago
- **OpenAI Agents SDK** [`v0.24.0-alpha.6`](https://github.com/openai/openai-agents-python/releases/tag/v0.24.0-alpha.6) — 3 days ago *(pre-release)*
- **Haystack** [`v2.31.1`](https://github.com/deepset-ai/haystack/releases/tag/v2.31.1) — 4 days ago

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

*Powered by GitHub Actions • Data refreshed daily • Last run: 2026-11-07 12:44 UTC*