# 🔬 AI Agent Framework Pulse Tracker

[![Daily Update](https://github.com/PurpleHaze2320/ai-agent-pulse/actions/workflows/track.yml/badge.svg)](https://github.com/PurpleHaze2320/ai-agent-pulse/actions/workflows/track.yml)
[![Frameworks Tracked](https://img.shields.io/badge/frameworks-19-blue)](https://github.com/PurpleHaze2320/ai-agent-pulse)
[![License: MIT](https://img.shields.io/badge/License-MIT-green.svg)](https://opensource.org/licenses/MIT)
[![GitHub stars](https://img.shields.io/github/stars/PurpleHaze2320/ai-agent-pulse?style=social)](https://github.com/PurpleHaze2320/ai-agent-pulse/stargazers)

> Automated daily tracking of the AI agent framework ecosystem's health, momentum, and trends.
> Last updated: **2026-08-16 06:47 UTC** | Tracking **19** frameworks

## How It Works

This bot runs daily via GitHub Actions and collects metrics from the GitHub API for the most important
AI agent frameworks. It computes a **Pulse Score** (0-100) based on six weighted signals: star velocity,
release freshness, issue health, commit activity, community size, and fork engagement. The result is
a living dashboard that shows which frameworks are gaining momentum and which are losing steam.

## 🏆 Pulse Leaderboard

| Rank | Framework | Pulse | Stars | ⭐ 7d | Commits (4w) | Last Release | Category |
|------|-----------|-------|-------|-------|--------------|--------------|----------|
| 1 | [BrowserUse](https://github.com/browser-use/browser-use) | 🟢 **88.9** | 109.4k | 🚀 +963 | 109 | 19 days ago | `web-agent` |
| 2 | [CrewAI](https://github.com/crewAIInc/crewAI) | 🟢 **80.6** | 57.1k | 🚀 +317 | 91 | 2 days ago | `multi-agent` |
| 3 | [Mastra](https://github.com/mastra-ai/mastra) | 🟢 **76.8** | 27.2k | 🚀 +169 | 1285 | 3 days ago | `typescript` |
| 4 | [OpenAI Agents SDK](https://github.com/openai/openai-agents-python) | 🟢 **76.6** | 28.7k | 🚀 +168 | 322 | 1 day ago | `orchestration` |
| 5 | [PydanticAI](https://github.com/pydantic/pydantic-ai) | 🟢 **75.6** | 19.3k | 🚀 +167 | 222 | 1 day ago | `structured` |
| 6 | [LangGraph](https://github.com/langchain-ai/langgraph) | 🟢 **75.5** | 39.8k | 🚀 +504 | 40 | 4 days ago | `orchestration` |
| 7 | [Google ADK](https://github.com/google/adk-python) | 🟢 **73.6** | 21.1k | 📈 +81 | 365 | 2 days ago | `orchestration` |
| 8 | [DSPy](https://github.com/stanfordnlp/dspy) | 🟢 **72.5** | 37.3k | 🚀 +477 | 44 | 12 days ago | `optimization` |
| 9 | [Haystack](https://github.com/deepset-ai/haystack) | 🟡 **69.3** | 26.2k | 📈 +68 | 211 | 26 days ago | `pipeline` |
| 10 | [Claude Agent SDK](https://github.com/anthropics/claude-code) | 🟡 **68.7** | 141.6k | 🚀 +843 | 20 | 1 day ago | `orchestration` |
| 11 | [Composio](https://github.com/ComposioHQ/composio) | 🟡 **67.9** | 29.7k | 🚀 +112 | 317 | 2 days ago | `tooling` |
| 12 | [Agno](https://github.com/agno-agi/agno) | 🟡 **66.0** | 41.7k | 📈 +96 | 74 | 2 days ago | `multi-agent` |
| 13 | [LlamaIndex](https://github.com/run-llama/llama_index) | 🟡 **63.2** | 51.7k | 🚀 +190 | 34 | 1 mo ago | `data-agent` |
| 14 | [AG2](https://github.com/ag2ai/ag2) | 🟡 **63.0** | 4.9k | ↗️ +17 | 65 | 1 day ago | `multi-agent` |
| 15 | [Semantic Kernel](https://github.com/microsoft/semantic-kernel) | 🟡 **54.1** | 28.5k | 📈 +24 | 20 | 9 days ago | `enterprise` |
| 16 | [Letta](https://github.com/letta-ai/letta) | 🟡 **41.8** | 24.3k | 🚀 +107 | 4 | 3 mo ago | `memory` |
| 17 | [Smolagents](https://github.com/huggingface/smolagents) | 🟠 **37.2** | 28.8k | 📈 +87 | 0 | 2 mo ago | `lightweight` |
| 18 | [AutoGen](https://github.com/microsoft/autogen) | 🟠 **33.9** | 60.4k | 🚀 +120 | 0 | 10 mo ago | `multi-agent` |
| 19 | [Swarm](https://github.com/openai/swarm) | 🔴 **9.4** | 21.9k | ↗️ +13 | 0 | — | `experimental` |

## 📂 By Category

- `data-agent`: **LlamaIndex** (63.2)
- `enterprise`: **Semantic Kernel** (54.1)
- `experimental`: **Swarm** (9.4)
- `lightweight`: **Smolagents** (37.2)
- `memory`: **Letta** (41.8)
- `multi-agent`: **CrewAI** (80.6), **Agno** (66.0), **AG2** (63.0), **AutoGen** (33.9)
- `optimization`: **DSPy** (72.5)
- `orchestration`: **OpenAI Agents SDK** (76.6), **LangGraph** (75.5), **Google ADK** (73.6), **Claude Agent SDK** (68.7)
- `pipeline`: **Haystack** (69.3)
- `structured`: **PydanticAI** (75.6)
- `tooling`: **Composio** (67.9)
- `typescript`: **Mastra** (76.8)
- `web-agent`: **BrowserUse** (88.9)

## 🔍 Top 5 — Score Breakdown

| Framework | Star Velocity | Release Freshness | Issue Health | Commit Activity | Community | Fork Ratio |
|-----------|:---:|:---:|:---:|:---:|:---:|:---:|
| **BrowserUse** | 100 | 93.7 | 93.8 | 100 | 66.8 | 44.0 |
| **CrewAI** | 66.3 | 99.3 | 94.9 | 91.0 | 60.0 | 57.1 |
| **Mastra** | 37.9 | 99.0 | 96.0 | 100 | 92.8 | 38.8 |
| **OpenAI Agents SDK** | 34.1 | 99.7 | 99.4 | 100 | 69.8 | 63.0 |
| **PydanticAI** | 34.1 | 99.7 | 82.9 | 100 | 95.0 | 52.4 |

## 💡 Key Insights

- **Hottest framework**: BrowserUse with a Pulse Score of 88.9
- **Fastest growing**: BrowserUse gained +963 stars this week
- **Most active development**: Mastra with 1285 commits in the last 4 weeks
- **Stale releases**: AutoGen, Swarm haven't released in a while

## 📦 Recent Releases

- **AG2** [`v1.0.2`](https://github.com/ag2ai/ag2/releases/tag/v1.0.2) — 1 day ago
- **PydanticAI** [`v2.31.0`](https://github.com/pydantic/pydantic-ai/releases/tag/v2.31.0) — 1 day ago
- **OpenAI Agents SDK** [`v0.21.0`](https://github.com/openai/openai-agents-python/releases/tag/v0.21.0) — 1 day ago
- **Claude Agent SDK** [`v2.1.233`](https://github.com/anthropics/claude-code/releases/tag/v2.1.233) — 1 day ago
- **CrewAI** [`1.15.16`](https://github.com/crewAIInc/crewAI/releases/tag/1.15.16) — 2 days ago
- **Google ADK** [`v2.7.0`](https://github.com/google/adk-python/releases/tag/v2.7.0) — 2 days ago
- **Composio** [`@composio/cli@0.3.4-beta.351`](https://github.com/ComposioHQ/composio/releases/tag/@composio/cli@0.3.4-beta.351) — 2 days ago *(pre-release)*
- **Agno** [`v2.9.0`](https://github.com/agno-agi/agno/releases/tag/v2.9.0) — 2 days ago
- **Mastra** [`@mastra/core@1.58.0`](https://github.com/mastra-ai/mastra/releases/tag/@mastra/core@1.58.0) — 3 days ago
- **LangGraph** [`1.2.11`](https://github.com/langchain-ai/langgraph/releases/tag/1.2.11) — 4 days ago

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

*Powered by GitHub Actions • Data refreshed daily • Last run: 2026-08-16 06:47 UTC*