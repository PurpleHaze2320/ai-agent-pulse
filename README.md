# 🔬 AI Agent Framework Pulse Tracker

[![Daily Update](https://github.com/PurpleHaze2320/ai-agent-pulse/actions/workflows/track.yml/badge.svg)](https://github.com/PurpleHaze2320/ai-agent-pulse/actions/workflows/track.yml)
[![Frameworks Tracked](https://img.shields.io/badge/frameworks-19-blue)](https://github.com/PurpleHaze2320/ai-agent-pulse)
[![License: MIT](https://img.shields.io/badge/License-MIT-green.svg)](https://opensource.org/licenses/MIT)
[![GitHub stars](https://img.shields.io/github/stars/PurpleHaze2320/ai-agent-pulse?style=social)](https://github.com/PurpleHaze2320/ai-agent-pulse/stargazers)

> Automated daily tracking of the AI agent framework ecosystem's health, momentum, and trends.
> Last updated: **2026-09-17 11:21 UTC** | Tracking **19** frameworks

## How It Works

This bot runs daily via GitHub Actions and collects metrics from the GitHub API for the most important
AI agent frameworks. It computes a **Pulse Score** (0-100) based on six weighted signals: star velocity,
release freshness, issue health, commit activity, community size, and fork engagement. The result is
a living dashboard that shows which frameworks are gaining momentum and which are losing steam.

## 🏆 Pulse Leaderboard

| Rank | Framework | Pulse | Stars | ⭐ 7d | Commits (4w) | Last Release | Category |
|------|-----------|-------|-------|-------|--------------|--------------|----------|
| 1 | [BrowserUse](https://github.com/browser-use/browser-use) | 🟢 **89.5** | 114.9k | 🚀 +873 | 204 | 13 days ago | `web-agent` |
| 2 | [Claude Agent SDK](https://github.com/anthropics/claude-code) | 🟢 **85.6** | 145.8k | 🚀 +1137 | 106 | today | `orchestration` |
| 3 | [CrewAI](https://github.com/crewAIInc/crewAI) | 🟢 **84.9** | 58.7k | 🚀 +368 | 117 | today | `multi-agent` |
| 4 | [Mastra](https://github.com/mastra-ai/mastra) | 🟢 **78.8** | 28.1k | 🚀 +226 | 1627 | 1 day ago | `typescript` |
| 5 | [OpenAI Agents SDK](https://github.com/openai/openai-agents-python) | 🟢 **78.0** | 29.5k | 🚀 +193 | 114 | 7 days ago | `orchestration` |
| 6 | [PydanticAI](https://github.com/pydantic/pydantic-ai) | 🟢 **75.0** | 20.0k | 🚀 +161 | 242 | today | `structured` |
| 7 | [Google ADK](https://github.com/google/adk-python) | 🟢 **73.9** | 21.6k | 📈 +82 | 387 | 1 day ago | `orchestration` |
| 8 | [Haystack](https://github.com/deepset-ai/haystack) | 🟢 **70.6** | 26.5k | 📈 +61 | 193 | 14 days ago | `pipeline` |
| 9 | [Agno](https://github.com/agno-agi/agno) | 🟢 **70.4** | 42.2k | 📈 +83 | 121 | today | `multi-agent` |
| 10 | [LangGraph](https://github.com/langchain-ai/langgraph) | 🟡 **69.2** | 41.8k | 🚀 +432 | 30 | 20 days ago | `orchestration` |
| 11 | [Composio](https://github.com/ComposioHQ/composio) | 🟡 **67.7** | 30.2k | 📈 +96 | 298 | today | `tooling` |
| 12 | [DSPy](https://github.com/stanfordnlp/dspy) | 🟡 **63.8** | 38.1k | 🚀 +192 | 55 | 5 days ago | `optimization` |
| 13 | [LlamaIndex](https://github.com/run-llama/llama_index) | 🟡 **59.4** | 52.2k | 📈 +84 | 31 | 28 days ago | `data-agent` |
| 14 | [AG2](https://github.com/ag2ai/ag2) | 🟡 **58.6** | 4.9k | ↗️ +20 | 44 | 5 days ago | `multi-agent` |
| 15 | [Semantic Kernel](https://github.com/microsoft/semantic-kernel) | 🟡 **53.5** | 28.6k | ↗️ +16 | 20 | 13 days ago | `enterprise` |
| 16 | [Letta](https://github.com/letta-ai/letta) | 🟠 **39.0** | 24.8k | 📈 +83 | 3 | 4 mo ago | `memory` |
| 17 | [Smolagents](https://github.com/huggingface/smolagents) | 🟠 **35.2** | 29.4k | 📈 +90 | 0 | 3 mo ago | `lightweight` |
| 18 | [AutoGen](https://github.com/microsoft/autogen) | 🟠 **32.7** | 61.0k | 📈 +99 | 0 | 11 mo ago | `multi-agent` |
| 19 | [Swarm](https://github.com/openai/swarm) | 🔴 **9.6** | 22.0k | 📈 +23 | 0 | — | `experimental` |

## 📂 By Category

- `data-agent`: **LlamaIndex** (59.4)
- `enterprise`: **Semantic Kernel** (53.5)
- `experimental`: **Swarm** (9.6)
- `lightweight`: **Smolagents** (35.2)
- `memory`: **Letta** (39.0)
- `multi-agent`: **CrewAI** (84.9), **Agno** (70.4), **AG2** (58.6), **AutoGen** (32.7)
- `optimization`: **DSPy** (63.8)
- `orchestration`: **Claude Agent SDK** (85.6), **OpenAI Agents SDK** (78.0), **Google ADK** (73.9), **LangGraph** (69.2)
- `pipeline`: **Haystack** (70.6)
- `structured`: **PydanticAI** (75.0)
- `tooling`: **Composio** (67.7)
- `typescript`: **Mastra** (78.8)
- `web-agent`: **BrowserUse** (89.5)

## 🔍 Top 5 — Score Breakdown

| Framework | Star Velocity | Release Freshness | Issue Health | Commit Activity | Community | Fork Ratio |
|-----------|:---:|:---:|:---:|:---:|:---:|:---:|
| **BrowserUse** | 100 | 95.7 | 91.9 | 100 | 72.2 | 44.0 |
| **Claude Agent SDK** | 100 | 100.0 | 87.3 | 100 | 10.8 | 64.5 |
| **CrewAI** | 73.4 | 100.0 | 94.2 | 100 | 66.6 | 57.9 |
| **Mastra** | 44.6 | 99.7 | 95.7 | 100 | 93.2 | 39.9 |
| **OpenAI Agents SDK** | 38.8 | 97.7 | 98.5 | 100 | 75.6 | 64.5 |

## 💡 Key Insights

- **Hottest framework**: BrowserUse with a Pulse Score of 89.5
- **Fastest growing**: Claude Agent SDK gained +1137 stars this week
- **Most active development**: Mastra with 1627 commits in the last 4 weeks
- **Stale releases**: AutoGen, Swarm haven't released in a while

## 📦 Recent Releases

- **PydanticAI** [`v2.44.0`](https://github.com/pydantic/pydantic-ai/releases/tag/v2.44.0) — today
- **Claude Agent SDK** [`v2.1.274`](https://github.com/anthropics/claude-code/releases/tag/v2.1.274) — today
- **CrewAI** [`1.15.22`](https://github.com/crewAIInc/crewAI/releases/tag/1.15.22) — today
- **Composio** [`@composio/cli@0.4.2-beta.397`](https://github.com/ComposioHQ/composio/releases/tag/@composio/cli@0.4.2-beta.397) — today *(pre-release)*
- **Agno** [`v3.0.10`](https://github.com/agno-agi/agno/releases/tag/v3.0.10) — today
- **Google ADK** [`v2.9.1`](https://github.com/google/adk-python/releases/tag/v2.9.1) — 1 day ago
- **Mastra** [`@mastra/core@1.67.0`](https://github.com/mastra-ai/mastra/releases/tag/@mastra/core@1.67.0) — 1 day ago
- **DSPy** [`3.4.0b1`](https://github.com/stanfordnlp/dspy/releases/tag/3.4.0b1) — 5 days ago *(pre-release)*
- **AG2** [`v1.0.5`](https://github.com/ag2ai/ag2/releases/tag/v1.0.5) — 5 days ago
- **OpenAI Agents SDK** [`v0.22.2`](https://github.com/openai/openai-agents-python/releases/tag/v0.22.2) — 7 days ago

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

*Powered by GitHub Actions • Data refreshed daily • Last run: 2026-09-17 11:21 UTC*