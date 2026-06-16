# 🔬 AI Agent Framework Pulse Tracker

[![Daily Update](https://github.com/PurpleHaze2320/ai-agent-pulse/actions/workflows/track.yml/badge.svg)](https://github.com/PurpleHaze2320/ai-agent-pulse/actions/workflows/track.yml)
[![Frameworks Tracked](https://img.shields.io/badge/frameworks-19-blue)](https://github.com/PurpleHaze2320/ai-agent-pulse)
[![License: MIT](https://img.shields.io/badge/License-MIT-green.svg)](https://opensource.org/licenses/MIT)
[![GitHub stars](https://img.shields.io/github/stars/PurpleHaze2320/ai-agent-pulse?style=social)](https://github.com/PurpleHaze2320/ai-agent-pulse/stargazers)

> Automated daily tracking of the AI agent framework ecosystem's health, momentum, and trends.
> Last updated: **2026-06-16 11:21 UTC** | Tracking **19** frameworks

## How It Works

This bot runs daily via GitHub Actions and collects metrics from the GitHub API for the most important
AI agent frameworks. It computes a **Pulse Score** (0-100) based on six weighted signals: star velocity,
release freshness, issue health, commit activity, community size, and fork engagement. The result is
a living dashboard that shows which frameworks are gaining momentum and which are losing steam.

## 🏆 Pulse Leaderboard

| Rank | Framework | Pulse | Stars | ⭐ 7d | Commits (4w) | Last Release | Category |
|------|-----------|-------|-------|-------|--------------|--------------|----------|
| 1 | [CrewAI](https://github.com/crewAIInc/crewAI) | 🟢 **90.2** | 53.7k | 🚀 +557 | 97 | 4 days ago | `multi-agent` |
| 2 | [BrowserUse](https://github.com/browser-use/browser-use) | 🟢 **89.9** | 99.1k | 🚀 +1194 | 408 | 3 days ago | `web-agent` |
| 3 | [LangGraph](https://github.com/langchain-ai/langgraph) | 🟢 **81.6** | 34.9k | 🚀 +661 | 67 | 3 days ago | `orchestration` |
| 4 | [Mastra](https://github.com/mastra-ai/mastra) | 🟢 **79.5** | 25.1k | 🚀 +234 | 780 | 3 days ago | `typescript` |
| 5 | [Agno](https://github.com/agno-agi/agno) | 🟢 **72.4** | 40.7k | 🚀 +113 | 99 | today | `multi-agent` |
| 6 | [Claude Agent SDK](https://github.com/anthropics/claude-code) | 🟢 **70.8** | 132.7k | 🚀 +1468 | 26 | today | `orchestration` |
| 7 | [Google ADK](https://github.com/google/adk-python) | 🟢 **70.6** | 20.1k | 📈 +96 | 198 | today | `orchestration` |
| 8 | [PydanticAI](https://github.com/pydantic/pydantic-ai) | 🟡 **69.2** | 17.8k | 🚀 +141 | 76 | 5 days ago | `structured` |
| 9 | [AG2](https://github.com/ag2ai/ag2) | 🟡 **60.3** | 4.7k | 📈 +26 | 58 | 3 days ago | `multi-agent` |
| 10 | [LlamaIndex](https://github.com/run-llama/llama_index) | 🟡 **60.1** | 50.2k | 🚀 +138 | 23 | 1 mo ago | `data-agent` |
| 11 | [OpenAI Agents SDK](https://github.com/openai/openai-agents-python) | 🟡 **59.5** | 27.2k | 🚀 +172 | 23 | 5 days ago | `orchestration` |
| 12 | [DSPy](https://github.com/stanfordnlp/dspy) | 🟡 **56.2** | 35.1k | 🚀 +118 | 37 | 19 days ago | `optimization` |
| 13 | [Semantic Kernel](https://github.com/microsoft/semantic-kernel) | 🟡 **52.3** | 28.1k | 📈 +52 | 7 | 12 days ago | `enterprise` |
| 14 | [Haystack](https://github.com/deepset-ai/haystack) | 🟡 **50.1** | 25.6k | 📈 +79 | 0 | 6 days ago | `pipeline` |
| 15 | [Composio](https://github.com/ComposioHQ/composio) | 🟡 **46.9** | 28.8k | 📈 +98 | 0 | today | `tooling` |
| 16 | [Letta](https://github.com/letta-ai/letta) | 🟡 **46.5** | 23.4k | 🚀 +133 | 0 | 1 mo ago | `memory` |
| 17 | [Smolagents](https://github.com/huggingface/smolagents) | 🟡 **44.0** | 27.9k | 🚀 +119 | 5 | 18 days ago | `lightweight` |
| 18 | [AutoGen](https://github.com/microsoft/autogen) | 🟡 **40.3** | 59.0k | 🚀 +197 | 0 | 8 mo ago | `multi-agent` |
| 19 | [Swarm](https://github.com/openai/swarm) | 🔴 **9.5** | 21.6k | 📈 +39 | 0 | — | `experimental` |

## 📂 By Category

- `data-agent`: **LlamaIndex** (60.1)
- `enterprise`: **Semantic Kernel** (52.3)
- `experimental`: **Swarm** (9.5)
- `lightweight`: **Smolagents** (44.0)
- `memory`: **Letta** (46.5)
- `multi-agent`: **CrewAI** (90.2), **Agno** (72.4), **AG2** (60.3), **AutoGen** (40.3)
- `optimization`: **DSPy** (56.2)
- `orchestration`: **LangGraph** (81.6), **Claude Agent SDK** (70.8), **Google ADK** (70.6), **OpenAI Agents SDK** (59.5)
- `pipeline`: **Haystack** (50.1)
- `structured`: **PydanticAI** (69.2)
- `tooling`: **Composio** (46.9)
- `typescript`: **Mastra** (79.5)
- `web-agent`: **BrowserUse** (89.9)

## 🔍 Top 5 — Score Breakdown

| Framework | Star Velocity | Release Freshness | Issue Health | Commit Activity | Community | Fork Ratio |
|-----------|:---:|:---:|:---:|:---:|:---:|:---:|
| **CrewAI** | 100 | 98.7 | 97.0 | 97.0 | 59.4 | 56.0 |
| **BrowserUse** | 100 | 99.0 | 95.7 | 100 | 63.0 | 44.7 |
| **LangGraph** | 100 | 99.0 | 74.8 | 67.0 | 55.0 | 67.0 |
| **Mastra** | 50.5 | 99.0 | 95.2 | 100 | 92.0 | 35.7 |
| **Agno** | 24.2 | 100.0 | 81.2 | 99.0 | 89.0 | 54.3 |

## 💡 Key Insights

- **Hottest framework**: CrewAI with a Pulse Score of 90.2
- **Fastest growing**: Claude Agent SDK gained +1468 stars this week
- **Most active development**: Mastra with 780 commits in the last 4 weeks
- **Stale releases**: Swarm haven't released in a while

## 📦 Recent Releases

- **Claude Agent SDK** [`v2.1.178`](https://github.com/anthropics/claude-code/releases/tag/v2.1.178) — today
- **Google ADK** [`v1.35.1`](https://github.com/google/adk-python/releases/tag/v1.35.1) — today
- **Agno** [`v2.6.16`](https://github.com/agno-agi/agno/releases/tag/v2.6.16) — today
- **Composio** [`@composio/cli@0.2.32-beta.264`](https://github.com/ComposioHQ/composio/releases/tag/@composio/cli@0.2.32-beta.264) — today *(pre-release)*
- **BrowserUse** [`0.13.2`](https://github.com/browser-use/browser-use/releases/tag/0.13.2) — 3 days ago
- **AG2** [`v0.13.4`](https://github.com/ag2ai/ag2/releases/tag/v0.13.4) — 3 days ago
- **LangGraph** [`1.2.5`](https://github.com/langchain-ai/langgraph/releases/tag/1.2.5) — 3 days ago
- **Mastra** [`@mastra/core@1.42.0`](https://github.com/mastra-ai/mastra/releases/tag/@mastra/core@1.42.0) — 3 days ago
- **CrewAI** [`1.14.7`](https://github.com/crewAIInc/crewAI/releases/tag/1.14.7) — 4 days ago
- **OpenAI Agents SDK** [`v0.17.5`](https://github.com/openai/openai-agents-python/releases/tag/v0.17.5) — 5 days ago

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

*Powered by GitHub Actions • Data refreshed daily • Last run: 2026-06-16 11:21 UTC*