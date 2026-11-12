# 🔬 AI Agent Framework Pulse Tracker

[![Daily Update](https://github.com/PurpleHaze2320/ai-agent-pulse/actions/workflows/track.yml/badge.svg)](https://github.com/PurpleHaze2320/ai-agent-pulse/actions/workflows/track.yml)
[![Frameworks Tracked](https://img.shields.io/badge/frameworks-19-blue)](https://github.com/PurpleHaze2320/ai-agent-pulse)
[![License: MIT](https://img.shields.io/badge/License-MIT-green.svg)](https://opensource.org/licenses/MIT)
[![GitHub stars](https://img.shields.io/github/stars/PurpleHaze2320/ai-agent-pulse?style=social)](https://github.com/PurpleHaze2320/ai-agent-pulse/stargazers)

> Automated daily tracking of the AI agent framework ecosystem's health, momentum, and trends.
> Last updated: **2026-11-12 14:55 UTC** | Tracking **19** frameworks

## How It Works

This bot runs daily via GitHub Actions and collects metrics from the GitHub API for the most important
AI agent frameworks. It computes a **Pulse Score** (0-100) based on six weighted signals: star velocity,
release freshness, issue health, commit activity, community size, and fork engagement. The result is
a living dashboard that shows which frameworks are gaining momentum and which are losing steam.

## 🏆 Pulse Leaderboard

| Rank | Framework | Pulse | Stars | ⭐ 7d | Commits (4w) | Last Release | Category |
|------|-----------|-------|-------|-------|--------------|--------------|----------|
| 1 | [BrowserUse](https://github.com/browser-use/browser-use) | 🟢 **90.1** | 120.8k | 🚀 +725 | 1069 | today | `web-agent` |
| 2 | [CrewAI](https://github.com/crewAIInc/crewAI) | 🟢 **79.8** | 60.8k | 🚀 +277 | 200 | today | `multi-agent` |
| 3 | [Google ADK](https://github.com/google/adk-python) | 🟢 **74.5** | 22.2k | 📈 +79 | 402 | 5 days ago | `orchestration` |
| 4 | [Mastra](https://github.com/mastra-ai/mastra) | 🟢 **74.4** | 29.5k | 🚀 +132 | 2378 | 8 days ago | `typescript` |
| 5 | [Claude Agent SDK](https://github.com/anthropics/claude-code) | 🟢 **73.9** | 155.4k | 🚀 +785 | 44 | 2 days ago | `orchestration` |
| 6 | [Haystack](https://github.com/deepset-ai/haystack) | 🟢 **72.1** | 27.0k | 📈 +67 | 255 | 2 days ago | `pipeline` |
| 7 | [OpenAI Agents SDK](https://github.com/openai/openai-agents-python) | 🟢 **70.5** | 30.6k | 🚀 +122 | 74 | 4 days ago | `orchestration` |
| 8 | [AG2](https://github.com/ag2ai/ag2) | 🟢 **70.2** | 5.1k | ↗️ +16 | 124 | 1 day ago | `multi-agent` |
| 9 | [Agno](https://github.com/agno-agi/agno) | 🟡 **69.9** | 43.2k | 🚀 +104 | 152 | 14 days ago | `multi-agent` |
| 10 | [Semantic Kernel](https://github.com/microsoft/semantic-kernel) | 🟡 **68.9** | 28.8k | 📈 +24 | 88 | 5 days ago | `enterprise` |
| 11 | [Composio](https://github.com/ComposioHQ/composio) | 🟡 **68.2** | 31.0k | 🚀 +107 | 309 | today | `tooling` |
| 12 | [LangGraph](https://github.com/langchain-ai/langgraph) | 🟡 **62.5** | 44.9k | 🚀 +343 | 0 | 6 days ago | `orchestration` |
| 13 | [PydanticAI](https://github.com/pydantic/pydantic-ai) | 🟡 **53.2** | 21.2k | 🚀 +133 | 0 | today | `structured` |
| 14 | [LlamaIndex](https://github.com/run-llama/llama_index) | 🟡 **51.5** | 52.9k | 📈 +63 | 5 | 1 mo ago | `data-agent` |
| 15 | [DSPy](https://github.com/stanfordnlp/dspy) | 🟡 **48.3** | 39.0k | 📈 +86 | 0 | 1 day ago | `optimization` |
| 16 | [Letta](https://github.com/letta-ai/letta) | 🟠 **33.6** | 25.4k | 📈 +68 | 1 | 6 mo ago | `memory` |
| 17 | [AutoGen](https://github.com/microsoft/autogen) | 🟠 **32.0** | 61.8k | 📈 +84 | 2 | 1y ago | `multi-agent` |
| 18 | [Smolagents](https://github.com/huggingface/smolagents) | 🟠 **31.5** | 30.3k | 🚀 +115 | 0 | 5 mo ago | `lightweight` |
| 19 | [Swarm](https://github.com/openai/swarm) | 🔴 **9.2** | 22.1k | ↗️ +16 | 0 | — | `experimental` |

## 📂 By Category

- `data-agent`: **LlamaIndex** (51.5)
- `enterprise`: **Semantic Kernel** (68.9)
- `experimental`: **Swarm** (9.2)
- `lightweight`: **Smolagents** (31.5)
- `memory`: **Letta** (33.6)
- `multi-agent`: **CrewAI** (79.8), **AG2** (70.2), **Agno** (69.9), **AutoGen** (32.0)
- `optimization`: **DSPy** (48.3)
- `orchestration`: **Google ADK** (74.5), **Claude Agent SDK** (73.9), **OpenAI Agents SDK** (70.5), **LangGraph** (62.5)
- `pipeline`: **Haystack** (72.1)
- `structured`: **PydanticAI** (53.2)
- `tooling`: **Composio** (68.2)
- `typescript`: **Mastra** (74.4)
- `web-agent`: **BrowserUse** (90.1)

## 🔍 Top 5 — Score Breakdown

| Framework | Star Velocity | Release Freshness | Issue Health | Commit Activity | Community | Fork Ratio |
|-----------|:---:|:---:|:---:|:---:|:---:|:---:|
| **BrowserUse** | 100 | 100.0 | 89.6 | 100 | 72.2 | 44.7 |
| **CrewAI** | 56.3 | 100.0 | 82.8 | 100 | 73.2 | 60.3 |
| **Google ADK** | 17.0 | 98.3 | 94.1 | 100 | 86.2 | 78.4 |
| **Mastra** | 29.1 | 97.3 | 94.3 | 100 | 93.2 | 42.0 |
| **Claude Agent SDK** | 100 | 99.3 | 84.6 | 44.0 | 11.2 | 64.2 |

## 💡 Key Insights

- **Hottest framework**: BrowserUse with a Pulse Score of 90.1
- **Fastest growing**: Claude Agent SDK gained +785 stars this week
- **Most active development**: Mastra with 2378 commits in the last 4 weeks
- **Stale releases**: AutoGen, Swarm haven't released in a while

## 📦 Recent Releases

- **Composio** [`@composio/cli@0.6.1-beta.544`](https://github.com/ComposioHQ/composio/releases/tag/@composio/cli@0.6.1-beta.544) — today *(pre-release)*
- **BrowserUse** [`1.0.3rc1`](https://github.com/browser-use/browser-use/releases/tag/1.0.3rc1) — today *(pre-release)*
- **PydanticAI** [`v2.68.0`](https://github.com/pydantic/pydantic-ai/releases/tag/v2.68.0) — today
- **CrewAI** [`1.15.40`](https://github.com/crewAIInc/crewAI/releases/tag/1.15.40) — today
- **AG2** [`v.1.3.1`](https://github.com/ag2ai/ag2/releases/tag/v.1.3.1) — 1 day ago
- **DSPy** [`3.5.0`](https://github.com/stanfordnlp/dspy/releases/tag/3.5.0) — 1 day ago
- **Haystack** [`v3.5.0`](https://github.com/deepset-ai/haystack/releases/tag/v3.5.0) — 2 days ago
- **Claude Agent SDK** [`v2.1.322`](https://github.com/anthropics/claude-code/releases/tag/v2.1.322) — 2 days ago
- **OpenAI Agents SDK** [`v0.24.0-alpha.7`](https://github.com/openai/openai-agents-python/releases/tag/v0.24.0-alpha.7) — 4 days ago *(pre-release)*
- **Semantic Kernel** [`dotnet-1.82.0`](https://github.com/microsoft/semantic-kernel/releases/tag/dotnet-1.82.0) — 5 days ago

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

*Powered by GitHub Actions • Data refreshed daily • Last run: 2026-11-12 14:55 UTC*