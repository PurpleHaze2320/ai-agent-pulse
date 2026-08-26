# 🔬 AI Agent Framework Pulse Tracker

[![Daily Update](https://github.com/PurpleHaze2320/ai-agent-pulse/actions/workflows/track.yml/badge.svg)](https://github.com/PurpleHaze2320/ai-agent-pulse/actions/workflows/track.yml)
[![Frameworks Tracked](https://img.shields.io/badge/frameworks-19-blue)](https://github.com/PurpleHaze2320/ai-agent-pulse)
[![License: MIT](https://img.shields.io/badge/License-MIT-green.svg)](https://opensource.org/licenses/MIT)
[![GitHub stars](https://img.shields.io/github/stars/PurpleHaze2320/ai-agent-pulse?style=social)](https://github.com/PurpleHaze2320/ai-agent-pulse/stargazers)

> Automated daily tracking of the AI agent framework ecosystem's health, momentum, and trends.
> Last updated: **2026-08-26 06:57 UTC** | Tracking **19** frameworks

## How It Works

This bot runs daily via GitHub Actions and collects metrics from the GitHub API for the most important
AI agent frameworks. It computes a **Pulse Score** (0-100) based on six weighted signals: star velocity,
release freshness, issue health, commit activity, community size, and fork engagement. The result is
a living dashboard that shows which frameworks are gaining momentum and which are losing steam.

## 🏆 Pulse Leaderboard

| Rank | Framework | Pulse | Stars | ⭐ 7d | Commits (4w) | Last Release | Category |
|------|-----------|-------|-------|-------|--------------|--------------|----------|
| 1 | [BrowserUse](https://github.com/browser-use/browser-use) | 🟢 **89.5** | 110.6k | 🚀 +874 | 113 | 9 days ago | `web-agent` |
| 2 | [CrewAI](https://github.com/crewAIInc/crewAI) | 🟢 **79.8** | 57.6k | 🚀 +322 | 88 | 6 days ago | `multi-agent` |
| 3 | [OpenAI Agents SDK](https://github.com/openai/openai-agents-python) | 🟢 **78.3** | 29.0k | 🚀 +211 | 333 | 6 days ago | `orchestration` |
| 4 | [Mastra](https://github.com/mastra-ai/mastra) | 🟢 **77.3** | 27.5k | 🚀 +186 | 1627 | 1 day ago | `typescript` |
| 5 | [Google ADK](https://github.com/google/adk-python) | 🟢 **74.0** | 21.3k | 🚀 +109 | 405 | 8 days ago | `orchestration` |
| 6 | [PydanticAI](https://github.com/pydantic/pydantic-ai) | 🟢 **73.9** | 19.5k | 🚀 +121 | 209 | today | `structured` |
| 7 | [LangGraph](https://github.com/langchain-ai/langgraph) | 🟢 **73.6** | 40.5k | 🚀 +481 | 32 | 6 days ago | `orchestration` |
| 8 | [Claude Agent SDK](https://github.com/anthropics/claude-code) | 🟡 **69.8** | 143.0k | 🚀 +1100 | 24 | today | `orchestration` |
| 9 | [Composio](https://github.com/ComposioHQ/composio) | 🟡 **68.1** | 29.9k | 🚀 +113 | 288 | today | `tooling` |
| 10 | [DSPy](https://github.com/stanfordnlp/dspy) | 🟡 **65.6** | 37.6k | 🚀 +197 | 54 | 4 days ago | `optimization` |
| 11 | [LlamaIndex](https://github.com/run-llama/llama_index) | 🟡 **62.6** | 51.9k | 🚀 +136 | 26 | 6 days ago | `data-agent` |
| 12 | [AG2](https://github.com/ag2ai/ag2) | 🟡 **59.6** | 4.9k | ↗️ +15 | 52 | 11 days ago | `multi-agent` |
| 13 | [Agno](https://github.com/agno-agi/agno) | 🟡 **53.1** | 41.9k | 🚀 +154 | 0 | 1 day ago | `multi-agent` |
| 14 | [Semantic Kernel](https://github.com/microsoft/semantic-kernel) | 🟡 **52.7** | 28.5k | 📈 +38 | 10 | 7 days ago | `enterprise` |
| 15 | [Haystack](https://github.com/deepset-ai/haystack) | 🟡 **51.2** | 26.3k | 📈 +68 | 0 | 1 day ago | `pipeline` |
| 16 | [Letta](https://github.com/letta-ai/letta) | 🟡 **42.3** | 24.4k | 🚀 +143 | 3 | 3 mo ago | `memory` |
| 17 | [Smolagents](https://github.com/huggingface/smolagents) | 🟠 **38.1** | 29.0k | 🚀 +123 | 2 | 2 mo ago | `lightweight` |
| 18 | [AutoGen](https://github.com/microsoft/autogen) | 🟠 **33.9** | 60.6k | 🚀 +127 | 0 | 11 mo ago | `multi-agent` |
| 19 | [Swarm](https://github.com/openai/swarm) | 🔴 **9.2** | 21.9k | ↗️ +12 | 0 | — | `experimental` |

## 📂 By Category

- `data-agent`: **LlamaIndex** (62.6)
- `enterprise`: **Semantic Kernel** (52.7)
- `experimental`: **Swarm** (9.2)
- `lightweight`: **Smolagents** (38.1)
- `memory`: **Letta** (42.3)
- `multi-agent`: **CrewAI** (79.8), **AG2** (59.6), **Agno** (53.1), **AutoGen** (33.9)
- `optimization`: **DSPy** (65.6)
- `orchestration`: **OpenAI Agents SDK** (78.3), **Google ADK** (74.0), **LangGraph** (73.6), **Claude Agent SDK** (69.8)
- `pipeline`: **Haystack** (51.2)
- `structured`: **PydanticAI** (73.9)
- `tooling`: **Composio** (68.1)
- `typescript`: **Mastra** (77.3)
- `web-agent`: **BrowserUse** (89.5)

## 🔍 Top 5 — Score Breakdown

| Framework | Star Velocity | Release Freshness | Issue Health | Commit Activity | Community | Fork Ratio |
|-----------|:---:|:---:|:---:|:---:|:---:|:---:|
| **BrowserUse** | 100 | 97.0 | 93.1 | 100 | 67.2 | 44.0 |
| **CrewAI** | 66.2 | 98.0 | 95.3 | 88.0 | 60.2 | 57.3 |
| **OpenAI Agents SDK** | 41.0 | 98.0 | 99.2 | 100 | 72.6 | 63.5 |
| **Mastra** | 39.1 | 99.7 | 96.1 | 100 | 93.0 | 39.2 |
| **Google ADK** | 21.1 | 97.3 | 90.3 | 100 | 83.6 | 73.2 |

## 💡 Key Insights

- **Hottest framework**: BrowserUse with a Pulse Score of 89.5
- **Fastest growing**: Claude Agent SDK gained +1100 stars this week
- **Most active development**: Mastra with 1627 commits in the last 4 weeks
- **Stale releases**: AutoGen, Swarm haven't released in a while

## 📦 Recent Releases

- **PydanticAI** [`v2.35.0`](https://github.com/pydantic/pydantic-ai/releases/tag/v2.35.0) — today
- **Claude Agent SDK** [`v2.1.246`](https://github.com/anthropics/claude-code/releases/tag/v2.1.246) — today
- **Composio** [`@composio/cli@0.4.1-beta.369`](https://github.com/ComposioHQ/composio/releases/tag/@composio/cli@0.4.1-beta.369) — today *(pre-release)*
- **Haystack** [`v3.1.0`](https://github.com/deepset-ai/haystack/releases/tag/v3.1.0) — 1 day ago
- **Agno** [`v3.0.0`](https://github.com/agno-agi/agno/releases/tag/v3.0.0) — 1 day ago
- **Mastra** [`@mastra/core@1.61.0`](https://github.com/mastra-ai/mastra/releases/tag/@mastra/core@1.61.0) — 1 day ago
- **DSPy** [`3.3.1`](https://github.com/stanfordnlp/dspy/releases/tag/3.3.1) — 4 days ago
- **CrewAI** [`1.15.17`](https://github.com/crewAIInc/crewAI/releases/tag/1.15.17) — 6 days ago
- **LlamaIndex** [`v0.14.24`](https://github.com/run-llama/llama_index/releases/tag/v0.14.24) — 6 days ago
- **LangGraph** [`sdk==0.4.3`](https://github.com/langchain-ai/langgraph/releases/tag/sdk==0.4.3) — 6 days ago

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

*Powered by GitHub Actions • Data refreshed daily • Last run: 2026-08-26 06:57 UTC*