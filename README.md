# 🔬 AI Agent Framework Pulse Tracker

[![Daily Update](https://github.com/PurpleHaze2320/ai-agent-pulse/actions/workflows/track.yml/badge.svg)](https://github.com/PurpleHaze2320/ai-agent-pulse/actions/workflows/track.yml)
[![Frameworks Tracked](https://img.shields.io/badge/frameworks-19-blue)](https://github.com/PurpleHaze2320/ai-agent-pulse)
[![License: MIT](https://img.shields.io/badge/License-MIT-green.svg)](https://opensource.org/licenses/MIT)
[![GitHub stars](https://img.shields.io/github/stars/PurpleHaze2320/ai-agent-pulse?style=social)](https://github.com/PurpleHaze2320/ai-agent-pulse/stargazers)

> Automated daily tracking of the AI agent framework ecosystem's health, momentum, and trends.
> Last updated: **2026-11-11 13:53 UTC** | Tracking **19** frameworks

## How It Works

This bot runs daily via GitHub Actions and collects metrics from the GitHub API for the most important
AI agent frameworks. It computes a **Pulse Score** (0-100) based on six weighted signals: star velocity,
release freshness, issue health, commit activity, community size, and fork engagement. The result is
a living dashboard that shows which frameworks are gaining momentum and which are losing steam.

## 🏆 Pulse Leaderboard

| Rank | Framework | Pulse | Stars | ⭐ 7d | Commits (4w) | Last Release | Category |
|------|-----------|-------|-------|-------|--------------|--------------|----------|
| 1 | [BrowserUse](https://github.com/browser-use/browser-use) | 🟢 **90.1** | 120.7k | 🚀 +687 | 1069 | today | `web-agent` |
| 2 | [LangGraph](https://github.com/langchain-ai/langgraph) | 🟢 **82.5** | 44.8k | 🚀 +341 | 104 | 5 days ago | `orchestration` |
| 3 | [CrewAI](https://github.com/crewAIInc/crewAI) | 🟢 **79.7** | 60.8k | 🚀 +278 | 193 | 2 days ago | `multi-agent` |
| 4 | [Mastra](https://github.com/mastra-ai/mastra) | 🟢 **75.2** | 29.5k | 🚀 +150 | 2215 | 7 days ago | `typescript` |
| 5 | [Google ADK](https://github.com/google/adk-python) | 🟢 **74.4** | 22.2k | 📈 +76 | 398 | 4 days ago | `orchestration` |
| 6 | [Claude Agent SDK](https://github.com/anthropics/claude-code) | 🟢 **73.6** | 155.3k | 🚀 +761 | 42 | 1 day ago | `orchestration` |
| 7 | [Haystack](https://github.com/deepset-ai/haystack) | 🟢 **72.0** | 27.0k | 📈 +64 | 237 | 1 day ago | `pipeline` |
| 8 | [OpenAI Agents SDK](https://github.com/openai/openai-agents-python) | 🟢 **70.7** | 30.6k | 🚀 +123 | 74 | 3 days ago | `orchestration` |
| 9 | [AG2](https://github.com/ag2ai/ag2) | 🟢 **70.1** | 5.1k | ↗️ +11 | 118 | today | `multi-agent` |
| 10 | [PydanticAI](https://github.com/pydantic/pydantic-ai) | 🟢 **70.0** | 21.1k | 🚀 +114 | 1116 | 1 mo ago | `structured` |
| 11 | [Agno](https://github.com/agno-agi/agno) | 🟡 **69.4** | 43.1k | 📈 +89 | 142 | 12 days ago | `multi-agent` |
| 12 | [Semantic Kernel](https://github.com/microsoft/semantic-kernel) | 🟡 **68.9** | 28.8k | 📈 +22 | 88 | 4 days ago | `enterprise` |
| 13 | [Composio](https://github.com/ComposioHQ/composio) | 🟡 **68.5** | 31.0k | 🚀 +118 | 285 | today | `tooling` |
| 14 | [DSPy](https://github.com/stanfordnlp/dspy) | 🟡 **66.8** | 39.0k | 📈 +96 | 90 | today | `optimization` |
| 15 | [LlamaIndex](https://github.com/run-llama/llama_index) | 🟡 **51.7** | 52.9k | 📈 +71 | 4 | 1 mo ago | `data-agent` |
| 16 | [Letta](https://github.com/letta-ai/letta) | 🟠 **33.8** | 25.4k | 📈 +71 | 1 | 6 mo ago | `memory` |
| 17 | [AutoGen](https://github.com/microsoft/autogen) | 🟠 **31.9** | 61.8k | 📈 +86 | 1 | 1y ago | `multi-agent` |
| 18 | [Smolagents](https://github.com/huggingface/smolagents) | 🟠 **31.2** | 30.3k | 🚀 +104 | 0 | 5 mo ago | `lightweight` |
| 19 | [Swarm](https://github.com/openai/swarm) | 🔴 **9.3** | 22.1k | ↗️ +17 | 0 | — | `experimental` |

## 📂 By Category

- `data-agent`: **LlamaIndex** (51.7)
- `enterprise`: **Semantic Kernel** (68.9)
- `experimental`: **Swarm** (9.3)
- `lightweight`: **Smolagents** (31.2)
- `memory`: **Letta** (33.8)
- `multi-agent`: **CrewAI** (79.7), **AG2** (70.1), **Agno** (69.4), **AutoGen** (31.9)
- `optimization`: **DSPy** (66.8)
- `orchestration`: **LangGraph** (82.5), **Google ADK** (74.4), **Claude Agent SDK** (73.6), **OpenAI Agents SDK** (70.7)
- `pipeline`: **Haystack** (72.0)
- `structured`: **PydanticAI** (70.0)
- `tooling`: **Composio** (68.5)
- `typescript`: **Mastra** (75.2)
- `web-agent`: **BrowserUse** (90.1)

## 🔍 Top 5 — Score Breakdown

| Framework | Star Velocity | Release Freshness | Issue Health | Commit Activity | Community | Fork Ratio |
|-----------|:---:|:---:|:---:|:---:|:---:|:---:|
| **BrowserUse** | 100 | 100.0 | 89.6 | 100 | 72.2 | 44.7 |
| **LangGraph** | 72.6 | 98.3 | 80.7 | 100 | 57.4 | 68.9 |
| **CrewAI** | 56.4 | 99.3 | 82.9 | 100 | 73.2 | 60.2 |
| **Mastra** | 32.0 | 97.7 | 94.0 | 100 | 93.2 | 42.0 |
| **Google ADK** | 16.6 | 98.7 | 94.2 | 100 | 86.2 | 78.3 |

## 💡 Key Insights

- **Hottest framework**: BrowserUse with a Pulse Score of 90.1
- **Fastest growing**: Claude Agent SDK gained +761 stars this week
- **Most active development**: Mastra with 2215 commits in the last 4 weeks
- **Stale releases**: AutoGen, Swarm haven't released in a while

## 📦 Recent Releases

- **Composio** [`@composio/cli@0.6.1-beta.540`](https://github.com/ComposioHQ/composio/releases/tag/@composio/cli@0.6.1-beta.540) — today *(pre-release)*
- **BrowserUse** [`1.0.2`](https://github.com/browser-use/browser-use/releases/tag/1.0.2) — today
- **AG2** [`v.1.3.1`](https://github.com/ag2ai/ag2/releases/tag/v.1.3.1) — today
- **DSPy** [`3.5.0`](https://github.com/stanfordnlp/dspy/releases/tag/3.5.0) — today
- **Haystack** [`v3.5.0`](https://github.com/deepset-ai/haystack/releases/tag/v3.5.0) — 1 day ago
- **Claude Agent SDK** [`v2.1.322`](https://github.com/anthropics/claude-code/releases/tag/v2.1.322) — 1 day ago
- **CrewAI** [`1.15.39`](https://github.com/crewAIInc/crewAI/releases/tag/1.15.39) — 2 days ago
- **OpenAI Agents SDK** [`v0.24.0-alpha.7`](https://github.com/openai/openai-agents-python/releases/tag/v0.24.0-alpha.7) — 3 days ago *(pre-release)*
- **Semantic Kernel** [`dotnet-1.82.0`](https://github.com/microsoft/semantic-kernel/releases/tag/dotnet-1.82.0) — 4 days ago
- **Google ADK** [`v2.14.0`](https://github.com/google/adk-python/releases/tag/v2.14.0) — 4 days ago

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

*Powered by GitHub Actions • Data refreshed daily • Last run: 2026-11-11 13:53 UTC*