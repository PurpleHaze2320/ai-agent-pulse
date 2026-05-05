# 🔬 AI Agent Framework Pulse Tracker

[![Daily Update](https://github.com/PurpleHaze2320/ai-agent-pulse/actions/workflows/track.yml/badge.svg)](https://github.com/PurpleHaze2320/ai-agent-pulse/actions/workflows/track.yml)
[![Frameworks Tracked](https://img.shields.io/badge/frameworks-19-blue)](https://github.com/PurpleHaze2320/ai-agent-pulse)
[![License: MIT](https://img.shields.io/badge/License-MIT-green.svg)](https://opensource.org/licenses/MIT)
[![GitHub stars](https://img.shields.io/github/stars/PurpleHaze2320/ai-agent-pulse?style=social)](https://github.com/PurpleHaze2320/ai-agent-pulse/stargazers)

> Automated daily tracking of the AI agent framework ecosystem's health, momentum, and trends.
> Last updated: **2026-05-05 08:19 UTC** | Tracking **19** frameworks

## How It Works

This bot runs daily via GitHub Actions and collects metrics from the GitHub API for the most important
AI agent frameworks. It computes a **Pulse Score** (0-100) based on six weighted signals: star velocity,
release freshness, issue health, commit activity, community size, and fork engagement. The result is
a living dashboard that shows which frameworks are gaining momentum and which are losing steam.

## 🏆 Pulse Leaderboard

| Rank | Framework | Pulse | Stars | ⭐ 7d | Commits (4w) | Last Release | Category |
|------|-----------|-------|-------|-------|--------------|--------------|----------|
| 1 | [Mastra](https://github.com/mastra-ai/mastra) | 🟢 **76.2** | 23.6k | 🚀 +194 | 835 | today | `typescript` |
| 2 | [CrewAI](https://github.com/crewAIInc/crewAI) | 🟢 **71.2** | 50.6k | 🚀 +499 | 0 | today | `multi-agent` |
| 3 | [OpenAI Agents SDK](https://github.com/openai/openai-agents-python) | 🟢 **70.6** | 25.9k | 🚀 +423 | 0 | 3 days ago | `orchestration` |
| 4 | [LangGraph](https://github.com/langchain-ai/langgraph) | 🟡 **69.0** | 31.2k | 🚀 +577 | 0 | today | `orchestration` |
| 5 | [BrowserUse](https://github.com/browser-use/browser-use) | 🟡 **68.1** | 92.2k | 🚀 +1305 | 0 | 1 mo ago | `web-agent` |
| 6 | [Claude Agent SDK](https://github.com/anthropics/claude-code) | 🟡 **64.8** | 120.5k | 🚀 +1797 | 0 | today | `orchestration` |
| 7 | [LlamaIndex](https://github.com/run-llama/llama_index) | 🟡 **56.9** | 49.1k | 🚀 +134 | 0 | 14 days ago | `data-agent` |
| 8 | [Agno](https://github.com/agno-agi/agno) | 🟡 **54.9** | 39.9k | 🚀 +186 | 0 | 6 days ago | `multi-agent` |
| 9 | [PydanticAI](https://github.com/pydantic/pydantic-ai) | 🟡 **54.0** | 16.8k | 🚀 +151 | 0 | today | `structured` |
| 10 | [Google ADK](https://github.com/google/adk-python) | 🟡 **51.0** | 19.4k | 🚀 +115 | 0 | 4 days ago | `orchestration` |
| 11 | [DSPy](https://github.com/stanfordnlp/dspy) | 🟡 **50.7** | 34.2k | 🚀 +156 | 0 | 13 days ago | `optimization` |
| 12 | [Semantic Kernel](https://github.com/microsoft/semantic-kernel) | 🟡 **50.6** | 27.8k | 📈 +38 | 0 | 5 days ago | `enterprise` |
| 13 | [AG2](https://github.com/ag2ai/ag2) | 🟡 **49.3** | 4.5k | 📈 +50 | 0 | 4 days ago | `multi-agent` |
| 14 | [Haystack](https://github.com/deepset-ai/haystack) | 🟡 **49.1** | 25.1k | 📈 +77 | 0 | 14 days ago | `pipeline` |
| 15 | [Composio](https://github.com/ComposioHQ/composio) | 🟡 **46.1** | 28.1k | 🚀 +119 | 0 | 3 days ago | `tooling` |
| 16 | [Letta](https://github.com/letta-ai/letta) | 🟡 **44.4** | 22.4k | 📈 +90 | 0 | 1 mo ago | `memory` |
| 17 | [AutoGen](https://github.com/microsoft/autogen) | 🟡 **43.4** | 57.7k | 🚀 +192 | 0 | 7 mo ago | `multi-agent` |
| 18 | [Smolagents](https://github.com/huggingface/smolagents) | 🟠 **37.7** | 27.1k | 🚀 +140 | 0 | 3 mo ago | `lightweight` |
| 19 | [Swarm](https://github.com/openai/swarm) | 🔴 **9.3** | 21.4k | 📈 +25 | 0 | — | `experimental` |

## 📂 By Category

- `data-agent`: **LlamaIndex** (56.9)
- `enterprise`: **Semantic Kernel** (50.6)
- `experimental`: **Swarm** (9.3)
- `lightweight`: **Smolagents** (37.7)
- `memory`: **Letta** (44.4)
- `multi-agent`: **CrewAI** (71.2), **Agno** (54.9), **AG2** (49.3), **AutoGen** (43.4)
- `optimization`: **DSPy** (50.7)
- `orchestration`: **OpenAI Agents SDK** (70.6), **LangGraph** (69.0), **Claude Agent SDK** (64.8), **Google ADK** (51.0)
- `pipeline`: **Haystack** (49.1)
- `structured`: **PydanticAI** (54.0)
- `tooling`: **Composio** (46.1)
- `typescript`: **Mastra** (76.2)
- `web-agent`: **BrowserUse** (68.1)

## 🔍 Top 5 — Score Breakdown

| Framework | Star Velocity | Release Freshness | Issue Health | Commit Activity | Community | Fork Ratio |
|-----------|:---:|:---:|:---:|:---:|:---:|:---:|
| **Mastra** | 40.4 | 100.0 | 94.7 | 100 | 84.6 | 34.1 |
| **CrewAI** | 100 | 100.0 | 98.7 | 0.0 | 58.8 | 55.2 |
| **OpenAI Agents SDK** | 100 | 99.0 | 96.1 | 0.0 | 52.6 | 61.0 |
| **LangGraph** | 100 | 100.0 | 78.2 | 0.0 | 54.8 | 68.1 |
| **BrowserUse** | 100 | 89.0 | 96.8 | 0.0 | 62.8 | 45.4 |

## 💡 Key Insights

- **Hottest framework**: Mastra with a Pulse Score of 76.2
- **Fastest growing**: Claude Agent SDK gained +1797 stars this week
- **Most active development**: Mastra with 835 commits in the last 4 weeks
- **Stale releases**: Swarm haven't released in a while

## 📦 Recent Releases

- **PydanticAI** [`v1.90.0`](https://github.com/pydantic/pydantic-ai/releases/tag/v1.90.0) — today
- **Claude Agent SDK** [`v2.1.128`](https://github.com/anthropics/claude-code/releases/tag/v2.1.128) — today
- **LangGraph** [`1.2.0a7`](https://github.com/langchain-ai/langgraph/releases/tag/1.2.0a7) — today
- **Mastra** [`@mastra/core@1.31.0`](https://github.com/mastra-ai/mastra/releases/tag/@mastra/core@1.31.0) — today
- **CrewAI** [`1.14.5a2`](https://github.com/crewAIInc/crewAI/releases/tag/1.14.5a2) — today *(pre-release)*
- **OpenAI Agents SDK** [`v0.15.1`](https://github.com/openai/openai-agents-python/releases/tag/v0.15.1) — 3 days ago
- **Composio** [`@composio/cli@0.2.28`](https://github.com/ComposioHQ/composio/releases/tag/@composio/cli@0.2.28) — 3 days ago
- **Google ADK** [`v1.32.0`](https://github.com/google/adk-python/releases/tag/v1.32.0) — 4 days ago
- **AG2** [`v0.12.2`](https://github.com/ag2ai/ag2/releases/tag/v0.12.2) — 4 days ago
- **Semantic Kernel** [`dotnet-1.75.0`](https://github.com/microsoft/semantic-kernel/releases/tag/dotnet-1.75.0) — 5 days ago

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

*Powered by GitHub Actions • Data refreshed daily • Last run: 2026-05-05 08:19 UTC*