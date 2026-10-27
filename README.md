# 🔬 AI Agent Framework Pulse Tracker

[![Daily Update](https://github.com/PurpleHaze2320/ai-agent-pulse/actions/workflows/track.yml/badge.svg)](https://github.com/PurpleHaze2320/ai-agent-pulse/actions/workflows/track.yml)
[![Frameworks Tracked](https://img.shields.io/badge/frameworks-19-blue)](https://github.com/PurpleHaze2320/ai-agent-pulse)
[![License: MIT](https://img.shields.io/badge/License-MIT-green.svg)](https://opensource.org/licenses/MIT)
[![GitHub stars](https://img.shields.io/github/stars/PurpleHaze2320/ai-agent-pulse?style=social)](https://github.com/PurpleHaze2320/ai-agent-pulse/stargazers)

> Automated daily tracking of the AI agent framework ecosystem's health, momentum, and trends.
> Last updated: **2026-10-27 11:52 UTC** | Tracking **19** frameworks

## How It Works

This bot runs daily via GitHub Actions and collects metrics from the GitHub API for the most important
AI agent frameworks. It computes a **Pulse Score** (0-100) based on six weighted signals: star velocity,
release freshness, issue health, commit activity, community size, and fork engagement. The result is
a living dashboard that shows which frameworks are gaining momentum and which are losing steam.

## 🏆 Pulse Leaderboard

| Rank | Framework | Pulse | Stars | ⭐ 7d | Commits (4w) | Last Release | Category |
|------|-----------|-------|-------|-------|--------------|--------------|----------|
| 1 | [BrowserUse](https://github.com/browser-use/browser-use) | 🟢 **90.0** | 119.3k | 🚀 +656 | 116 | today | `web-agent` |
| 2 | [LangGraph](https://github.com/langchain-ai/langgraph) | 🟢 **85.1** | 44.0k | 🚀 +412 | 112 | today | `orchestration` |
| 3 | [CrewAI](https://github.com/crewAIInc/crewAI) | 🟢 **79.0** | 60.2k | 🚀 +257 | 138 | 3 days ago | `multi-agent` |
| 4 | [Mastra](https://github.com/mastra-ai/mastra) | 🟢 **76.3** | 29.1k | 🚀 +171 | 2068 | 5 days ago | `typescript` |
| 5 | [Google ADK](https://github.com/google/adk-python) | 🟢 **75.2** | 22.0k | 🚀 +101 | 430 | 3 days ago | `orchestration` |
| 6 | [PydanticAI](https://github.com/pydantic/pydantic-ai) | 🟢 **74.5** | 20.9k | 🚀 +153 | 961 | today | `structured` |
| 7 | [Claude Agent SDK](https://github.com/anthropics/claude-code) | 🟢 **74.1** | 153.5k | 🚀 +654 | 42 | today | `orchestration` |
| 8 | [Haystack](https://github.com/deepset-ai/haystack) | 🟢 **71.6** | 26.9k | 📈 +69 | 217 | 5 days ago | `pipeline` |
| 9 | [OpenAI Agents SDK](https://github.com/openai/openai-agents-python) | 🟢 **71.1** | 30.3k | 🚀 +158 | 73 | 12 days ago | `orchestration` |
| 10 | [Agno](https://github.com/agno-agi/agno) | 🟢 **70.1** | 42.9k | 📈 +84 | 151 | 3 days ago | `multi-agent` |
| 11 | [AG2](https://github.com/ag2ai/ag2) | 🟡 **69.6** | 5.0k | ↗️ +19 | 99 | 5 days ago | `multi-agent` |
| 12 | [Composio](https://github.com/ComposioHQ/composio) | 🟡 **68.5** | 30.8k | 🚀 +128 | 307 | today | `tooling` |
| 13 | [Semantic Kernel](https://github.com/microsoft/semantic-kernel) | 🟡 **60.7** | 28.7k | 📈 +27 | 54 | 20 days ago | `enterprise` |
| 14 | [DSPy](https://github.com/stanfordnlp/dspy) | 🟡 **60.6** | 38.8k | 🚀 +114 | 61 | 14 days ago | `optimization` |
| 15 | [LlamaIndex](https://github.com/run-llama/llama_index) | 🟡 **54.8** | 52.7k | 🚀 +106 | 9 | 1 mo ago | `data-agent` |
| 16 | [Letta](https://github.com/letta-ai/letta) | 🟠 **34.8** | 25.3k | 📈 +64 | 1 | 5 mo ago | `memory` |
| 17 | [Smolagents](https://github.com/huggingface/smolagents) | 🟠 **34.3** | 30.1k | 🚀 +149 | 1 | 5 mo ago | `lightweight` |
| 18 | [AutoGen](https://github.com/microsoft/autogen) | 🟠 **32.0** | 61.6k | 📈 +89 | 1 | 1y ago | `multi-agent` |
| 19 | [Swarm](https://github.com/openai/swarm) | 🔴 **9.2** | 22.1k | ↗️ +17 | 0 | — | `experimental` |

## 📂 By Category

- `data-agent`: **LlamaIndex** (54.8)
- `enterprise`: **Semantic Kernel** (60.7)
- `experimental`: **Swarm** (9.2)
- `lightweight`: **Smolagents** (34.3)
- `memory`: **Letta** (34.8)
- `multi-agent`: **CrewAI** (79.0), **Agno** (70.1), **AG2** (69.6), **AutoGen** (32.0)
- `optimization`: **DSPy** (60.6)
- `orchestration`: **LangGraph** (85.1), **Google ADK** (75.2), **Claude Agent SDK** (74.1), **OpenAI Agents SDK** (71.1)
- `pipeline`: **Haystack** (71.6)
- `structured`: **PydanticAI** (74.5)
- `tooling`: **Composio** (68.5)
- `typescript`: **Mastra** (76.3)
- `web-agent`: **BrowserUse** (90.0)

## 🔍 Top 5 — Score Breakdown

| Framework | Star Velocity | Release Freshness | Issue Health | Commit Activity | Community | Fork Ratio |
|-----------|:---:|:---:|:---:|:---:|:---:|:---:|
| **BrowserUse** | 100 | 100.0 | 89.1 | 100 | 72.2 | 44.5 |
| **LangGraph** | 82.2 | 100.0 | 79.8 | 100 | 57.2 | 68.7 |
| **CrewAI** | 52.2 | 99.0 | 86.7 | 100 | 72.4 | 59.2 |
| **Mastra** | 35.2 | 98.3 | 95.0 | 100 | 93.6 | 41.9 |
| **Google ADK** | 19.6 | 99.0 | 94.4 | 100 | 85.6 | 77.3 |

## 💡 Key Insights

- **Hottest framework**: BrowserUse with a Pulse Score of 90.0
- **Fastest growing**: BrowserUse gained +656 stars this week
- **Most active development**: Mastra with 2068 commits in the last 4 weeks
- **Stale releases**: AutoGen, Swarm haven't released in a while

## 📦 Recent Releases

- **Composio** [`@composio/cli@0.5.1-beta.502`](https://github.com/ComposioHQ/composio/releases/tag/@composio/cli@0.5.1-beta.502) — today *(pre-release)*
- **PydanticAI** [`v2.62.0`](https://github.com/pydantic/pydantic-ai/releases/tag/v2.62.0) — today
- **BrowserUse** [`0.13.14`](https://github.com/browser-use/browser-use/releases/tag/0.13.14) — today
- **Claude Agent SDK** [`v2.1.311`](https://github.com/anthropics/claude-code/releases/tag/v2.1.311) — today
- **LangGraph** [`1.2.18`](https://github.com/langchain-ai/langgraph/releases/tag/1.2.18) — today
- **CrewAI** [`1.15.30`](https://github.com/crewAIInc/crewAI/releases/tag/1.15.30) — 3 days ago
- **Google ADK** [`v2.13.0`](https://github.com/google/adk-python/releases/tag/v2.13.0) — 3 days ago
- **Agno** [`v3.1.10`](https://github.com/agno-agi/agno/releases/tag/v3.1.10) — 3 days ago
- **AG2** [`v1.2.1`](https://github.com/ag2ai/ag2/releases/tag/v1.2.1) — 5 days ago
- **Haystack** [`v3.4.1`](https://github.com/deepset-ai/haystack/releases/tag/v3.4.1) — 5 days ago

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

*Powered by GitHub Actions • Data refreshed daily • Last run: 2026-10-27 11:52 UTC*