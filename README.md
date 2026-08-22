# 🔬 AI Agent Framework Pulse Tracker

[![Daily Update](https://github.com/PurpleHaze2320/ai-agent-pulse/actions/workflows/track.yml/badge.svg)](https://github.com/PurpleHaze2320/ai-agent-pulse/actions/workflows/track.yml)
[![Frameworks Tracked](https://img.shields.io/badge/frameworks-19-blue)](https://github.com/PurpleHaze2320/ai-agent-pulse)
[![License: MIT](https://img.shields.io/badge/License-MIT-green.svg)](https://opensource.org/licenses/MIT)
[![GitHub stars](https://img.shields.io/github/stars/PurpleHaze2320/ai-agent-pulse?style=social)](https://github.com/PurpleHaze2320/ai-agent-pulse/stargazers)

> Automated daily tracking of the AI agent framework ecosystem's health, momentum, and trends.
> Last updated: **2026-08-22 06:48 UTC** | Tracking **19** frameworks

## How It Works

This bot runs daily via GitHub Actions and collects metrics from the GitHub API for the most important
AI agent frameworks. It computes a **Pulse Score** (0-100) based on six weighted signals: star velocity,
release freshness, issue health, commit activity, community size, and fork engagement. The result is
a living dashboard that shows which frameworks are gaining momentum and which are losing steam.

## 🏆 Pulse Leaderboard

| Rank | Framework | Pulse | Stars | ⭐ 7d | Commits (4w) | Last Release | Category |
|------|-----------|-------|-------|-------|--------------|--------------|----------|
| 1 | [BrowserUse](https://github.com/browser-use/browser-use) | 🟢 **89.8** | 110.0k | 🚀 +778 | 118 | 5 days ago | `web-agent` |
| 2 | [CrewAI](https://github.com/crewAIInc/crewAI) | 🟢 **83.8** | 57.4k | 🚀 +360 | 102 | 2 days ago | `multi-agent` |
| 3 | [OpenAI Agents SDK](https://github.com/openai/openai-agents-python) | 🟢 **78.1** | 28.8k | 🚀 +202 | 373 | 2 days ago | `orchestration` |
| 4 | [Mastra](https://github.com/mastra-ai/mastra) | 🟢 **75.9** | 27.4k | 🚀 +149 | 1597 | 2 days ago | `typescript` |
| 5 | [LangGraph](https://github.com/langchain-ai/langgraph) | 🟢 **74.6** | 40.2k | 🚀 +506 | 35 | 2 days ago | `orchestration` |
| 6 | [PydanticAI](https://github.com/pydantic/pydantic-ai) | 🟢 **74.4** | 19.4k | 🚀 +135 | 276 | 1 day ago | `structured` |
| 7 | [Google ADK](https://github.com/google/adk-python) | 🟢 **74.0** | 21.2k | 🚀 +104 | 464 | 4 days ago | `orchestration` |
| 8 | [DSPy](https://github.com/stanfordnlp/dspy) | 🟢 **71.0** | 37.5k | 🚀 +294 | 63 | today | `optimization` |
| 9 | [Haystack](https://github.com/deepset-ai/haystack) | 🟢 **70.9** | 26.3k | 📈 +61 | 202 | today | `pipeline` |
| 10 | [Claude Agent SDK](https://github.com/anthropics/claude-code) | 🟡 **68.6** | 142.3k | 🚀 +834 | 18 | today | `orchestration` |
| 11 | [Composio](https://github.com/ComposioHQ/composio) | 🟡 **68.4** | 29.8k | 🚀 +123 | 336 | 1 day ago | `tooling` |
| 12 | [LlamaIndex](https://github.com/run-llama/llama_index) | 🟡 **63.7** | 51.8k | 🚀 +145 | 28 | 2 days ago | `data-agent` |
| 13 | [AG2](https://github.com/ag2ai/ag2) | 🟡 **63.0** | 4.9k | 📈 +22 | 66 | 7 days ago | `multi-agent` |
| 14 | [Agno](https://github.com/agno-agi/agno) | 🟡 **61.8** | 41.8k | 🚀 +113 | 51 | today | `multi-agent` |
| 15 | [Semantic Kernel](https://github.com/microsoft/semantic-kernel) | 🟡 **54.4** | 28.5k | 📈 +28 | 19 | 3 days ago | `enterprise` |
| 16 | [Letta](https://github.com/letta-ai/letta) | 🟡 **40.8** | 24.3k | 📈 +92 | 4 | 3 mo ago | `memory` |
| 17 | [Smolagents](https://github.com/huggingface/smolagents) | 🟠 **37.7** | 28.9k | 🚀 +114 | 0 | 2 mo ago | `lightweight` |
| 18 | [AutoGen](https://github.com/microsoft/autogen) | 🟠 **34.6** | 60.6k | 🚀 +141 | 0 | 10 mo ago | `multi-agent` |
| 19 | [Swarm](https://github.com/openai/swarm) | 🔴 **9.1** | 21.9k | ↗️ +6 | 0 | — | `experimental` |

## 📂 By Category

- `data-agent`: **LlamaIndex** (63.7)
- `enterprise`: **Semantic Kernel** (54.4)
- `experimental`: **Swarm** (9.1)
- `lightweight`: **Smolagents** (37.7)
- `memory`: **Letta** (40.8)
- `multi-agent`: **CrewAI** (83.8), **AG2** (63.0), **Agno** (61.8), **AutoGen** (34.6)
- `optimization`: **DSPy** (71.0)
- `orchestration`: **OpenAI Agents SDK** (78.1), **LangGraph** (74.6), **Google ADK** (74.0), **Claude Agent SDK** (68.6)
- `pipeline`: **Haystack** (70.9)
- `structured`: **PydanticAI** (74.4)
- `tooling`: **Composio** (68.4)
- `typescript`: **Mastra** (75.9)
- `web-agent`: **BrowserUse** (89.8)

## 🔍 Top 5 — Score Breakdown

| Framework | Star Velocity | Release Freshness | Issue Health | Commit Activity | Community | Fork Ratio |
|-----------|:---:|:---:|:---:|:---:|:---:|:---:|
| **BrowserUse** | 100 | 98.3 | 93.6 | 100 | 67.0 | 44.0 |
| **CrewAI** | 72.2 | 99.3 | 94.7 | 100 | 60.2 | 57.1 |
| **OpenAI Agents SDK** | 39.4 | 99.3 | 99.4 | 100 | 71.4 | 63.1 |
| **Mastra** | 34.2 | 99.3 | 95.1 | 100 | 93.0 | 39.1 |
| **LangGraph** | 100 | 99.3 | 69.3 | 35.0 | 55.6 | 67.3 |

## 💡 Key Insights

- **Hottest framework**: BrowserUse with a Pulse Score of 89.8
- **Fastest growing**: Claude Agent SDK gained +834 stars this week
- **Most active development**: Mastra with 1597 commits in the last 4 weeks
- **Stale releases**: AutoGen, Swarm haven't released in a while

## 📦 Recent Releases

- **Agno** [`v3.0.0a3`](https://github.com/agno-agi/agno/releases/tag/v3.0.0a3) — today *(pre-release)*
- **DSPy** [`3.3.1`](https://github.com/stanfordnlp/dspy/releases/tag/3.3.1) — today
- **Claude Agent SDK** [`v2.1.239`](https://github.com/anthropics/claude-code/releases/tag/v2.1.239) — today
- **Haystack** [`v3.1.0-rc3`](https://github.com/deepset-ai/haystack/releases/tag/v3.1.0-rc3) — today *(pre-release)*
- **PydanticAI** [`v2.33.0`](https://github.com/pydantic/pydantic-ai/releases/tag/v2.33.0) — 1 day ago
- **Composio** [`@composio/cli@0.3.4-beta.360`](https://github.com/ComposioHQ/composio/releases/tag/@composio/cli@0.3.4-beta.360) — 1 day ago *(pre-release)*
- **CrewAI** [`1.15.17`](https://github.com/crewAIInc/crewAI/releases/tag/1.15.17) — 2 days ago
- **LlamaIndex** [`v0.14.24`](https://github.com/run-llama/llama_index/releases/tag/v0.14.24) — 2 days ago
- **LangGraph** [`sdk==0.4.3`](https://github.com/langchain-ai/langgraph/releases/tag/sdk==0.4.3) — 2 days ago
- **Mastra** [`@mastra/core@1.60.0`](https://github.com/mastra-ai/mastra/releases/tag/@mastra/core@1.60.0) — 2 days ago

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

*Powered by GitHub Actions • Data refreshed daily • Last run: 2026-08-22 06:48 UTC*