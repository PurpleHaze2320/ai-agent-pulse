# 🔬 AI Agent Framework Pulse Tracker

[![Daily Update](https://github.com/PurpleHaze2320/ai-agent-pulse/actions/workflows/track.yml/badge.svg)](https://github.com/PurpleHaze2320/ai-agent-pulse/actions/workflows/track.yml)
[![Frameworks Tracked](https://img.shields.io/badge/frameworks-19-blue)](https://github.com/PurpleHaze2320/ai-agent-pulse)
[![License: MIT](https://img.shields.io/badge/License-MIT-green.svg)](https://opensource.org/licenses/MIT)
[![GitHub stars](https://img.shields.io/github/stars/PurpleHaze2320/ai-agent-pulse?style=social)](https://github.com/PurpleHaze2320/ai-agent-pulse/stargazers)

> Automated daily tracking of the AI agent framework ecosystem's health, momentum, and trends.
> Last updated: **2026-07-07 09:51 UTC** | Tracking **19** frameworks

## How It Works

This bot runs daily via GitHub Actions and collects metrics from the GitHub API for the most important
AI agent frameworks. It computes a **Pulse Score** (0-100) based on six weighted signals: star velocity,
release freshness, issue health, commit activity, community size, and fork engagement. The result is
a living dashboard that shows which frameworks are gaining momentum and which are losing steam.

## 🏆 Pulse Leaderboard

| Rank | Framework | Pulse | Stars | ⭐ 7d | Commits (4w) | Last Release | Category |
|------|-----------|-------|-------|-------|--------------|--------------|----------|
| 1 | [CrewAI](https://github.com/crewAIInc/crewAI) | 🟢 **88.6** | 55.1k | 🚀 +449 | 97 | 5 days ago | `multi-agent` |
| 2 | [Mastra](https://github.com/mastra-ai/mastra) | 🟢 **81.1** | 25.9k | 🚀 +283 | 907 | today | `typescript` |
| 3 | [BrowserUse](https://github.com/browser-use/browser-use) | 🟢 **80.0** | 103.2k | 🚀 +1671 | 52 | 5 days ago | `web-agent` |
| 4 | [LangGraph](https://github.com/langchain-ai/langgraph) | 🟢 **77.8** | 36.7k | 🚀 +558 | 48 | today | `orchestration` |
| 5 | [Google ADK](https://github.com/google/adk-python) | 🟢 **74.6** | 20.5k | 🚀 +163 | 296 | today | `orchestration` |
| 6 | [Claude Agent SDK](https://github.com/anthropics/claude-code) | 🟢 **70.5** | 136.6k | 🚀 +1562 | 25 | today | `orchestration` |
| 7 | [OpenAI Agents SDK](https://github.com/openai/openai-agents-python) | 🟡 **68.9** | 27.7k | 🚀 +177 | 66 | today | `orchestration` |
| 8 | [Composio](https://github.com/ComposioHQ/composio) | 🟡 **67.0** | 29.1k | 📈 +93 | 124 | today | `tooling` |
| 9 | [LlamaIndex](https://github.com/run-llama/llama_index) | 🟡 **63.1** | 50.7k | 🚀 +170 | 25 | 12 days ago | `data-agent` |
| 10 | [AG2](https://github.com/ag2ai/ag2) | 🟡 **62.5** | 4.7k | 📈 +28 | 61 | 3 days ago | `multi-agent` |
| 11 | [PydanticAI](https://github.com/pydantic/pydantic-ai) | 🟡 **55.5** | 18.3k | 🚀 +160 | 0 | today | `structured` |
| 12 | [DSPy](https://github.com/stanfordnlp/dspy) | 🟡 **53.7** | 35.9k | 🚀 +236 | 3 | 1 mo ago | `optimization` |
| 13 | [Agno](https://github.com/agno-agi/agno) | 🟡 **52.1** | 41.0k | 🚀 +112 | 0 | today | `multi-agent` |
| 14 | [Semantic Kernel](https://github.com/microsoft/semantic-kernel) | 🟡 **51.7** | 28.3k | 📈 +50 | 0 | today | `enterprise` |
| 15 | [Haystack](https://github.com/deepset-ai/haystack) | 🟡 **49.9** | 25.8k | 📈 +49 | 0 | today | `pipeline` |
| 16 | [Letta](https://github.com/letta-ai/letta) | 🟡 **43.6** | 23.7k | 🚀 +102 | 0 | 1 mo ago | `memory` |
| 17 | [Smolagents](https://github.com/huggingface/smolagents) | 🟡 **41.4** | 28.2k | 🚀 +123 | 0 | 1 mo ago | `lightweight` |
| 18 | [AutoGen](https://github.com/microsoft/autogen) | 🟠 **37.7** | 59.5k | 🚀 +175 | 0 | 9 mo ago | `multi-agent` |
| 19 | [Swarm](https://github.com/openai/swarm) | 🔴 **9.0** | 21.8k | ↗️ +18 | 0 | — | `experimental` |

## 📂 By Category

- `data-agent`: **LlamaIndex** (63.1)
- `enterprise`: **Semantic Kernel** (51.7)
- `experimental`: **Swarm** (9.0)
- `lightweight`: **Smolagents** (41.4)
- `memory`: **Letta** (43.6)
- `multi-agent`: **CrewAI** (88.6), **AG2** (62.5), **Agno** (52.1), **AutoGen** (37.7)
- `optimization`: **DSPy** (53.7)
- `orchestration`: **LangGraph** (77.8), **Google ADK** (74.6), **Claude Agent SDK** (70.5), **OpenAI Agents SDK** (68.9)
- `pipeline`: **Haystack** (49.9)
- `structured`: **PydanticAI** (55.5)
- `tooling`: **Composio** (67.0)
- `typescript`: **Mastra** (81.1)
- `web-agent`: **BrowserUse** (80.0)

## 🔍 Top 5 — Score Breakdown

| Framework | Star Velocity | Release Freshness | Issue Health | Commit Activity | Community | Fork Ratio |
|-----------|:---:|:---:|:---:|:---:|:---:|:---:|
| **CrewAI** | 94.3 | 98.3 | 95.6 | 97.0 | 59.6 | 56.2 |
| **Mastra** | 55.3 | 100.0 | 95.5 | 100 | 92.6 | 36.6 |
| **BrowserUse** | 100 | 98.3 | 95.0 | 52.0 | 63.0 | 44.3 |
| **LangGraph** | 100 | 100.0 | 73.4 | 48.0 | 55.0 | 67.1 |
| **Google ADK** | 30.3 | 100.0 | 85.2 | 100 | 71.4 | 71.3 |

## 💡 Key Insights

- **Hottest framework**: CrewAI with a Pulse Score of 88.6
- **Fastest growing**: BrowserUse gained +1671 stars this week
- **Most active development**: Mastra with 907 commits in the last 4 weeks
- **Stale releases**: AutoGen, Swarm haven't released in a while

## 📦 Recent Releases

- **Semantic Kernel** [`python-1.44.0`](https://github.com/microsoft/semantic-kernel/releases/tag/python-1.44.0) — today
- **Haystack** [`v2.31.0-rc2`](https://github.com/deepset-ai/haystack/releases/tag/v2.31.0-rc2) — today *(pre-release)*
- **Mastra** [`@mastra/core@1.49.0`](https://github.com/mastra-ai/mastra/releases/tag/@mastra/core@1.49.0) — today
- **OpenAI Agents SDK** [`v0.18.0`](https://github.com/openai/openai-agents-python/releases/tag/v0.18.0) — today
- **PydanticAI** [`v2.5.1`](https://github.com/pydantic/pydantic-ai/releases/tag/v2.5.1) — today
- **Agno** [`v2.7.0a7`](https://github.com/agno-agi/agno/releases/tag/v2.7.0a7) — today *(pre-release)*
- **Claude Agent SDK** [`v2.1.202`](https://github.com/anthropics/claude-code/releases/tag/v2.1.202) — today
- **Google ADK** [`v1.36.1`](https://github.com/google/adk-python/releases/tag/v1.36.1) — today
- **Composio** [`@composio/cli@0.2.32-beta.284`](https://github.com/ComposioHQ/composio/releases/tag/@composio/cli@0.2.32-beta.284) — today *(pre-release)*
- **LangGraph** [`1.2.8`](https://github.com/langchain-ai/langgraph/releases/tag/1.2.8) — today

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

*Powered by GitHub Actions • Data refreshed daily • Last run: 2026-07-07 09:51 UTC*