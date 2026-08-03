# 🔬 AI Agent Framework Pulse Tracker

[![Daily Update](https://github.com/PurpleHaze2320/ai-agent-pulse/actions/workflows/track.yml/badge.svg)](https://github.com/PurpleHaze2320/ai-agent-pulse/actions/workflows/track.yml)
[![Frameworks Tracked](https://img.shields.io/badge/frameworks-19-blue)](https://github.com/PurpleHaze2320/ai-agent-pulse)
[![License: MIT](https://img.shields.io/badge/License-MIT-green.svg)](https://opensource.org/licenses/MIT)
[![GitHub stars](https://img.shields.io/github/stars/PurpleHaze2320/ai-agent-pulse?style=social)](https://github.com/PurpleHaze2320/ai-agent-pulse/stargazers)

> Automated daily tracking of the AI agent framework ecosystem's health, momentum, and trends.
> Last updated: **2026-08-03 09:55 UTC** | Tracking **19** frameworks

## How It Works

This bot runs daily via GitHub Actions and collects metrics from the GitHub API for the most important
AI agent frameworks. It computes a **Pulse Score** (0-100) based on six weighted signals: star velocity,
release freshness, issue health, commit activity, community size, and fork engagement. The result is
a living dashboard that shows which frameworks are gaining momentum and which are losing steam.

## 🏆 Pulse Leaderboard

| Rank | Framework | Pulse | Stars | ⭐ 7d | Commits (4w) | Last Release | Category |
|------|-----------|-------|-------|-------|--------------|--------------|----------|
| 1 | [BrowserUse](https://github.com/browser-use/browser-use) | 🟢 **89.8** | 107.7k | 🚀 +718 | 153 | 6 days ago | `web-agent` |
| 2 | [Mastra](https://github.com/mastra-ai/mastra) | 🟢 **79.5** | 26.9k | 🚀 +244 | 995 | 2 days ago | `typescript` |
| 3 | [CrewAI](https://github.com/crewAIInc/crewAI) | 🟢 **76.2** | 56.5k | 🚀 +341 | 61 | 2 days ago | `multi-agent` |
| 4 | [OpenAI Agents SDK](https://github.com/openai/openai-agents-python) | 🟢 **75.2** | 28.4k | 🚀 +147 | 173 | 2 days ago | `orchestration` |
| 5 | [Google ADK](https://github.com/google/adk-python) | 🟢 **73.2** | 21.0k | 📈 +82 | 262 | 2 days ago | `orchestration` |
| 6 | [Agno](https://github.com/agno-agi/agno) | 🟢 **72.1** | 41.6k | 🚀 +111 | 107 | 3 days ago | `multi-agent` |
| 7 | [LangGraph](https://github.com/langchain-ai/langgraph) | 🟢 **71.2** | 38.7k | 🚀 +510 | 17 | 3 days ago | `orchestration` |
| 8 | [Haystack](https://github.com/deepset-ai/haystack) | 🟡 **69.8** | 26.1k | 📈 +67 | 192 | 13 days ago | `pipeline` |
| 9 | [Claude Agent SDK](https://github.com/anthropics/claude-code) | 🟡 **67.3** | 140.1k | 🚀 +823 | 15 | 9 days ago | `orchestration` |
| 10 | [Composio](https://github.com/ComposioHQ/composio) | 🟡 **67.1** | 29.5k | 🚀 +102 | 174 | 3 days ago | `tooling` |
| 11 | [LlamaIndex](https://github.com/run-llama/llama_index) | 🟡 **60.3** | 51.3k | 🚀 +197 | 16 | 1 mo ago | `data-agent` |
| 12 | [PydanticAI](https://github.com/pydantic/pydantic-ai) | 🟡 **57.1** | 19.0k | 🚀 +193 | 0 | 2 days ago | `structured` |
| 13 | [Semantic Kernel](https://github.com/microsoft/semantic-kernel) | 🟡 **52.0** | 28.4k | 📈 +31 | 14 | 27 days ago | `enterprise` |
| 14 | [AG2](https://github.com/ag2ai/ag2) | 🟡 **50.2** | 4.8k | 📈 +28 | 0 | 5 days ago | `multi-agent` |
| 15 | [DSPy](https://github.com/stanfordnlp/dspy) | 🟡 **48.1** | 36.6k | 🚀 +170 | 0 | 2 mo ago | `optimization` |
| 16 | [Letta](https://github.com/letta-ai/letta) | 🟡 **41.4** | 24.1k | 📈 +85 | 2 | 2 mo ago | `memory` |
| 17 | [Smolagents](https://github.com/huggingface/smolagents) | 🟠 **38.3** | 28.6k | 📈 +89 | 0 | 2 mo ago | `lightweight` |
| 18 | [AutoGen](https://github.com/microsoft/autogen) | 🟠 **35.5** | 60.2k | 🚀 +162 | 0 | 10 mo ago | `multi-agent` |
| 19 | [Swarm](https://github.com/openai/swarm) | 🔴 **9.3** | 21.9k | ↗️ +9 | 0 | — | `experimental` |

## 📂 By Category

- `data-agent`: **LlamaIndex** (60.3)
- `enterprise`: **Semantic Kernel** (52.0)
- `experimental`: **Swarm** (9.3)
- `lightweight`: **Smolagents** (38.3)
- `memory`: **Letta** (41.4)
- `multi-agent`: **CrewAI** (76.2), **Agno** (72.1), **AG2** (50.2), **AutoGen** (35.5)
- `optimization`: **DSPy** (48.1)
- `orchestration`: **OpenAI Agents SDK** (75.2), **Google ADK** (73.2), **LangGraph** (71.2), **Claude Agent SDK** (67.3)
- `pipeline`: **Haystack** (69.8)
- `structured`: **PydanticAI** (57.1)
- `tooling`: **Composio** (67.1)
- `typescript`: **Mastra** (79.5)
- `web-agent`: **BrowserUse** (89.8)

## 🔍 Top 5 — Score Breakdown

| Framework | Star Velocity | Release Freshness | Issue Health | Commit Activity | Community | Fork Ratio |
|-----------|:---:|:---:|:---:|:---:|:---:|:---:|
| **BrowserUse** | 100 | 98.0 | 94.8 | 100 | 66.0 | 43.9 |
| **Mastra** | 50.0 | 99.3 | 93.6 | 100 | 93.0 | 38.1 |
| **CrewAI** | 72.9 | 99.3 | 95.1 | 61.0 | 59.8 | 56.9 |
| **OpenAI Agents SDK** | 31.3 | 99.3 | 98.5 | 100 | 64.4 | 62.6 |
| **Google ADK** | 19.7 | 99.3 | 88.2 | 100 | 79.2 | 72.2 |

## 💡 Key Insights

- **Hottest framework**: BrowserUse with a Pulse Score of 89.8
- **Fastest growing**: Claude Agent SDK gained +823 stars this week
- **Most active development**: Mastra with 995 commits in the last 4 weeks
- **Stale releases**: AutoGen, Swarm haven't released in a while

## 📦 Recent Releases

- **PydanticAI** [`v2.22.0`](https://github.com/pydantic/pydantic-ai/releases/tag/v2.22.0) — 2 days ago
- **OpenAI Agents SDK** [`v0.19.2`](https://github.com/openai/openai-agents-python/releases/tag/v0.19.2) — 2 days ago
- **Google ADK** [`v2.6.1`](https://github.com/google/adk-python/releases/tag/v2.6.1) — 2 days ago
- **CrewAI** [`1.15.10`](https://github.com/crewAIInc/crewAI/releases/tag/1.15.10) — 2 days ago
- **Mastra** [`@mastra/core@1.55.0`](https://github.com/mastra-ai/mastra/releases/tag/@mastra/core@1.55.0) — 2 days ago
- **LangGraph** [`checkpointsqlite==3.1.1`](https://github.com/langchain-ai/langgraph/releases/tag/checkpointsqlite==3.1.1) — 3 days ago
- **Agno** [`v2.8.6`](https://github.com/agno-agi/agno/releases/tag/v2.8.6) — 3 days ago
- **Composio** [`@composio/slim@0.14.1`](https://github.com/ComposioHQ/composio/releases/tag/@composio/slim@0.14.1) — 3 days ago
- **AG2** [`v1.0.1`](https://github.com/ag2ai/ag2/releases/tag/v1.0.1) — 5 days ago
- **BrowserUse** [`0.13.7`](https://github.com/browser-use/browser-use/releases/tag/0.13.7) — 6 days ago

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

*Powered by GitHub Actions • Data refreshed daily • Last run: 2026-08-03 09:55 UTC*