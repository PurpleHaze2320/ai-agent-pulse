# 🔬 AI Agent Framework Pulse Tracker

[![Daily Update](https://github.com/PurpleHaze2320/ai-agent-pulse/actions/workflows/track.yml/badge.svg)](https://github.com/PurpleHaze2320/ai-agent-pulse/actions/workflows/track.yml)
[![Frameworks Tracked](https://img.shields.io/badge/frameworks-19-blue)](https://github.com/PurpleHaze2320/ai-agent-pulse)
[![License: MIT](https://img.shields.io/badge/License-MIT-green.svg)](https://opensource.org/licenses/MIT)
[![GitHub stars](https://img.shields.io/github/stars/PurpleHaze2320/ai-agent-pulse?style=social)](https://github.com/PurpleHaze2320/ai-agent-pulse/stargazers)

> Automated daily tracking of the AI agent framework ecosystem's health, momentum, and trends.
> Last updated: **2026-11-16 15:19 UTC** | Tracking **19** frameworks

## How It Works

This bot runs daily via GitHub Actions and collects metrics from the GitHub API for the most important
AI agent frameworks. It computes a **Pulse Score** (0-100) based on six weighted signals: star velocity,
release freshness, issue health, commit activity, community size, and fork engagement. The result is
a living dashboard that shows which frameworks are gaining momentum and which are losing steam.

## 🏆 Pulse Leaderboard

| Rank | Framework | Pulse | Stars | ⭐ 7d | Commits (4w) | Last Release | Category |
|------|-----------|-------|-------|-------|--------------|--------------|----------|
| 1 | [BrowserUse](https://github.com/browser-use/browser-use) | 🟢 **90.3** | 121.2k | 🚀 +777 | 1147 | today | `web-agent` |
| 2 | [LangGraph](https://github.com/langchain-ai/langgraph) | 🟢 **82.2** | 45.0k | 🚀 +330 | 103 | 2 days ago | `orchestration` |
| 3 | [Claude Agent SDK](https://github.com/anthropics/claude-code) | 🟢 **81.3** | 155.9k | 🚀 +816 | 81 | 2 days ago | `orchestration` |
| 4 | [CrewAI](https://github.com/crewAIInc/crewAI) | 🟢 **80.9** | 61.0k | 🚀 +300 | 165 | 3 days ago | `multi-agent` |
| 5 | [Google ADK](https://github.com/google/adk-python) | 🟢 **74.4** | 22.2k | 📈 +81 | 310 | 3 days ago | `orchestration` |
| 6 | [Mastra](https://github.com/mastra-ai/mastra) | 🟢 **74.0** | 29.5k | 🚀 +114 | 1958 | 3 days ago | `typescript` |
| 7 | [Haystack](https://github.com/deepset-ai/haystack) | 🟢 **71.6** | 27.0k | 📈 +61 | 211 | 6 days ago | `pipeline` |
| 8 | [PydanticAI](https://github.com/pydantic/pydantic-ai) | 🟢 **70.6** | 21.2k | 🚀 +137 | 930 | 1 mo ago | `structured` |
| 9 | [AG2](https://github.com/ag2ai/ag2) | 🟢 **70.4** | 5.1k | ↗️ +18 | 107 | today | `multi-agent` |
| 10 | [Agno](https://github.com/agno-agi/agno) | 🟢 **70.0** | 43.2k | 📈 +90 | 117 | 3 days ago | `multi-agent` |
| 11 | [OpenAI Agents SDK](https://github.com/openai/openai-agents-python) | 🟡 **69.0** | 30.7k | 🚀 +137 | 63 | today | `orchestration` |
| 12 | [Composio](https://github.com/ComposioHQ/composio) | 🟡 **68.2** | 31.1k | 🚀 +109 | 239 | today | `tooling` |
| 13 | [Semantic Kernel](https://github.com/microsoft/semantic-kernel) | 🟡 **67.8** | 28.8k | 📈 +33 | 82 | 9 days ago | `enterprise` |
| 14 | [DSPy](https://github.com/stanfordnlp/dspy) | 🟡 **64.1** | 39.1k | 🚀 +108 | 76 | 5 days ago | `optimization` |
| 15 | [LlamaIndex](https://github.com/run-llama/llama_index) | 🟡 **55.4** | 52.9k | 📈 +65 | 8 | 2 days ago | `data-agent` |
| 16 | [Letta](https://github.com/letta-ai/letta) | 🟠 **33.2** | 25.5k | 📈 +70 | 0 | 6 mo ago | `memory` |
| 17 | [AutoGen](https://github.com/microsoft/autogen) | 🟠 **33.1** | 61.9k | 🚀 +113 | 2 | 1y ago | `multi-agent` |
| 18 | [Smolagents](https://github.com/huggingface/smolagents) | 🟠 **33.0** | 30.4k | 🚀 +113 | 9 | 5 mo ago | `lightweight` |
| 19 | [Swarm](https://github.com/openai/swarm) | 🔴 **9.8** | 22.1k | 📈 +32 | 0 | — | `experimental` |

## 📂 By Category

- `data-agent`: **LlamaIndex** (55.4)
- `enterprise`: **Semantic Kernel** (67.8)
- `experimental`: **Swarm** (9.8)
- `lightweight`: **Smolagents** (33.0)
- `memory`: **Letta** (33.2)
- `multi-agent`: **CrewAI** (80.9), **AG2** (70.4), **Agno** (70.0), **AutoGen** (33.1)
- `optimization`: **DSPy** (64.1)
- `orchestration`: **LangGraph** (82.2), **Claude Agent SDK** (81.3), **Google ADK** (74.4), **OpenAI Agents SDK** (69.0)
- `pipeline`: **Haystack** (71.6)
- `structured`: **PydanticAI** (70.6)
- `tooling`: **Composio** (68.2)
- `typescript`: **Mastra** (74.0)
- `web-agent`: **BrowserUse** (90.3)

## 🔍 Top 5 — Score Breakdown

| Framework | Star Velocity | Release Freshness | Issue Health | Commit Activity | Community | Fork Ratio |
|-----------|:---:|:---:|:---:|:---:|:---:|:---:|
| **BrowserUse** | 100 | 100.0 | 90.3 | 100 | 72.4 | 44.7 |
| **LangGraph** | 70.8 | 99.3 | 79.9 | 100 | 57.6 | 69.1 |
| **Claude Agent SDK** | 100 | 99.3 | 84.7 | 81.0 | 11.2 | 64.2 |
| **CrewAI** | 60.0 | 99.0 | 83.5 | 100 | 74.8 | 60.4 |
| **Google ADK** | 16.6 | 99.0 | 93.3 | 100 | 86.0 | 78.6 |

## 💡 Key Insights

- **Hottest framework**: BrowserUse with a Pulse Score of 90.3
- **Fastest growing**: Claude Agent SDK gained +816 stars this week
- **Most active development**: Mastra with 1958 commits in the last 4 weeks
- **Stale releases**: AutoGen, Swarm haven't released in a while

## 📦 Recent Releases

- **Composio** [`@composio/cli@0.6.2`](https://github.com/ComposioHQ/composio/releases/tag/@composio/cli@0.6.2) — today
- **OpenAI Agents SDK** [`v0.24.0-alpha.8`](https://github.com/openai/openai-agents-python/releases/tag/v0.24.0-alpha.8) — today *(pre-release)*
- **BrowserUse** [`1.0.6`](https://github.com/browser-use/browser-use/releases/tag/1.0.6) — today
- **AG2** [`v1.3.2`](https://github.com/ag2ai/ag2/releases/tag/v1.3.2) — today
- **LangGraph** [`1.2.22`](https://github.com/langchain-ai/langgraph/releases/tag/1.2.22) — 2 days ago
- **LlamaIndex** [`v0.14.26`](https://github.com/run-llama/llama_index/releases/tag/v0.14.26) — 2 days ago
- **Claude Agent SDK** [`v2.1.325`](https://github.com/anthropics/claude-code/releases/tag/v2.1.325) — 2 days ago
- **Mastra** [`@mastra/core@1.83.0`](https://github.com/mastra-ai/mastra/releases/tag/@mastra/core@1.83.0) — 3 days ago
- **Google ADK** [`v2.14.1`](https://github.com/google/adk-python/releases/tag/v2.14.1) — 3 days ago
- **CrewAI** [`1.15.41`](https://github.com/crewAIInc/crewAI/releases/tag/1.15.41) — 3 days ago

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

*Powered by GitHub Actions • Data refreshed daily • Last run: 2026-11-16 15:19 UTC*