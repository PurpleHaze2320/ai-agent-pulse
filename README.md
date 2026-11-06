# 🔬 AI Agent Framework Pulse Tracker

[![Daily Update](https://github.com/PurpleHaze2320/ai-agent-pulse/actions/workflows/track.yml/badge.svg)](https://github.com/PurpleHaze2320/ai-agent-pulse/actions/workflows/track.yml)
[![Frameworks Tracked](https://img.shields.io/badge/frameworks-19-blue)](https://github.com/PurpleHaze2320/ai-agent-pulse)
[![License: MIT](https://img.shields.io/badge/License-MIT-green.svg)](https://opensource.org/licenses/MIT)
[![GitHub stars](https://img.shields.io/github/stars/PurpleHaze2320/ai-agent-pulse?style=social)](https://github.com/PurpleHaze2320/ai-agent-pulse/stargazers)

> Automated daily tracking of the AI agent framework ecosystem's health, momentum, and trends.
> Last updated: **2026-11-06 14:00 UTC** | Tracking **19** frameworks

## How It Works

This bot runs daily via GitHub Actions and collects metrics from the GitHub API for the most important
AI agent frameworks. It computes a **Pulse Score** (0-100) based on six weighted signals: star velocity,
release freshness, issue health, commit activity, community size, and fork engagement. The result is
a living dashboard that shows which frameworks are gaining momentum and which are losing steam.

## 🏆 Pulse Leaderboard

| Rank | Framework | Pulse | Stars | ⭐ 7d | Commits (4w) | Last Release | Category |
|------|-----------|-------|-------|-------|--------------|--------------|----------|
| 1 | [BrowserUse](https://github.com/browser-use/browser-use) | 🟢 **89.5** | 120.2k | 🚀 +632 | 107 | 10 days ago | `web-agent` |
| 2 | [LangGraph](https://github.com/langchain-ai/langgraph) | 🟢 **85.5** | 44.6k | 🚀 +406 | 129 | today | `orchestration` |
| 3 | [CrewAI](https://github.com/crewAIInc/crewAI) | 🟢 **79.5** | 60.6k | 🚀 +270 | 193 | today | `multi-agent` |
| 4 | [Mastra](https://github.com/mastra-ai/mastra) | 🟢 **76.3** | 29.4k | 🚀 +171 | 2379 | 2 days ago | `typescript` |
| 5 | [Claude Agent SDK](https://github.com/anthropics/claude-code) | 🟢 **74.5** | 154.8k | 🚀 +838 | 46 | 2 days ago | `orchestration` |
| 6 | [Google ADK](https://github.com/google/adk-python) | 🟢 **73.8** | 22.1k | 📈 +76 | 497 | 13 days ago | `orchestration` |
| 7 | [OpenAI Agents SDK](https://github.com/openai/openai-agents-python) | 🟢 **71.7** | 30.5k | 🚀 +135 | 77 | 2 days ago | `orchestration` |
| 8 | [Haystack](https://github.com/deepset-ai/haystack) | 🟢 **71.2** | 26.9k | 📈 +49 | 242 | 3 days ago | `pipeline` |
| 9 | [Agno](https://github.com/agno-agi/agno) | 🟢 **70.5** | 43.1k | 🚀 +114 | 163 | 7 days ago | `multi-agent` |
| 10 | [AG2](https://github.com/ag2ai/ag2) | 🟢 **70.1** | 5.0k | ↗️ +15 | 128 | 2 days ago | `multi-agent` |
| 11 | [Semantic Kernel](https://github.com/microsoft/semantic-kernel) | 🟡 **69.4** | 28.7k | ↗️ +18 | 90 | 1 day ago | `enterprise` |
| 12 | [Composio](https://github.com/ComposioHQ/composio) | 🟡 **68.6** | 30.9k | 🚀 +121 | 394 | today | `tooling` |
| 13 | [DSPy](https://github.com/stanfordnlp/dspy) | 🟡 **64.2** | 39.0k | 🚀 +107 | 83 | 24 days ago | `optimization` |
| 14 | [LlamaIndex](https://github.com/run-llama/llama_index) | 🟡 **53.1** | 52.8k | 📈 +86 | 7 | 1 mo ago | `data-agent` |
| 15 | [PydanticAI](https://github.com/pydantic/pydantic-ai) | 🟡 **50.1** | 21.1k | 📈 +99 | 0 | 1 mo ago | `structured` |
| 16 | [Letta](https://github.com/letta-ai/letta) | 🟠 **34.3** | 25.4k | 📈 +75 | 1 | 5 mo ago | `memory` |
| 17 | [AutoGen](https://github.com/microsoft/autogen) | 🟠 **32.9** | 61.7k | 🚀 +103 | 2 | 1y ago | `multi-agent` |
| 18 | [Smolagents](https://github.com/huggingface/smolagents) | 🟠 **31.0** | 30.2k | 📈 +85 | 0 | 5 mo ago | `lightweight` |
| 19 | [Swarm](https://github.com/openai/swarm) | 🔴 **9.5** | 22.1k | 📈 +25 | 0 | — | `experimental` |

## 📂 By Category

- `data-agent`: **LlamaIndex** (53.1)
- `enterprise`: **Semantic Kernel** (69.4)
- `experimental`: **Swarm** (9.5)
- `lightweight`: **Smolagents** (31.0)
- `memory`: **Letta** (34.3)
- `multi-agent`: **CrewAI** (79.5), **Agno** (70.5), **AG2** (70.1), **AutoGen** (32.9)
- `optimization`: **DSPy** (64.2)
- `orchestration`: **LangGraph** (85.5), **Claude Agent SDK** (74.5), **Google ADK** (73.8), **OpenAI Agents SDK** (71.7)
- `pipeline`: **Haystack** (71.2)
- `structured`: **PydanticAI** (50.1)
- `tooling`: **Composio** (68.6)
- `typescript`: **Mastra** (76.3)
- `web-agent`: **BrowserUse** (89.5)

## 🔍 Top 5 — Score Breakdown

| Framework | Star Velocity | Release Freshness | Issue Health | Commit Activity | Community | Fork Ratio |
|-----------|:---:|:---:|:---:|:---:|:---:|:---:|
| **BrowserUse** | 100 | 96.7 | 89.6 | 100 | 72.2 | 44.6 |
| **LangGraph** | 83.0 | 100.0 | 80.9 | 100 | 57.4 | 68.9 |
| **CrewAI** | 55.0 | 100.0 | 83.5 | 100 | 72.6 | 59.9 |
| **Mastra** | 35.4 | 99.3 | 94.0 | 100 | 93.2 | 41.9 |
| **Claude Agent SDK** | 100 | 99.3 | 84.6 | 46.0 | 11.2 | 66.1 |

## 💡 Key Insights

- **Hottest framework**: BrowserUse with a Pulse Score of 89.5
- **Fastest growing**: Claude Agent SDK gained +838 stars this week
- **Most active development**: Mastra with 2379 commits in the last 4 weeks
- **Stale releases**: AutoGen, Swarm haven't released in a while

## 📦 Recent Releases

- **Composio** [`@composio/cli@0.6.1-beta.535`](https://github.com/ComposioHQ/composio/releases/tag/@composio/cli@0.6.1-beta.535) — today *(pre-release)*
- **CrewAI** [`1.15.36`](https://github.com/crewAIInc/crewAI/releases/tag/1.15.36) — today
- **LangGraph** [`sdk==0.4.14`](https://github.com/langchain-ai/langgraph/releases/tag/sdk==0.4.14) — today
- **Semantic Kernel** [`python-1.47.0`](https://github.com/microsoft/semantic-kernel/releases/tag/python-1.47.0) — 1 day ago
- **Mastra** [`@mastra/core@1.82.0`](https://github.com/mastra-ai/mastra/releases/tag/@mastra/core@1.82.0) — 2 days ago
- **AG2** [`v1.3.0`](https://github.com/ag2ai/ag2/releases/tag/v1.3.0) — 2 days ago
- **Claude Agent SDK** [`v2.1.318`](https://github.com/anthropics/claude-code/releases/tag/v2.1.318) — 2 days ago
- **OpenAI Agents SDK** [`v0.24.0-alpha.6`](https://github.com/openai/openai-agents-python/releases/tag/v0.24.0-alpha.6) — 2 days ago *(pre-release)*
- **Haystack** [`v2.31.1`](https://github.com/deepset-ai/haystack/releases/tag/v2.31.1) — 3 days ago
- **Agno** [`v3.1.12`](https://github.com/agno-agi/agno/releases/tag/v3.1.12) — 7 days ago

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

*Powered by GitHub Actions • Data refreshed daily • Last run: 2026-11-06 14:00 UTC*