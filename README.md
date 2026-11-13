# 🔬 AI Agent Framework Pulse Tracker

[![Daily Update](https://github.com/PurpleHaze2320/ai-agent-pulse/actions/workflows/track.yml/badge.svg)](https://github.com/PurpleHaze2320/ai-agent-pulse/actions/workflows/track.yml)
[![Frameworks Tracked](https://img.shields.io/badge/frameworks-19-blue)](https://github.com/PurpleHaze2320/ai-agent-pulse)
[![License: MIT](https://img.shields.io/badge/License-MIT-green.svg)](https://opensource.org/licenses/MIT)
[![GitHub stars](https://img.shields.io/github/stars/PurpleHaze2320/ai-agent-pulse?style=social)](https://github.com/PurpleHaze2320/ai-agent-pulse/stargazers)

> Automated daily tracking of the AI agent framework ecosystem's health, momentum, and trends.
> Last updated: **2026-11-13 14:20 UTC** | Tracking **19** frameworks

## How It Works

This bot runs daily via GitHub Actions and collects metrics from the GitHub API for the most important
AI agent frameworks. It computes a **Pulse Score** (0-100) based on six weighted signals: star velocity,
release freshness, issue health, commit activity, community size, and fork engagement. The result is
a living dashboard that shows which frameworks are gaining momentum and which are losing steam.

## 🏆 Pulse Leaderboard

| Rank | Framework | Pulse | Stars | ⭐ 7d | Commits (4w) | Last Release | Category |
|------|-----------|-------|-------|-------|--------------|--------------|----------|
| 1 | [BrowserUse](https://github.com/browser-use/browser-use) | 🟢 **90.3** | 120.9k | 🚀 +725 | 1103 | today | `web-agent` |
| 2 | [LangGraph](https://github.com/langchain-ai/langgraph) | 🟢 **82.8** | 44.9k | 🚀 +341 | 119 | today | `orchestration` |
| 3 | [CrewAI](https://github.com/crewAIInc/crewAI) | 🟢 **80.2** | 60.8k | 🚀 +285 | 212 | today | `multi-agent` |
| 4 | [Claude Agent SDK](https://github.com/anthropics/claude-code) | 🟢 **75.2** | 155.5k | 🚀 +769 | 50 | today | `orchestration` |
| 5 | [Mastra](https://github.com/mastra-ai/mastra) | 🟢 **74.0** | 29.5k | 🚀 +125 | 2504 | 9 days ago | `typescript` |
| 6 | [Haystack](https://github.com/deepset-ai/haystack) | 🟢 **72.1** | 27.0k | 📈 +68 | 266 | 3 days ago | `pipeline` |
| 7 | [Agno](https://github.com/agno-agi/agno) | 🟢 **70.6** | 43.2k | 🚀 +102 | 161 | today | `multi-agent` |
| 8 | [OpenAI Agents SDK](https://github.com/openai/openai-agents-python) | 🟢 **70.4** | 30.6k | 🚀 +121 | 74 | 5 days ago | `orchestration` |
| 9 | [AG2](https://github.com/ag2ai/ag2) | 🟢 **70.1** | 5.1k | ↗️ +14 | 128 | 2 days ago | `multi-agent` |
| 10 | [Semantic Kernel](https://github.com/microsoft/semantic-kernel) | 🟡 **69.0** | 28.8k | 📈 +23 | 89 | 6 days ago | `enterprise` |
| 11 | [Composio](https://github.com/ComposioHQ/composio) | 🟡 **68.2** | 31.1k | 🚀 +108 | 326 | today | `tooling` |
| 12 | [DSPy](https://github.com/stanfordnlp/dspy) | 🟡 **66.0** | 39.0k | 📈 +68 | 92 | 2 days ago | `optimization` |
| 13 | [Google ADK](https://github.com/google/adk-python) | 🟡 **54.7** | 22.2k | 📈 +78 | 0 | today | `orchestration` |
| 14 | [LlamaIndex](https://github.com/run-llama/llama_index) | 🟡 **51.4** | 52.9k | 📈 +62 | 5 | 1 mo ago | `data-agent` |
| 15 | [PydanticAI](https://github.com/pydantic/pydantic-ai) | 🟡 **50.7** | 21.2k | 🚀 +134 | 0 | 1 mo ago | `structured` |
| 16 | [Letta](https://github.com/letta-ai/letta) | 🟠 **33.3** | 25.4k | 📈 +61 | 1 | 6 mo ago | `memory` |
| 17 | [AutoGen](https://github.com/microsoft/autogen) | 🟠 **31.7** | 61.8k | 📈 +73 | 2 | 1y ago | `multi-agent` |
| 18 | [Smolagents](https://github.com/huggingface/smolagents) | 🟠 **31.6** | 30.4k | 🚀 +121 | 0 | 5 mo ago | `lightweight` |
| 19 | [Swarm](https://github.com/openai/swarm) | 🔴 **9.5** | 22.1k | 📈 +24 | 0 | — | `experimental` |

## 📂 By Category

- `data-agent`: **LlamaIndex** (51.4)
- `enterprise`: **Semantic Kernel** (69.0)
- `experimental`: **Swarm** (9.5)
- `lightweight`: **Smolagents** (31.6)
- `memory`: **Letta** (33.3)
- `multi-agent`: **CrewAI** (80.2), **Agno** (70.6), **AG2** (70.1), **AutoGen** (31.7)
- `optimization`: **DSPy** (66.0)
- `orchestration`: **LangGraph** (82.8), **Claude Agent SDK** (75.2), **OpenAI Agents SDK** (70.4), **Google ADK** (54.7)
- `pipeline`: **Haystack** (72.1)
- `structured`: **PydanticAI** (50.7)
- `tooling`: **Composio** (68.2)
- `typescript`: **Mastra** (74.0)
- `web-agent`: **BrowserUse** (90.3)

## 🔍 Top 5 — Score Breakdown

| Framework | Star Velocity | Release Freshness | Issue Health | Commit Activity | Community | Fork Ratio |
|-----------|:---:|:---:|:---:|:---:|:---:|:---:|
| **BrowserUse** | 100 | 100.0 | 90.3 | 100 | 72.4 | 44.7 |
| **LangGraph** | 72.5 | 100.0 | 80.1 | 100 | 57.6 | 69.0 |
| **CrewAI** | 57.5 | 100.0 | 83.0 | 100 | 73.6 | 60.3 |
| **Claude Agent SDK** | 100 | 100.0 | 84.5 | 50.0 | 11.2 | 64.2 |
| **Mastra** | 27.9 | 97.0 | 94.3 | 100 | 93.2 | 42.0 |

## 💡 Key Insights

- **Hottest framework**: BrowserUse with a Pulse Score of 90.3
- **Fastest growing**: Claude Agent SDK gained +769 stars this week
- **Most active development**: Mastra with 2504 commits in the last 4 weeks
- **Stale releases**: AutoGen, Swarm haven't released in a while

## 📦 Recent Releases

- **Composio** [`@composio/cli@0.6.1-beta.548`](https://github.com/ComposioHQ/composio/releases/tag/@composio/cli@0.6.1-beta.548) — today *(pre-release)*
- **Claude Agent SDK** [`v2.1.323`](https://github.com/anthropics/claude-code/releases/tag/v2.1.323) — today
- **Google ADK** [`v2.14.1`](https://github.com/google/adk-python/releases/tag/v2.14.1) — today
- **CrewAI** [`1.15.41`](https://github.com/crewAIInc/crewAI/releases/tag/1.15.41) — today
- **LangGraph** [`1.2.21`](https://github.com/langchain-ai/langgraph/releases/tag/1.2.21) — today
- **Agno** [`v3.2.0`](https://github.com/agno-agi/agno/releases/tag/v3.2.0) — today
- **BrowserUse** [`1.0.3`](https://github.com/browser-use/browser-use/releases/tag/1.0.3) — today
- **AG2** [`v.1.3.1`](https://github.com/ag2ai/ag2/releases/tag/v.1.3.1) — 2 days ago
- **DSPy** [`3.5.0`](https://github.com/stanfordnlp/dspy/releases/tag/3.5.0) — 2 days ago
- **Haystack** [`v3.5.0`](https://github.com/deepset-ai/haystack/releases/tag/v3.5.0) — 3 days ago

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

*Powered by GitHub Actions • Data refreshed daily • Last run: 2026-11-13 14:20 UTC*