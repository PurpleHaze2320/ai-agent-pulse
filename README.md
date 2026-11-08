# 🔬 AI Agent Framework Pulse Tracker

[![Daily Update](https://github.com/PurpleHaze2320/ai-agent-pulse/actions/workflows/track.yml/badge.svg)](https://github.com/PurpleHaze2320/ai-agent-pulse/actions/workflows/track.yml)
[![Frameworks Tracked](https://img.shields.io/badge/frameworks-19-blue)](https://github.com/PurpleHaze2320/ai-agent-pulse)
[![License: MIT](https://img.shields.io/badge/License-MIT-green.svg)](https://opensource.org/licenses/MIT)
[![GitHub stars](https://img.shields.io/github/stars/PurpleHaze2320/ai-agent-pulse?style=social)](https://github.com/PurpleHaze2320/ai-agent-pulse/stargazers)

> Automated daily tracking of the AI agent framework ecosystem's health, momentum, and trends.
> Last updated: **2026-11-08 13:01 UTC** | Tracking **19** frameworks

## How It Works

This bot runs daily via GitHub Actions and collects metrics from the GitHub API for the most important
AI agent frameworks. It computes a **Pulse Score** (0-100) based on six weighted signals: star velocity,
release freshness, issue health, commit activity, community size, and fork engagement. The result is
a living dashboard that shows which frameworks are gaining momentum and which are losing steam.

## 🏆 Pulse Leaderboard

| Rank | Framework | Pulse | Stars | ⭐ 7d | Commits (4w) | Last Release | Category |
|------|-----------|-------|-------|-------|--------------|--------------|----------|
| 1 | [LangGraph](https://github.com/langchain-ai/langgraph) | 🟢 **84.4** | 44.6k | 🚀 +383 | 100 | 2 days ago | `orchestration` |
| 2 | [CrewAI](https://github.com/crewAIInc/crewAI) | 🟢 **79.3** | 60.6k | 🚀 +266 | 177 | 1 day ago | `multi-agent` |
| 3 | [Mastra](https://github.com/mastra-ai/mastra) | 🟢 **75.6** | 29.4k | 🚀 +157 | 1812 | 4 days ago | `typescript` |
| 4 | [Google ADK](https://github.com/google/adk-python) | 🟢 **74.4** | 22.1k | 📈 +73 | 354 | 1 day ago | `orchestration` |
| 5 | [Claude Agent SDK](https://github.com/anthropics/claude-code) | 🟢 **72.0** | 154.9k | 🚀 +820 | 33 | 1 day ago | `orchestration` |
| 6 | [BrowserUse](https://github.com/browser-use/browser-use) | 🟢 **71.7** | 120.3k | 🚀 +582 | 12 | 12 days ago | `web-agent` |
| 7 | [Haystack](https://github.com/deepset-ai/haystack) | 🟢 **70.9** | 26.9k | 📈 +45 | 182 | 5 days ago | `pipeline` |
| 8 | [PydanticAI](https://github.com/pydantic/pydantic-ai) | 🟢 **70.2** | 21.1k | 🚀 +108 | 1037 | 1 mo ago | `structured` |
| 9 | [AG2](https://github.com/ag2ai/ag2) | 🟢 **70.0** | 5.1k | ↗️ +15 | 104 | 4 days ago | `multi-agent` |
| 10 | [Agno](https://github.com/agno-agi/agno) | 🟡 **69.9** | 43.1k | 🚀 +102 | 122 | 9 days ago | `multi-agent` |
| 11 | [Semantic Kernel](https://github.com/microsoft/semantic-kernel) | 🟡 **68.7** | 28.7k | 📈 +22 | 86 | 1 day ago | `enterprise` |
| 12 | [Composio](https://github.com/ComposioHQ/composio) | 🟡 **68.3** | 31.0k | 🚀 +117 | 249 | 2 days ago | `tooling` |
| 13 | [OpenAI Agents SDK](https://github.com/openai/openai-agents-python) | 🟡 **66.9** | 30.6k | 🚀 +124 | 55 | today | `orchestration` |
| 14 | [DSPy](https://github.com/stanfordnlp/dspy) | 🟡 **59.3** | 39.0k | 📈 +97 | 61 | 26 days ago | `optimization` |
| 15 | [LlamaIndex](https://github.com/run-llama/llama_index) | 🟡 **51.4** | 52.8k | 📈 +76 | 1 | 1 mo ago | `data-agent` |
| 16 | [Letta](https://github.com/letta-ai/letta) | 🟠 **34.0** | 25.4k | 📈 +71 | 1 | 5 mo ago | `memory` |
| 17 | [AutoGen](https://github.com/microsoft/autogen) | 🟠 **32.0** | 61.7k | 📈 +86 | 1 | 1y ago | `multi-agent` |
| 18 | [Smolagents](https://github.com/huggingface/smolagents) | 🟠 **31.4** | 30.3k | 📈 +100 | 0 | 5 mo ago | `lightweight` |
| 19 | [Swarm](https://github.com/openai/swarm) | 🔴 **9.4** | 22.1k | 📈 +22 | 0 | — | `experimental` |

## 📂 By Category

- `data-agent`: **LlamaIndex** (51.4)
- `enterprise`: **Semantic Kernel** (68.7)
- `experimental`: **Swarm** (9.4)
- `lightweight`: **Smolagents** (31.4)
- `memory`: **Letta** (34.0)
- `multi-agent`: **CrewAI** (79.3), **AG2** (70.0), **Agno** (69.9), **AutoGen** (32.0)
- `optimization`: **DSPy** (59.3)
- `orchestration`: **LangGraph** (84.4), **Google ADK** (74.4), **Claude Agent SDK** (72.0), **OpenAI Agents SDK** (66.9)
- `pipeline`: **Haystack** (70.9)
- `structured`: **PydanticAI** (70.2)
- `tooling`: **Composio** (68.3)
- `typescript`: **Mastra** (75.6)
- `web-agent`: **BrowserUse** (71.7)

## 🔍 Top 5 — Score Breakdown

| Framework | Star Velocity | Release Freshness | Issue Health | Commit Activity | Community | Fork Ratio |
|-----------|:---:|:---:|:---:|:---:|:---:|:---:|
| **LangGraph** | 79.1 | 99.3 | 80.8 | 100 | 57.4 | 68.9 |
| **CrewAI** | 54.4 | 99.7 | 83.0 | 100 | 72.6 | 60.0 |
| **Mastra** | 33.1 | 98.7 | 93.8 | 100 | 93.2 | 42.0 |
| **Google ADK** | 15.9 | 99.7 | 94.3 | 100 | 85.8 | 78.0 |
| **Claude Agent SDK** | 100 | 99.7 | 84.6 | 33.0 | 11.2 | 66.1 |

## 💡 Key Insights

- **Hottest framework**: LangGraph with a Pulse Score of 84.4
- **Fastest growing**: Claude Agent SDK gained +820 stars this week
- **Most active development**: Mastra with 1812 commits in the last 4 weeks
- **Stale releases**: AutoGen, Swarm haven't released in a while

## 📦 Recent Releases

- **OpenAI Agents SDK** [`v0.24.0-alpha.7`](https://github.com/openai/openai-agents-python/releases/tag/v0.24.0-alpha.7) — today *(pre-release)*
- **CrewAI** [`1.15.37`](https://github.com/crewAIInc/crewAI/releases/tag/1.15.37) — 1 day ago
- **Semantic Kernel** [`dotnet-1.82.0`](https://github.com/microsoft/semantic-kernel/releases/tag/dotnet-1.82.0) — 1 day ago
- **Google ADK** [`v2.14.0`](https://github.com/google/adk-python/releases/tag/v2.14.0) — 1 day ago
- **Claude Agent SDK** [`v2.1.319`](https://github.com/anthropics/claude-code/releases/tag/v2.1.319) — 1 day ago
- **Composio** [`@composio/cli@0.6.1-beta.535`](https://github.com/ComposioHQ/composio/releases/tag/@composio/cli@0.6.1-beta.535) — 2 days ago *(pre-release)*
- **LangGraph** [`sdk==0.4.14`](https://github.com/langchain-ai/langgraph/releases/tag/sdk==0.4.14) — 2 days ago
- **Mastra** [`@mastra/core@1.82.0`](https://github.com/mastra-ai/mastra/releases/tag/@mastra/core@1.82.0) — 4 days ago
- **AG2** [`v1.3.0`](https://github.com/ag2ai/ag2/releases/tag/v1.3.0) — 4 days ago
- **Haystack** [`v2.31.1`](https://github.com/deepset-ai/haystack/releases/tag/v2.31.1) — 5 days ago

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

*Powered by GitHub Actions • Data refreshed daily • Last run: 2026-11-08 13:01 UTC*