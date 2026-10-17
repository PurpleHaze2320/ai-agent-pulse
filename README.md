# 🔬 AI Agent Framework Pulse Tracker

[![Daily Update](https://github.com/PurpleHaze2320/ai-agent-pulse/actions/workflows/track.yml/badge.svg)](https://github.com/PurpleHaze2320/ai-agent-pulse/actions/workflows/track.yml)
[![Frameworks Tracked](https://img.shields.io/badge/frameworks-19-blue)](https://github.com/PurpleHaze2320/ai-agent-pulse)
[![License: MIT](https://img.shields.io/badge/License-MIT-green.svg)](https://opensource.org/licenses/MIT)
[![GitHub stars](https://img.shields.io/github/stars/PurpleHaze2320/ai-agent-pulse?style=social)](https://github.com/PurpleHaze2320/ai-agent-pulse/stargazers)

> Automated daily tracking of the AI agent framework ecosystem's health, momentum, and trends.
> Last updated: **2026-10-17 10:24 UTC** | Tracking **19** frameworks

## How It Works

This bot runs daily via GitHub Actions and collects metrics from the GitHub API for the most important
AI agent frameworks. It computes a **Pulse Score** (0-100) based on six weighted signals: star velocity,
release freshness, issue health, commit activity, community size, and fork engagement. The result is
a living dashboard that shows which frameworks are gaining momentum and which are losing steam.

## 🏆 Pulse Leaderboard

| Rank | Framework | Pulse | Stars | ⭐ 7d | Commits (4w) | Last Release | Category |
|------|-----------|-------|-------|-------|--------------|--------------|----------|
| 1 | [BrowserUse](https://github.com/browser-use/browser-use) | 🟢 **87.4** | 118.3k | 🚀 +758 | 87 | 1 day ago | `web-agent` |
| 2 | [LangGraph](https://github.com/langchain-ai/langgraph) | 🟢 **82.7** | 43.4k | 🚀 +376 | 101 | today | `orchestration` |
| 3 | [Claude Agent SDK](https://github.com/anthropics/claude-code) | 🟢 **79.1** | 151.3k | 🚀 +1338 | 65 | today | `orchestration` |
| 4 | [Mastra](https://github.com/mastra-ai/mastra) | 🟢 **76.9** | 28.9k | 🚀 +183 | 2256 | 1 day ago | `typescript` |
| 5 | [CrewAI](https://github.com/crewAIInc/crewAI) | 🟢 **76.8** | 59.8k | 🚀 +260 | 89 | 3 days ago | `multi-agent` |
| 6 | [OpenAI Agents SDK](https://github.com/openai/openai-agents-python) | 🟢 **76.7** | 30.1k | 🚀 +146 | 224 | 2 days ago | `orchestration` |
| 7 | [Google ADK](https://github.com/google/adk-python) | 🟢 **76.0** | 21.9k | 🚀 +124 | 558 | 3 days ago | `orchestration` |
| 8 | [PydanticAI](https://github.com/pydantic/pydantic-ai) | 🟢 **73.8** | 20.7k | 🚀 +143 | 924 | 1 day ago | `structured` |
| 9 | [Agno](https://github.com/agno-agi/agno) | 🟢 **71.7** | 42.8k | 🚀 +123 | 130 | today | `multi-agent` |
| 10 | [Haystack](https://github.com/deepset-ai/haystack) | 🟢 **70.6** | 26.8k | 📈 +38 | 288 | 2 days ago | `pipeline` |
| 11 | [Composio](https://github.com/ComposioHQ/composio) | 🟡 **68.3** | 30.6k | 🚀 +121 | 336 | 1 day ago | `tooling` |
| 12 | [DSPy](https://github.com/stanfordnlp/dspy) | 🟡 **60.2** | 38.7k | 📈 +87 | 58 | 4 days ago | `optimization` |
| 13 | [LlamaIndex](https://github.com/run-llama/llama_index) | 🟡 **56.9** | 52.5k | 📈 +75 | 22 | 25 days ago | `data-agent` |
| 14 | [Semantic Kernel](https://github.com/microsoft/semantic-kernel) | 🟡 **54.8** | 28.7k | 📈 +31 | 23 | 10 days ago | `enterprise` |
| 15 | [AG2](https://github.com/ag2ai/ag2) | 🟡 **49.4** | 5.0k | ↗️ +12 | 0 | 6 days ago | `multi-agent` |
| 16 | [Letta](https://github.com/letta-ai/letta) | 🟠 **35.7** | 25.2k | 📈 +74 | 0 | 5 mo ago | `memory` |
| 17 | [Smolagents](https://github.com/huggingface/smolagents) | 🟠 **35.1** | 29.9k | 🚀 +129 | 5 | 4 mo ago | `lightweight` |
| 18 | [AutoGen](https://github.com/microsoft/autogen) | 🟠 **32.8** | 61.4k | 🚀 +108 | 1 | 1y ago | `multi-agent` |
| 19 | [Swarm](https://github.com/openai/swarm) | 🔴 **9.2** | 22.1k | ↗️ +14 | 0 | — | `experimental` |

## 📂 By Category

- `data-agent`: **LlamaIndex** (56.9)
- `enterprise`: **Semantic Kernel** (54.8)
- `experimental`: **Swarm** (9.2)
- `lightweight`: **Smolagents** (35.1)
- `memory`: **Letta** (35.7)
- `multi-agent`: **CrewAI** (76.8), **Agno** (71.7), **AG2** (49.4), **AutoGen** (32.8)
- `optimization`: **DSPy** (60.2)
- `orchestration`: **LangGraph** (82.7), **Claude Agent SDK** (79.1), **OpenAI Agents SDK** (76.7), **Google ADK** (76.0)
- `pipeline`: **Haystack** (70.6)
- `structured`: **PydanticAI** (73.8)
- `tooling`: **Composio** (68.3)
- `typescript`: **Mastra** (76.9)
- `web-agent`: **BrowserUse** (87.4)

## 🔍 Top 5 — Score Breakdown

| Framework | Star Velocity | Release Freshness | Issue Health | Commit Activity | Community | Fork Ratio |
|-----------|:---:|:---:|:---:|:---:|:---:|:---:|
| **BrowserUse** | 100 | 99.7 | 89.4 | 87.0 | 72.0 | 44.4 |
| **LangGraph** | 76.3 | 100.0 | 74.5 | 100 | 56.6 | 68.2 |
| **Claude Agent SDK** | 100 | 100.0 | 85.6 | 65.0 | 11.4 | 71.0 |
| **Mastra** | 36.6 | 99.7 | 95.3 | 100 | 93.4 | 41.5 |
| **CrewAI** | 52.9 | 99.0 | 88.1 | 89.0 | 69.0 | 58.6 |

## 💡 Key Insights

- **Hottest framework**: BrowserUse with a Pulse Score of 87.4
- **Fastest growing**: Claude Agent SDK gained +1338 stars this week
- **Most active development**: Mastra with 2256 commits in the last 4 weeks
- **Stale releases**: AutoGen, Swarm haven't released in a while

## 📦 Recent Releases

- **LangGraph** [`1.2.16`](https://github.com/langchain-ai/langgraph/releases/tag/1.2.16) — today
- **Claude Agent SDK** [`v2.1.302`](https://github.com/anthropics/claude-code/releases/tag/v2.1.302) — today
- **Agno** [`v3.1.4`](https://github.com/agno-agi/agno/releases/tag/v3.1.4) — today
- **Composio** [`@composio/cli@0.4.6-beta.457`](https://github.com/ComposioHQ/composio/releases/tag/@composio/cli@0.4.6-beta.457) — 1 day ago *(pre-release)*
- **Mastra** [`@mastra/core@1.78.0`](https://github.com/mastra-ai/mastra/releases/tag/@mastra/core@1.78.0) — 1 day ago
- **PydanticAI** [`v2.57.0`](https://github.com/pydantic/pydantic-ai/releases/tag/v2.57.0) — 1 day ago
- **BrowserUse** [`0.13.13`](https://github.com/browser-use/browser-use/releases/tag/0.13.13) — 1 day ago
- **Haystack** [`v3.4.0`](https://github.com/deepset-ai/haystack/releases/tag/v3.4.0) — 2 days ago
- **OpenAI Agents SDK** [`v0.24.0`](https://github.com/openai/openai-agents-python/releases/tag/v0.24.0) — 2 days ago
- **CrewAI** [`1.15.28`](https://github.com/crewAIInc/crewAI/releases/tag/1.15.28) — 3 days ago

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

*Powered by GitHub Actions • Data refreshed daily • Last run: 2026-10-17 10:24 UTC*