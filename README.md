# 🔬 AI Agent Framework Pulse Tracker

[![Daily Update](https://github.com/PurpleHaze2320/ai-agent-pulse/actions/workflows/track.yml/badge.svg)](https://github.com/PurpleHaze2320/ai-agent-pulse/actions/workflows/track.yml)
[![Frameworks Tracked](https://img.shields.io/badge/frameworks-19-blue)](https://github.com/PurpleHaze2320/ai-agent-pulse)
[![License: MIT](https://img.shields.io/badge/License-MIT-green.svg)](https://opensource.org/licenses/MIT)
[![GitHub stars](https://img.shields.io/github/stars/PurpleHaze2320/ai-agent-pulse?style=social)](https://github.com/PurpleHaze2320/ai-agent-pulse/stargazers)

> Automated daily tracking of the AI agent framework ecosystem's health, momentum, and trends.
> Last updated: **2026-04-11 07:08 UTC** | Tracking **19** frameworks

## How It Works

This bot runs daily via GitHub Actions and collects metrics from the GitHub API for the most important
AI agent frameworks. It computes a **Pulse Score** (0-100) based on six weighted signals: star velocity,
release freshness, issue health, commit activity, community size, and fork engagement. The result is
a living dashboard that shows which frameworks are gaining momentum and which are losing steam.

## 🏆 Pulse Leaderboard

| Rank | Framework | Pulse | Stars | ⭐ 7d | Commits (4w) | Last Release | Category |
|------|-----------|-------|-------|-------|--------------|--------------|----------|
| 1 | [Mastra](https://github.com/mastra-ai/mastra) | 🟢 **74.1** | 22.9k | 🚀 +233 | 810 | 2 days ago | `typescript` |
| 2 | [BrowserUse](https://github.com/browser-use/browser-use) | 🟡 **69.8** | 87.1k | 🚀 +1154 | 0 | 8 days ago | `web-agent` |
| 3 | [CrewAI](https://github.com/crewAIInc/crewAI) | 🟡 **68.9** | 48.6k | 🚀 +591 | 0 | today | `multi-agent` |
| 4 | [LangGraph](https://github.com/langchain-ai/langgraph) | 🟡 **66.7** | 28.9k | 🚀 +562 | 0 | today | `orchestration` |
| 5 | [Claude Agent SDK](https://github.com/anthropics/claude-code) | 🟡 **64.5** | 112.3k | 🚀 +4033 | 0 | today | `orchestration` |
| 6 | [LlamaIndex](https://github.com/run-llama/llama_index) | 🟡 **58.0** | 48.5k | 🚀 +212 | 0 | 7 days ago | `data-agent` |
| 7 | [Agno](https://github.com/agno-agi/agno) | 🟡 **53.7** | 39.3k | 🚀 +189 | 0 | today | `multi-agent` |
| 8 | [PydanticAI](https://github.com/pydantic/pydantic-ai) | 🟡 **52.0** | 16.3k | 🚀 +170 | 0 | today | `structured` |
| 9 | [OpenAI Agents SDK](https://github.com/openai/openai-agents-python) | 🟡 **51.0** | 20.7k | 🚀 +140 | 0 | 2 days ago | `orchestration` |
| 10 | [Semantic Kernel](https://github.com/microsoft/semantic-kernel) | 🟡 **50.0** | 27.7k | 📈 +46 | 0 | 3 days ago | `enterprise` |
| 11 | [Google ADK](https://github.com/google/adk-python) | 🟡 **49.3** | 18.9k | 🚀 +129 | 0 | 1 day ago | `orchestration` |
| 12 | [Haystack](https://github.com/deepset-ai/haystack) | 🟡 **49.2** | 24.8k | 🚀 +104 | 0 | 9 days ago | `pipeline` |
| 13 | [AG2](https://github.com/ag2ai/ag2) | 🟡 **47.0** | 4.4k | 📈 +27 | 0 | 6 days ago | `multi-agent` |
| 14 | [AutoGen](https://github.com/microsoft/autogen) | 🟡 **45.6** | 56.9k | 🚀 +279 | 0 | 6 mo ago | `multi-agent` |
| 15 | [DSPy](https://github.com/stanfordnlp/dspy) | 🟡 **45.6** | 33.6k | 🚀 +169 | 0 | 2 mo ago | `optimization` |
| 16 | [Letta](https://github.com/letta-ai/letta) | 🟡 **44.9** | 22.0k | 🚀 +110 | 0 | 10 days ago | `memory` |
| 17 | [Composio](https://github.com/ComposioHQ/composio) | 🟡 **44.6** | 27.7k | 🚀 +105 | 0 | today | `tooling` |
| 18 | [Smolagents](https://github.com/huggingface/smolagents) | 🟠 **37.0** | 26.5k | 🚀 +123 | 0 | 2 mo ago | `lightweight` |
| 19 | [Swarm](https://github.com/openai/swarm) | 🔴 **8.9** | 21.3k | ↗️ +15 | 0 | — | `experimental` |

## 📂 By Category

- `data-agent`: **LlamaIndex** (58.0)
- `enterprise`: **Semantic Kernel** (50.0)
- `experimental`: **Swarm** (8.9)
- `lightweight`: **Smolagents** (37.0)
- `memory`: **Letta** (44.9)
- `multi-agent`: **CrewAI** (68.9), **Agno** (53.7), **AG2** (47.0), **AutoGen** (45.6)
- `optimization`: **DSPy** (45.6)
- `orchestration`: **LangGraph** (66.7), **Claude Agent SDK** (64.5), **OpenAI Agents SDK** (51.0), **Google ADK** (49.3)
- `pipeline`: **Haystack** (49.2)
- `structured`: **PydanticAI** (52.0)
- `tooling`: **Composio** (44.6)
- `typescript`: **Mastra** (74.1)
- `web-agent`: **BrowserUse** (69.8)

## 🔍 Top 5 — Score Breakdown

| Framework | Star Velocity | Release Freshness | Issue Health | Commit Activity | Community | Fork Ratio |
|-----------|:---:|:---:|:---:|:---:|:---:|:---:|
| **Mastra** | 37.4 | 99.3 | 93.8 | 100 | 75.6 | 32.7 |
| **BrowserUse** | 100 | 97.3 | 97.2 | 0.0 | 61.2 | 46.1 |
| **CrewAI** | 94.2 | 100.0 | 94.9 | 0.0 | 56.8 | 54.6 |
| **LangGraph** | 90.0 | 100.0 | 79.9 | 0.0 | 54.2 | 68.5 |
| **Claude Agent SDK** | 100 | 100.0 | 79.4 | 0.0 | 9.4 | 66.8 |

## 💡 Key Insights

- **Hottest framework**: Mastra with a Pulse Score of 74.1
- **Fastest growing**: Claude Agent SDK gained +4033 stars this week
- **Most active development**: Mastra with 810 commits in the last 4 weeks
- **Stale releases**: Swarm haven't released in a while

## 📦 Recent Releases

- **Composio** [`@composio/cli@0.2.23-beta.199`](https://github.com/ComposioHQ/composio/releases/tag/@composio/cli@0.2.23-beta.199) — today *(pre-release)*
- **PydanticAI** [`v1.80.0`](https://github.com/pydantic/pydantic-ai/releases/tag/v1.80.0) — today
- **LangGraph** [`1.1.7a1`](https://github.com/langchain-ai/langgraph/releases/tag/1.1.7a1) — today
- **Agno** [`v2.5.16`](https://github.com/agno-agi/agno/releases/tag/v2.5.16) — today
- **Claude Agent SDK** [`v2.1.101`](https://github.com/anthropics/claude-code/releases/tag/v2.1.101) — today
- **CrewAI** [`1.14.2a2`](https://github.com/crewAIInc/crewAI/releases/tag/1.14.2a2) — today *(pre-release)*
- **Google ADK** [`v2.0.0a3`](https://github.com/google/adk-python/releases/tag/v2.0.0a3) — 1 day ago *(pre-release)*
- **OpenAI Agents SDK** [`v0.13.6`](https://github.com/openai/openai-agents-python/releases/tag/v0.13.6) — 2 days ago
- **Mastra** [`@mastra/core@1.24.0`](https://github.com/mastra-ai/mastra/releases/tag/@mastra/core@1.24.0) — 2 days ago
- **Semantic Kernel** [`python-1.41.2`](https://github.com/microsoft/semantic-kernel/releases/tag/python-1.41.2) — 3 days ago

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

*Powered by GitHub Actions • Data refreshed daily • Last run: 2026-04-11 07:08 UTC*