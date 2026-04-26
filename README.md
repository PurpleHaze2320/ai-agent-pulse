# 🔬 AI Agent Framework Pulse Tracker

[![Daily Update](https://github.com/PurpleHaze2320/ai-agent-pulse/actions/workflows/track.yml/badge.svg)](https://github.com/PurpleHaze2320/ai-agent-pulse/actions/workflows/track.yml)
[![Frameworks Tracked](https://img.shields.io/badge/frameworks-19-blue)](https://github.com/PurpleHaze2320/ai-agent-pulse)
[![License: MIT](https://img.shields.io/badge/License-MIT-green.svg)](https://opensource.org/licenses/MIT)
[![GitHub stars](https://img.shields.io/github/stars/PurpleHaze2320/ai-agent-pulse?style=social)](https://github.com/PurpleHaze2320/ai-agent-pulse/stargazers)

> Automated daily tracking of the AI agent framework ecosystem's health, momentum, and trends.
> Last updated: **2026-04-26 07:47 UTC** | Tracking **19** frameworks

## How It Works

This bot runs daily via GitHub Actions and collects metrics from the GitHub API for the most important
AI agent frameworks. It computes a **Pulse Score** (0-100) based on six weighted signals: star velocity,
release freshness, issue health, commit activity, community size, and fork engagement. The result is
a living dashboard that shows which frameworks are gaining momentum and which are losing steam.

## 🏆 Pulse Leaderboard

| Rank | Framework | Pulse | Stars | ⭐ 7d | Commits (4w) | Last Release | Category |
|------|-----------|-------|-------|-------|--------------|--------------|----------|
| 1 | [Mastra](https://github.com/mastra-ai/mastra) | 🟢 **74.6** | 23.3k | 🚀 +180 | 610 | 1 day ago | `typescript` |
| 2 | [OpenAI Agents SDK](https://github.com/openai/openai-agents-python) | 🟢 **70.6** | 25.2k | 🚀 +2641 | 0 | 1 day ago | `orchestration` |
| 3 | [CrewAI](https://github.com/crewAIInc/crewAI) | 🟢 **70.5** | 49.9k | 🚀 +739 | 0 | 1 day ago | `multi-agent` |
| 4 | [LangGraph](https://github.com/langchain-ai/langgraph) | 🟡 **69.1** | 30.4k | 🚀 +793 | 0 | 1 day ago | `orchestration` |
| 5 | [BrowserUse](https://github.com/browser-use/browser-use) | 🟡 **68.9** | 90.3k | 🚀 +1833 | 0 | 23 days ago | `web-agent` |
| 6 | [Composio](https://github.com/ComposioHQ/composio) | 🟡 **65.0** | 27.9k | 📈 +95 | 192 | 1 day ago | `tooling` |
| 7 | [Claude Agent SDK](https://github.com/anthropics/claude-code) | 🟡 **64.5** | 118.0k | 🚀 +2319 | 0 | 2 days ago | `orchestration` |
| 8 | [LlamaIndex](https://github.com/run-llama/llama_index) | 🟡 **61.5** | 48.9k | 🚀 +260 | 0 | 5 days ago | `data-agent` |
| 9 | [DSPy](https://github.com/stanfordnlp/dspy) | 🟡 **59.4** | 34.0k | 🚀 +207 | 34 | 4 days ago | `optimization` |
| 10 | [PydanticAI](https://github.com/pydantic/pydantic-ai) | 🟡 **54.2** | 16.6k | 🚀 +176 | 0 | 1 day ago | `structured` |
| 11 | [Agno](https://github.com/agno-agi/agno) | 🟡 **53.6** | 39.7k | 🚀 +152 | 0 | 1 day ago | `multi-agent` |
| 12 | [Semantic Kernel](https://github.com/microsoft/semantic-kernel) | 🟡 **52.6** | 27.8k | 📈 +46 | 16 | 18 days ago | `enterprise` |
| 13 | [Google ADK](https://github.com/google/adk-python) | 🟡 **52.5** | 19.3k | 🚀 +173 | 0 | 3 days ago | `orchestration` |
| 14 | [Haystack](https://github.com/deepset-ai/haystack) | 🟡 **50.1** | 25.0k | 📈 +97 | 0 | 5 days ago | `pipeline` |
| 15 | [AG2](https://github.com/ag2ai/ag2) | 🟡 **47.9** | 4.4k | 📈 +28 | 0 | 1 day ago | `multi-agent` |
| 16 | [Letta](https://github.com/letta-ai/letta) | 🟡 **46.5** | 22.3k | 🚀 +146 | 0 | 25 days ago | `memory` |
| 17 | [AutoGen](https://github.com/microsoft/autogen) | 🟡 **45.2** | 57.4k | 🚀 +243 | 0 | 6 mo ago | `multi-agent` |
| 18 | [Smolagents](https://github.com/huggingface/smolagents) | 🟠 **39.0** | 26.9k | 🚀 +172 | 0 | 3 mo ago | `lightweight` |
| 19 | [Swarm](https://github.com/openai/swarm) | 🔴 **10.1** | 21.4k | 📈 +51 | 0 | — | `experimental` |

## 📂 By Category

- `data-agent`: **LlamaIndex** (61.5)
- `enterprise`: **Semantic Kernel** (52.6)
- `experimental`: **Swarm** (10.1)
- `lightweight`: **Smolagents** (39.0)
- `memory`: **Letta** (46.5)
- `multi-agent`: **CrewAI** (70.5), **Agno** (53.6), **AG2** (47.9), **AutoGen** (45.2)
- `optimization`: **DSPy** (59.4)
- `orchestration`: **OpenAI Agents SDK** (70.6), **LangGraph** (69.1), **Claude Agent SDK** (64.5), **Google ADK** (52.5)
- `pipeline`: **Haystack** (50.1)
- `structured`: **PydanticAI** (54.2)
- `tooling`: **Composio** (65.0)
- `typescript`: **Mastra** (74.6)
- `web-agent`: **BrowserUse** (68.9)

## 🔍 Top 5 — Score Breakdown

| Framework | Star Velocity | Release Freshness | Issue Health | Commit Activity | Community | Fork Ratio |
|-----------|:---:|:---:|:---:|:---:|:---:|:---:|
| **Mastra** | 36.5 | 99.7 | 94.4 | 100 | 80.2 | 33.5 |
| **OpenAI Agents SDK** | 100 | 99.7 | 96.4 | 0.0 | 51.4 | 61.1 |
| **CrewAI** | 100 | 99.7 | 95.4 | 0.0 | 57.4 | 55.0 |
| **LangGraph** | 100 | 99.7 | 79.2 | 0.0 | 54.8 | 68.4 |
| **BrowserUse** | 100 | 92.3 | 97.6 | 0.0 | 62.0 | 45.7 |

## 💡 Key Insights

- **Hottest framework**: Mastra with a Pulse Score of 74.6
- **Fastest growing**: OpenAI Agents SDK gained +2641 stars this week
- **Most active development**: Mastra with 610 commits in the last 4 weeks
- **Stale releases**: Swarm haven't released in a while

## 📦 Recent Releases

- **Composio** [`@composio/cli@0.2.27-beta.219`](https://github.com/ComposioHQ/composio/releases/tag/@composio/cli@0.2.27-beta.219) — 1 day ago *(pre-release)*
- **OpenAI Agents SDK** [`v0.14.6`](https://github.com/openai/openai-agents-python/releases/tag/v0.14.6) — 1 day ago
- **PydanticAI** [`v1.87.0`](https://github.com/pydantic/pydantic-ai/releases/tag/v1.87.0) — 1 day ago
- **AG2** [`v0.12.1`](https://github.com/ag2ai/ag2/releases/tag/v0.12.1) — 1 day ago
- **LangGraph** [`prebuilt==1.0.11`](https://github.com/langchain-ai/langgraph/releases/tag/prebuilt==1.0.11) — 1 day ago
- **Agno** [`v2.6.1`](https://github.com/agno-agi/agno/releases/tag/v2.6.1) — 1 day ago
- **CrewAI** [`1.14.3`](https://github.com/crewAIInc/crewAI/releases/tag/1.14.3) — 1 day ago
- **Mastra** [`@mastra/core@1.27.0`](https://github.com/mastra-ai/mastra/releases/tag/@mastra/core@1.27.0) — 1 day ago
- **Claude Agent SDK** [`v2.1.119`](https://github.com/anthropics/claude-code/releases/tag/v2.1.119) — 2 days ago
- **Google ADK** [`v2.0.0b1`](https://github.com/google/adk-python/releases/tag/v2.0.0b1) — 3 days ago *(pre-release)*

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

*Powered by GitHub Actions • Data refreshed daily • Last run: 2026-04-26 07:47 UTC*