# 🔬 AI Agent Framework Pulse Tracker

[![Daily Update](https://github.com/PurpleHaze2320/ai-agent-pulse/actions/workflows/track.yml/badge.svg)](https://github.com/PurpleHaze2320/ai-agent-pulse/actions/workflows/track.yml)
[![Frameworks Tracked](https://img.shields.io/badge/frameworks-19-blue)](https://github.com/PurpleHaze2320/ai-agent-pulse)
[![License: MIT](https://img.shields.io/badge/License-MIT-green.svg)](https://opensource.org/licenses/MIT)
[![GitHub stars](https://img.shields.io/github/stars/PurpleHaze2320/ai-agent-pulse?style=social)](https://github.com/PurpleHaze2320/ai-agent-pulse/stargazers)

> Automated daily tracking of the AI agent framework ecosystem's health, momentum, and trends.
> Last updated: **2026-05-15 08:56 UTC** | Tracking **19** frameworks

## How It Works

This bot runs daily via GitHub Actions and collects metrics from the GitHub API for the most important
AI agent frameworks. It computes a **Pulse Score** (0-100) based on six weighted signals: star velocity,
release freshness, issue health, commit activity, community size, and fork engagement. The result is
a living dashboard that shows which frameworks are gaining momentum and which are losing steam.

## 🏆 Pulse Leaderboard

| Rank | Framework | Pulse | Stars | ⭐ 7d | Commits (4w) | Last Release | Category |
|------|-----------|-------|-------|-------|--------------|--------------|----------|
| 1 | [Mastra](https://github.com/mastra-ai/mastra) | 🟢 **78.1** | 23.9k | 🚀 +239 | 1026 | 1 day ago | `typescript` |
| 2 | [CrewAI](https://github.com/crewAIInc/crewAI) | 🟢 **71.1** | 51.4k | 🚀 +565 | 0 | 2 days ago | `multi-agent` |
| 3 | [OpenAI Agents SDK](https://github.com/openai/openai-agents-python) | 🟢 **70.8** | 26.3k | 🚀 +275 | 0 | 3 days ago | `orchestration` |
| 4 | [LangGraph](https://github.com/langchain-ai/langgraph) | 🟡 **68.7** | 32.1k | 🚀 +603 | 0 | 3 days ago | `orchestration` |
| 5 | [BrowserUse](https://github.com/browser-use/browser-use) | 🟡 **67.4** | 94.0k | 🚀 +1172 | 0 | 1 mo ago | `web-agent` |
| 6 | [Claude Agent SDK](https://github.com/anthropics/claude-code) | 🟡 **64.8** | 123.7k | 🚀 +2267 | 0 | today | `orchestration` |
| 7 | [LlamaIndex](https://github.com/run-llama/llama_index) | 🟡 **60.0** | 49.4k | 🚀 +196 | 0 | today | `data-agent` |
| 8 | [PydanticAI](https://github.com/pydantic/pydantic-ai) | 🟡 **53.9** | 17.1k | 🚀 +146 | 0 | today | `structured` |
| 9 | [Agno](https://github.com/agno-agi/agno) | 🟡 **53.6** | 40.1k | 🚀 +143 | 0 | 1 day ago | `multi-agent` |
| 10 | [DSPy](https://github.com/stanfordnlp/dspy) | 🟡 **51.7** | 34.4k | 🚀 +170 | 0 | 9 days ago | `optimization` |
| 11 | [Semantic Kernel](https://github.com/microsoft/semantic-kernel) | 🟡 **51.5** | 27.9k | 📈 +52 | 0 | 1 day ago | `enterprise` |
| 12 | [Haystack](https://github.com/deepset-ai/haystack) | 🟡 **51.4** | 25.2k | 🚀 +117 | 0 | 2 days ago | `pipeline` |
| 13 | [Letta](https://github.com/letta-ai/letta) | 🟡 **51.1** | 22.7k | 🚀 +204 | 0 | today | `memory` |
| 14 | [Google ADK](https://github.com/google/adk-python) | 🟡 **50.8** | 19.6k | 🚀 +118 | 0 | 6 days ago | `orchestration` |
| 15 | [AG2](https://github.com/ag2ai/ag2) | 🟡 **48.8** | 4.5k | 📈 +29 | 0 | 2 days ago | `multi-agent` |
| 16 | [Composio](https://github.com/ComposioHQ/composio) | 🟡 **48.2** | 28.2k | 🚀 +130 | 0 | 1 day ago | `tooling` |
| 17 | [Smolagents](https://github.com/huggingface/smolagents) | 🟡 **46.3** | 27.3k | 🚀 +162 | 0 | today | `lightweight` |
| 18 | [AutoGen](https://github.com/microsoft/autogen) | 🟡 **43.6** | 58.0k | 🚀 +225 | 0 | 7 mo ago | `multi-agent` |
| 19 | [Swarm](https://github.com/openai/swarm) | 🔴 **9.5** | 21.5k | 📈 +37 | 0 | — | `experimental` |

## 📂 By Category

- `data-agent`: **LlamaIndex** (60.0)
- `enterprise`: **Semantic Kernel** (51.5)
- `experimental`: **Swarm** (9.5)
- `lightweight`: **Smolagents** (46.3)
- `memory`: **Letta** (51.1)
- `multi-agent`: **CrewAI** (71.1), **Agno** (53.6), **AG2** (48.8), **AutoGen** (43.6)
- `optimization`: **DSPy** (51.7)
- `orchestration`: **OpenAI Agents SDK** (70.8), **LangGraph** (68.7), **Claude Agent SDK** (64.8), **Google ADK** (50.8)
- `pipeline`: **Haystack** (51.4)
- `structured`: **PydanticAI** (53.9)
- `tooling`: **Composio** (48.2)
- `typescript`: **Mastra** (78.1)
- `web-agent`: **BrowserUse** (67.4)

## 🔍 Top 5 — Score Breakdown

| Framework | Star Velocity | Release Freshness | Issue Health | Commit Activity | Community | Fork Ratio |
|-----------|:---:|:---:|:---:|:---:|:---:|:---:|
| **Mastra** | 46.8 | 99.7 | 94.9 | 100 | 87.2 | 34.7 |
| **CrewAI** | 100 | 99.3 | 98.6 | 0.0 | 59.2 | 55.3 |
| **OpenAI Agents SDK** | 100 | 99.0 | 96.5 | 0.0 | 54.0 | 61.3 |
| **LangGraph** | 100 | 99.0 | 77.5 | 0.0 | 54.6 | 67.9 |
| **BrowserUse** | 100 | 85.7 | 96.3 | 0.0 | 63.0 | 45.2 |

## 💡 Key Insights

- **Hottest framework**: Mastra with a Pulse Score of 78.1
- **Fastest growing**: Claude Agent SDK gained +2267 stars this week
- **Most active development**: Mastra with 1026 commits in the last 4 weeks
- **Stale releases**: Swarm haven't released in a while

## 📦 Recent Releases

- **PydanticAI** [`v1.96.1`](https://github.com/pydantic/pydantic-ai/releases/tag/v1.96.1) — today
- **Claude Agent SDK** [`v2.1.142`](https://github.com/anthropics/claude-code/releases/tag/v2.1.142) — today
- **LlamaIndex** [`v0.14.22`](https://github.com/run-llama/llama_index/releases/tag/v0.14.22) — today
- **Letta** [`0.16.8`](https://github.com/letta-ai/letta/releases/tag/0.16.8) — today
- **Smolagents** [`v1.25.0`](https://github.com/huggingface/smolagents/releases/tag/v1.25.0) — today
- **Agno** [`v2.6.6`](https://github.com/agno-agi/agno/releases/tag/v2.6.6) — 1 day ago
- **Semantic Kernel** [`python-1.42.0`](https://github.com/microsoft/semantic-kernel/releases/tag/python-1.42.0) — 1 day ago
- **Composio** [`@composio/cli@0.2.31-beta.251`](https://github.com/ComposioHQ/composio/releases/tag/@composio/cli@0.2.31-beta.251) — 1 day ago *(pre-release)*
- **Mastra** [`@mastra/core@1.33.0`](https://github.com/mastra-ai/mastra/releases/tag/@mastra/core@1.33.0) — 1 day ago
- **AG2** [`v0.13.0`](https://github.com/ag2ai/ag2/releases/tag/v0.13.0) — 2 days ago

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

*Powered by GitHub Actions • Data refreshed daily • Last run: 2026-05-15 08:56 UTC*