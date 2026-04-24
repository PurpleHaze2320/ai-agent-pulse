# 🔬 AI Agent Framework Pulse Tracker

[![Daily Update](https://github.com/PurpleHaze2320/ai-agent-pulse/actions/workflows/track.yml/badge.svg)](https://github.com/PurpleHaze2320/ai-agent-pulse/actions/workflows/track.yml)
[![Frameworks Tracked](https://img.shields.io/badge/frameworks-19-blue)](https://github.com/PurpleHaze2320/ai-agent-pulse)
[![License: MIT](https://img.shields.io/badge/License-MIT-green.svg)](https://opensource.org/licenses/MIT)
[![GitHub stars](https://img.shields.io/github/stars/PurpleHaze2320/ai-agent-pulse?style=social)](https://github.com/PurpleHaze2320/ai-agent-pulse/stargazers)

> Automated daily tracking of the AI agent framework ecosystem's health, momentum, and trends.
> Last updated: **2026-04-24 08:13 UTC** | Tracking **19** frameworks

## How It Works

This bot runs daily via GitHub Actions and collects metrics from the GitHub API for the most important
AI agent frameworks. It computes a **Pulse Score** (0-100) based on six weighted signals: star velocity,
release freshness, issue health, commit activity, community size, and fork engagement. The result is
a living dashboard that shows which frameworks are gaining momentum and which are losing steam.

## 🏆 Pulse Leaderboard

| Rank | Framework | Pulse | Stars | ⭐ 7d | Commits (4w) | Last Release | Category |
|------|-----------|-------|-------|-------|--------------|--------------|----------|
| 1 | [Mastra](https://github.com/mastra-ai/mastra) | 🟢 **73.9** | 23.3k | 🚀 +194 | 821 | 15 days ago | `typescript` |
| 2 | [OpenAI Agents SDK](https://github.com/openai/openai-agents-python) | 🟢 **70.6** | 24.9k | 🚀 +3462 | 0 | 1 day ago | `orchestration` |
| 3 | [CrewAI](https://github.com/crewAIInc/crewAI) | 🟢 **70.5** | 49.8k | 🚀 +681 | 0 | 1 day ago | `multi-agent` |
| 4 | [LangGraph](https://github.com/langchain-ai/langgraph) | 🟡 **69.1** | 30.2k | 🚀 +730 | 0 | 1 day ago | `orchestration` |
| 5 | [BrowserUse](https://github.com/browser-use/browser-use) | 🟡 **68.9** | 89.9k | 🚀 +1655 | 0 | 22 days ago | `web-agent` |
| 6 | [Claude Agent SDK](https://github.com/anthropics/claude-code) | 🟡 **64.6** | 117.5k | 🚀 +2447 | 0 | today | `orchestration` |
| 7 | [LlamaIndex](https://github.com/run-llama/llama_index) | 🟡 **60.4** | 48.9k | 🚀 +232 | 0 | 3 days ago | `data-agent` |
| 8 | [PydanticAI](https://github.com/pydantic/pydantic-ai) | 🟡 **53.7** | 16.6k | 🚀 +163 | 0 | today | `structured` |
| 9 | [Agno](https://github.com/agno-agi/agno) | 🟡 **53.6** | 39.6k | 🚀 +154 | 0 | today | `multi-agent` |
| 10 | [Google ADK](https://github.com/google/adk-python) | 🟡 **53.4** | 19.2k | 🚀 +201 | 0 | 1 day ago | `orchestration` |
| 11 | [DSPy](https://github.com/stanfordnlp/dspy) | 🟡 **52.8** | 34.0k | 🚀 +212 | 0 | 2 days ago | `optimization` |
| 12 | [Haystack](https://github.com/deepset-ai/haystack) | 🟡 **50.4** | 25.0k | 🚀 +106 | 0 | 3 days ago | `pipeline` |
| 13 | [Semantic Kernel](https://github.com/microsoft/semantic-kernel) | 🟡 **49.4** | 27.8k | 📈 +45 | 0 | 16 days ago | `enterprise` |
| 14 | [AG2](https://github.com/ag2ai/ag2) | 🟡 **47.3** | 4.4k | 📈 +29 | 0 | 6 days ago | `multi-agent` |
| 15 | [Letta](https://github.com/letta-ai/letta) | 🟡 **46.3** | 22.3k | 🚀 +142 | 0 | 23 days ago | `memory` |
| 16 | [Composio](https://github.com/ComposioHQ/composio) | 🟡 **44.8** | 27.9k | 📈 +87 | 0 | today | `tooling` |
| 17 | [AutoGen](https://github.com/microsoft/autogen) | 🟡 **44.3** | 57.4k | 🚀 +218 | 0 | 6 mo ago | `multi-agent` |
| 18 | [Smolagents](https://github.com/huggingface/smolagents) | 🟠 **39.5** | 26.9k | 🚀 +186 | 0 | 3 mo ago | `lightweight` |
| 19 | [Swarm](https://github.com/openai/swarm) | 🔴 **10.1** | 21.4k | 📈 +48 | 0 | — | `experimental` |

## 📂 By Category

- `data-agent`: **LlamaIndex** (60.4)
- `enterprise`: **Semantic Kernel** (49.4)
- `experimental`: **Swarm** (10.1)
- `lightweight`: **Smolagents** (39.5)
- `memory`: **Letta** (46.3)
- `multi-agent`: **CrewAI** (70.5), **Agno** (53.6), **AG2** (47.3), **AutoGen** (44.3)
- `optimization`: **DSPy** (52.8)
- `orchestration`: **OpenAI Agents SDK** (70.6), **LangGraph** (69.1), **Claude Agent SDK** (64.6), **Google ADK** (53.4)
- `pipeline`: **Haystack** (50.4)
- `structured`: **PydanticAI** (53.7)
- `tooling`: **Composio** (44.8)
- `typescript`: **Mastra** (73.9)
- `web-agent`: **BrowserUse** (68.9)

## 🔍 Top 5 — Score Breakdown

| Framework | Star Velocity | Release Freshness | Issue Health | Commit Activity | Community | Fork Ratio |
|-----------|:---:|:---:|:---:|:---:|:---:|:---:|
| **Mastra** | 37.7 | 95.0 | 94.6 | 100 | 79.8 | 33.5 |
| **OpenAI Agents SDK** | 100 | 99.7 | 96.3 | 0.0 | 51.2 | 61.1 |
| **CrewAI** | 100 | 99.7 | 95.6 | 0.0 | 57.4 | 54.9 |
| **LangGraph** | 100 | 99.7 | 79.3 | 0.0 | 54.8 | 68.4 |
| **BrowserUse** | 100 | 92.7 | 97.6 | 0.0 | 61.8 | 45.7 |

## 💡 Key Insights

- **Hottest framework**: Mastra with a Pulse Score of 73.9
- **Fastest growing**: OpenAI Agents SDK gained +3462 stars this week
- **Most active development**: Mastra with 821 commits in the last 4 weeks
- **Stale releases**: Swarm haven't released in a while

## 📦 Recent Releases

- **PydanticAI** [`v1.86.1`](https://github.com/pydantic/pydantic-ai/releases/tag/v1.86.1) — today
- **Claude Agent SDK** [`v2.1.119`](https://github.com/anthropics/claude-code/releases/tag/v2.1.119) — today
- **Composio** [`py@0.11.6`](https://github.com/ComposioHQ/composio/releases/tag/py@0.11.6) — today
- **Agno** [`v2.6.0`](https://github.com/agno-agi/agno/releases/tag/v2.6.0) — today
- **OpenAI Agents SDK** [`v0.14.5`](https://github.com/openai/openai-agents-python/releases/tag/v0.14.5) — 1 day ago
- **CrewAI** [`1.14.3a3`](https://github.com/crewAIInc/crewAI/releases/tag/1.14.3a3) — 1 day ago *(pre-release)*
- **LangGraph** [`cli==0.4.24`](https://github.com/langchain-ai/langgraph/releases/tag/cli==0.4.24) — 1 day ago
- **Google ADK** [`v2.0.0b1`](https://github.com/google/adk-python/releases/tag/v2.0.0b1) — 1 day ago *(pre-release)*
- **DSPy** [`3.2.0`](https://github.com/stanfordnlp/dspy/releases/tag/3.2.0) — 2 days ago
- **LlamaIndex** [`v0.14.21`](https://github.com/run-llama/llama_index/releases/tag/v0.14.21) — 3 days ago

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

*Powered by GitHub Actions • Data refreshed daily • Last run: 2026-04-24 08:13 UTC*