# 🔬 AI Agent Framework Pulse Tracker

[![Daily Update](https://github.com/PurpleHaze2320/ai-agent-pulse/actions/workflows/track.yml/badge.svg)](https://github.com/PurpleHaze2320/ai-agent-pulse/actions/workflows/track.yml)
[![Frameworks Tracked](https://img.shields.io/badge/frameworks-19-blue)](https://github.com/PurpleHaze2320/ai-agent-pulse)
[![License: MIT](https://img.shields.io/badge/License-MIT-green.svg)](https://opensource.org/licenses/MIT)
[![GitHub stars](https://img.shields.io/github/stars/PurpleHaze2320/ai-agent-pulse?style=social)](https://github.com/PurpleHaze2320/ai-agent-pulse/stargazers)

> Automated daily tracking of the AI agent framework ecosystem's health, momentum, and trends.
> Last updated: **2026-06-12 10:22 UTC** | Tracking **19** frameworks

## How It Works

This bot runs daily via GitHub Actions and collects metrics from the GitHub API for the most important
AI agent frameworks. It computes a **Pulse Score** (0-100) based on six weighted signals: star velocity,
release freshness, issue health, commit activity, community size, and fork engagement. The result is
a living dashboard that shows which frameworks are gaining momentum and which are losing steam.

## 🏆 Pulse Leaderboard

| Rank | Framework | Pulse | Stars | ⭐ 7d | Commits (4w) | Last Release | Category |
|------|-----------|-------|-------|-------|--------------|--------------|----------|
| 1 | [BrowserUse](https://github.com/browser-use/browser-use) | 🟢 **90.0** | 98.4k | 🚀 +1129 | 442 | 2 days ago | `web-agent` |
| 2 | [CrewAI](https://github.com/crewAIInc/crewAI) | 🟢 **88.9** | 53.3k | 🚀 +436 | 112 | today | `multi-agent` |
| 3 | [LangGraph](https://github.com/langchain-ai/langgraph) | 🟢 **86.6** | 34.5k | 🚀 +550 | 90 | today | `orchestration` |
| 4 | [Mastra](https://github.com/mastra-ai/mastra) | 🟢 **77.5** | 25.0k | 🚀 +188 | 910 | 7 days ago | `typescript` |
| 5 | [Claude Agent SDK](https://github.com/anthropics/claude-code) | 🟢 **72.7** | 132.0k | 🚀 +1640 | 36 | today | `orchestration` |
| 6 | [Haystack](https://github.com/deepset-ai/haystack) | 🟢 **70.4** | 25.5k | 📈 +84 | 123 | 2 days ago | `pipeline` |
| 7 | [Google ADK](https://github.com/google/adk-python) | 🟢 **70.0** | 20.1k | 📈 +89 | 210 | 2 days ago | `orchestration` |
| 8 | [LlamaIndex](https://github.com/run-llama/llama_index) | 🟡 **67.3** | 50.1k | 🚀 +164 | 53 | 28 days ago | `data-agent` |
| 9 | [AG2](https://github.com/ag2ai/ag2) | 🟡 **64.2** | 4.7k | 📈 +29 | 78 | 7 days ago | `multi-agent` |
| 10 | [OpenAI Agents SDK](https://github.com/openai/openai-agents-python) | 🟡 **61.8** | 27.1k | 🚀 +165 | 34 | 1 day ago | `orchestration` |
| 11 | [DSPy](https://github.com/stanfordnlp/dspy) | 🟡 **58.5** | 35.0k | 🚀 +138 | 43 | 15 days ago | `optimization` |
| 12 | [PydanticAI](https://github.com/pydantic/pydantic-ai) | 🟡 **55.1** | 17.7k | 🚀 +186 | 97 | — | `structured` |
| 13 | [Composio](https://github.com/ComposioHQ/composio) | 🟡 **53.8** | 28.7k | 🚀 +101 | 34 | 3 days ago | `tooling` |
| 14 | [Agno](https://github.com/agno-agi/agno) | 🟡 **53.0** | 40.7k | 🚀 +124 | 0 | 1 day ago | `multi-agent` |
| 15 | [Semantic Kernel](https://github.com/microsoft/semantic-kernel) | 🟡 **52.6** | 28.1k | 📈 +53 | 7 | 8 days ago | `enterprise` |
| 16 | [Letta](https://github.com/letta-ai/letta) | 🟡 **47.0** | 23.3k | 🚀 +139 | 0 | 28 days ago | `memory` |
| 17 | [Smolagents](https://github.com/huggingface/smolagents) | 🟡 **44.1** | 27.8k | 🚀 +109 | 6 | 14 days ago | `lightweight` |
| 18 | [AutoGen](https://github.com/microsoft/autogen) | 🟡 **40.3** | 58.9k | 🚀 +190 | 0 | 8 mo ago | `multi-agent` |
| 19 | [Swarm](https://github.com/openai/swarm) | 🔴 **9.8** | 21.6k | 📈 +37 | 0 | — | `experimental` |

## 📂 By Category

- `data-agent`: **LlamaIndex** (67.3)
- `enterprise`: **Semantic Kernel** (52.6)
- `experimental`: **Swarm** (9.8)
- `lightweight`: **Smolagents** (44.1)
- `memory`: **Letta** (47.0)
- `multi-agent`: **CrewAI** (88.9), **AG2** (64.2), **Agno** (53.0), **AutoGen** (40.3)
- `optimization`: **DSPy** (58.5)
- `orchestration`: **LangGraph** (86.6), **Claude Agent SDK** (72.7), **Google ADK** (70.0), **OpenAI Agents SDK** (61.8)
- `pipeline`: **Haystack** (70.4)
- `structured`: **PydanticAI** (55.1)
- `tooling`: **Composio** (53.8)
- `typescript`: **Mastra** (77.5)
- `web-agent`: **BrowserUse** (90.0)

## 🔍 Top 5 — Score Breakdown

| Framework | Star Velocity | Release Freshness | Issue Health | Commit Activity | Community | Fork Ratio |
|-----------|:---:|:---:|:---:|:---:|:---:|:---:|
| **BrowserUse** | 100 | 99.3 | 95.9 | 100 | 63.0 | 44.6 |
| **CrewAI** | 91.1 | 100.0 | 97.1 | 100 | 59.4 | 56.0 |
| **LangGraph** | 100 | 100.0 | 75.6 | 90.0 | 55.0 | 67.2 |
| **Mastra** | 43.6 | 97.7 | 95.2 | 100 | 92.0 | 35.5 |
| **Claude Agent SDK** | 100 | 100.0 | 86.7 | 36.0 | 10.2 | 64.8 |

## 💡 Key Insights

- **Hottest framework**: BrowserUse with a Pulse Score of 90.0
- **Fastest growing**: Claude Agent SDK gained +1640 stars this week
- **Most active development**: Mastra with 910 commits in the last 4 weeks
- **Stale releases**: PydanticAI, Swarm haven't released in a while

## 📦 Recent Releases

- **Claude Agent SDK** [`v2.1.175`](https://github.com/anthropics/claude-code/releases/tag/v2.1.175) — today
- **LangGraph** [`cli==0.4.29`](https://github.com/langchain-ai/langgraph/releases/tag/cli==0.4.29) — today
- **CrewAI** [`1.14.7`](https://github.com/crewAIInc/crewAI/releases/tag/1.14.7) — today
- **OpenAI Agents SDK** [`v0.17.5`](https://github.com/openai/openai-agents-python/releases/tag/v0.17.5) — 1 day ago
- **Agno** [`v2.6.13`](https://github.com/agno-agi/agno/releases/tag/v2.6.13) — 1 day ago
- **Google ADK** [`v1.35.0`](https://github.com/google/adk-python/releases/tag/v1.35.0) — 2 days ago
- **BrowserUse** [`0.13.1`](https://github.com/browser-use/browser-use/releases/tag/0.13.1) — 2 days ago
- **Haystack** [`v2.30.1`](https://github.com/deepset-ai/haystack/releases/tag/v2.30.1) — 2 days ago
- **Composio** [`@composio/cli@0.2.31`](https://github.com/ComposioHQ/composio/releases/tag/@composio/cli@0.2.31) — 3 days ago
- **Mastra** [`@mastra/core@1.41.0`](https://github.com/mastra-ai/mastra/releases/tag/@mastra/core@1.41.0) — 7 days ago

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

*Powered by GitHub Actions • Data refreshed daily • Last run: 2026-06-12 10:22 UTC*