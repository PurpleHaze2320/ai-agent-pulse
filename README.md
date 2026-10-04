# 🔬 AI Agent Framework Pulse Tracker

[![Daily Update](https://github.com/PurpleHaze2320/ai-agent-pulse/actions/workflows/track.yml/badge.svg)](https://github.com/PurpleHaze2320/ai-agent-pulse/actions/workflows/track.yml)
[![Frameworks Tracked](https://img.shields.io/badge/frameworks-19-blue)](https://github.com/PurpleHaze2320/ai-agent-pulse)
[![License: MIT](https://img.shields.io/badge/License-MIT-green.svg)](https://opensource.org/licenses/MIT)
[![GitHub stars](https://img.shields.io/github/stars/PurpleHaze2320/ai-agent-pulse?style=social)](https://github.com/PurpleHaze2320/ai-agent-pulse/stargazers)

> Automated daily tracking of the AI agent framework ecosystem's health, momentum, and trends.
> Last updated: **2026-10-04 12:04 UTC** | Tracking **19** frameworks

## How It Works

This bot runs daily via GitHub Actions and collects metrics from the GitHub API for the most important
AI agent frameworks. It computes a **Pulse Score** (0-100) based on six weighted signals: star velocity,
release freshness, issue health, commit activity, community size, and fork engagement. The result is
a living dashboard that shows which frameworks are gaining momentum and which are losing steam.

## 🏆 Pulse Leaderboard

| Rank | Framework | Pulse | Stars | ⭐ 7d | Commits (4w) | Last Release | Category |
|------|-----------|-------|-------|-------|--------------|--------------|----------|
| 1 | [Claude Agent SDK](https://github.com/anthropics/claude-code) | 🟢 **80.7** | 149.4k | 🚀 +1074 | 74 | today | `orchestration` |
| 2 | [BrowserUse](https://github.com/browser-use/browser-use) | 🟢 **77.3** | 117.1k | 🚀 +641 | 46 | 1 mo ago | `web-agent` |
| 3 | [Mastra](https://github.com/mastra-ai/mastra) | 🟢 **77.2** | 28.5k | 🚀 +185 | 1744 | 4 days ago | `typescript` |
| 4 | [OpenAI Agents SDK](https://github.com/openai/openai-agents-python) | 🟢 **75.6** | 29.8k | 🚀 +112 | 207 | 1 day ago | `orchestration` |
| 5 | [PydanticAI](https://github.com/pydantic/pydantic-ai) | 🟢 **75.2** | 20.4k | 🚀 +186 | 651 | 1 day ago | `structured` |
| 6 | [Google ADK](https://github.com/google/adk-python) | 🟢 **72.4** | 21.7k | 📈 +45 | 358 | 2 days ago | `orchestration` |
| 7 | [CrewAI](https://github.com/crewAIInc/crewAI) | 🟢 **72.2** | 59.3k | 🚀 +246 | 65 | 5 days ago | `multi-agent` |
| 8 | [Agno](https://github.com/agno-agi/agno) | 🟢 **70.9** | 42.5k | 🚀 +190 | 85 | 1 day ago | `multi-agent` |
| 9 | [Haystack](https://github.com/deepset-ai/haystack) | 🟢 **70.3** | 26.6k | 📈 +33 | 187 | 3 days ago | `pipeline` |
| 10 | [LangGraph](https://github.com/langchain-ai/langgraph) | 🟢 **70.1** | 42.7k | 🚀 +350 | 51 | 10 days ago | `orchestration` |
| 11 | [Composio](https://github.com/ComposioHQ/composio) | 🟡 **67.5** | 30.4k | 📈 +97 | 264 | 2 days ago | `tooling` |
| 12 | [AG2](https://github.com/ag2ai/ag2) | 🟡 **66.1** | 5.0k | ↗️ +11 | 82 | 1 day ago | `multi-agent` |
| 13 | [DSPy](https://github.com/stanfordnlp/dspy) | 🟡 **60.0** | 38.5k | 🚀 +127 | 49 | 9 days ago | `optimization` |
| 14 | [LlamaIndex](https://github.com/run-llama/llama_index) | 🟡 **58.0** | 52.4k | 📈 +74 | 22 | 12 days ago | `data-agent` |
| 15 | [Semantic Kernel](https://github.com/microsoft/semantic-kernel) | 🟡 **49.9** | 28.6k | ↗️ +16 | 8 | 1 mo ago | `enterprise` |
| 16 | [Letta](https://github.com/letta-ai/letta) | 🟠 **38.4** | 25.0k | 🚀 +123 | 0 | 4 mo ago | `memory` |
| 17 | [Smolagents](https://github.com/huggingface/smolagents) | 🟠 **36.8** | 29.7k | 🚀 +152 | 4 | 4 mo ago | `lightweight` |
| 18 | [AutoGen](https://github.com/microsoft/autogen) | 🟠 **31.2** | 61.3k | 📈 +66 | 0 | 1y ago | `multi-agent` |
| 19 | [Swarm](https://github.com/openai/swarm) | 🔴 **9.6** | 22.0k | 📈 +22 | 0 | — | `experimental` |

## 📂 By Category

- `data-agent`: **LlamaIndex** (58.0)
- `enterprise`: **Semantic Kernel** (49.9)
- `experimental`: **Swarm** (9.6)
- `lightweight`: **Smolagents** (36.8)
- `memory`: **Letta** (38.4)
- `multi-agent`: **CrewAI** (72.2), **Agno** (70.9), **AG2** (66.1), **AutoGen** (31.2)
- `optimization`: **DSPy** (60.0)
- `orchestration`: **Claude Agent SDK** (80.7), **OpenAI Agents SDK** (75.6), **Google ADK** (72.4), **LangGraph** (70.1)
- `pipeline`: **Haystack** (70.3)
- `structured`: **PydanticAI** (75.2)
- `tooling`: **Composio** (67.5)
- `typescript`: **Mastra** (77.2)
- `web-agent`: **BrowserUse** (77.3)

## 🔍 Top 5 — Score Breakdown

| Framework | Star Velocity | Release Freshness | Issue Health | Commit Activity | Community | Fork Ratio |
|-----------|:---:|:---:|:---:|:---:|:---:|:---:|
| **Claude Agent SDK** | 100 | 100.0 | 86.1 | 74.0 | 11.4 | 68.2 |
| **BrowserUse** | 100 | 90.0 | 90.1 | 46.0 | 72.0 | 44.1 |
| **Mastra** | 38.7 | 98.7 | 95.3 | 100 | 93.6 | 40.8 |
| **OpenAI Agents SDK** | 25.2 | 99.7 | 99.7 | 100 | 79.4 | 64.9 |
| **PydanticAI** | 36.2 | 99.7 | 74.4 | 100 | 95.0 | 56.0 |

## 💡 Key Insights

- **Hottest framework**: Claude Agent SDK with a Pulse Score of 80.7
- **Fastest growing**: Claude Agent SDK gained +1074 stars this week
- **Most active development**: Mastra with 1744 commits in the last 4 weeks
- **Stale releases**: AutoGen, Swarm haven't released in a while

## 📦 Recent Releases

- **Claude Agent SDK** [`v2.1.289`](https://github.com/anthropics/claude-code/releases/tag/v2.1.289) — today
- **AG2** [`v1.1.2`](https://github.com/ag2ai/ag2/releases/tag/v1.1.2) — 1 day ago
- **PydanticAI** [`v2.54.0`](https://github.com/pydantic/pydantic-ai/releases/tag/v2.54.0) — 1 day ago
- **OpenAI Agents SDK** [`v0.23.1`](https://github.com/openai/openai-agents-python/releases/tag/v0.23.1) — 1 day ago
- **Agno** [`v3.1.1`](https://github.com/agno-agi/agno/releases/tag/v3.1.1) — 1 day ago
- **Google ADK** [`v2.11.0`](https://github.com/google/adk-python/releases/tag/v2.11.0) — 2 days ago
- **Composio** [`@composio/cli@0.4.3-beta.411`](https://github.com/ComposioHQ/composio/releases/tag/@composio/cli@0.4.3-beta.411) — 2 days ago *(pre-release)*
- **Haystack** [`v3.3.0`](https://github.com/deepset-ai/haystack/releases/tag/v3.3.0) — 3 days ago
- **Mastra** [`@mastra/core@1.72.0`](https://github.com/mastra-ai/mastra/releases/tag/@mastra/core@1.72.0) — 4 days ago
- **CrewAI** [`1.15.23`](https://github.com/crewAIInc/crewAI/releases/tag/1.15.23) — 5 days ago

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

*Powered by GitHub Actions • Data refreshed daily • Last run: 2026-10-04 12:04 UTC*