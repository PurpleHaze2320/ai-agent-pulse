# 🔬 AI Agent Framework Pulse Tracker

[![Daily Update](https://github.com/PurpleHaze2320/ai-agent-pulse/actions/workflows/track.yml/badge.svg)](https://github.com/PurpleHaze2320/ai-agent-pulse/actions/workflows/track.yml)
[![Frameworks Tracked](https://img.shields.io/badge/frameworks-19-blue)](https://github.com/PurpleHaze2320/ai-agent-pulse)
[![License: MIT](https://img.shields.io/badge/License-MIT-green.svg)](https://opensource.org/licenses/MIT)
[![GitHub stars](https://img.shields.io/github/stars/PurpleHaze2320/ai-agent-pulse?style=social)](https://github.com/PurpleHaze2320/ai-agent-pulse/stargazers)

> Automated daily tracking of the AI agent framework ecosystem's health, momentum, and trends.
> Last updated: **2026-11-22 14:22 UTC** | Tracking **19** frameworks

## How It Works

This bot runs daily via GitHub Actions and collects metrics from the GitHub API for the most important
AI agent frameworks. It computes a **Pulse Score** (0-100) based on six weighted signals: star velocity,
release freshness, issue health, commit activity, community size, and fork engagement. The result is
a living dashboard that shows which frameworks are gaining momentum and which are losing steam.

## 🏆 Pulse Leaderboard

| Rank | Framework | Pulse | Stars | ⭐ 7d | Commits (4w) | Last Release | Category |
|------|-----------|-------|-------|-------|--------------|--------------|----------|
| 1 | [BrowserUse](https://github.com/browser-use/browser-use) | 🟢 **90.2** | 121.7k | 🚀 +657 | 1195 | today | `web-agent` |
| 2 | [Claude Agent SDK](https://github.com/anthropics/claude-code) | 🟢 **85.3** | 156.6k | 🚀 +903 | 146 | 1 day ago | `orchestration` |
| 3 | [CrewAI](https://github.com/crewAIInc/crewAI) | 🟢 **78.3** | 61.2k | 🚀 +222 | 144 | 2 days ago | `multi-agent` |
| 4 | [Mastra](https://github.com/mastra-ai/mastra) | 🟢 **76.8** | 29.7k | 🚀 +199 | 1845 | 4 days ago | `typescript` |
| 5 | [Google ADK](https://github.com/google/adk-python) | 🟢 **74.5** | 22.3k | 📈 +84 | 245 | 2 days ago | `orchestration` |
| 6 | [LangGraph](https://github.com/langchain-ai/langgraph) | 🟢 **74.0** | 45.3k | 🚀 +275 | 71 | 2 days ago | `orchestration` |
| 7 | [Haystack](https://github.com/deepset-ai/haystack) | 🟢 **71.3** | 27.1k | 📈 +64 | 217 | 12 days ago | `pipeline` |
| 8 | [Composio](https://github.com/ComposioHQ/composio) | 🟡 **69.6** | 31.2k | 🚀 +152 | 240 | 1 day ago | `tooling` |
| 9 | [PydanticAI](https://github.com/pydantic/pydantic-ai) | 🟡 **69.5** | 21.3k | 🚀 +112 | 803 | 1 mo ago | `structured` |
| 10 | [OpenAI Agents SDK](https://github.com/openai/openai-agents-python) | 🟡 **68.4** | 30.8k | 🚀 +119 | 65 | 1 day ago | `orchestration` |
| 11 | [AG2](https://github.com/ag2ai/ag2) | 🟡 **67.9** | 5.1k | ↗️ +13 | 89 | 2 days ago | `multi-agent` |
| 12 | [Agno](https://github.com/agno-agi/agno) | 🟡 **67.5** | 43.3k | 📈 +62 | 94 | 4 days ago | `multi-agent` |
| 13 | [DSPy](https://github.com/stanfordnlp/dspy) | 🟡 **59.9** | 39.2k | 🚀 +110 | 57 | 11 days ago | `optimization` |
| 14 | [Semantic Kernel](https://github.com/microsoft/semantic-kernel) | 🟡 **57.9** | 28.8k | 📈 +21 | 37 | 15 days ago | `enterprise` |
| 15 | [LlamaIndex](https://github.com/run-llama/llama_index) | 🟡 **55.1** | 53.0k | 📈 +73 | 8 | 8 days ago | `data-agent` |
| 16 | [Smolagents](https://github.com/huggingface/smolagents) | 🟠 **33.8** | 30.5k | 🚀 +106 | 17 | 5 mo ago | `lightweight` |
| 17 | [AutoGen](https://github.com/microsoft/autogen) | 🟠 **33.0** | 62.0k | 🚀 +116 | 1 | 1y ago | `multi-agent` |
| 18 | [Letta](https://github.com/letta-ai/letta) | 🟠 **32.4** | 25.5k | 📈 +62 | 0 | 6 mo ago | `memory` |
| 19 | [Swarm](https://github.com/openai/swarm) | 🔴 **9.2** | 22.2k | ↗️ +15 | 0 | — | `experimental` |

## 📂 By Category

- `data-agent`: **LlamaIndex** (55.1)
- `enterprise`: **Semantic Kernel** (57.9)
- `experimental`: **Swarm** (9.2)
- `lightweight`: **Smolagents** (33.8)
- `memory`: **Letta** (32.4)
- `multi-agent`: **CrewAI** (78.3), **AG2** (67.9), **Agno** (67.5), **AutoGen** (33.0)
- `optimization`: **DSPy** (59.9)
- `orchestration`: **Claude Agent SDK** (85.3), **Google ADK** (74.5), **LangGraph** (74.0), **OpenAI Agents SDK** (68.4)
- `pipeline`: **Haystack** (71.3)
- `structured`: **PydanticAI** (69.5)
- `tooling`: **Composio** (69.6)
- `typescript`: **Mastra** (76.8)
- `web-agent`: **BrowserUse** (90.2)

## 🔍 Top 5 — Score Breakdown

| Framework | Star Velocity | Release Freshness | Issue Health | Commit Activity | Community | Fork Ratio |
|-----------|:---:|:---:|:---:|:---:|:---:|:---:|
| **BrowserUse** | 100 | 100.0 | 90.0 | 100 | 72.2 | 44.7 |
| **Claude Agent SDK** | 100 | 99.7 | 85.8 | 100 | 11.2 | 64.1 |
| **CrewAI** | 48.2 | 99.3 | 84.4 | 100 | 77.0 | 60.4 |
| **Mastra** | 38.4 | 98.7 | 93.2 | 100 | 93.2 | 42.1 |
| **Google ADK** | 16.8 | 99.3 | 92.6 | 100 | 86.0 | 79.2 |

## 💡 Key Insights

- **Hottest framework**: BrowserUse with a Pulse Score of 90.2
- **Fastest growing**: Claude Agent SDK gained +903 stars this week
- **Most active development**: Mastra with 1845 commits in the last 4 weeks
- **⚠️ Archived**: AutoGen
- **Stale releases**: AutoGen, Swarm haven't released in a while

## 📦 Recent Releases

- **BrowserUse** [`1.0.8`](https://github.com/browser-use/browser-use/releases/tag/1.0.8) — today
- **Claude Agent SDK** [`v2.1.330`](https://github.com/anthropics/claude-code/releases/tag/v2.1.330) — 1 day ago
- **OpenAI Agents SDK** [`v1.0.0-alpha.1`](https://github.com/openai/openai-agents-python/releases/tag/v1.0.0-alpha.1) — 1 day ago *(pre-release)*
- **Composio** [`@composio/cli@0.6.4-beta.573`](https://github.com/ComposioHQ/composio/releases/tag/@composio/cli@0.6.4-beta.573) — 1 day ago *(pre-release)*
- **LangGraph** [`1.2.24`](https://github.com/langchain-ai/langgraph/releases/tag/1.2.24) — 2 days ago
- **Google ADK** [`v2.15.0`](https://github.com/google/adk-python/releases/tag/v2.15.0) — 2 days ago
- **AG2** [`v1.3.3`](https://github.com/ag2ai/ag2/releases/tag/v1.3.3) — 2 days ago
- **CrewAI** [`1.15.44`](https://github.com/crewAIInc/crewAI/releases/tag/1.15.44) — 2 days ago
- **Mastra** [`@mastra/core@1.84.0`](https://github.com/mastra-ai/mastra/releases/tag/@mastra/core@1.84.0) — 4 days ago
- **Agno** [`v3.2.1`](https://github.com/agno-agi/agno/releases/tag/v3.2.1) — 4 days ago

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

*Powered by GitHub Actions • Data refreshed daily • Last run: 2026-11-22 14:22 UTC*