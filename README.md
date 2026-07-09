# 🔬 AI Agent Framework Pulse Tracker

[![Daily Update](https://github.com/PurpleHaze2320/ai-agent-pulse/actions/workflows/track.yml/badge.svg)](https://github.com/PurpleHaze2320/ai-agent-pulse/actions/workflows/track.yml)
[![Frameworks Tracked](https://img.shields.io/badge/frameworks-19-blue)](https://github.com/PurpleHaze2320/ai-agent-pulse)
[![License: MIT](https://img.shields.io/badge/License-MIT-green.svg)](https://opensource.org/licenses/MIT)
[![GitHub stars](https://img.shields.io/github/stars/PurpleHaze2320/ai-agent-pulse?style=social)](https://github.com/PurpleHaze2320/ai-agent-pulse/stargazers)

> Automated daily tracking of the AI agent framework ecosystem's health, momentum, and trends.
> Last updated: **2026-07-09 09:49 UTC** | Tracking **19** frameworks

## How It Works

This bot runs daily via GitHub Actions and collects metrics from the GitHub API for the most important
AI agent frameworks. It computes a **Pulse Score** (0-100) based on six weighted signals: star velocity,
release freshness, issue health, commit activity, community size, and fork engagement. The result is
a living dashboard that shows which frameworks are gaining momentum and which are losing steam.

## 🏆 Pulse Leaderboard

| Rank | Framework | Pulse | Stars | ⭐ 7d | Commits (4w) | Last Release | Category |
|------|-----------|-------|-------|-------|--------------|--------------|----------|
| 1 | [CrewAI](https://github.com/crewAIInc/crewAI) | 🟢 **89.6** | 55.2k | 🚀 +455 | 103 | 1 day ago | `multi-agent` |
| 2 | [BrowserUse](https://github.com/browser-use/browser-use) | 🟢 **82.7** | 103.9k | 🚀 +1754 | 66 | 7 days ago | `web-agent` |
| 3 | [Mastra](https://github.com/mastra-ai/mastra) | 🟢 **80.8** | 26.0k | 🚀 +272 | 995 | today | `typescript` |
| 4 | [LangGraph](https://github.com/langchain-ai/langgraph) | 🟢 **77.6** | 36.9k | 🚀 +586 | 48 | 2 days ago | `orchestration` |
| 5 | [Agno](https://github.com/agno-agi/agno) | 🟢 **71.8** | 41.1k | 🚀 +106 | 106 | today | `multi-agent` |
| 6 | [Claude Agent SDK](https://github.com/anthropics/claude-code) | 🟢 **71.0** | 137.0k | 🚀 +1570 | 28 | today | `orchestration` |
| 7 | [OpenAI Agents SDK](https://github.com/openai/openai-agents-python) | 🟢 **70.4** | 27.8k | 🚀 +170 | 75 | 2 days ago | `orchestration` |
| 8 | [LlamaIndex](https://github.com/run-llama/llama_index) | 🟡 **62.8** | 50.7k | 🚀 +161 | 26 | 14 days ago | `data-agent` |
| 9 | [Semantic Kernel](https://github.com/microsoft/semantic-kernel) | 🟡 **59.2** | 28.3k | 📈 +50 | 38 | 2 days ago | `enterprise` |
| 10 | [PydanticAI](https://github.com/pydantic/pydantic-ai) | 🟡 **54.9** | 18.3k | 🚀 +146 | 0 | today | `structured` |
| 11 | [Google ADK](https://github.com/google/adk-python) | 🟡 **53.7** | 20.5k | 🚀 +134 | 0 | 1 day ago | `orchestration` |
| 12 | [DSPy](https://github.com/stanfordnlp/dspy) | 🟡 **53.1** | 36.0k | 🚀 +240 | 0 | 1 mo ago | `optimization` |
| 13 | [AG2](https://github.com/ag2ai/ag2) | 🟡 **50.0** | 4.8k | 📈 +24 | 0 | 5 days ago | `multi-agent` |
| 14 | [Haystack](https://github.com/deepset-ai/haystack) | 🟡 **49.8** | 25.9k | 📈 +47 | 0 | today | `pipeline` |
| 15 | [Composio](https://github.com/ComposioHQ/composio) | 🟡 **46.5** | 29.1k | 📈 +80 | 0 | 1 day ago | `tooling` |
| 16 | [Letta](https://github.com/letta-ai/letta) | 🟡 **43.5** | 23.7k | 📈 +93 | 2 | 1 mo ago | `memory` |
| 17 | [Smolagents](https://github.com/huggingface/smolagents) | 🟡 **41.1** | 28.3k | 🚀 +112 | 1 | 1 mo ago | `lightweight` |
| 18 | [AutoGen](https://github.com/microsoft/autogen) | 🟠 **37.7** | 59.6k | 🚀 +179 | 0 | 9 mo ago | `multi-agent` |
| 19 | [Swarm](https://github.com/openai/swarm) | 🔴 **9.1** | 21.8k | ↗️ +20 | 0 | — | `experimental` |

## 📂 By Category

- `data-agent`: **LlamaIndex** (62.8)
- `enterprise`: **Semantic Kernel** (59.2)
- `experimental`: **Swarm** (9.1)
- `lightweight`: **Smolagents** (41.1)
- `memory`: **Letta** (43.5)
- `multi-agent`: **CrewAI** (89.6), **Agno** (71.8), **AG2** (50.0), **AutoGen** (37.7)
- `optimization`: **DSPy** (53.1)
- `orchestration`: **LangGraph** (77.6), **Claude Agent SDK** (71.0), **OpenAI Agents SDK** (70.4), **Google ADK** (53.7)
- `pipeline`: **Haystack** (49.8)
- `structured`: **PydanticAI** (54.9)
- `tooling`: **Composio** (46.5)
- `typescript`: **Mastra** (80.8)
- `web-agent`: **BrowserUse** (82.7)

## 🔍 Top 5 — Score Breakdown

| Framework | Star Velocity | Release Freshness | Issue Health | Commit Activity | Community | Fork Ratio |
|-----------|:---:|:---:|:---:|:---:|:---:|:---:|
| **CrewAI** | 94.9 | 99.7 | 95.6 | 100 | 59.6 | 56.3 |
| **BrowserUse** | 100 | 97.7 | 94.9 | 66.0 | 63.0 | 44.2 |
| **Mastra** | 54.3 | 100.0 | 95.5 | 100 | 92.4 | 36.7 |
| **LangGraph** | 100 | 99.3 | 73.1 | 48.0 | 55.0 | 67.2 |
| **Agno** | 21.7 | 100.0 | 80.0 | 100 | 88.8 | 54.7 |

## 💡 Key Insights

- **Hottest framework**: CrewAI with a Pulse Score of 89.6
- **Fastest growing**: BrowserUse gained +1754 stars this week
- **Most active development**: Mastra with 995 commits in the last 4 weeks
- **Stale releases**: AutoGen, Swarm haven't released in a while

## 📦 Recent Releases

- **Agno** [`v2.7.2a4`](https://github.com/agno-agi/agno/releases/tag/v2.7.2a4) — today *(pre-release)*
- **PydanticAI** [`v2.7.0`](https://github.com/pydantic/pydantic-ai/releases/tag/v2.7.0) — today
- **Claude Agent SDK** [`v2.1.205`](https://github.com/anthropics/claude-code/releases/tag/v2.1.205) — today
- **Mastra** [`@mastra/core@1.50.0`](https://github.com/mastra-ai/mastra/releases/tag/@mastra/core@1.50.0) — today
- **Haystack** [`v2.31.0`](https://github.com/deepset-ai/haystack/releases/tag/v2.31.0) — today
- **CrewAI** [`1.15.2`](https://github.com/crewAIInc/crewAI/releases/tag/1.15.2) — 1 day ago
- **Google ADK** [`v2.4.0`](https://github.com/google/adk-python/releases/tag/v2.4.0) — 1 day ago
- **Composio** [`@composio/cli@0.2.32-beta.286`](https://github.com/ComposioHQ/composio/releases/tag/@composio/cli@0.2.32-beta.286) — 1 day ago *(pre-release)*
- **Semantic Kernel** [`python-1.44.0`](https://github.com/microsoft/semantic-kernel/releases/tag/python-1.44.0) — 2 days ago
- **OpenAI Agents SDK** [`v0.18.0`](https://github.com/openai/openai-agents-python/releases/tag/v0.18.0) — 2 days ago

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

*Powered by GitHub Actions • Data refreshed daily • Last run: 2026-07-09 09:49 UTC*