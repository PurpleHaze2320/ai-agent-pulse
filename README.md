# 🔬 AI Agent Framework Pulse Tracker

[![Daily Update](https://github.com/PurpleHaze2320/ai-agent-pulse/actions/workflows/track.yml/badge.svg)](https://github.com/PurpleHaze2320/ai-agent-pulse/actions/workflows/track.yml)
[![Frameworks Tracked](https://img.shields.io/badge/frameworks-19-blue)](https://github.com/PurpleHaze2320/ai-agent-pulse)
[![License: MIT](https://img.shields.io/badge/License-MIT-green.svg)](https://opensource.org/licenses/MIT)
[![GitHub stars](https://img.shields.io/github/stars/PurpleHaze2320/ai-agent-pulse?style=social)](https://github.com/PurpleHaze2320/ai-agent-pulse/stargazers)

> Automated daily tracking of the AI agent framework ecosystem's health, momentum, and trends.
> Last updated: **2026-07-12 08:25 UTC** | Tracking **19** frameworks

## How It Works

This bot runs daily via GitHub Actions and collects metrics from the GitHub API for the most important
AI agent frameworks. It computes a **Pulse Score** (0-100) based on six weighted signals: star velocity,
release freshness, issue health, commit activity, community size, and fork engagement. The result is
a living dashboard that shows which frameworks are gaining momentum and which are losing steam.

## 🏆 Pulse Leaderboard

| Rank | Framework | Pulse | Stars | ⭐ 7d | Commits (4w) | Last Release | Category |
|------|-----------|-------|-------|-------|--------------|--------------|----------|
| 1 | [CrewAI](https://github.com/crewAIInc/crewAI) | 🟢 **85.0** | 55.4k | 🚀 +445 | 80 | 4 days ago | `multi-agent` |
| 2 | [BrowserUse](https://github.com/browser-use/browser-use) | 🟢 **83.9** | 104.3k | 🚀 +1508 | 70 | today | `web-agent` |
| 3 | [Mastra](https://github.com/mastra-ai/mastra) | 🟢 **79.4** | 26.1k | 🚀 +238 | 882 | 3 days ago | `typescript` |
| 4 | [OpenAI Agents SDK](https://github.com/openai/openai-agents-python) | 🟢 **75.6** | 27.8k | 🚀 +173 | 102 | 1 day ago | `orchestration` |
| 5 | [LangGraph](https://github.com/langchain-ai/langgraph) | 🟢 **75.0** | 37.1k | 🚀 +575 | 35 | 2 days ago | `orchestration` |
| 6 | [Google ADK](https://github.com/google/adk-python) | 🟢 **72.7** | 20.6k | 🚀 +108 | 266 | 4 days ago | `orchestration` |
| 7 | [Claude Agent SDK](https://github.com/anthropics/claude-code) | 🟡 **69.5** | 137.5k | 🚀 +1370 | 21 | 1 day ago | `orchestration` |
| 8 | [Composio](https://github.com/ComposioHQ/composio) | 🟡 **67.0** | 29.2k | 📈 +100 | 110 | 4 days ago | `tooling` |
| 9 | [LlamaIndex](https://github.com/run-llama/llama_index) | 🟡 **61.6** | 50.8k | 🚀 +141 | 25 | 17 days ago | `data-agent` |
| 10 | [PydanticAI](https://github.com/pydantic/pydantic-ai) | 🟡 **57.4** | 18.4k | 🚀 +210 | 0 | 1 day ago | `structured` |
| 11 | [DSPy](https://github.com/stanfordnlp/dspy) | 🟡 **52.1** | 36.1k | 🚀 +214 | 0 | 1 mo ago | `optimization` |
| 12 | [Agno](https://github.com/agno-agi/agno) | 🟡 **51.8** | 41.1k | 🚀 +109 | 0 | 2 days ago | `multi-agent` |
| 13 | [Semantic Kernel](https://github.com/microsoft/semantic-kernel) | 🟡 **51.1** | 28.3k | 📈 +41 | 0 | 4 days ago | `enterprise` |
| 14 | [AG2](https://github.com/ag2ai/ag2) | 🟡 **49.8** | 4.8k | 📈 +25 | 0 | 8 days ago | `multi-agent` |
| 15 | [Haystack](https://github.com/deepset-ai/haystack) | 🟡 **49.6** | 25.9k | 📈 +48 | 0 | 3 days ago | `pipeline` |
| 16 | [Letta](https://github.com/letta-ai/letta) | 🟡 **43.2** | 23.7k | 📈 +94 | 2 | 1 mo ago | `memory` |
| 17 | [Smolagents](https://github.com/huggingface/smolagents) | 🟡 **41.6** | 28.3k | 🚀 +115 | 4 | 1 mo ago | `lightweight` |
| 18 | [AutoGen](https://github.com/microsoft/autogen) | 🟠 **37.1** | 59.7k | 🚀 +172 | 0 | 9 mo ago | `multi-agent` |
| 19 | [Swarm](https://github.com/openai/swarm) | 🔴 **9.2** | 21.8k | 📈 +24 | 0 | — | `experimental` |

## 📂 By Category

- `data-agent`: **LlamaIndex** (61.6)
- `enterprise`: **Semantic Kernel** (51.1)
- `experimental`: **Swarm** (9.2)
- `lightweight`: **Smolagents** (41.6)
- `memory`: **Letta** (43.2)
- `multi-agent`: **CrewAI** (85.0), **Agno** (51.8), **AG2** (49.8), **AutoGen** (37.1)
- `optimization`: **DSPy** (52.1)
- `orchestration`: **OpenAI Agents SDK** (75.6), **LangGraph** (75.0), **Google ADK** (72.7), **Claude Agent SDK** (69.5)
- `pipeline`: **Haystack** (49.6)
- `structured`: **PydanticAI** (57.4)
- `tooling`: **Composio** (67.0)
- `typescript`: **Mastra** (79.4)
- `web-agent`: **BrowserUse** (83.9)

## 🔍 Top 5 — Score Breakdown

| Framework | Star Velocity | Release Freshness | Issue Health | Commit Activity | Community | Fork Ratio |
|-----------|:---:|:---:|:---:|:---:|:---:|:---:|
| **CrewAI** | 93.2 | 98.7 | 95.8 | 80.0 | 59.6 | 56.4 |
| **BrowserUse** | 100 | 100.0 | 94.9 | 70.0 | 63.0 | 44.1 |
| **Mastra** | 49.5 | 99.0 | 94.9 | 100 | 92.6 | 36.8 |
| **OpenAI Agents SDK** | 35.1 | 99.7 | 98.0 | 100 | 60.0 | 61.8 |
| **LangGraph** | 100 | 99.3 | 73.0 | 35.0 | 55.0 | 67.1 |

## 💡 Key Insights

- **Hottest framework**: CrewAI with a Pulse Score of 85.0
- **Fastest growing**: BrowserUse gained +1508 stars this week
- **Most active development**: Mastra with 882 commits in the last 4 weeks
- **Stale releases**: AutoGen, Swarm haven't released in a while

## 📦 Recent Releases

- **BrowserUse** [`0.13.4`](https://github.com/browser-use/browser-use/releases/tag/0.13.4) — today
- **PydanticAI** [`v2.9.0`](https://github.com/pydantic/pydantic-ai/releases/tag/v2.9.0) — 1 day ago
- **OpenAI Agents SDK** [`v0.18.2`](https://github.com/openai/openai-agents-python/releases/tag/v0.18.2) — 1 day ago
- **Claude Agent SDK** [`v2.1.207`](https://github.com/anthropics/claude-code/releases/tag/v2.1.207) — 1 day ago
- **LangGraph** [`1.2.9`](https://github.com/langchain-ai/langgraph/releases/tag/1.2.9) — 2 days ago
- **Agno** [`v2.7.2`](https://github.com/agno-agi/agno/releases/tag/v2.7.2) — 2 days ago
- **Mastra** [`@mastra/core@1.50.0`](https://github.com/mastra-ai/mastra/releases/tag/@mastra/core@1.50.0) — 3 days ago
- **Haystack** [`v2.31.0`](https://github.com/deepset-ai/haystack/releases/tag/v2.31.0) — 3 days ago
- **CrewAI** [`1.15.2`](https://github.com/crewAIInc/crewAI/releases/tag/1.15.2) — 4 days ago
- **Google ADK** [`v2.4.0`](https://github.com/google/adk-python/releases/tag/v2.4.0) — 4 days ago

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

*Powered by GitHub Actions • Data refreshed daily • Last run: 2026-07-12 08:25 UTC*