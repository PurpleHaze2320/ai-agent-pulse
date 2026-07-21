# 🔬 AI Agent Framework Pulse Tracker

[![Daily Update](https://github.com/PurpleHaze2320/ai-agent-pulse/actions/workflows/track.yml/badge.svg)](https://github.com/PurpleHaze2320/ai-agent-pulse/actions/workflows/track.yml)
[![Frameworks Tracked](https://img.shields.io/badge/frameworks-19-blue)](https://github.com/PurpleHaze2320/ai-agent-pulse)
[![License: MIT](https://img.shields.io/badge/License-MIT-green.svg)](https://opensource.org/licenses/MIT)
[![GitHub stars](https://img.shields.io/github/stars/PurpleHaze2320/ai-agent-pulse?style=social)](https://github.com/PurpleHaze2320/ai-agent-pulse/stargazers)

> Automated daily tracking of the AI agent framework ecosystem's health, momentum, and trends.
> Last updated: **2026-07-21 08:37 UTC** | Tracking **19** frameworks

## How It Works

This bot runs daily via GitHub Actions and collects metrics from the GitHub API for the most important
AI agent frameworks. It computes a **Pulse Score** (0-100) based on six weighted signals: star velocity,
release freshness, issue health, commit activity, community size, and fork engagement. The result is
a living dashboard that shows which frameworks are gaining momentum and which are losing steam.

## 🏆 Pulse Leaderboard

| Rank | Framework | Pulse | Stars | ⭐ 7d | Commits (4w) | Last Release | Category |
|------|-----------|-------|-------|-------|--------------|--------------|----------|
| 1 | [BrowserUse](https://github.com/browser-use/browser-use) | 🟢 **84.1** | 105.8k | 🚀 +1169 | 72 | 4 days ago | `web-agent` |
| 2 | [CrewAI](https://github.com/crewAIInc/crewAI) | 🟢 **79.7** | 55.9k | 🚀 +395 | 65 | today | `multi-agent` |
| 3 | [Mastra](https://github.com/mastra-ai/mastra) | 🟢 **79.3** | 26.4k | 🚀 +236 | 916 | 5 days ago | `typescript` |
| 4 | [PydanticAI](https://github.com/pydantic/pydantic-ai) | 🟢 **76.9** | 18.7k | 🚀 +184 | 233 | today | `structured` |
| 5 | [Google ADK](https://github.com/google/adk-python) | 🟢 **76.7** | 20.8k | 🚀 +217 | 274 | 13 days ago | `orchestration` |
| 6 | [OpenAI Agents SDK](https://github.com/openai/openai-agents-python) | 🟢 **75.3** | 28.1k | 🚀 +159 | 112 | 4 days ago | `orchestration` |
| 7 | [Agno](https://github.com/agno-agi/agno) | 🟢 **74.4** | 41.3k | 🚀 +168 | 135 | today | `multi-agent` |
| 8 | [LangGraph](https://github.com/langchain-ai/langgraph) | 🟢 **72.5** | 37.7k | 🚀 +480 | 26 | 11 days ago | `orchestration` |
| 9 | [Claude Agent SDK](https://github.com/anthropics/claude-code) | 🟡 **69.9** | 138.5k | 🚀 +730 | 24 | today | `orchestration` |
| 10 | [LlamaIndex](https://github.com/run-llama/llama_index) | 🟡 **56.2** | 51.0k | 🚀 +144 | 0 | 26 days ago | `data-agent` |
| 11 | [Haystack](https://github.com/deepset-ai/haystack) | 🟡 **51.1** | 26.0k | 📈 +77 | 0 | today | `pipeline` |
| 12 | [Semantic Kernel](https://github.com/microsoft/semantic-kernel) | 🟡 **50.0** | 28.3k | 📈 +27 | 0 | 13 days ago | `enterprise` |
| 13 | [DSPy](https://github.com/stanfordnlp/dspy) | 🟡 **49.5** | 36.3k | 🚀 +159 | 0 | 1 mo ago | `optimization` |
| 14 | [AG2](https://github.com/ag2ai/ag2) | 🟡 **48.9** | 4.8k | ↗️ +18 | 0 | 17 days ago | `multi-agent` |
| 15 | [Composio](https://github.com/ComposioHQ/composio) | 🟡 **46.4** | 29.3k | 📈 +76 | 0 | today | `tooling` |
| 16 | [Letta](https://github.com/letta-ai/letta) | 🟡 **43.0** | 23.9k | 🚀 +115 | 0 | 2 mo ago | `memory` |
| 17 | [Smolagents](https://github.com/huggingface/smolagents) | 🟡 **41.2** | 28.5k | 🚀 +117 | 4 | 1 mo ago | `lightweight` |
| 18 | [AutoGen](https://github.com/microsoft/autogen) | 🟠 **35.5** | 59.9k | 🚀 +146 | 0 | 9 mo ago | `multi-agent` |
| 19 | [Swarm](https://github.com/openai/swarm) | 🔴 **10.3** | 21.8k | 📈 +52 | 0 | — | `experimental` |

## 📂 By Category

- `data-agent`: **LlamaIndex** (56.2)
- `enterprise`: **Semantic Kernel** (50.0)
- `experimental`: **Swarm** (10.3)
- `lightweight`: **Smolagents** (41.2)
- `memory`: **Letta** (43.0)
- `multi-agent`: **CrewAI** (79.7), **Agno** (74.4), **AG2** (48.9), **AutoGen** (35.5)
- `optimization`: **DSPy** (49.5)
- `orchestration`: **Google ADK** (76.7), **OpenAI Agents SDK** (75.3), **LangGraph** (72.5), **Claude Agent SDK** (69.9)
- `pipeline`: **Haystack** (51.1)
- `structured`: **PydanticAI** (76.9)
- `tooling`: **Composio** (46.4)
- `typescript`: **Mastra** (79.3)
- `web-agent`: **BrowserUse** (84.1)

## 🔍 Top 5 — Score Breakdown

| Framework | Star Velocity | Release Freshness | Issue Health | Commit Activity | Community | Fork Ratio |
|-----------|:---:|:---:|:---:|:---:|:---:|:---:|
| **BrowserUse** | 100 | 98.7 | 94.8 | 72.0 | 63.0 | 44.0 |
| **CrewAI** | 82.6 | 100.0 | 96.2 | 65.0 | 59.6 | 56.5 |
| **Mastra** | 49.5 | 98.3 | 94.9 | 100 | 93.0 | 37.6 |
| **PydanticAI** | 37.9 | 100.0 | 85.7 | 100 | 94.8 | 51.3 |
| **Google ADK** | 39.5 | 95.7 | 87.1 | 100 | 75.0 | 71.7 |

## 💡 Key Insights

- **Hottest framework**: BrowserUse with a Pulse Score of 84.1
- **Fastest growing**: BrowserUse gained +1169 stars this week
- **Most active development**: Mastra with 916 commits in the last 4 weeks
- **Stale releases**: AutoGen, Swarm haven't released in a while

## 📦 Recent Releases

- **Composio** [`@composio/cli@0.2.33-beta.298`](https://github.com/ComposioHQ/composio/releases/tag/@composio/cli@0.2.33-beta.298) — today *(pre-release)*
- **PydanticAI** [`v2.14.1`](https://github.com/pydantic/pydantic-ai/releases/tag/v2.14.1) — today
- **Claude Agent SDK** [`v2.1.216`](https://github.com/anthropics/claude-code/releases/tag/v2.1.216) — today
- **CrewAI** [`1.15.5`](https://github.com/crewAIInc/crewAI/releases/tag/1.15.5) — today
- **Agno** [`v2.8.0`](https://github.com/agno-agi/agno/releases/tag/v2.8.0) — today
- **Haystack** [`v3.0.0`](https://github.com/deepset-ai/haystack/releases/tag/v3.0.0) — today
- **BrowserUse** [`0.13.6`](https://github.com/browser-use/browser-use/releases/tag/0.13.6) — 4 days ago
- **OpenAI Agents SDK** [`v0.18.3`](https://github.com/openai/openai-agents-python/releases/tag/v0.18.3) — 4 days ago
- **Mastra** [`@mastra/core@1.51.0`](https://github.com/mastra-ai/mastra/releases/tag/@mastra/core@1.51.0) — 5 days ago
- **LangGraph** [`1.2.9`](https://github.com/langchain-ai/langgraph/releases/tag/1.2.9) — 11 days ago

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

*Powered by GitHub Actions • Data refreshed daily • Last run: 2026-07-21 08:37 UTC*