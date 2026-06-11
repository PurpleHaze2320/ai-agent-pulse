# 🔬 AI Agent Framework Pulse Tracker

[![Daily Update](https://github.com/PurpleHaze2320/ai-agent-pulse/actions/workflows/track.yml/badge.svg)](https://github.com/PurpleHaze2320/ai-agent-pulse/actions/workflows/track.yml)
[![Frameworks Tracked](https://img.shields.io/badge/frameworks-19-blue)](https://github.com/PurpleHaze2320/ai-agent-pulse)
[![License: MIT](https://img.shields.io/badge/License-MIT-green.svg)](https://opensource.org/licenses/MIT)
[![GitHub stars](https://img.shields.io/github/stars/PurpleHaze2320/ai-agent-pulse?style=social)](https://github.com/PurpleHaze2320/ai-agent-pulse/stargazers)

> Automated daily tracking of the AI agent framework ecosystem's health, momentum, and trends.
> Last updated: **2026-06-11 10:47 UTC** | Tracking **19** frameworks

## How It Works

This bot runs daily via GitHub Actions and collects metrics from the GitHub API for the most important
AI agent frameworks. It computes a **Pulse Score** (0-100) based on six weighted signals: star velocity,
release freshness, issue health, commit activity, community size, and fork engagement. The result is
a living dashboard that shows which frameworks are gaining momentum and which are losing steam.

## 🏆 Pulse Leaderboard

| Rank | Framework | Pulse | Stars | ⭐ 7d | Commits (4w) | Last Release | Category |
|------|-----------|-------|-------|-------|--------------|--------------|----------|
| 1 | [BrowserUse](https://github.com/browser-use/browser-use) | 🟢 **90.1** | 98.2k | 🚀 +1122 | 439 | 1 day ago | `web-agent` |
| 2 | [CrewAI](https://github.com/crewAIInc/crewAI) | 🟢 **89.4** | 53.3k | 🚀 +448 | 108 | today | `multi-agent` |
| 3 | [LangGraph](https://github.com/langchain-ai/langgraph) | 🟢 **86.4** | 34.4k | 🚀 +592 | 89 | today | `orchestration` |
| 4 | [Mastra](https://github.com/mastra-ai/mastra) | 🟢 **78.5** | 25.0k | 🚀 +214 | 862 | 6 days ago | `typescript` |
| 5 | [PydanticAI](https://github.com/pydantic/pydantic-ai) | 🟢 **73.6** | 17.7k | 🚀 +183 | 90 | today | `structured` |
| 6 | [Agno](https://github.com/agno-agi/agno) | 🟢 **73.1** | 40.6k | 🚀 +126 | 125 | today | `multi-agent` |
| 7 | [Claude Agent SDK](https://github.com/anthropics/claude-code) | 🟢 **72.3** | 131.7k | 🚀 +1694 | 34 | today | `orchestration` |
| 8 | [Haystack](https://github.com/deepset-ai/haystack) | 🟢 **70.2** | 25.5k | 📈 +77 | 116 | 1 day ago | `pipeline` |
| 9 | [Google ADK](https://github.com/google/adk-python) | 🟢 **70.0** | 20.1k | 📈 +86 | 184 | 1 day ago | `orchestration` |
| 10 | [AG2](https://github.com/ag2ai/ag2) | 🟡 **63.1** | 4.7k | 📈 +30 | 72 | 6 days ago | `multi-agent` |
| 11 | [OpenAI Agents SDK](https://github.com/openai/openai-agents-python) | 🟡 **62.3** | 27.1k | 🚀 +173 | 34 | today | `orchestration` |
| 12 | [DSPy](https://github.com/stanfordnlp/dspy) | 🟡 **57.2** | 35.0k | 🚀 +142 | 35 | 14 days ago | `optimization` |
| 13 | [LlamaIndex](https://github.com/run-llama/llama_index) | 🟡 **56.9** | 50.1k | 🚀 +168 | 0 | 27 days ago | `data-agent` |
| 14 | [Composio](https://github.com/ComposioHQ/composio) | 🟡 **53.3** | 28.7k | 🚀 +114 | 29 | 2 days ago | `tooling` |
| 15 | [Semantic Kernel](https://github.com/microsoft/semantic-kernel) | 🟡 **52.8** | 28.1k | 📈 +56 | 7 | 7 days ago | `enterprise` |
| 16 | [Letta](https://github.com/letta-ai/letta) | 🟡 **46.7** | 23.3k | 🚀 +128 | 0 | 27 days ago | `memory` |
| 17 | [Smolagents](https://github.com/huggingface/smolagents) | 🟡 **44.5** | 27.8k | 🚀 +116 | 6 | 13 days ago | `lightweight` |
| 18 | [AutoGen](https://github.com/microsoft/autogen) | 🟡 **40.1** | 58.9k | 🚀 +181 | 0 | 8 mo ago | `multi-agent` |
| 19 | [Swarm](https://github.com/openai/swarm) | 🔴 **9.7** | 21.6k | 📈 +34 | 0 | — | `experimental` |

## 📂 By Category

- `data-agent`: **LlamaIndex** (56.9)
- `enterprise`: **Semantic Kernel** (52.8)
- `experimental`: **Swarm** (9.7)
- `lightweight`: **Smolagents** (44.5)
- `memory`: **Letta** (46.7)
- `multi-agent`: **CrewAI** (89.4), **Agno** (73.1), **AG2** (63.1), **AutoGen** (40.1)
- `optimization`: **DSPy** (57.2)
- `orchestration`: **LangGraph** (86.4), **Claude Agent SDK** (72.3), **Google ADK** (70.0), **OpenAI Agents SDK** (62.3)
- `pipeline`: **Haystack** (70.2)
- `structured`: **PydanticAI** (73.6)
- `tooling`: **Composio** (53.3)
- `typescript`: **Mastra** (78.5)
- `web-agent`: **BrowserUse** (90.1)

## 🔍 Top 5 — Score Breakdown

| Framework | Star Velocity | Release Freshness | Issue Health | Commit Activity | Community | Fork Ratio |
|-----------|:---:|:---:|:---:|:---:|:---:|:---:|
| **BrowserUse** | 100 | 99.7 | 95.9 | 100 | 63.0 | 44.6 |
| **CrewAI** | 93.3 | 100.0 | 97.3 | 100 | 59.4 | 55.9 |
| **LangGraph** | 100 | 100.0 | 75.7 | 89.0 | 55.0 | 67.2 |
| **Mastra** | 47.4 | 98.0 | 95.4 | 100 | 92.0 | 35.5 |
| **PydanticAI** | 35.8 | 100.0 | 82.5 | 90.0 | 93.0 | 49.9 |

## 💡 Key Insights

- **Hottest framework**: BrowserUse with a Pulse Score of 90.1
- **Fastest growing**: Claude Agent SDK gained +1694 stars this week
- **Most active development**: Mastra with 862 commits in the last 4 weeks
- **Stale releases**: Swarm haven't released in a while

## 📦 Recent Releases

- **Claude Agent SDK** [`v2.1.173`](https://github.com/anthropics/claude-code/releases/tag/v2.1.173) — today
- **OpenAI Agents SDK** [`v0.17.5`](https://github.com/openai/openai-agents-python/releases/tag/v0.17.5) — today
- **CrewAI** [`1.14.7rc2`](https://github.com/crewAIInc/crewAI/releases/tag/1.14.7rc2) — today *(pre-release)*
- **Agno** [`v2.6.13`](https://github.com/agno-agi/agno/releases/tag/v2.6.13) — today
- **LangGraph** [`cli==0.4.28`](https://github.com/langchain-ai/langgraph/releases/tag/cli==0.4.28) — today
- **PydanticAI** [`v2.0.0b7`](https://github.com/pydantic/pydantic-ai/releases/tag/v2.0.0b7) — today *(pre-release)*
- **Google ADK** [`v1.35.0`](https://github.com/google/adk-python/releases/tag/v1.35.0) — 1 day ago
- **BrowserUse** [`0.13.1`](https://github.com/browser-use/browser-use/releases/tag/0.13.1) — 1 day ago
- **Haystack** [`v2.30.1`](https://github.com/deepset-ai/haystack/releases/tag/v2.30.1) — 1 day ago
- **Composio** [`@composio/cli@0.2.31`](https://github.com/ComposioHQ/composio/releases/tag/@composio/cli@0.2.31) — 2 days ago

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

*Powered by GitHub Actions • Data refreshed daily • Last run: 2026-06-11 10:47 UTC*