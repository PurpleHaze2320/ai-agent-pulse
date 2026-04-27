# 🔬 AI Agent Framework Pulse Tracker

[![Daily Update](https://github.com/PurpleHaze2320/ai-agent-pulse/actions/workflows/track.yml/badge.svg)](https://github.com/PurpleHaze2320/ai-agent-pulse/actions/workflows/track.yml)
[![Frameworks Tracked](https://img.shields.io/badge/frameworks-19-blue)](https://github.com/PurpleHaze2320/ai-agent-pulse)
[![License: MIT](https://img.shields.io/badge/License-MIT-green.svg)](https://opensource.org/licenses/MIT)
[![GitHub stars](https://img.shields.io/github/stars/PurpleHaze2320/ai-agent-pulse?style=social)](https://github.com/PurpleHaze2320/ai-agent-pulse/stargazers)

> Automated daily tracking of the AI agent framework ecosystem's health, momentum, and trends.
> Last updated: **2026-04-27 08:35 UTC** | Tracking **19** frameworks

## How It Works

This bot runs daily via GitHub Actions and collects metrics from the GitHub API for the most important
AI agent frameworks. It computes a **Pulse Score** (0-100) based on six weighted signals: star velocity,
release freshness, issue health, commit activity, community size, and fork engagement. The result is
a living dashboard that shows which frameworks are gaining momentum and which are losing steam.

## 🏆 Pulse Leaderboard

| Rank | Framework | Pulse | Stars | ⭐ 7d | Commits (4w) | Last Release | Category |
|------|-----------|-------|-------|-------|--------------|--------------|----------|
| 1 | [Mastra](https://github.com/mastra-ai/mastra) | 🟢 **74.8** | 23.3k | 🚀 +186 | 621 | 2 days ago | `typescript` |
| 2 | [OpenAI Agents SDK](https://github.com/openai/openai-agents-python) | 🟢 **70.6** | 25.4k | 🚀 +1827 | 0 | 2 days ago | `orchestration` |
| 3 | [CrewAI](https://github.com/crewAIInc/crewAI) | 🟢 **70.4** | 50.0k | 🚀 +749 | 0 | 2 days ago | `multi-agent` |
| 4 | [LangGraph](https://github.com/langchain-ai/langgraph) | 🟡 **69.1** | 30.5k | 🚀 +817 | 0 | 2 days ago | `orchestration` |
| 5 | [BrowserUse](https://github.com/browser-use/browser-use) | 🟡 **68.7** | 90.6k | 🚀 +1806 | 0 | 25 days ago | `web-agent` |
| 6 | [Claude Agent SDK](https://github.com/anthropics/claude-code) | 🟡 **64.5** | 118.3k | 🚀 +2259 | 0 | 3 days ago | `orchestration` |
| 7 | [LlamaIndex](https://github.com/run-llama/llama_index) | 🟡 **61.6** | 49.0k | 🚀 +262 | 0 | 6 days ago | `data-agent` |
| 8 | [Agno](https://github.com/agno-agi/agno) | 🟡 **54.4** | 39.7k | 🚀 +175 | 0 | 2 days ago | `multi-agent` |
| 9 | [PydanticAI](https://github.com/pydantic/pydantic-ai) | 🟡 **54.3** | 16.7k | 🚀 +176 | 0 | 2 days ago | `structured` |
| 10 | [Google ADK](https://github.com/google/adk-python) | 🟡 **52.4** | 19.3k | 🚀 +172 | 0 | 4 days ago | `orchestration` |
| 11 | [DSPy](https://github.com/stanfordnlp/dspy) | 🟡 **51.5** | 34.0k | 🚀 +175 | 0 | 5 days ago | `optimization` |
| 12 | [Haystack](https://github.com/deepset-ai/haystack) | 🟡 **49.7** | 25.0k | 📈 +87 | 0 | 6 days ago | `pipeline` |
| 13 | [Semantic Kernel](https://github.com/microsoft/semantic-kernel) | 🟡 **49.3** | 27.8k | 📈 +41 | 0 | 19 days ago | `enterprise` |
| 14 | [AG2](https://github.com/ag2ai/ag2) | 🟡 **47.8** | 4.4k | 📈 +25 | 0 | 2 days ago | `multi-agent` |
| 15 | [Letta](https://github.com/letta-ai/letta) | 🟡 **46.6** | 22.3k | 🚀 +148 | 0 | 26 days ago | `memory` |
| 16 | [AutoGen](https://github.com/microsoft/autogen) | 🟡 **45.6** | 57.5k | 🚀 +251 | 0 | 6 mo ago | `multi-agent` |
| 17 | [Composio](https://github.com/ComposioHQ/composio) | 🟡 **45.1** | 27.9k | 📈 +98 | 0 | 2 days ago | `tooling` |
| 18 | [Smolagents](https://github.com/huggingface/smolagents) | 🟠 **39.1** | 26.9k | 🚀 +175 | 0 | 3 mo ago | `lightweight` |
| 19 | [Swarm](https://github.com/openai/swarm) | 🔴 **9.8** | 21.4k | 📈 +43 | 0 | — | `experimental` |

## 📂 By Category

- `data-agent`: **LlamaIndex** (61.6)
- `enterprise`: **Semantic Kernel** (49.3)
- `experimental`: **Swarm** (9.8)
- `lightweight`: **Smolagents** (39.1)
- `memory`: **Letta** (46.6)
- `multi-agent`: **CrewAI** (70.4), **Agno** (54.4), **AG2** (47.8), **AutoGen** (45.6)
- `optimization`: **DSPy** (51.5)
- `orchestration`: **OpenAI Agents SDK** (70.6), **LangGraph** (69.1), **Claude Agent SDK** (64.5), **Google ADK** (52.4)
- `pipeline`: **Haystack** (49.7)
- `structured`: **PydanticAI** (54.3)
- `tooling`: **Composio** (45.1)
- `typescript`: **Mastra** (74.8)
- `web-agent`: **BrowserUse** (68.7)

## 🔍 Top 5 — Score Breakdown

| Framework | Star Velocity | Release Freshness | Issue Health | Commit Activity | Community | Fork Ratio |
|-----------|:---:|:---:|:---:|:---:|:---:|:---:|
| **Mastra** | 37.7 | 99.3 | 94.4 | 100 | 80.2 | 33.6 |
| **OpenAI Agents SDK** | 100 | 99.3 | 96.4 | 0.0 | 51.6 | 61.0 |
| **CrewAI** | 100 | 99.3 | 95.5 | 0.0 | 57.4 | 55.0 |
| **LangGraph** | 100 | 99.3 | 79.1 | 0.0 | 54.8 | 68.4 |
| **BrowserUse** | 100 | 91.7 | 97.5 | 0.0 | 62.2 | 45.6 |

## 💡 Key Insights

- **Hottest framework**: Mastra with a Pulse Score of 74.8
- **Fastest growing**: Claude Agent SDK gained +2259 stars this week
- **Most active development**: Mastra with 621 commits in the last 4 weeks
- **Stale releases**: Swarm haven't released in a while

## 📦 Recent Releases

- **Composio** [`@composio/cli@0.2.27-beta.219`](https://github.com/ComposioHQ/composio/releases/tag/@composio/cli@0.2.27-beta.219) — 2 days ago *(pre-release)*
- **OpenAI Agents SDK** [`v0.14.6`](https://github.com/openai/openai-agents-python/releases/tag/v0.14.6) — 2 days ago
- **PydanticAI** [`v1.87.0`](https://github.com/pydantic/pydantic-ai/releases/tag/v1.87.0) — 2 days ago
- **AG2** [`v0.12.1`](https://github.com/ag2ai/ag2/releases/tag/v0.12.1) — 2 days ago
- **LangGraph** [`prebuilt==1.0.11`](https://github.com/langchain-ai/langgraph/releases/tag/prebuilt==1.0.11) — 2 days ago
- **Agno** [`v2.6.1`](https://github.com/agno-agi/agno/releases/tag/v2.6.1) — 2 days ago
- **CrewAI** [`1.14.3`](https://github.com/crewAIInc/crewAI/releases/tag/1.14.3) — 2 days ago
- **Mastra** [`@mastra/core@1.27.0`](https://github.com/mastra-ai/mastra/releases/tag/@mastra/core@1.27.0) — 2 days ago
- **Claude Agent SDK** [`v2.1.119`](https://github.com/anthropics/claude-code/releases/tag/v2.1.119) — 3 days ago
- **Google ADK** [`v2.0.0b1`](https://github.com/google/adk-python/releases/tag/v2.0.0b1) — 4 days ago *(pre-release)*

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

*Powered by GitHub Actions • Data refreshed daily • Last run: 2026-04-27 08:35 UTC*