# 🔬 AI Agent Framework Pulse Tracker

[![Daily Update](https://github.com/PurpleHaze2320/ai-agent-pulse/actions/workflows/track.yml/badge.svg)](https://github.com/PurpleHaze2320/ai-agent-pulse/actions/workflows/track.yml)
[![Frameworks Tracked](https://img.shields.io/badge/frameworks-19-blue)](https://github.com/PurpleHaze2320/ai-agent-pulse)
[![License: MIT](https://img.shields.io/badge/License-MIT-green.svg)](https://opensource.org/licenses/MIT)
[![GitHub stars](https://img.shields.io/github/stars/PurpleHaze2320/ai-agent-pulse?style=social)](https://github.com/PurpleHaze2320/ai-agent-pulse/stargazers)

> Automated daily tracking of the AI agent framework ecosystem's health, momentum, and trends.
> Last updated: **2026-07-29 08:48 UTC** | Tracking **19** frameworks

## How It Works

This bot runs daily via GitHub Actions and collects metrics from the GitHub API for the most important
AI agent frameworks. It computes a **Pulse Score** (0-100) based on six weighted signals: star velocity,
release freshness, issue health, commit activity, community size, and fork engagement. The result is
a living dashboard that shows which frameworks are gaining momentum and which are losing steam.

## 🏆 Pulse Leaderboard

| Rank | Framework | Pulse | Stars | ⭐ 7d | Commits (4w) | Last Release | Category |
|------|-----------|-------|-------|-------|--------------|--------------|----------|
| 1 | [BrowserUse](https://github.com/browser-use/browser-use) | 🟢 **85.0** | 107.2k | 🚀 +1150 | 76 | 1 day ago | `web-agent` |
| 2 | [Mastra](https://github.com/mastra-ai/mastra) | 🟢 **80.2** | 26.7k | 🚀 +256 | 1018 | today | `typescript` |
| 3 | [CrewAI](https://github.com/crewAIInc/crewAI) | 🟢 **79.3** | 56.3k | 🚀 +362 | 70 | today | `multi-agent` |
| 4 | [PydanticAI](https://github.com/pydantic/pydantic-ai) | 🟢 **75.7** | 18.9k | 🚀 +147 | 216 | today | `structured` |
| 5 | [Agno](https://github.com/agno-agi/agno) | 🟢 **73.3** | 41.5k | 🚀 +136 | 135 | 1 day ago | `multi-agent` |
| 6 | [Google ADK](https://github.com/google/adk-python) | 🟢 **73.3** | 20.9k | 📈 +95 | 308 | 7 days ago | `orchestration` |
| 7 | [LangGraph](https://github.com/langchain-ai/langgraph) | 🟢 **71.8** | 38.4k | 🚀 +568 | 19 | today | `orchestration` |
| 8 | [Claude Agent SDK](https://github.com/anthropics/claude-code) | 🟡 **68.9** | 139.5k | 🚀 +822 | 21 | 4 days ago | `orchestration` |
| 9 | [Composio](https://github.com/ComposioHQ/composio) | 🟡 **67.6** | 29.4k | 🚀 +117 | 143 | 8 days ago | `tooling` |
| 10 | [LlamaIndex](https://github.com/run-llama/llama_index) | 🟡 **57.0** | 51.2k | 🚀 +184 | 0 | 1 mo ago | `data-agent` |
| 11 | [OpenAI Agents SDK](https://github.com/openai/openai-agents-python) | 🟡 **56.6** | 28.3k | 🚀 +185 | 0 | today | `orchestration` |
| 12 | [Semantic Kernel](https://github.com/microsoft/semantic-kernel) | 🟡 **53.4** | 28.4k | 📈 +40 | 17 | 21 days ago | `enterprise` |
| 13 | [AG2](https://github.com/ag2ai/ag2) | 🟡 **50.5** | 4.8k | 📈 +27 | 0 | today | `multi-agent` |
| 14 | [Haystack](https://github.com/deepset-ai/haystack) | 🟡 **50.1** | 26.1k | 📈 +70 | 0 | 8 days ago | `pipeline` |
| 15 | [DSPy](https://github.com/stanfordnlp/dspy) | 🟡 **48.1** | 36.4k | 🚀 +151 | 0 | 2 mo ago | `optimization` |
| 16 | [Letta](https://github.com/letta-ai/letta) | 🟡 **41.9** | 24.0k | 📈 +99 | 0 | 2 mo ago | `memory` |
| 17 | [Smolagents](https://github.com/huggingface/smolagents) | 🟠 **39.8** | 28.6k | 📈 +95 | 4 | 2 mo ago | `lightweight` |
| 18 | [AutoGen](https://github.com/microsoft/autogen) | 🟠 **36.2** | 60.1k | 🚀 +180 | 0 | 10 mo ago | `multi-agent` |
| 19 | [Swarm](https://github.com/openai/swarm) | 🔴 **9.5** | 21.9k | ↗️ +13 | 0 | — | `experimental` |

## 📂 By Category

- `data-agent`: **LlamaIndex** (57.0)
- `enterprise`: **Semantic Kernel** (53.4)
- `experimental`: **Swarm** (9.5)
- `lightweight`: **Smolagents** (39.8)
- `memory`: **Letta** (41.9)
- `multi-agent`: **CrewAI** (79.3), **Agno** (73.3), **AG2** (50.5), **AutoGen** (36.2)
- `optimization`: **DSPy** (48.1)
- `orchestration`: **Google ADK** (73.3), **LangGraph** (71.8), **Claude Agent SDK** (68.9), **OpenAI Agents SDK** (56.6)
- `pipeline`: **Haystack** (50.1)
- `structured`: **PydanticAI** (75.7)
- `tooling`: **Composio** (67.6)
- `typescript`: **Mastra** (80.2)
- `web-agent`: **BrowserUse** (85.0)

## 🔍 Top 5 — Score Breakdown

| Framework | Star Velocity | Release Freshness | Issue Health | Commit Activity | Community | Fork Ratio |
|-----------|:---:|:---:|:---:|:---:|:---:|:---:|
| **BrowserUse** | 100 | 99.7 | 94.7 | 76.0 | 63.0 | 44.0 |
| **Mastra** | 52.7 | 100.0 | 93.0 | 100 | 92.8 | 37.8 |
| **CrewAI** | 77.1 | 100.0 | 95.8 | 70.0 | 59.6 | 56.9 |
| **PydanticAI** | 32.8 | 100.0 | 85.8 | 100 | 94.8 | 51.7 |
| **Agno** | 27.9 | 99.7 | 80.2 | 100 | 88.8 | 55.1 |

## 💡 Key Insights

- **Hottest framework**: BrowserUse with a Pulse Score of 85.0
- **Fastest growing**: BrowserUse gained +1150 stars this week
- **Most active development**: Mastra with 1018 commits in the last 4 weeks
- **Stale releases**: AutoGen, Swarm haven't released in a while

## 📦 Recent Releases

- **Mastra** [`@mastra/core@1.53.0`](https://github.com/mastra-ai/mastra/releases/tag/@mastra/core@1.53.0) — today
- **OpenAI Agents SDK** [`v0.19.1`](https://github.com/openai/openai-agents-python/releases/tag/v0.19.1) — today
- **AG2** [`v1.0.1`](https://github.com/ag2ai/ag2/releases/tag/v1.0.1) — today
- **PydanticAI** [`v2.20.0`](https://github.com/pydantic/pydantic-ai/releases/tag/v2.20.0) — today
- **LangGraph** [`1.2.10`](https://github.com/langchain-ai/langgraph/releases/tag/1.2.10) — today
- **CrewAI** [`1.15.8`](https://github.com/crewAIInc/crewAI/releases/tag/1.15.8) — today
- **BrowserUse** [`0.13.7`](https://github.com/browser-use/browser-use/releases/tag/0.13.7) — 1 day ago
- **Agno** [`v2.8.5`](https://github.com/agno-agi/agno/releases/tag/v2.8.5) — 1 day ago
- **Claude Agent SDK** [`v2.1.220`](https://github.com/anthropics/claude-code/releases/tag/v2.1.220) — 4 days ago
- **Google ADK** [`v1.36.2`](https://github.com/google/adk-python/releases/tag/v1.36.2) — 7 days ago

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

*Powered by GitHub Actions • Data refreshed daily • Last run: 2026-07-29 08:48 UTC*