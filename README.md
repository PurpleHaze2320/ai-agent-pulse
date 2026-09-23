# 🔬 AI Agent Framework Pulse Tracker

[![Daily Update](https://github.com/PurpleHaze2320/ai-agent-pulse/actions/workflows/track.yml/badge.svg)](https://github.com/PurpleHaze2320/ai-agent-pulse/actions/workflows/track.yml)
[![Frameworks Tracked](https://img.shields.io/badge/frameworks-19-blue)](https://github.com/PurpleHaze2320/ai-agent-pulse)
[![License: MIT](https://img.shields.io/badge/License-MIT-green.svg)](https://opensource.org/licenses/MIT)
[![GitHub stars](https://img.shields.io/github/stars/PurpleHaze2320/ai-agent-pulse?style=social)](https://github.com/PurpleHaze2320/ai-agent-pulse/stargazers)

> Automated daily tracking of the AI agent framework ecosystem's health, momentum, and trends.
> Last updated: **2026-09-23 11:10 UTC** | Tracking **19** frameworks

## How It Works

This bot runs daily via GitHub Actions and collects metrics from the GitHub API for the most important
AI agent frameworks. It computes a **Pulse Score** (0-100) based on six weighted signals: star velocity,
release freshness, issue health, commit activity, community size, and fork engagement. The result is
a living dashboard that shows which frameworks are gaining momentum and which are losing steam.

## 🏆 Pulse Leaderboard

| Rank | Framework | Pulse | Stars | ⭐ 7d | Commits (4w) | Last Release | Category |
|------|-----------|-------|-------|-------|--------------|--------------|----------|
| 1 | [BrowserUse](https://github.com/browser-use/browser-use) | 🟢 **89.1** | 116.0k | 🚀 +1252 | 131 | 19 days ago | `web-agent` |
| 2 | [Claude Agent SDK](https://github.com/anthropics/claude-code) | 🟢 **85.8** | 147.7k | 🚀 +2485 | 112 | today | `orchestration` |
| 3 | [CrewAI](https://github.com/crewAIInc/crewAI) | 🟢 **81.3** | 58.9k | 🚀 +288 | 106 | 6 days ago | `multi-agent` |
| 4 | [Mastra](https://github.com/mastra-ai/mastra) | 🟢 **77.4** | 28.3k | 🚀 +186 | 1737 | today | `typescript` |
| 5 | [OpenAI Agents SDK](https://github.com/openai/openai-agents-python) | 🟢 **77.3** | 29.7k | 🚀 +166 | 140 | 5 days ago | `orchestration` |
| 6 | [PydanticAI](https://github.com/pydantic/pydantic-ai) | 🟢 **74.7** | 20.1k | 🚀 +151 | 243 | today | `structured` |
| 7 | [Google ADK](https://github.com/google/adk-python) | 🟢 **72.8** | 21.6k | 📈 +59 | 367 | 4 days ago | `orchestration` |
| 8 | [LangGraph](https://github.com/langchain-ai/langgraph) | 🟢 **71.4** | 42.2k | 🚀 +417 | 39 | 1 day ago | `orchestration` |
| 9 | [Agno](https://github.com/agno-agi/agno) | 🟢 **71.2** | 42.3k | 🚀 +119 | 118 | 6 days ago | `multi-agent` |
| 10 | [Composio](https://github.com/ComposioHQ/composio) | 🟡 **67.6** | 30.3k | 📈 +97 | 257 | today | `tooling` |
| 11 | [LlamaIndex](https://github.com/run-llama/llama_index) | 🟡 **60.9** | 52.3k | 🚀 +107 | 26 | 1 day ago | `data-agent` |
| 12 | [AG2](https://github.com/ag2ai/ag2) | 🟡 **59.4** | 5.0k | 📈 +23 | 46 | 1 day ago | `multi-agent` |
| 13 | [DSPy](https://github.com/stanfordnlp/dspy) | 🟡 **58.9** | 38.2k | 🚀 +160 | 39 | 11 days ago | `optimization` |
| 14 | [Semantic Kernel](https://github.com/microsoft/semantic-kernel) | 🟡 **52.0** | 28.6k | 📈 +30 | 12 | 19 days ago | `enterprise` |
| 15 | [Haystack](https://github.com/deepset-ai/haystack) | 🟡 **50.3** | 26.6k | 📈 +62 | 0 | 20 days ago | `pipeline` |
| 16 | [Letta](https://github.com/letta-ai/letta) | 🟠 **38.7** | 24.9k | 📈 +93 | 2 | 4 mo ago | `memory` |
| 17 | [Smolagents](https://github.com/huggingface/smolagents) | 🟠 **35.4** | 29.5k | 🚀 +110 | 0 | 3 mo ago | `lightweight` |
| 18 | [AutoGen](https://github.com/microsoft/autogen) | 🟠 **33.1** | 61.1k | 🚀 +112 | 0 | 11 mo ago | `multi-agent` |
| 19 | [Swarm](https://github.com/openai/swarm) | 🔴 **9.5** | 22.0k | 📈 +21 | 0 | — | `experimental` |

## 📂 By Category

- `data-agent`: **LlamaIndex** (60.9)
- `enterprise`: **Semantic Kernel** (52.0)
- `experimental`: **Swarm** (9.5)
- `lightweight`: **Smolagents** (35.4)
- `memory`: **Letta** (38.7)
- `multi-agent`: **CrewAI** (81.3), **Agno** (71.2), **AG2** (59.4), **AutoGen** (33.1)
- `optimization`: **DSPy** (58.9)
- `orchestration`: **Claude Agent SDK** (85.8), **OpenAI Agents SDK** (77.3), **Google ADK** (72.8), **LangGraph** (71.4)
- `pipeline`: **Haystack** (50.3)
- `structured`: **PydanticAI** (74.7)
- `tooling`: **Composio** (67.6)
- `typescript`: **Mastra** (77.4)
- `web-agent`: **BrowserUse** (89.1)

## 🔍 Top 5 — Score Breakdown

| Framework | Star Velocity | Release Freshness | Issue Health | Commit Activity | Community | Fork Ratio |
|-----------|:---:|:---:|:---:|:---:|:---:|:---:|
| **BrowserUse** | 100 | 93.7 | 91.3 | 100 | 72.2 | 44.0 |
| **Claude Agent SDK** | 100 | 100.0 | 87.6 | 100 | 11.0 | 65.4 |
| **CrewAI** | 61.3 | 98.0 | 92.5 | 100 | 67.0 | 58.1 |
| **Mastra** | 39.1 | 100.0 | 95.4 | 100 | 93.2 | 40.2 |
| **OpenAI Agents SDK** | 34.3 | 98.3 | 99.0 | 100 | 76.8 | 64.8 |

## 💡 Key Insights

- **Hottest framework**: BrowserUse with a Pulse Score of 89.1
- **Fastest growing**: Claude Agent SDK gained +2485 stars this week
- **Most active development**: Mastra with 1737 commits in the last 4 weeks
- **Stale releases**: AutoGen, Swarm haven't released in a while

## 📦 Recent Releases

- **Composio** [`versioning-example@0.1.4`](https://github.com/ComposioHQ/composio/releases/tag/versioning-example@0.1.4) — today
- **Mastra** [`@mastra/core@1.68.0`](https://github.com/mastra-ai/mastra/releases/tag/@mastra/core@1.68.0) — today
- **PydanticAI** [`v2.48.0`](https://github.com/pydantic/pydantic-ai/releases/tag/v2.48.0) — today
- **Claude Agent SDK** [`v2.1.280`](https://github.com/anthropics/claude-code/releases/tag/v2.1.280) — today
- **AG2** [`v1.0.6`](https://github.com/ag2ai/ag2/releases/tag/v1.0.6) — 1 day ago
- **LlamaIndex** [`v0.14.25`](https://github.com/run-llama/llama_index/releases/tag/v0.14.25) — 1 day ago
- **LangGraph** [`1.2.12`](https://github.com/langchain-ai/langgraph/releases/tag/1.2.12) — 1 day ago
- **Google ADK** [`v2.9.2`](https://github.com/google/adk-python/releases/tag/v2.9.2) — 4 days ago
- **OpenAI Agents SDK** [`v0.22.3`](https://github.com/openai/openai-agents-python/releases/tag/v0.22.3) — 5 days ago
- **CrewAI** [`1.15.22`](https://github.com/crewAIInc/crewAI/releases/tag/1.15.22) — 6 days ago

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

*Powered by GitHub Actions • Data refreshed daily • Last run: 2026-09-23 11:10 UTC*