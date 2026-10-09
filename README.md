# 🔬 AI Agent Framework Pulse Tracker

[![Daily Update](https://github.com/PurpleHaze2320/ai-agent-pulse/actions/workflows/track.yml/badge.svg)](https://github.com/PurpleHaze2320/ai-agent-pulse/actions/workflows/track.yml)
[![Frameworks Tracked](https://img.shields.io/badge/frameworks-19-blue)](https://github.com/PurpleHaze2320/ai-agent-pulse)
[![License: MIT](https://img.shields.io/badge/License-MIT-green.svg)](https://opensource.org/licenses/MIT)
[![GitHub stars](https://img.shields.io/github/stars/PurpleHaze2320/ai-agent-pulse?style=social)](https://github.com/PurpleHaze2320/ai-agent-pulse/stargazers)

> Automated daily tracking of the AI agent framework ecosystem's health, momentum, and trends.
> Last updated: **2026-10-09 12:54 UTC** | Tracking **19** frameworks

## How It Works

This bot runs daily via GitHub Actions and collects metrics from the GitHub API for the most important
AI agent frameworks. It computes a **Pulse Score** (0-100) based on six weighted signals: star velocity,
release freshness, issue health, commit activity, community size, and fork engagement. The result is
a living dashboard that shows which frameworks are gaining momentum and which are losing steam.

## 🏆 Pulse Leaderboard

| Rank | Framework | Pulse | Stars | ⭐ 7d | Commits (4w) | Last Release | Category |
|------|-----------|-------|-------|-------|--------------|--------------|----------|
| 1 | [Claude Agent SDK](https://github.com/anthropics/claude-code) | 🟢 **82.3** | 149.8k | 🚀 +886 | 82 | today | `orchestration` |
| 2 | [BrowserUse](https://github.com/browser-use/browser-use) | 🟢 **81.6** | 117.4k | 🚀 +391 | 58 | 2 days ago | `web-agent` |
| 3 | [Mastra](https://github.com/mastra-ai/mastra) | 🟢 **76.5** | 28.7k | 🚀 +164 | 2194 | 1 day ago | `typescript` |
| 4 | [OpenAI Agents SDK](https://github.com/openai/openai-agents-python) | 🟢 **76.1** | 29.9k | 🚀 +134 | 232 | 6 days ago | `orchestration` |
| 5 | [CrewAI](https://github.com/crewAIInc/crewAI) | 🟢 **75.7** | 59.5k | 🚀 +209 | 88 | today | `multi-agent` |
| 6 | [PydanticAI](https://github.com/pydantic/pydantic-ai) | 🟢 **73.7** | 20.5k | 🚀 +149 | 776 | 3 days ago | `structured` |
| 7 | [Google ADK](https://github.com/google/adk-python) | 🟢 **73.2** | 21.8k | 📈 +70 | 477 | 7 days ago | `orchestration` |
| 8 | [Agno](https://github.com/agno-agi/agno) | 🟢 **72.2** | 42.6k | 🚀 +139 | 117 | today | `multi-agent` |
| 9 | [Haystack](https://github.com/deepset-ai/haystack) | 🟢 **71.1** | 26.7k | 📈 +62 | 252 | 8 days ago | `pipeline` |
| 10 | [Composio](https://github.com/ComposioHQ/composio) | 🟡 **66.8** | 30.5k | 📈 +81 | 293 | today | `tooling` |
| 11 | [DSPy](https://github.com/stanfordnlp/dspy) | 🟡 **60.5** | 38.6k | 📈 +99 | 59 | 14 days ago | `optimization` |
| 12 | [LangGraph](https://github.com/langchain-ai/langgraph) | 🟡 **60.4** | 42.9k | 🚀 +341 | 0 | 1 day ago | `orchestration` |
| 13 | [LlamaIndex](https://github.com/run-llama/llama_index) | 🟡 **57.9** | 52.5k | 📈 +67 | 25 | 17 days ago | `data-agent` |
| 14 | [Semantic Kernel](https://github.com/microsoft/semantic-kernel) | 🟡 **53.7** | 28.6k | ↗️ +15 | 18 | 3 days ago | `enterprise` |
| 15 | [AG2](https://github.com/ag2ai/ag2) | 🟡 **49.5** | 5.0k | ↗️ +13 | 0 | 6 days ago | `multi-agent` |
| 16 | [Letta](https://github.com/letta-ai/letta) | 🟠 **36.6** | 25.1k | 📈 +82 | 0 | 4 mo ago | `memory` |
| 17 | [Smolagents](https://github.com/huggingface/smolagents) | 🟠 **34.8** | 29.8k | 🚀 +103 | 5 | 4 mo ago | `lightweight` |
| 18 | [AutoGen](https://github.com/microsoft/autogen) | 🟠 **31.2** | 61.3k | 📈 +67 | 0 | 1y ago | `multi-agent` |
| 19 | [Swarm](https://github.com/openai/swarm) | 🔴 **9.4** | 22.0k | ↗️ +16 | 0 | — | `experimental` |

## 📂 By Category

- `data-agent`: **LlamaIndex** (57.9)
- `enterprise`: **Semantic Kernel** (53.7)
- `experimental`: **Swarm** (9.4)
- `lightweight`: **Smolagents** (34.8)
- `memory`: **Letta** (36.6)
- `multi-agent`: **CrewAI** (75.7), **Agno** (72.2), **AG2** (49.5), **AutoGen** (31.2)
- `optimization`: **DSPy** (60.5)
- `orchestration`: **Claude Agent SDK** (82.3), **OpenAI Agents SDK** (76.1), **Google ADK** (73.2), **LangGraph** (60.4)
- `pipeline`: **Haystack** (71.1)
- `structured`: **PydanticAI** (73.7)
- `tooling`: **Composio** (66.8)
- `typescript`: **Mastra** (76.5)
- `web-agent`: **BrowserUse** (81.6)

## 🔍 Top 5 — Score Breakdown

| Framework | Star Velocity | Release Freshness | Issue Health | Commit Activity | Community | Fork Ratio |
|-----------|:---:|:---:|:---:|:---:|:---:|:---:|
| **Claude Agent SDK** | 100 | 100.0 | 85.8 | 82.0 | 11.4 | 69.1 |
| **BrowserUse** | 100 | 99.3 | 90.1 | 58.0 | 72.0 | 44.3 |
| **Mastra** | 35.4 | 99.7 | 95.2 | 100 | 93.6 | 41.1 |
| **OpenAI Agents SDK** | 28.3 | 98.0 | 99.5 | 100 | 80.2 | 64.9 |
| **CrewAI** | 47.5 | 100.0 | 90.6 | 88.0 | 68.4 | 58.3 |

## 💡 Key Insights

- **Hottest framework**: Claude Agent SDK with a Pulse Score of 82.3
- **Fastest growing**: Claude Agent SDK gained +886 stars this week
- **Most active development**: Mastra with 2194 commits in the last 4 weeks
- **Stale releases**: AutoGen, Swarm haven't released in a while

## 📦 Recent Releases

- **CrewAI** [`1.15.26`](https://github.com/crewAIInc/crewAI/releases/tag/1.15.26) — today
- **Agno** [`v3.1.2`](https://github.com/agno-agi/agno/releases/tag/v3.1.2) — today
- **Claude Agent SDK** [`v2.1.295`](https://github.com/anthropics/claude-code/releases/tag/v2.1.295) — today
- **Composio** [`@composio/cli@0.4.3-beta.418`](https://github.com/ComposioHQ/composio/releases/tag/@composio/cli@0.4.3-beta.418) — today *(pre-release)*
- **Mastra** [`@mastra/core@1.75.0`](https://github.com/mastra-ai/mastra/releases/tag/@mastra/core@1.75.0) — 1 day ago
- **LangGraph** [`cli==0.4.33`](https://github.com/langchain-ai/langgraph/releases/tag/cli==0.4.33) — 1 day ago
- **BrowserUse** [`0.13.11`](https://github.com/browser-use/browser-use/releases/tag/0.13.11) — 2 days ago
- **Semantic Kernel** [`python-1.45.0`](https://github.com/microsoft/semantic-kernel/releases/tag/python-1.45.0) — 3 days ago
- **PydanticAI** [`clai2-bleeding`](https://github.com/pydantic/pydantic-ai/releases/tag/clai2-bleeding) — 3 days ago *(pre-release)*
- **AG2** [`v1.1.2`](https://github.com/ag2ai/ag2/releases/tag/v1.1.2) — 6 days ago

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

*Powered by GitHub Actions • Data refreshed daily • Last run: 2026-10-09 12:54 UTC*