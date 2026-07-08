# 🔬 AI Agent Framework Pulse Tracker

[![Daily Update](https://github.com/PurpleHaze2320/ai-agent-pulse/actions/workflows/track.yml/badge.svg)](https://github.com/PurpleHaze2320/ai-agent-pulse/actions/workflows/track.yml)
[![Frameworks Tracked](https://img.shields.io/badge/frameworks-19-blue)](https://github.com/PurpleHaze2320/ai-agent-pulse)
[![License: MIT](https://img.shields.io/badge/License-MIT-green.svg)](https://opensource.org/licenses/MIT)
[![GitHub stars](https://img.shields.io/github/stars/PurpleHaze2320/ai-agent-pulse?style=social)](https://github.com/PurpleHaze2320/ai-agent-pulse/stargazers)

> Automated daily tracking of the AI agent framework ecosystem's health, momentum, and trends.
> Last updated: **2026-07-08 08:37 UTC** | Tracking **19** frameworks

## How It Works

This bot runs daily via GitHub Actions and collects metrics from the GitHub API for the most important
AI agent frameworks. It computes a **Pulse Score** (0-100) based on six weighted signals: star velocity,
release freshness, issue health, commit activity, community size, and fork engagement. The result is
a living dashboard that shows which frameworks are gaining momentum and which are losing steam.

## 🏆 Pulse Leaderboard

| Rank | Framework | Pulse | Stars | ⭐ 7d | Commits (4w) | Last Release | Category |
|------|-----------|-------|-------|-------|--------------|--------------|----------|
| 1 | [CrewAI](https://github.com/crewAIInc/crewAI) | 🟢 **89.6** | 55.1k | 🚀 +454 | 103 | today | `multi-agent` |
| 2 | [BrowserUse](https://github.com/browser-use/browser-use) | 🟢 **82.8** | 103.4k | 🚀 +1520 | 66 | 6 days ago | `web-agent` |
| 3 | [Mastra](https://github.com/mastra-ai/mastra) | 🟢 **81.2** | 25.9k | 🚀 +288 | 956 | 1 day ago | `typescript` |
| 4 | [LangGraph](https://github.com/langchain-ai/langgraph) | 🟢 **77.8** | 36.8k | 🚀 +575 | 48 | 1 day ago | `orchestration` |
| 5 | [PydanticAI](https://github.com/pydantic/pydantic-ai) | 🟢 **75.1** | 18.3k | 🚀 +151 | 190 | today | `structured` |
| 6 | [Google ADK](https://github.com/google/adk-python) | 🟢 **73.9** | 20.5k | 🚀 +141 | 308 | today | `orchestration` |
| 7 | [Agno](https://github.com/agno-agi/agno) | 🟢 **71.8** | 41.0k | 🚀 +110 | 99 | today | `multi-agent` |
| 8 | [Claude Agent SDK](https://github.com/anthropics/claude-code) | 🟢 **70.9** | 136.8k | 🚀 +1542 | 27 | today | `orchestration` |
| 9 | [OpenAI Agents SDK](https://github.com/openai/openai-agents-python) | 🟢 **70.0** | 27.7k | 🚀 +183 | 71 | 1 day ago | `orchestration` |
| 10 | [Composio](https://github.com/ComposioHQ/composio) | 🟡 **67.0** | 29.1k | 📈 +94 | 128 | today | `tooling` |
| 11 | [LlamaIndex](https://github.com/run-llama/llama_index) | 🟡 **62.8** | 50.7k | 🚀 +164 | 25 | 13 days ago | `data-agent` |
| 12 | [Semantic Kernel](https://github.com/microsoft/semantic-kernel) | 🟡 **59.4** | 28.3k | 📈 +53 | 38 | today | `enterprise` |
| 13 | [DSPy](https://github.com/stanfordnlp/dspy) | 🟡 **52.5** | 35.9k | 🚀 +220 | 0 | 1 mo ago | `optimization` |
| 14 | [AG2](https://github.com/ag2ai/ag2) | 🟡 **50.1** | 4.7k | 📈 +26 | 0 | 4 days ago | `multi-agent` |
| 15 | [Haystack](https://github.com/deepset-ai/haystack) | 🟡 **50.0** | 25.8k | 📈 +55 | 0 | 1 day ago | `pipeline` |
| 16 | [Letta](https://github.com/letta-ai/letta) | 🟡 **43.3** | 23.7k | 📈 +95 | 0 | 1 mo ago | `memory` |
| 17 | [Smolagents](https://github.com/huggingface/smolagents) | 🟡 **41.5** | 28.2k | 🚀 +120 | 1 | 1 mo ago | `lightweight` |
| 18 | [AutoGen](https://github.com/microsoft/autogen) | 🟠 **37.8** | 59.6k | 🚀 +180 | 0 | 9 mo ago | `multi-agent` |
| 19 | [Swarm](https://github.com/openai/swarm) | 🔴 **9.0** | 21.8k | ↗️ +18 | 0 | — | `experimental` |

## 📂 By Category

- `data-agent`: **LlamaIndex** (62.8)
- `enterprise`: **Semantic Kernel** (59.4)
- `experimental`: **Swarm** (9.0)
- `lightweight`: **Smolagents** (41.5)
- `memory`: **Letta** (43.3)
- `multi-agent`: **CrewAI** (89.6), **Agno** (71.8), **AG2** (50.1), **AutoGen** (37.8)
- `optimization`: **DSPy** (52.5)
- `orchestration`: **LangGraph** (77.8), **Google ADK** (73.9), **Claude Agent SDK** (70.9), **OpenAI Agents SDK** (70.0)
- `pipeline`: **Haystack** (50.0)
- `structured`: **PydanticAI** (75.1)
- `tooling`: **Composio** (67.0)
- `typescript`: **Mastra** (81.2)
- `web-agent`: **BrowserUse** (82.8)

## 🔍 Top 5 — Score Breakdown

| Framework | Star Velocity | Release Freshness | Issue Health | Commit Activity | Community | Fork Ratio |
|-----------|:---:|:---:|:---:|:---:|:---:|:---:|
| **CrewAI** | 94.8 | 100.0 | 95.7 | 100 | 59.6 | 56.2 |
| **BrowserUse** | 100 | 98.0 | 95.0 | 66.0 | 63.0 | 44.2 |
| **Mastra** | 56.2 | 99.7 | 95.5 | 100 | 92.4 | 36.6 |
| **LangGraph** | 100 | 99.7 | 73.4 | 48.0 | 55.0 | 67.1 |
| **PydanticAI** | 31.0 | 100.0 | 85.4 | 100 | 94.8 | 50.7 |

## 💡 Key Insights

- **Hottest framework**: CrewAI with a Pulse Score of 89.6
- **Fastest growing**: Claude Agent SDK gained +1542 stars this week
- **Most active development**: Mastra with 956 commits in the last 4 weeks
- **Stale releases**: AutoGen, Swarm haven't released in a while

## 📦 Recent Releases

- **CrewAI** [`1.15.2`](https://github.com/crewAIInc/crewAI/releases/tag/1.15.2) — today
- **PydanticAI** [`v2.6.0`](https://github.com/pydantic/pydantic-ai/releases/tag/v2.6.0) — today
- **Claude Agent SDK** [`v2.1.204`](https://github.com/anthropics/claude-code/releases/tag/v2.1.204) — today
- **Agno** [`v2.7.1`](https://github.com/agno-agi/agno/releases/tag/v2.7.1) — today
- **Google ADK** [`v2.4.0`](https://github.com/google/adk-python/releases/tag/v2.4.0) — today
- **Composio** [`@composio/cli@0.2.32-beta.286`](https://github.com/ComposioHQ/composio/releases/tag/@composio/cli@0.2.32-beta.286) — today *(pre-release)*
- **Semantic Kernel** [`python-1.44.0`](https://github.com/microsoft/semantic-kernel/releases/tag/python-1.44.0) — today
- **Haystack** [`v2.31.0-rc2`](https://github.com/deepset-ai/haystack/releases/tag/v2.31.0-rc2) — 1 day ago *(pre-release)*
- **Mastra** [`@mastra/core@1.49.0`](https://github.com/mastra-ai/mastra/releases/tag/@mastra/core@1.49.0) — 1 day ago
- **OpenAI Agents SDK** [`v0.18.0`](https://github.com/openai/openai-agents-python/releases/tag/v0.18.0) — 1 day ago

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

*Powered by GitHub Actions • Data refreshed daily • Last run: 2026-07-08 08:37 UTC*