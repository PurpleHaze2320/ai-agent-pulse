# 🔬 AI Agent Framework Pulse Tracker

[![Daily Update](https://github.com/PurpleHaze2320/ai-agent-pulse/actions/workflows/track.yml/badge.svg)](https://github.com/PurpleHaze2320/ai-agent-pulse/actions/workflows/track.yml)
[![Frameworks Tracked](https://img.shields.io/badge/frameworks-19-blue)](https://github.com/PurpleHaze2320/ai-agent-pulse)
[![License: MIT](https://img.shields.io/badge/License-MIT-green.svg)](https://opensource.org/licenses/MIT)
[![GitHub stars](https://img.shields.io/github/stars/PurpleHaze2320/ai-agent-pulse?style=social)](https://github.com/PurpleHaze2320/ai-agent-pulse/stargazers)

> Automated daily tracking of the AI agent framework ecosystem's health, momentum, and trends.
> Last updated: **2026-08-07 07:23 UTC** | Tracking **19** frameworks

## How It Works

This bot runs daily via GitHub Actions and collects metrics from the GitHub API for the most important
AI agent frameworks. It computes a **Pulse Score** (0-100) based on six weighted signals: star velocity,
release freshness, issue health, commit activity, community size, and fork engagement. The result is
a living dashboard that shows which frameworks are gaining momentum and which are losing steam.

## 🏆 Pulse Leaderboard

| Rank | Framework | Pulse | Stars | ⭐ 7d | Commits (4w) | Last Release | Category |
|------|-----------|-------|-------|-------|--------------|--------------|----------|
| 1 | [BrowserUse](https://github.com/browser-use/browser-use) | 🟢 **89.5** | 108.1k | 🚀 +751 | 172 | 10 days ago | `web-agent` |
| 2 | [Mastra](https://github.com/mastra-ai/mastra) | 🟢 **79.8** | 27.0k | 🚀 +245 | 1336 | today | `typescript` |
| 3 | [CrewAI](https://github.com/crewAIInc/crewAI) | 🟢 **78.9** | 56.7k | 🚀 +305 | 82 | 1 day ago | `multi-agent` |
| 4 | [OpenAI Agents SDK](https://github.com/openai/openai-agents-python) | 🟢 **75.7** | 28.5k | 🚀 +152 | 260 | 2 days ago | `orchestration` |
| 5 | [LangGraph](https://github.com/langchain-ai/langgraph) | 🟢 **74.2** | 39.1k | 🚀 +530 | 34 | 7 days ago | `orchestration` |
| 6 | [Agno](https://github.com/agno-agi/agno) | 🟢 **71.5** | 41.6k | 📈 +92 | 123 | today | `multi-agent` |
| 7 | [Haystack](https://github.com/deepset-ai/haystack) | 🟡 **69.4** | 26.1k | 📈 +60 | 237 | 17 days ago | `pipeline` |
| 8 | [Claude Agent SDK](https://github.com/anthropics/claude-code) | 🟡 **68.6** | 140.5k | 🚀 +795 | 19 | today | `orchestration` |
| 9 | [Composio](https://github.com/ComposioHQ/composio) | 🟡 **67.3** | 29.6k | 📈 +98 | 296 | 1 day ago | `tooling` |
| 10 | [PydanticAI](https://github.com/pydantic/pydantic-ai) | 🟡 **57.0** | 19.1k | 🚀 +189 | 0 | today | `structured` |
| 11 | [LlamaIndex](https://github.com/run-llama/llama_index) | 🟡 **56.6** | 51.4k | 🚀 +188 | 0 | 1 mo ago | `data-agent` |
| 12 | [Google ADK](https://github.com/google/adk-python) | 🟡 **53.1** | 21.0k | 📈 +74 | 0 | 3 days ago | `orchestration` |
| 13 | [DSPy](https://github.com/stanfordnlp/dspy) | 🟡 **52.8** | 36.7k | 🚀 +184 | 0 | 3 days ago | `optimization` |
| 14 | [Semantic Kernel](https://github.com/microsoft/semantic-kernel) | 🟡 **51.0** | 28.4k | 📈 +32 | 0 | today | `enterprise` |
| 15 | [AG2](https://github.com/ag2ai/ag2) | 🟡 **49.5** | 4.8k | ↗️ +17 | 0 | 9 days ago | `multi-agent` |
| 16 | [Letta](https://github.com/letta-ai/letta) | 🟡 **41.2** | 24.1k | 📈 +97 | 0 | 2 mo ago | `memory` |
| 17 | [Smolagents](https://github.com/huggingface/smolagents) | 🟠 **38.4** | 28.7k | 📈 +99 | 0 | 2 mo ago | `lightweight` |
| 18 | [AutoGen](https://github.com/microsoft/autogen) | 🟠 **35.5** | 60.3k | 🚀 +160 | 0 | 10 mo ago | `multi-agent` |
| 19 | [Swarm](https://github.com/openai/swarm) | 🔴 **9.7** | 21.9k | ↗️ +18 | 0 | — | `experimental` |

## 📂 By Category

- `data-agent`: **LlamaIndex** (56.6)
- `enterprise`: **Semantic Kernel** (51.0)
- `experimental`: **Swarm** (9.7)
- `lightweight`: **Smolagents** (38.4)
- `memory`: **Letta** (41.2)
- `multi-agent`: **CrewAI** (78.9), **Agno** (71.5), **AG2** (49.5), **AutoGen** (35.5)
- `optimization`: **DSPy** (52.8)
- `orchestration`: **OpenAI Agents SDK** (75.7), **LangGraph** (74.2), **Claude Agent SDK** (68.6), **Google ADK** (53.1)
- `pipeline`: **Haystack** (69.4)
- `structured`: **PydanticAI** (57.0)
- `tooling`: **Composio** (67.3)
- `typescript`: **Mastra** (79.8)
- `web-agent`: **BrowserUse** (89.5)

## 🔍 Top 5 — Score Breakdown

| Framework | Star Velocity | Release Freshness | Issue Health | Commit Activity | Community | Fork Ratio |
|-----------|:---:|:---:|:---:|:---:|:---:|:---:|
| **BrowserUse** | 100 | 96.7 | 94.3 | 100 | 66.6 | 44.0 |
| **Mastra** | 50.4 | 100.0 | 93.9 | 100 | 92.6 | 38.3 |
| **CrewAI** | 66.6 | 99.7 | 94.9 | 82.0 | 59.8 | 57.0 |
| **OpenAI Agents SDK** | 32.2 | 99.3 | 99.1 | 100 | 66.4 | 62.6 |
| **LangGraph** | 100 | 97.7 | 70.9 | 34.0 | 55.4 | 67.3 |

## 💡 Key Insights

- **Hottest framework**: BrowserUse with a Pulse Score of 89.5
- **Fastest growing**: Claude Agent SDK gained +795 stars this week
- **Most active development**: Mastra with 1336 commits in the last 4 weeks
- **Stale releases**: AutoGen, Swarm haven't released in a while

## 📦 Recent Releases

- **Claude Agent SDK** [`v2.1.224`](https://github.com/anthropics/claude-code/releases/tag/v2.1.224) — today
- **PydanticAI** [`v2.26.0`](https://github.com/pydantic/pydantic-ai/releases/tag/v2.26.0) — today
- **Agno** [`v3.0.0a1`](https://github.com/agno-agi/agno/releases/tag/v3.0.0a1) — today *(pre-release)*
- **Semantic Kernel** [`python-1.44.1`](https://github.com/microsoft/semantic-kernel/releases/tag/python-1.44.1) — today
- **Mastra** [`@mastra/core@1.56.0`](https://github.com/mastra-ai/mastra/releases/tag/@mastra/core@1.56.0) — today
- **Composio** [`@composio/cli@0.3.3-beta.340`](https://github.com/ComposioHQ/composio/releases/tag/@composio/cli@0.3.3-beta.340) — 1 day ago *(pre-release)*
- **CrewAI** [`1.15.12`](https://github.com/crewAIInc/crewAI/releases/tag/1.15.12) — 1 day ago
- **OpenAI Agents SDK** [`v0.19.4`](https://github.com/openai/openai-agents-python/releases/tag/v0.19.4) — 2 days ago
- **Google ADK** [`v2.6.2`](https://github.com/google/adk-python/releases/tag/v2.6.2) — 3 days ago
- **DSPy** [`3.3.0`](https://github.com/stanfordnlp/dspy/releases/tag/3.3.0) — 3 days ago

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

*Powered by GitHub Actions • Data refreshed daily • Last run: 2026-08-07 07:23 UTC*