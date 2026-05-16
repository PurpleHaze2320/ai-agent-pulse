# 🔬 AI Agent Framework Pulse Tracker

[![Daily Update](https://github.com/PurpleHaze2320/ai-agent-pulse/actions/workflows/track.yml/badge.svg)](https://github.com/PurpleHaze2320/ai-agent-pulse/actions/workflows/track.yml)
[![Frameworks Tracked](https://img.shields.io/badge/frameworks-19-blue)](https://github.com/PurpleHaze2320/ai-agent-pulse)
[![License: MIT](https://img.shields.io/badge/License-MIT-green.svg)](https://opensource.org/licenses/MIT)
[![GitHub stars](https://img.shields.io/github/stars/PurpleHaze2320/ai-agent-pulse?style=social)](https://github.com/PurpleHaze2320/ai-agent-pulse/stargazers)

> Automated daily tracking of the AI agent framework ecosystem's health, momentum, and trends.
> Last updated: **2026-05-16 08:11 UTC** | Tracking **19** frameworks

## How It Works

This bot runs daily via GitHub Actions and collects metrics from the GitHub API for the most important
AI agent frameworks. It computes a **Pulse Score** (0-100) based on six weighted signals: star velocity,
release freshness, issue health, commit activity, community size, and fork engagement. The result is
a living dashboard that shows which frameworks are gaining momentum and which are losing steam.

## 🏆 Pulse Leaderboard

| Rank | Framework | Pulse | Stars | ⭐ 7d | Commits (4w) | Last Release | Category |
|------|-----------|-------|-------|-------|--------------|--------------|----------|
| 1 | [Mastra](https://github.com/mastra-ai/mastra) | 🟢 **77.6** | 23.9k | 🚀 +225 | 1066 | today | `typescript` |
| 2 | [CrewAI](https://github.com/crewAIInc/crewAI) | 🟢 **71.2** | 51.5k | 🚀 +536 | 0 | today | `multi-agent` |
| 3 | [OpenAI Agents SDK](https://github.com/openai/openai-agents-python) | 🟢 **70.7** | 26.3k | 🚀 +246 | 0 | 4 days ago | `orchestration` |
| 4 | [LangGraph](https://github.com/langchain-ai/langgraph) | 🟡 **68.6** | 32.1k | 🚀 +567 | 0 | 4 days ago | `orchestration` |
| 5 | [BrowserUse](https://github.com/browser-use/browser-use) | 🟡 **67.3** | 94.1k | 🚀 +1089 | 0 | 1 mo ago | `web-agent` |
| 6 | [Claude Agent SDK](https://github.com/anthropics/claude-code) | 🟡 **64.8** | 124.0k | 🚀 +2165 | 0 | today | `orchestration` |
| 7 | [LlamaIndex](https://github.com/run-llama/llama_index) | 🟡 **59.7** | 49.4k | 🚀 +188 | 0 | 1 day ago | `data-agent` |
| 8 | [PydanticAI](https://github.com/pydantic/pydantic-ai) | 🟡 **53.7** | 17.1k | 🚀 +140 | 0 | today | `structured` |
| 9 | [Agno](https://github.com/agno-agi/agno) | 🟡 **53.2** | 40.1k | 🚀 +130 | 0 | today | `multi-agent` |
| 10 | [DSPy](https://github.com/stanfordnlp/dspy) | 🟡 **51.4** | 34.5k | 🚀 +165 | 0 | 10 days ago | `optimization` |
| 11 | [Semantic Kernel](https://github.com/microsoft/semantic-kernel) | 🟡 **51.3** | 27.9k | 📈 +49 | 0 | 2 days ago | `enterprise` |
| 12 | [Haystack](https://github.com/deepset-ai/haystack) | 🟡 **51.2** | 25.2k | 🚀 +112 | 0 | 3 days ago | `pipeline` |
| 13 | [Google ADK](https://github.com/google/adk-python) | 🟡 **50.5** | 19.7k | 🚀 +111 | 0 | 7 days ago | `orchestration` |
| 14 | [Letta](https://github.com/letta-ai/letta) | 🟡 **50.2** | 22.7k | 🚀 +179 | 0 | 1 day ago | `memory` |
| 15 | [AG2](https://github.com/ag2ai/ag2) | 🟡 **49.0** | 4.6k | 📈 +36 | 0 | 3 days ago | `multi-agent` |
| 16 | [Composio](https://github.com/ComposioHQ/composio) | 🟡 **48.7** | 28.3k | 🚀 +140 | 0 | today | `tooling` |
| 17 | [Smolagents](https://github.com/huggingface/smolagents) | 🟡 **45.7** | 27.3k | 🚀 +147 | 0 | 1 day ago | `lightweight` |
| 18 | [AutoGen](https://github.com/microsoft/autogen) | 🟡 **43.2** | 58.1k | 🚀 +216 | 0 | 7 mo ago | `multi-agent` |
| 19 | [Swarm](https://github.com/openai/swarm) | 🔴 **9.3** | 21.5k | 📈 +31 | 0 | — | `experimental` |

## 📂 By Category

- `data-agent`: **LlamaIndex** (59.7)
- `enterprise`: **Semantic Kernel** (51.3)
- `experimental`: **Swarm** (9.3)
- `lightweight`: **Smolagents** (45.7)
- `memory`: **Letta** (50.2)
- `multi-agent`: **CrewAI** (71.2), **Agno** (53.2), **AG2** (49.0), **AutoGen** (43.2)
- `optimization`: **DSPy** (51.4)
- `orchestration`: **OpenAI Agents SDK** (70.7), **LangGraph** (68.6), **Claude Agent SDK** (64.8), **Google ADK** (50.5)
- `pipeline`: **Haystack** (51.2)
- `structured`: **PydanticAI** (53.7)
- `tooling`: **Composio** (48.7)
- `typescript`: **Mastra** (77.6)
- `web-agent`: **BrowserUse** (67.3)

## 🔍 Top 5 — Score Breakdown

| Framework | Star Velocity | Release Freshness | Issue Health | Commit Activity | Community | Fork Ratio |
|-----------|:---:|:---:|:---:|:---:|:---:|:---:|
| **Mastra** | 44.7 | 100.0 | 94.8 | 100 | 87.4 | 34.7 |
| **CrewAI** | 100 | 100.0 | 98.4 | 0.0 | 59.2 | 55.3 |
| **OpenAI Agents SDK** | 100 | 98.7 | 96.5 | 0.0 | 54.0 | 61.3 |
| **LangGraph** | 100 | 98.7 | 77.4 | 0.0 | 54.6 | 67.9 |
| **BrowserUse** | 100 | 85.3 | 96.3 | 0.0 | 63.0 | 45.2 |

## 💡 Key Insights

- **Hottest framework**: Mastra with a Pulse Score of 77.6
- **Fastest growing**: Claude Agent SDK gained +2165 stars this week
- **Most active development**: Mastra with 1066 commits in the last 4 weeks
- **Stale releases**: Swarm haven't released in a while

## 📦 Recent Releases

- **Composio** [`@composio/cli@0.2.31-beta.252`](https://github.com/ComposioHQ/composio/releases/tag/@composio/cli@0.2.31-beta.252) — today *(pre-release)*
- **Mastra** [`@mastra/core@1.34.0`](https://github.com/mastra-ai/mastra/releases/tag/@mastra/core@1.34.0) — today
- **Claude Agent SDK** [`v2.1.143`](https://github.com/anthropics/claude-code/releases/tag/v2.1.143) — today
- **PydanticAI** [`v1.97.0`](https://github.com/pydantic/pydantic-ai/releases/tag/v1.97.0) — today
- **CrewAI** [`1.14.5a6`](https://github.com/crewAIInc/crewAI/releases/tag/1.14.5a6) — today *(pre-release)*
- **Agno** [`v2.6.7`](https://github.com/agno-agi/agno/releases/tag/v2.6.7) — today
- **LlamaIndex** [`v0.14.22`](https://github.com/run-llama/llama_index/releases/tag/v0.14.22) — 1 day ago
- **Letta** [`0.16.8`](https://github.com/letta-ai/letta/releases/tag/0.16.8) — 1 day ago
- **Smolagents** [`v1.25.0`](https://github.com/huggingface/smolagents/releases/tag/v1.25.0) — 1 day ago
- **Semantic Kernel** [`python-1.42.0`](https://github.com/microsoft/semantic-kernel/releases/tag/python-1.42.0) — 2 days ago

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

*Powered by GitHub Actions • Data refreshed daily • Last run: 2026-05-16 08:11 UTC*