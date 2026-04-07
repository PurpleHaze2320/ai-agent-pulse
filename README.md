# 🔬 AI Agent Framework Pulse Tracker

[![Daily Update](https://github.com/PurpleHaze2320/ai-agent-pulse/actions/workflows/track.yml/badge.svg)](https://github.com/PurpleHaze2320/ai-agent-pulse/actions/workflows/track.yml)
[![Frameworks Tracked](https://img.shields.io/badge/frameworks-19-blue)](https://github.com/PurpleHaze2320/ai-agent-pulse)
[![License: MIT](https://img.shields.io/badge/License-MIT-green.svg)](https://opensource.org/licenses/MIT)
[![GitHub stars](https://img.shields.io/github/stars/PurpleHaze2320/ai-agent-pulse?style=social)](https://github.com/PurpleHaze2320/ai-agent-pulse/stargazers)

> Automated daily tracking of the AI agent framework ecosystem's health, momentum, and trends.
> Last updated: **2026-04-07 07:27 UTC** | Tracking **19** frameworks

## How It Works

This bot runs daily via GitHub Actions and collects metrics from the GitHub API for the most important
AI agent frameworks. It computes a **Pulse Score** (0-100) based on six weighted signals: star velocity,
release freshness, issue health, commit activity, community size, and fork engagement. The result is
a living dashboard that shows which frameworks are gaining momentum and which are losing steam.

## 🏆 Pulse Leaderboard

| Rank | Framework | Pulse | Stars | ⭐ 7d | Commits (4w) | Last Release | Category |
|------|-----------|-------|-------|-------|--------------|--------------|----------|
| 1 | [Mastra](https://github.com/mastra-ai/mastra) | 🟢 **71.2** | 22.8k | 🚀 +181 | 695 | 11 days ago | `typescript` |
| 2 | [BrowserUse](https://github.com/browser-use/browser-use) | 🟢 **70.1** | 86.3k | 🚀 +764 | 0 | 4 days ago | `web-agent` |
| 3 | [Claude Agent SDK](https://github.com/anthropics/claude-code) | 🟡 **64.3** | 110.2k | 🚀 +8083 | 0 | 3 days ago | `orchestration` |
| 4 | [CrewAI](https://github.com/crewAIInc/crewAI) | 🟡 **61.0** | 48.2k | 🚀 +403 | 0 | today | `multi-agent` |
| 5 | [LangGraph](https://github.com/langchain-ai/langgraph) | 🟡 **60.1** | 28.6k | 🚀 +410 | 0 | 3 days ago | `orchestration` |
| 6 | [LlamaIndex](https://github.com/run-llama/llama_index) | 🟡 **55.4** | 48.4k | 🚀 +143 | 0 | 3 days ago | `data-agent` |
| 7 | [Agno](https://github.com/agno-agi/agno) | 🟡 **50.6** | 39.2k | 🚀 +126 | 0 | 4 days ago | `multi-agent` |
| 8 | [OpenAI Agents SDK](https://github.com/openai/openai-agents-python) | 🟡 **50.1** | 20.6k | 🚀 +123 | 0 | 1 day ago | `orchestration` |
| 9 | [PydanticAI](https://github.com/pydantic/pydantic-ai) | 🟡 **49.4** | 16.1k | 🚀 +127 | 0 | 4 days ago | `structured` |
| 10 | [Semantic Kernel](https://github.com/microsoft/semantic-kernel) | 🟡 **49.3** | 27.7k | 📈 +50 | 0 | 13 days ago | `enterprise` |
| 11 | [Haystack](https://github.com/deepset-ai/haystack) | 🟡 **47.9** | 24.7k | 📈 +66 | 0 | 5 days ago | `pipeline` |
| 12 | [Google ADK](https://github.com/google/adk-python) | 🟡 **47.5** | 18.8k | 📈 +90 | 0 | 4 days ago | `orchestration` |
| 13 | [AG2](https://github.com/ag2ai/ag2) | 🟡 **47.2** | 4.4k | 📈 +28 | 0 | 2 days ago | `multi-agent` |
| 14 | [DSPy](https://github.com/stanfordnlp/dspy) | 🟡 **44.1** | 33.5k | 🚀 +129 | 0 | 2 mo ago | `optimization` |
| 15 | [Letta](https://github.com/letta-ai/letta) | 🟡 **43.5** | 21.9k | 📈 +71 | 0 | 6 days ago | `memory` |
| 16 | [Composio](https://github.com/ComposioHQ/composio) | 🟡 **43.0** | 27.7k | 📈 +59 | 0 | today | `tooling` |
| 17 | [AutoGen](https://github.com/microsoft/autogen) | 🟡 **42.6** | 56.8k | 🚀 +198 | 0 | 6 mo ago | `multi-agent` |
| 18 | [Smolagents](https://github.com/huggingface/smolagents) | 🟠 **35.9** | 26.5k | 📈 +90 | 0 | 2 mo ago | `lightweight` |
| 19 | [Swarm](https://github.com/openai/swarm) | 🔴 **8.9** | 21.3k | ↗️ +8 | 0 | — | `experimental` |

## 📂 By Category

- `data-agent`: **LlamaIndex** (55.4)
- `enterprise`: **Semantic Kernel** (49.3)
- `experimental`: **Swarm** (8.9)
- `lightweight`: **Smolagents** (35.9)
- `memory`: **Letta** (43.5)
- `multi-agent`: **CrewAI** (61.0), **Agno** (50.6), **AG2** (47.2), **AutoGen** (42.6)
- `optimization`: **DSPy** (44.1)
- `orchestration`: **Claude Agent SDK** (64.3), **LangGraph** (60.1), **OpenAI Agents SDK** (50.1), **Google ADK** (47.5)
- `pipeline`: **Haystack** (47.9)
- `structured`: **PydanticAI** (49.4)
- `tooling`: **Composio** (43.0)
- `typescript`: **Mastra** (71.2)
- `web-agent`: **BrowserUse** (70.1)

## 🔍 Top 5 — Score Breakdown

| Framework | Star Velocity | Release Freshness | Issue Health | Commit Activity | Community | Fork Ratio |
|-----------|:---:|:---:|:---:|:---:|:---:|:---:|
| **Mastra** | 28.1 | 96.3 | 94.1 | 100 | 75.6 | 32.5 |
| **BrowserUse** | 100 | 98.7 | 97.5 | 0.0 | 61.0 | 46.3 |
| **Claude Agent SDK** | 100 | 99.0 | 79.3 | 0.0 | 9.4 | 66.5 |
| **CrewAI** | 62.5 | 100.0 | 94.7 | 0.0 | 56.8 | 54.5 |
| **LangGraph** | 63.5 | 99.0 | 80.7 | 0.0 | 54.4 | 68.4 |

## 💡 Key Insights

- **Hottest framework**: Mastra with a Pulse Score of 71.2
- **Fastest growing**: Claude Agent SDK gained +8083 stars this week
- **Most active development**: Mastra with 695 commits in the last 4 weeks
- **Stale releases**: Swarm haven't released in a while

## 📦 Recent Releases

- **Composio** [`@composio/cli@0.2.20-beta.182`](https://github.com/ComposioHQ/composio/releases/tag/@composio/cli@0.2.20-beta.182) — today *(pre-release)*
- **CrewAI** [`1.14.0a3`](https://github.com/crewAIInc/crewAI/releases/tag/1.14.0a3) — today *(pre-release)*
- **OpenAI Agents SDK** [`v0.13.5`](https://github.com/openai/openai-agents-python/releases/tag/v0.13.5) — 1 day ago
- **AG2** [`v0.11.5`](https://github.com/ag2ai/ag2/releases/tag/v0.11.5) — 2 days ago
- **Claude Agent SDK** [`v2.1.92`](https://github.com/anthropics/claude-code/releases/tag/v2.1.92) — 3 days ago
- **LlamaIndex** [`v0.14.20`](https://github.com/run-llama/llama_index/releases/tag/v0.14.20) — 3 days ago
- **LangGraph** [`1.1.6`](https://github.com/langchain-ai/langgraph/releases/tag/1.1.6) — 3 days ago
- **PydanticAI** [`v1.77.0`](https://github.com/pydantic/pydantic-ai/releases/tag/v1.77.0) — 4 days ago
- **Google ADK** [`v1.28.1`](https://github.com/google/adk-python/releases/tag/v1.28.1) — 4 days ago
- **Agno** [`v2.5.14`](https://github.com/agno-agi/agno/releases/tag/v2.5.14) — 4 days ago

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

*Powered by GitHub Actions • Data refreshed daily • Last run: 2026-04-07 07:27 UTC*