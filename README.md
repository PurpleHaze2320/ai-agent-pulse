# 🔬 AI Agent Framework Pulse Tracker

[![Daily Update](https://github.com/PurpleHaze2320/ai-agent-pulse/actions/workflows/track.yml/badge.svg)](https://github.com/PurpleHaze2320/ai-agent-pulse/actions/workflows/track.yml)
[![Frameworks Tracked](https://img.shields.io/badge/frameworks-19-blue)](https://github.com/PurpleHaze2320/ai-agent-pulse)
[![License: MIT](https://img.shields.io/badge/License-MIT-green.svg)](https://opensource.org/licenses/MIT)
[![GitHub stars](https://img.shields.io/github/stars/PurpleHaze2320/ai-agent-pulse?style=social)](https://github.com/PurpleHaze2320/ai-agent-pulse/stargazers)

> Automated daily tracking of the AI agent framework ecosystem's health, momentum, and trends.
> Last updated: **2026-08-06 08:45 UTC** | Tracking **19** frameworks

## How It Works

This bot runs daily via GitHub Actions and collects metrics from the GitHub API for the most important
AI agent frameworks. It computes a **Pulse Score** (0-100) based on six weighted signals: star velocity,
release freshness, issue health, commit activity, community size, and fork engagement. The result is
a living dashboard that shows which frameworks are gaining momentum and which are losing steam.

## 🏆 Pulse Leaderboard

| Rank | Framework | Pulse | Stars | ⭐ 7d | Commits (4w) | Last Release | Category |
|------|-----------|-------|-------|-------|--------------|--------------|----------|
| 1 | [BrowserUse](https://github.com/browser-use/browser-use) | 🟢 **89.6** | 108.0k | 🚀 +746 | 170 | 9 days ago | `web-agent` |
| 2 | [CrewAI](https://github.com/crewAIInc/crewAI) | 🟢 **79.4** | 56.7k | 🚀 +315 | 82 | today | `multi-agent` |
| 3 | [Mastra](https://github.com/mastra-ai/mastra) | 🟢 **79.4** | 27.0k | 🚀 +245 | 1172 | 5 days ago | `typescript` |
| 4 | [LangGraph](https://github.com/langchain-ai/langgraph) | 🟢 **74.1** | 39.0k | 🚀 +526 | 33 | 6 days ago | `orchestration` |
| 5 | [Google ADK](https://github.com/google/adk-python) | 🟢 **72.8** | 21.0k | 📈 +72 | 317 | 2 days ago | `orchestration` |
| 6 | [Agno](https://github.com/agno-agi/agno) | 🟢 **71.9** | 41.6k | 📈 +98 | 121 | today | `multi-agent` |
| 7 | [Claude Agent SDK](https://github.com/anthropics/claude-code) | 🟡 **68.5** | 140.4k | 🚀 +832 | 18 | today | `orchestration` |
| 8 | [Composio](https://github.com/ComposioHQ/composio) | 🟡 **67.6** | 29.6k | 🚀 +103 | 294 | today | `tooling` |
| 9 | [PydanticAI](https://github.com/pydantic/pydantic-ai) | 🟡 **57.3** | 19.1k | 🚀 +198 | 0 | today | `structured` |
| 10 | [LlamaIndex](https://github.com/run-llama/llama_index) | 🟡 **56.8** | 51.4k | 🚀 +192 | 0 | 1 mo ago | `data-agent` |
| 11 | [OpenAI Agents SDK](https://github.com/openai/openai-agents-python) | 🟡 **55.3** | 28.4k | 🚀 +142 | 0 | 1 day ago | `orchestration` |
| 12 | [DSPy](https://github.com/stanfordnlp/dspy) | 🟡 **52.9** | 36.6k | 🚀 +184 | 0 | 2 days ago | `optimization` |
| 13 | [Haystack](https://github.com/deepset-ai/haystack) | 🟡 **49.6** | 26.1k | 📈 +63 | 0 | 16 days ago | `pipeline` |
| 14 | [AG2](https://github.com/ag2ai/ag2) | 🟡 **49.6** | 4.8k | ↗️ +19 | 0 | 8 days ago | `multi-agent` |
| 15 | [Semantic Kernel](https://github.com/microsoft/semantic-kernel) | 🟡 **49.2** | 28.4k | 📈 +35 | 0 | 29 days ago | `enterprise` |
| 16 | [Letta](https://github.com/letta-ai/letta) | 🟡 **40.9** | 24.1k | 📈 +90 | 0 | 2 mo ago | `memory` |
| 17 | [Smolagents](https://github.com/huggingface/smolagents) | 🟠 **38.5** | 28.7k | 🚀 +102 | 0 | 2 mo ago | `lightweight` |
| 18 | [AutoGen](https://github.com/microsoft/autogen) | 🟠 **35.4** | 60.3k | 🚀 +159 | 0 | 10 mo ago | `multi-agent` |
| 19 | [Swarm](https://github.com/openai/swarm) | 🔴 **9.7** | 21.9k | ↗️ +18 | 0 | — | `experimental` |

## 📂 By Category

- `data-agent`: **LlamaIndex** (56.8)
- `enterprise`: **Semantic Kernel** (49.2)
- `experimental`: **Swarm** (9.7)
- `lightweight`: **Smolagents** (38.5)
- `memory`: **Letta** (40.9)
- `multi-agent`: **CrewAI** (79.4), **Agno** (71.9), **AG2** (49.6), **AutoGen** (35.4)
- `optimization`: **DSPy** (52.9)
- `orchestration`: **LangGraph** (74.1), **Google ADK** (72.8), **Claude Agent SDK** (68.5), **OpenAI Agents SDK** (55.3)
- `pipeline`: **Haystack** (49.6)
- `structured`: **PydanticAI** (57.3)
- `tooling`: **Composio** (67.6)
- `typescript`: **Mastra** (79.4)
- `web-agent`: **BrowserUse** (89.6)

## 🔍 Top 5 — Score Breakdown

| Framework | Star Velocity | Release Freshness | Issue Health | Commit Activity | Community | Fork Ratio |
|-----------|:---:|:---:|:---:|:---:|:---:|:---:|
| **BrowserUse** | 100 | 97.0 | 94.3 | 100 | 66.4 | 44.0 |
| **CrewAI** | 68.4 | 100.0 | 95.0 | 82.0 | 59.8 | 57.0 |
| **Mastra** | 50.4 | 98.3 | 93.6 | 100 | 92.6 | 38.2 |
| **LangGraph** | 100 | 98.0 | 70.9 | 33.0 | 55.4 | 67.3 |
| **Google ADK** | 17.7 | 99.3 | 88.6 | 100 | 79.4 | 72.4 |

## 💡 Key Insights

- **Hottest framework**: BrowserUse with a Pulse Score of 89.6
- **Fastest growing**: Claude Agent SDK gained +832 stars this week
- **Most active development**: Mastra with 1172 commits in the last 4 weeks
- **Stale releases**: AutoGen, Swarm haven't released in a while

## 📦 Recent Releases

- **Composio** [`@composio/cli@0.3.3-beta.340`](https://github.com/ComposioHQ/composio/releases/tag/@composio/cli@0.3.3-beta.340) — today *(pre-release)*
- **PydanticAI** [`v2.25.0`](https://github.com/pydantic/pydantic-ai/releases/tag/v2.25.0) — today
- **Claude Agent SDK** [`v2.1.223`](https://github.com/anthropics/claude-code/releases/tag/v2.1.223) — today
- **CrewAI** [`1.15.12`](https://github.com/crewAIInc/crewAI/releases/tag/1.15.12) — today
- **Agno** [`v2.8.7`](https://github.com/agno-agi/agno/releases/tag/v2.8.7) — today
- **OpenAI Agents SDK** [`v0.19.4`](https://github.com/openai/openai-agents-python/releases/tag/v0.19.4) — 1 day ago
- **Google ADK** [`v2.6.2`](https://github.com/google/adk-python/releases/tag/v2.6.2) — 2 days ago
- **DSPy** [`3.3.0`](https://github.com/stanfordnlp/dspy/releases/tag/3.3.0) — 2 days ago
- **Mastra** [`@mastra/core@1.55.0`](https://github.com/mastra-ai/mastra/releases/tag/@mastra/core@1.55.0) — 5 days ago
- **LangGraph** [`checkpointsqlite==3.1.1`](https://github.com/langchain-ai/langgraph/releases/tag/checkpointsqlite==3.1.1) — 6 days ago

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

*Powered by GitHub Actions • Data refreshed daily • Last run: 2026-08-06 08:45 UTC*