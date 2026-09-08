# 🔬 AI Agent Framework Pulse Tracker

[![Daily Update](https://github.com/PurpleHaze2320/ai-agent-pulse/actions/workflows/track.yml/badge.svg)](https://github.com/PurpleHaze2320/ai-agent-pulse/actions/workflows/track.yml)
[![Frameworks Tracked](https://img.shields.io/badge/frameworks-19-blue)](https://github.com/PurpleHaze2320/ai-agent-pulse)
[![License: MIT](https://img.shields.io/badge/License-MIT-green.svg)](https://opensource.org/licenses/MIT)
[![GitHub stars](https://img.shields.io/github/stars/PurpleHaze2320/ai-agent-pulse?style=social)](https://github.com/PurpleHaze2320/ai-agent-pulse/stargazers)

> Automated daily tracking of the AI agent framework ecosystem's health, momentum, and trends.
> Last updated: **2026-09-08 10:57 UTC** | Tracking **19** frameworks

## How It Works

This bot runs daily via GitHub Actions and collects metrics from the GitHub API for the most important
AI agent frameworks. It computes a **Pulse Score** (0-100) based on six weighted signals: star velocity,
release freshness, issue health, commit activity, community size, and fork engagement. The result is
a living dashboard that shows which frameworks are gaining momentum and which are losing steam.

## 🏆 Pulse Leaderboard

| Rank | Framework | Pulse | Stars | ⭐ 7d | Commits (4w) | Last Release | Category |
|------|-----------|-------|-------|-------|--------------|--------------|----------|
| 1 | [BrowserUse](https://github.com/browser-use/browser-use) | 🟢 **90.3** | 113.0k | 🚀 +1109 | 185 | 4 days ago | `web-agent` |
| 2 | [CrewAI](https://github.com/crewAIInc/crewAI) | 🟢 **78.8** | 58.2k | 🚀 +296 | 85 | 3 days ago | `multi-agent` |
| 3 | [OpenAI Agents SDK](https://github.com/openai/openai-agents-python) | 🟢 **76.8** | 29.3k | 🚀 +150 | 148 | today | `orchestration` |
| 4 | [Mastra](https://github.com/mastra-ai/mastra) | 🟢 **76.7** | 27.8k | 🚀 +187 | 1224 | 3 days ago | `typescript` |
| 5 | [PydanticAI](https://github.com/pydantic/pydantic-ai) | 🟢 **74.6** | 19.8k | 🚀 +147 | 233 | today | `structured` |
| 6 | [Google ADK](https://github.com/google/adk-python) | 🟢 **73.6** | 21.5k | 📈 +97 | 341 | 11 days ago | `orchestration` |
| 7 | [Claude Agent SDK](https://github.com/anthropics/claude-code) | 🟢 **70.1** | 144.4k | 🚀 +781 | 24 | 2 days ago | `orchestration` |
| 8 | [LangGraph](https://github.com/langchain-ai/langgraph) | 🟡 **68.8** | 41.2k | 🚀 +403 | 28 | 11 days ago | `orchestration` |
| 9 | [Agno](https://github.com/agno-agi/agno) | 🟡 **68.1** | 42.1k | 🚀 +101 | 85 | today | `multi-agent` |
| 10 | [Composio](https://github.com/ComposioHQ/composio) | 🟡 **67.8** | 30.1k | 📈 +99 | 210 | today | `tooling` |
| 11 | [DSPy](https://github.com/stanfordnlp/dspy) | 🟡 **61.9** | 37.8k | 🚀 +147 | 51 | 17 days ago | `optimization` |
| 12 | [LlamaIndex](https://github.com/run-llama/llama_index) | 🟡 **61.6** | 52.1k | 🚀 +112 | 32 | 19 days ago | `data-agent` |
| 13 | [AG2](https://github.com/ag2ai/ag2) | 🟡 **58.3** | 4.9k | ↗️ +15 | 42 | 1 day ago | `multi-agent` |
| 14 | [Semantic Kernel](https://github.com/microsoft/semantic-kernel) | 🟡 **54.8** | 28.5k | 📈 +25 | 22 | 4 days ago | `enterprise` |
| 15 | [Haystack](https://github.com/deepset-ai/haystack) | 🟡 **51.2** | 26.4k | 📈 +65 | 0 | 5 days ago | `pipeline` |
| 16 | [Letta](https://github.com/letta-ai/letta) | 🟡 **40.8** | 24.7k | 🚀 +132 | 1 | 3 mo ago | `memory` |
| 17 | [Smolagents](https://github.com/huggingface/smolagents) | 🟠 **37.8** | 29.2k | 🚀 +136 | 2 | 3 mo ago | `lightweight` |
| 18 | [AutoGen](https://github.com/microsoft/autogen) | 🟠 **34.0** | 60.9k | 🚀 +134 | 0 | 11 mo ago | `multi-agent` |
| 19 | [Swarm](https://github.com/openai/swarm) | 🔴 **9.2** | 21.9k | ↗️ +14 | 0 | — | `experimental` |

## 📂 By Category

- `data-agent`: **LlamaIndex** (61.6)
- `enterprise`: **Semantic Kernel** (54.8)
- `experimental`: **Swarm** (9.2)
- `lightweight`: **Smolagents** (37.8)
- `memory`: **Letta** (40.8)
- `multi-agent`: **CrewAI** (78.8), **Agno** (68.1), **AG2** (58.3), **AutoGen** (34.0)
- `optimization`: **DSPy** (61.9)
- `orchestration`: **OpenAI Agents SDK** (76.8), **Google ADK** (73.6), **Claude Agent SDK** (70.1), **LangGraph** (68.8)
- `pipeline`: **Haystack** (51.2)
- `structured`: **PydanticAI** (74.6)
- `tooling`: **Composio** (67.8)
- `typescript`: **Mastra** (76.7)
- `web-agent`: **BrowserUse** (90.3)

## 🔍 Top 5 — Score Breakdown

| Framework | Star Velocity | Release Freshness | Issue Health | Commit Activity | Community | Fork Ratio |
|-----------|:---:|:---:|:---:|:---:|:---:|:---:|
| **BrowserUse** | 100 | 98.7 | 92.7 | 100 | 72.0 | 44.1 |
| **CrewAI** | 62.6 | 99.0 | 95.7 | 85.0 | 62.6 | 57.6 |
| **OpenAI Agents SDK** | 32.5 | 100.0 | 98.9 | 100 | 74.6 | 63.9 |
| **Mastra** | 37.4 | 99.0 | 95.2 | 100 | 93.2 | 39.5 |
| **PydanticAI** | 30.1 | 100.0 | 81.2 | 100 | 95.0 | 53.9 |

## 💡 Key Insights

- **Hottest framework**: BrowserUse with a Pulse Score of 90.3
- **Fastest growing**: BrowserUse gained +1109 stars this week
- **Most active development**: Mastra with 1224 commits in the last 4 weeks
- **Stale releases**: AutoGen, Swarm haven't released in a while

## 📦 Recent Releases

- **Agno** [`v3.0.7`](https://github.com/agno-agi/agno/releases/tag/v3.0.7) — today
- **OpenAI Agents SDK** [`v0.22.1`](https://github.com/openai/openai-agents-python/releases/tag/v0.22.1) — today
- **PydanticAI** [`v2.41.0`](https://github.com/pydantic/pydantic-ai/releases/tag/v2.41.0) — today
- **Composio** [`@composio/cli@0.4.2-beta.382`](https://github.com/ComposioHQ/composio/releases/tag/@composio/cli@0.4.2-beta.382) — today *(pre-release)*
- **AG2** [`v1.0.4`](https://github.com/ag2ai/ag2/releases/tag/v1.0.4) — 1 day ago
- **Claude Agent SDK** [`v2.1.263`](https://github.com/anthropics/claude-code/releases/tag/v2.1.263) — 2 days ago
- **Mastra** [`@mastra/core@1.64.0`](https://github.com/mastra-ai/mastra/releases/tag/@mastra/core@1.64.0) — 3 days ago
- **CrewAI** [`1.15.20`](https://github.com/crewAIInc/crewAI/releases/tag/1.15.20) — 3 days ago
- **BrowserUse** [`0.13.10`](https://github.com/browser-use/browser-use/releases/tag/0.13.10) — 4 days ago
- **Semantic Kernel** [`dotnet-1.80.1`](https://github.com/microsoft/semantic-kernel/releases/tag/dotnet-1.80.1) — 4 days ago

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

*Powered by GitHub Actions • Data refreshed daily • Last run: 2026-09-08 10:57 UTC*