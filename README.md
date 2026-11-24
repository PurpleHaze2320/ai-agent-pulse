# 🔬 AI Agent Framework Pulse Tracker

[![Daily Update](https://github.com/PurpleHaze2320/ai-agent-pulse/actions/workflows/track.yml/badge.svg)](https://github.com/PurpleHaze2320/ai-agent-pulse/actions/workflows/track.yml)
[![Frameworks Tracked](https://img.shields.io/badge/frameworks-19-blue)](https://github.com/PurpleHaze2320/ai-agent-pulse)
[![License: MIT](https://img.shields.io/badge/License-MIT-green.svg)](https://opensource.org/licenses/MIT)
[![GitHub stars](https://img.shields.io/github/stars/PurpleHaze2320/ai-agent-pulse?style=social)](https://github.com/PurpleHaze2320/ai-agent-pulse/stargazers)

> Automated daily tracking of the AI agent framework ecosystem's health, momentum, and trends.
> Last updated: **2026-11-24 17:18 UTC** | Tracking **19** frameworks

## How It Works

This bot runs daily via GitHub Actions and collects metrics from the GitHub API for the most important
AI agent frameworks. It computes a **Pulse Score** (0-100) based on six weighted signals: star velocity,
release freshness, issue health, commit activity, community size, and fork engagement. The result is
a living dashboard that shows which frameworks are gaining momentum and which are losing steam.

## 🏆 Pulse Leaderboard

| Rank | Framework | Pulse | Stars | ⭐ 7d | Commits (4w) | Last Release | Category |
|------|-----------|-------|-------|-------|--------------|--------------|----------|
| 1 | [BrowserUse](https://github.com/browser-use/browser-use) | 🟢 **90.0** | 121.9k | 🚀 +628 | 1195 | 2 days ago | `web-agent` |
| 2 | [CrewAI](https://github.com/crewAIInc/crewAI) | 🟢 **77.9** | 61.2k | 🚀 +199 | 163 | today | `multi-agent` |
| 3 | [Mastra](https://github.com/mastra-ai/mastra) | 🟢 **77.6** | 29.8k | 🚀 +224 | 2049 | 6 days ago | `typescript` |
| 4 | [LangGraph](https://github.com/langchain-ai/langgraph) | 🟢 **75.1** | 45.4k | 🚀 +294 | 74 | 4 days ago | `orchestration` |
| 5 | [Google ADK](https://github.com/google/adk-python) | 🟢 **74.7** | 22.3k | 📈 +93 | 261 | 4 days ago | `orchestration` |
| 6 | [OpenAI Agents SDK](https://github.com/openai/openai-agents-python) | 🟢 **72.7** | 30.9k | 🚀 +119 | 86 | today | `orchestration` |
| 7 | [PydanticAI](https://github.com/pydantic/pydantic-ai) | 🟢 **72.6** | 21.4k | 🚀 +110 | 881 | today | `structured` |
| 8 | [Haystack](https://github.com/deepset-ai/haystack) | 🟢 **71.6** | 27.1k | 📈 +74 | 239 | 14 days ago | `pipeline` |
| 9 | [AG2](https://github.com/ag2ai/ag2) | 🟢 **70.2** | 5.1k | ↗️ +13 | 103 | 1 day ago | `multi-agent` |
| 10 | [Composio](https://github.com/ComposioHQ/composio) | 🟡 **69.7** | 31.3k | 🚀 +152 | 277 | today | `tooling` |
| 11 | [Agno](https://github.com/agno-agi/agno) | 🟡 **68.7** | 43.3k | 📈 +66 | 106 | 7 days ago | `multi-agent` |
| 12 | [Claude Agent SDK](https://github.com/anthropics/claude-code) | 🟡 **65.4** | 156.9k | 🚀 +927 | 0 | today | `orchestration` |
| 13 | [DSPy](https://github.com/stanfordnlp/dspy) | 🟡 **59.6** | 39.2k | 📈 +99 | 58 | 14 days ago | `optimization` |
| 14 | [Semantic Kernel](https://github.com/microsoft/semantic-kernel) | 🟡 **57.7** | 28.8k | ↗️ +19 | 37 | 17 days ago | `enterprise` |
| 15 | [LlamaIndex](https://github.com/run-llama/llama_index) | 🟡 **54.8** | 53.0k | 📈 +69 | 8 | 10 days ago | `data-agent` |
| 16 | [Smolagents](https://github.com/huggingface/smolagents) | 🟠 **34.5** | 30.5k | 🚀 +109 | 20 | 5 mo ago | `lightweight` |
| 17 | [Letta](https://github.com/letta-ai/letta) | 🟠 **32.3** | 25.5k | 📈 +62 | 0 | 6 mo ago | `memory` |
| 18 | [AutoGen](https://github.com/microsoft/autogen) | 🟠 **31.7** | 62.0k | 📈 +80 | 1 | 1y ago | `multi-agent` |
| 19 | [Swarm](https://github.com/openai/swarm) | 🔴 **9.3** | 22.2k | ↗️ +16 | 0 | — | `experimental` |

## 📂 By Category

- `data-agent`: **LlamaIndex** (54.8)
- `enterprise`: **Semantic Kernel** (57.7)
- `experimental`: **Swarm** (9.3)
- `lightweight`: **Smolagents** (34.5)
- `memory`: **Letta** (32.3)
- `multi-agent`: **CrewAI** (77.9), **AG2** (70.2), **Agno** (68.7), **AutoGen** (31.7)
- `optimization`: **DSPy** (59.6)
- `orchestration`: **LangGraph** (75.1), **Google ADK** (74.7), **OpenAI Agents SDK** (72.7), **Claude Agent SDK** (65.4)
- `pipeline`: **Haystack** (71.6)
- `structured`: **PydanticAI** (72.6)
- `tooling`: **Composio** (69.7)
- `typescript`: **Mastra** (77.6)
- `web-agent`: **BrowserUse** (90.0)

## 🔍 Top 5 — Score Breakdown

| Framework | Star Velocity | Release Freshness | Issue Health | Commit Activity | Community | Fork Ratio |
|-----------|:---:|:---:|:---:|:---:|:---:|:---:|
| **BrowserUse** | 100 | 99.3 | 89.9 | 100 | 72.2 | 44.7 |
| **CrewAI** | 45.0 | 100.0 | 85.0 | 100 | 78.0 | 60.6 |
| **Mastra** | 42.2 | 98.0 | 93.1 | 100 | 93.2 | 42.1 |
| **LangGraph** | 63.7 | 98.7 | 79.9 | 74.0 | 57.6 | 69.2 |
| **Google ADK** | 18.1 | 98.7 | 92.5 | 100 | 86.2 | 79.3 |

## 💡 Key Insights

- **Hottest framework**: BrowserUse with a Pulse Score of 90.0
- **Fastest growing**: Claude Agent SDK gained +927 stars this week
- **Most active development**: Mastra with 2049 commits in the last 4 weeks
- **⚠️ Archived**: AutoGen
- **Stale releases**: AutoGen, Swarm haven't released in a while

## 📦 Recent Releases

- **Composio** [`@composio/cli@0.6.4-beta.582`](https://github.com/ComposioHQ/composio/releases/tag/@composio/cli@0.6.4-beta.582) — today *(pre-release)*
- **CrewAI** [`1.15.45`](https://github.com/crewAIInc/crewAI/releases/tag/1.15.45) — today
- **PydanticAI** [`v2.73.0`](https://github.com/pydantic/pydantic-ai/releases/tag/v2.73.0) — today
- **OpenAI Agents SDK** [`v0.26.0`](https://github.com/openai/openai-agents-python/releases/tag/v0.26.0) — today
- **Claude Agent SDK** [`v2.1.331`](https://github.com/anthropics/claude-code/releases/tag/v2.1.331) — today
- **AG2** [`v1.3.4`](https://github.com/ag2ai/ag2/releases/tag/v1.3.4) — 1 day ago
- **BrowserUse** [`1.0.8`](https://github.com/browser-use/browser-use/releases/tag/1.0.8) — 2 days ago
- **LangGraph** [`1.2.24`](https://github.com/langchain-ai/langgraph/releases/tag/1.2.24) — 4 days ago
- **Google ADK** [`v2.15.0`](https://github.com/google/adk-python/releases/tag/v2.15.0) — 4 days ago
- **Mastra** [`@mastra/core@1.84.0`](https://github.com/mastra-ai/mastra/releases/tag/@mastra/core@1.84.0) — 6 days ago

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

*Powered by GitHub Actions • Data refreshed daily • Last run: 2026-11-24 17:18 UTC*