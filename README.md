# 🔬 AI Agent Framework Pulse Tracker

[![Daily Update](https://github.com/PurpleHaze2320/ai-agent-pulse/actions/workflows/track.yml/badge.svg)](https://github.com/PurpleHaze2320/ai-agent-pulse/actions/workflows/track.yml)
[![Frameworks Tracked](https://img.shields.io/badge/frameworks-19-blue)](https://github.com/PurpleHaze2320/ai-agent-pulse)
[![License: MIT](https://img.shields.io/badge/License-MIT-green.svg)](https://opensource.org/licenses/MIT)
[![GitHub stars](https://img.shields.io/github/stars/PurpleHaze2320/ai-agent-pulse?style=social)](https://github.com/PurpleHaze2320/ai-agent-pulse/stargazers)

> Automated daily tracking of the AI agent framework ecosystem's health, momentum, and trends.
> Last updated: **2026-06-01 11:46 UTC** | Tracking **19** frameworks

## How It Works

This bot runs daily via GitHub Actions and collects metrics from the GitHub API for the most important
AI agent frameworks. It computes a **Pulse Score** (0-100) based on six weighted signals: star velocity,
release freshness, issue health, commit activity, community size, and fork engagement. The result is
a living dashboard that shows which frameworks are gaining momentum and which are losing steam.

## 🏆 Pulse Leaderboard

| Rank | Framework | Pulse | Stars | ⭐ 7d | Commits (4w) | Last Release | Category |
|------|-----------|-------|-------|-------|--------------|--------------|----------|
| 1 | [Mastra](https://github.com/mastra-ai/mastra) | 🟢 **82.9** | 24.6k | 🚀 +341 | 769 | 4 days ago | `typescript` |
| 2 | [BrowserUse](https://github.com/browser-use/browser-use) | 🟡 **69.7** | 96.5k | 🚀 +1088 | 0 | 6 days ago | `web-agent` |
| 3 | [CrewAI](https://github.com/crewAIInc/crewAI) | 🟡 **69.4** | 52.6k | 🚀 +441 | 0 | 3 days ago | `multi-agent` |
| 4 | [LangGraph](https://github.com/langchain-ai/langgraph) | 🟡 **68.5** | 33.6k | 🚀 +666 | 0 | 3 days ago | `orchestration` |
| 5 | [Claude Agent SDK](https://github.com/anthropics/claude-code) | 🟡 **65.6** | 129.2k | 🚀 +2841 | 0 | today | `orchestration` |
| 6 | [LlamaIndex](https://github.com/run-llama/llama_index) | 🟡 **58.0** | 49.8k | 🚀 +178 | 0 | 17 days ago | `data-agent` |
| 7 | [OpenAI Agents SDK](https://github.com/openai/openai-agents-python) | 🟡 **56.4** | 26.8k | 🚀 +189 | 0 | 6 days ago | `orchestration` |
| 8 | [PydanticAI](https://github.com/pydantic/pydantic-ai) | 🟡 **54.3** | 17.4k | 🚀 +158 | 0 | 3 days ago | `structured` |
| 9 | [Agno](https://github.com/agno-agi/agno) | 🟡 **51.7** | 40.4k | 🚀 +102 | 0 | 10 days ago | `multi-agent` |
| 10 | [Semantic Kernel](https://github.com/microsoft/semantic-kernel) | 🟡 **51.1** | 28.0k | 📈 +46 | 0 | 4 days ago | `enterprise` |
| 11 | [DSPy](https://github.com/stanfordnlp/dspy) | 🟡 **50.6** | 34.8k | 🚀 +140 | 0 | 4 days ago | `optimization` |
| 12 | [Google ADK](https://github.com/google/adk-python) | 🟡 **50.3** | 19.9k | 🚀 +112 | 0 | 9 days ago | `orchestration` |
| 13 | [AG2](https://github.com/ag2ai/ag2) | 🟡 **48.7** | 4.6k | 📈 +22 | 0 | 3 days ago | `multi-agent` |
| 14 | [Haystack](https://github.com/deepset-ai/haystack) | 🟡 **48.5** | 25.4k | 📈 +63 | 0 | 19 days ago | `pipeline` |
| 15 | [Letta](https://github.com/letta-ai/letta) | 🟡 **47.7** | 23.1k | 🚀 +131 | 0 | 17 days ago | `memory` |
| 16 | [Composio](https://github.com/ComposioHQ/composio) | 🟡 **47.4** | 28.6k | 🚀 +123 | 0 | 12 days ago | `tooling` |
| 17 | [Smolagents](https://github.com/huggingface/smolagents) | 🟡 **44.9** | 27.6k | 🚀 +139 | 0 | 3 days ago | `lightweight` |
| 18 | [AutoGen](https://github.com/microsoft/autogen) | 🟡 **42.3** | 58.6k | 🚀 +220 | 0 | 8 mo ago | `multi-agent` |
| 19 | [Swarm](https://github.com/openai/swarm) | 🔴 **9.3** | 21.6k | 📈 +33 | 0 | — | `experimental` |

## 📂 By Category

- `data-agent`: **LlamaIndex** (58.0)
- `enterprise`: **Semantic Kernel** (51.1)
- `experimental`: **Swarm** (9.3)
- `lightweight`: **Smolagents** (44.9)
- `memory`: **Letta** (47.7)
- `multi-agent`: **CrewAI** (69.4), **Agno** (51.7), **AG2** (48.7), **AutoGen** (42.3)
- `optimization`: **DSPy** (50.6)
- `orchestration`: **LangGraph** (68.5), **Claude Agent SDK** (65.6), **OpenAI Agents SDK** (56.4), **Google ADK** (50.3)
- `pipeline`: **Haystack** (48.5)
- `structured`: **PydanticAI** (54.3)
- `tooling`: **Composio** (47.4)
- `typescript`: **Mastra** (82.9)
- `web-agent`: **BrowserUse** (69.7)

## 🔍 Top 5 — Score Breakdown

| Framework | Star Velocity | Release Freshness | Issue Health | Commit Activity | Community | Fork Ratio |
|-----------|:---:|:---:|:---:|:---:|:---:|:---:|
| **Mastra** | 65.0 | 98.7 | 95.7 | 100 | 90.6 | 35.3 |
| **BrowserUse** | 100 | 98.0 | 95.5 | 0.0 | 63.0 | 44.8 |
| **CrewAI** | 93.7 | 99.0 | 98.0 | 0.0 | 59.4 | 55.7 |
| **LangGraph** | 100 | 99.0 | 76.2 | 0.0 | 55.0 | 67.4 |
| **Claude Agent SDK** | 100 | 100.0 | 87.0 | 0.0 | 10.2 | 65.1 |

## 💡 Key Insights

- **Hottest framework**: Mastra with a Pulse Score of 82.9
- **Fastest growing**: Claude Agent SDK gained +2841 stars this week
- **Most active development**: Mastra with 769 commits in the last 4 weeks
- **Stale releases**: Swarm haven't released in a while

## 📦 Recent Releases

- **Claude Agent SDK** [`v2.1.159`](https://github.com/anthropics/claude-code/releases/tag/v2.1.159) — today
- **Smolagents** [`v1.26.0`](https://github.com/huggingface/smolagents/releases/tag/v1.26.0) — 3 days ago
- **PydanticAI** [`v2.0.0b4`](https://github.com/pydantic/pydantic-ai/releases/tag/v2.0.0b4) — 3 days ago *(pre-release)*
- **AG2** [`v0.13.2`](https://github.com/ag2ai/ag2/releases/tag/v0.13.2) — 3 days ago
- **CrewAI** [`1.14.6`](https://github.com/crewAIInc/crewAI/releases/tag/1.14.6) — 3 days ago
- **LangGraph** [`sdk==0.4.0`](https://github.com/langchain-ai/langgraph/releases/tag/sdk==0.4.0) — 3 days ago
- **Semantic Kernel** [`dotnet-1.77.0`](https://github.com/microsoft/semantic-kernel/releases/tag/dotnet-1.77.0) — 4 days ago
- **DSPy** [`3.3.0b1`](https://github.com/stanfordnlp/dspy/releases/tag/3.3.0b1) — 4 days ago *(pre-release)*
- **Mastra** [`@mastra/core@1.37.0`](https://github.com/mastra-ai/mastra/releases/tag/@mastra/core@1.37.0) — 4 days ago
- **OpenAI Agents SDK** [`v0.17.4`](https://github.com/openai/openai-agents-python/releases/tag/v0.17.4) — 6 days ago

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

*Powered by GitHub Actions • Data refreshed daily • Last run: 2026-06-01 11:46 UTC*