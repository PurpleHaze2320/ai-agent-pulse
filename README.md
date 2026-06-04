# 🔬 AI Agent Framework Pulse Tracker

[![Daily Update](https://github.com/PurpleHaze2320/ai-agent-pulse/actions/workflows/track.yml/badge.svg)](https://github.com/PurpleHaze2320/ai-agent-pulse/actions/workflows/track.yml)
[![Frameworks Tracked](https://img.shields.io/badge/frameworks-19-blue)](https://github.com/PurpleHaze2320/ai-agent-pulse)
[![License: MIT](https://img.shields.io/badge/License-MIT-green.svg)](https://opensource.org/licenses/MIT)
[![GitHub stars](https://img.shields.io/github/stars/PurpleHaze2320/ai-agent-pulse?style=social)](https://github.com/PurpleHaze2320/ai-agent-pulse/stargazers)

> Automated daily tracking of the AI agent framework ecosystem's health, momentum, and trends.
> Last updated: **2026-06-04 10:04 UTC** | Tracking **19** frameworks

## How It Works

This bot runs daily via GitHub Actions and collects metrics from the GitHub API for the most important
AI agent frameworks. It computes a **Pulse Score** (0-100) based on six weighted signals: star velocity,
release freshness, issue health, commit activity, community size, and fork engagement. The result is
a living dashboard that shows which frameworks are gaining momentum and which are losing steam.

## 🏆 Pulse Leaderboard

| Rank | Framework | Pulse | Stars | ⭐ 7d | Commits (4w) | Last Release | Category |
|------|-----------|-------|-------|-------|--------------|--------------|----------|
| 1 | [Mastra](https://github.com/mastra-ai/mastra) | 🟢 **81.9** | 24.7k | 🚀 +298 | 902 | today | `typescript` |
| 2 | [CrewAI](https://github.com/crewAIInc/crewAI) | 🟢 **70.5** | 52.8k | 🚀 +461 | 0 | today | `multi-agent` |
| 3 | [BrowserUse](https://github.com/browser-use/browser-use) | 🟡 **69.6** | 97.1k | 🚀 +1150 | 0 | 9 days ago | `web-agent` |
| 4 | [LangGraph](https://github.com/langchain-ai/langgraph) | 🟡 **68.6** | 33.8k | 🚀 +612 | 0 | 1 day ago | `orchestration` |
| 5 | [Claude Agent SDK](https://github.com/anthropics/claude-code) | 🟡 **65.6** | 130.0k | 🚀 +2835 | 0 | today | `orchestration` |
| 6 | [LlamaIndex](https://github.com/run-llama/llama_index) | 🟡 **58.2** | 49.9k | 🚀 +186 | 0 | 20 days ago | `data-agent` |
| 7 | [OpenAI Agents SDK](https://github.com/openai/openai-agents-python) | 🟡 **56.0** | 26.9k | 🚀 +188 | 0 | 9 days ago | `orchestration` |
| 8 | [PydanticAI](https://github.com/pydantic/pydantic-ai) | 🟡 **54.3** | 17.5k | 🚀 +152 | 0 | 2 days ago | `structured` |
| 9 | [Agno](https://github.com/agno-agi/agno) | 🟡 **52.9** | 40.5k | 🚀 +117 | 0 | 1 day ago | `multi-agent` |
| 10 | [Semantic Kernel](https://github.com/microsoft/semantic-kernel) | 🟡 **51.7** | 28.0k | 📈 +52 | 0 | today | `enterprise` |
| 11 | [DSPy](https://github.com/stanfordnlp/dspy) | 🟡 **50.5** | 34.8k | 🚀 +140 | 0 | 7 days ago | `optimization` |
| 12 | [Google ADK](https://github.com/google/adk-python) | 🟡 **50.2** | 20.0k | 📈 +87 | 0 | 2 days ago | `orchestration` |
| 13 | [Haystack](https://github.com/deepset-ai/haystack) | 🟡 **49.6** | 25.5k | 📈 +57 | 0 | today | `pipeline` |
| 14 | [AG2](https://github.com/ag2ai/ag2) | 🟡 **48.5** | 4.6k | 📈 +24 | 0 | 6 days ago | `multi-agent` |
| 15 | [Letta](https://github.com/letta-ai/letta) | 🟡 **47.4** | 23.1k | 🚀 +124 | 0 | 20 days ago | `memory` |
| 16 | [Composio](https://github.com/ComposioHQ/composio) | 🟡 **46.7** | 28.6k | 🚀 +115 | 0 | 15 days ago | `tooling` |
| 17 | [Smolagents](https://github.com/huggingface/smolagents) | 🟡 **44.6** | 27.7k | 🚀 +136 | 0 | 6 days ago | `lightweight` |
| 18 | [AutoGen](https://github.com/microsoft/autogen) | 🟡 **41.7** | 58.7k | 🚀 +206 | 0 | 8 mo ago | `multi-agent` |
| 19 | [Swarm](https://github.com/openai/swarm) | 🔴 **9.5** | 21.6k | 📈 +37 | 0 | — | `experimental` |

## 📂 By Category

- `data-agent`: **LlamaIndex** (58.2)
- `enterprise`: **Semantic Kernel** (51.7)
- `experimental`: **Swarm** (9.5)
- `lightweight`: **Smolagents** (44.6)
- `memory`: **Letta** (47.4)
- `multi-agent`: **CrewAI** (70.5), **Agno** (52.9), **AG2** (48.5), **AutoGen** (41.7)
- `optimization`: **DSPy** (50.5)
- `orchestration`: **LangGraph** (68.6), **Claude Agent SDK** (65.6), **OpenAI Agents SDK** (56.0), **Google ADK** (50.2)
- `pipeline`: **Haystack** (49.6)
- `structured`: **PydanticAI** (54.3)
- `tooling`: **Composio** (46.7)
- `typescript`: **Mastra** (81.9)
- `web-agent`: **BrowserUse** (69.6)

## 🔍 Top 5 — Score Breakdown

| Framework | Star Velocity | Release Freshness | Issue Health | Commit Activity | Community | Fork Ratio |
|-----------|:---:|:---:|:---:|:---:|:---:|:---:|
| **Mastra** | 59.2 | 100.0 | 95.7 | 100 | 92.0 | 35.5 |
| **CrewAI** | 97.1 | 100.0 | 98.0 | 0.0 | 59.4 | 55.9 |
| **BrowserUse** | 100 | 97.0 | 95.9 | 0.0 | 63.0 | 44.7 |
| **LangGraph** | 100 | 99.7 | 76.0 | 0.0 | 55.0 | 67.3 |
| **Claude Agent SDK** | 100 | 100.0 | 87.4 | 0.0 | 10.2 | 65.0 |

## 💡 Key Insights

- **Hottest framework**: Mastra with a Pulse Score of 81.9
- **Fastest growing**: Claude Agent SDK gained +2835 stars this week
- **Most active development**: Mastra with 902 commits in the last 4 weeks
- **Stale releases**: Swarm haven't released in a while

## 📦 Recent Releases

- **Semantic Kernel** [`python-1.43.0`](https://github.com/microsoft/semantic-kernel/releases/tag/python-1.43.0) — today
- **Claude Agent SDK** [`v2.1.162`](https://github.com/anthropics/claude-code/releases/tag/v2.1.162) — today
- **Mastra** [`@mastra/core@1.38.0`](https://github.com/mastra-ai/mastra/releases/tag/@mastra/core@1.38.0) — today
- **CrewAI** [`1.14.7a1`](https://github.com/crewAIInc/crewAI/releases/tag/1.14.7a1) — today *(pre-release)*
- **Haystack** [`v2.30.0`](https://github.com/deepset-ai/haystack/releases/tag/v2.30.0) — today
- **LangGraph** [`1.2.4`](https://github.com/langchain-ai/langgraph/releases/tag/1.2.4) — 1 day ago
- **Agno** [`v2.6.11`](https://github.com/agno-agi/agno/releases/tag/v2.6.11) — 1 day ago
- **PydanticAI** [`v2.0.0b5`](https://github.com/pydantic/pydantic-ai/releases/tag/v2.0.0b5) — 2 days ago *(pre-release)*
- **Google ADK** [`v1.34.2`](https://github.com/google/adk-python/releases/tag/v1.34.2) — 2 days ago
- **Smolagents** [`v1.26.0`](https://github.com/huggingface/smolagents/releases/tag/v1.26.0) — 6 days ago

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

*Powered by GitHub Actions • Data refreshed daily • Last run: 2026-06-04 10:04 UTC*