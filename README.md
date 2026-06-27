# 🔬 AI Agent Framework Pulse Tracker

[![Daily Update](https://github.com/PurpleHaze2320/ai-agent-pulse/actions/workflows/track.yml/badge.svg)](https://github.com/PurpleHaze2320/ai-agent-pulse/actions/workflows/track.yml)
[![Frameworks Tracked](https://img.shields.io/badge/frameworks-19-blue)](https://github.com/PurpleHaze2320/ai-agent-pulse)
[![License: MIT](https://img.shields.io/badge/License-MIT-green.svg)](https://opensource.org/licenses/MIT)
[![GitHub stars](https://img.shields.io/github/stars/PurpleHaze2320/ai-agent-pulse?style=social)](https://github.com/PurpleHaze2320/ai-agent-pulse/stargazers)

> Automated daily tracking of the AI agent framework ecosystem's health, momentum, and trends.
> Last updated: **2026-06-27 08:43 UTC** | Tracking **19** frameworks

## How It Works

This bot runs daily via GitHub Actions and collects metrics from the GitHub API for the most important
AI agent frameworks. It computes a **Pulse Score** (0-100) based on six weighted signals: star velocity,
release freshness, issue health, commit activity, community size, and fork engagement. The result is
a living dashboard that shows which frameworks are gaining momentum and which are losing steam.

## 🏆 Pulse Leaderboard

| Rank | Framework | Pulse | Stars | ⭐ 7d | Commits (4w) | Last Release | Category |
|------|-----------|-------|-------|-------|--------------|--------------|----------|
| 1 | [Mastra](https://github.com/mastra-ai/mastra) | 🟢 **79.0** | 25.5k | 🚀 +230 | 1031 | 2 days ago | `typescript` |
| 2 | [Claude Agent SDK](https://github.com/anthropics/claude-code) | 🟢 **72.1** | 134.6k | 🚀 +1230 | 32 | today | `orchestration` |
| 3 | [Google ADK](https://github.com/google/adk-python) | 🟢 **71.9** | 20.3k | 🚀 +118 | 324 | 8 days ago | `orchestration` |
| 4 | [Agno](https://github.com/agno-agi/agno) | 🟢 **71.1** | 40.9k | 📈 +88 | 114 | 3 days ago | `multi-agent` |
| 5 | [BrowserUse](https://github.com/browser-use/browser-use) | 🟡 **69.1** | 100.9k | 🚀 +1232 | 0 | 14 days ago | `web-agent` |
| 6 | [CrewAI](https://github.com/crewAIInc/crewAI) | 🟡 **68.9** | 54.4k | 🚀 +430 | 0 | today | `multi-agent` |
| 7 | [LangGraph](https://github.com/langchain-ai/langgraph) | 🟡 **67.8** | 35.9k | 🚀 +609 | 0 | 8 days ago | `orchestration` |
| 8 | [Composio](https://github.com/ComposioHQ/composio) | 🟡 **67.7** | 29.0k | 🚀 +111 | 121 | today | `tooling` |
| 9 | [OpenAI Agents SDK](https://github.com/openai/openai-agents-python) | 🟡 **66.1** | 27.5k | 🚀 +187 | 52 | 3 days ago | `orchestration` |
| 10 | [LlamaIndex](https://github.com/run-llama/llama_index) | 🟡 **62.4** | 50.4k | 🚀 +207 | 12 | 2 days ago | `data-agent` |
| 11 | [PydanticAI](https://github.com/pydantic/pydantic-ai) | 🟡 **54.7** | 18.0k | 🚀 +156 | 0 | 3 days ago | `structured` |
| 12 | [DSPy](https://github.com/stanfordnlp/dspy) | 🟡 **54.3** | 35.4k | 🚀 +280 | 0 | 1 mo ago | `optimization` |
| 13 | [Haystack](https://github.com/deepset-ai/haystack) | 🟡 **52.2** | 25.8k | 🚀 +135 | 0 | 9 days ago | `pipeline` |
| 14 | [Semantic Kernel](https://github.com/microsoft/semantic-kernel) | 🟡 **50.4** | 28.2k | 📈 +34 | 0 | 10 days ago | `enterprise` |
| 15 | [AG2](https://github.com/ag2ai/ag2) | 🟡 **50.1** | 4.7k | ↗️ +18 | 0 | 1 day ago | `multi-agent` |
| 16 | [Letta](https://github.com/letta-ai/letta) | 🟡 **44.9** | 23.5k | 🚀 +122 | 0 | 1 mo ago | `memory` |
| 17 | [Smolagents](https://github.com/huggingface/smolagents) | 🟡 **42.0** | 28.0k | 🚀 +107 | 2 | 29 days ago | `lightweight` |
| 18 | [AutoGen](https://github.com/microsoft/autogen) | 🟠 **39.4** | 59.3k | 🚀 +203 | 0 | 9 mo ago | `multi-agent` |
| 19 | [Swarm](https://github.com/openai/swarm) | 🔴 **10.9** | 21.7k | 📈 +82 | 0 | — | `experimental` |

## 📂 By Category

- `data-agent`: **LlamaIndex** (62.4)
- `enterprise`: **Semantic Kernel** (50.4)
- `experimental`: **Swarm** (10.9)
- `lightweight`: **Smolagents** (42.0)
- `memory`: **Letta** (44.9)
- `multi-agent`: **Agno** (71.1), **CrewAI** (68.9), **AG2** (50.1), **AutoGen** (39.4)
- `optimization`: **DSPy** (54.3)
- `orchestration`: **Claude Agent SDK** (72.1), **Google ADK** (71.9), **LangGraph** (67.8), **OpenAI Agents SDK** (66.1)
- `pipeline`: **Haystack** (52.2)
- `structured`: **PydanticAI** (54.7)
- `tooling`: **Composio** (67.7)
- `typescript`: **Mastra** (79.0)
- `web-agent`: **BrowserUse** (69.1)

## 🔍 Top 5 — Score Breakdown

| Framework | Star Velocity | Release Freshness | Issue Health | Commit Activity | Community | Fork Ratio |
|-----------|:---:|:---:|:---:|:---:|:---:|:---:|
| **Mastra** | 47.9 | 99.3 | 95.5 | 100 | 92.2 | 36.0 |
| **Claude Agent SDK** | 100 | 100.0 | 87.8 | 32.0 | 10.4 | 64.6 |
| **Google ADK** | 22.7 | 97.3 | 85.3 | 100 | 68.2 | 71.3 |
| **Agno** | 19.3 | 99.0 | 81.0 | 100 | 88.8 | 54.5 |
| **BrowserUse** | 100 | 95.3 | 95.4 | 0.0 | 63.0 | 44.5 |

## 💡 Key Insights

- **Hottest framework**: Mastra with a Pulse Score of 79.0
- **Fastest growing**: BrowserUse gained +1232 stars this week
- **Most active development**: Mastra with 1031 commits in the last 4 weeks
- **Stale releases**: Swarm haven't released in a while

## 📦 Recent Releases

- **Composio** [`@composio/slim@0.13.1`](https://github.com/ComposioHQ/composio/releases/tag/@composio/slim@0.13.1) — today
- **CrewAI** [`1.15.1`](https://github.com/crewAIInc/crewAI/releases/tag/1.15.1) — today
- **Claude Agent SDK** [`v2.1.195`](https://github.com/anthropics/claude-code/releases/tag/v2.1.195) — today
- **AG2** [`v0.14.0`](https://github.com/ag2ai/ag2/releases/tag/v0.14.0) — 1 day ago
- **LlamaIndex** [`v0.14.23`](https://github.com/run-llama/llama_index/releases/tag/v0.14.23) — 2 days ago
- **Mastra** [`@mastra/core@1.46.0`](https://github.com/mastra-ai/mastra/releases/tag/@mastra/core@1.46.0) — 2 days ago
- **OpenAI Agents SDK** [`v0.17.7`](https://github.com/openai/openai-agents-python/releases/tag/v0.17.7) — 3 days ago
- **PydanticAI** [`v2.0.0`](https://github.com/pydantic/pydantic-ai/releases/tag/v2.0.0) — 3 days ago
- **Agno** [`v2.6.19`](https://github.com/agno-agi/agno/releases/tag/v2.6.19) — 3 days ago
- **LangGraph** [`1.2.6`](https://github.com/langchain-ai/langgraph/releases/tag/1.2.6) — 8 days ago

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

*Powered by GitHub Actions • Data refreshed daily • Last run: 2026-06-27 08:43 UTC*