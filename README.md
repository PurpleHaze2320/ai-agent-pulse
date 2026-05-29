# 🔬 AI Agent Framework Pulse Tracker

[![Daily Update](https://github.com/PurpleHaze2320/ai-agent-pulse/actions/workflows/track.yml/badge.svg)](https://github.com/PurpleHaze2320/ai-agent-pulse/actions/workflows/track.yml)
[![Frameworks Tracked](https://img.shields.io/badge/frameworks-19-blue)](https://github.com/PurpleHaze2320/ai-agent-pulse)
[![License: MIT](https://img.shields.io/badge/License-MIT-green.svg)](https://opensource.org/licenses/MIT)
[![GitHub stars](https://img.shields.io/github/stars/PurpleHaze2320/ai-agent-pulse?style=social)](https://github.com/PurpleHaze2320/ai-agent-pulse/stargazers)

> Automated daily tracking of the AI agent framework ecosystem's health, momentum, and trends.
> Last updated: **2026-05-29 10:03 UTC** | Tracking **19** frameworks

## How It Works

This bot runs daily via GitHub Actions and collects metrics from the GitHub API for the most important
AI agent frameworks. It computes a **Pulse Score** (0-100) based on six weighted signals: star velocity,
release freshness, issue health, commit activity, community size, and fork engagement. The result is
a living dashboard that shows which frameworks are gaining momentum and which are losing steam.

## 🏆 Pulse Leaderboard

| Rank | Framework | Pulse | Stars | ⭐ 7d | Commits (4w) | Last Release | Category |
|------|-----------|-------|-------|-------|--------------|--------------|----------|
| 1 | [Mastra](https://github.com/mastra-ai/mastra) | 🟢 **82.0** | 24.5k | 🚀 +326 | 906 | 1 day ago | `typescript` |
| 2 | [CrewAI](https://github.com/crewAIInc/crewAI) | 🟢 **70.9** | 52.4k | 🚀 +474 | 0 | today | `multi-agent` |
| 3 | [BrowserUse](https://github.com/browser-use/browser-use) | 🟢 **70.0** | 96.1k | 🚀 +1057 | 0 | 3 days ago | `web-agent` |
| 4 | [LangGraph](https://github.com/langchain-ai/langgraph) | 🟡 **68.7** | 33.3k | 🚀 +622 | 0 | today | `orchestration` |
| 5 | [Claude Agent SDK](https://github.com/anthropics/claude-code) | 🟡 **65.5** | 127.5k | 🚀 +1888 | 0 | today | `orchestration` |
| 6 | [LlamaIndex](https://github.com/run-llama/llama_index) | 🟡 **57.8** | 49.7k | 🚀 +170 | 0 | 14 days ago | `data-agent` |
| 7 | [OpenAI Agents SDK](https://github.com/openai/openai-agents-python) | 🟡 **56.5** | 26.7k | 🚀 +173 | 0 | 3 days ago | `orchestration` |
| 8 | [PydanticAI](https://github.com/pydantic/pydantic-ai) | 🟡 **54.8** | 17.4k | 🚀 +166 | 0 | today | `structured` |
| 9 | [Agno](https://github.com/agno-agi/agno) | 🟡 **52.8** | 40.4k | 🚀 +123 | 0 | 7 days ago | `multi-agent` |
| 10 | [Semantic Kernel](https://github.com/microsoft/semantic-kernel) | 🟡 **51.3** | 28.0k | 📈 +45 | 0 | 1 day ago | `enterprise` |
| 11 | [DSPy](https://github.com/stanfordnlp/dspy) | 🟡 **50.8** | 34.7k | 🚀 +138 | 0 | 1 day ago | `optimization` |
| 12 | [Google ADK](https://github.com/google/adk-python) | 🟡 **50.5** | 19.9k | 🚀 +113 | 0 | 6 days ago | `orchestration` |
| 13 | [Haystack](https://github.com/deepset-ai/haystack) | 🟡 **49.0** | 25.4k | 📈 +72 | 0 | 16 days ago | `pipeline` |
| 14 | [AG2](https://github.com/ag2ai/ag2) | 🟡 **48.7** | 4.6k | ↗️ +17 | 0 | today | `multi-agent` |
| 15 | [Letta](https://github.com/letta-ai/letta) | 🟡 **48.6** | 23.0k | 🚀 +151 | 0 | 14 days ago | `memory` |
| 16 | [Composio](https://github.com/ComposioHQ/composio) | 🟡 **47.5** | 28.5k | 🚀 +120 | 0 | 9 days ago | `tooling` |
| 17 | [Smolagents](https://github.com/huggingface/smolagents) | 🟡 **44.9** | 27.6k | 🚀 +133 | 0 | today | `lightweight` |
| 18 | [AutoGen](https://github.com/microsoft/autogen) | 🟡 **42.9** | 58.5k | 🚀 +230 | 0 | 8 mo ago | `multi-agent` |
| 19 | [Swarm](https://github.com/openai/swarm) | 🔴 **9.1** | 21.5k | 📈 +27 | 0 | — | `experimental` |

## 📂 By Category

- `data-agent`: **LlamaIndex** (57.8)
- `enterprise`: **Semantic Kernel** (51.3)
- `experimental`: **Swarm** (9.1)
- `lightweight`: **Smolagents** (44.9)
- `memory`: **Letta** (48.6)
- `multi-agent`: **CrewAI** (70.9), **Agno** (52.8), **AG2** (48.7), **AutoGen** (42.9)
- `optimization`: **DSPy** (50.8)
- `orchestration`: **LangGraph** (68.7), **Claude Agent SDK** (65.5), **OpenAI Agents SDK** (56.5), **Google ADK** (50.5)
- `pipeline`: **Haystack** (49.0)
- `structured`: **PydanticAI** (54.8)
- `tooling`: **Composio** (47.5)
- `typescript`: **Mastra** (82.0)
- `web-agent`: **BrowserUse** (70.0)

## 🔍 Top 5 — Score Breakdown

| Framework | Star Velocity | Release Freshness | Issue Health | Commit Activity | Community | Fork Ratio |
|-----------|:---:|:---:|:---:|:---:|:---:|:---:|
| **Mastra** | 62.2 | 99.7 | 94.3 | 100 | 88.2 | 35.1 |
| **CrewAI** | 99.1 | 100.0 | 98.0 | 0.0 | 59.2 | 55.6 |
| **BrowserUse** | 100 | 99.0 | 95.8 | 0.0 | 63.0 | 44.9 |
| **LangGraph** | 100 | 100.0 | 76.4 | 0.0 | 55.0 | 67.5 |
| **Claude Agent SDK** | 100 | 100.0 | 85.9 | 0.0 | 10.2 | 65.5 |

## 💡 Key Insights

- **Hottest framework**: Mastra with a Pulse Score of 82.0
- **Fastest growing**: Claude Agent SDK gained +1888 stars this week
- **Most active development**: Mastra with 906 commits in the last 4 weeks
- **Stale releases**: Swarm haven't released in a while

## 📦 Recent Releases

- **Smolagents** [`v1.26.0`](https://github.com/huggingface/smolagents/releases/tag/v1.26.0) — today
- **PydanticAI** [`v2.0.0b4`](https://github.com/pydantic/pydantic-ai/releases/tag/v2.0.0b4) — today *(pre-release)*
- **Claude Agent SDK** [`v2.1.156`](https://github.com/anthropics/claude-code/releases/tag/v2.1.156) — today
- **AG2** [`v0.13.2`](https://github.com/ag2ai/ag2/releases/tag/v0.13.2) — today
- **CrewAI** [`1.14.6`](https://github.com/crewAIInc/crewAI/releases/tag/1.14.6) — today
- **LangGraph** [`sdk==0.4.0`](https://github.com/langchain-ai/langgraph/releases/tag/sdk==0.4.0) — today
- **Semantic Kernel** [`dotnet-1.77.0`](https://github.com/microsoft/semantic-kernel/releases/tag/dotnet-1.77.0) — 1 day ago
- **DSPy** [`3.3.0b1`](https://github.com/stanfordnlp/dspy/releases/tag/3.3.0b1) — 1 day ago *(pre-release)*
- **Mastra** [`@mastra/core@1.37.0`](https://github.com/mastra-ai/mastra/releases/tag/@mastra/core@1.37.0) — 1 day ago
- **OpenAI Agents SDK** [`v0.17.4`](https://github.com/openai/openai-agents-python/releases/tag/v0.17.4) — 3 days ago

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

*Powered by GitHub Actions • Data refreshed daily • Last run: 2026-05-29 10:03 UTC*