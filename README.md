# 🔬 AI Agent Framework Pulse Tracker

[![Daily Update](https://github.com/PurpleHaze2320/ai-agent-pulse/actions/workflows/track.yml/badge.svg)](https://github.com/PurpleHaze2320/ai-agent-pulse/actions/workflows/track.yml)
[![Frameworks Tracked](https://img.shields.io/badge/frameworks-19-blue)](https://github.com/PurpleHaze2320/ai-agent-pulse)
[![License: MIT](https://img.shields.io/badge/License-MIT-green.svg)](https://opensource.org/licenses/MIT)
[![GitHub stars](https://img.shields.io/github/stars/PurpleHaze2320/ai-agent-pulse?style=social)](https://github.com/PurpleHaze2320/ai-agent-pulse/stargazers)

> Automated daily tracking of the AI agent framework ecosystem's health, momentum, and trends.
> Last updated: **2026-06-03 11:10 UTC** | Tracking **19** frameworks

## How It Works

This bot runs daily via GitHub Actions and collects metrics from the GitHub API for the most important
AI agent frameworks. It computes a **Pulse Score** (0-100) based on six weighted signals: star velocity,
release freshness, issue health, commit activity, community size, and fork engagement. The result is
a living dashboard that shows which frameworks are gaining momentum and which are losing steam.

## 🏆 Pulse Leaderboard

| Rank | Framework | Pulse | Stars | ⭐ 7d | Commits (4w) | Last Release | Category |
|------|-----------|-------|-------|-------|--------------|--------------|----------|
| 1 | [Mastra](https://github.com/mastra-ai/mastra) | 🟢 **82.5** | 24.7k | 🚀 +328 | 861 | 6 days ago | `typescript` |
| 2 | [CrewAI](https://github.com/crewAIInc/crewAI) | 🟢 **70.2** | 52.7k | 🚀 +463 | 0 | 5 days ago | `multi-agent` |
| 3 | [BrowserUse](https://github.com/browser-use/browser-use) | 🟡 **69.6** | 96.9k | 🚀 +1115 | 0 | 8 days ago | `web-agent` |
| 4 | [LangGraph](https://github.com/langchain-ai/langgraph) | 🟡 **68.6** | 33.7k | 🚀 +628 | 0 | today | `orchestration` |
| 5 | [Claude Agent SDK](https://github.com/anthropics/claude-code) | 🟡 **65.6** | 129.8k | 🚀 +2875 | 0 | today | `orchestration` |
| 6 | [LlamaIndex](https://github.com/run-llama/llama_index) | 🟡 **57.9** | 49.9k | 🚀 +177 | 0 | 19 days ago | `data-agent` |
| 7 | [OpenAI Agents SDK](https://github.com/openai/openai-agents-python) | 🟡 **55.6** | 26.9k | 🚀 +177 | 0 | 8 days ago | `orchestration` |
| 8 | [PydanticAI](https://github.com/pydantic/pydantic-ai) | 🟡 **54.3** | 17.5k | 🚀 +151 | 0 | 1 day ago | `structured` |
| 9 | [Agno](https://github.com/agno-agi/agno) | 🟡 **52.7** | 40.5k | 🚀 +112 | 0 | today | `multi-agent` |
| 10 | [Semantic Kernel](https://github.com/microsoft/semantic-kernel) | 🟡 **51.2** | 28.0k | 📈 +49 | 0 | 6 days ago | `enterprise` |
| 11 | [Google ADK](https://github.com/google/adk-python) | 🟡 **50.3** | 20.0k | 📈 +92 | 0 | 1 day ago | `orchestration` |
| 12 | [DSPy](https://github.com/stanfordnlp/dspy) | 🟡 **50.2** | 34.8k | 🚀 +132 | 0 | 6 days ago | `optimization` |
| 13 | [Haystack](https://github.com/deepset-ai/haystack) | 🟡 **49.7** | 25.4k | 📈 +60 | 0 | today | `pipeline` |
| 14 | [AG2](https://github.com/ag2ai/ag2) | 🟡 **48.4** | 4.6k | ↗️ +19 | 0 | 5 days ago | `multi-agent` |
| 15 | [Letta](https://github.com/letta-ai/letta) | 🟡 **47.8** | 23.1k | 🚀 +134 | 0 | 19 days ago | `memory` |
| 16 | [Composio](https://github.com/ComposioHQ/composio) | 🟡 **46.8** | 28.6k | 🚀 +116 | 0 | 14 days ago | `tooling` |
| 17 | [Smolagents](https://github.com/huggingface/smolagents) | 🟡 **44.9** | 27.7k | 🚀 +140 | 0 | 5 days ago | `lightweight` |
| 18 | [AutoGen](https://github.com/microsoft/autogen) | 🟡 **41.9** | 58.7k | 🚀 +210 | 0 | 8 mo ago | `multi-agent` |
| 19 | [Swarm](https://github.com/openai/swarm) | 🔴 **9.4** | 21.6k | 📈 +35 | 0 | — | `experimental` |

## 📂 By Category

- `data-agent`: **LlamaIndex** (57.9)
- `enterprise`: **Semantic Kernel** (51.2)
- `experimental`: **Swarm** (9.4)
- `lightweight`: **Smolagents** (44.9)
- `memory`: **Letta** (47.8)
- `multi-agent`: **CrewAI** (70.2), **Agno** (52.7), **AG2** (48.4), **AutoGen** (41.9)
- `optimization`: **DSPy** (50.2)
- `orchestration`: **LangGraph** (68.6), **Claude Agent SDK** (65.6), **OpenAI Agents SDK** (55.6), **Google ADK** (50.3)
- `pipeline`: **Haystack** (49.7)
- `structured`: **PydanticAI** (54.3)
- `tooling`: **Composio** (46.8)
- `typescript`: **Mastra** (82.5)
- `web-agent`: **BrowserUse** (69.6)

## 🔍 Top 5 — Score Breakdown

| Framework | Star Velocity | Release Freshness | Issue Health | Commit Activity | Community | Fork Ratio |
|-----------|:---:|:---:|:---:|:---:|:---:|:---:|
| **Mastra** | 63.4 | 98.0 | 95.7 | 100 | 92.0 | 35.4 |
| **CrewAI** | 97.4 | 98.3 | 97.9 | 0.0 | 59.4 | 55.8 |
| **BrowserUse** | 100 | 97.3 | 95.9 | 0.0 | 63.0 | 44.8 |
| **LangGraph** | 100 | 100.0 | 76.0 | 0.0 | 55.0 | 67.3 |
| **Claude Agent SDK** | 100 | 100.0 | 87.5 | 0.0 | 10.2 | 65.0 |

## 💡 Key Insights

- **Hottest framework**: Mastra with a Pulse Score of 82.5
- **Fastest growing**: Claude Agent SDK gained +2875 stars this week
- **Most active development**: Mastra with 861 commits in the last 4 weeks
- **Stale releases**: Swarm haven't released in a while

## 📦 Recent Releases

- **Haystack** [`v2.30.0`](https://github.com/deepset-ai/haystack/releases/tag/v2.30.0) — today
- **Claude Agent SDK** [`v2.1.161`](https://github.com/anthropics/claude-code/releases/tag/v2.1.161) — today
- **LangGraph** [`1.2.4`](https://github.com/langchain-ai/langgraph/releases/tag/1.2.4) — today
- **Agno** [`v2.6.11`](https://github.com/agno-agi/agno/releases/tag/v2.6.11) — today
- **PydanticAI** [`v2.0.0b5`](https://github.com/pydantic/pydantic-ai/releases/tag/v2.0.0b5) — 1 day ago *(pre-release)*
- **Google ADK** [`v1.34.2`](https://github.com/google/adk-python/releases/tag/v1.34.2) — 1 day ago
- **Smolagents** [`v1.26.0`](https://github.com/huggingface/smolagents/releases/tag/v1.26.0) — 5 days ago
- **AG2** [`v0.13.2`](https://github.com/ag2ai/ag2/releases/tag/v0.13.2) — 5 days ago
- **CrewAI** [`1.14.6`](https://github.com/crewAIInc/crewAI/releases/tag/1.14.6) — 5 days ago
- **Semantic Kernel** [`dotnet-1.77.0`](https://github.com/microsoft/semantic-kernel/releases/tag/dotnet-1.77.0) — 6 days ago

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

*Powered by GitHub Actions • Data refreshed daily • Last run: 2026-06-03 11:10 UTC*