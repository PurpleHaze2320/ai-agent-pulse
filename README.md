# 🔬 AI Agent Framework Pulse Tracker

[![Daily Update](https://github.com/PurpleHaze2320/ai-agent-pulse/actions/workflows/track.yml/badge.svg)](https://github.com/PurpleHaze2320/ai-agent-pulse/actions/workflows/track.yml)
[![Frameworks Tracked](https://img.shields.io/badge/frameworks-19-blue)](https://github.com/PurpleHaze2320/ai-agent-pulse)
[![License: MIT](https://img.shields.io/badge/License-MIT-green.svg)](https://opensource.org/licenses/MIT)
[![GitHub stars](https://img.shields.io/github/stars/PurpleHaze2320/ai-agent-pulse?style=social)](https://github.com/PurpleHaze2320/ai-agent-pulse/stargazers)

> Automated daily tracking of the AI agent framework ecosystem's health, momentum, and trends.
> Last updated: **2026-08-01 08:27 UTC** | Tracking **19** frameworks

## How It Works

This bot runs daily via GitHub Actions and collects metrics from the GitHub API for the most important
AI agent frameworks. It computes a **Pulse Score** (0-100) based on six weighted signals: star velocity,
release freshness, issue health, commit activity, community size, and fork engagement. The result is
a living dashboard that shows which frameworks are gaining momentum and which are losing steam.

## 🏆 Pulse Leaderboard

| Rank | Framework | Pulse | Stars | ⭐ 7d | Commits (4w) | Last Release | Category |
|------|-----------|-------|-------|-------|--------------|--------------|----------|
| 1 | [BrowserUse](https://github.com/browser-use/browser-use) | 🟢 **84.8** | 107.5k | 🚀 +769 | 76 | 4 days ago | `web-agent` |
| 2 | [CrewAI](https://github.com/crewAIInc/crewAI) | 🟢 **80.5** | 56.4k | 🚀 +347 | 80 | today | `multi-agent` |
| 3 | [Mastra](https://github.com/mastra-ai/mastra) | 🟢 **80.1** | 26.8k | 🚀 +251 | 1216 | today | `typescript` |
| 4 | [PydanticAI](https://github.com/pydantic/pydantic-ai) | 🟢 **75.1** | 18.9k | 🚀 +137 | 273 | today | `structured` |
| 5 | [Google ADK](https://github.com/google/adk-python) | 🟢 **73.6** | 21.0k | 📈 +90 | 373 | today | `orchestration` |
| 6 | [Agno](https://github.com/agno-agi/agno) | 🟢 **72.5** | 41.5k | 🚀 +116 | 138 | 1 day ago | `multi-agent` |
| 7 | [LangGraph](https://github.com/langchain-ai/langgraph) | 🟢 **72.3** | 38.6k | 🚀 +510 | 22 | 1 day ago | `orchestration` |
| 8 | [Haystack](https://github.com/deepset-ai/haystack) | 🟡 **69.8** | 26.1k | 📈 +65 | 262 | 11 days ago | `pipeline` |
| 9 | [Claude Agent SDK](https://github.com/anthropics/claude-code) | 🟡 **68.7** | 139.9k | 🚀 +860 | 21 | 7 days ago | `orchestration` |
| 10 | [Composio](https://github.com/ComposioHQ/composio) | 🟡 **68.0** | 29.5k | 🚀 +118 | 198 | 1 day ago | `tooling` |
| 11 | [LlamaIndex](https://github.com/run-llama/llama_index) | 🟡 **60.3** | 51.3k | 🚀 +189 | 17 | 1 mo ago | `data-agent` |
| 12 | [OpenAI Agents SDK](https://github.com/openai/openai-agents-python) | 🟡 **56.1** | 28.3k | 🚀 +169 | 0 | today | `orchestration` |
| 13 | [AG2](https://github.com/ag2ai/ag2) | 🟡 **50.2** | 4.8k | 📈 +24 | 0 | 3 days ago | `multi-agent` |
| 14 | [Semantic Kernel](https://github.com/microsoft/semantic-kernel) | 🟡 **49.6** | 28.4k | 📈 +37 | 0 | 24 days ago | `enterprise` |
| 15 | [DSPy](https://github.com/stanfordnlp/dspy) | 🟡 **47.3** | 36.5k | 🚀 +143 | 0 | 2 mo ago | `optimization` |
| 16 | [Letta](https://github.com/letta-ai/letta) | 🟡 **41.7** | 24.0k | 📈 +96 | 1 | 2 mo ago | `memory` |
| 17 | [Smolagents](https://github.com/huggingface/smolagents) | 🟠 **39.3** | 28.6k | 📈 +91 | 4 | 2 mo ago | `lightweight` |
| 18 | [AutoGen](https://github.com/microsoft/autogen) | 🟠 **36.3** | 60.1k | 🚀 +184 | 0 | 10 mo ago | `multi-agent` |
| 19 | [Swarm](https://github.com/openai/swarm) | 🔴 **9.5** | 21.9k | ↗️ +13 | 0 | — | `experimental` |

## 📂 By Category

- `data-agent`: **LlamaIndex** (60.3)
- `enterprise`: **Semantic Kernel** (49.6)
- `experimental`: **Swarm** (9.5)
- `lightweight`: **Smolagents** (39.3)
- `memory`: **Letta** (41.7)
- `multi-agent`: **CrewAI** (80.5), **Agno** (72.5), **AG2** (50.2), **AutoGen** (36.3)
- `optimization`: **DSPy** (47.3)
- `orchestration`: **Google ADK** (73.6), **LangGraph** (72.3), **Claude Agent SDK** (68.7), **OpenAI Agents SDK** (56.1)
- `pipeline`: **Haystack** (69.8)
- `structured`: **PydanticAI** (75.1)
- `tooling`: **Composio** (68.0)
- `typescript`: **Mastra** (80.1)
- `web-agent`: **BrowserUse** (84.8)

## 🔍 Top 5 — Score Breakdown

| Framework | Star Velocity | Release Freshness | Issue Health | Commit Activity | Community | Fork Ratio |
|-----------|:---:|:---:|:---:|:---:|:---:|:---:|
| **BrowserUse** | 100 | 98.7 | 94.5 | 76.0 | 63.0 | 44.0 |
| **CrewAI** | 74.0 | 100.0 | 95.4 | 80.0 | 59.8 | 56.9 |
| **Mastra** | 51.6 | 100.0 | 93.8 | 100 | 93.0 | 38.0 |
| **PydanticAI** | 31.1 | 100.0 | 84.6 | 100 | 94.8 | 51.9 |
| **Google ADK** | 21.0 | 100.0 | 88.2 | 100 | 79.2 | 72.1 |

## 💡 Key Insights

- **Hottest framework**: BrowserUse with a Pulse Score of 84.8
- **Fastest growing**: Claude Agent SDK gained +860 stars this week
- **Most active development**: Mastra with 1216 commits in the last 4 weeks
- **Stale releases**: AutoGen, Swarm haven't released in a while

## 📦 Recent Releases

- **PydanticAI** [`v2.22.0`](https://github.com/pydantic/pydantic-ai/releases/tag/v2.22.0) — today
- **OpenAI Agents SDK** [`v0.19.2`](https://github.com/openai/openai-agents-python/releases/tag/v0.19.2) — today
- **Google ADK** [`v2.6.1`](https://github.com/google/adk-python/releases/tag/v2.6.1) — today
- **CrewAI** [`1.15.10`](https://github.com/crewAIInc/crewAI/releases/tag/1.15.10) — today
- **Mastra** [`@mastra/core@1.55.0`](https://github.com/mastra-ai/mastra/releases/tag/@mastra/core@1.55.0) — today
- **LangGraph** [`checkpointsqlite==3.1.1`](https://github.com/langchain-ai/langgraph/releases/tag/checkpointsqlite==3.1.1) — 1 day ago
- **Agno** [`v2.8.6`](https://github.com/agno-agi/agno/releases/tag/v2.8.6) — 1 day ago
- **Composio** [`@composio/slim@0.14.1`](https://github.com/ComposioHQ/composio/releases/tag/@composio/slim@0.14.1) — 1 day ago
- **AG2** [`v1.0.1`](https://github.com/ag2ai/ag2/releases/tag/v1.0.1) — 3 days ago
- **BrowserUse** [`0.13.7`](https://github.com/browser-use/browser-use/releases/tag/0.13.7) — 4 days ago

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

*Powered by GitHub Actions • Data refreshed daily • Last run: 2026-08-01 08:27 UTC*