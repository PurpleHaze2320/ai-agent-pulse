# 🔬 AI Agent Framework Pulse Tracker

[![Daily Update](https://github.com/PurpleHaze2320/ai-agent-pulse/actions/workflows/track.yml/badge.svg)](https://github.com/PurpleHaze2320/ai-agent-pulse/actions/workflows/track.yml)
[![Frameworks Tracked](https://img.shields.io/badge/frameworks-19-blue)](https://github.com/PurpleHaze2320/ai-agent-pulse)
[![License: MIT](https://img.shields.io/badge/License-MIT-green.svg)](https://opensource.org/licenses/MIT)
[![GitHub stars](https://img.shields.io/github/stars/PurpleHaze2320/ai-agent-pulse?style=social)](https://github.com/PurpleHaze2320/ai-agent-pulse/stargazers)

> Automated daily tracking of the AI agent framework ecosystem's health, momentum, and trends.
> Last updated: **2026-07-31 08:56 UTC** | Tracking **19** frameworks

## How It Works

This bot runs daily via GitHub Actions and collects metrics from the GitHub API for the most important
AI agent frameworks. It computes a **Pulse Score** (0-100) based on six weighted signals: star velocity,
release freshness, issue health, commit activity, community size, and fork engagement. The result is
a living dashboard that shows which frameworks are gaining momentum and which are losing steam.

## 🏆 Pulse Leaderboard

| Rank | Framework | Pulse | Stars | ⭐ 7d | Commits (4w) | Last Release | Category |
|------|-----------|-------|-------|-------|--------------|--------------|----------|
| 1 | [BrowserUse](https://github.com/browser-use/browser-use) | 🟢 **84.9** | 107.4k | 🚀 +905 | 76 | 3 days ago | `web-agent` |
| 2 | [CrewAI](https://github.com/crewAIInc/crewAI) | 🟢 **80.3** | 56.4k | 🚀 +358 | 77 | 1 day ago | `multi-agent` |
| 3 | [Mastra](https://github.com/mastra-ai/mastra) | 🟢 **80.0** | 26.8k | 🚀 +246 | 1187 | today | `typescript` |
| 4 | [OpenAI Agents SDK](https://github.com/openai/openai-agents-python) | 🟢 **75.9** | 28.3k | 🚀 +169 | 177 | 2 days ago | `orchestration` |
| 5 | [PydanticAI](https://github.com/pydantic/pydantic-ai) | 🟢 **75.2** | 18.9k | 🚀 +140 | 262 | 1 day ago | `structured` |
| 6 | [Google ADK](https://github.com/google/adk-python) | 🟢 **73.7** | 21.0k | 📈 +93 | 358 | today | `orchestration` |
| 7 | [Agno](https://github.com/agno-agi/agno) | 🟢 **72.9** | 41.5k | 🚀 +122 | 138 | today | `multi-agent` |
| 8 | [LangGraph](https://github.com/langchain-ai/langgraph) | 🟢 **72.4** | 38.6k | 🚀 +550 | 22 | today | `orchestration` |
| 9 | [Haystack](https://github.com/deepset-ai/haystack) | 🟢 **70.2** | 26.1k | 📈 +75 | 256 | 10 days ago | `pipeline` |
| 10 | [Claude Agent SDK](https://github.com/anthropics/claude-code) | 🟡 **68.8** | 139.7k | 🚀 +837 | 21 | 6 days ago | `orchestration` |
| 11 | [LlamaIndex](https://github.com/run-llama/llama_index) | 🟡 **57.2** | 51.3k | 🚀 +194 | 0 | 1 mo ago | `data-agent` |
| 12 | [AG2](https://github.com/ag2ai/ag2) | 🟡 **50.5** | 4.8k | 📈 +29 | 0 | 2 days ago | `multi-agent` |
| 13 | [Semantic Kernel](https://github.com/microsoft/semantic-kernel) | 🟡 **49.9** | 28.4k | 📈 +43 | 0 | 23 days ago | `enterprise` |
| 14 | [Composio](https://github.com/ComposioHQ/composio) | 🟡 **48.5** | 29.5k | 🚀 +127 | 0 | today | `tooling` |
| 15 | [DSPy](https://github.com/stanfordnlp/dspy) | 🟡 **47.8** | 36.5k | 🚀 +155 | 0 | 2 mo ago | `optimization` |
| 16 | [Letta](https://github.com/letta-ai/letta) | 🟡 **42.0** | 24.0k | 🚀 +101 | 1 | 2 mo ago | `memory` |
| 17 | [Smolagents](https://github.com/huggingface/smolagents) | 🟠 **39.5** | 28.6k | 📈 +94 | 4 | 2 mo ago | `lightweight` |
| 18 | [AutoGen](https://github.com/microsoft/autogen) | 🟠 **36.7** | 60.1k | 🚀 +194 | 0 | 10 mo ago | `multi-agent` |
| 19 | [Swarm](https://github.com/openai/swarm) | 🔴 **9.5** | 21.9k | ↗️ +13 | 0 | — | `experimental` |

## 📂 By Category

- `data-agent`: **LlamaIndex** (57.2)
- `enterprise`: **Semantic Kernel** (49.9)
- `experimental`: **Swarm** (9.5)
- `lightweight`: **Smolagents** (39.5)
- `memory`: **Letta** (42.0)
- `multi-agent`: **CrewAI** (80.3), **Agno** (72.9), **AG2** (50.5), **AutoGen** (36.7)
- `optimization`: **DSPy** (47.8)
- `orchestration`: **OpenAI Agents SDK** (75.9), **Google ADK** (73.7), **LangGraph** (72.4), **Claude Agent SDK** (68.8)
- `pipeline`: **Haystack** (70.2)
- `structured`: **PydanticAI** (75.2)
- `tooling`: **Composio** (48.5)
- `typescript`: **Mastra** (80.0)
- `web-agent`: **BrowserUse** (84.9)

## 🔍 Top 5 — Score Breakdown

| Framework | Star Velocity | Release Freshness | Issue Health | Commit Activity | Community | Fork Ratio |
|-----------|:---:|:---:|:---:|:---:|:---:|:---:|
| **BrowserUse** | 100 | 99.0 | 94.5 | 76.0 | 63.0 | 44.0 |
| **CrewAI** | 76.2 | 99.7 | 95.4 | 77.0 | 59.6 | 56.9 |
| **Mastra** | 51.2 | 100.0 | 93.9 | 100 | 93.0 | 38.0 |
| **OpenAI Agents SDK** | 35.1 | 99.3 | 97.8 | 100 | 63.6 | 62.3 |
| **PydanticAI** | 31.6 | 99.7 | 84.4 | 100 | 94.8 | 51.8 |

## 💡 Key Insights

- **Hottest framework**: BrowserUse with a Pulse Score of 84.9
- **Fastest growing**: BrowserUse gained +905 stars this week
- **Most active development**: Mastra with 1187 commits in the last 4 weeks
- **Stale releases**: AutoGen, Swarm haven't released in a while

## 📦 Recent Releases

- **LangGraph** [`checkpointsqlite==3.1.1`](https://github.com/langchain-ai/langgraph/releases/tag/checkpointsqlite==3.1.1) — today
- **Google ADK** [`v2.6.0`](https://github.com/google/adk-python/releases/tag/v2.6.0) — today
- **Agno** [`v2.8.6`](https://github.com/agno-agi/agno/releases/tag/v2.8.6) — today
- **Mastra** [`@mastra/core@1.54.0`](https://github.com/mastra-ai/mastra/releases/tag/@mastra/core@1.54.0) — today
- **Composio** [`@composio/slim@0.14.1`](https://github.com/ComposioHQ/composio/releases/tag/@composio/slim@0.14.1) — today
- **CrewAI** [`1.15.9`](https://github.com/crewAIInc/crewAI/releases/tag/1.15.9) — 1 day ago
- **PydanticAI** [`v2.21.0`](https://github.com/pydantic/pydantic-ai/releases/tag/v2.21.0) — 1 day ago
- **OpenAI Agents SDK** [`v0.19.1`](https://github.com/openai/openai-agents-python/releases/tag/v0.19.1) — 2 days ago
- **AG2** [`v1.0.1`](https://github.com/ag2ai/ag2/releases/tag/v1.0.1) — 2 days ago
- **BrowserUse** [`0.13.7`](https://github.com/browser-use/browser-use/releases/tag/0.13.7) — 3 days ago

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

*Powered by GitHub Actions • Data refreshed daily • Last run: 2026-07-31 08:56 UTC*