# 🔬 AI Agent Framework Pulse Tracker

[![Daily Update](https://github.com/PurpleHaze2320/ai-agent-pulse/actions/workflows/track.yml/badge.svg)](https://github.com/PurpleHaze2320/ai-agent-pulse/actions/workflows/track.yml)
[![Frameworks Tracked](https://img.shields.io/badge/frameworks-19-blue)](https://github.com/PurpleHaze2320/ai-agent-pulse)
[![License: MIT](https://img.shields.io/badge/License-MIT-green.svg)](https://opensource.org/licenses/MIT)
[![GitHub stars](https://img.shields.io/github/stars/PurpleHaze2320/ai-agent-pulse?style=social)](https://github.com/PurpleHaze2320/ai-agent-pulse/stargazers)

> Automated daily tracking of the AI agent framework ecosystem's health, momentum, and trends.
> Last updated: **2026-06-30 09:50 UTC** | Tracking **19** frameworks

## How It Works

This bot runs daily via GitHub Actions and collects metrics from the GitHub API for the most important
AI agent frameworks. It computes a **Pulse Score** (0-100) based on six weighted signals: star velocity,
release freshness, issue health, commit activity, community size, and fork engagement. The result is
a living dashboard that shows which frameworks are gaining momentum and which are losing steam.

## 🏆 Pulse Leaderboard

| Rank | Framework | Pulse | Stars | ⭐ 7d | Commits (4w) | Last Release | Category |
|------|-----------|-------|-------|-------|--------------|--------------|----------|
| 1 | [CrewAI](https://github.com/crewAIInc/crewAI) | 🟢 **87.7** | 54.6k | 🚀 +402 | 112 | 3 days ago | `multi-agent` |
| 2 | [Mastra](https://github.com/mastra-ai/mastra) | 🟢 **79.6** | 25.6k | 🚀 +253 | 809 | 5 days ago | `typescript` |
| 3 | [LangGraph](https://github.com/langchain-ai/langgraph) | 🟢 **77.1** | 36.1k | 🚀 +622 | 44 | today | `orchestration` |
| 4 | [BrowserUse](https://github.com/browser-use/browser-use) | 🟢 **77.1** | 101.6k | 🚀 +1346 | 41 | 17 days ago | `web-agent` |
| 5 | [Haystack](https://github.com/deepset-ai/haystack) | 🟢 **72.6** | 25.8k | 🚀 +151 | 160 | 12 days ago | `pipeline` |
| 6 | [Claude Agent SDK](https://github.com/anthropics/claude-code) | 🟢 **70.9** | 135.1k | 🚀 +1185 | 26 | today | `orchestration` |
| 7 | [Google ADK](https://github.com/google/adk-python) | 🟢 **70.8** | 20.3k | 📈 +93 | 301 | 11 days ago | `orchestration` |
| 8 | [Composio](https://github.com/ComposioHQ/composio) | 🟡 **67.8** | 29.0k | 🚀 +115 | 116 | today | `tooling` |
| 9 | [OpenAI Agents SDK](https://github.com/openai/openai-agents-python) | 🟡 **64.1** | 27.5k | 🚀 +164 | 47 | 6 days ago | `orchestration` |
| 10 | [LlamaIndex](https://github.com/run-llama/llama_index) | 🟡 **62.8** | 50.5k | 🚀 +224 | 12 | 5 days ago | `data-agent` |
| 11 | [DSPy](https://github.com/stanfordnlp/dspy) | 🟡 **59.6** | 35.7k | 🚀 +350 | 12 | 1 mo ago | `optimization` |
| 12 | [Semantic Kernel](https://github.com/microsoft/semantic-kernel) | 🟡 **57.0** | 28.2k | 📈 +49 | 31 | 13 days ago | `enterprise` |
| 13 | [PydanticAI](https://github.com/pydantic/pydantic-ai) | 🟡 **55.4** | 18.1k | 🚀 +167 | 0 | today | `structured` |
| 14 | [Agno](https://github.com/agno-agi/agno) | 🟡 **51.3** | 40.9k | 📈 +99 | 0 | 6 days ago | `multi-agent` |
| 15 | [AG2](https://github.com/ag2ai/ag2) | 🟡 **49.7** | 4.7k | ↗️ +14 | 0 | 4 days ago | `multi-agent` |
| 16 | [Letta](https://github.com/letta-ai/letta) | 🟡 **44.5** | 23.6k | 🚀 +113 | 0 | 1 mo ago | `memory` |
| 17 | [Smolagents](https://github.com/huggingface/smolagents) | 🟡 **42.2** | 28.1k | 🚀 +131 | 0 | 1 mo ago | `lightweight` |
| 18 | [AutoGen](https://github.com/microsoft/autogen) | 🟠 **38.8** | 59.4k | 🚀 +190 | 0 | 9 mo ago | `multi-agent` |
| 19 | [Swarm](https://github.com/openai/swarm) | 🔴 **10.2** | 21.8k | 📈 +50 | 0 | — | `experimental` |

## 📂 By Category

- `data-agent`: **LlamaIndex** (62.8)
- `enterprise`: **Semantic Kernel** (57.0)
- `experimental`: **Swarm** (10.2)
- `lightweight`: **Smolagents** (42.2)
- `memory`: **Letta** (44.5)
- `multi-agent`: **CrewAI** (87.7), **Agno** (51.3), **AG2** (49.7), **AutoGen** (38.8)
- `optimization`: **DSPy** (59.6)
- `orchestration`: **LangGraph** (77.1), **Claude Agent SDK** (70.9), **Google ADK** (70.8), **OpenAI Agents SDK** (64.1)
- `pipeline`: **Haystack** (72.6)
- `structured`: **PydanticAI** (55.4)
- `tooling`: **Composio** (67.8)
- `typescript`: **Mastra** (79.6)
- `web-agent`: **BrowserUse** (77.1)

## 🔍 Top 5 — Score Breakdown

| Framework | Star Velocity | Release Freshness | Issue Health | Commit Activity | Community | Fork Ratio |
|-----------|:---:|:---:|:---:|:---:|:---:|:---:|
| **CrewAI** | 87.9 | 99.0 | 96.0 | 100 | 59.6 | 56.0 |
| **Mastra** | 50.9 | 98.3 | 95.4 | 100 | 92.4 | 36.3 |
| **LangGraph** | 100 | 100.0 | 73.7 | 44.0 | 55.0 | 67.0 |
| **BrowserUse** | 100 | 94.3 | 95.4 | 41.0 | 63.0 | 44.4 |
| **Haystack** | 26.7 | 96.0 | 98.2 | 100 | 75.2 | 44.9 |

## 💡 Key Insights

- **Hottest framework**: CrewAI with a Pulse Score of 87.7
- **Fastest growing**: BrowserUse gained +1346 stars this week
- **Most active development**: Mastra with 809 commits in the last 4 weeks
- **Stale releases**: AutoGen, Swarm haven't released in a while

## 📦 Recent Releases

- **LangGraph** [`1.2.7`](https://github.com/langchain-ai/langgraph/releases/tag/1.2.7) — today
- **PydanticAI** [`v2.1.1`](https://github.com/pydantic/pydantic-ai/releases/tag/v2.1.1) — today
- **Claude Agent SDK** [`v2.1.196`](https://github.com/anthropics/claude-code/releases/tag/v2.1.196) — today
- **Composio** [`@composio/cli@0.2.32-beta.280`](https://github.com/ComposioHQ/composio/releases/tag/@composio/cli@0.2.32-beta.280) — today *(pre-release)*
- **CrewAI** [`1.15.1`](https://github.com/crewAIInc/crewAI/releases/tag/1.15.1) — 3 days ago
- **AG2** [`v0.14.0`](https://github.com/ag2ai/ag2/releases/tag/v0.14.0) — 4 days ago
- **LlamaIndex** [`v0.14.23`](https://github.com/run-llama/llama_index/releases/tag/v0.14.23) — 5 days ago
- **Mastra** [`@mastra/core@1.46.0`](https://github.com/mastra-ai/mastra/releases/tag/@mastra/core@1.46.0) — 5 days ago
- **OpenAI Agents SDK** [`v0.17.7`](https://github.com/openai/openai-agents-python/releases/tag/v0.17.7) — 6 days ago
- **Agno** [`v2.6.19`](https://github.com/agno-agi/agno/releases/tag/v2.6.19) — 6 days ago

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

*Powered by GitHub Actions • Data refreshed daily • Last run: 2026-06-30 09:50 UTC*