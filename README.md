# 🔬 AI Agent Framework Pulse Tracker

[![Daily Update](https://github.com/PurpleHaze2320/ai-agent-pulse/actions/workflows/track.yml/badge.svg)](https://github.com/PurpleHaze2320/ai-agent-pulse/actions/workflows/track.yml)
[![Frameworks Tracked](https://img.shields.io/badge/frameworks-19-blue)](https://github.com/PurpleHaze2320/ai-agent-pulse)
[![License: MIT](https://img.shields.io/badge/License-MIT-green.svg)](https://opensource.org/licenses/MIT)
[![GitHub stars](https://img.shields.io/github/stars/PurpleHaze2320/ai-agent-pulse?style=social)](https://github.com/PurpleHaze2320/ai-agent-pulse/stargazers)

> Automated daily tracking of the AI agent framework ecosystem's health, momentum, and trends.
> Last updated: **2026-11-25 16:59 UTC** | Tracking **19** frameworks

## How It Works

This bot runs daily via GitHub Actions and collects metrics from the GitHub API for the most important
AI agent frameworks. It computes a **Pulse Score** (0-100) based on six weighted signals: star velocity,
release freshness, issue health, commit activity, community size, and fork engagement. The result is
a living dashboard that shows which frameworks are gaining momentum and which are losing steam.

## 🏆 Pulse Leaderboard

| Rank | Framework | Pulse | Stars | ⭐ 7d | Commits (4w) | Last Release | Category |
|------|-----------|-------|-------|-------|--------------|--------------|----------|
| 1 | [BrowserUse](https://github.com/browser-use/browser-use) | 🟢 **90.0** | 122.0k | 🚀 +633 | 1198 | 3 days ago | `web-agent` |
| 2 | [Claude Agent SDK](https://github.com/anthropics/claude-code) | 🟢 **85.4** | 157.0k | 🚀 +910 | 195 | today | `orchestration` |
| 3 | [Mastra](https://github.com/mastra-ai/mastra) | 🟢 **77.6** | 29.8k | 🚀 +210 | 2196 | today | `typescript` |
| 4 | [CrewAI](https://github.com/crewAIInc/crewAI) | 🟢 **77.3** | 61.3k | 🚀 +185 | 175 | 1 day ago | `multi-agent` |
| 5 | [LangGraph](https://github.com/langchain-ai/langgraph) | 🟢 **75.4** | 45.4k | 🚀 +299 | 75 | 5 days ago | `orchestration` |
| 6 | [Google ADK](https://github.com/google/adk-python) | 🟢 **74.8** | 22.4k | 📈 +90 | 265 | today | `orchestration` |
| 7 | [OpenAI Agents SDK](https://github.com/openai/openai-agents-python) | 🟢 **72.7** | 30.9k | 🚀 +120 | 86 | 1 day ago | `orchestration` |
| 8 | [Haystack](https://github.com/deepset-ai/haystack) | 🟢 **71.2** | 27.1k | 📈 +65 | 259 | 15 days ago | `pipeline` |
| 9 | [AG2](https://github.com/ag2ai/ag2) | 🟢 **70.1** | 5.1k | ↗️ +13 | 107 | 2 days ago | `multi-agent` |
| 10 | [Composio](https://github.com/ComposioHQ/composio) | 🟡 **68.8** | 31.3k | 🚀 +129 | 286 | 1 day ago | `tooling` |
| 11 | [Agno](https://github.com/agno-agi/agno) | 🟡 **68.6** | 43.3k | 📈 +65 | 107 | 7 days ago | `multi-agent` |
| 12 | [Semantic Kernel](https://github.com/microsoft/semantic-kernel) | 🟡 **57.8** | 28.8k | 📈 +21 | 37 | 18 days ago | `enterprise` |
| 13 | [LlamaIndex](https://github.com/run-llama/llama_index) | 🟡 **54.3** | 53.0k | 📈 +59 | 8 | 11 days ago | `data-agent` |
| 14 | [PydanticAI](https://github.com/pydantic/pydantic-ai) | 🟡 **49.1** | 21.4k | 🚀 +110 | 0 | 1 mo ago | `structured` |
| 15 | [DSPy](https://github.com/stanfordnlp/dspy) | 🟡 **48.2** | 39.2k | 🚀 +107 | 0 | 15 days ago | `optimization` |
| 16 | [Smolagents](https://github.com/huggingface/smolagents) | 🟠 **34.6** | 30.5k | 🚀 +103 | 22 | 6 mo ago | `lightweight` |
| 17 | [Letta](https://github.com/letta-ai/letta) | 🟠 **32.4** | 25.5k | 📈 +64 | 0 | 6 mo ago | `memory` |
| 18 | [AutoGen](https://github.com/microsoft/autogen) | 🟠 **30.4** | 62.0k | 📈 +44 | 1 | 1y ago | `multi-agent` |
| 19 | [Swarm](https://github.com/openai/swarm) | 🔴 **9.5** | 22.2k | ↗️ +20 | 0 | — | `experimental` |

## 📂 By Category

- `data-agent`: **LlamaIndex** (54.3)
- `enterprise`: **Semantic Kernel** (57.8)
- `experimental`: **Swarm** (9.5)
- `lightweight`: **Smolagents** (34.6)
- `memory`: **Letta** (32.4)
- `multi-agent`: **CrewAI** (77.3), **AG2** (70.1), **Agno** (68.6), **AutoGen** (30.4)
- `optimization`: **DSPy** (48.2)
- `orchestration`: **Claude Agent SDK** (85.4), **LangGraph** (75.4), **Google ADK** (74.8), **OpenAI Agents SDK** (72.7)
- `pipeline`: **Haystack** (71.2)
- `structured`: **PydanticAI** (49.1)
- `tooling`: **Composio** (68.8)
- `typescript`: **Mastra** (77.6)
- `web-agent`: **BrowserUse** (90.0)

## 🔍 Top 5 — Score Breakdown

| Framework | Star Velocity | Release Freshness | Issue Health | Commit Activity | Community | Fork Ratio |
|-----------|:---:|:---:|:---:|:---:|:---:|:---:|
| **BrowserUse** | 100 | 99.0 | 89.9 | 100 | 72.2 | 44.7 |
| **Claude Agent SDK** | 100 | 100.0 | 85.7 | 100 | 11.2 | 64.0 |
| **Mastra** | 40.3 | 100.0 | 93.0 | 100 | 93.2 | 42.1 |
| **CrewAI** | 43.0 | 99.7 | 85.1 | 100 | 78.4 | 60.6 |
| **LangGraph** | 64.2 | 98.3 | 79.8 | 75.0 | 57.6 | 69.2 |

## 💡 Key Insights

- **Hottest framework**: BrowserUse with a Pulse Score of 90.0
- **Fastest growing**: Claude Agent SDK gained +910 stars this week
- **Most active development**: Mastra with 2196 commits in the last 4 weeks
- **⚠️ Archived**: AutoGen
- **Stale releases**: AutoGen, Swarm haven't released in a while

## 📦 Recent Releases

- **Mastra** [`@mastra/core@1.86.0`](https://github.com/mastra-ai/mastra/releases/tag/@mastra/core@1.86.0) — today
- **Claude Agent SDK** [`v2.1.332`](https://github.com/anthropics/claude-code/releases/tag/v2.1.332) — today
- **Google ADK** [`v2.15.1`](https://github.com/google/adk-python/releases/tag/v2.15.1) — today
- **Composio** [`@composio/cli@0.6.4-beta.582`](https://github.com/ComposioHQ/composio/releases/tag/@composio/cli@0.6.4-beta.582) — 1 day ago *(pre-release)*
- **CrewAI** [`1.15.45`](https://github.com/crewAIInc/crewAI/releases/tag/1.15.45) — 1 day ago
- **OpenAI Agents SDK** [`v0.26.0`](https://github.com/openai/openai-agents-python/releases/tag/v0.26.0) — 1 day ago
- **AG2** [`v1.3.4`](https://github.com/ag2ai/ag2/releases/tag/v1.3.4) — 2 days ago
- **BrowserUse** [`1.0.8`](https://github.com/browser-use/browser-use/releases/tag/1.0.8) — 3 days ago
- **LangGraph** [`1.2.24`](https://github.com/langchain-ai/langgraph/releases/tag/1.2.24) — 5 days ago
- **Agno** [`v3.2.1`](https://github.com/agno-agi/agno/releases/tag/v3.2.1) — 7 days ago

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

*Powered by GitHub Actions • Data refreshed daily • Last run: 2026-11-25 16:59 UTC*