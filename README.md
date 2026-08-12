# 🔬 AI Agent Framework Pulse Tracker

[![Daily Update](https://github.com/PurpleHaze2320/ai-agent-pulse/actions/workflows/track.yml/badge.svg)](https://github.com/PurpleHaze2320/ai-agent-pulse/actions/workflows/track.yml)
[![Frameworks Tracked](https://img.shields.io/badge/frameworks-19-blue)](https://github.com/PurpleHaze2320/ai-agent-pulse)
[![License: MIT](https://img.shields.io/badge/License-MIT-green.svg)](https://opensource.org/licenses/MIT)
[![GitHub stars](https://img.shields.io/github/stars/PurpleHaze2320/ai-agent-pulse?style=social)](https://github.com/PurpleHaze2320/ai-agent-pulse/stargazers)

> Automated daily tracking of the AI agent framework ecosystem's health, momentum, and trends.
> Last updated: **2026-08-12 07:39 UTC** | Tracking **19** frameworks

## How It Works

This bot runs daily via GitHub Actions and collects metrics from the GitHub API for the most important
AI agent frameworks. It computes a **Pulse Score** (0-100) based on six weighted signals: star velocity,
release freshness, issue health, commit activity, community size, and fork engagement. The result is
a living dashboard that shows which frameworks are gaining momentum and which are losing steam.

## 🏆 Pulse Leaderboard

| Rank | Framework | Pulse | Stars | ⭐ 7d | Commits (4w) | Last Release | Category |
|------|-----------|-------|-------|-------|--------------|--------------|----------|
| 1 | [BrowserUse](https://github.com/browser-use/browser-use) | 🟢 **89.2** | 108.9k | 🚀 +956 | 149 | 15 days ago | `web-agent` |
| 2 | [CrewAI](https://github.com/crewAIInc/crewAI) | 🟢 **79.2** | 57.0k | 🚀 +328 | 80 | today | `multi-agent` |
| 3 | [Mastra](https://github.com/mastra-ai/mastra) | 🟢 **77.5** | 27.1k | 🚀 +180 | 1357 | 1 day ago | `typescript` |
| 4 | [OpenAI Agents SDK](https://github.com/openai/openai-agents-python) | 🟢 **76.6** | 28.6k | 🚀 +175 | 318 | 1 day ago | `orchestration` |
| 5 | [LangGraph](https://github.com/langchain-ai/langgraph) | 🟢 **75.8** | 39.5k | 🚀 +571 | 40 | today | `orchestration` |
| 6 | [Claude Agent SDK](https://github.com/anthropics/claude-code) | 🟡 **68.0** | 141.1k | 🚀 +832 | 16 | today | `orchestration` |
| 7 | [Composio](https://github.com/ComposioHQ/composio) | 🟡 **67.6** | 29.6k | 🚀 +101 | 307 | today | `tooling` |
| 8 | [Agno](https://github.com/agno-agi/agno) | 🟡 **65.5** | 41.7k | 📈 +94 | 72 | 5 days ago | `multi-agent` |
| 9 | [DSPy](https://github.com/stanfordnlp/dspy) | 🟡 **64.7** | 37.1k | 🚀 +500 | 0 | 8 days ago | `optimization` |
| 10 | [LlamaIndex](https://github.com/run-llama/llama_index) | 🟡 **62.1** | 51.6k | 🚀 +187 | 28 | 1 mo ago | `data-agent` |
| 11 | [PydanticAI](https://github.com/pydantic/pydantic-ai) | 🟡 **56.4** | 19.2k | 🚀 +180 | 0 | today | `structured` |
| 12 | [Semantic Kernel](https://github.com/microsoft/semantic-kernel) | 🟡 **54.4** | 28.4k | 📈 +24 | 20 | 5 days ago | `enterprise` |
| 13 | [Google ADK](https://github.com/google/adk-python) | 🟡 **52.7** | 21.1k | 📈 +66 | 0 | 4 days ago | `orchestration` |
| 14 | [Haystack](https://github.com/deepset-ai/haystack) | 🟡 **49.7** | 26.2k | 📈 +71 | 0 | 22 days ago | `pipeline` |
| 15 | [AG2](https://github.com/ag2ai/ag2) | 🟡 **49.3** | 4.9k | ↗️ +20 | 0 | 14 days ago | `multi-agent` |
| 16 | [Letta](https://github.com/letta-ai/letta) | 🟡 **41.8** | 24.2k | 🚀 +112 | 2 | 2 mo ago | `memory` |
| 17 | [Smolagents](https://github.com/huggingface/smolagents) | 🟠 **37.5** | 28.8k | 📈 +86 | 0 | 2 mo ago | `lightweight` |
| 18 | [AutoGen](https://github.com/microsoft/autogen) | 🟠 **34.6** | 60.4k | 🚀 +139 | 0 | 10 mo ago | `multi-agent` |
| 19 | [Swarm](https://github.com/openai/swarm) | 🔴 **9.6** | 21.9k | ↗️ +18 | 0 | — | `experimental` |

## 📂 By Category

- `data-agent`: **LlamaIndex** (62.1)
- `enterprise`: **Semantic Kernel** (54.4)
- `experimental`: **Swarm** (9.6)
- `lightweight`: **Smolagents** (37.5)
- `memory`: **Letta** (41.8)
- `multi-agent`: **CrewAI** (79.2), **Agno** (65.5), **AG2** (49.3), **AutoGen** (34.6)
- `optimization`: **DSPy** (64.7)
- `orchestration`: **OpenAI Agents SDK** (76.6), **LangGraph** (75.8), **Claude Agent SDK** (68.0), **Google ADK** (52.7)
- `pipeline`: **Haystack** (49.7)
- `structured`: **PydanticAI** (56.4)
- `tooling`: **Composio** (67.6)
- `typescript`: **Mastra** (77.5)
- `web-agent`: **BrowserUse** (89.2)

## 🔍 Top 5 — Score Breakdown

| Framework | Star Velocity | Release Freshness | Issue Health | Commit Activity | Community | Fork Ratio |
|-----------|:---:|:---:|:---:|:---:|:---:|:---:|
| **BrowserUse** | 100 | 95.0 | 93.9 | 100 | 66.8 | 43.9 |
| **CrewAI** | 69.2 | 100.0 | 95.0 | 80.0 | 59.8 | 57.1 |
| **Mastra** | 40.1 | 99.7 | 95.9 | 100 | 92.6 | 38.5 |
| **OpenAI Agents SDK** | 35.1 | 99.7 | 99.4 | 100 | 67.6 | 62.7 |
| **LangGraph** | 100 | 100.0 | 70.5 | 40.0 | 55.4 | 67.2 |

## 💡 Key Insights

- **Hottest framework**: BrowserUse with a Pulse Score of 89.2
- **Fastest growing**: BrowserUse gained +956 stars this week
- **Most active development**: Mastra with 1357 commits in the last 4 weeks
- **Stale releases**: AutoGen, Swarm haven't released in a while

## 📦 Recent Releases

- **PydanticAI** [`v1.107.4`](https://github.com/pydantic/pydantic-ai/releases/tag/v1.107.4) — today
- **CrewAI** [`1.15.15`](https://github.com/crewAIInc/crewAI/releases/tag/1.15.15) — today
- **Claude Agent SDK** [`v2.1.228`](https://github.com/anthropics/claude-code/releases/tag/v2.1.228) — today
- **LangGraph** [`1.2.11`](https://github.com/langchain-ai/langgraph/releases/tag/1.2.11) — today
- **Composio** [`@composio/slim@0.16.0`](https://github.com/ComposioHQ/composio/releases/tag/@composio/slim@0.16.0) — today
- **OpenAI Agents SDK** [`v0.20.0`](https://github.com/openai/openai-agents-python/releases/tag/v0.20.0) — 1 day ago
- **Mastra** [`@mastra/core@1.57.0`](https://github.com/mastra-ai/mastra/releases/tag/@mastra/core@1.57.0) — 1 day ago
- **Google ADK** [`v2.6.3`](https://github.com/google/adk-python/releases/tag/v2.6.3) — 4 days ago
- **Agno** [`v3.0.0a1`](https://github.com/agno-agi/agno/releases/tag/v3.0.0a1) — 5 days ago *(pre-release)*
- **Semantic Kernel** [`python-1.44.1`](https://github.com/microsoft/semantic-kernel/releases/tag/python-1.44.1) — 5 days ago

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

*Powered by GitHub Actions • Data refreshed daily • Last run: 2026-08-12 07:39 UTC*