# 🔬 AI Agent Framework Pulse Tracker

[![Daily Update](https://github.com/PurpleHaze2320/ai-agent-pulse/actions/workflows/track.yml/badge.svg)](https://github.com/PurpleHaze2320/ai-agent-pulse/actions/workflows/track.yml)
[![Frameworks Tracked](https://img.shields.io/badge/frameworks-19-blue)](https://github.com/PurpleHaze2320/ai-agent-pulse)
[![License: MIT](https://img.shields.io/badge/License-MIT-green.svg)](https://opensource.org/licenses/MIT)
[![GitHub stars](https://img.shields.io/github/stars/PurpleHaze2320/ai-agent-pulse?style=social)](https://github.com/PurpleHaze2320/ai-agent-pulse/stargazers)

> Automated daily tracking of the AI agent framework ecosystem's health, momentum, and trends.
> Last updated: **2026-09-01 11:24 UTC** | Tracking **19** frameworks

## How It Works

This bot runs daily via GitHub Actions and collects metrics from the GitHub API for the most important
AI agent frameworks. It computes a **Pulse Score** (0-100) based on six weighted signals: star velocity,
release freshness, issue health, commit activity, community size, and fork engagement. The result is
a living dashboard that shows which frameworks are gaining momentum and which are losing steam.

## 🏆 Pulse Leaderboard

| Rank | Framework | Pulse | Stars | ⭐ 7d | Commits (4w) | Last Release | Category |
|------|-----------|-------|-------|-------|--------------|--------------|----------|
| 1 | [BrowserUse](https://github.com/browser-use/browser-use) | 🟢 **89.3** | 111.9k | 🚀 +1501 | 136 | 15 days ago | `web-agent` |
| 2 | [CrewAI](https://github.com/crewAIInc/crewAI) | 🟢 **79.1** | 57.9k | 🚀 +360 | 75 | 4 days ago | `multi-agent` |
| 3 | [OpenAI Agents SDK](https://github.com/openai/openai-agents-python) | 🟢 **76.9** | 29.1k | 🚀 +176 | 201 | 12 days ago | `orchestration` |
| 4 | [Mastra](https://github.com/mastra-ai/mastra) | 🟢 **75.7** | 27.6k | 🚀 +160 | 1242 | 4 days ago | `typescript` |
| 5 | [PydanticAI](https://github.com/pydantic/pydantic-ai) | 🟢 **75.0** | 19.6k | 🚀 +154 | 200 | today | `structured` |
| 6 | [Google ADK](https://github.com/google/adk-python) | 🟢 **73.6** | 21.4k | 📈 +88 | 410 | 4 days ago | `orchestration` |
| 7 | [Claude Agent SDK](https://github.com/anthropics/claude-code) | 🟡 **69.6** | 143.6k | 🚀 +717 | 23 | today | `orchestration` |
| 8 | [Composio](https://github.com/ComposioHQ/composio) | 🟡 **68.6** | 30.0k | 🚀 +126 | 209 | 1 day ago | `tooling` |
| 9 | [LangGraph](https://github.com/langchain-ai/langgraph) | 🟡 **68.3** | 40.8k | 🚀 +444 | 11 | 4 days ago | `orchestration` |
| 10 | [Agno](https://github.com/agno-agi/agno) | 🟡 **64.8** | 42.0k | 🚀 +104 | 67 | today | `multi-agent` |
| 11 | [DSPy](https://github.com/stanfordnlp/dspy) | 🟡 **64.2** | 37.7k | 🚀 +127 | 61 | 10 days ago | `optimization` |
| 12 | [LlamaIndex](https://github.com/run-llama/llama_index) | 🟡 **62.2** | 52.0k | 🚀 +102 | 33 | 12 days ago | `data-agent` |
| 13 | [Semantic Kernel](https://github.com/microsoft/semantic-kernel) | 🟡 **53.1** | 28.5k | 📈 +25 | 16 | 13 days ago | `enterprise` |
| 14 | [Haystack](https://github.com/deepset-ai/haystack) | 🟡 **51.2** | 26.4k | 📈 +75 | 0 | 7 days ago | `pipeline` |
| 15 | [AG2](https://github.com/ag2ai/ag2) | 🟡 **49.7** | 4.9k | ↗️ +15 | 0 | 3 days ago | `multi-agent` |
| 16 | [Letta](https://github.com/letta-ai/letta) | 🟡 **40.5** | 24.5k | 📈 +100 | 3 | 3 mo ago | `memory` |
| 17 | [Smolagents](https://github.com/huggingface/smolagents) | 🟠 **37.6** | 29.1k | 🚀 +119 | 2 | 3 mo ago | `lightweight` |
| 18 | [AutoGen](https://github.com/microsoft/autogen) | 🟠 **33.5** | 60.7k | 🚀 +118 | 0 | 11 mo ago | `multi-agent` |
| 19 | [Swarm](https://github.com/openai/swarm) | 🔴 **9.2** | 21.9k | ↗️ +12 | 0 | — | `experimental` |

## 📂 By Category

- `data-agent`: **LlamaIndex** (62.2)
- `enterprise`: **Semantic Kernel** (53.1)
- `experimental`: **Swarm** (9.2)
- `lightweight`: **Smolagents** (37.6)
- `memory`: **Letta** (40.5)
- `multi-agent`: **CrewAI** (79.1), **Agno** (64.8), **AG2** (49.7), **AutoGen** (33.5)
- `optimization`: **DSPy** (64.2)
- `orchestration`: **OpenAI Agents SDK** (76.9), **Google ADK** (73.6), **Claude Agent SDK** (69.6), **LangGraph** (68.3)
- `pipeline`: **Haystack** (51.2)
- `structured`: **PydanticAI** (75.0)
- `tooling`: **Composio** (68.6)
- `typescript`: **Mastra** (75.7)
- `web-agent`: **BrowserUse** (89.3)

## 🔍 Top 5 — Score Breakdown

| Framework | Star Velocity | Release Freshness | Issue Health | Commit Activity | Community | Fork Ratio |
|-----------|:---:|:---:|:---:|:---:|:---:|:---:|
| **BrowserUse** | 100 | 95.0 | 92.6 | 100 | 70.2 | 43.9 |
| **CrewAI** | 72.1 | 98.7 | 96.9 | 75.0 | 60.4 | 57.3 |
| **OpenAI Agents SDK** | 36.3 | 96.0 | 99.0 | 100 | 73.6 | 63.9 |
| **Mastra** | 34.2 | 98.7 | 94.7 | 100 | 93.0 | 39.4 |
| **PydanticAI** | 31.5 | 100.0 | 81.6 | 100 | 95.0 | 53.4 |

## 💡 Key Insights

- **Hottest framework**: BrowserUse with a Pulse Score of 89.3
- **Fastest growing**: BrowserUse gained +1501 stars this week
- **Most active development**: Mastra with 1242 commits in the last 4 weeks
- **Stale releases**: AutoGen, Swarm haven't released in a while

## 📦 Recent Releases

- **Agno** [`v3.0.5`](https://github.com/agno-agi/agno/releases/tag/v3.0.5) — today
- **PydanticAI** [`v2.37.0`](https://github.com/pydantic/pydantic-ai/releases/tag/v2.37.0) — today
- **Claude Agent SDK** [`v2.1.252`](https://github.com/anthropics/claude-code/releases/tag/v2.1.252) — today
- **Composio** [`@composio/cli@0.4.1-beta.373`](https://github.com/ComposioHQ/composio/releases/tag/@composio/cli@0.4.1-beta.373) — 1 day ago *(pre-release)*
- **AG2** [`v1.0.3`](https://github.com/ag2ai/ag2/releases/tag/v1.0.3) — 3 days ago
- **Mastra** [`@mastra/core@1.63.0`](https://github.com/mastra-ai/mastra/releases/tag/@mastra/core@1.63.0) — 4 days ago
- **Google ADK** [`v1.39.1`](https://github.com/google/adk-python/releases/tag/v1.39.1) — 4 days ago
- **LangGraph** [`sdk==0.4.4`](https://github.com/langchain-ai/langgraph/releases/tag/sdk==0.4.4) — 4 days ago
- **CrewAI** [`1.15.18`](https://github.com/crewAIInc/crewAI/releases/tag/1.15.18) — 4 days ago
- **Haystack** [`v3.1.0`](https://github.com/deepset-ai/haystack/releases/tag/v3.1.0) — 7 days ago

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

*Powered by GitHub Actions • Data refreshed daily • Last run: 2026-09-01 11:24 UTC*