# 🔬 AI Agent Framework Pulse Tracker

[![Daily Update](https://github.com/PurpleHaze2320/ai-agent-pulse/actions/workflows/track.yml/badge.svg)](https://github.com/PurpleHaze2320/ai-agent-pulse/actions/workflows/track.yml)
[![Frameworks Tracked](https://img.shields.io/badge/frameworks-19-blue)](https://github.com/PurpleHaze2320/ai-agent-pulse)
[![License: MIT](https://img.shields.io/badge/License-MIT-green.svg)](https://opensource.org/licenses/MIT)
[![GitHub stars](https://img.shields.io/github/stars/PurpleHaze2320/ai-agent-pulse?style=social)](https://github.com/PurpleHaze2320/ai-agent-pulse/stargazers)

> Automated daily tracking of the AI agent framework ecosystem's health, momentum, and trends.
> Last updated: **2026-10-08 13:08 UTC** | Tracking **19** frameworks

## How It Works

This bot runs daily via GitHub Actions and collects metrics from the GitHub API for the most important
AI agent frameworks. It computes a **Pulse Score** (0-100) based on six weighted signals: star velocity,
release freshness, issue health, commit activity, community size, and fork engagement. The result is
a living dashboard that shows which frameworks are gaining momentum and which are losing steam.

## 🏆 Pulse Leaderboard

| Rank | Framework | Pulse | Stars | ⭐ 7d | Commits (4w) | Last Release | Category |
|------|-----------|-------|-------|-------|--------------|--------------|----------|
| 1 | [Claude Agent SDK](https://github.com/anthropics/claude-code) | 🟢 **81.9** | 149.8k | 🚀 +1056 | 80 | today | `orchestration` |
| 2 | [BrowserUse](https://github.com/browser-use/browser-use) | 🟢 **81.7** | 117.5k | 🚀 +576 | 58 | 1 day ago | `web-agent` |
| 3 | [Mastra](https://github.com/mastra-ai/mastra) | 🟢 **77.0** | 28.6k | 🚀 +172 | 2107 | today | `typescript` |
| 4 | [OpenAI Agents SDK](https://github.com/openai/openai-agents-python) | 🟢 **75.4** | 29.9k | 🚀 +111 | 231 | 5 days ago | `orchestration` |
| 5 | [PydanticAI](https://github.com/pydantic/pydantic-ai) | 🟢 **74.9** | 20.5k | 🚀 +179 | 768 | 2 days ago | `structured` |
| 6 | [LangGraph](https://github.com/langchain-ai/langgraph) | 🟢 **74.2** | 42.9k | 🚀 +340 | 69 | today | `orchestration` |
| 7 | [CrewAI](https://github.com/crewAIInc/crewAI) | 🟢 **73.7** | 59.5k | 🚀 +197 | 80 | today | `multi-agent` |
| 8 | [Agno](https://github.com/agno-agi/agno) | 🟢 **72.6** | 42.6k | 🚀 +162 | 108 | 6 days ago | `multi-agent` |
| 9 | [Haystack](https://github.com/deepset-ai/haystack) | 🟢 **71.0** | 26.7k | 📈 +59 | 240 | 7 days ago | `pipeline` |
| 10 | [AG2](https://github.com/ag2ai/ag2) | 🟡 **68.7** | 5.0k | ↗️ +12 | 96 | 5 days ago | `multi-agent` |
| 11 | [Composio](https://github.com/ComposioHQ/composio) | 🟡 **66.9** | 30.5k | 📈 +82 | 290 | today | `tooling` |
| 12 | [DSPy](https://github.com/stanfordnlp/dspy) | 🟡 **60.8** | 38.6k | 🚀 +110 | 58 | 13 days ago | `optimization` |
| 13 | [LlamaIndex](https://github.com/run-llama/llama_index) | 🟡 **57.4** | 52.4k | 📈 +58 | 24 | 16 days ago | `data-agent` |
| 14 | [Semantic Kernel](https://github.com/microsoft/semantic-kernel) | 🟡 **53.7** | 28.6k | ↗️ +15 | 18 | 2 days ago | `enterprise` |
| 15 | [Google ADK](https://github.com/google/adk-python) | 🟡 **52.6** | 21.7k | 📈 +56 | 0 | 6 days ago | `orchestration` |
| 16 | [Letta](https://github.com/letta-ai/letta) | 🟠 **36.7** | 25.1k | 📈 +82 | 0 | 4 mo ago | `memory` |
| 17 | [Smolagents](https://github.com/huggingface/smolagents) | 🟠 **35.4** | 29.7k | 🚀 +116 | 5 | 4 mo ago | `lightweight` |
| 18 | [AutoGen](https://github.com/microsoft/autogen) | 🟠 **30.6** | 61.3k | 📈 +52 | 0 | 1y ago | `multi-agent` |
| 19 | [Swarm](https://github.com/openai/swarm) | 🔴 **9.4** | 22.0k | ↗️ +16 | 0 | — | `experimental` |

## 📂 By Category

- `data-agent`: **LlamaIndex** (57.4)
- `enterprise`: **Semantic Kernel** (53.7)
- `experimental`: **Swarm** (9.4)
- `lightweight`: **Smolagents** (35.4)
- `memory`: **Letta** (36.7)
- `multi-agent`: **CrewAI** (73.7), **Agno** (72.6), **AG2** (68.7), **AutoGen** (30.6)
- `optimization`: **DSPy** (60.8)
- `orchestration`: **Claude Agent SDK** (81.9), **OpenAI Agents SDK** (75.4), **LangGraph** (74.2), **Google ADK** (52.6)
- `pipeline`: **Haystack** (71.0)
- `structured`: **PydanticAI** (74.9)
- `tooling`: **Composio** (66.9)
- `typescript`: **Mastra** (77.0)
- `web-agent`: **BrowserUse** (81.7)

## 🔍 Top 5 — Score Breakdown

| Framework | Star Velocity | Release Freshness | Issue Health | Commit Activity | Community | Fork Ratio |
|-----------|:---:|:---:|:---:|:---:|:---:|:---:|
| **Claude Agent SDK** | 100 | 100.0 | 85.8 | 80.0 | 11.4 | 68.7 |
| **BrowserUse** | 100 | 99.7 | 90.1 | 58.0 | 72.0 | 44.2 |
| **Mastra** | 36.7 | 100.0 | 95.4 | 100 | 93.6 | 41.1 |
| **OpenAI Agents SDK** | 25.2 | 98.3 | 99.6 | 100 | 80.2 | 64.9 |
| **PydanticAI** | 35.6 | 99.3 | 73.8 | 100 | 95.0 | 56.2 |

## 💡 Key Insights

- **Hottest framework**: Claude Agent SDK with a Pulse Score of 81.9
- **Fastest growing**: Claude Agent SDK gained +1056 stars this week
- **Most active development**: Mastra with 2107 commits in the last 4 weeks
- **Stale releases**: AutoGen, Swarm haven't released in a while

## 📦 Recent Releases

- **Composio** [`@composio/cli@0.4.3-beta.417`](https://github.com/ComposioHQ/composio/releases/tag/@composio/cli@0.4.3-beta.417) — today *(pre-release)*
- **Claude Agent SDK** [`v2.1.294`](https://github.com/anthropics/claude-code/releases/tag/v2.1.294) — today
- **CrewAI** [`1.15.25`](https://github.com/crewAIInc/crewAI/releases/tag/1.15.25) — today
- **Mastra** [`@mastra/core@1.75.0`](https://github.com/mastra-ai/mastra/releases/tag/@mastra/core@1.75.0) — today
- **LangGraph** [`cli==0.4.33`](https://github.com/langchain-ai/langgraph/releases/tag/cli==0.4.33) — today
- **BrowserUse** [`0.13.11`](https://github.com/browser-use/browser-use/releases/tag/0.13.11) — 1 day ago
- **Semantic Kernel** [`python-1.45.0`](https://github.com/microsoft/semantic-kernel/releases/tag/python-1.45.0) — 2 days ago
- **PydanticAI** [`clai2-bleeding`](https://github.com/pydantic/pydantic-ai/releases/tag/clai2-bleeding) — 2 days ago *(pre-release)*
- **AG2** [`v1.1.2`](https://github.com/ag2ai/ag2/releases/tag/v1.1.2) — 5 days ago
- **OpenAI Agents SDK** [`v0.23.1`](https://github.com/openai/openai-agents-python/releases/tag/v0.23.1) — 5 days ago

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

*Powered by GitHub Actions • Data refreshed daily • Last run: 2026-10-08 13:08 UTC*