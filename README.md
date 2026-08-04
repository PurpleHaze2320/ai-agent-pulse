# 🔬 AI Agent Framework Pulse Tracker

[![Daily Update](https://github.com/PurpleHaze2320/ai-agent-pulse/actions/workflows/track.yml/badge.svg)](https://github.com/PurpleHaze2320/ai-agent-pulse/actions/workflows/track.yml)
[![Frameworks Tracked](https://img.shields.io/badge/frameworks-19-blue)](https://github.com/PurpleHaze2320/ai-agent-pulse)
[![License: MIT](https://img.shields.io/badge/License-MIT-green.svg)](https://opensource.org/licenses/MIT)
[![GitHub stars](https://img.shields.io/github/stars/PurpleHaze2320/ai-agent-pulse?style=social)](https://github.com/PurpleHaze2320/ai-agent-pulse/stargazers)

> Automated daily tracking of the AI agent framework ecosystem's health, momentum, and trends.
> Last updated: **2026-08-04 08:46 UTC** | Tracking **19** frameworks

## How It Works

This bot runs daily via GitHub Actions and collects metrics from the GitHub API for the most important
AI agent frameworks. It computes a **Pulse Score** (0-100) based on six weighted signals: star velocity,
release freshness, issue health, commit activity, community size, and fork engagement. The result is
a living dashboard that shows which frameworks are gaining momentum and which are losing steam.

## 🏆 Pulse Leaderboard

| Rank | Framework | Pulse | Stars | ⭐ 7d | Commits (4w) | Last Release | Category |
|------|-----------|-------|-------|-------|--------------|--------------|----------|
| 1 | [BrowserUse](https://github.com/browser-use/browser-use) | 🟢 **89.7** | 107.8k | 🚀 +746 | 156 | 7 days ago | `web-agent` |
| 2 | [Mastra](https://github.com/mastra-ai/mastra) | 🟢 **80.0** | 26.9k | 🚀 +260 | 1016 | 3 days ago | `typescript` |
| 3 | [PydanticAI](https://github.com/pydantic/pydantic-ai) | 🟢 **77.1** | 19.0k | 🚀 +191 | 231 | today | `structured` |
| 4 | [CrewAI](https://github.com/crewAIInc/crewAI) | 🟢 **76.6** | 56.6k | 🚀 +337 | 64 | 3 days ago | `multi-agent` |
| 5 | [Google ADK](https://github.com/google/adk-python) | 🟢 **73.1** | 21.0k | 📈 +76 | 278 | today | `orchestration` |
| 6 | [Agno](https://github.com/agno-agi/agno) | 🟢 **71.6** | 41.6k | 📈 +97 | 109 | 4 days ago | `multi-agent` |
| 7 | [LangGraph](https://github.com/langchain-ai/langgraph) | 🟢 **71.1** | 38.8k | 🚀 +522 | 17 | 4 days ago | `orchestration` |
| 8 | [Haystack](https://github.com/deepset-ai/haystack) | 🟡 **69.8** | 26.1k | 📈 +68 | 207 | 14 days ago | `pipeline` |
| 9 | [Claude Agent SDK](https://github.com/anthropics/claude-code) | 🟡 **68.1** | 140.2k | 🚀 +802 | 16 | today | `orchestration` |
| 10 | [Composio](https://github.com/ComposioHQ/composio) | 🟡 **67.8** | 29.5k | 🚀 +111 | 188 | today | `tooling` |
| 11 | [LlamaIndex](https://github.com/run-llama/llama_index) | 🟡 **61.2** | 51.4k | 🚀 +211 | 18 | 1 mo ago | `data-agent` |
| 12 | [DSPy](https://github.com/stanfordnlp/dspy) | 🟡 **60.7** | 36.6k | 🚀 +184 | 38 | today | `optimization` |
| 13 | [OpenAI Agents SDK](https://github.com/openai/openai-agents-python) | 🟡 **55.2** | 28.4k | 🚀 +141 | 0 | today | `orchestration` |
| 14 | [Semantic Kernel](https://github.com/microsoft/semantic-kernel) | 🟡 **52.1** | 28.4k | 📈 +34 | 14 | 27 days ago | `enterprise` |
| 15 | [AG2](https://github.com/ag2ai/ag2) | 🟡 **50.1** | 4.8k | 📈 +26 | 0 | 6 days ago | `multi-agent` |
| 16 | [Letta](https://github.com/letta-ai/letta) | 🟡 **41.5** | 24.1k | 📈 +89 | 2 | 2 mo ago | `memory` |
| 17 | [Smolagents](https://github.com/huggingface/smolagents) | 🟠 **38.3** | 28.7k | 📈 +91 | 0 | 2 mo ago | `lightweight` |
| 18 | [AutoGen](https://github.com/microsoft/autogen) | 🟠 **35.5** | 60.2k | 🚀 +161 | 0 | 10 mo ago | `multi-agent` |
| 19 | [Swarm](https://github.com/openai/swarm) | 🔴 **9.2** | 21.9k | ↗️ +5 | 0 | — | `experimental` |

## 📂 By Category

- `data-agent`: **LlamaIndex** (61.2)
- `enterprise`: **Semantic Kernel** (52.1)
- `experimental`: **Swarm** (9.2)
- `lightweight`: **Smolagents** (38.3)
- `memory`: **Letta** (41.5)
- `multi-agent`: **CrewAI** (76.6), **Agno** (71.6), **AG2** (50.1), **AutoGen** (35.5)
- `optimization`: **DSPy** (60.7)
- `orchestration`: **Google ADK** (73.1), **LangGraph** (71.1), **Claude Agent SDK** (68.1), **OpenAI Agents SDK** (55.2)
- `pipeline`: **Haystack** (69.8)
- `structured`: **PydanticAI** (77.1)
- `tooling`: **Composio** (67.8)
- `typescript`: **Mastra** (80.0)
- `web-agent`: **BrowserUse** (89.7)

## 🔍 Top 5 — Score Breakdown

| Framework | Star Velocity | Release Freshness | Issue Health | Commit Activity | Community | Fork Ratio |
|-----------|:---:|:---:|:---:|:---:|:---:|:---:|
| **BrowserUse** | 100 | 97.7 | 94.3 | 100 | 66.2 | 44.0 |
| **Mastra** | 52.5 | 99.0 | 93.4 | 100 | 93.0 | 38.1 |
| **PydanticAI** | 39.2 | 100.0 | 84.4 | 100 | 94.8 | 52.0 |
| **CrewAI** | 72.2 | 99.0 | 95.0 | 64.0 | 59.8 | 56.9 |
| **Google ADK** | 18.6 | 100.0 | 88.4 | 100 | 79.4 | 72.2 |

## 💡 Key Insights

- **Hottest framework**: BrowserUse with a Pulse Score of 89.7
- **Fastest growing**: Claude Agent SDK gained +802 stars this week
- **Most active development**: Mastra with 1016 commits in the last 4 weeks
- **Stale releases**: AutoGen, Swarm haven't released in a while

## 📦 Recent Releases

- **OpenAI Agents SDK** [`v0.19.3`](https://github.com/openai/openai-agents-python/releases/tag/v0.19.3) — today
- **PydanticAI** [`v2.23.0`](https://github.com/pydantic/pydantic-ai/releases/tag/v2.23.0) — today
- **Google ADK** [`v2.6.2`](https://github.com/google/adk-python/releases/tag/v2.6.2) — today
- **Claude Agent SDK** [`v2.1.221`](https://github.com/anthropics/claude-code/releases/tag/v2.1.221) — today
- **DSPy** [`3.3.0`](https://github.com/stanfordnlp/dspy/releases/tag/3.3.0) — today
- **Composio** [`@composio/cli@0.3.2-beta.332`](https://github.com/ComposioHQ/composio/releases/tag/@composio/cli@0.3.2-beta.332) — today *(pre-release)*
- **CrewAI** [`1.15.10`](https://github.com/crewAIInc/crewAI/releases/tag/1.15.10) — 3 days ago
- **Mastra** [`@mastra/core@1.55.0`](https://github.com/mastra-ai/mastra/releases/tag/@mastra/core@1.55.0) — 3 days ago
- **LangGraph** [`checkpointsqlite==3.1.1`](https://github.com/langchain-ai/langgraph/releases/tag/checkpointsqlite==3.1.1) — 4 days ago
- **Agno** [`v2.8.6`](https://github.com/agno-agi/agno/releases/tag/v2.8.6) — 4 days ago

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

*Powered by GitHub Actions • Data refreshed daily • Last run: 2026-08-04 08:46 UTC*