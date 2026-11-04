# 🔬 AI Agent Framework Pulse Tracker

[![Daily Update](https://github.com/PurpleHaze2320/ai-agent-pulse/actions/workflows/track.yml/badge.svg)](https://github.com/PurpleHaze2320/ai-agent-pulse/actions/workflows/track.yml)
[![Frameworks Tracked](https://img.shields.io/badge/frameworks-19-blue)](https://github.com/PurpleHaze2320/ai-agent-pulse)
[![License: MIT](https://img.shields.io/badge/License-MIT-green.svg)](https://opensource.org/licenses/MIT)
[![GitHub stars](https://img.shields.io/github/stars/PurpleHaze2320/ai-agent-pulse?style=social)](https://github.com/PurpleHaze2320/ai-agent-pulse/stargazers)

> Automated daily tracking of the AI agent framework ecosystem's health, momentum, and trends.
> Last updated: **2026-11-04 14:04 UTC** | Tracking **19** frameworks

## How It Works

This bot runs daily via GitHub Actions and collects metrics from the GitHub API for the most important
AI agent frameworks. It computes a **Pulse Score** (0-100) based on six weighted signals: star velocity,
release freshness, issue health, commit activity, community size, and fork engagement. The result is
a living dashboard that shows which frameworks are gaining momentum and which are losing steam.

## 🏆 Pulse Leaderboard

| Rank | Framework | Pulse | Stars | ⭐ 7d | Commits (4w) | Last Release | Category |
|------|-----------|-------|-------|-------|--------------|--------------|----------|
| 1 | [BrowserUse](https://github.com/browser-use/browser-use) | 🟢 **89.6** | 120.0k | 🚀 +652 | 107 | 8 days ago | `web-agent` |
| 2 | [LangGraph](https://github.com/langchain-ai/langgraph) | 🟢 **85.5** | 44.5k | 🚀 +407 | 113 | today | `orchestration` |
| 3 | [CrewAI](https://github.com/crewAIInc/crewAI) | 🟢 **79.8** | 60.5k | 🚀 +279 | 177 | today | `multi-agent` |
| 4 | [Mastra](https://github.com/mastra-ai/mastra) | 🟢 **76.7** | 29.3k | 🚀 +178 | 2217 | today | `typescript` |
| 5 | [Claude Agent SDK](https://github.com/anthropics/claude-code) | 🟢 **74.5** | 154.5k | 🚀 +829 | 45 | today | `orchestration` |
| 6 | [Google ADK](https://github.com/google/adk-python) | 🟢 **73.8** | 22.1k | 📈 +75 | 451 | 11 days ago | `orchestration` |
| 7 | [PydanticAI](https://github.com/pydantic/pydantic-ai) | 🟢 **72.1** | 21.0k | 📈 +99 | 1162 | today | `structured` |
| 8 | [Haystack](https://github.com/deepset-ai/haystack) | 🟢 **71.7** | 26.9k | 📈 +59 | 193 | 1 day ago | `pipeline` |
| 9 | [Agno](https://github.com/agno-agi/agno) | 🟢 **71.2** | 43.1k | 🚀 +129 | 149 | 6 days ago | `multi-agent` |
| 10 | [AG2](https://github.com/ag2ai/ag2) | 🟢 **70.4** | 5.0k | ↗️ +20 | 124 | today | `multi-agent` |
| 11 | [OpenAI Agents SDK](https://github.com/openai/openai-agents-python) | 🟡 **69.2** | 30.5k | 🚀 +139 | 63 | today | `orchestration` |
| 12 | [Composio](https://github.com/ComposioHQ/composio) | 🟡 **68.6** | 30.9k | 🚀 +123 | 362 | 1 day ago | `tooling` |
| 13 | [Semantic Kernel](https://github.com/microsoft/semantic-kernel) | 🟡 **67.1** | 28.7k | 📈 +22 | 80 | 6 days ago | `enterprise` |
| 14 | [DSPy](https://github.com/stanfordnlp/dspy) | 🟡 **61.8** | 38.9k | 📈 +86 | 74 | 22 days ago | `optimization` |
| 15 | [LlamaIndex](https://github.com/run-llama/llama_index) | 🟡 **53.7** | 52.8k | 📈 +97 | 7 | 1 mo ago | `data-agent` |
| 16 | [Letta](https://github.com/letta-ai/letta) | 🟠 **34.5** | 25.3k | 📈 +75 | 1 | 5 mo ago | `memory` |
| 17 | [AutoGen](https://github.com/microsoft/autogen) | 🟠 **32.6** | 61.7k | 📈 +96 | 2 | 1y ago | `multi-agent` |
| 18 | [Smolagents](https://github.com/huggingface/smolagents) | 🟠 **31.4** | 30.2k | 📈 +92 | 0 | 5 mo ago | `lightweight` |
| 19 | [Swarm](https://github.com/openai/swarm) | 🔴 **9.4** | 22.1k | 📈 +22 | 0 | — | `experimental` |

## 📂 By Category

- `data-agent`: **LlamaIndex** (53.7)
- `enterprise`: **Semantic Kernel** (67.1)
- `experimental`: **Swarm** (9.4)
- `lightweight`: **Smolagents** (31.4)
- `memory`: **Letta** (34.5)
- `multi-agent`: **CrewAI** (79.8), **Agno** (71.2), **AG2** (70.4), **AutoGen** (32.6)
- `optimization`: **DSPy** (61.8)
- `orchestration`: **LangGraph** (85.5), **Claude Agent SDK** (74.5), **Google ADK** (73.8), **OpenAI Agents SDK** (69.2)
- `pipeline`: **Haystack** (71.7)
- `structured`: **PydanticAI** (72.1)
- `tooling`: **Composio** (68.6)
- `typescript`: **Mastra** (76.7)
- `web-agent`: **BrowserUse** (89.6)

## 🔍 Top 5 — Score Breakdown

| Framework | Star Velocity | Release Freshness | Issue Health | Commit Activity | Community | Fork Ratio |
|-----------|:---:|:---:|:---:|:---:|:---:|:---:|
| **BrowserUse** | 100 | 97.3 | 89.5 | 100 | 72.2 | 44.6 |
| **LangGraph** | 82.7 | 100.0 | 81.3 | 100 | 57.4 | 68.8 |
| **CrewAI** | 56.0 | 100.0 | 84.1 | 100 | 72.6 | 59.7 |
| **Mastra** | 36.3 | 100.0 | 94.3 | 100 | 93.2 | 41.9 |
| **Claude Agent SDK** | 100 | 100.0 | 84.9 | 45.0 | 11.2 | 66.2 |

## 💡 Key Insights

- **Hottest framework**: BrowserUse with a Pulse Score of 89.6
- **Fastest growing**: Claude Agent SDK gained +829 stars this week
- **Most active development**: Mastra with 2217 commits in the last 4 weeks
- **Stale releases**: AutoGen, Swarm haven't released in a while

## 📦 Recent Releases

- **PydanticAI** [`v2.66.0`](https://github.com/pydantic/pydantic-ai/releases/tag/v2.66.0) — today
- **Mastra** [`@mastra/core@1.82.0`](https://github.com/mastra-ai/mastra/releases/tag/@mastra/core@1.82.0) — today
- **AG2** [`v1.3.0`](https://github.com/ag2ai/ag2/releases/tag/v1.3.0) — today
- **Claude Agent SDK** [`v2.1.318`](https://github.com/anthropics/claude-code/releases/tag/v2.1.318) — today
- **CrewAI** [`1.15.35`](https://github.com/crewAIInc/crewAI/releases/tag/1.15.35) — today
- **LangGraph** [`sdk==0.4.12`](https://github.com/langchain-ai/langgraph/releases/tag/sdk==0.4.12) — today
- **OpenAI Agents SDK** [`v0.24.0-alpha.6`](https://github.com/openai/openai-agents-python/releases/tag/v0.24.0-alpha.6) — today *(pre-release)*
- **Composio** [`@composio/cli@0.6.1-beta.533`](https://github.com/ComposioHQ/composio/releases/tag/@composio/cli@0.6.1-beta.533) — 1 day ago *(pre-release)*
- **Haystack** [`v2.31.1`](https://github.com/deepset-ai/haystack/releases/tag/v2.31.1) — 1 day ago
- **Agno** [`v3.1.12`](https://github.com/agno-agi/agno/releases/tag/v3.1.12) — 6 days ago

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

*Powered by GitHub Actions • Data refreshed daily • Last run: 2026-11-04 14:04 UTC*