# 🔬 AI Agent Framework Pulse Tracker

[![Daily Update](https://github.com/PurpleHaze2320/ai-agent-pulse/actions/workflows/track.yml/badge.svg)](https://github.com/PurpleHaze2320/ai-agent-pulse/actions/workflows/track.yml)
[![Frameworks Tracked](https://img.shields.io/badge/frameworks-19-blue)](https://github.com/PurpleHaze2320/ai-agent-pulse)
[![License: MIT](https://img.shields.io/badge/License-MIT-green.svg)](https://opensource.org/licenses/MIT)
[![GitHub stars](https://img.shields.io/github/stars/PurpleHaze2320/ai-agent-pulse?style=social)](https://github.com/PurpleHaze2320/ai-agent-pulse/stargazers)

> Automated daily tracking of the AI agent framework ecosystem's health, momentum, and trends.
> Last updated: **2026-09-16 11:13 UTC** | Tracking **19** frameworks

## How It Works

This bot runs daily via GitHub Actions and collects metrics from the GitHub API for the most important
AI agent frameworks. It computes a **Pulse Score** (0-100) based on six weighted signals: star velocity,
release freshness, issue health, commit activity, community size, and fork engagement. The result is
a living dashboard that shows which frameworks are gaining momentum and which are losing steam.

## 🏆 Pulse Leaderboard

| Rank | Framework | Pulse | Stars | ⭐ 7d | Commits (4w) | Last Release | Category |
|------|-----------|-------|-------|-------|--------------|--------------|----------|
| 1 | [BrowserUse](https://github.com/browser-use/browser-use) | 🟢 **89.6** | 114.8k | 🚀 +915 | 204 | 12 days ago | `web-agent` |
| 2 | [Claude Agent SDK](https://github.com/anthropics/claude-code) | 🟢 **85.6** | 145.2k | 🚀 +729 | 104 | today | `orchestration` |
| 3 | [CrewAI](https://github.com/crewAIInc/crewAI) | 🟢 **84.7** | 58.6k | 🚀 +372 | 108 | 6 days ago | `multi-agent` |
| 4 | [Mastra](https://github.com/mastra-ai/mastra) | 🟢 **79.9** | 28.1k | 🚀 +262 | 1481 | today | `typescript` |
| 5 | [OpenAI Agents SDK](https://github.com/openai/openai-agents-python) | 🟢 **78.1** | 29.5k | 🚀 +193 | 110 | 6 days ago | `orchestration` |
| 6 | [PydanticAI](https://github.com/pydantic/pydantic-ai) | 🟢 **74.5** | 20.0k | 🚀 +153 | 211 | 4 days ago | `structured` |
| 7 | [Google ADK](https://github.com/google/adk-python) | 🟢 **74.2** | 21.6k | 📈 +89 | 372 | today | `orchestration` |
| 8 | [Haystack](https://github.com/deepset-ai/haystack) | 🟢 **71.0** | 26.5k | 📈 +69 | 184 | 13 days ago | `pipeline` |
| 9 | [Agno](https://github.com/agno-agi/agno) | 🟢 **70.1** | 42.2k | 📈 +87 | 106 | 7 days ago | `multi-agent` |
| 10 | [LangGraph](https://github.com/langchain-ai/langgraph) | 🟡 **69.8** | 41.8k | 🚀 +447 | 30 | 19 days ago | `orchestration` |
| 11 | [Composio](https://github.com/ComposioHQ/composio) | 🟡 **67.4** | 30.2k | 📈 +90 | 258 | today | `tooling` |
| 12 | [DSPy](https://github.com/stanfordnlp/dspy) | 🟡 **62.7** | 38.1k | 🚀 +190 | 49 | 4 days ago | `optimization` |
| 13 | [LlamaIndex](https://github.com/run-llama/llama_index) | 🟡 **60.0** | 52.2k | 📈 +98 | 31 | 27 days ago | `data-agent` |
| 14 | [AG2](https://github.com/ag2ai/ag2) | 🟡 **58.3** | 4.9k | ↗️ +16 | 43 | 4 days ago | `multi-agent` |
| 15 | [Semantic Kernel](https://github.com/microsoft/semantic-kernel) | 🟡 **53.5** | 28.6k | ↗️ +15 | 20 | 12 days ago | `enterprise` |
| 16 | [Letta](https://github.com/letta-ai/letta) | 🟠 **39.2** | 24.8k | 📈 +88 | 3 | 4 mo ago | `memory` |
| 17 | [Smolagents](https://github.com/huggingface/smolagents) | 🟠 **35.5** | 29.3k | 📈 +95 | 0 | 3 mo ago | `lightweight` |
| 18 | [AutoGen](https://github.com/microsoft/autogen) | 🟠 **33.3** | 61.0k | 🚀 +115 | 0 | 11 mo ago | `multi-agent` |
| 19 | [Swarm](https://github.com/openai/swarm) | 🔴 **9.6** | 22.0k | 📈 +23 | 0 | — | `experimental` |

## 📂 By Category

- `data-agent`: **LlamaIndex** (60.0)
- `enterprise`: **Semantic Kernel** (53.5)
- `experimental`: **Swarm** (9.6)
- `lightweight`: **Smolagents** (35.5)
- `memory`: **Letta** (39.2)
- `multi-agent`: **CrewAI** (84.7), **Agno** (70.1), **AG2** (58.3), **AutoGen** (33.3)
- `optimization`: **DSPy** (62.7)
- `orchestration`: **Claude Agent SDK** (85.6), **OpenAI Agents SDK** (78.1), **Google ADK** (74.2), **LangGraph** (69.8)
- `pipeline`: **Haystack** (71.0)
- `structured`: **PydanticAI** (74.5)
- `tooling`: **Composio** (67.4)
- `typescript`: **Mastra** (79.9)
- `web-agent`: **BrowserUse** (89.6)

## 🔍 Top 5 — Score Breakdown

| Framework | Star Velocity | Release Freshness | Issue Health | Commit Activity | Community | Fork Ratio |
|-----------|:---:|:---:|:---:|:---:|:---:|:---:|
| **BrowserUse** | 100 | 96.0 | 92.0 | 100 | 72.2 | 44.0 |
| **Claude Agent SDK** | 100 | 100.0 | 87.3 | 100 | 10.8 | 64.4 |
| **CrewAI** | 74.0 | 98.0 | 94.5 | 100 | 66.0 | 57.8 |
| **Mastra** | 49.6 | 100.0 | 95.2 | 100 | 92.8 | 39.8 |
| **OpenAI Agents SDK** | 38.8 | 98.0 | 98.4 | 100 | 75.6 | 64.4 |

## 💡 Key Insights

- **Hottest framework**: BrowserUse with a Pulse Score of 89.6
- **Fastest growing**: BrowserUse gained +915 stars this week
- **Most active development**: Mastra with 1481 commits in the last 4 weeks
- **Stale releases**: AutoGen, Swarm haven't released in a while

## 📦 Recent Releases

- **Claude Agent SDK** [`v2.1.273`](https://github.com/anthropics/claude-code/releases/tag/v2.1.273) — today
- **Google ADK** [`v2.9.1`](https://github.com/google/adk-python/releases/tag/v2.9.1) — today
- **Mastra** [`@mastra/core@1.67.0`](https://github.com/mastra-ai/mastra/releases/tag/@mastra/core@1.67.0) — today
- **Composio** [`@composio/cli@0.4.2-beta.394`](https://github.com/ComposioHQ/composio/releases/tag/@composio/cli@0.4.2-beta.394) — today *(pre-release)*
- **PydanticAI** [`v2.43.0`](https://github.com/pydantic/pydantic-ai/releases/tag/v2.43.0) — 4 days ago
- **DSPy** [`3.4.0b1`](https://github.com/stanfordnlp/dspy/releases/tag/3.4.0b1) — 4 days ago *(pre-release)*
- **AG2** [`v1.0.5`](https://github.com/ag2ai/ag2/releases/tag/v1.0.5) — 4 days ago
- **CrewAI** [`1.15.21`](https://github.com/crewAIInc/crewAI/releases/tag/1.15.21) — 6 days ago
- **OpenAI Agents SDK** [`v0.22.2`](https://github.com/openai/openai-agents-python/releases/tag/v0.22.2) — 6 days ago
- **Agno** [`v3.0.9`](https://github.com/agno-agi/agno/releases/tag/v3.0.9) — 7 days ago

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

*Powered by GitHub Actions • Data refreshed daily • Last run: 2026-09-16 11:13 UTC*