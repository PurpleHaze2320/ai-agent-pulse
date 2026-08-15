# 🔬 AI Agent Framework Pulse Tracker

[![Daily Update](https://github.com/PurpleHaze2320/ai-agent-pulse/actions/workflows/track.yml/badge.svg)](https://github.com/PurpleHaze2320/ai-agent-pulse/actions/workflows/track.yml)
[![Frameworks Tracked](https://img.shields.io/badge/frameworks-19-blue)](https://github.com/PurpleHaze2320/ai-agent-pulse)
[![License: MIT](https://img.shields.io/badge/License-MIT-green.svg)](https://opensource.org/licenses/MIT)
[![GitHub stars](https://img.shields.io/github/stars/PurpleHaze2320/ai-agent-pulse?style=social)](https://github.com/PurpleHaze2320/ai-agent-pulse/stargazers)

> Automated daily tracking of the AI agent framework ecosystem's health, momentum, and trends.
> Last updated: **2026-08-15 06:46 UTC** | Tracking **19** frameworks

## How It Works

This bot runs daily via GitHub Actions and collects metrics from the GitHub API for the most important
AI agent frameworks. It computes a **Pulse Score** (0-100) based on six weighted signals: star velocity,
release freshness, issue health, commit activity, community size, and fork engagement. The result is
a living dashboard that shows which frameworks are gaining momentum and which are losing steam.

## 🏆 Pulse Leaderboard

| Rank | Framework | Pulse | Stars | ⭐ 7d | Commits (4w) | Last Release | Category |
|------|-----------|-------|-------|-------|--------------|--------------|----------|
| 1 | [BrowserUse](https://github.com/browser-use/browser-use) | 🟢 **89.0** | 109.3k | 🚀 +1035 | 161 | 18 days ago | `web-agent` |
| 2 | [CrewAI](https://github.com/crewAIInc/crewAI) | 🟢 **80.9** | 57.1k | 🚀 +322 | 91 | 1 day ago | `multi-agent` |
| 3 | [Mastra](https://github.com/mastra-ai/mastra) | 🟢 **77.2** | 27.2k | 🚀 +172 | 1581 | 2 days ago | `typescript` |
| 4 | [OpenAI Agents SDK](https://github.com/openai/openai-agents-python) | 🟢 **76.4** | 28.6k | 🚀 +163 | 348 | today | `orchestration` |
| 5 | [PydanticAI](https://github.com/pydantic/pydantic-ai) | 🟢 **75.7** | 19.3k | 🚀 +164 | 283 | today | `structured` |
| 6 | [LangGraph](https://github.com/langchain-ai/langgraph) | 🟢 **75.6** | 39.7k | 🚀 +533 | 40 | 3 days ago | `orchestration` |
| 7 | [Google ADK](https://github.com/google/adk-python) | 🟢 **73.5** | 21.1k | 📈 +75 | 431 | 1 day ago | `orchestration` |
| 8 | [DSPy](https://github.com/stanfordnlp/dspy) | 🟢 **73.4** | 37.2k | 🚀 +505 | 44 | 11 days ago | `optimization` |
| 9 | [Haystack](https://github.com/deepset-ai/haystack) | 🟡 **69.5** | 26.2k | 📈 +71 | 211 | 25 days ago | `pipeline` |
| 10 | [Claude Agent SDK](https://github.com/anthropics/claude-code) | 🟡 **68.7** | 141.5k | 🚀 +864 | 20 | today | `orchestration` |
| 11 | [Composio](https://github.com/ComposioHQ/composio) | 🟡 **68.0** | 29.7k | 🚀 +112 | 317 | 1 day ago | `tooling` |
| 12 | [Agno](https://github.com/agno-agi/agno) | 🟡 **66.0** | 41.7k | 📈 +94 | 74 | 1 day ago | `multi-agent` |
| 13 | [LlamaIndex](https://github.com/run-llama/llama_index) | 🟡 **63.5** | 51.6k | 🚀 +197 | 34 | 1 mo ago | `data-agent` |
| 14 | [Semantic Kernel](https://github.com/microsoft/semantic-kernel) | 🟡 **54.0** | 28.4k | ↗️ +20 | 20 | 8 days ago | `enterprise` |
| 15 | [AG2](https://github.com/ag2ai/ag2) | 🟡 **50.3** | 4.9k | 📈 +22 | 0 | today | `multi-agent` |
| 16 | [Letta](https://github.com/letta-ai/letta) | 🟡 **41.4** | 24.2k | 📈 +99 | 3 | 3 mo ago | `memory` |
| 17 | [Smolagents](https://github.com/huggingface/smolagents) | 🟠 **37.1** | 28.8k | 📈 +83 | 0 | 2 mo ago | `lightweight` |
| 18 | [AutoGen](https://github.com/microsoft/autogen) | 🟠 **33.9** | 60.4k | 🚀 +120 | 0 | 10 mo ago | `multi-agent` |
| 19 | [Swarm](https://github.com/openai/swarm) | 🔴 **9.5** | 21.9k | ↗️ +16 | 0 | — | `experimental` |

## 📂 By Category

- `data-agent`: **LlamaIndex** (63.5)
- `enterprise`: **Semantic Kernel** (54.0)
- `experimental`: **Swarm** (9.5)
- `lightweight`: **Smolagents** (37.1)
- `memory`: **Letta** (41.4)
- `multi-agent`: **CrewAI** (80.9), **Agno** (66.0), **AG2** (50.3), **AutoGen** (33.9)
- `optimization`: **DSPy** (73.4)
- `orchestration`: **OpenAI Agents SDK** (76.4), **LangGraph** (75.6), **Google ADK** (73.5), **Claude Agent SDK** (68.7)
- `pipeline`: **Haystack** (69.5)
- `structured`: **PydanticAI** (75.7)
- `tooling`: **Composio** (68.0)
- `typescript`: **Mastra** (77.2)
- `web-agent`: **BrowserUse** (89.0)

## 🔍 Top 5 — Score Breakdown

| Framework | Star Velocity | Release Freshness | Issue Health | Commit Activity | Community | Fork Ratio |
|-----------|:---:|:---:|:---:|:---:|:---:|:---:|
| **BrowserUse** | 100 | 94.0 | 93.9 | 100 | 66.8 | 44.0 |
| **CrewAI** | 67.3 | 99.7 | 94.9 | 91.0 | 60.0 | 57.1 |
| **Mastra** | 39.1 | 99.3 | 96.2 | 100 | 92.8 | 38.7 |
| **OpenAI Agents SDK** | 33.4 | 100.0 | 99.2 | 100 | 68.6 | 62.8 |
| **PydanticAI** | 34.0 | 100.0 | 83.0 | 100 | 95.0 | 52.3 |

## 💡 Key Insights

- **Hottest framework**: BrowserUse with a Pulse Score of 89.0
- **Fastest growing**: BrowserUse gained +1035 stars this week
- **Most active development**: Mastra with 1581 commits in the last 4 weeks
- **Stale releases**: AutoGen, Swarm haven't released in a while

## 📦 Recent Releases

- **AG2** [`v1.0.2`](https://github.com/ag2ai/ag2/releases/tag/v1.0.2) — today
- **PydanticAI** [`v2.31.0`](https://github.com/pydantic/pydantic-ai/releases/tag/v2.31.0) — today
- **OpenAI Agents SDK** [`v0.21.0`](https://github.com/openai/openai-agents-python/releases/tag/v0.21.0) — today
- **Claude Agent SDK** [`v2.1.233`](https://github.com/anthropics/claude-code/releases/tag/v2.1.233) — today
- **CrewAI** [`1.15.16`](https://github.com/crewAIInc/crewAI/releases/tag/1.15.16) — 1 day ago
- **Google ADK** [`v2.7.0`](https://github.com/google/adk-python/releases/tag/v2.7.0) — 1 day ago
- **Composio** [`@composio/cli@0.3.4-beta.351`](https://github.com/ComposioHQ/composio/releases/tag/@composio/cli@0.3.4-beta.351) — 1 day ago *(pre-release)*
- **Agno** [`v2.9.0`](https://github.com/agno-agi/agno/releases/tag/v2.9.0) — 1 day ago
- **Mastra** [`@mastra/core@1.58.0`](https://github.com/mastra-ai/mastra/releases/tag/@mastra/core@1.58.0) — 2 days ago
- **LangGraph** [`1.2.11`](https://github.com/langchain-ai/langgraph/releases/tag/1.2.11) — 3 days ago

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

*Powered by GitHub Actions • Data refreshed daily • Last run: 2026-08-15 06:46 UTC*