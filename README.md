# 🔬 AI Agent Framework Pulse Tracker

[![Daily Update](https://github.com/PurpleHaze2320/ai-agent-pulse/actions/workflows/track.yml/badge.svg)](https://github.com/PurpleHaze2320/ai-agent-pulse/actions/workflows/track.yml)
[![Frameworks Tracked](https://img.shields.io/badge/frameworks-19-blue)](https://github.com/PurpleHaze2320/ai-agent-pulse)
[![License: MIT](https://img.shields.io/badge/License-MIT-green.svg)](https://opensource.org/licenses/MIT)
[![GitHub stars](https://img.shields.io/github/stars/PurpleHaze2320/ai-agent-pulse?style=social)](https://github.com/PurpleHaze2320/ai-agent-pulse/stargazers)

> Automated daily tracking of the AI agent framework ecosystem's health, momentum, and trends.
> Last updated: **2026-07-16 08:22 UTC** | Tracking **19** frameworks

## How It Works

This bot runs daily via GitHub Actions and collects metrics from the GitHub API for the most important
AI agent frameworks. It computes a **Pulse Score** (0-100) based on six weighted signals: star velocity,
release freshness, issue health, commit activity, community size, and fork engagement. The result is
a living dashboard that shows which frameworks are gaining momentum and which are losing steam.

## 🏆 Pulse Leaderboard

| Rank | Framework | Pulse | Stars | ⭐ 7d | Commits (4w) | Last Release | Category |
|------|-----------|-------|-------|-------|--------------|--------------|----------|
| 1 | [CrewAI](https://github.com/crewAIInc/crewAI) | 🟢 **84.0** | 55.6k | 🚀 +398 | 87 | 8 days ago | `multi-agent` |
| 2 | [BrowserUse](https://github.com/browser-use/browser-use) | 🟢 **84.0** | 105.0k | 🚀 +1143 | 72 | 4 days ago | `web-agent` |
| 3 | [Mastra](https://github.com/mastra-ai/mastra) | 🟢 **79.4** | 26.2k | 🚀 +230 | 1114 | today | `typescript` |
| 4 | [OpenAI Agents SDK](https://github.com/openai/openai-agents-python) | 🟢 **76.2** | 27.9k | 🚀 +191 | 113 | 5 days ago | `orchestration` |
| 5 | [LangGraph](https://github.com/langchain-ai/langgraph) | 🟢 **75.5** | 37.4k | 🚀 +534 | 39 | 6 days ago | `orchestration` |
| 6 | [Agno](https://github.com/agno-agi/agno) | 🟢 **72.5** | 41.2k | 🚀 +124 | 139 | 1 day ago | `multi-agent` |
| 7 | [Google ADK](https://github.com/google/adk-python) | 🟢 **72.3** | 20.6k | 📈 +97 | 316 | 8 days ago | `orchestration` |
| 8 | [Claude Agent SDK](https://github.com/anthropics/claude-code) | 🟢 **70.5** | 138.0k | 🚀 +1068 | 26 | today | `orchestration` |
| 9 | [Composio](https://github.com/ComposioHQ/composio) | 🟡 **67.7** | 29.3k | 🚀 +111 | 163 | 1 day ago | `tooling` |
| 10 | [PydanticAI](https://github.com/pydantic/pydantic-ai) | 🟡 **60.0** | 18.6k | 🚀 +276 | 0 | today | `structured` |
| 11 | [LlamaIndex](https://github.com/run-llama/llama_index) | 🟡 **56.1** | 50.9k | 🚀 +134 | 0 | 21 days ago | `data-agent` |
| 12 | [DSPy](https://github.com/stanfordnlp/dspy) | 🟡 **51.3** | 36.2k | 🚀 +191 | 0 | 1 mo ago | `optimization` |
| 13 | [Semantic Kernel](https://github.com/microsoft/semantic-kernel) | 🟡 **50.5** | 28.3k | 📈 +31 | 0 | 8 days ago | `enterprise` |
| 14 | [AG2](https://github.com/ag2ai/ag2) | 🟡 **49.7** | 4.8k | 📈 +29 | 0 | 12 days ago | `multi-agent` |
| 15 | [Haystack](https://github.com/deepset-ai/haystack) | 🟡 **49.6** | 25.9k | 📈 +54 | 0 | 7 days ago | `pipeline` |
| 16 | [Letta](https://github.com/letta-ai/letta) | 🟡 **43.0** | 23.8k | 📈 +96 | 2 | 2 mo ago | `memory` |
| 17 | [Smolagents](https://github.com/huggingface/smolagents) | 🟡 **41.8** | 28.4k | 🚀 +125 | 4 | 1 mo ago | `lightweight` |
| 18 | [AutoGen](https://github.com/microsoft/autogen) | 🟠 **36.7** | 59.8k | 🚀 +168 | 0 | 9 mo ago | `multi-agent` |
| 19 | [Swarm](https://github.com/openai/swarm) | 🔴 **9.0** | 21.8k | 📈 +21 | 0 | — | `experimental` |

## 📂 By Category

- `data-agent`: **LlamaIndex** (56.1)
- `enterprise`: **Semantic Kernel** (50.5)
- `experimental`: **Swarm** (9.0)
- `lightweight`: **Smolagents** (41.8)
- `memory`: **Letta** (43.0)
- `multi-agent`: **CrewAI** (84.0), **Agno** (72.5), **AG2** (49.7), **AutoGen** (36.7)
- `optimization`: **DSPy** (51.3)
- `orchestration`: **OpenAI Agents SDK** (76.2), **LangGraph** (75.5), **Google ADK** (72.3), **Claude Agent SDK** (70.5)
- `pipeline`: **Haystack** (49.6)
- `structured`: **PydanticAI** (60.0)
- `tooling`: **Composio** (67.7)
- `typescript`: **Mastra** (79.4)
- `web-agent`: **BrowserUse** (84.0)

## 🔍 Top 5 — Score Breakdown

| Framework | Star Velocity | Release Freshness | Issue Health | Commit Activity | Community | Fork Ratio |
|-----------|:---:|:---:|:---:|:---:|:---:|:---:|
| **CrewAI** | 84.5 | 97.3 | 95.9 | 87.0 | 59.6 | 56.4 |
| **BrowserUse** | 100 | 98.7 | 94.7 | 72.0 | 63.0 | 44.0 |
| **Mastra** | 48.3 | 100.0 | 95.2 | 100 | 92.8 | 37.2 |
| **OpenAI Agents SDK** | 38.0 | 98.3 | 98.1 | 100 | 60.6 | 62.1 |
| **LangGraph** | 100 | 98.0 | 72.8 | 39.0 | 55.2 | 67.0 |

## 💡 Key Insights

- **Hottest framework**: CrewAI with a Pulse Score of 84.0
- **Fastest growing**: BrowserUse gained +1143 stars this week
- **Most active development**: Mastra with 1114 commits in the last 4 weeks
- **Stale releases**: AutoGen, Swarm haven't released in a while

## 📦 Recent Releases

- **PydanticAI** [`v2.11.0`](https://github.com/pydantic/pydantic-ai/releases/tag/v2.11.0) — today
- **Claude Agent SDK** [`v2.1.211`](https://github.com/anthropics/claude-code/releases/tag/v2.1.211) — today
- **Mastra** [`@mastra/core@1.51.0`](https://github.com/mastra-ai/mastra/releases/tag/@mastra/core@1.51.0) — today
- **Composio** [`@composio/cli@0.2.32`](https://github.com/ComposioHQ/composio/releases/tag/@composio/cli@0.2.32) — 1 day ago
- **Agno** [`v2.7.3`](https://github.com/agno-agi/agno/releases/tag/v2.7.3) — 1 day ago
- **BrowserUse** [`0.13.4`](https://github.com/browser-use/browser-use/releases/tag/0.13.4) — 4 days ago
- **OpenAI Agents SDK** [`v0.18.2`](https://github.com/openai/openai-agents-python/releases/tag/v0.18.2) — 5 days ago
- **LangGraph** [`1.2.9`](https://github.com/langchain-ai/langgraph/releases/tag/1.2.9) — 6 days ago
- **Haystack** [`v2.31.0`](https://github.com/deepset-ai/haystack/releases/tag/v2.31.0) — 7 days ago
- **CrewAI** [`1.15.2`](https://github.com/crewAIInc/crewAI/releases/tag/1.15.2) — 8 days ago

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

*Powered by GitHub Actions • Data refreshed daily • Last run: 2026-07-16 08:22 UTC*