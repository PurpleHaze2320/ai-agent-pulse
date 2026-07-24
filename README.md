# 🔬 AI Agent Framework Pulse Tracker

[![Daily Update](https://github.com/PurpleHaze2320/ai-agent-pulse/actions/workflows/track.yml/badge.svg)](https://github.com/PurpleHaze2320/ai-agent-pulse/actions/workflows/track.yml)
[![Frameworks Tracked](https://img.shields.io/badge/frameworks-19-blue)](https://github.com/PurpleHaze2320/ai-agent-pulse)
[![License: MIT](https://img.shields.io/badge/License-MIT-green.svg)](https://opensource.org/licenses/MIT)
[![GitHub stars](https://img.shields.io/github/stars/PurpleHaze2320/ai-agent-pulse?style=social)](https://github.com/PurpleHaze2320/ai-agent-pulse/stargazers)

> Automated daily tracking of the AI agent framework ecosystem's health, momentum, and trends.
> Last updated: **2026-07-24 08:34 UTC** | Tracking **19** frameworks

## How It Works

This bot runs daily via GitHub Actions and collects metrics from the GitHub API for the most important
AI agent frameworks. It computes a **Pulse Score** (0-100) based on six weighted signals: star velocity,
release freshness, issue health, commit activity, community size, and fork engagement. The result is
a living dashboard that shows which frameworks are gaining momentum and which are losing steam.

## 🏆 Pulse Leaderboard

| Rank | Framework | Pulse | Stars | ⭐ 7d | Commits (4w) | Last Release | Category |
|------|-----------|-------|-------|-------|--------------|--------------|----------|
| 1 | [BrowserUse](https://github.com/browser-use/browser-use) | 🟢 **88.2** | 106.5k | 🚀 +1315 | 94 | 7 days ago | `web-agent` |
| 2 | [CrewAI](https://github.com/crewAIInc/crewAI) | 🟢 **79.8** | 56.1k | 🚀 +384 | 69 | 3 days ago | `multi-agent` |
| 3 | [Mastra](https://github.com/mastra-ai/mastra) | 🟢 **79.5** | 26.5k | 🚀 +246 | 1173 | 8 days ago | `typescript` |
| 4 | [Google ADK](https://github.com/google/adk-python) | 🟢 **77.9** | 20.9k | 🚀 +226 | 319 | 2 days ago | `orchestration` |
| 5 | [PydanticAI](https://github.com/pydantic/pydantic-ai) | 🟢 **76.7** | 18.8k | 🚀 +176 | 271 | today | `structured` |
| 6 | [Agno](https://github.com/agno-agi/agno) | 🟢 **75.7** | 41.4k | 🚀 +200 | 148 | today | `multi-agent` |
| 7 | [OpenAI Agents SDK](https://github.com/openai/openai-agents-python) | 🟢 **75.7** | 28.1k | 🚀 +178 | 133 | 7 days ago | `orchestration` |
| 8 | [LangGraph](https://github.com/langchain-ai/langgraph) | 🟢 **72.9** | 38.0k | 🚀 +516 | 29 | 14 days ago | `orchestration` |
| 9 | [Claude Agent SDK](https://github.com/anthropics/claude-code) | 🟢 **70.6** | 138.9k | 🚀 +865 | 28 | 1 day ago | `orchestration` |
| 10 | [Composio](https://github.com/ComposioHQ/composio) | 🟡 **66.6** | 29.3k | 📈 +89 | 131 | 3 days ago | `tooling` |
| 11 | [LlamaIndex](https://github.com/run-llama/llama_index) | 🟡 **63.6** | 51.1k | 🚀 +160 | 35 | 29 days ago | `data-agent` |
| 12 | [Haystack](https://github.com/deepset-ai/haystack) | 🟡 **50.8** | 26.0k | 📈 +74 | 0 | 3 days ago | `pipeline` |
| 13 | [Semantic Kernel](https://github.com/microsoft/semantic-kernel) | 🟡 **50.0** | 28.4k | 📈 +32 | 0 | 16 days ago | `enterprise` |
| 14 | [DSPy](https://github.com/stanfordnlp/dspy) | 🟡 **48.9** | 36.3k | 🚀 +150 | 0 | 1 mo ago | `optimization` |
| 15 | [AG2](https://github.com/ag2ai/ag2) | 🟡 **48.4** | 4.8k | ↗️ +8 | 0 | 20 days ago | `multi-agent` |
| 16 | [Letta](https://github.com/letta-ai/letta) | 🟡 **42.5** | 23.9k | 🚀 +108 | 0 | 2 mo ago | `memory` |
| 17 | [Smolagents](https://github.com/huggingface/smolagents) | 🟡 **41.0** | 28.5k | 🚀 +118 | 4 | 1 mo ago | `lightweight` |
| 18 | [AutoGen](https://github.com/microsoft/autogen) | 🟠 **35.2** | 59.9k | 🚀 +145 | 0 | 9 mo ago | `multi-agent` |
| 19 | [Swarm](https://github.com/openai/swarm) | 🔴 **10.9** | 21.9k | 📈 +54 | 0 | — | `experimental` |

## 📂 By Category

- `data-agent`: **LlamaIndex** (63.6)
- `enterprise`: **Semantic Kernel** (50.0)
- `experimental`: **Swarm** (10.9)
- `lightweight`: **Smolagents** (41.0)
- `memory`: **Letta** (42.5)
- `multi-agent`: **CrewAI** (79.8), **Agno** (75.7), **AG2** (48.4), **AutoGen** (35.2)
- `optimization`: **DSPy** (48.9)
- `orchestration`: **Google ADK** (77.9), **OpenAI Agents SDK** (75.7), **LangGraph** (72.9), **Claude Agent SDK** (70.6)
- `pipeline`: **Haystack** (50.8)
- `structured`: **PydanticAI** (76.7)
- `tooling`: **Composio** (66.6)
- `typescript`: **Mastra** (79.5)
- `web-agent`: **BrowserUse** (88.2)

## 🔍 Top 5 — Score Breakdown

| Framework | Star Velocity | Release Freshness | Issue Health | Commit Activity | Community | Fork Ratio |
|-----------|:---:|:---:|:---:|:---:|:---:|:---:|
| **BrowserUse** | 100 | 97.7 | 94.7 | 94.0 | 63.0 | 44.0 |
| **CrewAI** | 80.6 | 99.0 | 96.3 | 69.0 | 59.6 | 56.6 |
| **Mastra** | 51.1 | 97.3 | 94.3 | 100 | 93.0 | 37.8 |
| **Google ADK** | 40.5 | 99.3 | 87.6 | 100 | 75.8 | 71.9 |
| **PydanticAI** | 37.0 | 100.0 | 85.8 | 100 | 94.8 | 51.3 |

## 💡 Key Insights

- **Hottest framework**: BrowserUse with a Pulse Score of 88.2
- **Fastest growing**: BrowserUse gained +1315 stars this week
- **Most active development**: Mastra with 1173 commits in the last 4 weeks
- **Stale releases**: AutoGen, Swarm haven't released in a while

## 📦 Recent Releases

- **PydanticAI** [`v2.17.0`](https://github.com/pydantic/pydantic-ai/releases/tag/v2.17.0) — today
- **Agno** [`v2.8.1`](https://github.com/agno-agi/agno/releases/tag/v2.8.1) — today
- **Claude Agent SDK** [`v2.1.218`](https://github.com/anthropics/claude-code/releases/tag/v2.1.218) — 1 day ago
- **Google ADK** [`v1.36.2`](https://github.com/google/adk-python/releases/tag/v1.36.2) — 2 days ago
- **Composio** [`@composio/cli@0.2.33-beta.298`](https://github.com/ComposioHQ/composio/releases/tag/@composio/cli@0.2.33-beta.298) — 3 days ago *(pre-release)*
- **CrewAI** [`1.15.5`](https://github.com/crewAIInc/crewAI/releases/tag/1.15.5) — 3 days ago
- **Haystack** [`v3.0.0`](https://github.com/deepset-ai/haystack/releases/tag/v3.0.0) — 3 days ago
- **BrowserUse** [`0.13.6`](https://github.com/browser-use/browser-use/releases/tag/0.13.6) — 7 days ago
- **OpenAI Agents SDK** [`v0.18.3`](https://github.com/openai/openai-agents-python/releases/tag/v0.18.3) — 7 days ago
- **Mastra** [`@mastra/core@1.51.0`](https://github.com/mastra-ai/mastra/releases/tag/@mastra/core@1.51.0) — 8 days ago

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

*Powered by GitHub Actions • Data refreshed daily • Last run: 2026-07-24 08:34 UTC*