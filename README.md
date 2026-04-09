# 🔬 AI Agent Framework Pulse Tracker

[![Daily Update](https://github.com/PurpleHaze2320/ai-agent-pulse/actions/workflows/track.yml/badge.svg)](https://github.com/PurpleHaze2320/ai-agent-pulse/actions/workflows/track.yml)
[![Frameworks Tracked](https://img.shields.io/badge/frameworks-19-blue)](https://github.com/PurpleHaze2320/ai-agent-pulse)
[![License: MIT](https://img.shields.io/badge/License-MIT-green.svg)](https://opensource.org/licenses/MIT)
[![GitHub stars](https://img.shields.io/github/stars/PurpleHaze2320/ai-agent-pulse?style=social)](https://github.com/PurpleHaze2320/ai-agent-pulse/stargazers)

> Automated daily tracking of the AI agent framework ecosystem's health, momentum, and trends.
> Last updated: **2026-04-09 07:46 UTC** | Tracking **19** frameworks

## How It Works

This bot runs daily via GitHub Actions and collects metrics from the GitHub API for the most important
AI agent frameworks. It computes a **Pulse Score** (0-100) based on six weighted signals: star velocity,
release freshness, issue health, commit activity, community size, and fork engagement. The result is
a living dashboard that shows which frameworks are gaining momentum and which are losing steam.

## 🏆 Pulse Leaderboard

| Rank | Framework | Pulse | Stars | ⭐ 7d | Commits (4w) | Last Release | Category |
|------|-----------|-------|-------|-------|--------------|--------------|----------|
| 1 | [CrewAI](https://github.com/crewAIInc/crewAI) | 🟢 **87.9** | 48.4k | 🚀 +580 | 179 | today | `multi-agent` |
| 2 | [Mastra](https://github.com/mastra-ai/mastra) | 🟢 **74.3** | 22.8k | 🚀 +241 | 783 | today | `typescript` |
| 3 | [BrowserUse](https://github.com/browser-use/browser-use) | 🟢 **70.0** | 86.6k | 🚀 +1034 | 0 | 6 days ago | `web-agent` |
| 4 | [LangGraph](https://github.com/langchain-ai/langgraph) | 🟡 **66.0** | 28.8k | 🚀 +559 | 0 | 1 day ago | `orchestration` |
| 5 | [Claude Agent SDK](https://github.com/anthropics/claude-code) | 🟡 **64.5** | 111.4k | 🚀 +7967 | 0 | today | `orchestration` |
| 6 | [Composio](https://github.com/ComposioHQ/composio) | 🟡 **63.7** | 27.7k | 📈 +78 | 232 | today | `tooling` |
| 7 | [LlamaIndex](https://github.com/run-llama/llama_index) | 🟡 **57.6** | 48.4k | 🚀 +203 | 0 | 5 days ago | `data-agent` |
| 8 | [Agno](https://github.com/agno-agi/agno) | 🟡 **53.1** | 39.3k | 🚀 +181 | 0 | today | `multi-agent` |
| 9 | [OpenAI Agents SDK](https://github.com/openai/openai-agents-python) | 🟡 **51.5** | 20.7k | 🚀 +155 | 0 | today | `orchestration` |
| 10 | [PydanticAI](https://github.com/pydantic/pydantic-ai) | 🟡 **51.0** | 16.2k | 🚀 +152 | 0 | 1 day ago | `structured` |
| 11 | [Semantic Kernel](https://github.com/microsoft/semantic-kernel) | 🟡 **50.5** | 27.7k | 📈 +58 | 0 | 1 day ago | `enterprise` |
| 12 | [Google ADK](https://github.com/google/adk-python) | 🟡 **48.8** | 18.8k | 🚀 +129 | 0 | 6 days ago | `orchestration` |
| 13 | [Haystack](https://github.com/deepset-ai/haystack) | 🟡 **48.7** | 24.8k | 📈 +88 | 0 | 7 days ago | `pipeline` |
| 14 | [AG2](https://github.com/ag2ai/ag2) | 🟡 **47.3** | 4.4k | 📈 +32 | 0 | 4 days ago | `multi-agent` |
| 15 | [DSPy](https://github.com/stanfordnlp/dspy) | 🟡 **45.9** | 33.5k | 🚀 +178 | 0 | 2 mo ago | `optimization` |
| 16 | [AutoGen](https://github.com/microsoft/autogen) | 🟡 **45.0** | 56.9k | 🚀 +264 | 0 | 6 mo ago | `multi-agent` |
| 17 | [Letta](https://github.com/letta-ai/letta) | 🟡 **44.5** | 22.0k | 📈 +98 | 0 | 8 days ago | `memory` |
| 18 | [Smolagents](https://github.com/huggingface/smolagents) | 🟠 **36.5** | 26.5k | 🚀 +109 | 0 | 2 mo ago | `lightweight` |
| 19 | [Swarm](https://github.com/openai/swarm) | 🔴 **9.3** | 21.3k | ↗️ +17 | 0 | — | `experimental` |

## 📂 By Category

- `data-agent`: **LlamaIndex** (57.6)
- `enterprise`: **Semantic Kernel** (50.5)
- `experimental`: **Swarm** (9.3)
- `lightweight`: **Smolagents** (36.5)
- `memory`: **Letta** (44.5)
- `multi-agent`: **CrewAI** (87.9), **Agno** (53.1), **AG2** (47.3), **AutoGen** (45.0)
- `optimization`: **DSPy** (45.9)
- `orchestration`: **LangGraph** (66.0), **Claude Agent SDK** (64.5), **OpenAI Agents SDK** (51.5), **Google ADK** (48.8)
- `pipeline`: **Haystack** (48.7)
- `structured`: **PydanticAI** (51.0)
- `tooling`: **Composio** (63.7)
- `typescript`: **Mastra** (74.3)
- `web-agent`: **BrowserUse** (70.0)

## 🔍 Top 5 — Score Breakdown

| Framework | Star Velocity | Release Freshness | Issue Health | Commit Activity | Community | Fork Ratio |
|-----------|:---:|:---:|:---:|:---:|:---:|:---:|
| **CrewAI** | 90.1 | 100.0 | 94.8 | 100 | 56.8 | 54.5 |
| **Mastra** | 37.5 | 100.0 | 94.2 | 100 | 75.6 | 32.6 |
| **BrowserUse** | 100 | 98.0 | 97.4 | 0.0 | 61.2 | 46.2 |
| **LangGraph** | 87.0 | 99.7 | 80.3 | 0.0 | 54.4 | 68.3 |
| **Claude Agent SDK** | 100 | 100.0 | 79.2 | 0.0 | 9.4 | 66.8 |

## 💡 Key Insights

- **Hottest framework**: CrewAI with a Pulse Score of 87.9
- **Fastest growing**: Claude Agent SDK gained +7967 stars this week
- **Most active development**: Mastra with 783 commits in the last 4 weeks
- **Stale releases**: Swarm haven't released in a while

## 📦 Recent Releases

- **Agno** [`v2.5.15`](https://github.com/agno-agi/agno/releases/tag/v2.5.15) — today
- **Composio** [`@composio/cli@0.2.20`](https://github.com/ComposioHQ/composio/releases/tag/@composio/cli@0.2.20) — today
- **OpenAI Agents SDK** [`v0.13.6`](https://github.com/openai/openai-agents-python/releases/tag/v0.13.6) — today
- **CrewAI** [`1.14.2a1`](https://github.com/crewAIInc/crewAI/releases/tag/1.14.2a1) — today *(pre-release)*
- **Claude Agent SDK** [`v2.1.97`](https://github.com/anthropics/claude-code/releases/tag/v2.1.97) — today
- **Mastra** [`@mastra/core@1.24.0`](https://github.com/mastra-ai/mastra/releases/tag/@mastra/core@1.24.0) — today
- **Semantic Kernel** [`python-1.41.2`](https://github.com/microsoft/semantic-kernel/releases/tag/python-1.41.2) — 1 day ago
- **PydanticAI** [`v1.78.0`](https://github.com/pydantic/pydantic-ai/releases/tag/v1.78.0) — 1 day ago
- **LangGraph** [`cli==0.4.21`](https://github.com/langchain-ai/langgraph/releases/tag/cli==0.4.21) — 1 day ago
- **AG2** [`v0.11.5`](https://github.com/ag2ai/ag2/releases/tag/v0.11.5) — 4 days ago

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

*Powered by GitHub Actions • Data refreshed daily • Last run: 2026-04-09 07:46 UTC*