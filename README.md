# 🔬 AI Agent Framework Pulse Tracker

[![Daily Update](https://github.com/PurpleHaze2320/ai-agent-pulse/actions/workflows/track.yml/badge.svg)](https://github.com/PurpleHaze2320/ai-agent-pulse/actions/workflows/track.yml)
[![Frameworks Tracked](https://img.shields.io/badge/frameworks-19-blue)](https://github.com/PurpleHaze2320/ai-agent-pulse)
[![License: MIT](https://img.shields.io/badge/License-MIT-green.svg)](https://opensource.org/licenses/MIT)
[![GitHub stars](https://img.shields.io/github/stars/PurpleHaze2320/ai-agent-pulse?style=social)](https://github.com/PurpleHaze2320/ai-agent-pulse/stargazers)

> Automated daily tracking of the AI agent framework ecosystem's health, momentum, and trends.
> Last updated: **2026-08-13 07:41 UTC** | Tracking **19** frameworks

## How It Works

This bot runs daily via GitHub Actions and collects metrics from the GitHub API for the most important
AI agent frameworks. It computes a **Pulse Score** (0-100) based on six weighted signals: star velocity,
release freshness, issue health, commit activity, community size, and fork engagement. The result is
a living dashboard that shows which frameworks are gaining momentum and which are losing steam.

## 🏆 Pulse Leaderboard

| Rank | Framework | Pulse | Stars | ⭐ 7d | Commits (4w) | Last Release | Category |
|------|-----------|-------|-------|-------|--------------|--------------|----------|
| 1 | [BrowserUse](https://github.com/browser-use/browser-use) | 🟢 **89.1** | 109.0k | 🚀 +1002 | 149 | 16 days ago | `web-agent` |
| 2 | [CrewAI](https://github.com/crewAIInc/crewAI) | 🟢 **80.1** | 57.0k | 🚀 +329 | 85 | 1 day ago | `multi-agent` |
| 3 | [Mastra](https://github.com/mastra-ai/mastra) | 🟢 **78.0** | 27.2k | 🚀 +191 | 1408 | today | `typescript` |
| 4 | [PydanticAI](https://github.com/pydantic/pydantic-ai) | 🟢 **76.0** | 19.3k | 🚀 +172 | 257 | today | `structured` |
| 5 | [LangGraph](https://github.com/langchain-ai/langgraph) | 🟢 **75.7** | 39.6k | 🚀 +573 | 40 | 1 day ago | `orchestration` |
| 6 | [Haystack](https://github.com/deepset-ai/haystack) | 🟡 **69.5** | 26.2k | 📈 +66 | 199 | 23 days ago | `pipeline` |
| 7 | [Claude Agent SDK](https://github.com/anthropics/claude-code) | 🟡 **68.1** | 141.3k | 🚀 +849 | 17 | today | `orchestration` |
| 8 | [Composio](https://github.com/ComposioHQ/composio) | 🟡 **67.8** | 29.7k | 🚀 +104 | 311 | today | `tooling` |
| 9 | [Agno](https://github.com/agno-agi/agno) | 🟡 **65.3** | 41.7k | 📈 +87 | 73 | 6 days ago | `multi-agent` |
| 10 | [DSPy](https://github.com/stanfordnlp/dspy) | 🟡 **64.8** | 37.2k | 🚀 +507 | 0 | 9 days ago | `optimization` |
| 11 | [LlamaIndex](https://github.com/run-llama/llama_index) | 🟡 **62.5** | 51.6k | 🚀 +199 | 28 | 1 mo ago | `data-agent` |
| 12 | [OpenAI Agents SDK](https://github.com/openai/openai-agents-python) | 🟡 **56.5** | 28.6k | 🚀 +173 | 0 | 2 days ago | `orchestration` |
| 13 | [Semantic Kernel](https://github.com/microsoft/semantic-kernel) | 🟡 **54.2** | 28.4k | ↗️ +20 | 20 | 6 days ago | `enterprise` |
| 14 | [Google ADK](https://github.com/google/adk-python) | 🟡 **53.1** | 21.1k | 📈 +75 | 0 | 5 days ago | `orchestration` |
| 15 | [AG2](https://github.com/ag2ai/ag2) | 🟡 **49.3** | 4.9k | 📈 +21 | 0 | 15 days ago | `multi-agent` |
| 16 | [Letta](https://github.com/letta-ai/letta) | 🟡 **41.8** | 24.2k | 🚀 +112 | 2 | 3 mo ago | `memory` |
| 17 | [Smolagents](https://github.com/huggingface/smolagents) | 🟠 **37.7** | 28.8k | 📈 +95 | 0 | 2 mo ago | `lightweight` |
| 18 | [AutoGen](https://github.com/microsoft/autogen) | 🟠 **34.4** | 60.4k | 🚀 +133 | 0 | 10 mo ago | `multi-agent` |
| 19 | [Swarm](https://github.com/openai/swarm) | 🔴 **9.6** | 21.9k | ↗️ +18 | 0 | — | `experimental` |

## 📂 By Category

- `data-agent`: **LlamaIndex** (62.5)
- `enterprise`: **Semantic Kernel** (54.2)
- `experimental`: **Swarm** (9.6)
- `lightweight`: **Smolagents** (37.7)
- `memory`: **Letta** (41.8)
- `multi-agent`: **CrewAI** (80.1), **Agno** (65.3), **AG2** (49.3), **AutoGen** (34.4)
- `optimization`: **DSPy** (64.8)
- `orchestration`: **LangGraph** (75.7), **Claude Agent SDK** (68.1), **OpenAI Agents SDK** (56.5), **Google ADK** (53.1)
- `pipeline`: **Haystack** (69.5)
- `structured`: **PydanticAI** (76.0)
- `tooling`: **Composio** (67.8)
- `typescript`: **Mastra** (78.0)
- `web-agent`: **BrowserUse** (89.1)

## 🔍 Top 5 — Score Breakdown

| Framework | Star Velocity | Release Freshness | Issue Health | Commit Activity | Community | Fork Ratio |
|-----------|:---:|:---:|:---:|:---:|:---:|:---:|
| **BrowserUse** | 100 | 94.7 | 93.9 | 100 | 66.8 | 43.9 |
| **CrewAI** | 69.0 | 99.7 | 95.0 | 85.0 | 60.0 | 57.1 |
| **Mastra** | 41.9 | 100.0 | 95.9 | 100 | 92.8 | 38.6 |
| **PydanticAI** | 35.4 | 100.0 | 82.9 | 100 | 95.0 | 52.2 |
| **LangGraph** | 100 | 99.7 | 70.4 | 40.0 | 55.4 | 67.1 |

## 💡 Key Insights

- **Hottest framework**: BrowserUse with a Pulse Score of 89.1
- **Fastest growing**: BrowserUse gained +1002 stars this week
- **Most active development**: Mastra with 1408 commits in the last 4 weeks
- **Stale releases**: AutoGen, Swarm haven't released in a while

## 📦 Recent Releases

- **PydanticAI** [`v2.29.0`](https://github.com/pydantic/pydantic-ai/releases/tag/v2.29.0) — today
- **Composio** [`@composio/cli@0.3.4-beta.350`](https://github.com/ComposioHQ/composio/releases/tag/@composio/cli@0.3.4-beta.350) — today *(pre-release)*
- **Claude Agent SDK** [`v2.1.229`](https://github.com/anthropics/claude-code/releases/tag/v2.1.229) — today
- **Mastra** [`@mastra/core@1.58.0`](https://github.com/mastra-ai/mastra/releases/tag/@mastra/core@1.58.0) — today
- **CrewAI** [`1.15.15`](https://github.com/crewAIInc/crewAI/releases/tag/1.15.15) — 1 day ago
- **LangGraph** [`1.2.11`](https://github.com/langchain-ai/langgraph/releases/tag/1.2.11) — 1 day ago
- **OpenAI Agents SDK** [`v0.20.0`](https://github.com/openai/openai-agents-python/releases/tag/v0.20.0) — 2 days ago
- **Google ADK** [`v2.6.3`](https://github.com/google/adk-python/releases/tag/v2.6.3) — 5 days ago
- **Agno** [`v3.0.0a1`](https://github.com/agno-agi/agno/releases/tag/v3.0.0a1) — 6 days ago *(pre-release)*
- **Semantic Kernel** [`python-1.44.1`](https://github.com/microsoft/semantic-kernel/releases/tag/python-1.44.1) — 6 days ago

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

*Powered by GitHub Actions • Data refreshed daily • Last run: 2026-08-13 07:41 UTC*