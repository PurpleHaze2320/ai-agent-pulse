# 🔬 AI Agent Framework Pulse Tracker

[![Daily Update](https://github.com/PurpleHaze2320/ai-agent-pulse/actions/workflows/track.yml/badge.svg)](https://github.com/PurpleHaze2320/ai-agent-pulse/actions/workflows/track.yml)
[![Frameworks Tracked](https://img.shields.io/badge/frameworks-19-blue)](https://github.com/PurpleHaze2320/ai-agent-pulse)
[![License: MIT](https://img.shields.io/badge/License-MIT-green.svg)](https://opensource.org/licenses/MIT)
[![GitHub stars](https://img.shields.io/github/stars/PurpleHaze2320/ai-agent-pulse?style=social)](https://github.com/PurpleHaze2320/ai-agent-pulse/stargazers)

> Automated daily tracking of the AI agent framework ecosystem's health, momentum, and trends.
> Last updated: **2026-09-14 12:19 UTC** | Tracking **19** frameworks

## How It Works

This bot runs daily via GitHub Actions and collects metrics from the GitHub API for the most important
AI agent frameworks. It computes a **Pulse Score** (0-100) based on six weighted signals: star velocity,
release freshness, issue health, commit activity, community size, and fork engagement. The result is
a living dashboard that shows which frameworks are gaining momentum and which are losing steam.

## 🏆 Pulse Leaderboard

| Rank | Framework | Pulse | Stars | ⭐ 7d | Commits (4w) | Last Release | Category |
|------|-----------|-------|-------|-------|--------------|--------------|----------|
| 1 | [BrowserUse](https://github.com/browser-use/browser-use) | 🟢 **89.8** | 114.6k | 🚀 +1714 | 192 | 10 days ago | `web-agent` |
| 2 | [CrewAI](https://github.com/crewAIInc/crewAI) | 🟢 **81.4** | 58.5k | 🚀 +327 | 92 | 4 days ago | `multi-agent` |
| 3 | [Claude Agent SDK](https://github.com/anthropics/claude-code) | 🟢 **81.0** | 145.0k | 🚀 +648 | 78 | 1 day ago | `orchestration` |
| 4 | [Mastra](https://github.com/mastra-ai/mastra) | 🟢 **79.7** | 28.0k | 🚀 +266 | 1245 | 3 days ago | `typescript` |
| 5 | [OpenAI Agents SDK](https://github.com/openai/openai-agents-python) | 🟢 **77.6** | 29.4k | 🚀 +175 | 102 | 4 days ago | `orchestration` |
| 6 | [Google ADK](https://github.com/google/adk-python) | 🟢 **74.2** | 21.5k | 📈 +94 | 328 | 3 days ago | `orchestration` |
| 7 | [Haystack](https://github.com/deepset-ai/haystack) | 🟢 **71.2** | 26.5k | 📈 +71 | 176 | 11 days ago | `pipeline` |
| 8 | [Agno](https://github.com/agno-agi/agno) | 🟡 **69.8** | 42.2k | 📈 +80 | 99 | 5 days ago | `multi-agent` |
| 9 | [LangGraph](https://github.com/langchain-ai/langgraph) | 🟡 **69.7** | 41.6k | 🚀 +444 | 29 | 17 days ago | `orchestration` |
| 10 | [Composio](https://github.com/ComposioHQ/composio) | 🟡 **67.0** | 30.2k | 📈 +77 | 206 | today | `tooling` |
| 11 | [DSPy](https://github.com/stanfordnlp/dspy) | 🟡 **60.3** | 38.0k | 🚀 +186 | 36 | 2 days ago | `optimization` |
| 12 | [LlamaIndex](https://github.com/run-llama/llama_index) | 🟡 **59.8** | 52.2k | 🚀 +104 | 28 | 25 days ago | `data-agent` |
| 13 | [AG2](https://github.com/ag2ai/ag2) | 🟡 **57.8** | 4.9k | ↗️ +16 | 40 | 2 days ago | `multi-agent` |
| 14 | [PydanticAI](https://github.com/pydantic/pydantic-ai) | 🟡 **55.0** | 19.9k | 🚀 +164 | 0 | 2 days ago | `structured` |
| 15 | [Semantic Kernel](https://github.com/microsoft/semantic-kernel) | 🟡 **53.8** | 28.6k | ↗️ +17 | 20 | 10 days ago | `enterprise` |
| 16 | [Letta](https://github.com/letta-ai/letta) | 🟠 **39.5** | 24.7k | 📈 +92 | 3 | 4 mo ago | `memory` |
| 17 | [Smolagents](https://github.com/huggingface/smolagents) | 🟠 **36.2** | 29.3k | 🚀 +112 | 0 | 3 mo ago | `lightweight` |
| 18 | [AutoGen](https://github.com/microsoft/autogen) | 🟠 **33.6** | 61.0k | 🚀 +123 | 0 | 11 mo ago | `multi-agent` |
| 19 | [Swarm](https://github.com/openai/swarm) | 🔴 **9.8** | 22.0k | 📈 +32 | 0 | — | `experimental` |

## 📂 By Category

- `data-agent`: **LlamaIndex** (59.8)
- `enterprise`: **Semantic Kernel** (53.8)
- `experimental`: **Swarm** (9.8)
- `lightweight`: **Smolagents** (36.2)
- `memory`: **Letta** (39.5)
- `multi-agent`: **CrewAI** (81.4), **Agno** (69.8), **AG2** (57.8), **AutoGen** (33.6)
- `optimization`: **DSPy** (60.3)
- `orchestration`: **Claude Agent SDK** (81.0), **OpenAI Agents SDK** (77.6), **Google ADK** (74.2), **LangGraph** (69.7)
- `pipeline`: **Haystack** (71.2)
- `structured`: **PydanticAI** (55.0)
- `tooling`: **Composio** (67.0)
- `typescript`: **Mastra** (79.7)
- `web-agent`: **BrowserUse** (89.8)

## 🔍 Top 5 — Score Breakdown

| Framework | Star Velocity | Release Freshness | Issue Health | Commit Activity | Community | Fork Ratio |
|-----------|:---:|:---:|:---:|:---:|:---:|:---:|
| **BrowserUse** | 100 | 96.7 | 92.3 | 100 | 72.0 | 44.0 |
| **CrewAI** | 67.2 | 98.7 | 94.8 | 92.0 | 64.8 | 57.7 |
| **Claude Agent SDK** | 100 | 99.7 | 87.0 | 78.0 | 10.8 | 63.8 |
| **Mastra** | 49.5 | 99.0 | 94.7 | 100 | 93.0 | 39.7 |
| **OpenAI Agents SDK** | 36.1 | 98.7 | 98.8 | 100 | 75.6 | 64.3 |

## 💡 Key Insights

- **Hottest framework**: BrowserUse with a Pulse Score of 89.8
- **Fastest growing**: BrowserUse gained +1714 stars this week
- **Most active development**: Mastra with 1245 commits in the last 4 weeks
- **Stale releases**: AutoGen, Swarm haven't released in a while

## 📦 Recent Releases

- **Composio** [`@composio/cli@0.4.2-beta.387`](https://github.com/ComposioHQ/composio/releases/tag/@composio/cli@0.4.2-beta.387) — today *(pre-release)*
- **Claude Agent SDK** [`v2.1.270`](https://github.com/anthropics/claude-code/releases/tag/v2.1.270) — 1 day ago
- **PydanticAI** [`v2.43.0`](https://github.com/pydantic/pydantic-ai/releases/tag/v2.43.0) — 2 days ago
- **DSPy** [`3.4.0b1`](https://github.com/stanfordnlp/dspy/releases/tag/3.4.0b1) — 2 days ago *(pre-release)*
- **AG2** [`v1.0.5`](https://github.com/ag2ai/ag2/releases/tag/v1.0.5) — 2 days ago
- **Mastra** [`@mastra/core@1.66.0`](https://github.com/mastra-ai/mastra/releases/tag/@mastra/core@1.66.0) — 3 days ago
- **Google ADK** [`v2.9.0`](https://github.com/google/adk-python/releases/tag/v2.9.0) — 3 days ago
- **CrewAI** [`1.15.21`](https://github.com/crewAIInc/crewAI/releases/tag/1.15.21) — 4 days ago
- **OpenAI Agents SDK** [`v0.22.2`](https://github.com/openai/openai-agents-python/releases/tag/v0.22.2) — 4 days ago
- **Agno** [`v3.0.9`](https://github.com/agno-agi/agno/releases/tag/v3.0.9) — 5 days ago

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

*Powered by GitHub Actions • Data refreshed daily • Last run: 2026-09-14 12:19 UTC*