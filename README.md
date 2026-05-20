# 🔬 AI Agent Framework Pulse Tracker

[![Daily Update](https://github.com/PurpleHaze2320/ai-agent-pulse/actions/workflows/track.yml/badge.svg)](https://github.com/PurpleHaze2320/ai-agent-pulse/actions/workflows/track.yml)
[![Frameworks Tracked](https://img.shields.io/badge/frameworks-19-blue)](https://github.com/PurpleHaze2320/ai-agent-pulse)
[![License: MIT](https://img.shields.io/badge/License-MIT-green.svg)](https://opensource.org/licenses/MIT)
[![GitHub stars](https://img.shields.io/github/stars/PurpleHaze2320/ai-agent-pulse?style=social)](https://github.com/PurpleHaze2320/ai-agent-pulse/stargazers)

> Automated daily tracking of the AI agent framework ecosystem's health, momentum, and trends.
> Last updated: **2026-05-20 09:44 UTC** | Tracking **19** frameworks

## How It Works

This bot runs daily via GitHub Actions and collects metrics from the GitHub API for the most important
AI agent frameworks. It computes a **Pulse Score** (0-100) based on six weighted signals: star velocity,
release freshness, issue health, commit activity, community size, and fork engagement. The result is
a living dashboard that shows which frameworks are gaining momentum and which are losing steam.

## 🏆 Pulse Leaderboard

| Rank | Framework | Pulse | Stars | ⭐ 7d | Commits (4w) | Last Release | Category |
|------|-----------|-------|-------|-------|--------------|--------------|----------|
| 1 | [Mastra](https://github.com/mastra-ai/mastra) | 🟢 **77.7** | 24.1k | 🚀 +228 | 927 | 1 day ago | `typescript` |
| 2 | [CrewAI](https://github.com/crewAIInc/crewAI) | 🟢 **71.2** | 51.8k | 🚀 +473 | 0 | 1 day ago | `multi-agent` |
| 3 | [BrowserUse](https://github.com/browser-use/browser-use) | 🟢 **70.2** | 94.8k | 🚀 +1101 | 0 | 1 day ago | `web-agent` |
| 4 | [LangGraph](https://github.com/langchain-ai/langgraph) | 🟡 **68.2** | 32.5k | 🚀 +565 | 0 | 8 days ago | `orchestration` |
| 5 | [OpenAI Agents SDK](https://github.com/openai/openai-agents-python) | 🟡 **65.1** | 26.5k | 🚀 +230 | 0 | 1 day ago | `orchestration` |
| 6 | [Claude Agent SDK](https://github.com/anthropics/claude-code) | 🟡 **64.8** | 125.1k | 🚀 +2043 | 0 | today | `orchestration` |
| 7 | [LlamaIndex](https://github.com/run-llama/llama_index) | 🟡 **58.2** | 49.5k | 🚀 +152 | 0 | 5 days ago | `data-agent` |
| 8 | [Agno](https://github.com/agno-agi/agno) | 🟡 **54.0** | 40.2k | 🚀 +150 | 0 | today | `multi-agent` |
| 9 | [PydanticAI](https://github.com/pydantic/pydantic-ai) | 🟡 **53.0** | 17.2k | 🚀 +121 | 0 | today | `structured` |
| 10 | [Google ADK](https://github.com/google/adk-python) | 🟡 **51.4** | 19.7k | 🚀 +126 | 0 | today | `orchestration` |
| 11 | [Semantic Kernel](https://github.com/microsoft/semantic-kernel) | 🟡 **51.0** | 27.9k | 📈 +48 | 0 | 6 days ago | `enterprise` |
| 12 | [DSPy](https://github.com/stanfordnlp/dspy) | 🟡 **50.6** | 34.5k | 🚀 +151 | 0 | 14 days ago | `optimization` |
| 13 | [Haystack](https://github.com/deepset-ai/haystack) | 🟡 **50.3** | 25.3k | 📈 +92 | 0 | 7 days ago | `pipeline` |
| 14 | [Composio](https://github.com/ComposioHQ/composio) | 🟡 **49.4** | 28.4k | 🚀 +158 | 0 | today | `tooling` |
| 15 | [Letta](https://github.com/letta-ai/letta) | 🟡 **49.0** | 22.8k | 🚀 +149 | 0 | 5 days ago | `memory` |
| 16 | [AG2](https://github.com/ag2ai/ag2) | 🟡 **49.0** | 4.6k | 📈 +42 | 0 | 7 days ago | `multi-agent` |
| 17 | [Smolagents](https://github.com/huggingface/smolagents) | 🟡 **44.7** | 27.4k | 🚀 +130 | 0 | 5 days ago | `lightweight` |
| 18 | [AutoGen](https://github.com/microsoft/autogen) | 🟡 **43.1** | 58.2k | 🚀 +214 | 0 | 7 mo ago | `multi-agent` |
| 19 | [Swarm](https://github.com/openai/swarm) | 🔴 **9.1** | 21.5k | 📈 +31 | 0 | — | `experimental` |

## 📂 By Category

- `data-agent`: **LlamaIndex** (58.2)
- `enterprise`: **Semantic Kernel** (51.0)
- `experimental`: **Swarm** (9.1)
- `lightweight`: **Smolagents** (44.7)
- `memory`: **Letta** (49.0)
- `multi-agent`: **CrewAI** (71.2), **Agno** (54.0), **AG2** (49.0), **AutoGen** (43.1)
- `optimization`: **DSPy** (50.6)
- `orchestration`: **LangGraph** (68.2), **OpenAI Agents SDK** (65.1), **Claude Agent SDK** (64.8), **Google ADK** (51.4)
- `pipeline`: **Haystack** (50.3)
- `structured`: **PydanticAI** (53.0)
- `tooling`: **Composio** (49.4)
- `typescript`: **Mastra** (77.7)
- `web-agent`: **BrowserUse** (70.2)

## 🔍 Top 5 — Score Breakdown

| Framework | Star Velocity | Release Freshness | Issue Health | Commit Activity | Community | Fork Ratio |
|-----------|:---:|:---:|:---:|:---:|:---:|:---:|
| **Mastra** | 45.4 | 99.7 | 94.8 | 100 | 87.2 | 34.8 |
| **CrewAI** | 100 | 99.7 | 98.4 | 0.0 | 59.4 | 55.4 |
| **BrowserUse** | 100 | 99.7 | 96.1 | 0.0 | 63.0 | 45.1 |
| **LangGraph** | 100 | 97.3 | 76.5 | 0.0 | 54.6 | 67.8 |
| **OpenAI Agents SDK** | 76.5 | 99.7 | 96.6 | 0.0 | 54.6 | 61.4 |

## 💡 Key Insights

- **Hottest framework**: Mastra with a Pulse Score of 77.7
- **Fastest growing**: Claude Agent SDK gained +2043 stars this week
- **Most active development**: Mastra with 927 commits in the last 4 weeks
- **Stale releases**: Swarm haven't released in a while

## 📦 Recent Releases

- **Composio** [`@composio/cli@0.2.31-beta.256`](https://github.com/ComposioHQ/composio/releases/tag/@composio/cli@0.2.31-beta.256) — today *(pre-release)*
- **PydanticAI** [`v1.99.0`](https://github.com/pydantic/pydantic-ai/releases/tag/v1.99.0) — today
- **Agno** [`v2.6.8`](https://github.com/agno-agi/agno/releases/tag/v2.6.8) — today
- **Claude Agent SDK** [`v2.1.145`](https://github.com/anthropics/claude-code/releases/tag/v2.1.145) — today
- **Google ADK** [`v2.0.0`](https://github.com/google/adk-python/releases/tag/v2.0.0) — today
- **OpenAI Agents SDK** [`v0.17.3`](https://github.com/openai/openai-agents-python/releases/tag/v0.17.3) — 1 day ago
- **BrowserUse** [`0.12.7`](https://github.com/browser-use/browser-use/releases/tag/0.12.7) — 1 day ago
- **CrewAI** [`1.14.5`](https://github.com/crewAIInc/crewAI/releases/tag/1.14.5) — 1 day ago
- **Mastra** [`@mastra/core@1.35.0`](https://github.com/mastra-ai/mastra/releases/tag/@mastra/core@1.35.0) — 1 day ago
- **LlamaIndex** [`v0.14.22`](https://github.com/run-llama/llama_index/releases/tag/v0.14.22) — 5 days ago

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

*Powered by GitHub Actions • Data refreshed daily • Last run: 2026-05-20 09:44 UTC*