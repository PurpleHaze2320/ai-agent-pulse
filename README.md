# 🔬 AI Agent Framework Pulse Tracker

[![Daily Update](https://github.com/PurpleHaze2320/ai-agent-pulse/actions/workflows/track.yml/badge.svg)](https://github.com/PurpleHaze2320/ai-agent-pulse/actions/workflows/track.yml)
[![Frameworks Tracked](https://img.shields.io/badge/frameworks-19-blue)](https://github.com/PurpleHaze2320/ai-agent-pulse)
[![License: MIT](https://img.shields.io/badge/License-MIT-green.svg)](https://opensource.org/licenses/MIT)
[![GitHub stars](https://img.shields.io/github/stars/PurpleHaze2320/ai-agent-pulse?style=social)](https://github.com/PurpleHaze2320/ai-agent-pulse/stargazers)

> Automated daily tracking of the AI agent framework ecosystem's health, momentum, and trends.
> Last updated: **2026-04-28 08:33 UTC** | Tracking **19** frameworks

## How It Works

This bot runs daily via GitHub Actions and collects metrics from the GitHub API for the most important
AI agent frameworks. It computes a **Pulse Score** (0-100) based on six weighted signals: star velocity,
release freshness, issue health, commit activity, community size, and fork engagement. The result is
a living dashboard that shows which frameworks are gaining momentum and which are losing steam.

## 🏆 Pulse Leaderboard

| Rank | Framework | Pulse | Stars | ⭐ 7d | Commits (4w) | Last Release | Category |
|------|-----------|-------|-------|-------|--------------|--------------|----------|
| 1 | [Mastra](https://github.com/mastra-ai/mastra) | 🟢 **75.5** | 23.4k | 🚀 +200 | 650 | 3 days ago | `typescript` |
| 2 | [OpenAI Agents SDK](https://github.com/openai/openai-agents-python) | 🟢 **70.7** | 25.5k | 🚀 +1289 | 0 | today | `orchestration` |
| 3 | [CrewAI](https://github.com/crewAIInc/crewAI) | 🟢 **70.5** | 50.1k | 🚀 +764 | 0 | 3 days ago | `multi-agent` |
| 4 | [LangGraph](https://github.com/langchain-ai/langgraph) | 🟡 **69.2** | 30.6k | 🚀 +814 | 0 | today | `orchestration` |
| 5 | [BrowserUse](https://github.com/browser-use/browser-use) | 🟡 **68.7** | 90.9k | 🚀 +1782 | 0 | 26 days ago | `web-agent` |
| 6 | [Composio](https://github.com/ComposioHQ/composio) | 🟡 **65.2** | 27.9k | 📈 +96 | 222 | today | `tooling` |
| 7 | [Claude Agent SDK](https://github.com/anthropics/claude-code) | 🟡 **64.7** | 118.7k | 🚀 +2256 | 0 | today | `orchestration` |
| 8 | [LlamaIndex](https://github.com/run-llama/llama_index) | 🟡 **61.3** | 49.0k | 🚀 +252 | 0 | 7 days ago | `data-agent` |
| 9 | [PydanticAI](https://github.com/pydantic/pydantic-ai) | 🟡 **54.4** | 16.7k | 🚀 +178 | 0 | 3 days ago | `structured` |
| 10 | [Agno](https://github.com/agno-agi/agno) | 🟡 **54.2** | 39.7k | 🚀 +163 | 0 | today | `multi-agent` |
| 11 | [Google ADK](https://github.com/google/adk-python) | 🟡 **52.4** | 19.3k | 🚀 +170 | 0 | 5 days ago | `orchestration` |
| 12 | [DSPy](https://github.com/stanfordnlp/dspy) | 🟡 **51.0** | 34.0k | 🚀 +160 | 0 | 6 days ago | `optimization` |
| 13 | [Semantic Kernel](https://github.com/microsoft/semantic-kernel) | 🟡 **50.9** | 27.8k | 📈 +49 | 0 | today | `enterprise` |
| 14 | [Haystack](https://github.com/deepset-ai/haystack) | 🟡 **49.5** | 25.0k | 📈 +81 | 0 | 7 days ago | `pipeline` |
| 15 | [AG2](https://github.com/ag2ai/ag2) | 🟡 **48.3** | 4.5k | 📈 +29 | 0 | 3 days ago | `multi-agent` |
| 16 | [Letta](https://github.com/letta-ai/letta) | 🟡 **46.6** | 22.3k | 🚀 +146 | 0 | 27 days ago | `memory` |
| 17 | [AutoGen](https://github.com/microsoft/autogen) | 🟡 **45.8** | 57.5k | 🚀 +255 | 0 | 7 mo ago | `multi-agent` |
| 18 | [Smolagents](https://github.com/huggingface/smolagents) | 🟠 **39.1** | 26.9k | 🚀 +174 | 0 | 3 mo ago | `lightweight` |
| 19 | [Swarm](https://github.com/openai/swarm) | 🔴 **9.8** | 21.4k | 📈 +40 | 0 | — | `experimental` |

## 📂 By Category

- `data-agent`: **LlamaIndex** (61.3)
- `enterprise`: **Semantic Kernel** (50.9)
- `experimental`: **Swarm** (9.8)
- `lightweight`: **Smolagents** (39.1)
- `memory`: **Letta** (46.6)
- `multi-agent`: **CrewAI** (70.5), **Agno** (54.2), **AG2** (48.3), **AutoGen** (45.8)
- `optimization`: **DSPy** (51.0)
- `orchestration`: **OpenAI Agents SDK** (70.7), **LangGraph** (69.2), **Claude Agent SDK** (64.7), **Google ADK** (52.4)
- `pipeline`: **Haystack** (49.5)
- `structured`: **PydanticAI** (54.4)
- `tooling`: **Composio** (65.2)
- `typescript`: **Mastra** (75.5)
- `web-agent`: **BrowserUse** (68.7)

## 🔍 Top 5 — Score Breakdown

| Framework | Star Velocity | Release Freshness | Issue Health | Commit Activity | Community | Fork Ratio |
|-----------|:---:|:---:|:---:|:---:|:---:|:---:|
| **Mastra** | 40.1 | 99.0 | 94.6 | 100 | 80.8 | 33.7 |
| **OpenAI Agents SDK** | 100 | 100.0 | 96.4 | 0.0 | 51.8 | 61.0 |
| **CrewAI** | 100 | 99.0 | 95.9 | 0.0 | 57.8 | 55.0 |
| **LangGraph** | 100 | 100.0 | 79.0 | 0.0 | 54.8 | 68.4 |
| **BrowserUse** | 100 | 91.3 | 97.5 | 0.0 | 62.2 | 45.6 |

## 💡 Key Insights

- **Hottest framework**: Mastra with a Pulse Score of 75.5
- **Fastest growing**: Claude Agent SDK gained +2256 stars this week
- **Most active development**: Mastra with 650 commits in the last 4 weeks
- **Stale releases**: Swarm haven't released in a while

## 📦 Recent Releases

- **OpenAI Agents SDK** [`v0.14.7`](https://github.com/openai/openai-agents-python/releases/tag/v0.14.7) — today
- **Composio** [`py@0.12.0`](https://github.com/ComposioHQ/composio/releases/tag/py@0.12.0) — today
- **Semantic Kernel** [`python-1.41.3`](https://github.com/microsoft/semantic-kernel/releases/tag/python-1.41.3) — today
- **Agno** [`v2.6.3`](https://github.com/agno-agi/agno/releases/tag/v2.6.3) — today
- **Claude Agent SDK** [`v2.1.121`](https://github.com/anthropics/claude-code/releases/tag/v2.1.121) — today
- **LangGraph** [`1.1.10`](https://github.com/langchain-ai/langgraph/releases/tag/1.1.10) — today
- **PydanticAI** [`v1.87.0`](https://github.com/pydantic/pydantic-ai/releases/tag/v1.87.0) — 3 days ago
- **AG2** [`v0.12.1`](https://github.com/ag2ai/ag2/releases/tag/v0.12.1) — 3 days ago
- **CrewAI** [`1.14.3`](https://github.com/crewAIInc/crewAI/releases/tag/1.14.3) — 3 days ago
- **Mastra** [`@mastra/core@1.27.0`](https://github.com/mastra-ai/mastra/releases/tag/@mastra/core@1.27.0) — 3 days ago

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

*Powered by GitHub Actions • Data refreshed daily • Last run: 2026-04-28 08:33 UTC*