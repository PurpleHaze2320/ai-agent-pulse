# 🔬 AI Agent Framework Pulse Tracker

[![Daily Update](https://github.com/PurpleHaze2320/ai-agent-pulse/actions/workflows/track.yml/badge.svg)](https://github.com/PurpleHaze2320/ai-agent-pulse/actions/workflows/track.yml)
[![Frameworks Tracked](https://img.shields.io/badge/frameworks-19-blue)](https://github.com/PurpleHaze2320/ai-agent-pulse)
[![License: MIT](https://img.shields.io/badge/License-MIT-green.svg)](https://opensource.org/licenses/MIT)
[![GitHub stars](https://img.shields.io/github/stars/PurpleHaze2320/ai-agent-pulse?style=social)](https://github.com/PurpleHaze2320/ai-agent-pulse/stargazers)

> Automated daily tracking of the AI agent framework ecosystem's health, momentum, and trends.
> Last updated: **2026-11-20 15:08 UTC** | Tracking **19** frameworks

## How It Works

This bot runs daily via GitHub Actions and collects metrics from the GitHub API for the most important
AI agent frameworks. It computes a **Pulse Score** (0-100) based on six weighted signals: star velocity,
release freshness, issue health, commit activity, community size, and fork engagement. The result is
a living dashboard that shows which frameworks are gaining momentum and which are losing steam.

## 🏆 Pulse Leaderboard

| Rank | Framework | Pulse | Stars | ⭐ 7d | Commits (4w) | Last Release | Category |
|------|-----------|-------|-------|-------|--------------|--------------|----------|
| 1 | [BrowserUse](https://github.com/browser-use/browser-use) | 🟢 **89.9** | 121.6k | 🚀 +681 | 1158 | 4 days ago | `web-agent` |
| 2 | [Claude Agent SDK](https://github.com/anthropics/claude-code) | 🟢 **85.3** | 156.4k | 🚀 +894 | 135 | today | `orchestration` |
| 3 | [LangGraph](https://github.com/langchain-ai/langgraph) | 🟢 **80.7** | 45.2k | 🚀 +291 | 111 | today | `orchestration` |
| 4 | [CrewAI](https://github.com/crewAIInc/crewAI) | 🟢 **80.5** | 61.1k | 🚀 +278 | 203 | today | `multi-agent` |
| 5 | [Mastra](https://github.com/mastra-ai/mastra) | 🟢 **76.7** | 29.7k | 🚀 +187 | 2383 | 2 days ago | `typescript` |
| 6 | [OpenAI Agents SDK](https://github.com/openai/openai-agents-python) | 🟢 **74.7** | 30.8k | 🚀 +135 | 93 | 2 days ago | `orchestration` |
| 7 | [Google ADK](https://github.com/google/adk-python) | 🟢 **74.5** | 22.3k | 📈 +80 | 369 | today | `orchestration` |
| 8 | [AG2](https://github.com/ag2ai/ag2) | 🟢 **70.2** | 5.1k | ↗️ +14 | 118 | today | `multi-agent` |
| 9 | [Composio](https://github.com/ComposioHQ/composio) | 🟡 **69.5** | 31.2k | 🚀 +145 | 308 | today | `tooling` |
| 10 | [Agno](https://github.com/agno-agi/agno) | 🟡 **68.9** | 43.2k | 📈 +62 | 136 | 2 days ago | `multi-agent` |
| 11 | [Semantic Kernel](https://github.com/microsoft/semantic-kernel) | 🟡 **67.7** | 28.8k | 📈 +28 | 84 | 13 days ago | `enterprise` |
| 12 | [DSPy](https://github.com/stanfordnlp/dspy) | 🟡 **64.8** | 39.2k | 🚀 +123 | 78 | 9 days ago | `optimization` |
| 13 | [LlamaIndex](https://github.com/run-llama/llama_index) | 🟡 **55.4** | 53.0k | 📈 +76 | 8 | 6 days ago | `data-agent` |
| 14 | [Haystack](https://github.com/deepset-ai/haystack) | 🟡 **51.3** | 27.1k | 📈 +60 | 0 | 10 days ago | `pipeline` |
| 15 | [PydanticAI](https://github.com/pydantic/pydantic-ai) | 🟡 **50.1** | 21.3k | 🚀 +123 | 0 | 1 mo ago | `structured` |
| 16 | [AutoGen](https://github.com/microsoft/autogen) | 🟠 **34.5** | 62.0k | 🚀 +150 | 2 | 1y ago | `multi-agent` |
| 17 | [Smolagents](https://github.com/huggingface/smolagents) | 🟠 **34.3** | 30.5k | 🚀 +110 | 17 | 5 mo ago | `lightweight` |
| 18 | [Letta](https://github.com/letta-ai/letta) | 🟠 **33.0** | 25.5k | 📈 +73 | 0 | 6 mo ago | `memory` |
| 19 | [Swarm](https://github.com/openai/swarm) | 🔴 **9.3** | 22.2k | ↗️ +16 | 0 | — | `experimental` |

## 📂 By Category

- `data-agent`: **LlamaIndex** (55.4)
- `enterprise`: **Semantic Kernel** (67.7)
- `experimental`: **Swarm** (9.3)
- `lightweight`: **Smolagents** (34.3)
- `memory`: **Letta** (33.0)
- `multi-agent`: **CrewAI** (80.5), **AG2** (70.2), **Agno** (68.9), **AutoGen** (34.5)
- `optimization`: **DSPy** (64.8)
- `orchestration`: **Claude Agent SDK** (85.3), **LangGraph** (80.7), **OpenAI Agents SDK** (74.7), **Google ADK** (74.5)
- `pipeline`: **Haystack** (51.3)
- `structured`: **PydanticAI** (50.1)
- `tooling`: **Composio** (69.5)
- `typescript`: **Mastra** (76.7)
- `web-agent`: **BrowserUse** (89.9)

## 🔍 Top 5 — Score Breakdown

| Framework | Star Velocity | Release Freshness | Issue Health | Commit Activity | Community | Fork Ratio |
|-----------|:---:|:---:|:---:|:---:|:---:|:---:|
| **BrowserUse** | 100 | 98.7 | 90.0 | 100 | 72.2 | 44.7 |
| **Claude Agent SDK** | 100 | 100.0 | 85.4 | 100 | 11.2 | 64.1 |
| **LangGraph** | 64.1 | 100.0 | 80.2 | 100 | 57.6 | 69.0 |
| **CrewAI** | 56.6 | 100.0 | 84.5 | 100 | 76.4 | 60.4 |
| **Mastra** | 37.0 | 99.3 | 93.5 | 100 | 93.2 | 42.1 |

## 💡 Key Insights

- **Hottest framework**: BrowserUse with a Pulse Score of 89.9
- **Fastest growing**: Claude Agent SDK gained +894 stars this week
- **Most active development**: Mastra with 2383 commits in the last 4 weeks
- **⚠️ Archived**: AutoGen
- **Stale releases**: AutoGen, Swarm haven't released in a while

## 📦 Recent Releases

- **LangGraph** [`1.2.24`](https://github.com/langchain-ai/langgraph/releases/tag/1.2.24) — today
- **Google ADK** [`v2.15.0`](https://github.com/google/adk-python/releases/tag/v2.15.0) — today
- **Claude Agent SDK** [`v2.1.329`](https://github.com/anthropics/claude-code/releases/tag/v2.1.329) — today
- **AG2** [`v1.3.3`](https://github.com/ag2ai/ag2/releases/tag/v1.3.3) — today
- **Composio** [`@composio/cli@0.6.3-beta.571`](https://github.com/ComposioHQ/composio/releases/tag/@composio/cli@0.6.3-beta.571) — today *(pre-release)*
- **CrewAI** [`1.15.44`](https://github.com/crewAIInc/crewAI/releases/tag/1.15.44) — today
- **Mastra** [`@mastra/core@1.84.0`](https://github.com/mastra-ai/mastra/releases/tag/@mastra/core@1.84.0) — 2 days ago
- **OpenAI Agents SDK** [`v0.25.0`](https://github.com/openai/openai-agents-python/releases/tag/v0.25.0) — 2 days ago
- **Agno** [`v3.2.1`](https://github.com/agno-agi/agno/releases/tag/v3.2.1) — 2 days ago
- **BrowserUse** [`1.0.6`](https://github.com/browser-use/browser-use/releases/tag/1.0.6) — 4 days ago

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

*Powered by GitHub Actions • Data refreshed daily • Last run: 2026-11-20 15:08 UTC*