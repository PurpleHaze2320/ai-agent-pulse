# 🔬 AI Agent Framework Pulse Tracker

[![Daily Update](https://github.com/PurpleHaze2320/ai-agent-pulse/actions/workflows/track.yml/badge.svg)](https://github.com/PurpleHaze2320/ai-agent-pulse/actions/workflows/track.yml)
[![Frameworks Tracked](https://img.shields.io/badge/frameworks-19-blue)](https://github.com/PurpleHaze2320/ai-agent-pulse)
[![License: MIT](https://img.shields.io/badge/License-MIT-green.svg)](https://opensource.org/licenses/MIT)
[![GitHub stars](https://img.shields.io/github/stars/PurpleHaze2320/ai-agent-pulse?style=social)](https://github.com/PurpleHaze2320/ai-agent-pulse/stargazers)

> Automated daily tracking of the AI agent framework ecosystem's health, momentum, and trends.
> Last updated: **2026-04-14 07:57 UTC** | Tracking **19** frameworks

## How It Works

This bot runs daily via GitHub Actions and collects metrics from the GitHub API for the most important
AI agent frameworks. It computes a **Pulse Score** (0-100) based on six weighted signals: star velocity,
release freshness, issue health, commit activity, community size, and fork engagement. The result is
a living dashboard that shows which frameworks are gaining momentum and which are losing steam.

## 🏆 Pulse Leaderboard

| Rank | Framework | Pulse | Stars | ⭐ 7d | Commits (4w) | Last Release | Category |
|------|-----------|-------|-------|-------|--------------|--------------|----------|
| 1 | [Mastra](https://github.com/mastra-ai/mastra) | 🟢 **74.1** | 23.0k | 🚀 +229 | 633 | 5 days ago | `typescript` |
| 2 | [CrewAI](https://github.com/crewAIInc/crewAI) | 🟢 **70.5** | 48.8k | 🚀 +624 | 0 | today | `multi-agent` |
| 3 | [BrowserUse](https://github.com/browser-use/browser-use) | 🟡 **69.5** | 87.7k | 🚀 +1394 | 0 | 12 days ago | `web-agent` |
| 4 | [LangGraph](https://github.com/langchain-ai/langgraph) | 🟡 **69.1** | 29.2k | 🚀 +613 | 0 | 3 days ago | `orchestration` |
| 5 | [Claude Agent SDK](https://github.com/anthropics/claude-code) | 🟡 **64.6** | 113.7k | 🚀 +3507 | 0 | today | `orchestration` |
| 6 | [LlamaIndex](https://github.com/run-llama/llama_index) | 🟡 **58.1** | 48.6k | 🚀 +213 | 0 | 10 days ago | `data-agent` |
| 7 | [Agno](https://github.com/agno-agi/agno) | 🟡 **54.0** | 39.4k | 🚀 +194 | 0 | 3 days ago | `multi-agent` |
| 8 | [PydanticAI](https://github.com/pydantic/pydantic-ai) | 🟡 **53.4** | 16.3k | 🚀 +194 | 0 | today | `structured` |
| 9 | [Google ADK](https://github.com/google/adk-python) | 🟡 **51.4** | 19.0k | 🚀 +175 | 0 | today | `orchestration` |
| 10 | [OpenAI Agents SDK](https://github.com/openai/openai-agents-python) | 🟡 **51.3** | 20.8k | 🚀 +144 | 0 | 5 days ago | `orchestration` |
| 11 | [Semantic Kernel](https://github.com/microsoft/semantic-kernel) | 🟡 **49.5** | 27.7k | 📈 +37 | 0 | 6 days ago | `enterprise` |
| 12 | [Haystack](https://github.com/deepset-ai/haystack) | 🟡 **48.5** | 24.8k | 📈 +85 | 0 | 12 days ago | `pipeline` |
| 13 | [AG2](https://github.com/ag2ai/ag2) | 🟡 **46.8** | 4.4k | 📈 +26 | 0 | 9 days ago | `multi-agent` |
| 14 | [AutoGen](https://github.com/microsoft/autogen) | 🟡 **46.2** | 57.1k | 🚀 +288 | 0 | 6 mo ago | `multi-agent` |
| 15 | [DSPy](https://github.com/stanfordnlp/dspy) | 🟡 **46.1** | 33.7k | 🚀 +179 | 0 | 2 mo ago | `optimization` |
| 16 | [Letta](https://github.com/letta-ai/letta) | 🟡 **45.5** | 22.0k | 🚀 +126 | 0 | 13 days ago | `memory` |
| 17 | [Composio](https://github.com/ComposioHQ/composio) | 🟡 **45.1** | 27.8k | 🚀 +111 | 0 | today | `tooling` |
| 18 | [Smolagents](https://github.com/huggingface/smolagents) | 🟠 **36.9** | 26.6k | 🚀 +120 | 0 | 2 mo ago | `lightweight` |
| 19 | [Swarm](https://github.com/openai/swarm) | 🔴 **9.2** | 21.3k | 📈 +24 | 0 | — | `experimental` |

## 📂 By Category

- `data-agent`: **LlamaIndex** (58.1)
- `enterprise`: **Semantic Kernel** (49.5)
- `experimental`: **Swarm** (9.2)
- `lightweight`: **Smolagents** (36.9)
- `memory`: **Letta** (45.5)
- `multi-agent`: **CrewAI** (70.5), **Agno** (54.0), **AG2** (46.8), **AutoGen** (46.2)
- `optimization`: **DSPy** (46.1)
- `orchestration`: **LangGraph** (69.1), **Claude Agent SDK** (64.6), **Google ADK** (51.4), **OpenAI Agents SDK** (51.3)
- `pipeline`: **Haystack** (48.5)
- `structured`: **PydanticAI** (53.4)
- `tooling`: **Composio** (45.1)
- `typescript`: **Mastra** (74.1)
- `web-agent`: **BrowserUse** (69.5)

## 🔍 Top 5 — Score Breakdown

| Framework | Star Velocity | Release Freshness | Issue Health | Commit Activity | Community | Fork Ratio |
|-----------|:---:|:---:|:---:|:---:|:---:|:---:|
| **Mastra** | 38.2 | 98.3 | 93.8 | 100 | 75.6 | 32.8 |
| **CrewAI** | 100 | 100.0 | 95.6 | 0.0 | 57.0 | 54.6 |
| **BrowserUse** | 100 | 96.0 | 97.2 | 0.0 | 61.4 | 46.0 |
| **LangGraph** | 100 | 99.0 | 80.0 | 0.0 | 54.4 | 68.6 |
| **Claude Agent SDK** | 100 | 100.0 | 79.7 | 0.0 | 9.4 | 66.8 |

## 💡 Key Insights

- **Hottest framework**: Mastra with a Pulse Score of 74.1
- **Fastest growing**: Claude Agent SDK gained +3507 stars this week
- **Most active development**: Mastra with 633 commits in the last 4 weeks
- **Stale releases**: Swarm haven't released in a while

## 📦 Recent Releases

- **Composio** [`@composio/cli@0.2.23-beta.205`](https://github.com/ComposioHQ/composio/releases/tag/@composio/cli@0.2.23-beta.205) — today *(pre-release)*
- **Claude Agent SDK** [`v2.1.107`](https://github.com/anthropics/claude-code/releases/tag/v2.1.107) — today
- **PydanticAI** [`v1.81.0`](https://github.com/pydantic/pydantic-ai/releases/tag/v1.81.0) — today
- **Google ADK** [`v1.30.0`](https://github.com/google/adk-python/releases/tag/v1.30.0) — today
- **CrewAI** [`1.14.2a3`](https://github.com/crewAIInc/crewAI/releases/tag/1.14.2a3) — today *(pre-release)*
- **LangGraph** [`1.1.7a1`](https://github.com/langchain-ai/langgraph/releases/tag/1.1.7a1) — 3 days ago
- **Agno** [`v2.5.16`](https://github.com/agno-agi/agno/releases/tag/v2.5.16) — 3 days ago
- **OpenAI Agents SDK** [`v0.13.6`](https://github.com/openai/openai-agents-python/releases/tag/v0.13.6) — 5 days ago
- **Mastra** [`@mastra/core@1.24.0`](https://github.com/mastra-ai/mastra/releases/tag/@mastra/core@1.24.0) — 5 days ago
- **Semantic Kernel** [`python-1.41.2`](https://github.com/microsoft/semantic-kernel/releases/tag/python-1.41.2) — 6 days ago

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

*Powered by GitHub Actions • Data refreshed daily • Last run: 2026-04-14 07:57 UTC*