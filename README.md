# 🔬 AI Agent Framework Pulse Tracker

[![Daily Update](https://github.com/PurpleHaze2320/ai-agent-pulse/actions/workflows/track.yml/badge.svg)](https://github.com/PurpleHaze2320/ai-agent-pulse/actions/workflows/track.yml)
[![Frameworks Tracked](https://img.shields.io/badge/frameworks-19-blue)](https://github.com/PurpleHaze2320/ai-agent-pulse)
[![License: MIT](https://img.shields.io/badge/License-MIT-green.svg)](https://opensource.org/licenses/MIT)
[![GitHub stars](https://img.shields.io/github/stars/PurpleHaze2320/ai-agent-pulse?style=social)](https://github.com/PurpleHaze2320/ai-agent-pulse/stargazers)

> Automated daily tracking of the AI agent framework ecosystem's health, momentum, and trends.
> Last updated: **2026-08-10 07:50 UTC** | Tracking **19** frameworks

## How It Works

This bot runs daily via GitHub Actions and collects metrics from the GitHub API for the most important
AI agent frameworks. It computes a **Pulse Score** (0-100) based on six weighted signals: star velocity,
release freshness, issue health, commit activity, community size, and fork engagement. The result is
a living dashboard that shows which frameworks are gaining momentum and which are losing steam.

## 🏆 Pulse Leaderboard

| Rank | Framework | Pulse | Stars | ⭐ 7d | Commits (4w) | Last Release | Category |
|------|-----------|-------|-------|-------|--------------|--------------|----------|
| 1 | [BrowserUse](https://github.com/browser-use/browser-use) | 🟢 **89.3** | 108.5k | 🚀 +865 | 147 | 13 days ago | `web-agent` |
| 2 | [Mastra](https://github.com/mastra-ai/mastra) | 🟢 **78.8** | 27.1k | 🚀 +217 | 1239 | 3 days ago | `typescript` |
| 3 | [CrewAI](https://github.com/crewAIInc/crewAI) | 🟢 **77.6** | 56.9k | 🚀 +337 | 72 | 1 day ago | `multi-agent` |
| 4 | [LangGraph](https://github.com/langchain-ai/langgraph) | 🟢 **75.3** | 39.3k | 🚀 +599 | 38 | 2 days ago | `orchestration` |
| 5 | [Claude Agent SDK](https://github.com/anthropics/claude-code) | 🟡 **67.5** | 140.9k | 🚀 +802 | 14 | 2 days ago | `orchestration` |
| 6 | [Composio](https://github.com/ComposioHQ/composio) | 🟡 **67.5** | 29.6k | 🚀 +105 | 246 | 2 days ago | `tooling` |
| 7 | [Agno](https://github.com/agno-agi/agno) | 🟡 **64.2** | 41.6k | 📈 +89 | 66 | 3 days ago | `multi-agent` |
| 8 | [DSPy](https://github.com/stanfordnlp/dspy) | 🟡 **60.7** | 37.0k | 🚀 +394 | 0 | 6 days ago | `optimization` |
| 9 | [LlamaIndex](https://github.com/run-llama/llama_index) | 🟡 **56.6** | 51.5k | 🚀 +189 | 0 | 1 mo ago | `data-agent` |
| 10 | [OpenAI Agents SDK](https://github.com/openai/openai-agents-python) | 🟡 **56.3** | 28.5k | 🚀 +173 | 0 | 5 days ago | `orchestration` |
| 11 | [PydanticAI](https://github.com/pydantic/pydantic-ai) | 🟡 **55.8** | 19.2k | 🚀 +164 | 0 | 2 days ago | `structured` |
| 12 | [Google ADK](https://github.com/google/adk-python) | 🟡 **53.1** | 21.1k | 📈 +74 | 0 | 2 days ago | `orchestration` |
| 13 | [Semantic Kernel](https://github.com/microsoft/semantic-kernel) | 🟡 **50.7** | 28.4k | 📈 +29 | 0 | 3 days ago | `enterprise` |
| 14 | [Haystack](https://github.com/deepset-ai/haystack) | 🟡 **49.6** | 26.2k | 📈 +68 | 0 | 20 days ago | `pipeline` |
| 15 | [AG2](https://github.com/ag2ai/ag2) | 🟡 **49.3** | 4.8k | ↗️ +18 | 0 | 12 days ago | `multi-agent` |
| 16 | [Letta](https://github.com/letta-ai/letta) | 🟡 **41.3** | 24.2k | 🚀 +105 | 0 | 2 mo ago | `memory` |
| 17 | [Smolagents](https://github.com/huggingface/smolagents) | 🟠 **37.8** | 28.7k | 📈 +90 | 0 | 2 mo ago | `lightweight` |
| 18 | [AutoGen](https://github.com/microsoft/autogen) | 🟠 **35.4** | 60.3k | 🚀 +159 | 0 | 10 mo ago | `multi-agent` |
| 19 | [Swarm](https://github.com/openai/swarm) | 🔴 **9.6** | 21.9k | ↗️ +18 | 0 | — | `experimental` |

## 📂 By Category

- `data-agent`: **LlamaIndex** (56.6)
- `enterprise`: **Semantic Kernel** (50.7)
- `experimental`: **Swarm** (9.6)
- `lightweight`: **Smolagents** (37.8)
- `memory`: **Letta** (41.3)
- `multi-agent`: **CrewAI** (77.6), **Agno** (64.2), **AG2** (49.3), **AutoGen** (35.4)
- `optimization`: **DSPy** (60.7)
- `orchestration`: **LangGraph** (75.3), **Claude Agent SDK** (67.5), **OpenAI Agents SDK** (56.3), **Google ADK** (53.1)
- `pipeline`: **Haystack** (49.6)
- `structured`: **PydanticAI** (55.8)
- `tooling`: **Composio** (67.5)
- `typescript`: **Mastra** (78.8)
- `web-agent`: **BrowserUse** (89.3)

## 🔍 Top 5 — Score Breakdown

| Framework | Star Velocity | Release Freshness | Issue Health | Commit Activity | Community | Fork Ratio |
|-----------|:---:|:---:|:---:|:---:|:---:|:---:|
| **BrowserUse** | 100 | 95.7 | 94.0 | 100 | 66.6 | 44.0 |
| **Mastra** | 45.9 | 99.0 | 96.1 | 100 | 92.6 | 38.5 |
| **CrewAI** | 70.5 | 99.7 | 93.1 | 72.0 | 59.8 | 57.0 |
| **LangGraph** | 100 | 99.3 | 70.8 | 38.0 | 55.4 | 67.2 |
| **Claude Agent SDK** | 100 | 99.3 | 82.1 | 14.0 | 10.4 | 64.3 |

## 💡 Key Insights

- **Hottest framework**: BrowserUse with a Pulse Score of 89.3
- **Fastest growing**: BrowserUse gained +865 stars this week
- **Most active development**: Mastra with 1239 commits in the last 4 weeks
- **Stale releases**: AutoGen, Swarm haven't released in a while

## 📦 Recent Releases

- **CrewAI** [`1.15.14`](https://github.com/crewAIInc/crewAI/releases/tag/1.15.14) — 1 day ago
- **PydanticAI** [`v2.27.0`](https://github.com/pydantic/pydantic-ai/releases/tag/v2.27.0) — 2 days ago
- **Claude Agent SDK** [`v2.1.226`](https://github.com/anthropics/claude-code/releases/tag/v2.1.226) — 2 days ago
- **Google ADK** [`v2.6.3`](https://github.com/google/adk-python/releases/tag/v2.6.3) — 2 days ago
- **LangGraph** [`checkpointpostgres==3.1.2`](https://github.com/langchain-ai/langgraph/releases/tag/checkpointpostgres==3.1.2) — 2 days ago
- **Composio** [`@composio/slim@0.15.0`](https://github.com/ComposioHQ/composio/releases/tag/@composio/slim@0.15.0) — 2 days ago
- **Agno** [`v3.0.0a1`](https://github.com/agno-agi/agno/releases/tag/v3.0.0a1) — 3 days ago *(pre-release)*
- **Semantic Kernel** [`python-1.44.1`](https://github.com/microsoft/semantic-kernel/releases/tag/python-1.44.1) — 3 days ago
- **Mastra** [`@mastra/core@1.56.0`](https://github.com/mastra-ai/mastra/releases/tag/@mastra/core@1.56.0) — 3 days ago
- **OpenAI Agents SDK** [`v0.19.4`](https://github.com/openai/openai-agents-python/releases/tag/v0.19.4) — 5 days ago

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

*Powered by GitHub Actions • Data refreshed daily • Last run: 2026-08-10 07:50 UTC*