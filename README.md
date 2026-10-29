# 🔬 AI Agent Framework Pulse Tracker

[![Daily Update](https://github.com/PurpleHaze2320/ai-agent-pulse/actions/workflows/track.yml/badge.svg)](https://github.com/PurpleHaze2320/ai-agent-pulse/actions/workflows/track.yml)
[![Frameworks Tracked](https://img.shields.io/badge/frameworks-19-blue)](https://github.com/PurpleHaze2320/ai-agent-pulse)
[![License: MIT](https://img.shields.io/badge/License-MIT-green.svg)](https://opensource.org/licenses/MIT)
[![GitHub stars](https://img.shields.io/github/stars/PurpleHaze2320/ai-agent-pulse?style=social)](https://github.com/PurpleHaze2320/ai-agent-pulse/stargazers)

> Automated daily tracking of the AI agent framework ecosystem's health, momentum, and trends.
> Last updated: **2026-10-29 12:38 UTC** | Tracking **19** frameworks

## How It Works

This bot runs daily via GitHub Actions and collects metrics from the GitHub API for the most important
AI agent frameworks. It computes a **Pulse Score** (0-100) based on six weighted signals: star velocity,
release freshness, issue health, commit activity, community size, and fork engagement. The result is
a living dashboard that shows which frameworks are gaining momentum and which are losing steam.

## 🏆 Pulse Leaderboard

| Rank | Framework | Pulse | Stars | ⭐ 7d | Commits (4w) | Last Release | Category |
|------|-----------|-------|-------|-------|--------------|--------------|----------|
| 1 | [BrowserUse](https://github.com/browser-use/browser-use) | 🟢 **89.9** | 119.5k | 🚀 +616 | 116 | 2 days ago | `web-agent` |
| 2 | [LangGraph](https://github.com/langchain-ai/langgraph) | 🟢 **83.7** | 44.1k | 🚀 +377 | 121 | 2 days ago | `orchestration` |
| 3 | [CrewAI](https://github.com/crewAIInc/crewAI) | 🟢 **79.5** | 60.2k | 🚀 +267 | 184 | today | `multi-agent` |
| 4 | [Mastra](https://github.com/mastra-ai/mastra) | 🟢 **76.9** | 29.2k | 🚀 +180 | 2279 | today | `typescript` |
| 5 | [Claude Agent SDK](https://github.com/anthropics/claude-code) | 🟢 **74.8** | 153.8k | 🚀 +976 | 46 | 1 day ago | `orchestration` |
| 6 | [Google ADK](https://github.com/google/adk-python) | 🟢 **74.3** | 22.0k | 📈 +79 | 480 | 5 days ago | `orchestration` |
| 7 | [OpenAI Agents SDK](https://github.com/openai/openai-agents-python) | 🟢 **73.1** | 30.4k | 🚀 +146 | 86 | 14 days ago | `orchestration` |
| 8 | [Haystack](https://github.com/deepset-ai/haystack) | 🟢 **71.5** | 26.9k | 📈 +67 | 231 | 7 days ago | `pipeline` |
| 9 | [Agno](https://github.com/agno-agi/agno) | 🟢 **70.4** | 43.0k | 📈 +89 | 168 | 1 day ago | `multi-agent` |
| 10 | [AG2](https://github.com/ag2ai/ag2) | 🟢 **70.1** | 5.0k | ↗️ +19 | 110 | 1 day ago | `multi-agent` |
| 11 | [Composio](https://github.com/ComposioHQ/composio) | 🟡 **68.8** | 30.8k | 🚀 +129 | 350 | today | `tooling` |
| 12 | [Semantic Kernel](https://github.com/microsoft/semantic-kernel) | 🟡 **64.9** | 28.7k | 📈 +28 | 67 | today | `enterprise` |
| 13 | [DSPy](https://github.com/stanfordnlp/dspy) | 🟡 **62.9** | 38.8k | 🚀 +115 | 72 | 16 days ago | `optimization` |
| 14 | [LlamaIndex](https://github.com/run-llama/llama_index) | 🟡 **54.9** | 52.7k | 🚀 +112 | 9 | 1 mo ago | `data-agent` |
| 15 | [PydanticAI](https://github.com/pydantic/pydantic-ai) | 🟡 **52.9** | 20.9k | 🚀 +155 | 0 | 23 days ago | `structured` |
| 16 | [Smolagents](https://github.com/huggingface/smolagents) | 🟠 **34.2** | 30.1k | 🚀 +151 | 1 | 5 mo ago | `lightweight` |
| 17 | [Letta](https://github.com/letta-ai/letta) | 🟠 **34.2** | 25.3k | 📈 +56 | 1 | 5 mo ago | `memory` |
| 18 | [AutoGen](https://github.com/microsoft/autogen) | 🟠 **32.5** | 61.6k | 📈 +98 | 2 | 1y ago | `multi-agent` |
| 19 | [Swarm](https://github.com/openai/swarm) | 🔴 **9.2** | 22.1k | ↗️ +17 | 0 | — | `experimental` |

## 📂 By Category

- `data-agent`: **LlamaIndex** (54.9)
- `enterprise`: **Semantic Kernel** (64.9)
- `experimental`: **Swarm** (9.2)
- `lightweight`: **Smolagents** (34.2)
- `memory`: **Letta** (34.2)
- `multi-agent`: **CrewAI** (79.5), **Agno** (70.4), **AG2** (70.1), **AutoGen** (32.5)
- `optimization`: **DSPy** (62.9)
- `orchestration`: **LangGraph** (83.7), **Claude Agent SDK** (74.8), **Google ADK** (74.3), **OpenAI Agents SDK** (73.1)
- `pipeline`: **Haystack** (71.5)
- `structured`: **PydanticAI** (52.9)
- `tooling`: **Composio** (68.8)
- `typescript`: **Mastra** (76.9)
- `web-agent`: **BrowserUse** (89.9)

## 🔍 Top 5 — Score Breakdown

| Framework | Star Velocity | Release Freshness | Issue Health | Commit Activity | Community | Fork Ratio |
|-----------|:---:|:---:|:---:|:---:|:---:|:---:|
| **BrowserUse** | 100 | 99.3 | 89.1 | 100 | 72.2 | 44.5 |
| **LangGraph** | 77.2 | 99.3 | 79.2 | 100 | 57.4 | 68.8 |
| **CrewAI** | 53.5 | 100.0 | 85.9 | 100 | 72.6 | 59.4 |
| **Mastra** | 36.7 | 100.0 | 94.6 | 100 | 93.4 | 41.9 |
| **Claude Agent SDK** | 100 | 99.7 | 85.1 | 46.0 | 11.4 | 67.8 |

## 💡 Key Insights

- **Hottest framework**: BrowserUse with a Pulse Score of 89.9
- **Fastest growing**: Claude Agent SDK gained +976 stars this week
- **Most active development**: Mastra with 2279 commits in the last 4 weeks
- **Stale releases**: AutoGen, Swarm haven't released in a while

## 📦 Recent Releases

- **CrewAI** [`1.15.33`](https://github.com/crewAIInc/crewAI/releases/tag/1.15.33) — today
- **Composio** [`@composio/cli@0.5.1-beta.521`](https://github.com/ComposioHQ/composio/releases/tag/@composio/cli@0.5.1-beta.521) — today *(pre-release)*
- **Mastra** [`@mastra/core@1.80.0`](https://github.com/mastra-ai/mastra/releases/tag/@mastra/core@1.80.0) — today
- **Semantic Kernel** [`python-1.46.0`](https://github.com/microsoft/semantic-kernel/releases/tag/python-1.46.0) — today
- **AG2** [`v1.2.2`](https://github.com/ag2ai/ag2/releases/tag/v1.2.2) — 1 day ago
- **Claude Agent SDK** [`v2.1.312`](https://github.com/anthropics/claude-code/releases/tag/v2.1.312) — 1 day ago
- **Agno** [`v3.1.11`](https://github.com/agno-agi/agno/releases/tag/v3.1.11) — 1 day ago
- **BrowserUse** [`0.13.14`](https://github.com/browser-use/browser-use/releases/tag/0.13.14) — 2 days ago
- **LangGraph** [`1.2.18`](https://github.com/langchain-ai/langgraph/releases/tag/1.2.18) — 2 days ago
- **Google ADK** [`v2.13.0`](https://github.com/google/adk-python/releases/tag/v2.13.0) — 5 days ago

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

*Powered by GitHub Actions • Data refreshed daily • Last run: 2026-10-29 12:38 UTC*