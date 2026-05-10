# 🔬 AI Agent Framework Pulse Tracker

[![Daily Update](https://github.com/PurpleHaze2320/ai-agent-pulse/actions/workflows/track.yml/badge.svg)](https://github.com/PurpleHaze2320/ai-agent-pulse/actions/workflows/track.yml)
[![Frameworks Tracked](https://img.shields.io/badge/frameworks-19-blue)](https://github.com/PurpleHaze2320/ai-agent-pulse)
[![License: MIT](https://img.shields.io/badge/License-MIT-green.svg)](https://opensource.org/licenses/MIT)
[![GitHub stars](https://img.shields.io/github/stars/PurpleHaze2320/ai-agent-pulse?style=social)](https://github.com/PurpleHaze2320/ai-agent-pulse/stargazers)

> Automated daily tracking of the AI agent framework ecosystem's health, momentum, and trends.
> Last updated: **2026-05-10 08:15 UTC** | Tracking **19** frameworks

## How It Works

This bot runs daily via GitHub Actions and collects metrics from the GitHub API for the most important
AI agent frameworks. It computes a **Pulse Score** (0-100) based on six weighted signals: star velocity,
release freshness, issue health, commit activity, community size, and fork engagement. The result is
a living dashboard that shows which frameworks are gaining momentum and which are losing steam.

## 🏆 Pulse Leaderboard

| Rank | Framework | Pulse | Stars | ⭐ 7d | Commits (4w) | Last Release | Category |
|------|-----------|-------|-------|-------|--------------|--------------|----------|
| 1 | [Mastra](https://github.com/mastra-ai/mastra) | 🟢 **77.7** | 23.7k | 🚀 +240 | 813 | 3 days ago | `typescript` |
| 2 | [CrewAI](https://github.com/crewAIInc/crewAI) | 🟢 **71.2** | 51.0k | 🚀 +537 | 0 | 1 day ago | `multi-agent` |
| 3 | [OpenAI Agents SDK](https://github.com/openai/openai-agents-python) | 🟢 **70.8** | 26.1k | 🚀 +326 | 0 | 2 days ago | `orchestration` |
| 4 | [LangGraph](https://github.com/langchain-ai/langgraph) | 🟡 **68.8** | 31.6k | 🚀 +562 | 0 | 2 days ago | `orchestration` |
| 5 | [BrowserUse](https://github.com/browser-use/browser-use) | 🟡 **67.8** | 93.2k | 🚀 +1384 | 0 | 1 mo ago | `web-agent` |
| 6 | [Claude Agent SDK](https://github.com/anthropics/claude-code) | 🟡 **64.7** | 122.1k | 🚀 +2121 | 0 | 1 day ago | `orchestration` |
| 7 | [LlamaIndex](https://github.com/run-llama/llama_index) | 🟡 **57.8** | 49.3k | 🚀 +171 | 0 | 19 days ago | `data-agent` |
| 8 | [PydanticAI](https://github.com/pydantic/pydantic-ai) | 🟡 **54.2** | 17.0k | 🚀 +153 | 0 | 1 day ago | `structured` |
| 9 | [Agno](https://github.com/agno-agi/agno) | 🟡 **54.2** | 40.0k | 🚀 +158 | 0 | 3 days ago | `multi-agent` |
| 10 | [Google ADK](https://github.com/google/adk-python) | 🟡 **52.4** | 19.6k | 🚀 +148 | 0 | 1 day ago | `orchestration` |
| 11 | [DSPy](https://github.com/stanfordnlp/dspy) | 🟡 **51.0** | 34.3k | 🚀 +144 | 0 | 4 days ago | `optimization` |
| 12 | [Semantic Kernel](https://github.com/microsoft/semantic-kernel) | 🟡 **50.8** | 27.9k | 📈 +51 | 0 | 10 days ago | `enterprise` |
| 13 | [AG2](https://github.com/ag2ai/ag2) | 🟡 **49.5** | 4.5k | 📈 +56 | 0 | 4 days ago | `multi-agent` |
| 14 | [Haystack](https://github.com/deepset-ai/haystack) | 🟡 **48.8** | 25.1k | 📈 +79 | 0 | 19 days ago | `pipeline` |
| 15 | [Letta](https://github.com/letta-ai/letta) | 🟡 **47.3** | 22.6k | 🚀 +174 | 0 | 1 mo ago | `memory` |
| 16 | [Composio](https://github.com/ComposioHQ/composio) | 🟡 **47.0** | 28.1k | 🚀 +137 | 0 | 2 days ago | `tooling` |
| 17 | [AutoGen](https://github.com/microsoft/autogen) | 🟡 **43.5** | 57.9k | 🚀 +208 | 0 | 7 mo ago | `multi-agent` |
| 18 | [Smolagents](https://github.com/huggingface/smolagents) | 🟠 **37.5** | 27.2k | 🚀 +138 | 0 | 3 mo ago | `lightweight` |
| 19 | [Swarm](https://github.com/openai/swarm) | 🔴 **9.9** | 21.5k | 📈 +43 | 0 | — | `experimental` |

## 📂 By Category

- `data-agent`: **LlamaIndex** (57.8)
- `enterprise`: **Semantic Kernel** (50.8)
- `experimental`: **Swarm** (9.9)
- `lightweight`: **Smolagents** (37.5)
- `memory`: **Letta** (47.3)
- `multi-agent`: **CrewAI** (71.2), **Agno** (54.2), **AG2** (49.5), **AutoGen** (43.5)
- `optimization`: **DSPy** (51.0)
- `orchestration`: **OpenAI Agents SDK** (70.8), **LangGraph** (68.8), **Claude Agent SDK** (64.7), **Google ADK** (52.4)
- `pipeline`: **Haystack** (48.8)
- `structured`: **PydanticAI** (54.2)
- `tooling`: **Composio** (47.0)
- `typescript`: **Mastra** (77.7)
- `web-agent`: **BrowserUse** (67.8)

## 🔍 Top 5 — Score Breakdown

| Framework | Star Velocity | Release Freshness | Issue Health | Commit Activity | Community | Fork Ratio |
|-----------|:---:|:---:|:---:|:---:|:---:|:---:|
| **Mastra** | 46.8 | 99.0 | 94.6 | 100 | 85.8 | 34.4 |
| **CrewAI** | 100 | 99.7 | 98.6 | 0.0 | 59.2 | 55.3 |
| **OpenAI Agents SDK** | 100 | 99.3 | 96.3 | 0.0 | 53.2 | 61.4 |
| **LangGraph** | 100 | 99.3 | 78.1 | 0.0 | 54.6 | 68.0 |
| **BrowserUse** | 100 | 87.3 | 96.4 | 0.0 | 63.0 | 45.3 |

## 💡 Key Insights

- **Hottest framework**: Mastra with a Pulse Score of 77.7
- **Fastest growing**: Claude Agent SDK gained +2121 stars this week
- **Most active development**: Mastra with 813 commits in the last 4 weeks
- **Stale releases**: Swarm haven't released in a while

## 📦 Recent Releases

- **Claude Agent SDK** [`v2.1.138`](https://github.com/anthropics/claude-code/releases/tag/v2.1.138) — 1 day ago
- **PydanticAI** [`v1.93.0`](https://github.com/pydantic/pydantic-ai/releases/tag/v1.93.0) — 1 day ago
- **Google ADK** [`v1.33.0`](https://github.com/google/adk-python/releases/tag/v1.33.0) — 1 day ago
- **CrewAI** [`1.14.5a4`](https://github.com/crewAIInc/crewAI/releases/tag/1.14.5a4) — 1 day ago *(pre-release)*
- **OpenAI Agents SDK** [`v0.17.0`](https://github.com/openai/openai-agents-python/releases/tag/v0.17.0) — 2 days ago
- **LangGraph** [`cli==0.4.25`](https://github.com/langchain-ai/langgraph/releases/tag/cli==0.4.25) — 2 days ago
- **Composio** [`py@0.13.0`](https://github.com/ComposioHQ/composio/releases/tag/py@0.13.0) — 2 days ago
- **Agno** [`v2.6.5`](https://github.com/agno-agi/agno/releases/tag/v2.6.5) — 3 days ago
- **Mastra** [`@mastra/core@1.32.0`](https://github.com/mastra-ai/mastra/releases/tag/@mastra/core@1.32.0) — 3 days ago
- **AG2** [`v0.12.3`](https://github.com/ag2ai/ag2/releases/tag/v0.12.3) — 4 days ago

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

*Powered by GitHub Actions • Data refreshed daily • Last run: 2026-05-10 08:15 UTC*