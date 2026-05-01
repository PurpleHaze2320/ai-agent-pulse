# 🔬 AI Agent Framework Pulse Tracker

[![Daily Update](https://github.com/PurpleHaze2320/ai-agent-pulse/actions/workflows/track.yml/badge.svg)](https://github.com/PurpleHaze2320/ai-agent-pulse/actions/workflows/track.yml)
[![Frameworks Tracked](https://img.shields.io/badge/frameworks-19-blue)](https://github.com/PurpleHaze2320/ai-agent-pulse)
[![License: MIT](https://img.shields.io/badge/License-MIT-green.svg)](https://opensource.org/licenses/MIT)
[![GitHub stars](https://img.shields.io/github/stars/PurpleHaze2320/ai-agent-pulse?style=social)](https://github.com/PurpleHaze2320/ai-agent-pulse/stargazers)

> Automated daily tracking of the AI agent framework ecosystem's health, momentum, and trends.
> Last updated: **2026-05-01 08:20 UTC** | Tracking **19** frameworks

## How It Works

This bot runs daily via GitHub Actions and collects metrics from the GitHub API for the most important
AI agent frameworks. It computes a **Pulse Score** (0-100) based on six weighted signals: star velocity,
release freshness, issue health, commit activity, community size, and fork engagement. The result is
a living dashboard that shows which frameworks are gaining momentum and which are losing steam.

## 🏆 Pulse Leaderboard

| Rank | Framework | Pulse | Stars | ⭐ 7d | Commits (4w) | Last Release | Category |
|------|-----------|-------|-------|-------|--------------|--------------|----------|
| 1 | [Mastra](https://github.com/mastra-ai/mastra) | 🟢 **75.7** | 23.5k | 🚀 +181 | 894 | today | `typescript` |
| 2 | [CrewAI](https://github.com/crewAIInc/crewAI) | 🟢 **70.8** | 50.4k | 🚀 +642 | 0 | today | `multi-agent` |
| 3 | [OpenAI Agents SDK](https://github.com/openai/openai-agents-python) | 🟢 **70.8** | 25.7k | 🚀 +739 | 0 | today | `orchestration` |
| 4 | [LangGraph](https://github.com/langchain-ai/langgraph) | 🟡 **69.1** | 31.0k | 🚀 +737 | 0 | today | `orchestration` |
| 5 | [AG2](https://github.com/ag2ai/ag2) | 🟡 **68.6** | 4.5k | 📈 +27 | 164 | today | `multi-agent` |
| 6 | [BrowserUse](https://github.com/browser-use/browser-use) | 🟡 **68.4** | 91.5k | 🚀 +1604 | 0 | 29 days ago | `web-agent` |
| 7 | [Claude Agent SDK](https://github.com/anthropics/claude-code) | 🟡 **64.7** | 119.6k | 🚀 +2114 | 0 | today | `orchestration` |
| 8 | [LlamaIndex](https://github.com/run-llama/llama_index) | 🟡 **59.5** | 49.1k | 🚀 +196 | 0 | 10 days ago | `data-agent` |
| 9 | [Agno](https://github.com/agno-agi/agno) | 🟡 **55.5** | 39.8k | 🚀 +191 | 0 | 2 days ago | `multi-agent` |
| 10 | [PydanticAI](https://github.com/pydantic/pydantic-ai) | 🟡 **54.8** | 16.8k | 🚀 +175 | 0 | today | `structured` |
| 11 | [Google ADK](https://github.com/google/adk-python) | 🟡 **52.3** | 19.4k | 🚀 +148 | 0 | today | `orchestration` |
| 12 | [Semantic Kernel](https://github.com/microsoft/semantic-kernel) | 🟡 **51.6** | 27.8k | 📈 +55 | 0 | 1 day ago | `enterprise` |
| 13 | [DSPy](https://github.com/stanfordnlp/dspy) | 🟡 **51.0** | 34.1k | 🚀 +156 | 0 | 9 days ago | `optimization` |
| 14 | [Haystack](https://github.com/deepset-ai/haystack) | 🟡 **49.1** | 25.0k | 📈 +71 | 0 | 10 days ago | `pipeline` |
| 15 | [Letta](https://github.com/letta-ai/letta) | 🟡 **46.3** | 22.4k | 🚀 +137 | 0 | 1 mo ago | `memory` |
| 16 | [AutoGen](https://github.com/microsoft/autogen) | 🟡 **45.5** | 57.6k | 🚀 +240 | 0 | 7 mo ago | `multi-agent` |
| 17 | [Composio](https://github.com/ComposioHQ/composio) | 🟡 **44.9** | 28.0k | 📈 +82 | 0 | today | `tooling` |
| 18 | [Smolagents](https://github.com/huggingface/smolagents) | 🟠 **38.7** | 27.0k | 🚀 +161 | 0 | 3 mo ago | `lightweight` |
| 19 | [Swarm](https://github.com/openai/swarm) | 🔴 **10.0** | 21.4k | 📈 +45 | 0 | — | `experimental` |

## 📂 By Category

- `data-agent`: **LlamaIndex** (59.5)
- `enterprise`: **Semantic Kernel** (51.6)
- `experimental`: **Swarm** (10.0)
- `lightweight`: **Smolagents** (38.7)
- `memory`: **Letta** (46.3)
- `multi-agent`: **CrewAI** (70.8), **AG2** (68.6), **Agno** (55.5), **AutoGen** (45.5)
- `optimization`: **DSPy** (51.0)
- `orchestration`: **OpenAI Agents SDK** (70.8), **LangGraph** (69.1), **Claude Agent SDK** (64.7), **Google ADK** (52.3)
- `pipeline`: **Haystack** (49.1)
- `structured`: **PydanticAI** (54.8)
- `tooling`: **Composio** (44.9)
- `typescript`: **Mastra** (75.7)
- `web-agent`: **BrowserUse** (68.4)

## 🔍 Top 5 — Score Breakdown

| Framework | Star Velocity | Release Freshness | Issue Health | Commit Activity | Community | Fork Ratio |
|-----------|:---:|:---:|:---:|:---:|:---:|:---:|
| **Mastra** | 38.6 | 100.0 | 94.9 | 100 | 83.8 | 33.9 |
| **CrewAI** | 100 | 100.0 | 96.8 | 0.0 | 58.0 | 55.1 |
| **OpenAI Agents SDK** | 100 | 100.0 | 96.4 | 0.0 | 52.2 | 61.0 |
| **LangGraph** | 100 | 100.0 | 78.8 | 0.0 | 55.0 | 68.3 |
| **AG2** | 5.6 | 100.0 | 88.0 | 100 | 86.4 | 53.7 |

## 💡 Key Insights

- **Hottest framework**: Mastra with a Pulse Score of 75.7
- **Fastest growing**: Claude Agent SDK gained +2114 stars this week
- **Most active development**: Mastra with 894 commits in the last 4 weeks
- **Stale releases**: Swarm haven't released in a while

## 📦 Recent Releases

- **Mastra** [`@mastra/core@1.30.0`](https://github.com/mastra-ai/mastra/releases/tag/@mastra/core@1.30.0) — today
- **OpenAI Agents SDK** [`v0.15.0`](https://github.com/openai/openai-agents-python/releases/tag/v0.15.0) — today
- **PydanticAI** [`v1.89.0`](https://github.com/pydantic/pydantic-ai/releases/tag/v1.89.0) — today
- **Claude Agent SDK** [`v2.1.126`](https://github.com/anthropics/claude-code/releases/tag/v2.1.126) — today
- **Google ADK** [`v1.32.0`](https://github.com/google/adk-python/releases/tag/v1.32.0) — today
- **AG2** [`v0.12.2`](https://github.com/ag2ai/ag2/releases/tag/v0.12.2) — today
- **LangGraph** [`1.2.0a2`](https://github.com/langchain-ai/langgraph/releases/tag/1.2.0a2) — today
- **CrewAI** [`1.14.4`](https://github.com/crewAIInc/crewAI/releases/tag/1.14.4) — today
- **Composio** [`@composio/core@0.8.1`](https://github.com/ComposioHQ/composio/releases/tag/@composio/core@0.8.1) — today
- **Semantic Kernel** [`dotnet-1.75.0`](https://github.com/microsoft/semantic-kernel/releases/tag/dotnet-1.75.0) — 1 day ago

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

*Powered by GitHub Actions • Data refreshed daily • Last run: 2026-05-01 08:20 UTC*