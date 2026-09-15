# 🔬 AI Agent Framework Pulse Tracker

[![Daily Update](https://github.com/PurpleHaze2320/ai-agent-pulse/actions/workflows/track.yml/badge.svg)](https://github.com/PurpleHaze2320/ai-agent-pulse/actions/workflows/track.yml)
[![Frameworks Tracked](https://img.shields.io/badge/frameworks-19-blue)](https://github.com/PurpleHaze2320/ai-agent-pulse)
[![License: MIT](https://img.shields.io/badge/License-MIT-green.svg)](https://opensource.org/licenses/MIT)
[![GitHub stars](https://img.shields.io/github/stars/PurpleHaze2320/ai-agent-pulse?style=social)](https://github.com/PurpleHaze2320/ai-agent-pulse/stargazers)

> Automated daily tracking of the AI agent framework ecosystem's health, momentum, and trends.
> Last updated: **2026-09-15 11:26 UTC** | Tracking **19** frameworks

## How It Works

This bot runs daily via GitHub Actions and collects metrics from the GitHub API for the most important
AI agent frameworks. It computes a **Pulse Score** (0-100) based on six weighted signals: star velocity,
release freshness, issue health, commit activity, community size, and fork engagement. The result is
a living dashboard that shows which frameworks are gaining momentum and which are losing steam.

## 🏆 Pulse Leaderboard

| Rank | Framework | Pulse | Stars | ⭐ 7d | Commits (4w) | Last Release | Category |
|------|-----------|-------|-------|-------|--------------|--------------|----------|
| 1 | [BrowserUse](https://github.com/browser-use/browser-use) | 🟢 **89.7** | 114.7k | 🚀 +1659 | 192 | 11 days ago | `web-agent` |
| 2 | [Claude Agent SDK](https://github.com/anthropics/claude-code) | 🟢 **85.6** | 145.1k | 🚀 +705 | 101 | today | `orchestration` |
| 3 | [CrewAI](https://github.com/crewAIInc/crewAI) | 🟢 **82.9** | 58.6k | 🚀 +353 | 95 | 5 days ago | `multi-agent` |
| 4 | [Mastra](https://github.com/mastra-ai/mastra) | 🟢 **79.5** | 28.1k | 🚀 +262 | 1357 | 4 days ago | `typescript` |
| 5 | [OpenAI Agents SDK](https://github.com/openai/openai-agents-python) | 🟢 **77.9** | 29.5k | 🚀 +185 | 102 | 5 days ago | `orchestration` |
| 6 | [Agno](https://github.com/agno-agi/agno) | 🟢 **70.1** | 42.2k | 📈 +85 | 103 | 6 days ago | `multi-agent` |
| 7 | [LangGraph](https://github.com/langchain-ai/langgraph) | 🟡 **69.6** | 41.7k | 🚀 +437 | 30 | 18 days ago | `orchestration` |
| 8 | [Composio](https://github.com/ComposioHQ/composio) | 🟡 **67.5** | 30.2k | 📈 +90 | 242 | today | `tooling` |
| 9 | [DSPy](https://github.com/stanfordnlp/dspy) | 🟡 **61.9** | 38.0k | 🚀 +186 | 45 | 3 days ago | `optimization` |
| 10 | [LlamaIndex](https://github.com/run-llama/llama_index) | 🟡 **59.8** | 52.2k | 📈 +95 | 30 | 26 days ago | `data-agent` |
| 11 | [AG2](https://github.com/ag2ai/ag2) | 🟡 **58.1** | 4.9k | ↗️ +13 | 42 | 3 days ago | `multi-agent` |
| 12 | [PydanticAI](https://github.com/pydantic/pydantic-ai) | 🟡 **54.9** | 19.9k | 🚀 +162 | 0 | 3 days ago | `structured` |
| 13 | [Google ADK](https://github.com/google/adk-python) | 🟡 **54.0** | 21.5k | 📈 +89 | 0 | 4 days ago | `orchestration` |
| 14 | [Semantic Kernel](https://github.com/microsoft/semantic-kernel) | 🟡 **53.6** | 28.6k | ↗️ +15 | 20 | 11 days ago | `enterprise` |
| 15 | [Haystack](https://github.com/deepset-ai/haystack) | 🟡 **50.8** | 26.5k | 📈 +63 | 0 | 12 days ago | `pipeline` |
| 16 | [Letta](https://github.com/letta-ai/letta) | 🟠 **39.4** | 24.7k | 📈 +91 | 3 | 4 mo ago | `memory` |
| 17 | [Smolagents](https://github.com/huggingface/smolagents) | 🟠 **35.8** | 29.3k | 🚀 +102 | 0 | 3 mo ago | `lightweight` |
| 18 | [AutoGen](https://github.com/microsoft/autogen) | 🟠 **33.6** | 61.0k | 🚀 +122 | 0 | 11 mo ago | `multi-agent` |
| 19 | [Swarm](https://github.com/openai/swarm) | 🔴 **9.9** | 22.0k | 📈 +33 | 0 | — | `experimental` |

## 📂 By Category

- `data-agent`: **LlamaIndex** (59.8)
- `enterprise`: **Semantic Kernel** (53.6)
- `experimental`: **Swarm** (9.9)
- `lightweight`: **Smolagents** (35.8)
- `memory`: **Letta** (39.4)
- `multi-agent`: **CrewAI** (82.9), **Agno** (70.1), **AG2** (58.1), **AutoGen** (33.6)
- `optimization`: **DSPy** (61.9)
- `orchestration`: **Claude Agent SDK** (85.6), **OpenAI Agents SDK** (77.9), **LangGraph** (69.6), **Google ADK** (54.0)
- `pipeline`: **Haystack** (50.8)
- `structured`: **PydanticAI** (54.9)
- `tooling`: **Composio** (67.5)
- `typescript`: **Mastra** (79.5)
- `web-agent`: **BrowserUse** (89.7)

## 🔍 Top 5 — Score Breakdown

| Framework | Star Velocity | Release Freshness | Issue Health | Commit Activity | Community | Fork Ratio |
|-----------|:---:|:---:|:---:|:---:|:---:|:---:|
| **BrowserUse** | 100 | 96.3 | 92.1 | 100 | 72.0 | 44.0 |
| **Claude Agent SDK** | 100 | 100.0 | 87.3 | 100 | 10.8 | 63.8 |
| **CrewAI** | 71.1 | 98.3 | 94.6 | 95.0 | 65.0 | 57.7 |
| **Mastra** | 49.2 | 98.7 | 94.9 | 100 | 92.8 | 39.7 |
| **OpenAI Agents SDK** | 37.7 | 98.3 | 98.5 | 100 | 75.6 | 64.3 |

## 💡 Key Insights

- **Hottest framework**: BrowserUse with a Pulse Score of 89.7
- **Fastest growing**: BrowserUse gained +1659 stars this week
- **Most active development**: Mastra with 1357 commits in the last 4 weeks
- **Stale releases**: AutoGen, Swarm haven't released in a while

## 📦 Recent Releases

- **Claude Agent SDK** [`v2.1.272`](https://github.com/anthropics/claude-code/releases/tag/v2.1.272) — today
- **Composio** [`@composio/cli@0.4.2-beta.393`](https://github.com/ComposioHQ/composio/releases/tag/@composio/cli@0.4.2-beta.393) — today *(pre-release)*
- **PydanticAI** [`v2.43.0`](https://github.com/pydantic/pydantic-ai/releases/tag/v2.43.0) — 3 days ago
- **DSPy** [`3.4.0b1`](https://github.com/stanfordnlp/dspy/releases/tag/3.4.0b1) — 3 days ago *(pre-release)*
- **AG2** [`v1.0.5`](https://github.com/ag2ai/ag2/releases/tag/v1.0.5) — 3 days ago
- **Mastra** [`@mastra/core@1.66.0`](https://github.com/mastra-ai/mastra/releases/tag/@mastra/core@1.66.0) — 4 days ago
- **Google ADK** [`v2.9.0`](https://github.com/google/adk-python/releases/tag/v2.9.0) — 4 days ago
- **CrewAI** [`1.15.21`](https://github.com/crewAIInc/crewAI/releases/tag/1.15.21) — 5 days ago
- **OpenAI Agents SDK** [`v0.22.2`](https://github.com/openai/openai-agents-python/releases/tag/v0.22.2) — 5 days ago
- **Agno** [`v3.0.9`](https://github.com/agno-agi/agno/releases/tag/v3.0.9) — 6 days ago

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

*Powered by GitHub Actions • Data refreshed daily • Last run: 2026-09-15 11:26 UTC*