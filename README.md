# 🔬 AI Agent Framework Pulse Tracker

[![Daily Update](https://github.com/PurpleHaze2320/ai-agent-pulse/actions/workflows/track.yml/badge.svg)](https://github.com/PurpleHaze2320/ai-agent-pulse/actions/workflows/track.yml)
[![Frameworks Tracked](https://img.shields.io/badge/frameworks-19-blue)](https://github.com/PurpleHaze2320/ai-agent-pulse)
[![License: MIT](https://img.shields.io/badge/License-MIT-green.svg)](https://opensource.org/licenses/MIT)
[![GitHub stars](https://img.shields.io/github/stars/PurpleHaze2320/ai-agent-pulse?style=social)](https://github.com/PurpleHaze2320/ai-agent-pulse/stargazers)

> Automated daily tracking of the AI agent framework ecosystem's health, momentum, and trends.
> Last updated: **2026-11-10 14:38 UTC** | Tracking **19** frameworks

## How It Works

This bot runs daily via GitHub Actions and collects metrics from the GitHub API for the most important
AI agent frameworks. It computes a **Pulse Score** (0-100) based on six weighted signals: star velocity,
release freshness, issue health, commit activity, community size, and fork engagement. The result is
a living dashboard that shows which frameworks are gaining momentum and which are losing steam.

## 🏆 Pulse Leaderboard

| Rank | Framework | Pulse | Stars | ⭐ 7d | Commits (4w) | Last Release | Category |
|------|-----------|-------|-------|-------|--------------|--------------|----------|
| 1 | [BrowserUse](https://github.com/browser-use/browser-use) | 🟢 **90.1** | 120.5k | 🚀 +612 | 1057 | today | `web-agent` |
| 2 | [LangGraph](https://github.com/langchain-ai/langgraph) | 🟢 **83.4** | 44.8k | 🚀 +360 | 100 | 4 days ago | `orchestration` |
| 3 | [CrewAI](https://github.com/crewAIInc/crewAI) | 🟢 **79.7** | 60.7k | 🚀 +276 | 187 | 1 day ago | `multi-agent` |
| 4 | [Mastra](https://github.com/mastra-ai/mastra) | 🟢 **74.8** | 29.4k | 🚀 +140 | 2007 | 6 days ago | `typescript` |
| 5 | [Google ADK](https://github.com/google/adk-python) | 🟢 **74.7** | 22.2k | 📈 +84 | 375 | 3 days ago | `orchestration` |
| 6 | [Claude Agent SDK](https://github.com/anthropics/claude-code) | 🟢 **73.0** | 155.2k | 🚀 +790 | 39 | today | `orchestration` |
| 7 | [Haystack](https://github.com/deepset-ai/haystack) | 🟢 **72.0** | 27.0k | 📈 +62 | 217 | today | `pipeline` |
| 8 | [OpenAI Agents SDK](https://github.com/openai/openai-agents-python) | 🟢 **70.7** | 30.6k | 🚀 +127 | 73 | 2 days ago | `orchestration` |
| 9 | [Agno](https://github.com/agno-agi/agno) | 🟡 **69.9** | 43.1k | 🚀 +101 | 131 | 12 days ago | `multi-agent` |
| 10 | [AG2](https://github.com/ag2ai/ag2) | 🟡 **69.7** | 5.1k | ↗️ +10 | 111 | 6 days ago | `multi-agent` |
| 11 | [Semantic Kernel](https://github.com/microsoft/semantic-kernel) | 🟡 **68.8** | 28.8k | 📈 +23 | 87 | 3 days ago | `enterprise` |
| 12 | [Composio](https://github.com/ComposioHQ/composio) | 🟡 **68.4** | 31.0k | 🚀 +116 | 276 | today | `tooling` |
| 13 | [DSPy](https://github.com/stanfordnlp/dspy) | 🟡 **63.9** | 39.0k | 📈 +91 | 86 | 28 days ago | `optimization` |
| 14 | [LlamaIndex](https://github.com/run-llama/llama_index) | 🟡 **51.4** | 52.9k | 📈 +72 | 2 | 1 mo ago | `data-agent` |
| 15 | [PydanticAI](https://github.com/pydantic/pydantic-ai) | 🟡 **50.2** | 21.1k | 🚀 +115 | 0 | 1 mo ago | `structured` |
| 16 | [Letta](https://github.com/letta-ai/letta) | 🟠 **33.9** | 25.4k | 📈 +73 | 1 | 5 mo ago | `memory` |
| 17 | [AutoGen](https://github.com/microsoft/autogen) | 🟠 **31.9** | 61.8k | 📈 +84 | 1 | 1y ago | `multi-agent` |
| 18 | [Smolagents](https://github.com/huggingface/smolagents) | 🟠 **31.3** | 30.3k | 🚀 +102 | 0 | 5 mo ago | `lightweight` |
| 19 | [Swarm](https://github.com/openai/swarm) | 🔴 **9.3** | 22.1k | ↗️ +19 | 0 | — | `experimental` |

## 📂 By Category

- `data-agent`: **LlamaIndex** (51.4)
- `enterprise`: **Semantic Kernel** (68.8)
- `experimental`: **Swarm** (9.3)
- `lightweight`: **Smolagents** (31.3)
- `memory`: **Letta** (33.9)
- `multi-agent`: **CrewAI** (79.7), **Agno** (69.9), **AG2** (69.7), **AutoGen** (31.9)
- `optimization`: **DSPy** (63.9)
- `orchestration`: **LangGraph** (83.4), **Google ADK** (74.7), **Claude Agent SDK** (73.0), **OpenAI Agents SDK** (70.7)
- `pipeline`: **Haystack** (72.0)
- `structured`: **PydanticAI** (50.2)
- `tooling`: **Composio** (68.4)
- `typescript`: **Mastra** (74.8)
- `web-agent`: **BrowserUse** (90.1)

## 🔍 Top 5 — Score Breakdown

| Framework | Star Velocity | Release Freshness | Issue Health | Commit Activity | Community | Fork Ratio |
|-----------|:---:|:---:|:---:|:---:|:---:|:---:|
| **BrowserUse** | 100 | 100.0 | 89.4 | 100 | 72.2 | 44.7 |
| **LangGraph** | 75.8 | 98.7 | 80.7 | 100 | 57.4 | 68.9 |
| **CrewAI** | 56.1 | 99.7 | 82.6 | 100 | 72.8 | 60.2 |
| **Mastra** | 30.8 | 98.0 | 93.4 | 100 | 93.2 | 41.9 |
| **Google ADK** | 17.7 | 99.0 | 94.1 | 100 | 85.8 | 78.1 |

## 💡 Key Insights

- **Hottest framework**: BrowserUse with a Pulse Score of 90.1
- **Fastest growing**: Claude Agent SDK gained +790 stars this week
- **Most active development**: Mastra with 2007 commits in the last 4 weeks
- **Stale releases**: AutoGen, Swarm haven't released in a while

## 📦 Recent Releases

- **Haystack** [`v3.5.0`](https://github.com/deepset-ai/haystack/releases/tag/v3.5.0) — today
- **BrowserUse** [`1.0.1`](https://github.com/browser-use/browser-use/releases/tag/1.0.1) — today
- **Claude Agent SDK** [`v2.1.322`](https://github.com/anthropics/claude-code/releases/tag/v2.1.322) — today
- **Composio** [`@composio/cli@0.6.1-beta.537`](https://github.com/ComposioHQ/composio/releases/tag/@composio/cli@0.6.1-beta.537) — today *(pre-release)*
- **CrewAI** [`1.15.39`](https://github.com/crewAIInc/crewAI/releases/tag/1.15.39) — 1 day ago
- **OpenAI Agents SDK** [`v0.24.0-alpha.7`](https://github.com/openai/openai-agents-python/releases/tag/v0.24.0-alpha.7) — 2 days ago *(pre-release)*
- **Semantic Kernel** [`dotnet-1.82.0`](https://github.com/microsoft/semantic-kernel/releases/tag/dotnet-1.82.0) — 3 days ago
- **Google ADK** [`v2.14.0`](https://github.com/google/adk-python/releases/tag/v2.14.0) — 3 days ago
- **LangGraph** [`sdk==0.4.14`](https://github.com/langchain-ai/langgraph/releases/tag/sdk==0.4.14) — 4 days ago
- **Mastra** [`@mastra/core@1.82.0`](https://github.com/mastra-ai/mastra/releases/tag/@mastra/core@1.82.0) — 6 days ago

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

*Powered by GitHub Actions • Data refreshed daily • Last run: 2026-11-10 14:38 UTC*