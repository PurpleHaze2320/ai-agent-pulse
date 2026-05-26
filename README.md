# 🔬 AI Agent Framework Pulse Tracker

[![Daily Update](https://github.com/PurpleHaze2320/ai-agent-pulse/actions/workflows/track.yml/badge.svg)](https://github.com/PurpleHaze2320/ai-agent-pulse/actions/workflows/track.yml)
[![Frameworks Tracked](https://img.shields.io/badge/frameworks-19-blue)](https://github.com/PurpleHaze2320/ai-agent-pulse)
[![License: MIT](https://img.shields.io/badge/License-MIT-green.svg)](https://opensource.org/licenses/MIT)
[![GitHub stars](https://img.shields.io/github/stars/PurpleHaze2320/ai-agent-pulse?style=social)](https://github.com/PurpleHaze2320/ai-agent-pulse/stargazers)

> Automated daily tracking of the AI agent framework ecosystem's health, momentum, and trends.
> Last updated: **2026-05-26 10:06 UTC** | Tracking **19** frameworks

## How It Works

This bot runs daily via GitHub Actions and collects metrics from the GitHub API for the most important
AI agent frameworks. It computes a **Pulse Score** (0-100) based on six weighted signals: star velocity,
release freshness, issue health, commit activity, community size, and fork engagement. The result is
a living dashboard that shows which frameworks are gaining momentum and which are losing steam.

## 🏆 Pulse Leaderboard

| Rank | Framework | Pulse | Stars | ⭐ 7d | Commits (4w) | Last Release | Category |
|------|-----------|-------|-------|-------|--------------|--------------|----------|
| 1 | [Mastra](https://github.com/mastra-ai/mastra) | 🟢 **80.1** | 24.3k | 🚀 +295 | 793 | 7 days ago | `typescript` |
| 2 | [CrewAI](https://github.com/crewAIInc/crewAI) | 🟢 **70.9** | 52.2k | 🚀 +500 | 0 | 4 days ago | `multi-agent` |
| 3 | [BrowserUse](https://github.com/browser-use/browser-use) | 🟢 **70.2** | 95.6k | 🚀 +992 | 0 | today | `web-agent` |
| 4 | [LangGraph](https://github.com/langchain-ai/langgraph) | 🟡 **68.5** | 33.0k | 🚀 +614 | 0 | 3 days ago | `orchestration` |
| 5 | [Claude Agent SDK](https://github.com/anthropics/claude-code) | 🟡 **65.0** | 126.6k | 🚀 +1798 | 0 | 3 days ago | `orchestration` |
| 6 | [OpenAI Agents SDK](https://github.com/openai/openai-agents-python) | 🟡 **58.6** | 26.7k | 🚀 +201 | 0 | today | `orchestration` |
| 7 | [LlamaIndex](https://github.com/run-llama/llama_index) | 🟡 **58.1** | 49.7k | 🚀 +171 | 0 | 11 days ago | `data-agent` |
| 8 | [PydanticAI](https://github.com/pydantic/pydantic-ai) | 🟡 **54.9** | 17.3k | 🚀 +170 | 0 | 3 days ago | `structured` |
| 9 | [Agno](https://github.com/agno-agi/agno) | 🟡 **53.7** | 40.4k | 🚀 +147 | 0 | 4 days ago | `multi-agent` |
| 10 | [Google ADK](https://github.com/google/adk-python) | 🟡 **51.6** | 19.9k | 🚀 +139 | 0 | 3 days ago | `orchestration` |
| 11 | [Semantic Kernel](https://github.com/microsoft/semantic-kernel) | 🟡 **50.6** | 28.0k | 📈 +48 | 0 | 12 days ago | `enterprise` |
| 12 | [Haystack](https://github.com/deepset-ai/haystack) | 🟡 **49.7** | 25.4k | 📈 +87 | 0 | 13 days ago | `pipeline` |
| 13 | [DSPy](https://github.com/stanfordnlp/dspy) | 🟡 **49.3** | 34.7k | 🚀 +132 | 0 | 20 days ago | `optimization` |
| 14 | [Letta](https://github.com/letta-ai/letta) | 🟡 **49.0** | 23.0k | 🚀 +156 | 0 | 11 days ago | `memory` |
| 15 | [AG2](https://github.com/ag2ai/ag2) | 🟡 **48.8** | 4.6k | 📈 +26 | 0 | 3 days ago | `multi-agent` |
| 16 | [Composio](https://github.com/ComposioHQ/composio) | 🟡 **47.4** | 28.5k | 🚀 +116 | 0 | 6 days ago | `tooling` |
| 17 | [Smolagents](https://github.com/huggingface/smolagents) | 🟡 **44.1** | 27.5k | 🚀 +129 | 0 | 11 days ago | `lightweight` |
| 18 | [AutoGen](https://github.com/microsoft/autogen) | 🟡 **43.6** | 58.4k | 🚀 +243 | 0 | 7 mo ago | `multi-agent` |
| 19 | [Swarm](https://github.com/openai/swarm) | 🔴 **8.8** | 21.5k | ↗️ +18 | 0 | — | `experimental` |

## 📂 By Category

- `data-agent`: **LlamaIndex** (58.1)
- `enterprise`: **Semantic Kernel** (50.6)
- `experimental`: **Swarm** (8.8)
- `lightweight`: **Smolagents** (44.1)
- `memory`: **Letta** (49.0)
- `multi-agent`: **CrewAI** (70.9), **Agno** (53.7), **AG2** (48.8), **AutoGen** (43.6)
- `optimization`: **DSPy** (49.3)
- `orchestration`: **LangGraph** (68.5), **Claude Agent SDK** (65.0), **OpenAI Agents SDK** (58.6), **Google ADK** (51.6)
- `pipeline`: **Haystack** (49.7)
- `structured`: **PydanticAI** (54.9)
- `tooling`: **Composio** (47.4)
- `typescript`: **Mastra** (80.1)
- `web-agent`: **BrowserUse** (70.2)

## 🔍 Top 5 — Score Breakdown

| Framework | Star Velocity | Release Freshness | Issue Health | Commit Activity | Community | Fork Ratio |
|-----------|:---:|:---:|:---:|:---:|:---:|:---:|
| **Mastra** | 56.2 | 97.7 | 94.5 | 100 | 88.0 | 35.1 |
| **CrewAI** | 100 | 98.7 | 98.1 | 0.0 | 59.4 | 55.5 |
| **BrowserUse** | 100 | 100.0 | 95.8 | 0.0 | 63.0 | 45.0 |
| **LangGraph** | 100 | 99.0 | 76.6 | 0.0 | 54.8 | 67.6 |
| **Claude Agent SDK** | 100 | 99.0 | 84.5 | 0.0 | 10.0 | 65.6 |

## 💡 Key Insights

- **Hottest framework**: Mastra with a Pulse Score of 80.1
- **Fastest growing**: Claude Agent SDK gained +1798 stars this week
- **Most active development**: Mastra with 793 commits in the last 4 weeks
- **Stale releases**: Swarm haven't released in a while

## 📦 Recent Releases

- **OpenAI Agents SDK** [`v0.17.4`](https://github.com/openai/openai-agents-python/releases/tag/v0.17.4) — today
- **BrowserUse** [`0.12.9`](https://github.com/browser-use/browser-use/releases/tag/0.12.9) — today
- **Claude Agent SDK** [`v2.1.150`](https://github.com/anthropics/claude-code/releases/tag/v2.1.150) — 3 days ago
- **PydanticAI** [`v2.0.0b3`](https://github.com/pydantic/pydantic-ai/releases/tag/v2.0.0b3) — 3 days ago *(pre-release)*
- **AG2** [`v0.13.1`](https://github.com/ag2ai/ag2/releases/tag/v0.13.1) — 3 days ago
- **Google ADK** [`v2.1.0`](https://github.com/google/adk-python/releases/tag/v2.1.0) — 3 days ago
- **LangGraph** [`sdk==0.3.15`](https://github.com/langchain-ai/langgraph/releases/tag/sdk==0.3.15) — 3 days ago
- **Agno** [`v2.6.9`](https://github.com/agno-agi/agno/releases/tag/v2.6.9) — 4 days ago
- **CrewAI** [`1.14.6a1`](https://github.com/crewAIInc/crewAI/releases/tag/1.14.6a1) — 4 days ago *(pre-release)*
- **Composio** [`@composio/cli@0.2.31-beta.256`](https://github.com/ComposioHQ/composio/releases/tag/@composio/cli@0.2.31-beta.256) — 6 days ago *(pre-release)*

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

*Powered by GitHub Actions • Data refreshed daily • Last run: 2026-05-26 10:06 UTC*