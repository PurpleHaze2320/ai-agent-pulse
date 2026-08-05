# 🔬 AI Agent Framework Pulse Tracker

[![Daily Update](https://github.com/PurpleHaze2320/ai-agent-pulse/actions/workflows/track.yml/badge.svg)](https://github.com/PurpleHaze2320/ai-agent-pulse/actions/workflows/track.yml)
[![Frameworks Tracked](https://img.shields.io/badge/frameworks-19-blue)](https://github.com/PurpleHaze2320/ai-agent-pulse)
[![License: MIT](https://img.shields.io/badge/License-MIT-green.svg)](https://opensource.org/licenses/MIT)
[![GitHub stars](https://img.shields.io/github/stars/PurpleHaze2320/ai-agent-pulse?style=social)](https://github.com/PurpleHaze2320/ai-agent-pulse/stargazers)

> Automated daily tracking of the AI agent framework ecosystem's health, momentum, and trends.
> Last updated: **2026-08-05 08:43 UTC** | Tracking **19** frameworks

## How It Works

This bot runs daily via GitHub Actions and collects metrics from the GitHub API for the most important
AI agent frameworks. It computes a **Pulse Score** (0-100) based on six weighted signals: star velocity,
release freshness, issue health, commit activity, community size, and fork engagement. The result is
a living dashboard that shows which frameworks are gaining momentum and which are losing steam.

## 🏆 Pulse Leaderboard

| Rank | Framework | Pulse | Stars | ⭐ 7d | Commits (4w) | Last Release | Category |
|------|-----------|-------|-------|-------|--------------|--------------|----------|
| 1 | [BrowserUse](https://github.com/browser-use/browser-use) | 🟢 **89.6** | 107.9k | 🚀 +756 | 170 | 8 days ago | `web-agent` |
| 2 | [Mastra](https://github.com/mastra-ai/mastra) | 🟢 **79.8** | 26.9k | 🚀 +254 | 1051 | 4 days ago | `typescript` |
| 3 | [PydanticAI](https://github.com/pydantic/pydantic-ai) | 🟢 **77.0** | 19.1k | 🚀 +189 | 250 | today | `structured` |
| 4 | [OpenAI Agents SDK](https://github.com/openai/openai-agents-python) | 🟢 **75.0** | 28.4k | 🚀 +134 | 214 | today | `orchestration` |
| 5 | [Google ADK](https://github.com/google/adk-python) | 🟢 **73.2** | 21.0k | 📈 +82 | 284 | 1 day ago | `orchestration` |
| 6 | [Agno](https://github.com/agno-agi/agno) | 🟢 **71.5** | 41.6k | 📈 +98 | 111 | 5 days ago | `multi-agent` |
| 7 | [Haystack](https://github.com/deepset-ai/haystack) | 🟡 **69.6** | 26.1k | 📈 +62 | 219 | 15 days ago | `pipeline` |
| 8 | [Claude Agent SDK](https://github.com/anthropics/claude-code) | 🟡 **68.3** | 140.3k | 🚀 +838 | 17 | today | `orchestration` |
| 9 | [Composio](https://github.com/ComposioHQ/composio) | 🟡 **67.7** | 29.5k | 🚀 +107 | 193 | today | `tooling` |
| 10 | [LangGraph](https://github.com/langchain-ai/langgraph) | 🟡 **67.6** | 38.9k | 🚀 +533 | 0 | 5 days ago | `orchestration` |
| 11 | [CrewAI](https://github.com/crewAIInc/crewAI) | 🟡 **63.9** | 56.6k | 🚀 +337 | 0 | today | `multi-agent` |
| 12 | [LlamaIndex](https://github.com/run-llama/llama_index) | 🟡 **62.3** | 51.4k | 🚀 +205 | 25 | 1 mo ago | `data-agent` |
| 13 | [DSPy](https://github.com/stanfordnlp/dspy) | 🟡 **61.5** | 36.6k | 🚀 +181 | 43 | 1 day ago | `optimization` |
| 14 | [Semantic Kernel](https://github.com/microsoft/semantic-kernel) | 🟡 **52.0** | 28.4k | 📈 +33 | 14 | 28 days ago | `enterprise` |
| 15 | [AG2](https://github.com/ag2ai/ag2) | 🟡 **49.8** | 4.8k | 📈 +21 | 0 | 7 days ago | `multi-agent` |
| 16 | [Letta](https://github.com/letta-ai/letta) | 🟡 **41.3** | 24.1k | 📈 +86 | 2 | 2 mo ago | `memory` |
| 17 | [Smolagents](https://github.com/huggingface/smolagents) | 🟠 **38.4** | 28.7k | 📈 +97 | 0 | 2 mo ago | `lightweight` |
| 18 | [AutoGen](https://github.com/microsoft/autogen) | 🟠 **35.8** | 60.2k | 🚀 +168 | 0 | 10 mo ago | `multi-agent` |
| 19 | [Swarm](https://github.com/openai/swarm) | 🔴 **9.4** | 21.9k | ↗️ +11 | 0 | — | `experimental` |

## 📂 By Category

- `data-agent`: **LlamaIndex** (62.3)
- `enterprise`: **Semantic Kernel** (52.0)
- `experimental`: **Swarm** (9.4)
- `lightweight`: **Smolagents** (38.4)
- `memory`: **Letta** (41.3)
- `multi-agent`: **Agno** (71.5), **CrewAI** (63.9), **AG2** (49.8), **AutoGen** (35.8)
- `optimization`: **DSPy** (61.5)
- `orchestration`: **OpenAI Agents SDK** (75.0), **Google ADK** (73.2), **Claude Agent SDK** (68.3), **LangGraph** (67.6)
- `pipeline`: **Haystack** (69.6)
- `structured`: **PydanticAI** (77.0)
- `tooling`: **Composio** (67.7)
- `typescript`: **Mastra** (79.8)
- `web-agent`: **BrowserUse** (89.6)

## 🔍 Top 5 — Score Breakdown

| Framework | Star Velocity | Release Freshness | Issue Health | Commit Activity | Community | Fork Ratio |
|-----------|:---:|:---:|:---:|:---:|:---:|:---:|
| **BrowserUse** | 100 | 97.3 | 94.3 | 100 | 66.4 | 43.9 |
| **Mastra** | 51.7 | 98.7 | 93.5 | 100 | 92.8 | 38.1 |
| **PydanticAI** | 38.8 | 100.0 | 84.3 | 100 | 95.0 | 52.1 |
| **OpenAI Agents SDK** | 29.4 | 100.0 | 98.8 | 100 | 65.6 | 62.6 |
| **Google ADK** | 19.3 | 99.7 | 88.4 | 100 | 79.4 | 72.3 |

## 💡 Key Insights

- **Hottest framework**: BrowserUse with a Pulse Score of 89.6
- **Fastest growing**: Claude Agent SDK gained +838 stars this week
- **Most active development**: Mastra with 1051 commits in the last 4 weeks
- **Stale releases**: AutoGen, Swarm haven't released in a while

## 📦 Recent Releases

- **CrewAI** [`1.15.11`](https://github.com/crewAIInc/crewAI/releases/tag/1.15.11) — today
- **OpenAI Agents SDK** [`v0.19.4`](https://github.com/openai/openai-agents-python/releases/tag/v0.19.4) — today
- **PydanticAI** [`v2.24.0`](https://github.com/pydantic/pydantic-ai/releases/tag/v2.24.0) — today
- **Claude Agent SDK** [`v2.1.222`](https://github.com/anthropics/claude-code/releases/tag/v2.1.222) — today
- **Composio** [`@composio/cli@0.3.2-beta.333`](https://github.com/ComposioHQ/composio/releases/tag/@composio/cli@0.3.2-beta.333) — today *(pre-release)*
- **Google ADK** [`v2.6.2`](https://github.com/google/adk-python/releases/tag/v2.6.2) — 1 day ago
- **DSPy** [`3.3.0`](https://github.com/stanfordnlp/dspy/releases/tag/3.3.0) — 1 day ago
- **Mastra** [`@mastra/core@1.55.0`](https://github.com/mastra-ai/mastra/releases/tag/@mastra/core@1.55.0) — 4 days ago
- **LangGraph** [`checkpointsqlite==3.1.1`](https://github.com/langchain-ai/langgraph/releases/tag/checkpointsqlite==3.1.1) — 5 days ago
- **Agno** [`v2.8.6`](https://github.com/agno-agi/agno/releases/tag/v2.8.6) — 5 days ago

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

*Powered by GitHub Actions • Data refreshed daily • Last run: 2026-08-05 08:43 UTC*