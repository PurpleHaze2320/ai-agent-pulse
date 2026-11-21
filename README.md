# 🔬 AI Agent Framework Pulse Tracker

[![Daily Update](https://github.com/PurpleHaze2320/ai-agent-pulse/actions/workflows/track.yml/badge.svg)](https://github.com/PurpleHaze2320/ai-agent-pulse/actions/workflows/track.yml)
[![Frameworks Tracked](https://img.shields.io/badge/frameworks-19-blue)](https://github.com/PurpleHaze2320/ai-agent-pulse)
[![License: MIT](https://img.shields.io/badge/License-MIT-green.svg)](https://opensource.org/licenses/MIT)
[![GitHub stars](https://img.shields.io/github/stars/PurpleHaze2320/ai-agent-pulse?style=social)](https://github.com/PurpleHaze2320/ai-agent-pulse/stargazers)

> Automated daily tracking of the AI agent framework ecosystem's health, momentum, and trends.
> Last updated: **2026-11-21 14:27 UTC** | Tracking **19** frameworks

## How It Works

This bot runs daily via GitHub Actions and collects metrics from the GitHub API for the most important
AI agent frameworks. It computes a **Pulse Score** (0-100) based on six weighted signals: star velocity,
release freshness, issue health, commit activity, community size, and fork engagement. The result is
a living dashboard that shows which frameworks are gaining momentum and which are losing steam.

## 🏆 Pulse Leaderboard

| Rank | Framework | Pulse | Stars | ⭐ 7d | Commits (4w) | Last Release | Category |
|------|-----------|-------|-------|-------|--------------|--------------|----------|
| 1 | [BrowserUse](https://github.com/browser-use/browser-use) | 🟢 **90.2** | 121.7k | 🚀 +665 | 1199 | today | `web-agent` |
| 2 | [Claude Agent SDK](https://github.com/anthropics/claude-code) | 🟢 **85.4** | 156.5k | 🚀 +901 | 147 | today | `orchestration` |
| 3 | [LangGraph](https://github.com/langchain-ai/langgraph) | 🟢 **79.9** | 45.2k | 🚀 +274 | 113 | 1 day ago | `orchestration` |
| 4 | [CrewAI](https://github.com/crewAIInc/crewAI) | 🟢 **79.8** | 61.1k | 🚀 +259 | 210 | 1 day ago | `multi-agent` |
| 5 | [Mastra](https://github.com/mastra-ai/mastra) | 🟢 **77.2** | 29.7k | 🚀 +205 | 2436 | 3 days ago | `typescript` |
| 6 | [Google ADK](https://github.com/google/adk-python) | 🟢 **74.5** | 22.3k | 📈 +84 | 375 | 1 day ago | `orchestration` |
| 7 | [OpenAI Agents SDK](https://github.com/openai/openai-agents-python) | 🟢 **74.2** | 30.8k | 🚀 +121 | 93 | today | `orchestration` |
| 8 | [Haystack](https://github.com/deepset-ai/haystack) | 🟢 **71.4** | 27.1k | 📈 +64 | 250 | 11 days ago | `pipeline` |
| 9 | [AG2](https://github.com/ag2ai/ag2) | 🟢 **70.1** | 5.1k | ↗️ +12 | 119 | 1 day ago | `multi-agent` |
| 10 | [PydanticAI](https://github.com/pydantic/pydantic-ai) | 🟢 **70.0** | 21.3k | 🚀 +121 | 1193 | 1 mo ago | `structured` |
| 11 | [Composio](https://github.com/ComposioHQ/composio) | 🟡 **69.7** | 31.2k | 🚀 +153 | 315 | today | `tooling` |
| 12 | [Agno](https://github.com/agno-agi/agno) | 🟡 **69.0** | 43.3k | 📈 +66 | 136 | 3 days ago | `multi-agent` |
| 13 | [Semantic Kernel](https://github.com/microsoft/semantic-kernel) | 🟡 **67.9** | 28.8k | 📈 +29 | 85 | 14 days ago | `enterprise` |
| 14 | [LlamaIndex](https://github.com/run-llama/llama_index) | 🟡 **55.2** | 53.0k | 📈 +74 | 8 | 7 days ago | `data-agent` |
| 15 | [DSPy](https://github.com/stanfordnlp/dspy) | 🟡 **48.8** | 39.2k | 🚀 +116 | 0 | 10 days ago | `optimization` |
| 16 | [AutoGen](https://github.com/microsoft/autogen) | 🟠 **34.1** | 62.0k | 🚀 +141 | 2 | 1y ago | `multi-agent` |
| 17 | [Smolagents](https://github.com/huggingface/smolagents) | 🟠 **33.7** | 30.5k | 📈 +99 | 17 | 5 mo ago | `lightweight` |
| 18 | [Letta](https://github.com/letta-ai/letta) | 🟠 **33.0** | 25.5k | 📈 +74 | 0 | 6 mo ago | `memory` |
| 19 | [Swarm](https://github.com/openai/swarm) | 🔴 **9.3** | 22.2k | ↗️ +16 | 0 | — | `experimental` |

## 📂 By Category

- `data-agent`: **LlamaIndex** (55.2)
- `enterprise`: **Semantic Kernel** (67.9)
- `experimental`: **Swarm** (9.3)
- `lightweight`: **Smolagents** (33.7)
- `memory`: **Letta** (33.0)
- `multi-agent`: **CrewAI** (79.8), **AG2** (70.1), **Agno** (69.0), **AutoGen** (34.1)
- `optimization`: **DSPy** (48.8)
- `orchestration`: **Claude Agent SDK** (85.4), **LangGraph** (79.9), **Google ADK** (74.5), **OpenAI Agents SDK** (74.2)
- `pipeline`: **Haystack** (71.4)
- `structured`: **PydanticAI** (70.0)
- `tooling`: **Composio** (69.7)
- `typescript`: **Mastra** (77.2)
- `web-agent`: **BrowserUse** (90.2)

## 🔍 Top 5 — Score Breakdown

| Framework | Star Velocity | Release Freshness | Issue Health | Commit Activity | Community | Fork Ratio |
|-----------|:---:|:---:|:---:|:---:|:---:|:---:|
| **BrowserUse** | 100 | 100.0 | 89.9 | 100 | 72.2 | 44.7 |
| **Claude Agent SDK** | 100 | 100.0 | 85.8 | 100 | 11.2 | 64.1 |
| **LangGraph** | 61.1 | 99.7 | 80.1 | 100 | 57.6 | 69.1 |
| **CrewAI** | 53.7 | 99.7 | 84.4 | 100 | 77.0 | 60.4 |
| **Mastra** | 39.5 | 99.0 | 93.3 | 100 | 93.2 | 42.1 |

## 💡 Key Insights

- **Hottest framework**: BrowserUse with a Pulse Score of 90.2
- **Fastest growing**: Claude Agent SDK gained +901 stars this week
- **Most active development**: Mastra with 2436 commits in the last 4 weeks
- **⚠️ Archived**: AutoGen
- **Stale releases**: AutoGen, Swarm haven't released in a while

## 📦 Recent Releases

- **BrowserUse** [`1.0.8rc1`](https://github.com/browser-use/browser-use/releases/tag/1.0.8rc1) — today *(pre-release)*
- **Claude Agent SDK** [`v2.1.330`](https://github.com/anthropics/claude-code/releases/tag/v2.1.330) — today
- **OpenAI Agents SDK** [`v1.0.0-alpha.1`](https://github.com/openai/openai-agents-python/releases/tag/v1.0.0-alpha.1) — today *(pre-release)*
- **Composio** [`@composio/cli@0.6.4-beta.573`](https://github.com/ComposioHQ/composio/releases/tag/@composio/cli@0.6.4-beta.573) — today *(pre-release)*
- **LangGraph** [`1.2.24`](https://github.com/langchain-ai/langgraph/releases/tag/1.2.24) — 1 day ago
- **Google ADK** [`v2.15.0`](https://github.com/google/adk-python/releases/tag/v2.15.0) — 1 day ago
- **AG2** [`v1.3.3`](https://github.com/ag2ai/ag2/releases/tag/v1.3.3) — 1 day ago
- **CrewAI** [`1.15.44`](https://github.com/crewAIInc/crewAI/releases/tag/1.15.44) — 1 day ago
- **Mastra** [`@mastra/core@1.84.0`](https://github.com/mastra-ai/mastra/releases/tag/@mastra/core@1.84.0) — 3 days ago
- **Agno** [`v3.2.1`](https://github.com/agno-agi/agno/releases/tag/v3.2.1) — 3 days ago

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

*Powered by GitHub Actions • Data refreshed daily • Last run: 2026-11-21 14:27 UTC*