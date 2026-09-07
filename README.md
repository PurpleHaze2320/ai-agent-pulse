# 🔬 AI Agent Framework Pulse Tracker

[![Daily Update](https://github.com/PurpleHaze2320/ai-agent-pulse/actions/workflows/track.yml/badge.svg)](https://github.com/PurpleHaze2320/ai-agent-pulse/actions/workflows/track.yml)
[![Frameworks Tracked](https://img.shields.io/badge/frameworks-19-blue)](https://github.com/PurpleHaze2320/ai-agent-pulse)
[![License: MIT](https://img.shields.io/badge/License-MIT-green.svg)](https://opensource.org/licenses/MIT)
[![GitHub stars](https://img.shields.io/github/stars/PurpleHaze2320/ai-agent-pulse?style=social)](https://github.com/PurpleHaze2320/ai-agent-pulse/stargazers)

> Automated daily tracking of the AI agent framework ecosystem's health, momentum, and trends.
> Last updated: **2026-09-07 12:03 UTC** | Tracking **19** frameworks

## How It Works

This bot runs daily via GitHub Actions and collects metrics from the GitHub API for the most important
AI agent frameworks. It computes a **Pulse Score** (0-100) based on six weighted signals: star velocity,
release freshness, issue health, commit activity, community size, and fork engagement. The result is
a living dashboard that shows which frameworks are gaining momentum and which are losing steam.

## 🏆 Pulse Leaderboard

| Rank | Framework | Pulse | Stars | ⭐ 7d | Commits (4w) | Last Release | Category |
|------|-----------|-------|-------|-------|--------------|--------------|----------|
| 1 | [BrowserUse](https://github.com/browser-use/browser-use) | 🟢 **90.3** | 112.9k | 🚀 +1043 | 179 | 3 days ago | `web-agent` |
| 2 | [CrewAI](https://github.com/crewAIInc/crewAI) | 🟢 **78.4** | 58.2k | 🚀 +317 | 79 | 2 days ago | `multi-agent` |
| 3 | [Mastra](https://github.com/mastra-ai/mastra) | 🟢 **76.1** | 27.8k | 🚀 +170 | 1160 | 2 days ago | `typescript` |
| 4 | [OpenAI Agents SDK](https://github.com/openai/openai-agents-python) | 🟢 **75.4** | 29.2k | 🚀 +149 | 122 | 18 days ago | `orchestration` |
| 5 | [Google ADK](https://github.com/google/adk-python) | 🟢 **73.6** | 21.4k | 📈 +96 | 341 | 10 days ago | `orchestration` |
| 6 | [Haystack](https://github.com/deepset-ai/haystack) | 🟢 **71.2** | 26.4k | 📈 +67 | 177 | 4 days ago | `pipeline` |
| 7 | [Claude Agent SDK](https://github.com/anthropics/claude-code) | 🟢 **70.1** | 144.3k | 🚀 +784 | 24 | 1 day ago | `orchestration` |
| 8 | [LangGraph](https://github.com/langchain-ai/langgraph) | 🟡 **68.6** | 41.2k | 🚀 +392 | 28 | 10 days ago | `orchestration` |
| 9 | [Composio](https://github.com/ComposioHQ/composio) | 🟡 **68.3** | 30.1k | 🚀 +112 | 207 | today | `tooling` |
| 10 | [Agno](https://github.com/agno-agi/agno) | 🟡 **67.1** | 42.1k | 📈 +99 | 81 | 2 days ago | `multi-agent` |
| 11 | [DSPy](https://github.com/stanfordnlp/dspy) | 🟡 **62.0** | 37.8k | 🚀 +141 | 51 | 16 days ago | `optimization` |
| 12 | [LlamaIndex](https://github.com/run-llama/llama_index) | 🟡 **61.7** | 52.1k | 🚀 +113 | 32 | 18 days ago | `data-agent` |
| 13 | [PydanticAI](https://github.com/pydantic/pydantic-ai) | 🟡 **54.7** | 19.8k | 🚀 +153 | 0 | 2 days ago | `structured` |
| 14 | [Semantic Kernel](https://github.com/microsoft/semantic-kernel) | 🟡 **54.6** | 28.5k | 📈 +21 | 21 | 3 days ago | `enterprise` |
| 15 | [AG2](https://github.com/ag2ai/ag2) | 🟡 **49.9** | 4.9k | ↗️ +13 | 0 | today | `multi-agent` |
| 16 | [Letta](https://github.com/letta-ai/letta) | 🟡 **40.9** | 24.6k | 🚀 +133 | 1 | 3 mo ago | `memory` |
| 17 | [Smolagents](https://github.com/huggingface/smolagents) | 🟠 **37.7** | 29.2k | 🚀 +134 | 2 | 3 mo ago | `lightweight` |
| 18 | [AutoGen](https://github.com/microsoft/autogen) | 🟠 **34.0** | 60.9k | 🚀 +136 | 0 | 11 mo ago | `multi-agent` |
| 19 | [Swarm](https://github.com/openai/swarm) | 🔴 **9.1** | 21.9k | ↗️ +11 | 0 | — | `experimental` |

## 📂 By Category

- `data-agent`: **LlamaIndex** (61.7)
- `enterprise`: **Semantic Kernel** (54.6)
- `experimental`: **Swarm** (9.1)
- `lightweight`: **Smolagents** (37.7)
- `memory`: **Letta** (40.9)
- `multi-agent`: **CrewAI** (78.4), **Agno** (67.1), **AG2** (49.9), **AutoGen** (34.0)
- `optimization`: **DSPy** (62.0)
- `orchestration`: **OpenAI Agents SDK** (75.4), **Google ADK** (73.6), **Claude Agent SDK** (70.1), **LangGraph** (68.6)
- `pipeline`: **Haystack** (71.2)
- `structured`: **PydanticAI** (54.7)
- `tooling`: **Composio** (68.3)
- `typescript`: **Mastra** (76.1)
- `web-agent`: **BrowserUse** (90.3)

## 🔍 Top 5 — Score Breakdown

| Framework | Star Velocity | Release Freshness | Issue Health | Commit Activity | Community | Fork Ratio |
|-----------|:---:|:---:|:---:|:---:|:---:|:---:|
| **BrowserUse** | 100 | 99.0 | 92.9 | 100 | 71.8 | 44.1 |
| **CrewAI** | 65.7 | 99.3 | 95.8 | 79.0 | 61.8 | 57.5 |
| **Mastra** | 34.7 | 99.3 | 95.2 | 100 | 93.2 | 39.5 |
| **OpenAI Agents SDK** | 32.2 | 94.0 | 98.3 | 100 | 73.6 | 63.9 |
| **Google ADK** | 19.4 | 96.7 | 91.0 | 100 | 84.0 | 73.9 |

## 💡 Key Insights

- **Hottest framework**: BrowserUse with a Pulse Score of 90.3
- **Fastest growing**: BrowserUse gained +1043 stars this week
- **Most active development**: Mastra with 1160 commits in the last 4 weeks
- **Stale releases**: AutoGen, Swarm haven't released in a while

## 📦 Recent Releases

- **Composio** [`@composio/cli@0.4.2-beta.381`](https://github.com/ComposioHQ/composio/releases/tag/@composio/cli@0.4.2-beta.381) — today *(pre-release)*
- **AG2** [`v1.0.4`](https://github.com/ag2ai/ag2/releases/tag/v1.0.4) — today
- **Claude Agent SDK** [`v2.1.263`](https://github.com/anthropics/claude-code/releases/tag/v2.1.263) — 1 day ago
- **PydanticAI** [`v2.40.0`](https://github.com/pydantic/pydantic-ai/releases/tag/v2.40.0) — 2 days ago
- **Mastra** [`@mastra/core@1.64.0`](https://github.com/mastra-ai/mastra/releases/tag/@mastra/core@1.64.0) — 2 days ago
- **Agno** [`v3.0.6`](https://github.com/agno-agi/agno/releases/tag/v3.0.6) — 2 days ago
- **CrewAI** [`1.15.20`](https://github.com/crewAIInc/crewAI/releases/tag/1.15.20) — 2 days ago
- **BrowserUse** [`0.13.10`](https://github.com/browser-use/browser-use/releases/tag/0.13.10) — 3 days ago
- **Semantic Kernel** [`dotnet-1.80.1`](https://github.com/microsoft/semantic-kernel/releases/tag/dotnet-1.80.1) — 3 days ago
- **Haystack** [`v3.1.1`](https://github.com/deepset-ai/haystack/releases/tag/v3.1.1) — 4 days ago

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

*Powered by GitHub Actions • Data refreshed daily • Last run: 2026-09-07 12:03 UTC*