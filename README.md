# 🔬 AI Agent Framework Pulse Tracker

[![Daily Update](https://github.com/PurpleHaze2320/ai-agent-pulse/actions/workflows/track.yml/badge.svg)](https://github.com/PurpleHaze2320/ai-agent-pulse/actions/workflows/track.yml)
[![Frameworks Tracked](https://img.shields.io/badge/frameworks-19-blue)](https://github.com/PurpleHaze2320/ai-agent-pulse)
[![License: MIT](https://img.shields.io/badge/License-MIT-green.svg)](https://opensource.org/licenses/MIT)
[![GitHub stars](https://img.shields.io/github/stars/PurpleHaze2320/ai-agent-pulse?style=social)](https://github.com/PurpleHaze2320/ai-agent-pulse/stargazers)

> Automated daily tracking of the AI agent framework ecosystem's health, momentum, and trends.
> Last updated: **2026-05-27 10:04 UTC** | Tracking **19** frameworks

## How It Works

This bot runs daily via GitHub Actions and collects metrics from the GitHub API for the most important
AI agent frameworks. It computes a **Pulse Score** (0-100) based on six weighted signals: star velocity,
release freshness, issue health, commit activity, community size, and fork engagement. The result is
a living dashboard that shows which frameworks are gaining momentum and which are losing steam.

## 🏆 Pulse Leaderboard

| Rank | Framework | Pulse | Stars | ⭐ 7d | Commits (4w) | Last Release | Category |
|------|-----------|-------|-------|-------|--------------|--------------|----------|
| 1 | [Mastra](https://github.com/mastra-ai/mastra) | 🟢 **80.8** | 24.4k | 🚀 +316 | 836 | 8 days ago | `typescript` |
| 2 | [CrewAI](https://github.com/crewAIInc/crewAI) | 🟢 **70.8** | 52.3k | 🚀 +496 | 0 | 5 days ago | `multi-agent` |
| 3 | [BrowserUse](https://github.com/browser-use/browser-use) | 🟢 **70.1** | 95.8k | 🚀 +1014 | 0 | 1 day ago | `web-agent` |
| 4 | [LangGraph](https://github.com/langchain-ai/langgraph) | 🟡 **68.7** | 33.1k | 🚀 +616 | 0 | today | `orchestration` |
| 5 | [Claude Agent SDK](https://github.com/anthropics/claude-code) | 🟡 **65.3** | 126.9k | 🚀 +1766 | 0 | today | `orchestration` |
| 6 | [LlamaIndex](https://github.com/run-llama/llama_index) | 🟡 **57.9** | 49.7k | 🚀 +169 | 0 | 12 days ago | `data-agent` |
| 7 | [OpenAI Agents SDK](https://github.com/openai/openai-agents-python) | 🟡 **57.9** | 26.7k | 🚀 +198 | 0 | 1 day ago | `orchestration` |
| 8 | [PydanticAI](https://github.com/pydantic/pydantic-ai) | 🟡 **55.2** | 17.3k | 🚀 +174 | 0 | today | `structured` |
| 9 | [Agno](https://github.com/agno-agi/agno) | 🟡 **53.1** | 40.4k | 🚀 +132 | 0 | 5 days ago | `multi-agent` |
| 10 | [Google ADK](https://github.com/google/adk-python) | 🟡 **51.4** | 19.9k | 🚀 +135 | 0 | 4 days ago | `orchestration` |
| 11 | [Semantic Kernel](https://github.com/microsoft/semantic-kernel) | 🟡 **50.5** | 28.0k | 📈 +47 | 0 | 13 days ago | `enterprise` |
| 12 | [DSPy](https://github.com/stanfordnlp/dspy) | 🟡 **49.6** | 34.7k | 🚀 +140 | 0 | 21 days ago | `optimization` |
| 13 | [Haystack](https://github.com/deepset-ai/haystack) | 🟡 **49.5** | 25.4k | 📈 +83 | 0 | 14 days ago | `pipeline` |
| 14 | [AG2](https://github.com/ag2ai/ag2) | 🟡 **48.7** | 4.6k | 📈 +26 | 0 | 4 days ago | `multi-agent` |
| 15 | [Letta](https://github.com/letta-ai/letta) | 🟡 **48.6** | 23.0k | 🚀 +149 | 0 | 12 days ago | `memory` |
| 16 | [Composio](https://github.com/ComposioHQ/composio) | 🟡 **47.8** | 28.5k | 🚀 +125 | 0 | 7 days ago | `tooling` |
| 17 | [Smolagents](https://github.com/huggingface/smolagents) | 🟡 **44.2** | 27.5k | 🚀 +134 | 0 | 12 days ago | `lightweight` |
| 18 | [AutoGen](https://github.com/microsoft/autogen) | 🟡 **43.4** | 58.4k | 🚀 +239 | 0 | 7 mo ago | `multi-agent` |
| 19 | [Swarm](https://github.com/openai/swarm) | 🔴 **8.8** | 21.5k | ↗️ +19 | 0 | — | `experimental` |

## 📂 By Category

- `data-agent`: **LlamaIndex** (57.9)
- `enterprise`: **Semantic Kernel** (50.5)
- `experimental`: **Swarm** (8.8)
- `lightweight`: **Smolagents** (44.2)
- `memory`: **Letta** (48.6)
- `multi-agent`: **CrewAI** (70.8), **Agno** (53.1), **AG2** (48.7), **AutoGen** (43.4)
- `optimization`: **DSPy** (49.6)
- `orchestration`: **LangGraph** (68.7), **Claude Agent SDK** (65.3), **OpenAI Agents SDK** (57.9), **Google ADK** (51.4)
- `pipeline`: **Haystack** (49.5)
- `structured`: **PydanticAI** (55.2)
- `tooling`: **Composio** (47.8)
- `typescript`: **Mastra** (80.8)
- `web-agent`: **BrowserUse** (70.1)

## 🔍 Top 5 — Score Breakdown

| Framework | Star Velocity | Release Freshness | Issue Health | Commit Activity | Community | Fork Ratio |
|-----------|:---:|:---:|:---:|:---:|:---:|:---:|
| **Mastra** | 59.6 | 97.3 | 94.4 | 100 | 88.0 | 35.1 |
| **CrewAI** | 100 | 98.3 | 98.0 | 0.0 | 59.2 | 55.6 |
| **BrowserUse** | 100 | 99.7 | 95.7 | 0.0 | 63.0 | 45.0 |
| **LangGraph** | 100 | 100.0 | 76.4 | 0.0 | 54.8 | 67.6 |
| **Claude Agent SDK** | 100 | 100.0 | 85.0 | 0.0 | 10.2 | 65.6 |

## 💡 Key Insights

- **Hottest framework**: Mastra with a Pulse Score of 80.8
- **Fastest growing**: Claude Agent SDK gained +1766 stars this week
- **Most active development**: Mastra with 836 commits in the last 4 weeks
- **Stale releases**: Swarm haven't released in a while

## 📦 Recent Releases

- **PydanticAI** [`v1.103.0`](https://github.com/pydantic/pydantic-ai/releases/tag/v1.103.0) — today
- **Claude Agent SDK** [`v2.1.152`](https://github.com/anthropics/claude-code/releases/tag/v2.1.152) — today
- **LangGraph** [`1.2.2`](https://github.com/langchain-ai/langgraph/releases/tag/1.2.2) — today
- **OpenAI Agents SDK** [`v0.17.4`](https://github.com/openai/openai-agents-python/releases/tag/v0.17.4) — 1 day ago
- **BrowserUse** [`0.12.9`](https://github.com/browser-use/browser-use/releases/tag/0.12.9) — 1 day ago
- **AG2** [`v0.13.1`](https://github.com/ag2ai/ag2/releases/tag/v0.13.1) — 4 days ago
- **Google ADK** [`v2.1.0`](https://github.com/google/adk-python/releases/tag/v2.1.0) — 4 days ago
- **Agno** [`v2.6.9`](https://github.com/agno-agi/agno/releases/tag/v2.6.9) — 5 days ago
- **CrewAI** [`1.14.6a1`](https://github.com/crewAIInc/crewAI/releases/tag/1.14.6a1) — 5 days ago *(pre-release)*
- **Composio** [`@composio/cli@0.2.31-beta.256`](https://github.com/ComposioHQ/composio/releases/tag/@composio/cli@0.2.31-beta.256) — 7 days ago *(pre-release)*

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

*Powered by GitHub Actions • Data refreshed daily • Last run: 2026-05-27 10:04 UTC*