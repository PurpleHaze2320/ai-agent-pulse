# 🔬 AI Agent Framework Pulse Tracker

[![Daily Update](https://github.com/PurpleHaze2320/ai-agent-pulse/actions/workflows/track.yml/badge.svg)](https://github.com/PurpleHaze2320/ai-agent-pulse/actions/workflows/track.yml)
[![Frameworks Tracked](https://img.shields.io/badge/frameworks-19-blue)](https://github.com/PurpleHaze2320/ai-agent-pulse)
[![License: MIT](https://img.shields.io/badge/License-MIT-green.svg)](https://opensource.org/licenses/MIT)
[![GitHub stars](https://img.shields.io/github/stars/PurpleHaze2320/ai-agent-pulse?style=social)](https://github.com/PurpleHaze2320/ai-agent-pulse/stargazers)

> Automated daily tracking of the AI agent framework ecosystem's health, momentum, and trends.
> Last updated: **2026-06-21 09:57 UTC** | Tracking **19** frameworks

## How It Works

This bot runs daily via GitHub Actions and collects metrics from the GitHub API for the most important
AI agent frameworks. It computes a **Pulse Score** (0-100) based on six weighted signals: star velocity,
release freshness, issue health, commit activity, community size, and fork engagement. The result is
a living dashboard that shows which frameworks are gaining momentum and which are losing steam.

## 🏆 Pulse Leaderboard

| Rank | Framework | Pulse | Stars | ⭐ 7d | Commits (4w) | Last Release | Category |
|------|-----------|-------|-------|-------|--------------|--------------|----------|
| 1 | [CrewAI](https://github.com/crewAIInc/crewAI) | 🟢 **90.9** | 54.1k | 🚀 +537 | 101 | 2 days ago | `multi-agent` |
| 2 | [BrowserUse](https://github.com/browser-use/browser-use) | 🟢 **89.5** | 99.8k | 🚀 +1075 | 409 | 8 days ago | `web-agent` |
| 3 | [Mastra](https://github.com/mastra-ai/mastra) | 🟢 **79.5** | 25.3k | 🚀 +242 | 675 | 1 day ago | `typescript` |
| 4 | [LangGraph](https://github.com/langchain-ai/langgraph) | 🟢 **78.9** | 35.3k | 🚀 +637 | 53 | 2 days ago | `orchestration` |
| 5 | [Claude Agent SDK](https://github.com/anthropics/claude-code) | 🟢 **70.9** | 133.5k | 🚀 +1255 | 26 | today | `orchestration` |
| 6 | [Haystack](https://github.com/deepset-ai/haystack) | 🟡 **69.3** | 25.6k | 📈 +55 | 132 | 3 days ago | `pipeline` |
| 7 | [Agno](https://github.com/agno-agi/agno) | 🟡 **67.1** | 40.8k | 🚀 +111 | 75 | 2 days ago | `multi-agent` |
| 8 | [PydanticAI](https://github.com/pydantic/pydantic-ai) | 🟡 **65.0** | 17.9k | 🚀 +134 | 58 | 10 days ago | `structured` |
| 9 | [OpenAI Agents SDK](https://github.com/openai/openai-agents-python) | 🟡 **59.2** | 27.3k | 🚀 +155 | 25 | 2 days ago | `orchestration` |
| 10 | [Composio](https://github.com/ComposioHQ/composio) | 🟡 **59.1** | 28.9k | 🚀 +125 | 56 | today | `tooling` |
| 11 | [Semantic Kernel](https://github.com/microsoft/semantic-kernel) | 🟡 **56.8** | 28.2k | 📈 +54 | 26 | 4 days ago | `enterprise` |
| 12 | [LlamaIndex](https://github.com/run-llama/llama_index) | 🟡 **56.7** | 50.2k | 🚀 +135 | 9 | 1 mo ago | `data-agent` |
| 13 | [AG2](https://github.com/ag2ai/ag2) | 🟡 **56.3** | 4.7k | ↗️ +20 | 41 | 8 days ago | `multi-agent` |
| 14 | [DSPy](https://github.com/stanfordnlp/dspy) | 🟡 **56.0** | 35.2k | 🚀 +223 | 18 | 24 days ago | `optimization` |
| 15 | [Google ADK](https://github.com/google/adk-python) | 🟡 **51.4** | 20.2k | 🚀 +105 | 0 | 2 days ago | `orchestration` |
| 16 | [Letta](https://github.com/letta-ai/letta) | 🟡 **45.5** | 23.4k | 🚀 +121 | 0 | 1 mo ago | `memory` |
| 17 | [Smolagents](https://github.com/huggingface/smolagents) | 🟡 **41.8** | 27.9k | 📈 +99 | 0 | 23 days ago | `lightweight` |
| 18 | [AutoGen](https://github.com/microsoft/autogen) | 🟠 **38.4** | 59.1k | 🚀 +161 | 0 | 8 mo ago | `multi-agent` |
| 19 | [Swarm](https://github.com/openai/swarm) | 🔴 **9.0** | 21.7k | 📈 +26 | 0 | — | `experimental` |

## 📂 By Category

- `data-agent`: **LlamaIndex** (56.7)
- `enterprise`: **Semantic Kernel** (56.8)
- `experimental`: **Swarm** (9.0)
- `lightweight`: **Smolagents** (41.8)
- `memory`: **Letta** (45.5)
- `multi-agent`: **CrewAI** (90.9), **Agno** (67.1), **AG2** (56.3), **AutoGen** (38.4)
- `optimization`: **DSPy** (56.0)
- `orchestration`: **LangGraph** (78.9), **Claude Agent SDK** (70.9), **OpenAI Agents SDK** (59.2), **Google ADK** (51.4)
- `pipeline`: **Haystack** (69.3)
- `structured`: **PydanticAI** (65.0)
- `tooling`: **Composio** (59.1)
- `typescript`: **Mastra** (79.5)
- `web-agent`: **BrowserUse** (89.5)

## 🔍 Top 5 — Score Breakdown

| Framework | Star Velocity | Release Freshness | Issue Health | Commit Activity | Community | Fork Ratio |
|-----------|:---:|:---:|:---:|:---:|:---:|:---:|
| **CrewAI** | 100 | 99.3 | 96.5 | 100 | 59.4 | 56.0 |
| **BrowserUse** | 100 | 97.3 | 95.4 | 100 | 63.0 | 44.6 |
| **Mastra** | 50.4 | 99.7 | 94.6 | 100 | 91.8 | 35.8 |
| **LangGraph** | 100 | 99.3 | 74.5 | 53.0 | 55.0 | 67.1 |
| **Claude Agent SDK** | 100 | 100.0 | 87.9 | 26.0 | 10.4 | 64.7 |

## 💡 Key Insights

- **Hottest framework**: CrewAI with a Pulse Score of 90.9
- **Fastest growing**: Claude Agent SDK gained +1255 stars this week
- **Most active development**: Mastra with 675 commits in the last 4 weeks
- **Stale releases**: Swarm haven't released in a while

## 📦 Recent Releases

- **Composio** [`@composio/cli@0.2.32-beta.270`](https://github.com/ComposioHQ/composio/releases/tag/@composio/cli@0.2.32-beta.270) — today *(pre-release)*
- **Claude Agent SDK** [`v2.1.185`](https://github.com/anthropics/claude-code/releases/tag/v2.1.185) — today
- **Mastra** [`@mastra/core@1.45.0`](https://github.com/mastra-ai/mastra/releases/tag/@mastra/core@1.45.0) — 1 day ago
- **OpenAI Agents SDK** [`v0.17.6`](https://github.com/openai/openai-agents-python/releases/tag/v0.17.6) — 2 days ago
- **CrewAI** [`1.14.8a2`](https://github.com/crewAIInc/crewAI/releases/tag/1.14.8a2) — 2 days ago *(pre-release)*
- **LangGraph** [`1.2.6`](https://github.com/langchain-ai/langgraph/releases/tag/1.2.6) — 2 days ago
- **Agno** [`v2.6.18`](https://github.com/agno-agi/agno/releases/tag/v2.6.18) — 2 days ago
- **Google ADK** [`v2.3.0`](https://github.com/google/adk-python/releases/tag/v2.3.0) — 2 days ago
- **Haystack** [`v2.30.2`](https://github.com/deepset-ai/haystack/releases/tag/v2.30.2) — 3 days ago
- **Semantic Kernel** [`python-1.43.1`](https://github.com/microsoft/semantic-kernel/releases/tag/python-1.43.1) — 4 days ago

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

*Powered by GitHub Actions • Data refreshed daily • Last run: 2026-06-21 09:57 UTC*