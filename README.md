# 🔬 AI Agent Framework Pulse Tracker

[![Daily Update](https://github.com/PurpleHaze2320/ai-agent-pulse/actions/workflows/track.yml/badge.svg)](https://github.com/PurpleHaze2320/ai-agent-pulse/actions/workflows/track.yml)
[![Frameworks Tracked](https://img.shields.io/badge/frameworks-19-blue)](https://github.com/PurpleHaze2320/ai-agent-pulse)
[![License: MIT](https://img.shields.io/badge/License-MIT-green.svg)](https://opensource.org/licenses/MIT)
[![GitHub stars](https://img.shields.io/github/stars/PurpleHaze2320/ai-agent-pulse?style=social)](https://github.com/PurpleHaze2320/ai-agent-pulse/stargazers)

> Automated daily tracking of the AI agent framework ecosystem's health, momentum, and trends.
> Last updated: **2026-11-18 15:25 UTC** | Tracking **19** frameworks

## How It Works

This bot runs daily via GitHub Actions and collects metrics from the GitHub API for the most important
AI agent frameworks. It computes a **Pulse Score** (0-100) based on six weighted signals: star velocity,
release freshness, issue health, commit activity, community size, and fork engagement. The result is
a living dashboard that shows which frameworks are gaining momentum and which are losing steam.

## 🏆 Pulse Leaderboard

| Rank | Framework | Pulse | Stars | ⭐ 7d | Commits (4w) | Last Release | Category |
|------|-----------|-------|-------|-------|--------------|--------------|----------|
| 1 | [BrowserUse](https://github.com/browser-use/browser-use) | 🟢 **90.1** | 121.4k | 🚀 +718 | 1158 | 2 days ago | `web-agent` |
| 2 | [Claude Agent SDK](https://github.com/anthropics/claude-code) | 🟢 **85.2** | 156.1k | 🚀 +860 | 112 | today | `orchestration` |
| 3 | [LangGraph](https://github.com/langchain-ai/langgraph) | 🟢 **81.8** | 45.1k | 🚀 +324 | 104 | 4 days ago | `orchestration` |
| 4 | [CrewAI](https://github.com/crewAIInc/crewAI) | 🟢 **80.9** | 61.1k | 🚀 +305 | 174 | 5 days ago | `multi-agent` |
| 5 | [Mastra](https://github.com/mastra-ai/mastra) | 🟢 **74.8** | 29.6k | 🚀 +130 | 2234 | today | `typescript` |
| 6 | [OpenAI Agents SDK](https://github.com/openai/openai-agents-python) | 🟢 **74.7** | 30.8k | 🚀 +136 | 91 | today | `orchestration` |
| 7 | [Google ADK](https://github.com/google/adk-python) | 🟢 **74.3** | 22.3k | 📈 +83 | 343 | 5 days ago | `orchestration` |
| 8 | [Haystack](https://github.com/deepset-ai/haystack) | 🟢 **71.2** | 27.0k | 📈 +53 | 225 | 8 days ago | `pipeline` |
| 9 | [AG2](https://github.com/ag2ai/ag2) | 🟢 **70.3** | 5.1k | ↗️ +19 | 110 | 2 days ago | `multi-agent` |
| 10 | [Agno](https://github.com/agno-agi/agno) | 🟢 **70.0** | 43.2k | 📈 +85 | 131 | today | `multi-agent` |
| 11 | [Composio](https://github.com/ComposioHQ/composio) | 🟡 **69.2** | 31.2k | 🚀 +137 | 282 | today | `tooling` |
| 12 | [Semantic Kernel](https://github.com/microsoft/semantic-kernel) | 🟡 **67.6** | 28.8k | 📈 +32 | 82 | 11 days ago | `enterprise` |
| 13 | [DSPy](https://github.com/stanfordnlp/dspy) | 🟡 **64.4** | 39.1k | 🚀 +115 | 77 | 7 days ago | `optimization` |
| 14 | [LlamaIndex](https://github.com/run-llama/llama_index) | 🟡 **55.3** | 52.9k | 📈 +69 | 8 | 4 days ago | `data-agent` |
| 15 | [PydanticAI](https://github.com/pydantic/pydantic-ai) | 🟡 **50.6** | 21.3k | 🚀 +136 | 0 | 1 mo ago | `structured` |
| 16 | [AutoGen](https://github.com/microsoft/autogen) | 🟠 **34.1** | 61.9k | 🚀 +138 | 2 | 1y ago | `multi-agent` |
| 17 | [Smolagents](https://github.com/huggingface/smolagents) | 🟠 **33.8** | 30.4k | 🚀 +115 | 13 | 5 mo ago | `lightweight` |
| 18 | [Letta](https://github.com/letta-ai/letta) | 🟠 **32.8** | 25.5k | 📈 +63 | 0 | 6 mo ago | `memory` |
| 19 | [Swarm](https://github.com/openai/swarm) | 🔴 **9.5** | 22.1k | 📈 +22 | 0 | — | `experimental` |

## 📂 By Category

- `data-agent`: **LlamaIndex** (55.3)
- `enterprise`: **Semantic Kernel** (67.6)
- `experimental`: **Swarm** (9.5)
- `lightweight`: **Smolagents** (33.8)
- `memory`: **Letta** (32.8)
- `multi-agent`: **CrewAI** (80.9), **AG2** (70.3), **Agno** (70.0), **AutoGen** (34.1)
- `optimization`: **DSPy** (64.4)
- `orchestration`: **Claude Agent SDK** (85.2), **LangGraph** (81.8), **OpenAI Agents SDK** (74.7), **Google ADK** (74.3)
- `pipeline`: **Haystack** (71.2)
- `structured`: **PydanticAI** (50.6)
- `tooling`: **Composio** (69.2)
- `typescript`: **Mastra** (74.8)
- `web-agent`: **BrowserUse** (90.1)

## 🔍 Top 5 — Score Breakdown

| Framework | Star Velocity | Release Freshness | Issue Health | Commit Activity | Community | Fork Ratio |
|-----------|:---:|:---:|:---:|:---:|:---:|:---:|
| **BrowserUse** | 100 | 99.3 | 90.2 | 100 | 72.4 | 44.7 |
| **Claude Agent SDK** | 100 | 100.0 | 84.7 | 100 | 11.2 | 64.1 |
| **LangGraph** | 69.6 | 98.7 | 80.3 | 100 | 57.6 | 69.0 |
| **CrewAI** | 60.7 | 98.3 | 83.8 | 100 | 74.8 | 60.4 |
| **Mastra** | 28.7 | 100.0 | 93.7 | 100 | 93.2 | 42.1 |

## 💡 Key Insights

- **Hottest framework**: BrowserUse with a Pulse Score of 90.1
- **Fastest growing**: Claude Agent SDK gained +860 stars this week
- **Most active development**: Mastra with 2234 commits in the last 4 weeks
- **Stale releases**: AutoGen, Swarm haven't released in a while

## 📦 Recent Releases

- **Composio** [`@composio/cli@0.6.3-beta.564`](https://github.com/ComposioHQ/composio/releases/tag/@composio/cli@0.6.3-beta.564) — today *(pre-release)*
- **Mastra** [`@mastra/core@1.84.0`](https://github.com/mastra-ai/mastra/releases/tag/@mastra/core@1.84.0) — today
- **OpenAI Agents SDK** [`v0.25.0`](https://github.com/openai/openai-agents-python/releases/tag/v0.25.0) — today
- **Claude Agent SDK** [`v2.1.327`](https://github.com/anthropics/claude-code/releases/tag/v2.1.327) — today
- **Agno** [`v3.2.1`](https://github.com/agno-agi/agno/releases/tag/v3.2.1) — today
- **BrowserUse** [`1.0.6`](https://github.com/browser-use/browser-use/releases/tag/1.0.6) — 2 days ago
- **AG2** [`v1.3.2`](https://github.com/ag2ai/ag2/releases/tag/v1.3.2) — 2 days ago
- **LangGraph** [`1.2.22`](https://github.com/langchain-ai/langgraph/releases/tag/1.2.22) — 4 days ago
- **LlamaIndex** [`v0.14.26`](https://github.com/run-llama/llama_index/releases/tag/v0.14.26) — 4 days ago
- **Google ADK** [`v2.14.1`](https://github.com/google/adk-python/releases/tag/v2.14.1) — 5 days ago

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

*Powered by GitHub Actions • Data refreshed daily • Last run: 2026-11-18 15:25 UTC*