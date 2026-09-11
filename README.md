# 🔬 AI Agent Framework Pulse Tracker

[![Daily Update](https://github.com/PurpleHaze2320/ai-agent-pulse/actions/workflows/track.yml/badge.svg)](https://github.com/PurpleHaze2320/ai-agent-pulse/actions/workflows/track.yml)
[![Frameworks Tracked](https://img.shields.io/badge/frameworks-19-blue)](https://github.com/PurpleHaze2320/ai-agent-pulse)
[![License: MIT](https://img.shields.io/badge/License-MIT-green.svg)](https://opensource.org/licenses/MIT)
[![GitHub stars](https://img.shields.io/github/stars/PurpleHaze2320/ai-agent-pulse?style=social)](https://github.com/PurpleHaze2320/ai-agent-pulse/stargazers)

> Automated daily tracking of the AI agent framework ecosystem's health, momentum, and trends.
> Last updated: **2026-09-11 10:57 UTC** | Tracking **19** frameworks

## How It Works

This bot runs daily via GitHub Actions and collects metrics from the GitHub API for the most important
AI agent frameworks. It computes a **Pulse Score** (0-100) based on six weighted signals: star velocity,
release freshness, issue health, commit activity, community size, and fork engagement. The result is
a living dashboard that shows which frameworks are gaining momentum and which are losing steam.

## 🏆 Pulse Leaderboard

| Rank | Framework | Pulse | Stars | ⭐ 7d | Commits (4w) | Last Release | Category |
|------|-----------|-------|-------|-------|--------------|--------------|----------|
| 1 | [BrowserUse](https://github.com/browser-use/browser-use) | 🟢 **90.0** | 114.2k | 🚀 +1927 | 206 | 7 days ago | `web-agent` |
| 2 | [CrewAI](https://github.com/crewAIInc/crewAI) | 🟢 **81.6** | 58.4k | 🚀 +284 | 104 | 1 day ago | `multi-agent` |
| 3 | [Mastra](https://github.com/mastra-ai/mastra) | 🟢 **79.1** | 27.9k | 🚀 +242 | 1486 | today | `typescript` |
| 4 | [OpenAI Agents SDK](https://github.com/openai/openai-agents-python) | 🟢 **77.3** | 29.4k | 🚀 +162 | 154 | 1 day ago | `orchestration` |
| 5 | [PydanticAI](https://github.com/pydantic/pydantic-ai) | 🟢 **74.3** | 19.9k | 🚀 +145 | 249 | 2 days ago | `structured` |
| 6 | [Google ADK](https://github.com/google/adk-python) | 🟢 **74.3** | 21.5k | 📈 +93 | 407 | today | `orchestration` |
| 7 | [Claude Agent SDK](https://github.com/anthropics/claude-code) | 🟢 **72.3** | 144.7k | 🚀 +714 | 34 | today | `orchestration` |
| 8 | [Haystack](https://github.com/deepset-ai/haystack) | 🟢 **71.0** | 26.5k | 📈 +63 | 217 | 8 days ago | `pipeline` |
| 9 | [Agno](https://github.com/agno-agi/agno) | 🟢 **70.6** | 42.1k | 📈 +91 | 100 | 2 days ago | `multi-agent` |
| 10 | [LangGraph](https://github.com/langchain-ai/langgraph) | 🟡 **69.9** | 41.5k | 🚀 +417 | 33 | 14 days ago | `orchestration` |
| 11 | [Composio](https://github.com/ComposioHQ/composio) | 🟡 **67.6** | 30.1k | 📈 +93 | 259 | today | `tooling` |
| 12 | [LlamaIndex](https://github.com/run-llama/llama_index) | 🟡 **61.5** | 52.1k | 🚀 +113 | 33 | 22 days ago | `data-agent` |
| 13 | [DSPy](https://github.com/stanfordnlp/dspy) | 🟡 **61.4** | 37.9k | 🚀 +146 | 55 | 20 days ago | `optimization` |
| 14 | [AG2](https://github.com/ag2ai/ag2) | 🟡 **58.9** | 4.9k | ↗️ +15 | 46 | 4 days ago | `multi-agent` |
| 15 | [Semantic Kernel](https://github.com/microsoft/semantic-kernel) | 🟡 **55.0** | 28.6k | 📈 +24 | 24 | 7 days ago | `enterprise` |
| 16 | [Letta](https://github.com/letta-ai/letta) | 🟠 **39.5** | 24.7k | 📈 +84 | 3 | 3 mo ago | `memory` |
| 17 | [Smolagents](https://github.com/huggingface/smolagents) | 🟠 **37.6** | 29.3k | 🚀 +134 | 2 | 3 mo ago | `lightweight` |
| 18 | [AutoGen](https://github.com/microsoft/autogen) | 🟠 **34.1** | 60.9k | 🚀 +137 | 0 | 11 mo ago | `multi-agent` |
| 19 | [Swarm](https://github.com/openai/swarm) | 🔴 **9.7** | 22.0k | 📈 +27 | 0 | — | `experimental` |

## 📂 By Category

- `data-agent`: **LlamaIndex** (61.5)
- `enterprise`: **Semantic Kernel** (55.0)
- `experimental`: **Swarm** (9.7)
- `lightweight`: **Smolagents** (37.6)
- `memory`: **Letta** (39.5)
- `multi-agent`: **CrewAI** (81.6), **Agno** (70.6), **AG2** (58.9), **AutoGen** (34.1)
- `optimization`: **DSPy** (61.4)
- `orchestration`: **OpenAI Agents SDK** (77.3), **Google ADK** (74.3), **Claude Agent SDK** (72.3), **LangGraph** (69.9)
- `pipeline`: **Haystack** (71.0)
- `structured`: **PydanticAI** (74.3)
- `tooling`: **Composio** (67.6)
- `typescript`: **Mastra** (79.1)
- `web-agent`: **BrowserUse** (90.0)

## 🔍 Top 5 — Score Breakdown

| Framework | Star Velocity | Release Freshness | Issue Health | Commit Activity | Community | Fork Ratio |
|-----------|:---:|:---:|:---:|:---:|:---:|:---:|
| **BrowserUse** | 100 | 97.7 | 92.3 | 100 | 72.0 | 44.0 |
| **CrewAI** | 60.6 | 99.7 | 95.6 | 100 | 64.2 | 57.6 |
| **Mastra** | 46.1 | 100.0 | 95.2 | 100 | 93.0 | 39.6 |
| **OpenAI Agents SDK** | 34.4 | 99.7 | 99.1 | 100 | 74.8 | 64.1 |
| **PydanticAI** | 29.6 | 99.3 | 80.9 | 100 | 95.0 | 54.2 |

## 💡 Key Insights

- **Hottest framework**: BrowserUse with a Pulse Score of 90.0
- **Fastest growing**: BrowserUse gained +1927 stars this week
- **Most active development**: Mastra with 1486 commits in the last 4 weeks
- **Stale releases**: AutoGen, Swarm haven't released in a while

## 📦 Recent Releases

- **Mastra** [`@mastra/core@1.66.0`](https://github.com/mastra-ai/mastra/releases/tag/@mastra/core@1.66.0) — today
- **Google ADK** [`v2.9.0`](https://github.com/google/adk-python/releases/tag/v2.9.0) — today
- **Claude Agent SDK** [`v2.1.268`](https://github.com/anthropics/claude-code/releases/tag/v2.1.268) — today
- **Composio** [`@composio/cli@0.4.2-beta.386`](https://github.com/ComposioHQ/composio/releases/tag/@composio/cli@0.4.2-beta.386) — today *(pre-release)*
- **CrewAI** [`1.15.21`](https://github.com/crewAIInc/crewAI/releases/tag/1.15.21) — 1 day ago
- **OpenAI Agents SDK** [`v0.22.2`](https://github.com/openai/openai-agents-python/releases/tag/v0.22.2) — 1 day ago
- **PydanticAI** [`v2.42.0`](https://github.com/pydantic/pydantic-ai/releases/tag/v2.42.0) — 2 days ago
- **Agno** [`v3.0.9`](https://github.com/agno-agi/agno/releases/tag/v3.0.9) — 2 days ago
- **AG2** [`v1.0.4`](https://github.com/ag2ai/ag2/releases/tag/v1.0.4) — 4 days ago
- **BrowserUse** [`0.13.10`](https://github.com/browser-use/browser-use/releases/tag/0.13.10) — 7 days ago

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

*Powered by GitHub Actions • Data refreshed daily • Last run: 2026-09-11 10:57 UTC*