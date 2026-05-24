# 🔬 AI Agent Framework Pulse Tracker

[![Daily Update](https://github.com/PurpleHaze2320/ai-agent-pulse/actions/workflows/track.yml/badge.svg)](https://github.com/PurpleHaze2320/ai-agent-pulse/actions/workflows/track.yml)
[![Frameworks Tracked](https://img.shields.io/badge/frameworks-19-blue)](https://github.com/PurpleHaze2320/ai-agent-pulse)
[![License: MIT](https://img.shields.io/badge/License-MIT-green.svg)](https://opensource.org/licenses/MIT)
[![GitHub stars](https://img.shields.io/github/stars/PurpleHaze2320/ai-agent-pulse?style=social)](https://github.com/PurpleHaze2320/ai-agent-pulse/stargazers)

> Automated daily tracking of the AI agent framework ecosystem's health, momentum, and trends.
> Last updated: **2026-05-24 08:37 UTC** | Tracking **19** frameworks

## How It Works

This bot runs daily via GitHub Actions and collects metrics from the GitHub API for the most important
AI agent frameworks. It computes a **Pulse Score** (0-100) based on six weighted signals: star velocity,
release freshness, issue health, commit activity, community size, and fork engagement. The result is
a living dashboard that shows which frameworks are gaining momentum and which are losing steam.

## 🏆 Pulse Leaderboard

| Rank | Framework | Pulse | Stars | ⭐ 7d | Commits (4w) | Last Release | Category |
|------|-----------|-------|-------|-------|--------------|--------------|----------|
| 1 | [Mastra](https://github.com/mastra-ai/mastra) | 🟢 **80.2** | 24.2k | 🚀 +298 | 742 | 5 days ago | `typescript` |
| 2 | [CrewAI](https://github.com/crewAIInc/crewAI) | 🟢 **71.1** | 52.1k | 🚀 +505 | 0 | 2 days ago | `multi-agent` |
| 3 | [BrowserUse](https://github.com/browser-use/browser-use) | 🟢 **70.2** | 95.3k | 🚀 +1030 | 0 | today | `web-agent` |
| 4 | [LangGraph](https://github.com/langchain-ai/langgraph) | 🟡 **68.7** | 32.8k | 🚀 +585 | 0 | 1 day ago | `orchestration` |
| 5 | [Claude Agent SDK](https://github.com/anthropics/claude-code) | 🟡 **64.9** | 126.1k | 🚀 +1864 | 0 | 1 day ago | `orchestration` |
| 6 | [OpenAI Agents SDK](https://github.com/openai/openai-agents-python) | 🟡 **60.4** | 26.6k | 🚀 +235 | 0 | 5 days ago | `orchestration` |
| 7 | [LlamaIndex](https://github.com/run-llama/llama_index) | 🟡 **58.0** | 49.6k | 🚀 +163 | 0 | 9 days ago | `data-agent` |
| 8 | [Agno](https://github.com/agno-agi/agno) | 🟡 **54.3** | 40.3k | 🚀 +163 | 0 | 2 days ago | `multi-agent` |
| 9 | [PydanticAI](https://github.com/pydantic/pydantic-ai) | 🟡 **54.0** | 17.2k | 🚀 +147 | 0 | 1 day ago | `structured` |
| 10 | [Google ADK](https://github.com/google/adk-python) | 🟡 **52.5** | 19.8k | 🚀 +159 | 0 | 1 day ago | `orchestration` |
| 11 | [Semantic Kernel](https://github.com/microsoft/semantic-kernel) | 🟡 **50.7** | 28.0k | 📈 +47 | 0 | 10 days ago | `enterprise` |
| 12 | [Haystack](https://github.com/deepset-ai/haystack) | 🟡 **50.5** | 25.4k | 🚀 +107 | 0 | 11 days ago | `pipeline` |
| 13 | [DSPy](https://github.com/stanfordnlp/dspy) | 🟡 **49.3** | 34.6k | 🚀 +129 | 0 | 18 days ago | `optimization` |
| 14 | [Letta](https://github.com/letta-ai/letta) | 🟡 **49.3** | 22.9k | 🚀 +163 | 0 | 9 days ago | `memory` |
| 15 | [AG2](https://github.com/ag2ai/ag2) | 🟡 **49.2** | 4.6k | 📈 +35 | 0 | 1 day ago | `multi-agent` |
| 16 | [Composio](https://github.com/ComposioHQ/composio) | 🟡 **48.1** | 28.4k | 🚀 +130 | 0 | 3 days ago | `tooling` |
| 17 | [Smolagents](https://github.com/huggingface/smolagents) | 🟡 **44.5** | 27.5k | 🚀 +137 | 0 | 9 days ago | `lightweight` |
| 18 | [AutoGen](https://github.com/microsoft/autogen) | 🟡 **43.7** | 58.3k | 🚀 +243 | 0 | 7 mo ago | `multi-agent` |
| 19 | [Swarm](https://github.com/openai/swarm) | 🔴 **9.2** | 21.5k | 📈 +29 | 0 | — | `experimental` |

## 📂 By Category

- `data-agent`: **LlamaIndex** (58.0)
- `enterprise`: **Semantic Kernel** (50.7)
- `experimental`: **Swarm** (9.2)
- `lightweight`: **Smolagents** (44.5)
- `memory`: **Letta** (49.3)
- `multi-agent`: **CrewAI** (71.1), **Agno** (54.3), **AG2** (49.2), **AutoGen** (43.7)
- `optimization`: **DSPy** (49.3)
- `orchestration`: **LangGraph** (68.7), **Claude Agent SDK** (64.9), **OpenAI Agents SDK** (60.4), **Google ADK** (52.5)
- `pipeline`: **Haystack** (50.5)
- `structured`: **PydanticAI** (54.0)
- `tooling`: **Composio** (48.1)
- `typescript`: **Mastra** (80.2)
- `web-agent`: **BrowserUse** (70.2)

## 🔍 Top 5 — Score Breakdown

| Framework | Star Velocity | Release Freshness | Issue Health | Commit Activity | Community | Fork Ratio |
|-----------|:---:|:---:|:---:|:---:|:---:|:---:|
| **Mastra** | 56.2 | 98.3 | 94.7 | 100 | 87.6 | 34.8 |
| **CrewAI** | 100 | 99.3 | 98.1 | 0.0 | 59.4 | 55.4 |
| **BrowserUse** | 100 | 100.0 | 95.9 | 0.0 | 63.0 | 45.0 |
| **LangGraph** | 100 | 99.7 | 76.6 | 0.0 | 54.8 | 67.7 |
| **Claude Agent SDK** | 100 | 99.7 | 82.7 | 0.0 | 10.0 | 65.7 |

## 💡 Key Insights

- **Hottest framework**: Mastra with a Pulse Score of 80.2
- **Fastest growing**: Claude Agent SDK gained +1864 stars this week
- **Most active development**: Mastra with 742 commits in the last 4 weeks
- **Stale releases**: Swarm haven't released in a while

## 📦 Recent Releases

- **BrowserUse** [`0.12.8`](https://github.com/browser-use/browser-use/releases/tag/0.12.8) — today
- **Claude Agent SDK** [`v2.1.150`](https://github.com/anthropics/claude-code/releases/tag/v2.1.150) — 1 day ago
- **PydanticAI** [`v2.0.0b3`](https://github.com/pydantic/pydantic-ai/releases/tag/v2.0.0b3) — 1 day ago *(pre-release)*
- **AG2** [`v0.13.1`](https://github.com/ag2ai/ag2/releases/tag/v0.13.1) — 1 day ago
- **Google ADK** [`v2.1.0`](https://github.com/google/adk-python/releases/tag/v2.1.0) — 1 day ago
- **LangGraph** [`sdk==0.3.15`](https://github.com/langchain-ai/langgraph/releases/tag/sdk==0.3.15) — 1 day ago
- **Agno** [`v2.6.9`](https://github.com/agno-agi/agno/releases/tag/v2.6.9) — 2 days ago
- **CrewAI** [`1.14.6a1`](https://github.com/crewAIInc/crewAI/releases/tag/1.14.6a1) — 2 days ago *(pre-release)*
- **Composio** [`@composio/cli@0.2.31-beta.256`](https://github.com/ComposioHQ/composio/releases/tag/@composio/cli@0.2.31-beta.256) — 3 days ago *(pre-release)*
- **OpenAI Agents SDK** [`v0.17.3`](https://github.com/openai/openai-agents-python/releases/tag/v0.17.3) — 5 days ago

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

*Powered by GitHub Actions • Data refreshed daily • Last run: 2026-05-24 08:37 UTC*