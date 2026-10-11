# 🔬 AI Agent Framework Pulse Tracker

[![Daily Update](https://github.com/PurpleHaze2320/ai-agent-pulse/actions/workflows/track.yml/badge.svg)](https://github.com/PurpleHaze2320/ai-agent-pulse/actions/workflows/track.yml)
[![Frameworks Tracked](https://img.shields.io/badge/frameworks-19-blue)](https://github.com/PurpleHaze2320/ai-agent-pulse)
[![License: MIT](https://img.shields.io/badge/License-MIT-green.svg)](https://opensource.org/licenses/MIT)
[![GitHub stars](https://img.shields.io/github/stars/PurpleHaze2320/ai-agent-pulse?style=social)](https://github.com/PurpleHaze2320/ai-agent-pulse/stargazers)

> Automated daily tracking of the AI agent framework ecosystem's health, momentum, and trends.
> Last updated: **2026-10-11 12:26 UTC** | Tracking **19** frameworks

## How It Works

This bot runs daily via GitHub Actions and collects metrics from the GitHub API for the most important
AI agent frameworks. It computes a **Pulse Score** (0-100) based on six weighted signals: star velocity,
release freshness, issue health, commit activity, community size, and fork engagement. The result is
a living dashboard that shows which frameworks are gaining momentum and which are losing steam.

## 🏆 Pulse Leaderboard

| Rank | Framework | Pulse | Stars | ⭐ 7d | Commits (4w) | Last Release | Category |
|------|-----------|-------|-------|-------|--------------|--------------|----------|
| 1 | [BrowserUse](https://github.com/browser-use/browser-use) | 🟢 **80.1** | 117.6k | 🚀 +510 | 51 | 4 days ago | `web-agent` |
| 2 | [Claude Agent SDK](https://github.com/anthropics/claude-code) | 🟢 **76.5** | 150.1k | 🚀 +785 | 53 | 1 day ago | `orchestration` |
| 3 | [Mastra](https://github.com/mastra-ai/mastra) | 🟢 **75.9** | 28.7k | 🚀 +153 | 1721 | 3 days ago | `typescript` |
| 4 | [OpenAI Agents SDK](https://github.com/openai/openai-agents-python) | 🟢 **75.9** | 30.0k | 🚀 +135 | 201 | 8 days ago | `orchestration` |
| 5 | [LangGraph](https://github.com/langchain-ai/langgraph) | 🟢 **75.1** | 43.1k | 🚀 +358 | 72 | 3 days ago | `orchestration` |
| 6 | [PydanticAI](https://github.com/pydantic/pydantic-ai) | 🟢 **73.7** | 20.5k | 🚀 +148 | 684 | 5 days ago | `structured` |
| 7 | [Google ADK](https://github.com/google/adk-python) | 🟢 **73.1** | 21.8k | 📈 +74 | 400 | 9 days ago | `orchestration` |
| 8 | [Haystack](https://github.com/deepset-ai/haystack) | 🟢 **71.2** | 26.7k | 📈 +71 | 219 | 10 days ago | `pipeline` |
| 9 | [AG2](https://github.com/ag2ai/ag2) | 🟡 **69.9** | 5.0k | ↗️ +13 | 104 | today | `multi-agent` |
| 10 | [CrewAI](https://github.com/crewAIInc/crewAI) | 🟡 **69.6** | 59.6k | 🚀 +228 | 55 | 1 day ago | `multi-agent` |
| 11 | [Composio](https://github.com/ComposioHQ/composio) | 🟡 **66.0** | 30.5k | 📈 +61 | 189 | 2 days ago | `tooling` |
| 12 | [LlamaIndex](https://github.com/run-llama/llama_index) | 🟡 **55.5** | 52.5k | 📈 +58 | 16 | 19 days ago | `data-agent` |
| 13 | [DSPy](https://github.com/stanfordnlp/dspy) | 🟡 **55.0** | 38.6k | 📈 +96 | 33 | 16 days ago | `optimization` |
| 14 | [Semantic Kernel](https://github.com/microsoft/semantic-kernel) | 🟡 **53.9** | 28.6k | ↗️ +18 | 19 | 4 days ago | `enterprise` |
| 15 | [Agno](https://github.com/agno-agi/agno) | 🟡 **51.2** | 42.7k | 🚀 +115 | 0 | 2 days ago | `multi-agent` |
| 16 | [Letta](https://github.com/letta-ai/letta) | 🟠 **36.2** | 25.1k | 📈 +76 | 0 | 4 mo ago | `memory` |
| 17 | [Smolagents](https://github.com/huggingface/smolagents) | 🟠 **35.0** | 29.8k | 🚀 +114 | 5 | 4 mo ago | `lightweight` |
| 18 | [AutoGen](https://github.com/microsoft/autogen) | 🟠 **32.2** | 61.3k | 📈 +98 | 0 | 1y ago | `multi-agent` |
| 19 | [Swarm](https://github.com/openai/swarm) | 🔴 **9.3** | 22.0k | ↗️ +14 | 0 | — | `experimental` |

## 📂 By Category

- `data-agent`: **LlamaIndex** (55.5)
- `enterprise`: **Semantic Kernel** (53.9)
- `experimental`: **Swarm** (9.3)
- `lightweight`: **Smolagents** (35.0)
- `memory`: **Letta** (36.2)
- `multi-agent`: **AG2** (69.9), **CrewAI** (69.6), **Agno** (51.2), **AutoGen** (32.2)
- `optimization`: **DSPy** (55.0)
- `orchestration`: **Claude Agent SDK** (76.5), **OpenAI Agents SDK** (75.9), **LangGraph** (75.1), **Google ADK** (73.1)
- `pipeline`: **Haystack** (71.2)
- `structured`: **PydanticAI** (73.7)
- `tooling`: **Composio** (66.0)
- `typescript`: **Mastra** (75.9)
- `web-agent`: **BrowserUse** (80.1)

## 🔍 Top 5 — Score Breakdown

| Framework | Star Velocity | Release Freshness | Issue Health | Commit Activity | Community | Fork Ratio |
|-----------|:---:|:---:|:---:|:---:|:---:|:---:|
| **BrowserUse** | 100 | 98.7 | 90.1 | 51.0 | 72.0 | 44.3 |
| **Claude Agent SDK** | 100 | 99.7 | 85.8 | 53.0 | 11.4 | 69.7 |
| **Mastra** | 32.9 | 99.0 | 95.8 | 100 | 93.4 | 41.1 |
| **OpenAI Agents SDK** | 28.0 | 97.3 | 99.1 | 100 | 80.2 | 64.9 |
| **LangGraph** | 74.2 | 99.0 | 66.0 | 72.0 | 56.4 | 68.0 |

## 💡 Key Insights

- **Hottest framework**: BrowserUse with a Pulse Score of 80.1
- **Fastest growing**: Claude Agent SDK gained +785 stars this week
- **Most active development**: Mastra with 1721 commits in the last 4 weeks
- **Stale releases**: AutoGen, Swarm haven't released in a while

## 📦 Recent Releases

- **AG2** [`v1.2.0`](https://github.com/ag2ai/ag2/releases/tag/v1.2.0) — today
- **CrewAI** [`1.15.27`](https://github.com/crewAIInc/crewAI/releases/tag/1.15.27) — 1 day ago
- **Claude Agent SDK** [`v2.1.296`](https://github.com/anthropics/claude-code/releases/tag/v2.1.296) — 1 day ago
- **Agno** [`v3.1.2`](https://github.com/agno-agi/agno/releases/tag/v3.1.2) — 2 days ago
- **Composio** [`@composio/cli@0.4.3-beta.418`](https://github.com/ComposioHQ/composio/releases/tag/@composio/cli@0.4.3-beta.418) — 2 days ago *(pre-release)*
- **Mastra** [`@mastra/core@1.75.0`](https://github.com/mastra-ai/mastra/releases/tag/@mastra/core@1.75.0) — 3 days ago
- **LangGraph** [`cli==0.4.33`](https://github.com/langchain-ai/langgraph/releases/tag/cli==0.4.33) — 3 days ago
- **BrowserUse** [`0.13.11`](https://github.com/browser-use/browser-use/releases/tag/0.13.11) — 4 days ago
- **Semantic Kernel** [`python-1.45.0`](https://github.com/microsoft/semantic-kernel/releases/tag/python-1.45.0) — 4 days ago
- **PydanticAI** [`clai2-bleeding`](https://github.com/pydantic/pydantic-ai/releases/tag/clai2-bleeding) — 5 days ago *(pre-release)*

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

*Powered by GitHub Actions • Data refreshed daily • Last run: 2026-10-11 12:26 UTC*