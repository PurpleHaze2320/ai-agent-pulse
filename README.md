# 🔬 AI Agent Framework Pulse Tracker

[![Daily Update](https://github.com/PurpleHaze2320/ai-agent-pulse/actions/workflows/track.yml/badge.svg)](https://github.com/PurpleHaze2320/ai-agent-pulse/actions/workflows/track.yml)
[![Frameworks Tracked](https://img.shields.io/badge/frameworks-19-blue)](https://github.com/PurpleHaze2320/ai-agent-pulse)
[![License: MIT](https://img.shields.io/badge/License-MIT-green.svg)](https://opensource.org/licenses/MIT)
[![GitHub stars](https://img.shields.io/github/stars/PurpleHaze2320/ai-agent-pulse?style=social)](https://github.com/PurpleHaze2320/ai-agent-pulse/stargazers)

> Automated daily tracking of the AI agent framework ecosystem's health, momentum, and trends.
> Last updated: **2026-09-19 10:38 UTC** | Tracking **19** frameworks

## How It Works

This bot runs daily via GitHub Actions and collects metrics from the GitHub API for the most important
AI agent frameworks. It computes a **Pulse Score** (0-100) based on six weighted signals: star velocity,
release freshness, issue health, commit activity, community size, and fork engagement. The result is
a living dashboard that shows which frameworks are gaining momentum and which are losing steam.

## 🏆 Pulse Leaderboard

| Rank | Framework | Pulse | Stars | ⭐ 7d | Commits (4w) | Last Release | Category |
|------|-----------|-------|-------|-------|--------------|--------------|----------|
| 1 | [BrowserUse](https://github.com/browser-use/browser-use) | 🟢 **89.4** | 115.2k | 🚀 +952 | 204 | 15 days ago | `web-agent` |
| 2 | [Claude Agent SDK](https://github.com/anthropics/claude-code) | 🟢 **85.7** | 146.5k | 🚀 +1674 | 116 | today | `orchestration` |
| 3 | [CrewAI](https://github.com/crewAIInc/crewAI) | 🟢 **83.9** | 58.8k | 🚀 +352 | 124 | 2 days ago | `multi-agent` |
| 4 | [Mastra](https://github.com/mastra-ai/mastra) | 🟢 **78.2** | 28.2k | 🚀 +214 | 1822 | 3 days ago | `typescript` |
| 5 | [OpenAI Agents SDK](https://github.com/openai/openai-agents-python) | 🟢 **77.8** | 29.6k | 🚀 +177 | 117 | 1 day ago | `orchestration` |
| 6 | [PydanticAI](https://github.com/pydantic/pydantic-ai) | 🟢 **75.2** | 20.0k | 🚀 +167 | 284 | today | `structured` |
| 7 | [Google ADK](https://github.com/google/adk-python) | 🟢 **73.4** | 21.6k | 📈 +67 | 422 | today | `orchestration` |
| 8 | [Agno](https://github.com/agno-agi/agno) | 🟢 **70.8** | 42.2k | 🚀 +101 | 125 | 2 days ago | `multi-agent` |
| 9 | [Haystack](https://github.com/deepset-ai/haystack) | 🟢 **70.5** | 26.5k | 📈 +62 | 196 | 16 days ago | `pipeline` |
| 10 | [LangGraph](https://github.com/langchain-ai/langgraph) | 🟡 **69.7** | 41.9k | 🚀 +412 | 38 | 22 days ago | `orchestration` |
| 11 | [Composio](https://github.com/ComposioHQ/composio) | 🟡 **67.6** | 30.2k | 📈 +97 | 326 | 1 day ago | `tooling` |
| 12 | [DSPy](https://github.com/stanfordnlp/dspy) | 🟡 **64.1** | 38.1k | 🚀 +165 | 62 | 7 days ago | `optimization` |
| 13 | [LlamaIndex](https://github.com/run-llama/llama_index) | 🟡 **60.9** | 52.2k | 📈 +96 | 37 | 1 mo ago | `data-agent` |
| 14 | [AG2](https://github.com/ag2ai/ag2) | 🟡 **58.9** | 4.9k | ↗️ +20 | 46 | 7 days ago | `multi-agent` |
| 15 | [Semantic Kernel](https://github.com/microsoft/semantic-kernel) | 🟡 **53.8** | 28.6k | 📈 +26 | 20 | 15 days ago | `enterprise` |
| 16 | [Letta](https://github.com/letta-ai/letta) | 🟠 **39.0** | 24.8k | 📈 +87 | 3 | 4 mo ago | `memory` |
| 17 | [Smolagents](https://github.com/huggingface/smolagents) | 🟠 **35.6** | 29.4k | 🚀 +106 | 0 | 3 mo ago | `lightweight` |
| 18 | [AutoGen](https://github.com/microsoft/autogen) | 🟠 **33.3** | 61.1k | 🚀 +119 | 0 | 11 mo ago | `multi-agent` |
| 19 | [Swarm](https://github.com/openai/swarm) | 🔴 **9.4** | 22.0k | ↗️ +18 | 0 | — | `experimental` |

## 📂 By Category

- `data-agent`: **LlamaIndex** (60.9)
- `enterprise`: **Semantic Kernel** (53.8)
- `experimental`: **Swarm** (9.4)
- `lightweight`: **Smolagents** (35.6)
- `memory`: **Letta** (39.0)
- `multi-agent`: **CrewAI** (83.9), **Agno** (70.8), **AG2** (58.9), **AutoGen** (33.3)
- `optimization`: **DSPy** (64.1)
- `orchestration`: **Claude Agent SDK** (85.7), **OpenAI Agents SDK** (77.8), **Google ADK** (73.4), **LangGraph** (69.7)
- `pipeline`: **Haystack** (70.5)
- `structured`: **PydanticAI** (75.2)
- `tooling`: **Composio** (67.6)
- `typescript`: **Mastra** (78.2)
- `web-agent`: **BrowserUse** (89.4)

## 🔍 Top 5 — Score Breakdown

| Framework | Star Velocity | Release Freshness | Issue Health | Commit Activity | Community | Fork Ratio |
|-----------|:---:|:---:|:---:|:---:|:---:|:---:|
| **BrowserUse** | 100 | 95.0 | 91.7 | 100 | 72.2 | 44.0 |
| **Claude Agent SDK** | 100 | 100.0 | 87.4 | 100 | 10.8 | 65.1 |
| **CrewAI** | 70.3 | 99.3 | 93.4 | 100 | 67.0 | 57.9 |
| **Mastra** | 42.9 | 99.0 | 95.6 | 100 | 93.2 | 40.1 |
| **OpenAI Agents SDK** | 36.5 | 99.7 | 98.2 | 100 | 75.4 | 64.5 |

## 💡 Key Insights

- **Hottest framework**: BrowserUse with a Pulse Score of 89.4
- **Fastest growing**: Claude Agent SDK gained +1674 stars this week
- **Most active development**: Mastra with 1822 commits in the last 4 weeks
- **Stale releases**: AutoGen, Swarm haven't released in a while

## 📦 Recent Releases

- **PydanticAI** [`v2.46.0`](https://github.com/pydantic/pydantic-ai/releases/tag/v2.46.0) — today
- **Claude Agent SDK** [`v2.1.278`](https://github.com/anthropics/claude-code/releases/tag/v2.1.278) — today
- **Google ADK** [`v2.9.2`](https://github.com/google/adk-python/releases/tag/v2.9.2) — today
- **OpenAI Agents SDK** [`v0.22.3`](https://github.com/openai/openai-agents-python/releases/tag/v0.22.3) — 1 day ago
- **Composio** [`@composio/cli@0.4.2-beta.398`](https://github.com/ComposioHQ/composio/releases/tag/@composio/cli@0.4.2-beta.398) — 1 day ago *(pre-release)*
- **CrewAI** [`1.15.22`](https://github.com/crewAIInc/crewAI/releases/tag/1.15.22) — 2 days ago
- **Agno** [`v3.0.10`](https://github.com/agno-agi/agno/releases/tag/v3.0.10) — 2 days ago
- **Mastra** [`@mastra/core@1.67.0`](https://github.com/mastra-ai/mastra/releases/tag/@mastra/core@1.67.0) — 3 days ago
- **DSPy** [`3.4.0b1`](https://github.com/stanfordnlp/dspy/releases/tag/3.4.0b1) — 7 days ago *(pre-release)*
- **AG2** [`v1.0.5`](https://github.com/ag2ai/ag2/releases/tag/v1.0.5) — 7 days ago

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

*Powered by GitHub Actions • Data refreshed daily • Last run: 2026-09-19 10:38 UTC*