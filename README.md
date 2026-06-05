# 🔬 AI Agent Framework Pulse Tracker

[![Daily Update](https://github.com/PurpleHaze2320/ai-agent-pulse/actions/workflows/track.yml/badge.svg)](https://github.com/PurpleHaze2320/ai-agent-pulse/actions/workflows/track.yml)
[![Frameworks Tracked](https://img.shields.io/badge/frameworks-19-blue)](https://github.com/PurpleHaze2320/ai-agent-pulse)
[![License: MIT](https://img.shields.io/badge/License-MIT-green.svg)](https://opensource.org/licenses/MIT)
[![GitHub stars](https://img.shields.io/github/stars/PurpleHaze2320/ai-agent-pulse?style=social)](https://github.com/PurpleHaze2320/ai-agent-pulse/stargazers)

> Automated daily tracking of the AI agent framework ecosystem's health, momentum, and trends.
> Last updated: **2026-06-05 10:01 UTC** | Tracking **19** frameworks

## How It Works

This bot runs daily via GitHub Actions and collects metrics from the GitHub API for the most important
AI agent frameworks. It computes a **Pulse Score** (0-100) based on six weighted signals: star velocity,
release freshness, issue health, commit activity, community size, and fork engagement. The result is
a living dashboard that shows which frameworks are gaining momentum and which are losing steam.

## 🏆 Pulse Leaderboard

| Rank | Framework | Pulse | Stars | ⭐ 7d | Commits (4w) | Last Release | Category |
|------|-----------|-------|-------|-------|--------------|--------------|----------|
| 1 | [LangGraph](https://github.com/langchain-ai/langgraph) | 🟢 **88.5** | 34.0k | 🚀 +653 | 103 | 2 days ago | `orchestration` |
| 2 | [CrewAI](https://github.com/crewAIInc/crewAI) | 🟢 **88.5** | 52.9k | 🚀 +461 | 92 | 1 day ago | `multi-agent` |
| 3 | [Mastra](https://github.com/mastra-ai/mastra) | 🟢 **81.2** | 24.8k | 🚀 +277 | 952 | today | `typescript` |
| 4 | [BrowserUse](https://github.com/browser-use/browser-use) | 🟢 **78.5** | 97.3k | 🚀 +1162 | 45 | 10 days ago | `web-agent` |
| 5 | [PydanticAI](https://github.com/pydantic/pydantic-ai) | 🟢 **74.8** | 17.5k | 🚀 +163 | 117 | today | `structured` |
| 6 | [Agno](https://github.com/agno-agi/agno) | 🟢 **72.6** | 40.5k | 🚀 +113 | 146 | 2 days ago | `multi-agent` |
| 7 | [Claude Agent SDK](https://github.com/anthropics/claude-code) | 🟢 **71.8** | 130.3k | 🚀 +2765 | 31 | today | `orchestration` |
| 8 | [OpenAI Agents SDK](https://github.com/openai/openai-agents-python) | 🟢 **71.5** | 26.9k | 🚀 +194 | 78 | 10 days ago | `orchestration` |
| 9 | [Google ADK](https://github.com/google/adk-python) | 🟢 **70.2** | 20.0k | 📈 +87 | 176 | today | `orchestration` |
| 10 | [Haystack](https://github.com/deepset-ai/haystack) | 🟡 **69.5** | 25.5k | 📈 +56 | 129 | 1 day ago | `pipeline` |
| 11 | [LlamaIndex](https://github.com/run-llama/llama_index) | 🟡 **68.5** | 49.9k | 🚀 +181 | 53 | 21 days ago | `data-agent` |
| 12 | [Composio](https://github.com/ComposioHQ/composio) | 🟡 **61.8** | 28.6k | 🚀 +127 | 74 | 16 days ago | `tooling` |
| 13 | [DSPy](https://github.com/stanfordnlp/dspy) | 🟡 **59.5** | 34.9k | 🚀 +139 | 46 | 8 days ago | `optimization` |
| 14 | [Semantic Kernel](https://github.com/microsoft/semantic-kernel) | 🟡 **54.2** | 28.1k | 📈 +52 | 13 | 1 day ago | `enterprise` |
| 15 | [AG2](https://github.com/ag2ai/ag2) | 🟡 **49.0** | 4.6k | 📈 +30 | 0 | today | `multi-agent` |
| 16 | [Letta](https://github.com/letta-ai/letta) | 🟡 **47.4** | 23.2k | 🚀 +123 | 1 | 21 days ago | `memory` |
| 17 | [Smolagents](https://github.com/huggingface/smolagents) | 🟡 **46.5** | 27.7k | 🚀 +136 | 10 | 7 days ago | `lightweight` |
| 18 | [AutoGen](https://github.com/microsoft/autogen) | 🟡 **41.0** | 58.7k | 🚀 +192 | 0 | 8 mo ago | `multi-agent` |
| 19 | [Swarm](https://github.com/openai/swarm) | 🔴 **9.3** | 21.6k | 📈 +33 | 0 | — | `experimental` |

## 📂 By Category

- `data-agent`: **LlamaIndex** (68.5)
- `enterprise`: **Semantic Kernel** (54.2)
- `experimental`: **Swarm** (9.3)
- `lightweight`: **Smolagents** (46.5)
- `memory`: **Letta** (47.4)
- `multi-agent`: **CrewAI** (88.5), **Agno** (72.6), **AG2** (49.0), **AutoGen** (41.0)
- `optimization`: **DSPy** (59.5)
- `orchestration`: **LangGraph** (88.5), **Claude Agent SDK** (71.8), **OpenAI Agents SDK** (71.5), **Google ADK** (70.2)
- `pipeline`: **Haystack** (69.5)
- `structured`: **PydanticAI** (74.8)
- `tooling`: **Composio** (61.8)
- `typescript`: **Mastra** (81.2)
- `web-agent`: **BrowserUse** (78.5)

## 🔍 Top 5 — Score Breakdown

| Framework | Star Velocity | Release Freshness | Issue Health | Commit Activity | Community | Fork Ratio |
|-----------|:---:|:---:|:---:|:---:|:---:|:---:|
| **LangGraph** | 100 | 99.3 | 75.9 | 100 | 55.0 | 67.2 |
| **CrewAI** | 95.9 | 99.7 | 97.9 | 92.0 | 59.4 | 55.8 |
| **Mastra** | 56.2 | 100.0 | 95.6 | 100 | 92.2 | 35.5 |
| **BrowserUse** | 100 | 96.7 | 95.8 | 45.0 | 63.0 | 44.7 |
| **PydanticAI** | 32.6 | 100.0 | 82.8 | 100 | 92.2 | 49.6 |

## 💡 Key Insights

- **Hottest framework**: LangGraph with a Pulse Score of 88.5
- **Fastest growing**: Claude Agent SDK gained +2765 stars this week
- **Most active development**: Mastra with 952 commits in the last 4 weeks
- **Stale releases**: Swarm haven't released in a while

## 📦 Recent Releases

- **Mastra** [`@mastra/core@1.41.0`](https://github.com/mastra-ai/mastra/releases/tag/@mastra/core@1.41.0) — today
- **AG2** [`v0.13.3`](https://github.com/ag2ai/ag2/releases/tag/v0.13.3) — today
- **Claude Agent SDK** [`v2.1.165`](https://github.com/anthropics/claude-code/releases/tag/v2.1.165) — today
- **PydanticAI** [`v2.0.0b6`](https://github.com/pydantic/pydantic-ai/releases/tag/v2.0.0b6) — today *(pre-release)*
- **Google ADK** [`v2.2.0`](https://github.com/google/adk-python/releases/tag/v2.2.0) — today
- **Semantic Kernel** [`python-1.43.0`](https://github.com/microsoft/semantic-kernel/releases/tag/python-1.43.0) — 1 day ago
- **CrewAI** [`1.14.7a1`](https://github.com/crewAIInc/crewAI/releases/tag/1.14.7a1) — 1 day ago *(pre-release)*
- **Haystack** [`v2.30.0`](https://github.com/deepset-ai/haystack/releases/tag/v2.30.0) — 1 day ago
- **LangGraph** [`1.2.4`](https://github.com/langchain-ai/langgraph/releases/tag/1.2.4) — 2 days ago
- **Agno** [`v2.6.11`](https://github.com/agno-agi/agno/releases/tag/v2.6.11) — 2 days ago

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

*Powered by GitHub Actions • Data refreshed daily • Last run: 2026-06-05 10:01 UTC*