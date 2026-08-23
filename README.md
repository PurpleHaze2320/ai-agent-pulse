# 🔬 AI Agent Framework Pulse Tracker

[![Daily Update](https://github.com/PurpleHaze2320/ai-agent-pulse/actions/workflows/track.yml/badge.svg)](https://github.com/PurpleHaze2320/ai-agent-pulse/actions/workflows/track.yml)
[![Frameworks Tracked](https://img.shields.io/badge/frameworks-19-blue)](https://github.com/PurpleHaze2320/ai-agent-pulse)
[![License: MIT](https://img.shields.io/badge/License-MIT-green.svg)](https://opensource.org/licenses/MIT)
[![GitHub stars](https://img.shields.io/github/stars/PurpleHaze2320/ai-agent-pulse?style=social)](https://github.com/PurpleHaze2320/ai-agent-pulse/stargazers)

> Automated daily tracking of the AI agent framework ecosystem's health, momentum, and trends.
> Last updated: **2026-08-23 06:49 UTC** | Tracking **19** frameworks

## How It Works

This bot runs daily via GitHub Actions and collects metrics from the GitHub API for the most important
AI agent frameworks. It computes a **Pulse Score** (0-100) based on six weighted signals: star velocity,
release freshness, issue health, commit activity, community size, and fork engagement. The result is
a living dashboard that shows which frameworks are gaining momentum and which are losing steam.

## 🏆 Pulse Leaderboard

| Rank | Framework | Pulse | Stars | ⭐ 7d | Commits (4w) | Last Release | Category |
|------|-----------|-------|-------|-------|--------------|--------------|----------|
| 1 | [BrowserUse](https://github.com/browser-use/browser-use) | 🟢 **89.7** | 110.2k | 🚀 +811 | 105 | 6 days ago | `web-agent` |
| 2 | [CrewAI](https://github.com/crewAIInc/crewAI) | 🟢 **83.3** | 57.5k | 🚀 +349 | 102 | 3 days ago | `multi-agent` |
| 3 | [OpenAI Agents SDK](https://github.com/openai/openai-agents-python) | 🟢 **78.3** | 28.9k | 🚀 +211 | 308 | 3 days ago | `orchestration` |
| 4 | [Mastra](https://github.com/mastra-ai/mastra) | 🟢 **75.9** | 27.4k | 🚀 +153 | 1387 | 3 days ago | `typescript` |
| 5 | [LangGraph](https://github.com/langchain-ai/langgraph) | 🟢 **74.5** | 40.3k | 🚀 +498 | 35 | 3 days ago | `orchestration` |
| 6 | [PydanticAI](https://github.com/pydantic/pydantic-ai) | 🟢 **73.8** | 19.4k | 🚀 +122 | 278 | 2 days ago | `structured` |
| 7 | [Google ADK](https://github.com/google/adk-python) | 🟢 **73.8** | 21.2k | 🚀 +102 | 346 | 5 days ago | `orchestration` |
| 8 | [Haystack](https://github.com/deepset-ai/haystack) | 🟢 **71.1** | 26.3k | 📈 +67 | 202 | 1 day ago | `pipeline` |
| 9 | [DSPy](https://github.com/stanfordnlp/dspy) | 🟡 **69.9** | 37.5k | 🚀 +262 | 63 | 1 day ago | `optimization` |
| 10 | [Claude Agent SDK](https://github.com/anthropics/claude-code) | 🟡 **69.0** | 142.6k | 🚀 +1040 | 20 | today | `orchestration` |
| 11 | [Composio](https://github.com/ComposioHQ/composio) | 🟡 **68.8** | 29.8k | 🚀 +135 | 337 | 2 days ago | `tooling` |
| 12 | [LlamaIndex](https://github.com/run-llama/llama_index) | 🟡 **63.4** | 51.8k | 🚀 +140 | 28 | 3 days ago | `data-agent` |
| 13 | [AG2](https://github.com/ag2ai/ag2) | 🟡 **62.8** | 4.9k | ↗️ +20 | 66 | 8 days ago | `multi-agent` |
| 14 | [Agno](https://github.com/agno-agi/agno) | 🟡 **61.6** | 41.8k | 🚀 +110 | 51 | 1 day ago | `multi-agent` |
| 15 | [Semantic Kernel](https://github.com/microsoft/semantic-kernel) | 🟡 **54.3** | 28.5k | 📈 +25 | 19 | 4 days ago | `enterprise` |
| 16 | [Letta](https://github.com/letta-ai/letta) | 🟡 **40.8** | 24.4k | 📈 +94 | 4 | 3 mo ago | `memory` |
| 17 | [Smolagents](https://github.com/huggingface/smolagents) | 🟠 **38.0** | 28.9k | 🚀 +114 | 2 | 2 mo ago | `lightweight` |
| 18 | [AutoGen](https://github.com/microsoft/autogen) | 🟠 **34.5** | 60.6k | 🚀 +138 | 0 | 10 mo ago | `multi-agent` |
| 19 | [Swarm](https://github.com/openai/swarm) | 🔴 **9.3** | 21.9k | ↗️ +12 | 0 | — | `experimental` |

## 📂 By Category

- `data-agent`: **LlamaIndex** (63.4)
- `enterprise`: **Semantic Kernel** (54.3)
- `experimental`: **Swarm** (9.3)
- `lightweight`: **Smolagents** (38.0)
- `memory`: **Letta** (40.8)
- `multi-agent`: **CrewAI** (83.3), **AG2** (62.8), **Agno** (61.6), **AutoGen** (34.5)
- `optimization`: **DSPy** (69.9)
- `orchestration`: **OpenAI Agents SDK** (78.3), **LangGraph** (74.5), **Google ADK** (73.8), **Claude Agent SDK** (69.0)
- `pipeline`: **Haystack** (71.1)
- `structured`: **PydanticAI** (73.8)
- `tooling`: **Composio** (68.8)
- `typescript`: **Mastra** (75.9)
- `web-agent`: **BrowserUse** (89.7)

## 🔍 Top 5 — Score Breakdown

| Framework | Star Velocity | Release Freshness | Issue Health | Commit Activity | Community | Fork Ratio |
|-----------|:---:|:---:|:---:|:---:|:---:|:---:|
| **BrowserUse** | 100 | 98.0 | 93.4 | 100 | 67.0 | 44.0 |
| **CrewAI** | 70.3 | 99.0 | 94.7 | 100 | 60.2 | 57.1 |
| **OpenAI Agents SDK** | 40.6 | 99.0 | 99.4 | 100 | 71.4 | 63.2 |
| **Mastra** | 34.2 | 99.0 | 95.6 | 100 | 93.0 | 39.1 |
| **LangGraph** | 100 | 99.0 | 69.2 | 35.0 | 55.6 | 67.3 |

## 💡 Key Insights

- **Hottest framework**: BrowserUse with a Pulse Score of 89.7
- **Fastest growing**: Claude Agent SDK gained +1040 stars this week
- **Most active development**: Mastra with 1387 commits in the last 4 weeks
- **Stale releases**: AutoGen, Swarm haven't released in a while

## 📦 Recent Releases

- **Claude Agent SDK** [`v2.1.241`](https://github.com/anthropics/claude-code/releases/tag/v2.1.241) — today
- **Agno** [`v3.0.0a3`](https://github.com/agno-agi/agno/releases/tag/v3.0.0a3) — 1 day ago *(pre-release)*
- **DSPy** [`3.3.1`](https://github.com/stanfordnlp/dspy/releases/tag/3.3.1) — 1 day ago
- **Haystack** [`v3.1.0-rc3`](https://github.com/deepset-ai/haystack/releases/tag/v3.1.0-rc3) — 1 day ago *(pre-release)*
- **PydanticAI** [`v2.33.0`](https://github.com/pydantic/pydantic-ai/releases/tag/v2.33.0) — 2 days ago
- **Composio** [`@composio/cli@0.3.4-beta.360`](https://github.com/ComposioHQ/composio/releases/tag/@composio/cli@0.3.4-beta.360) — 2 days ago *(pre-release)*
- **CrewAI** [`1.15.17`](https://github.com/crewAIInc/crewAI/releases/tag/1.15.17) — 3 days ago
- **LlamaIndex** [`v0.14.24`](https://github.com/run-llama/llama_index/releases/tag/v0.14.24) — 3 days ago
- **LangGraph** [`sdk==0.4.3`](https://github.com/langchain-ai/langgraph/releases/tag/sdk==0.4.3) — 3 days ago
- **Mastra** [`@mastra/core@1.60.0`](https://github.com/mastra-ai/mastra/releases/tag/@mastra/core@1.60.0) — 3 days ago

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

*Powered by GitHub Actions • Data refreshed daily • Last run: 2026-08-23 06:49 UTC*