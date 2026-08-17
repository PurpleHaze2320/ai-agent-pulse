# 🔬 AI Agent Framework Pulse Tracker

[![Daily Update](https://github.com/PurpleHaze2320/ai-agent-pulse/actions/workflows/track.yml/badge.svg)](https://github.com/PurpleHaze2320/ai-agent-pulse/actions/workflows/track.yml)
[![Frameworks Tracked](https://img.shields.io/badge/frameworks-19-blue)](https://github.com/PurpleHaze2320/ai-agent-pulse)
[![License: MIT](https://img.shields.io/badge/License-MIT-green.svg)](https://opensource.org/licenses/MIT)
[![GitHub stars](https://img.shields.io/github/stars/PurpleHaze2320/ai-agent-pulse?style=social)](https://github.com/PurpleHaze2320/ai-agent-pulse/stargazers)

> Automated daily tracking of the AI agent framework ecosystem's health, momentum, and trends.
> Last updated: **2026-08-17 07:04 UTC** | Tracking **19** frameworks

## How It Works

This bot runs daily via GitHub Actions and collects metrics from the GitHub API for the most important
AI agent frameworks. It computes a **Pulse Score** (0-100) based on six weighted signals: star velocity,
release freshness, issue health, commit activity, community size, and fork engagement. The result is
a living dashboard that shows which frameworks are gaining momentum and which are losing steam.

## 🏆 Pulse Leaderboard

| Rank | Framework | Pulse | Stars | ⭐ 7d | Commits (4w) | Last Release | Category |
|------|-----------|-------|-------|-------|--------------|--------------|----------|
| 1 | [BrowserUse](https://github.com/browser-use/browser-use) | 🟢 **90.1** | 109.5k | 🚀 +932 | 111 | today | `web-agent` |
| 2 | [Mastra](https://github.com/mastra-ai/mastra) | 🟢 **76.8** | 27.2k | 🚀 +166 | 1294 | today | `typescript` |
| 3 | [Haystack](https://github.com/deepset-ai/haystack) | 🟡 **69.1** | 26.2k | 📈 +64 | 145 | 27 days ago | `pipeline` |
| 4 | [Composio](https://github.com/ComposioHQ/composio) | 🟡 **68.2** | 29.7k | 🚀 +116 | 275 | today | `tooling` |
| 5 | [LangGraph](https://github.com/langchain-ai/langgraph) | 🟡 **67.4** | 39.8k | 🚀 +487 | 0 | 5 days ago | `orchestration` |
| 6 | [Claude Agent SDK](https://github.com/anthropics/claude-code) | 🟡 **64.8** | 141.7k | 🚀 +827 | 0 | 2 days ago | `orchestration` |
| 7 | [CrewAI](https://github.com/crewAIInc/crewAI) | 🟡 **61.8** | 57.2k | 🚀 +302 | 0 | 3 days ago | `multi-agent` |
| 8 | [LlamaIndex](https://github.com/run-llama/llama_index) | 🟡 **59.9** | 51.7k | 🚀 +168 | 22 | 1 mo ago | `data-agent` |
| 9 | [DSPy](https://github.com/stanfordnlp/dspy) | 🟡 **59.5** | 37.3k | 🚀 +354 | 0 | 13 days ago | `optimization` |
| 10 | [OpenAI Agents SDK](https://github.com/openai/openai-agents-python) | 🟡 **57.1** | 28.7k | 🚀 +178 | 0 | today | `orchestration` |
| 11 | [PydanticAI](https://github.com/pydantic/pydantic-ai) | 🟡 **55.3** | 19.3k | 🚀 +160 | 0 | 2 days ago | `structured` |
| 12 | [Google ADK](https://github.com/google/adk-python) | 🟡 **54.0** | 21.2k | 📈 +92 | 0 | 3 days ago | `orchestration` |
| 13 | [Agno](https://github.com/agno-agi/agno) | 🟡 **51.1** | 41.7k | 📈 +96 | 0 | 3 days ago | `multi-agent` |
| 14 | [AG2](https://github.com/ag2ai/ag2) | 🟡 **50.0** | 4.9k | ↗️ +19 | 0 | 2 days ago | `multi-agent` |
| 15 | [Semantic Kernel](https://github.com/microsoft/semantic-kernel) | 🟡 **49.9** | 28.5k | 📈 +21 | 0 | 10 days ago | `enterprise` |
| 16 | [Letta](https://github.com/letta-ai/letta) | 🟡 **41.0** | 24.3k | 🚀 +109 | 0 | 3 mo ago | `memory` |
| 17 | [Smolagents](https://github.com/huggingface/smolagents) | 🟠 **37.4** | 28.8k | 📈 +94 | 0 | 2 mo ago | `lightweight` |
| 18 | [AutoGen](https://github.com/microsoft/autogen) | 🟠 **33.7** | 60.5k | 🚀 +117 | 0 | 10 mo ago | `multi-agent` |
| 19 | [Swarm](https://github.com/openai/swarm) | 🔴 **9.5** | 21.9k | ↗️ +15 | 0 | — | `experimental` |

## 📂 By Category

- `data-agent`: **LlamaIndex** (59.9)
- `enterprise`: **Semantic Kernel** (49.9)
- `experimental`: **Swarm** (9.5)
- `lightweight`: **Smolagents** (37.4)
- `memory`: **Letta** (41.0)
- `multi-agent`: **CrewAI** (61.8), **Agno** (51.1), **AG2** (50.0), **AutoGen** (33.7)
- `optimization`: **DSPy** (59.5)
- `orchestration`: **LangGraph** (67.4), **Claude Agent SDK** (64.8), **OpenAI Agents SDK** (57.1), **Google ADK** (54.0)
- `pipeline`: **Haystack** (69.1)
- `structured`: **PydanticAI** (55.3)
- `tooling`: **Composio** (68.2)
- `typescript`: **Mastra** (76.8)
- `web-agent`: **BrowserUse** (90.1)

## 🔍 Top 5 — Score Breakdown

| Framework | Star Velocity | Release Freshness | Issue Health | Commit Activity | Community | Fork Ratio |
|-----------|:---:|:---:|:---:|:---:|:---:|:---:|
| **BrowserUse** | 100 | 100.0 | 93.8 | 100 | 66.8 | 44.0 |
| **Mastra** | 37.2 | 100.0 | 95.8 | 100 | 92.8 | 38.8 |
| **Haystack** | 13.4 | 91.0 | 98.4 | 100 | 82.0 | 46.0 |
| **Composio** | 23.1 | 100.0 | 95.9 | 100 | 17.0 | 63.4 |
| **LangGraph** | 100 | 98.3 | 69.9 | 0.0 | 55.4 | 67.2 |

## 💡 Key Insights

- **Hottest framework**: BrowserUse with a Pulse Score of 90.1
- **Fastest growing**: BrowserUse gained +932 stars this week
- **Most active development**: Mastra with 1294 commits in the last 4 weeks
- **Stale releases**: AutoGen, Swarm haven't released in a while

## 📦 Recent Releases

- **OpenAI Agents SDK** [`v0.21.1`](https://github.com/openai/openai-agents-python/releases/tag/v0.21.1) — today
- **BrowserUse** [`0.13.8`](https://github.com/browser-use/browser-use/releases/tag/0.13.8) — today
- **Composio** [`@composio/cli@0.3.4-beta.352`](https://github.com/ComposioHQ/composio/releases/tag/@composio/cli@0.3.4-beta.352) — today *(pre-release)*
- **Mastra** [`@mastra/core@1.59.0`](https://github.com/mastra-ai/mastra/releases/tag/@mastra/core@1.59.0) — today
- **AG2** [`v1.0.2`](https://github.com/ag2ai/ag2/releases/tag/v1.0.2) — 2 days ago
- **PydanticAI** [`v2.31.0`](https://github.com/pydantic/pydantic-ai/releases/tag/v2.31.0) — 2 days ago
- **Claude Agent SDK** [`v2.1.233`](https://github.com/anthropics/claude-code/releases/tag/v2.1.233) — 2 days ago
- **CrewAI** [`1.15.16`](https://github.com/crewAIInc/crewAI/releases/tag/1.15.16) — 3 days ago
- **Google ADK** [`v2.7.0`](https://github.com/google/adk-python/releases/tag/v2.7.0) — 3 days ago
- **Agno** [`v2.9.0`](https://github.com/agno-agi/agno/releases/tag/v2.9.0) — 3 days ago

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

*Powered by GitHub Actions • Data refreshed daily • Last run: 2026-08-17 07:04 UTC*