# 🔬 AI Agent Framework Pulse Tracker

[![Daily Update](https://github.com/PurpleHaze2320/ai-agent-pulse/actions/workflows/track.yml/badge.svg)](https://github.com/PurpleHaze2320/ai-agent-pulse/actions/workflows/track.yml)
[![Frameworks Tracked](https://img.shields.io/badge/frameworks-19-blue)](https://github.com/PurpleHaze2320/ai-agent-pulse)
[![License: MIT](https://img.shields.io/badge/License-MIT-green.svg)](https://opensource.org/licenses/MIT)
[![GitHub stars](https://img.shields.io/github/stars/PurpleHaze2320/ai-agent-pulse?style=social)](https://github.com/PurpleHaze2320/ai-agent-pulse/stargazers)

> Automated daily tracking of the AI agent framework ecosystem's health, momentum, and trends.
> Last updated: **2026-06-06 08:40 UTC** | Tracking **19** frameworks

## How It Works

This bot runs daily via GitHub Actions and collects metrics from the GitHub API for the most important
AI agent frameworks. It computes a **Pulse Score** (0-100) based on six weighted signals: star velocity,
release freshness, issue health, commit activity, community size, and fork engagement. The result is
a living dashboard that shows which frameworks are gaining momentum and which are losing steam.

## 🏆 Pulse Leaderboard

| Rank | Framework | Pulse | Stars | ⭐ 7d | Commits (4w) | Last Release | Category |
|------|-----------|-------|-------|-------|--------------|--------------|----------|
| 1 | [CrewAI](https://github.com/crewAIInc/crewAI) | 🟢 **89.7** | 52.9k | 🚀 +459 | 97 | today | `multi-agent` |
| 2 | [LangGraph](https://github.com/langchain-ai/langgraph) | 🟢 **88.4** | 34.0k | 🚀 +654 | 104 | 3 days ago | `orchestration` |
| 3 | [Mastra](https://github.com/mastra-ai/mastra) | 🟢 **81.0** | 24.8k | 🚀 +270 | 1003 | today | `typescript` |
| 4 | [PydanticAI](https://github.com/pydantic/pydantic-ai) | 🟢 **74.6** | 17.6k | 🚀 +161 | 118 | 1 day ago | `structured` |
| 5 | [Agno](https://github.com/agno-agi/agno) | 🟢 **73.0** | 40.5k | 🚀 +120 | 154 | today | `multi-agent` |
| 6 | [Claude Agent SDK](https://github.com/anthropics/claude-code) | 🟢 **72.2** | 130.5k | 🚀 +2448 | 33 | today | `orchestration` |
| 7 | [OpenAI Agents SDK](https://github.com/openai/openai-agents-python) | 🟢 **71.5** | 26.9k | 🚀 +186 | 79 | 10 days ago | `orchestration` |
| 8 | [Google ADK](https://github.com/google/adk-python) | 🟢 **70.0** | 20.0k | 📈 +82 | 176 | 1 day ago | `orchestration` |
| 9 | [BrowserUse](https://github.com/browser-use/browser-use) | 🟡 **69.4** | 97.4k | 🚀 +1173 | 0 | 11 days ago | `web-agent` |
| 10 | [LlamaIndex](https://github.com/run-llama/llama_index) | 🟡 **68.4** | 49.9k | 🚀 +180 | 53 | 22 days ago | `data-agent` |
| 11 | [Composio](https://github.com/ComposioHQ/composio) | 🟡 **61.9** | 28.7k | 🚀 +128 | 74 | 16 days ago | `tooling` |
| 12 | [DSPy](https://github.com/stanfordnlp/dspy) | 🟡 **59.9** | 34.9k | 🚀 +145 | 47 | 9 days ago | `optimization` |
| 13 | [Semantic Kernel](https://github.com/microsoft/semantic-kernel) | 🟡 **54.2** | 28.1k | 📈 +52 | 13 | 2 days ago | `enterprise` |
| 14 | [Haystack](https://github.com/deepset-ai/haystack) | 🟡 **49.4** | 25.5k | 📈 +56 | 0 | 2 days ago | `pipeline` |
| 15 | [AG2](https://github.com/ag2ai/ag2) | 🟡 **48.8** | 4.6k | 📈 +25 | 0 | 1 day ago | `multi-agent` |
| 16 | [Letta](https://github.com/letta-ai/letta) | 🟡 **47.5** | 23.2k | 🚀 +128 | 1 | 22 days ago | `memory` |
| 17 | [Smolagents](https://github.com/huggingface/smolagents) | 🟡 **44.3** | 27.7k | 🚀 +131 | 0 | 8 days ago | `lightweight` |
| 18 | [AutoGen](https://github.com/microsoft/autogen) | 🟡 **40.9** | 58.7k | 🚀 +191 | 0 | 8 mo ago | `multi-agent` |
| 19 | [Swarm](https://github.com/openai/swarm) | 🔴 **9.4** | 21.6k | 📈 +35 | 0 | — | `experimental` |

## 📂 By Category

- `data-agent`: **LlamaIndex** (68.4)
- `enterprise`: **Semantic Kernel** (54.2)
- `experimental`: **Swarm** (9.4)
- `lightweight`: **Smolagents** (44.3)
- `memory`: **Letta** (47.5)
- `multi-agent`: **CrewAI** (89.7), **Agno** (73.0), **AG2** (48.8), **AutoGen** (40.9)
- `optimization`: **DSPy** (59.9)
- `orchestration`: **LangGraph** (88.4), **Claude Agent SDK** (72.2), **OpenAI Agents SDK** (71.5), **Google ADK** (70.0)
- `pipeline`: **Haystack** (49.4)
- `structured`: **PydanticAI** (74.6)
- `tooling`: **Composio** (61.9)
- `typescript`: **Mastra** (81.0)
- `web-agent`: **BrowserUse** (69.4)

## 🔍 Top 5 — Score Breakdown

| Framework | Star Velocity | Release Freshness | Issue Health | Commit Activity | Community | Fork Ratio |
|-----------|:---:|:---:|:---:|:---:|:---:|:---:|
| **CrewAI** | 96.2 | 100.0 | 97.9 | 97.0 | 59.4 | 55.9 |
| **LangGraph** | 100 | 99.0 | 76.0 | 100 | 55.0 | 67.2 |
| **Mastra** | 55.5 | 100.0 | 95.6 | 100 | 92.2 | 35.5 |
| **PydanticAI** | 32.6 | 99.7 | 82.5 | 100 | 92.2 | 49.7 |
| **Agno** | 25.5 | 100.0 | 82.1 | 100 | 89.0 | 54.1 |

## 💡 Key Insights

- **Hottest framework**: CrewAI with a Pulse Score of 89.7
- **Fastest growing**: Claude Agent SDK gained +2448 stars this week
- **Most active development**: Mastra with 1003 commits in the last 4 weeks
- **Stale releases**: Swarm haven't released in a while

## 📦 Recent Releases

- **Claude Agent SDK** [`v2.1.167`](https://github.com/anthropics/claude-code/releases/tag/v2.1.167) — today
- **CrewAI** [`1.14.7a2`](https://github.com/crewAIInc/crewAI/releases/tag/1.14.7a2) — today *(pre-release)*
- **Agno** [`v2.6.12`](https://github.com/agno-agi/agno/releases/tag/v2.6.12) — today
- **Mastra** [`@mastra/core@1.41.0`](https://github.com/mastra-ai/mastra/releases/tag/@mastra/core@1.41.0) — today
- **AG2** [`v0.13.3`](https://github.com/ag2ai/ag2/releases/tag/v0.13.3) — 1 day ago
- **PydanticAI** [`v2.0.0b6`](https://github.com/pydantic/pydantic-ai/releases/tag/v2.0.0b6) — 1 day ago *(pre-release)*
- **Google ADK** [`v2.2.0`](https://github.com/google/adk-python/releases/tag/v2.2.0) — 1 day ago
- **Semantic Kernel** [`python-1.43.0`](https://github.com/microsoft/semantic-kernel/releases/tag/python-1.43.0) — 2 days ago
- **Haystack** [`v2.30.0`](https://github.com/deepset-ai/haystack/releases/tag/v2.30.0) — 2 days ago
- **LangGraph** [`1.2.4`](https://github.com/langchain-ai/langgraph/releases/tag/1.2.4) — 3 days ago

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

*Powered by GitHub Actions • Data refreshed daily • Last run: 2026-06-06 08:40 UTC*