# 🔬 AI Agent Framework Pulse Tracker

[![Daily Update](https://github.com/PurpleHaze2320/ai-agent-pulse/actions/workflows/track.yml/badge.svg)](https://github.com/PurpleHaze2320/ai-agent-pulse/actions/workflows/track.yml)
[![Frameworks Tracked](https://img.shields.io/badge/frameworks-19-blue)](https://github.com/PurpleHaze2320/ai-agent-pulse)
[![License: MIT](https://img.shields.io/badge/License-MIT-green.svg)](https://opensource.org/licenses/MIT)
[![GitHub stars](https://img.shields.io/github/stars/PurpleHaze2320/ai-agent-pulse?style=social)](https://github.com/PurpleHaze2320/ai-agent-pulse/stargazers)

> Automated daily tracking of the AI agent framework ecosystem's health, momentum, and trends.
> Last updated: **2026-10-31 11:57 UTC** | Tracking **19** frameworks

## How It Works

This bot runs daily via GitHub Actions and collects metrics from the GitHub API for the most important
AI agent frameworks. It computes a **Pulse Score** (0-100) based on six weighted signals: star velocity,
release freshness, issue health, commit activity, community size, and fork engagement. The result is
a living dashboard that shows which frameworks are gaining momentum and which are losing steam.

## 🏆 Pulse Leaderboard

| Rank | Framework | Pulse | Stars | ⭐ 7d | Commits (4w) | Last Release | Category |
|------|-----------|-------|-------|-------|--------------|--------------|----------|
| 1 | [BrowserUse](https://github.com/browser-use/browser-use) | 🟢 **89.8** | 119.6k | 🚀 +617 | 119 | 4 days ago | `web-agent` |
| 2 | [LangGraph](https://github.com/langchain-ai/langgraph) | 🟢 **84.7** | 44.2k | 🚀 +401 | 128 | today | `orchestration` |
| 3 | [CrewAI](https://github.com/crewAIInc/crewAI) | 🟢 **79.8** | 60.3k | 🚀 +282 | 186 | 2 days ago | `multi-agent` |
| 4 | [Mastra](https://github.com/mastra-ai/mastra) | 🟢 **76.7** | 29.2k | 🚀 +180 | 2541 | 2 days ago | `typescript` |
| 5 | [Claude Agent SDK](https://github.com/anthropics/claude-code) | 🟢 **75.7** | 154.0k | 🚀 +797 | 50 | today | `orchestration` |
| 6 | [Google ADK](https://github.com/google/adk-python) | 🟢 **73.8** | 22.1k | 📈 +70 | 534 | 7 days ago | `orchestration` |
| 7 | [OpenAI Agents SDK](https://github.com/openai/openai-agents-python) | 🟢 **73.4** | 30.4k | 🚀 +154 | 87 | 16 days ago | `orchestration` |
| 8 | [PydanticAI](https://github.com/pydantic/pydantic-ai) | 🟢 **72.0** | 21.0k | 🚀 +141 | 1214 | 25 days ago | `structured` |
| 9 | [Haystack](https://github.com/deepset-ai/haystack) | 🟢 **71.5** | 26.9k | 📈 +72 | 235 | 9 days ago | `pipeline` |
| 10 | [Agno](https://github.com/agno-agi/agno) | 🟢 **71.3** | 43.0k | 🚀 +119 | 179 | 1 day ago | `multi-agent` |
| 11 | [AG2](https://github.com/ag2ai/ag2) | 🟢 **70.0** | 5.0k | 📈 +21 | 113 | 3 days ago | `multi-agent` |
| 12 | [Composio](https://github.com/ComposioHQ/composio) | 🟡 **68.6** | 30.8k | 🚀 +124 | 369 | today | `tooling` |
| 13 | [Semantic Kernel](https://github.com/microsoft/semantic-kernel) | 🟡 **65.6** | 28.7k | 📈 +30 | 71 | 2 days ago | `enterprise` |
| 14 | [DSPy](https://github.com/stanfordnlp/dspy) | 🟡 **62.5** | 38.9k | 📈 +100 | 74 | 18 days ago | `optimization` |
| 15 | [LlamaIndex](https://github.com/run-llama/llama_index) | 🟡 **55.1** | 52.8k | 🚀 +122 | 9 | 1 mo ago | `data-agent` |
| 16 | [Letta](https://github.com/letta-ai/letta) | 🟠 **34.3** | 25.3k | 📈 +62 | 1 | 5 mo ago | `memory` |
| 17 | [Smolagents](https://github.com/huggingface/smolagents) | 🟠 **33.3** | 30.2k | 🚀 +131 | 1 | 5 mo ago | `lightweight` |
| 18 | [AutoGen](https://github.com/microsoft/autogen) | 🟠 **32.5** | 61.6k | 📈 +99 | 2 | 1y ago | `multi-agent` |
| 19 | [Swarm](https://github.com/openai/swarm) | 🔴 **9.2** | 22.1k | ↗️ +18 | 0 | — | `experimental` |

## 📂 By Category

- `data-agent`: **LlamaIndex** (55.1)
- `enterprise`: **Semantic Kernel** (65.6)
- `experimental`: **Swarm** (9.2)
- `lightweight`: **Smolagents** (33.3)
- `memory`: **Letta** (34.3)
- `multi-agent`: **CrewAI** (79.8), **Agno** (71.3), **AG2** (70.0), **AutoGen** (32.5)
- `optimization`: **DSPy** (62.5)
- `orchestration`: **LangGraph** (84.7), **Claude Agent SDK** (75.7), **Google ADK** (73.8), **OpenAI Agents SDK** (73.4)
- `pipeline`: **Haystack** (71.5)
- `structured`: **PydanticAI** (72.0)
- `tooling`: **Composio** (68.6)
- `typescript`: **Mastra** (76.7)
- `web-agent`: **BrowserUse** (89.8)

## 🔍 Top 5 — Score Breakdown

| Framework | Star Velocity | Release Freshness | Issue Health | Commit Activity | Community | Fork Ratio |
|-----------|:---:|:---:|:---:|:---:|:---:|:---:|
| **BrowserUse** | 100 | 98.7 | 89.2 | 100 | 72.2 | 44.5 |
| **LangGraph** | 81.0 | 100.0 | 79.0 | 100 | 57.4 | 68.8 |
| **CrewAI** | 55.6 | 99.3 | 85.2 | 100 | 72.6 | 59.6 |
| **Mastra** | 36.6 | 99.3 | 94.5 | 100 | 93.4 | 41.9 |
| **Claude Agent SDK** | 100 | 100.0 | 84.9 | 50.0 | 11.4 | 67.8 |

## 💡 Key Insights

- **Hottest framework**: BrowserUse with a Pulse Score of 89.8
- **Fastest growing**: Claude Agent SDK gained +797 stars this week
- **Most active development**: Mastra with 2541 commits in the last 4 weeks
- **Stale releases**: AutoGen, Swarm haven't released in a while

## 📦 Recent Releases

- **Claude Agent SDK** [`v2.1.316`](https://github.com/anthropics/claude-code/releases/tag/v2.1.316) — today
- **LangGraph** [`1.2.19`](https://github.com/langchain-ai/langgraph/releases/tag/1.2.19) — today
- **Composio** [`@composio/cli@0.5.1-beta.523`](https://github.com/ComposioHQ/composio/releases/tag/@composio/cli@0.5.1-beta.523) — today *(pre-release)*
- **Agno** [`v3.1.12`](https://github.com/agno-agi/agno/releases/tag/v3.1.12) — 1 day ago
- **CrewAI** [`1.15.33`](https://github.com/crewAIInc/crewAI/releases/tag/1.15.33) — 2 days ago
- **Mastra** [`@mastra/core@1.80.0`](https://github.com/mastra-ai/mastra/releases/tag/@mastra/core@1.80.0) — 2 days ago
- **Semantic Kernel** [`python-1.46.0`](https://github.com/microsoft/semantic-kernel/releases/tag/python-1.46.0) — 2 days ago
- **AG2** [`v1.2.2`](https://github.com/ag2ai/ag2/releases/tag/v1.2.2) — 3 days ago
- **BrowserUse** [`0.13.14`](https://github.com/browser-use/browser-use/releases/tag/0.13.14) — 4 days ago
- **Google ADK** [`v2.13.0`](https://github.com/google/adk-python/releases/tag/v2.13.0) — 7 days ago

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

*Powered by GitHub Actions • Data refreshed daily • Last run: 2026-10-31 11:57 UTC*