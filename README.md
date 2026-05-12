# 🔬 AI Agent Framework Pulse Tracker

[![Daily Update](https://github.com/PurpleHaze2320/ai-agent-pulse/actions/workflows/track.yml/badge.svg)](https://github.com/PurpleHaze2320/ai-agent-pulse/actions/workflows/track.yml)
[![Frameworks Tracked](https://img.shields.io/badge/frameworks-19-blue)](https://github.com/PurpleHaze2320/ai-agent-pulse)
[![License: MIT](https://img.shields.io/badge/License-MIT-green.svg)](https://opensource.org/licenses/MIT)
[![GitHub stars](https://img.shields.io/github/stars/PurpleHaze2320/ai-agent-pulse?style=social)](https://github.com/PurpleHaze2320/ai-agent-pulse/stargazers)

> Automated daily tracking of the AI agent framework ecosystem's health, momentum, and trends.
> Last updated: **2026-05-12 08:48 UTC** | Tracking **19** frameworks

## How It Works

This bot runs daily via GitHub Actions and collects metrics from the GitHub API for the most important
AI agent frameworks. It computes a **Pulse Score** (0-100) based on six weighted signals: star velocity,
release freshness, issue health, commit activity, community size, and fork engagement. The result is
a living dashboard that shows which frameworks are gaining momentum and which are losing steam.

## 🏆 Pulse Leaderboard

| Rank | Framework | Pulse | Stars | ⭐ 7d | Commits (4w) | Last Release | Category |
|------|-----------|-------|-------|-------|--------------|--------------|----------|
| 1 | [Mastra](https://github.com/mastra-ai/mastra) | 🟢 **77.0** | 23.8k | 🚀 +218 | 888 | 5 days ago | `typescript` |
| 2 | [CrewAI](https://github.com/crewAIInc/crewAI) | 🟢 **71.1** | 51.2k | 🚀 +581 | 0 | 3 days ago | `multi-agent` |
| 3 | [OpenAI Agents SDK](https://github.com/openai/openai-agents-python) | 🟢 **70.9** | 26.2k | 🚀 +338 | 0 | today | `orchestration` |
| 4 | [LangGraph](https://github.com/langchain-ai/langgraph) | 🟡 **68.9** | 31.8k | 🚀 +622 | 0 | today | `orchestration` |
| 5 | [BrowserUse](https://github.com/browser-use/browser-use) | 🟡 **67.6** | 93.5k | 🚀 +1345 | 0 | 1 mo ago | `web-agent` |
| 6 | [Claude Agent SDK](https://github.com/anthropics/claude-code) | 🟡 **64.8** | 122.7k | 🚀 +2282 | 0 | today | `orchestration` |
| 7 | [LlamaIndex](https://github.com/run-llama/llama_index) | 🟡 **59.8** | 49.4k | 🚀 +226 | 0 | 21 days ago | `data-agent` |
| 8 | [PydanticAI](https://github.com/pydantic/pydantic-ai) | 🟡 **54.8** | 17.0k | 🚀 +172 | 0 | today | `structured` |
| 9 | [Agno](https://github.com/agno-agi/agno) | 🟡 **54.4** | 40.1k | 🚀 +170 | 0 | 5 days ago | `multi-agent` |
| 10 | [Google ADK](https://github.com/google/adk-python) | 🟡 **52.4** | 19.6k | 🚀 +154 | 0 | 3 days ago | `orchestration` |
| 11 | [Semantic Kernel](https://github.com/microsoft/semantic-kernel) | 🟡 **51.7** | 27.9k | 📈 +58 | 0 | today | `enterprise` |
| 12 | [DSPy](https://github.com/stanfordnlp/dspy) | 🟡 **51.2** | 34.3k | 🚀 +152 | 0 | 6 days ago | `optimization` |
| 13 | [Haystack](https://github.com/deepset-ai/haystack) | 🟡 **50.8** | 25.2k | 📈 +99 | 0 | today | `pipeline` |
| 14 | [Letta](https://github.com/letta-ai/letta) | 🟡 **48.9** | 22.7k | 🚀 +221 | 0 | 1 mo ago | `memory` |
| 15 | [AG2](https://github.com/ag2ai/ag2) | 🟡 **48.4** | 4.5k | 📈 +27 | 0 | 6 days ago | `multi-agent` |
| 16 | [Composio](https://github.com/ComposioHQ/composio) | 🟡 **47.6** | 28.2k | 🚀 +116 | 0 | today | `tooling` |
| 17 | [AutoGen](https://github.com/microsoft/autogen) | 🟡 **44.6** | 58.0k | 🚀 +244 | 0 | 7 mo ago | `multi-agent` |
| 18 | [Smolagents](https://github.com/huggingface/smolagents) | 🟠 **38.3** | 27.2k | 🚀 +162 | 0 | 3 mo ago | `lightweight` |
| 19 | [Swarm](https://github.com/openai/swarm) | 🔴 **10.1** | 21.5k | 📈 +54 | 0 | — | `experimental` |

## 📂 By Category

- `data-agent`: **LlamaIndex** (59.8)
- `enterprise`: **Semantic Kernel** (51.7)
- `experimental`: **Swarm** (10.1)
- `lightweight`: **Smolagents** (38.3)
- `memory`: **Letta** (48.9)
- `multi-agent`: **CrewAI** (71.1), **Agno** (54.4), **AG2** (48.4), **AutoGen** (44.6)
- `optimization`: **DSPy** (51.2)
- `orchestration`: **OpenAI Agents SDK** (70.9), **LangGraph** (68.9), **Claude Agent SDK** (64.8), **Google ADK** (52.4)
- `pipeline`: **Haystack** (50.8)
- `structured`: **PydanticAI** (54.8)
- `tooling`: **Composio** (47.6)
- `typescript`: **Mastra** (77.0)
- `web-agent`: **BrowserUse** (67.6)

## 🔍 Top 5 — Score Breakdown

| Framework | Star Velocity | Release Freshness | Issue Health | Commit Activity | Community | Fork Ratio |
|-----------|:---:|:---:|:---:|:---:|:---:|:---:|
| **Mastra** | 43.8 | 98.3 | 94.7 | 100 | 86.6 | 34.6 |
| **CrewAI** | 100 | 99.0 | 98.8 | 0.0 | 59.2 | 55.3 |
| **OpenAI Agents SDK** | 100 | 100.0 | 96.4 | 0.0 | 53.6 | 61.3 |
| **LangGraph** | 100 | 100.0 | 77.9 | 0.0 | 54.6 | 67.9 |
| **BrowserUse** | 100 | 86.7 | 96.4 | 0.0 | 63.0 | 45.3 |

## 💡 Key Insights

- **Hottest framework**: Mastra with a Pulse Score of 77.0
- **Fastest growing**: Claude Agent SDK gained +2282 stars this week
- **Most active development**: Mastra with 888 commits in the last 4 weeks
- **Stale releases**: Swarm haven't released in a while

## 📦 Recent Releases

- **PydanticAI** [`v1.94.0`](https://github.com/pydantic/pydantic-ai/releases/tag/v1.94.0) — today
- **LangGraph** [`1.2.0`](https://github.com/langchain-ai/langgraph/releases/tag/1.2.0) — today
- **OpenAI Agents SDK** [`v0.17.2`](https://github.com/openai/openai-agents-python/releases/tag/v0.17.2) — today
- **Composio** [`@composio/vercel@0.9.1`](https://github.com/ComposioHQ/composio/releases/tag/@composio/vercel@0.9.1) — today
- **Claude Agent SDK** [`v2.1.139`](https://github.com/anthropics/claude-code/releases/tag/v2.1.139) — today
- **Haystack** [`v2.29.0-rc1`](https://github.com/deepset-ai/haystack/releases/tag/v2.29.0-rc1) — today *(pre-release)*
- **Semantic Kernel** [`dotnet-1.76.0`](https://github.com/microsoft/semantic-kernel/releases/tag/dotnet-1.76.0) — today
- **Google ADK** [`v1.33.0`](https://github.com/google/adk-python/releases/tag/v1.33.0) — 3 days ago
- **CrewAI** [`1.14.5a4`](https://github.com/crewAIInc/crewAI/releases/tag/1.14.5a4) — 3 days ago *(pre-release)*
- **Agno** [`v2.6.5`](https://github.com/agno-agi/agno/releases/tag/v2.6.5) — 5 days ago

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

*Powered by GitHub Actions • Data refreshed daily • Last run: 2026-05-12 08:48 UTC*