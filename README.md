# 🔬 AI Agent Framework Pulse Tracker

[![Daily Update](https://github.com/PurpleHaze2320/ai-agent-pulse/actions/workflows/track.yml/badge.svg)](https://github.com/PurpleHaze2320/ai-agent-pulse/actions/workflows/track.yml)
[![Frameworks Tracked](https://img.shields.io/badge/frameworks-19-blue)](https://github.com/PurpleHaze2320/ai-agent-pulse)
[![License: MIT](https://img.shields.io/badge/License-MIT-green.svg)](https://opensource.org/licenses/MIT)
[![GitHub stars](https://img.shields.io/github/stars/PurpleHaze2320/ai-agent-pulse?style=social)](https://github.com/PurpleHaze2320/ai-agent-pulse/stargazers)

> Automated daily tracking of the AI agent framework ecosystem's health, momentum, and trends.
> Last updated: **2026-06-26 09:37 UTC** | Tracking **19** frameworks

## How It Works

This bot runs daily via GitHub Actions and collects metrics from the GitHub API for the most important
AI agent frameworks. It computes a **Pulse Score** (0-100) based on six weighted signals: star velocity,
release freshness, issue health, commit activity, community size, and fork engagement. The result is
a living dashboard that shows which frameworks are gaining momentum and which are losing steam.

## 🏆 Pulse Leaderboard

| Rank | Framework | Pulse | Stars | ⭐ 7d | Commits (4w) | Last Release | Category |
|------|-----------|-------|-------|-------|--------------|--------------|----------|
| 1 | [CrewAI](https://github.com/crewAIInc/crewAI) | 🟢 **89.7** | 54.4k | 🚀 +449 | 130 | today | `multi-agent` |
| 2 | [BrowserUse](https://github.com/browser-use/browser-use) | 🟢 **89.2** | 100.8k | 🚀 +1229 | 412 | 13 days ago | `web-agent` |
| 3 | [LangGraph](https://github.com/langchain-ai/langgraph) | 🟢 **80.7** | 35.8k | 🚀 +610 | 64 | 7 days ago | `orchestration` |
| 4 | [Mastra](https://github.com/mastra-ai/mastra) | 🟢 **79.3** | 25.5k | 🚀 +233 | 984 | 1 day ago | `typescript` |
| 5 | [PydanticAI](https://github.com/pydantic/pydantic-ai) | 🟢 **74.1** | 18.0k | 🚀 +157 | 96 | 2 days ago | `structured` |
| 6 | [Google ADK](https://github.com/google/adk-python) | 🟢 **72.1** | 20.3k | 🚀 +123 | 309 | 7 days ago | `orchestration` |
| 7 | [Claude Agent SDK](https://github.com/anthropics/claude-code) | 🟢 **71.9** | 134.5k | 🚀 +1212 | 31 | today | `orchestration` |
| 8 | [OpenAI Agents SDK](https://github.com/openai/openai-agents-python) | 🟡 **66.1** | 27.4k | 🚀 +185 | 52 | 2 days ago | `orchestration` |
| 9 | [LlamaIndex](https://github.com/run-llama/llama_index) | 🟡 **61.6** | 50.4k | 🚀 +191 | 11 | 1 day ago | `data-agent` |
| 10 | [DSPy](https://github.com/stanfordnlp/dspy) | 🟡 **57.2** | 35.4k | 🚀 +260 | 18 | 29 days ago | `optimization` |
| 11 | [Semantic Kernel](https://github.com/microsoft/semantic-kernel) | 🟡 **57.0** | 28.2k | 📈 +37 | 32 | 9 days ago | `enterprise` |
| 12 | [Haystack](https://github.com/deepset-ai/haystack) | 🟡 **51.8** | 25.7k | 🚀 +123 | 0 | 8 days ago | `pipeline` |
| 13 | [Agno](https://github.com/agno-agi/agno) | 🟡 **51.3** | 40.9k | 📈 +90 | 0 | 2 days ago | `multi-agent` |
| 14 | [AG2](https://github.com/ag2ai/ag2) | 🟡 **48.6** | 4.7k | ↗️ +20 | 0 | today | `multi-agent` |
| 15 | [Composio](https://github.com/ComposioHQ/composio) | 🟡 **48.0** | 29.0k | 🚀 +119 | 0 | today | `tooling` |
| 16 | [Letta](https://github.com/letta-ai/letta) | 🟡 **44.9** | 23.5k | 🚀 +118 | 0 | 1 mo ago | `memory` |
| 17 | [Smolagents](https://github.com/huggingface/smolagents) | 🟡 **41.6** | 28.0k | 📈 +94 | 2 | 28 days ago | `lightweight` |
| 18 | [AutoGen](https://github.com/microsoft/autogen) | 🟠 **39.4** | 59.3k | 🚀 +200 | 0 | 8 mo ago | `multi-agent` |
| 19 | [Swarm](https://github.com/openai/swarm) | 🔴 **10.8** | 21.7k | 📈 +80 | 0 | — | `experimental` |

## 📂 By Category

- `data-agent`: **LlamaIndex** (61.6)
- `enterprise`: **Semantic Kernel** (57.0)
- `experimental`: **Swarm** (10.8)
- `lightweight`: **Smolagents** (41.6)
- `memory`: **Letta** (44.9)
- `multi-agent`: **CrewAI** (89.7), **Agno** (51.3), **AG2** (48.6), **AutoGen** (39.4)
- `optimization`: **DSPy** (57.2)
- `orchestration`: **LangGraph** (80.7), **Google ADK** (72.1), **Claude Agent SDK** (71.9), **OpenAI Agents SDK** (66.1)
- `pipeline`: **Haystack** (51.8)
- `structured`: **PydanticAI** (74.1)
- `tooling`: **Composio** (48.0)
- `typescript`: **Mastra** (79.3)
- `web-agent`: **BrowserUse** (89.2)

## 🔍 Top 5 — Score Breakdown

| Framework | Star Velocity | Release Freshness | Issue Health | Commit Activity | Community | Fork Ratio |
|-----------|:---:|:---:|:---:|:---:|:---:|:---:|
| **CrewAI** | 94.8 | 100.0 | 96.2 | 100 | 59.4 | 56.0 |
| **BrowserUse** | 100 | 95.7 | 95.4 | 100 | 63.0 | 44.5 |
| **LangGraph** | 100 | 97.7 | 74.3 | 64.0 | 55.0 | 66.9 |
| **Mastra** | 49.1 | 99.7 | 95.4 | 100 | 92.0 | 36.0 |
| **PydanticAI** | 32.1 | 99.3 | 82.7 | 96.0 | 95.4 | 50.1 |

## 💡 Key Insights

- **Hottest framework**: CrewAI with a Pulse Score of 89.7
- **Fastest growing**: BrowserUse gained +1229 stars this week
- **Most active development**: Mastra with 984 commits in the last 4 weeks
- **Stale releases**: Swarm haven't released in a while

## 📦 Recent Releases

- **AG2** [`v0.14.0`](https://github.com/ag2ai/ag2/releases/tag/v0.14.0) — today
- **Composio** [`@composio/core@0.13.0`](https://github.com/ComposioHQ/composio/releases/tag/@composio/core@0.13.0) — today
- **CrewAI** [`1.15.0`](https://github.com/crewAIInc/crewAI/releases/tag/1.15.0) — today
- **Claude Agent SDK** [`v2.1.193`](https://github.com/anthropics/claude-code/releases/tag/v2.1.193) — today
- **LlamaIndex** [`v0.14.23`](https://github.com/run-llama/llama_index/releases/tag/v0.14.23) — 1 day ago
- **Mastra** [`@mastra/core@1.46.0`](https://github.com/mastra-ai/mastra/releases/tag/@mastra/core@1.46.0) — 1 day ago
- **OpenAI Agents SDK** [`v0.17.7`](https://github.com/openai/openai-agents-python/releases/tag/v0.17.7) — 2 days ago
- **PydanticAI** [`v2.0.0`](https://github.com/pydantic/pydantic-ai/releases/tag/v2.0.0) — 2 days ago
- **Agno** [`v2.6.19`](https://github.com/agno-agi/agno/releases/tag/v2.6.19) — 2 days ago
- **LangGraph** [`1.2.6`](https://github.com/langchain-ai/langgraph/releases/tag/1.2.6) — 7 days ago

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

*Powered by GitHub Actions • Data refreshed daily • Last run: 2026-06-26 09:37 UTC*