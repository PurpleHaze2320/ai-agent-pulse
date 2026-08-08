# 🔬 AI Agent Framework Pulse Tracker

[![Daily Update](https://github.com/PurpleHaze2320/ai-agent-pulse/actions/workflows/track.yml/badge.svg)](https://github.com/PurpleHaze2320/ai-agent-pulse/actions/workflows/track.yml)
[![Frameworks Tracked](https://img.shields.io/badge/frameworks-19-blue)](https://github.com/PurpleHaze2320/ai-agent-pulse)
[![License: MIT](https://img.shields.io/badge/License-MIT-green.svg)](https://opensource.org/licenses/MIT)
[![GitHub stars](https://img.shields.io/github/stars/PurpleHaze2320/ai-agent-pulse?style=social)](https://github.com/PurpleHaze2320/ai-agent-pulse/stargazers)

> Automated daily tracking of the AI agent framework ecosystem's health, momentum, and trends.
> Last updated: **2026-08-08 07:01 UTC** | Tracking **19** frameworks

## How It Works

This bot runs daily via GitHub Actions and collects metrics from the GitHub API for the most important
AI agent frameworks. It computes a **Pulse Score** (0-100) based on six weighted signals: star velocity,
release freshness, issue health, commit activity, community size, and fork engagement. The result is
a living dashboard that shows which frameworks are gaining momentum and which are losing steam.

## 🏆 Pulse Leaderboard

| Rank | Framework | Pulse | Stars | ⭐ 7d | Commits (4w) | Last Release | Category |
|------|-----------|-------|-------|-------|--------------|--------------|----------|
| 1 | [BrowserUse](https://github.com/browser-use/browser-use) | 🟢 **89.5** | 108.2k | 🚀 +782 | 172 | 11 days ago | `web-agent` |
| 2 | [Mastra](https://github.com/mastra-ai/mastra) | 🟢 **79.5** | 27.0k | 🚀 +236 | 1497 | 1 day ago | `typescript` |
| 3 | [LangGraph](https://github.com/langchain-ai/langgraph) | 🟡 **67.9** | 39.2k | 🚀 +567 | 0 | today | `orchestration` |
| 4 | [Claude Agent SDK](https://github.com/anthropics/claude-code) | 🟡 **64.8** | 140.6k | 🚀 +777 | 0 | today | `orchestration` |
| 5 | [CrewAI](https://github.com/crewAIInc/crewAI) | 🟡 **62.9** | 56.8k | 🚀 +317 | 0 | today | `multi-agent` |
| 6 | [PydanticAI](https://github.com/pydantic/pydantic-ai) | 🟡 **57.3** | 19.1k | 🚀 +198 | 0 | today | `structured` |
| 7 | [LlamaIndex](https://github.com/run-llama/llama_index) | 🟡 **56.3** | 51.5k | 🚀 +183 | 0 | 1 mo ago | `data-agent` |
| 8 | [OpenAI Agents SDK](https://github.com/openai/openai-agents-python) | 🟡 **55.9** | 28.5k | 🚀 +158 | 0 | 3 days ago | `orchestration` |
| 9 | [Google ADK](https://github.com/google/adk-python) | 🟡 **53.5** | 21.0k | 📈 +79 | 0 | today | `orchestration` |
| 10 | [DSPy](https://github.com/stanfordnlp/dspy) | 🟡 **52.7** | 36.7k | 🚀 +186 | 0 | 4 days ago | `optimization` |
| 11 | [Agno](https://github.com/agno-agi/agno) | 🟡 **51.4** | 41.6k | 📈 +92 | 0 | 1 day ago | `multi-agent` |
| 12 | [Semantic Kernel](https://github.com/microsoft/semantic-kernel) | 🟡 **50.8** | 28.4k | 📈 +30 | 0 | 1 day ago | `enterprise` |
| 13 | [Haystack](https://github.com/deepset-ai/haystack) | 🟡 **49.7** | 26.1k | 📈 +69 | 0 | 18 days ago | `pipeline` |
| 14 | [AG2](https://github.com/ag2ai/ag2) | 🟡 **49.4** | 4.8k | ↗️ +17 | 0 | 10 days ago | `multi-agent` |
| 15 | [Composio](https://github.com/ComposioHQ/composio) | 🟡 **47.4** | 29.6k | 📈 +98 | 0 | today | `tooling` |
| 16 | [Letta](https://github.com/letta-ai/letta) | 🟡 **41.4** | 24.1k | 🚀 +103 | 0 | 2 mo ago | `memory` |
| 17 | [Smolagents](https://github.com/huggingface/smolagents) | 🟠 **38.7** | 28.7k | 🚀 +110 | 0 | 2 mo ago | `lightweight` |
| 18 | [AutoGen](https://github.com/microsoft/autogen) | 🟠 **35.7** | 60.3k | 🚀 +167 | 0 | 10 mo ago | `multi-agent` |
| 19 | [Swarm](https://github.com/openai/swarm) | 🔴 **9.7** | 21.9k | ↗️ +19 | 0 | — | `experimental` |

## 📂 By Category

- `data-agent`: **LlamaIndex** (56.3)
- `enterprise`: **Semantic Kernel** (50.8)
- `experimental`: **Swarm** (9.7)
- `lightweight`: **Smolagents** (38.7)
- `memory`: **Letta** (41.4)
- `multi-agent`: **CrewAI** (62.9), **Agno** (51.4), **AG2** (49.4), **AutoGen** (35.7)
- `optimization`: **DSPy** (52.7)
- `orchestration`: **LangGraph** (67.9), **Claude Agent SDK** (64.8), **OpenAI Agents SDK** (55.9), **Google ADK** (53.5)
- `pipeline`: **Haystack** (49.7)
- `structured`: **PydanticAI** (57.3)
- `tooling`: **Composio** (47.4)
- `typescript`: **Mastra** (79.5)
- `web-agent`: **BrowserUse** (89.5)

## 🔍 Top 5 — Score Breakdown

| Framework | Star Velocity | Release Freshness | Issue Health | Commit Activity | Community | Fork Ratio |
|-----------|:---:|:---:|:---:|:---:|:---:|:---:|
| **BrowserUse** | 100 | 96.3 | 94.3 | 100 | 66.6 | 44.0 |
| **Mastra** | 48.9 | 99.7 | 95.2 | 100 | 92.6 | 38.3 |
| **LangGraph** | 100 | 100.0 | 71.0 | 0.0 | 55.4 | 67.2 |
| **Claude Agent SDK** | 100 | 100.0 | 82.3 | 0.0 | 10.4 | 64.3 |
| **CrewAI** | 67.8 | 100.0 | 95.1 | 0.0 | 59.8 | 57.0 |

## 💡 Key Insights

- **Hottest framework**: BrowserUse with a Pulse Score of 89.5
- **Fastest growing**: BrowserUse gained +782 stars this week
- **Most active development**: Mastra with 1497 commits in the last 4 weeks
- **Stale releases**: AutoGen, Swarm haven't released in a while

## 📦 Recent Releases

- **PydanticAI** [`v2.27.0`](https://github.com/pydantic/pydantic-ai/releases/tag/v2.27.0) — today
- **Claude Agent SDK** [`v2.1.226`](https://github.com/anthropics/claude-code/releases/tag/v2.1.226) — today
- **Google ADK** [`v2.6.3`](https://github.com/google/adk-python/releases/tag/v2.6.3) — today
- **CrewAI** [`1.15.13`](https://github.com/crewAIInc/crewAI/releases/tag/1.15.13) — today
- **LangGraph** [`checkpointpostgres==3.1.2`](https://github.com/langchain-ai/langgraph/releases/tag/checkpointpostgres==3.1.2) — today
- **Composio** [`@composio/slim@0.15.0`](https://github.com/ComposioHQ/composio/releases/tag/@composio/slim@0.15.0) — today
- **Agno** [`v3.0.0a1`](https://github.com/agno-agi/agno/releases/tag/v3.0.0a1) — 1 day ago *(pre-release)*
- **Semantic Kernel** [`python-1.44.1`](https://github.com/microsoft/semantic-kernel/releases/tag/python-1.44.1) — 1 day ago
- **Mastra** [`@mastra/core@1.56.0`](https://github.com/mastra-ai/mastra/releases/tag/@mastra/core@1.56.0) — 1 day ago
- **OpenAI Agents SDK** [`v0.19.4`](https://github.com/openai/openai-agents-python/releases/tag/v0.19.4) — 3 days ago

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

*Powered by GitHub Actions • Data refreshed daily • Last run: 2026-08-08 07:01 UTC*