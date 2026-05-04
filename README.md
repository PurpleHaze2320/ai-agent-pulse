# 🔬 AI Agent Framework Pulse Tracker

[![Daily Update](https://github.com/PurpleHaze2320/ai-agent-pulse/actions/workflows/track.yml/badge.svg)](https://github.com/PurpleHaze2320/ai-agent-pulse/actions/workflows/track.yml)
[![Frameworks Tracked](https://img.shields.io/badge/frameworks-19-blue)](https://github.com/PurpleHaze2320/ai-agent-pulse)
[![License: MIT](https://img.shields.io/badge/License-MIT-green.svg)](https://opensource.org/licenses/MIT)
[![GitHub stars](https://img.shields.io/github/stars/PurpleHaze2320/ai-agent-pulse?style=social)](https://github.com/PurpleHaze2320/ai-agent-pulse/stargazers)

> Automated daily tracking of the AI agent framework ecosystem's health, momentum, and trends.
> Last updated: **2026-05-04 08:37 UTC** | Tracking **19** frameworks

## How It Works

This bot runs daily via GitHub Actions and collects metrics from the GitHub API for the most important
AI agent frameworks. It computes a **Pulse Score** (0-100) based on six weighted signals: star velocity,
release freshness, issue health, commit activity, community size, and fork engagement. The result is
a living dashboard that shows which frameworks are gaining momentum and which are losing steam.

## 🏆 Pulse Leaderboard

| Rank | Framework | Pulse | Stars | ⭐ 7d | Commits (4w) | Last Release | Category |
|------|-----------|-------|-------|-------|--------------|--------------|----------|
| 1 | [OpenAI Agents SDK](https://github.com/openai/openai-agents-python) | 🟢 **90.6** | 25.8k | 🚀 +470 | 102 | 2 days ago | `orchestration` |
| 2 | [Mastra](https://github.com/mastra-ai/mastra) | 🟢 **75.8** | 23.5k | 🚀 +192 | 756 | 3 days ago | `typescript` |
| 3 | [CrewAI](https://github.com/crewAIInc/crewAI) | 🟢 **71.0** | 50.6k | 🚀 +526 | 0 | 2 days ago | `multi-agent` |
| 4 | [LangGraph](https://github.com/langchain-ai/langgraph) | 🟡 **68.9** | 31.1k | 🚀 +621 | 0 | 2 days ago | `orchestration` |
| 5 | [BrowserUse](https://github.com/browser-use/browser-use) | 🟡 **68.2** | 92.0k | 🚀 +1368 | 0 | 1 mo ago | `web-agent` |
| 6 | [Claude Agent SDK](https://github.com/anthropics/claude-code) | 🟡 **64.5** | 120.2k | 🚀 +1901 | 0 | 3 days ago | `orchestration` |
| 7 | [LlamaIndex](https://github.com/run-llama/llama_index) | 🟡 **57.9** | 49.1k | 🚀 +159 | 0 | 13 days ago | `data-agent` |
| 8 | [Agno](https://github.com/agno-agi/agno) | 🟡 **55.4** | 39.9k | 🚀 +196 | 0 | 5 days ago | `multi-agent` |
| 9 | [PydanticAI](https://github.com/pydantic/pydantic-ai) | 🟡 **53.9** | 16.8k | 🚀 +154 | 0 | 2 days ago | `structured` |
| 10 | [Google ADK](https://github.com/google/adk-python) | 🟡 **51.1** | 19.4k | 🚀 +117 | 0 | 3 days ago | `orchestration` |
| 11 | [DSPy](https://github.com/stanfordnlp/dspy) | 🟡 **51.0** | 34.2k | 🚀 +164 | 0 | 12 days ago | `optimization` |
| 12 | [Semantic Kernel](https://github.com/microsoft/semantic-kernel) | 🟡 **50.9** | 27.8k | 📈 +43 | 0 | 4 days ago | `enterprise` |
| 13 | [Haystack](https://github.com/deepset-ai/haystack) | 🟡 **48.9** | 25.1k | 📈 +71 | 0 | 13 days ago | `pipeline` |
| 14 | [AG2](https://github.com/ag2ai/ag2) | 🟡 **48.9** | 4.5k | 📈 +38 | 0 | 3 days ago | `multi-agent` |
| 15 | [Composio](https://github.com/ComposioHQ/composio) | 🟡 **45.9** | 28.0k | 🚀 +110 | 0 | 2 days ago | `tooling` |
| 16 | [Letta](https://github.com/letta-ai/letta) | 🟡 **44.9** | 22.4k | 🚀 +102 | 0 | 1 mo ago | `memory` |
| 17 | [AutoGen](https://github.com/microsoft/autogen) | 🟡 **44.1** | 57.7k | 🚀 +210 | 0 | 7 mo ago | `multi-agent` |
| 18 | [Smolagents](https://github.com/huggingface/smolagents) | 🟠 **38.3** | 27.1k | 🚀 +152 | 0 | 3 mo ago | `lightweight` |
| 19 | [Swarm](https://github.com/openai/swarm) | 🔴 **9.5** | 21.4k | 📈 +31 | 0 | — | `experimental` |

## 📂 By Category

- `data-agent`: **LlamaIndex** (57.9)
- `enterprise`: **Semantic Kernel** (50.9)
- `experimental`: **Swarm** (9.5)
- `lightweight`: **Smolagents** (38.3)
- `memory`: **Letta** (44.9)
- `multi-agent`: **CrewAI** (71.0), **Agno** (55.4), **AG2** (48.9), **AutoGen** (44.1)
- `optimization`: **DSPy** (51.0)
- `orchestration`: **OpenAI Agents SDK** (90.6), **LangGraph** (68.9), **Claude Agent SDK** (64.5), **Google ADK** (51.1)
- `pipeline`: **Haystack** (48.9)
- `structured`: **PydanticAI** (53.9)
- `tooling`: **Composio** (45.9)
- `typescript`: **Mastra** (75.8)
- `web-agent`: **BrowserUse** (68.2)

## 🔍 Top 5 — Score Breakdown

| Framework | Star Velocity | Release Freshness | Issue Health | Commit Activity | Community | Fork Ratio |
|-----------|:---:|:---:|:---:|:---:|:---:|:---:|
| **OpenAI Agents SDK** | 100 | 99.3 | 96.0 | 100 | 52.6 | 61.0 |
| **Mastra** | 40.1 | 99.0 | 94.6 | 100 | 84.2 | 34.1 |
| **CrewAI** | 100 | 99.3 | 98.6 | 0.0 | 58.2 | 55.2 |
| **LangGraph** | 100 | 99.3 | 78.5 | 0.0 | 54.8 | 68.2 |
| **BrowserUse** | 100 | 89.3 | 96.9 | 0.0 | 62.8 | 45.5 |

## 💡 Key Insights

- **Hottest framework**: OpenAI Agents SDK with a Pulse Score of 90.6
- **Fastest growing**: Claude Agent SDK gained +1901 stars this week
- **Most active development**: Mastra with 756 commits in the last 4 weeks
- **Stale releases**: Swarm haven't released in a while

## 📦 Recent Releases

- **OpenAI Agents SDK** [`v0.15.1`](https://github.com/openai/openai-agents-python/releases/tag/v0.15.1) — 2 days ago
- **Composio** [`@composio/cli@0.2.28`](https://github.com/ComposioHQ/composio/releases/tag/@composio/cli@0.2.28) — 2 days ago
- **CrewAI** [`1.14.5a1`](https://github.com/crewAIInc/crewAI/releases/tag/1.14.5a1) — 2 days ago *(pre-release)*
- **PydanticAI** [`v1.89.1`](https://github.com/pydantic/pydantic-ai/releases/tag/v1.89.1) — 2 days ago
- **LangGraph** [`1.2.0a5`](https://github.com/langchain-ai/langgraph/releases/tag/1.2.0a5) — 2 days ago
- **Mastra** [`@mastra/core@1.30.0`](https://github.com/mastra-ai/mastra/releases/tag/@mastra/core@1.30.0) — 3 days ago
- **Claude Agent SDK** [`v2.1.126`](https://github.com/anthropics/claude-code/releases/tag/v2.1.126) — 3 days ago
- **Google ADK** [`v1.32.0`](https://github.com/google/adk-python/releases/tag/v1.32.0) — 3 days ago
- **AG2** [`v0.12.2`](https://github.com/ag2ai/ag2/releases/tag/v0.12.2) — 3 days ago
- **Semantic Kernel** [`dotnet-1.75.0`](https://github.com/microsoft/semantic-kernel/releases/tag/dotnet-1.75.0) — 4 days ago

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

*Powered by GitHub Actions • Data refreshed daily • Last run: 2026-05-04 08:37 UTC*