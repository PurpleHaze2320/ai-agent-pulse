# 🔬 AI Agent Framework Pulse Tracker

[![Daily Update](https://github.com/PurpleHaze2320/ai-agent-pulse/actions/workflows/track.yml/badge.svg)](https://github.com/PurpleHaze2320/ai-agent-pulse/actions/workflows/track.yml)
[![Frameworks Tracked](https://img.shields.io/badge/frameworks-19-blue)](https://github.com/PurpleHaze2320/ai-agent-pulse)
[![License: MIT](https://img.shields.io/badge/License-MIT-green.svg)](https://opensource.org/licenses/MIT)
[![GitHub stars](https://img.shields.io/github/stars/PurpleHaze2320/ai-agent-pulse?style=social)](https://github.com/PurpleHaze2320/ai-agent-pulse/stargazers)

> Automated daily tracking of the AI agent framework ecosystem's health, momentum, and trends.
> Last updated: **2026-07-06 10:47 UTC** | Tracking **19** frameworks

## How It Works

This bot runs daily via GitHub Actions and collects metrics from the GitHub API for the most important
AI agent frameworks. It computes a **Pulse Score** (0-100) based on six weighted signals: star velocity,
release freshness, issue health, commit activity, community size, and fork engagement. The result is
a living dashboard that shows which frameworks are gaining momentum and which are losing steam.

## 🏆 Pulse Leaderboard

| Rank | Framework | Pulse | Stars | ⭐ 7d | Commits (4w) | Last Release | Category |
|------|-----------|-------|-------|-------|--------------|--------------|----------|
| 1 | [CrewAI](https://github.com/crewAIInc/crewAI) | 🟢 **88.0** | 55.0k | 🚀 +455 | 93 | 4 days ago | `multi-agent` |
| 2 | [Mastra](https://github.com/mastra-ai/mastra) | 🟢 **81.4** | 25.9k | 🚀 +300 | 851 | 4 days ago | `typescript` |
| 3 | [BrowserUse](https://github.com/browser-use/browser-use) | 🟢 **77.1** | 103.0k | 🚀 +1744 | 37 | 4 days ago | `web-agent` |
| 4 | [LangGraph](https://github.com/langchain-ai/langgraph) | 🟢 **77.0** | 36.6k | 🚀 +605 | 46 | 6 days ago | `orchestration` |
| 5 | [PydanticAI](https://github.com/pydantic/pydantic-ai) | 🟢 **76.1** | 18.2k | 🚀 +181 | 164 | 2 days ago | `structured` |
| 6 | [Google ADK](https://github.com/google/adk-python) | 🟢 **73.1** | 20.5k | 🚀 +157 | 265 | 17 days ago | `orchestration` |
| 7 | [Agno](https://github.com/agno-agi/agno) | 🟢 **71.2** | 41.0k | 🚀 +122 | 94 | today | `multi-agent` |
| 8 | [Claude Agent SDK](https://github.com/anthropics/claude-code) | 🟢 **70.2** | 136.5k | 🚀 +1566 | 24 | 2 days ago | `orchestration` |
| 9 | [Haystack](https://github.com/deepset-ai/haystack) | 🟡 **69.2** | 25.8k | 📈 +63 | 158 | 18 days ago | `pipeline` |
| 10 | [OpenAI Agents SDK](https://github.com/openai/openai-agents-python) | 🟡 **66.8** | 27.7k | 🚀 +187 | 58 | 12 days ago | `orchestration` |
| 11 | [LlamaIndex](https://github.com/run-llama/llama_index) | 🟡 **63.8** | 50.7k | 🚀 +189 | 25 | 11 days ago | `data-agent` |
| 12 | [AG2](https://github.com/ag2ai/ag2) | 🟡 **62.4** | 4.7k | 📈 +23 | 61 | 2 days ago | `multi-agent` |
| 13 | [Semantic Kernel](https://github.com/microsoft/semantic-kernel) | 🟡 **57.3** | 28.3k | 📈 +52 | 34 | 19 days ago | `enterprise` |
| 14 | [DSPy](https://github.com/stanfordnlp/dspy) | 🟡 **54.5** | 35.9k | 🚀 +261 | 3 | 1 mo ago | `optimization` |
| 15 | [Composio](https://github.com/ComposioHQ/composio) | 🟡 **47.1** | 29.1k | 🚀 +103 | 0 | 2 days ago | `tooling` |
| 16 | [Letta](https://github.com/letta-ai/letta) | 🟡 **43.5** | 23.7k | 📈 +96 | 0 | 1 mo ago | `memory` |
| 17 | [Smolagents](https://github.com/huggingface/smolagents) | 🟡 **42.0** | 28.2k | 🚀 +131 | 1 | 1 mo ago | `lightweight` |
| 18 | [AutoGen](https://github.com/microsoft/autogen) | 🟠 **37.8** | 59.5k | 🚀 +177 | 0 | 9 mo ago | `multi-agent` |
| 19 | [Swarm](https://github.com/openai/swarm) | 🔴 **9.1** | 21.8k | 📈 +21 | 0 | — | `experimental` |

## 📂 By Category

- `data-agent`: **LlamaIndex** (63.8)
- `enterprise`: **Semantic Kernel** (57.3)
- `experimental`: **Swarm** (9.1)
- `lightweight`: **Smolagents** (42.0)
- `memory`: **Letta** (43.5)
- `multi-agent`: **CrewAI** (88.0), **Agno** (71.2), **AG2** (62.4), **AutoGen** (37.8)
- `optimization`: **DSPy** (54.5)
- `orchestration`: **LangGraph** (77.0), **Google ADK** (73.1), **Claude Agent SDK** (70.2), **OpenAI Agents SDK** (66.8)
- `pipeline`: **Haystack** (69.2)
- `structured`: **PydanticAI** (76.1)
- `tooling`: **Composio** (47.1)
- `typescript`: **Mastra** (81.4)
- `web-agent`: **BrowserUse** (77.1)

## 🔍 Top 5 — Score Breakdown

| Framework | Star Velocity | Release Freshness | Issue Health | Commit Activity | Community | Fork Ratio |
|-----------|:---:|:---:|:---:|:---:|:---:|:---:|
| **CrewAI** | 94.9 | 98.7 | 95.6 | 93.0 | 59.6 | 56.2 |
| **Mastra** | 57.6 | 98.7 | 95.3 | 100 | 92.6 | 36.6 |
| **BrowserUse** | 100 | 98.7 | 94.9 | 37.0 | 63.0 | 44.3 |
| **LangGraph** | 100 | 98.0 | 73.5 | 46.0 | 55.0 | 67.0 |
| **PydanticAI** | 35.7 | 99.3 | 85.1 | 100 | 95.0 | 50.6 |

## 💡 Key Insights

- **Hottest framework**: CrewAI with a Pulse Score of 88.0
- **Fastest growing**: BrowserUse gained +1744 stars this week
- **Most active development**: Mastra with 851 commits in the last 4 weeks
- **Stale releases**: AutoGen, Swarm haven't released in a while

## 📦 Recent Releases

- **Agno** [`v2.7.0a4`](https://github.com/agno-agi/agno/releases/tag/v2.7.0a4) — today *(pre-release)*
- **PydanticAI** [`v2.5.0`](https://github.com/pydantic/pydantic-ai/releases/tag/v2.5.0) — 2 days ago
- **Claude Agent SDK** [`v2.1.201`](https://github.com/anthropics/claude-code/releases/tag/v2.1.201) — 2 days ago
- **AG2** [`v1.0.0b0`](https://github.com/ag2ai/ag2/releases/tag/v1.0.0b0) — 2 days ago
- **Composio** [`@composio/cli@0.2.32-beta.281`](https://github.com/ComposioHQ/composio/releases/tag/@composio/cli@0.2.32-beta.281) — 2 days ago *(pre-release)*
- **CrewAI** [`1.15.2a2`](https://github.com/crewAIInc/crewAI/releases/tag/1.15.2a2) — 4 days ago *(pre-release)*
- **Mastra** [`@mastra/core@1.48.0`](https://github.com/mastra-ai/mastra/releases/tag/@mastra/core@1.48.0) — 4 days ago
- **BrowserUse** [`0.13.3`](https://github.com/browser-use/browser-use/releases/tag/0.13.3) — 4 days ago
- **LangGraph** [`1.2.7`](https://github.com/langchain-ai/langgraph/releases/tag/1.2.7) — 6 days ago
- **LlamaIndex** [`v0.14.23`](https://github.com/run-llama/llama_index/releases/tag/v0.14.23) — 11 days ago

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

*Powered by GitHub Actions • Data refreshed daily • Last run: 2026-07-06 10:47 UTC*