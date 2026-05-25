# 🔬 AI Agent Framework Pulse Tracker

[![Daily Update](https://github.com/PurpleHaze2320/ai-agent-pulse/actions/workflows/track.yml/badge.svg)](https://github.com/PurpleHaze2320/ai-agent-pulse/actions/workflows/track.yml)
[![Frameworks Tracked](https://img.shields.io/badge/frameworks-19-blue)](https://github.com/PurpleHaze2320/ai-agent-pulse)
[![License: MIT](https://img.shields.io/badge/License-MIT-green.svg)](https://opensource.org/licenses/MIT)
[![GitHub stars](https://img.shields.io/github/stars/PurpleHaze2320/ai-agent-pulse?style=social)](https://github.com/PurpleHaze2320/ai-agent-pulse/stargazers)

> Automated daily tracking of the AI agent framework ecosystem's health, momentum, and trends.
> Last updated: **2026-05-25 10:20 UTC** | Tracking **19** frameworks

## How It Works

This bot runs daily via GitHub Actions and collects metrics from the GitHub API for the most important
AI agent frameworks. It computes a **Pulse Score** (0-100) based on six weighted signals: star velocity,
release freshness, issue health, commit activity, community size, and fork engagement. The result is
a living dashboard that shows which frameworks are gaining momentum and which are losing steam.

## 🏆 Pulse Leaderboard

| Rank | Framework | Pulse | Stars | ⭐ 7d | Commits (4w) | Last Release | Category |
|------|-----------|-------|-------|-------|--------------|--------------|----------|
| 1 | [Mastra](https://github.com/mastra-ai/mastra) | 🟢 **80.2** | 24.3k | 🚀 +299 | 746 | 6 days ago | `typescript` |
| 2 | [CrewAI](https://github.com/crewAIInc/crewAI) | 🟢 **71.0** | 52.1k | 🚀 +509 | 0 | 3 days ago | `multi-agent` |
| 3 | [BrowserUse](https://github.com/browser-use/browser-use) | 🟢 **70.1** | 95.4k | 🚀 +990 | 0 | 1 day ago | `web-agent` |
| 4 | [LangGraph](https://github.com/langchain-ai/langgraph) | 🟡 **68.6** | 32.9k | 🚀 +567 | 0 | 2 days ago | `orchestration` |
| 5 | [Claude Agent SDK](https://github.com/anthropics/claude-code) | 🟡 **65.0** | 126.4k | 🚀 +1856 | 0 | 2 days ago | `orchestration` |
| 6 | [OpenAI Agents SDK](https://github.com/openai/openai-agents-python) | 🟡 **58.8** | 26.6k | 🚀 +203 | 0 | 6 days ago | `orchestration` |
| 7 | [LlamaIndex](https://github.com/run-llama/llama_index) | 🟡 **57.9** | 49.6k | 🚀 +164 | 0 | 10 days ago | `data-agent` |
| 8 | [Agno](https://github.com/agno-agi/agno) | 🟡 **54.7** | 40.3k | 🚀 +175 | 0 | 3 days ago | `multi-agent` |
| 9 | [PydanticAI](https://github.com/pydantic/pydantic-ai) | 🟡 **54.3** | 17.3k | 🚀 +155 | 0 | 2 days ago | `structured` |
| 10 | [Google ADK](https://github.com/google/adk-python) | 🟡 **52.1** | 19.8k | 🚀 +151 | 0 | 2 days ago | `orchestration` |
| 11 | [Semantic Kernel](https://github.com/microsoft/semantic-kernel) | 🟡 **50.6** | 28.0k | 📈 +45 | 0 | 11 days ago | `enterprise` |
| 12 | [Haystack](https://github.com/deepset-ai/haystack) | 🟡 **50.2** | 25.4k | 📈 +100 | 0 | 12 days ago | `pipeline` |
| 13 | [DSPy](https://github.com/stanfordnlp/dspy) | 🟡 **49.3** | 34.6k | 🚀 +130 | 0 | 19 days ago | `optimization` |
| 14 | [Letta](https://github.com/letta-ai/letta) | 🟡 **49.1** | 22.9k | 🚀 +158 | 0 | 10 days ago | `memory` |
| 15 | [AG2](https://github.com/ag2ai/ag2) | 🟡 **48.9** | 4.6k | 📈 +29 | 0 | 2 days ago | `multi-agent` |
| 16 | [Composio](https://github.com/ComposioHQ/composio) | 🟡 **48.0** | 28.4k | 🚀 +131 | 0 | 5 days ago | `tooling` |
| 17 | [Smolagents](https://github.com/huggingface/smolagents) | 🟡 **44.3** | 27.5k | 🚀 +134 | 0 | 10 days ago | `lightweight` |
| 18 | [AutoGen](https://github.com/microsoft/autogen) | 🟡 **43.3** | 58.4k | 🚀 +234 | 0 | 7 mo ago | `multi-agent` |
| 19 | [Swarm](https://github.com/openai/swarm) | 🔴 **9.1** | 21.5k | 📈 +26 | 0 | — | `experimental` |

## 📂 By Category

- `data-agent`: **LlamaIndex** (57.9)
- `enterprise`: **Semantic Kernel** (50.6)
- `experimental`: **Swarm** (9.1)
- `lightweight`: **Smolagents** (44.3)
- `memory`: **Letta** (49.1)
- `multi-agent`: **CrewAI** (71.0), **Agno** (54.7), **AG2** (48.9), **AutoGen** (43.3)
- `optimization`: **DSPy** (49.3)
- `orchestration`: **LangGraph** (68.6), **Claude Agent SDK** (65.0), **OpenAI Agents SDK** (58.8), **Google ADK** (52.1)
- `pipeline`: **Haystack** (50.2)
- `structured`: **PydanticAI** (54.3)
- `tooling`: **Composio** (48.0)
- `typescript`: **Mastra** (80.2)
- `web-agent`: **BrowserUse** (70.1)

## 🔍 Top 5 — Score Breakdown

| Framework | Star Velocity | Release Freshness | Issue Health | Commit Activity | Community | Fork Ratio |
|-----------|:---:|:---:|:---:|:---:|:---:|:---:|
| **Mastra** | 56.5 | 98.0 | 94.6 | 100 | 87.6 | 34.9 |
| **CrewAI** | 100 | 99.0 | 98.2 | 0.0 | 59.4 | 55.5 |
| **BrowserUse** | 100 | 99.7 | 95.8 | 0.0 | 63.0 | 45.0 |
| **LangGraph** | 100 | 99.3 | 76.6 | 0.0 | 54.8 | 67.7 |
| **Claude Agent SDK** | 100 | 99.3 | 83.7 | 0.0 | 10.0 | 65.6 |

## 💡 Key Insights

- **Hottest framework**: Mastra with a Pulse Score of 80.2
- **Fastest growing**: Claude Agent SDK gained +1856 stars this week
- **Most active development**: Mastra with 746 commits in the last 4 weeks
- **Stale releases**: Swarm haven't released in a while

## 📦 Recent Releases

- **BrowserUse** [`0.12.8`](https://github.com/browser-use/browser-use/releases/tag/0.12.8) — 1 day ago
- **Claude Agent SDK** [`v2.1.150`](https://github.com/anthropics/claude-code/releases/tag/v2.1.150) — 2 days ago
- **PydanticAI** [`v2.0.0b3`](https://github.com/pydantic/pydantic-ai/releases/tag/v2.0.0b3) — 2 days ago *(pre-release)*
- **AG2** [`v0.13.1`](https://github.com/ag2ai/ag2/releases/tag/v0.13.1) — 2 days ago
- **Google ADK** [`v2.1.0`](https://github.com/google/adk-python/releases/tag/v2.1.0) — 2 days ago
- **LangGraph** [`sdk==0.3.15`](https://github.com/langchain-ai/langgraph/releases/tag/sdk==0.3.15) — 2 days ago
- **Agno** [`v2.6.9`](https://github.com/agno-agi/agno/releases/tag/v2.6.9) — 3 days ago
- **CrewAI** [`1.14.6a1`](https://github.com/crewAIInc/crewAI/releases/tag/1.14.6a1) — 3 days ago *(pre-release)*
- **Composio** [`@composio/cli@0.2.31-beta.256`](https://github.com/ComposioHQ/composio/releases/tag/@composio/cli@0.2.31-beta.256) — 5 days ago *(pre-release)*
- **OpenAI Agents SDK** [`v0.17.3`](https://github.com/openai/openai-agents-python/releases/tag/v0.17.3) — 6 days ago

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

*Powered by GitHub Actions • Data refreshed daily • Last run: 2026-05-25 10:20 UTC*