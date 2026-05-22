# 🔬 AI Agent Framework Pulse Tracker

[![Daily Update](https://github.com/PurpleHaze2320/ai-agent-pulse/actions/workflows/track.yml/badge.svg)](https://github.com/PurpleHaze2320/ai-agent-pulse/actions/workflows/track.yml)
[![Frameworks Tracked](https://img.shields.io/badge/frameworks-19-blue)](https://github.com/PurpleHaze2320/ai-agent-pulse)
[![License: MIT](https://img.shields.io/badge/License-MIT-green.svg)](https://opensource.org/licenses/MIT)
[![GitHub stars](https://img.shields.io/github/stars/PurpleHaze2320/ai-agent-pulse?style=social)](https://github.com/PurpleHaze2320/ai-agent-pulse/stargazers)

> Automated daily tracking of the AI agent framework ecosystem's health, momentum, and trends.
> Last updated: **2026-05-22 09:38 UTC** | Tracking **19** frameworks

## How It Works

This bot runs daily via GitHub Actions and collects metrics from the GitHub API for the most important
AI agent frameworks. It computes a **Pulse Score** (0-100) based on six weighted signals: star velocity,
release freshness, issue health, commit activity, community size, and fork engagement. The result is
a living dashboard that shows which frameworks are gaining momentum and which are losing steam.

## 🏆 Pulse Leaderboard

| Rank | Framework | Pulse | Stars | ⭐ 7d | Commits (4w) | Last Release | Category |
|------|-----------|-------|-------|-------|--------------|--------------|----------|
| 1 | [Mastra](https://github.com/mastra-ai/mastra) | 🟢 **80.0** | 24.2k | 🚀 +286 | 1026 | 3 days ago | `typescript` |
| 2 | [CrewAI](https://github.com/crewAIInc/crewAI) | 🟢 **71.2** | 51.9k | 🚀 +501 | 0 | today | `multi-agent` |
| 3 | [BrowserUse](https://github.com/browser-use/browser-use) | 🟢 **70.0** | 95.1k | 🚀 +1059 | 0 | 3 days ago | `web-agent` |
| 4 | [LangGraph](https://github.com/langchain-ai/langgraph) | 🟡 **68.8** | 32.7k | 🚀 +594 | 0 | today | `orchestration` |
| 5 | [Claude Agent SDK](https://github.com/anthropics/claude-code) | 🟡 **64.8** | 125.7k | 🚀 +1929 | 0 | today | `orchestration` |
| 6 | [OpenAI Agents SDK](https://github.com/openai/openai-agents-python) | 🟡 **62.3** | 26.6k | 🚀 +243 | 0 | 3 days ago | `orchestration` |
| 7 | [LlamaIndex](https://github.com/run-llama/llama_index) | 🟡 **57.9** | 49.6k | 🚀 +152 | 0 | 7 days ago | `data-agent` |
| 8 | [Agno](https://github.com/agno-agi/agno) | 🟡 **54.6** | 40.3k | 🚀 +165 | 0 | today | `multi-agent` |
| 9 | [PydanticAI](https://github.com/pydantic/pydantic-ai) | 🟡 **53.7** | 17.2k | 🚀 +137 | 0 | today | `structured` |
| 10 | [Google ADK](https://github.com/google/adk-python) | 🟡 **52.2** | 19.8k | 🚀 +152 | 0 | 2 days ago | `orchestration` |
| 11 | [Semantic Kernel](https://github.com/microsoft/semantic-kernel) | 🟡 **50.9** | 28.0k | 📈 +48 | 0 | 8 days ago | `enterprise` |
| 12 | [Haystack](https://github.com/deepset-ai/haystack) | 🟡 **50.6** | 25.3k | 🚀 +106 | 0 | 9 days ago | `pipeline` |
| 13 | [DSPy](https://github.com/stanfordnlp/dspy) | 🟡 **50.1** | 34.6k | 🚀 +143 | 0 | 16 days ago | `optimization` |
| 14 | [Composio](https://github.com/ComposioHQ/composio) | 🟡 **48.9** | 28.4k | 🚀 +148 | 0 | 2 days ago | `tooling` |
| 15 | [Letta](https://github.com/letta-ai/letta) | 🟡 **48.9** | 22.9k | 🚀 +151 | 0 | 7 days ago | `memory` |
| 16 | [AG2](https://github.com/ag2ai/ag2) | 🟡 **48.9** | 4.6k | 📈 +41 | 0 | 9 days ago | `multi-agent` |
| 17 | [Smolagents](https://github.com/huggingface/smolagents) | 🟡 **44.5** | 27.4k | 🚀 +130 | 0 | 7 days ago | `lightweight` |
| 18 | [AutoGen](https://github.com/microsoft/autogen) | 🟡 **43.9** | 58.3k | 🚀 +243 | 0 | 7 mo ago | `multi-agent` |
| 19 | [Swarm](https://github.com/openai/swarm) | 🔴 **9.1** | 21.5k | 📈 +30 | 0 | — | `experimental` |

## 📂 By Category

- `data-agent`: **LlamaIndex** (57.9)
- `enterprise`: **Semantic Kernel** (50.9)
- `experimental`: **Swarm** (9.1)
- `lightweight`: **Smolagents** (44.5)
- `memory`: **Letta** (48.9)
- `multi-agent`: **CrewAI** (71.2), **Agno** (54.6), **AG2** (48.9), **AutoGen** (43.9)
- `optimization`: **DSPy** (50.1)
- `orchestration`: **LangGraph** (68.8), **Claude Agent SDK** (64.8), **OpenAI Agents SDK** (62.3), **Google ADK** (52.2)
- `pipeline`: **Haystack** (50.6)
- `structured`: **PydanticAI** (53.7)
- `tooling`: **Composio** (48.9)
- `typescript`: **Mastra** (80.0)
- `web-agent`: **BrowserUse** (70.0)

## 🔍 Top 5 — Score Breakdown

| Framework | Star Velocity | Release Freshness | Issue Health | Commit Activity | Community | Fork Ratio |
|-----------|:---:|:---:|:---:|:---:|:---:|:---:|
| **Mastra** | 54.7 | 99.0 | 95.0 | 100 | 87.6 | 34.8 |
| **CrewAI** | 100 | 100.0 | 98.2 | 0.0 | 59.4 | 55.4 |
| **BrowserUse** | 100 | 99.0 | 96.1 | 0.0 | 63.0 | 45.1 |
| **LangGraph** | 100 | 100.0 | 77.0 | 0.0 | 54.6 | 67.7 |
| **Claude Agent SDK** | 100 | 100.0 | 81.6 | 0.0 | 10.0 | 65.7 |

## 💡 Key Insights

- **Hottest framework**: Mastra with a Pulse Score of 80.0
- **Fastest growing**: Claude Agent SDK gained +1929 stars this week
- **Most active development**: Mastra with 1026 commits in the last 4 weeks
- **Stale releases**: Swarm haven't released in a while

## 📦 Recent Releases

- **PydanticAI** [`v2.0.0b2`](https://github.com/pydantic/pydantic-ai/releases/tag/v2.0.0b2) — today *(pre-release)*
- **Claude Agent SDK** [`v2.1.148`](https://github.com/anthropics/claude-code/releases/tag/v2.1.148) — today
- **Agno** [`v2.6.9`](https://github.com/agno-agi/agno/releases/tag/v2.6.9) — today
- **LangGraph** [`1.2.1`](https://github.com/langchain-ai/langgraph/releases/tag/1.2.1) — today
- **CrewAI** [`1.14.6a1`](https://github.com/crewAIInc/crewAI/releases/tag/1.14.6a1) — today *(pre-release)*
- **Composio** [`@composio/cli@0.2.31-beta.256`](https://github.com/ComposioHQ/composio/releases/tag/@composio/cli@0.2.31-beta.256) — 2 days ago *(pre-release)*
- **Google ADK** [`v2.0.0`](https://github.com/google/adk-python/releases/tag/v2.0.0) — 2 days ago
- **OpenAI Agents SDK** [`v0.17.3`](https://github.com/openai/openai-agents-python/releases/tag/v0.17.3) — 3 days ago
- **BrowserUse** [`0.12.7`](https://github.com/browser-use/browser-use/releases/tag/0.12.7) — 3 days ago
- **Mastra** [`@mastra/core@1.35.0`](https://github.com/mastra-ai/mastra/releases/tag/@mastra/core@1.35.0) — 3 days ago

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

*Powered by GitHub Actions • Data refreshed daily • Last run: 2026-05-22 09:38 UTC*