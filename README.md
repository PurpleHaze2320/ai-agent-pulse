# 🔬 AI Agent Framework Pulse Tracker

[![Daily Update](https://github.com/PurpleHaze2320/ai-agent-pulse/actions/workflows/track.yml/badge.svg)](https://github.com/PurpleHaze2320/ai-agent-pulse/actions/workflows/track.yml)
[![Frameworks Tracked](https://img.shields.io/badge/frameworks-19-blue)](https://github.com/PurpleHaze2320/ai-agent-pulse)
[![License: MIT](https://img.shields.io/badge/License-MIT-green.svg)](https://opensource.org/licenses/MIT)
[![GitHub stars](https://img.shields.io/github/stars/PurpleHaze2320/ai-agent-pulse?style=social)](https://github.com/PurpleHaze2320/ai-agent-pulse/stargazers)

> Automated daily tracking of the AI agent framework ecosystem's health, momentum, and trends.
> Last updated: **2026-11-01 12:57 UTC** | Tracking **19** frameworks

## How It Works

This bot runs daily via GitHub Actions and collects metrics from the GitHub API for the most important
AI agent frameworks. It computes a **Pulse Score** (0-100) based on six weighted signals: star velocity,
release freshness, issue health, commit activity, community size, and fork engagement. The result is
a living dashboard that shows which frameworks are gaining momentum and which are losing steam.

## 🏆 Pulse Leaderboard

| Rank | Framework | Pulse | Stars | ⭐ 7d | Commits (4w) | Last Release | Category |
|------|-----------|-------|-------|-------|--------------|--------------|----------|
| 1 | [BrowserUse](https://github.com/browser-use/browser-use) | 🟢 **89.8** | 119.7k | 🚀 +643 | 107 | 5 days ago | `web-agent` |
| 2 | [LangGraph](https://github.com/langchain-ai/langgraph) | 🟢 **84.5** | 44.3k | 🚀 +397 | 98 | 1 day ago | `orchestration` |
| 3 | [CrewAI](https://github.com/crewAIInc/crewAI) | 🟢 **80.1** | 60.4k | 🚀 +292 | 166 | 3 days ago | `multi-agent` |
| 4 | [Mastra](https://github.com/mastra-ai/mastra) | 🟢 **76.8** | 29.2k | 🚀 +186 | 1950 | 3 days ago | `typescript` |
| 5 | [Google ADK](https://github.com/google/adk-python) | 🟢 **73.7** | 22.1k | 📈 +69 | 398 | 8 days ago | `orchestration` |
| 6 | [Claude Agent SDK](https://github.com/anthropics/claude-code) | 🟢 **73.2** | 154.1k | 🚀 +799 | 39 | 1 day ago | `orchestration` |
| 7 | [PydanticAI](https://github.com/pydantic/pydantic-ai) | 🟢 **71.2** | 21.0k | 🚀 +122 | 1035 | 26 days ago | `structured` |
| 8 | [Haystack](https://github.com/deepset-ai/haystack) | 🟢 **71.1** | 26.9k | 📈 +61 | 169 | 10 days ago | `pipeline` |
| 9 | [Agno](https://github.com/agno-agi/agno) | 🟢 **71.1** | 43.0k | 🚀 +119 | 140 | 2 days ago | `multi-agent` |
| 10 | [AG2](https://github.com/ag2ai/ag2) | 🟡 **69.8** | 5.0k | ↗️ +17 | 104 | 4 days ago | `multi-agent` |
| 11 | [OpenAI Agents SDK](https://github.com/openai/openai-agents-python) | 🟡 **68.7** | 30.4k | 🚀 +161 | 62 | 17 days ago | `orchestration` |
| 12 | [Composio](https://github.com/ComposioHQ/composio) | 🟡 **68.3** | 30.9k | 🚀 +117 | 337 | 1 day ago | `tooling` |
| 13 | [Semantic Kernel](https://github.com/microsoft/semantic-kernel) | 🟡 **63.3** | 28.7k | 📈 +28 | 60 | 3 days ago | `enterprise` |
| 14 | [DSPy](https://github.com/stanfordnlp/dspy) | 🟡 **60.2** | 38.9k | 📈 +98 | 63 | 19 days ago | `optimization` |
| 15 | [LlamaIndex](https://github.com/run-llama/llama_index) | 🟡 **54.1** | 52.8k | 🚀 +111 | 6 | 1 mo ago | `data-agent` |
| 16 | [Letta](https://github.com/letta-ai/letta) | 🟠 **34.3** | 25.3k | 📈 +64 | 1 | 5 mo ago | `memory` |
| 17 | [AutoGen](https://github.com/microsoft/autogen) | 🟠 **32.9** | 61.7k | 🚀 +107 | 2 | 1y ago | `multi-agent` |
| 18 | [Smolagents](https://github.com/huggingface/smolagents) | 🟠 **32.9** | 30.2k | 🚀 +128 | 0 | 5 mo ago | `lightweight` |
| 19 | [Swarm](https://github.com/openai/swarm) | 🔴 **9.1** | 22.1k | ↗️ +15 | 0 | — | `experimental` |

## 📂 By Category

- `data-agent`: **LlamaIndex** (54.1)
- `enterprise`: **Semantic Kernel** (63.3)
- `experimental`: **Swarm** (9.1)
- `lightweight`: **Smolagents** (32.9)
- `memory`: **Letta** (34.3)
- `multi-agent`: **CrewAI** (80.1), **Agno** (71.1), **AG2** (69.8), **AutoGen** (32.9)
- `optimization`: **DSPy** (60.2)
- `orchestration`: **LangGraph** (84.5), **Google ADK** (73.7), **Claude Agent SDK** (73.2), **OpenAI Agents SDK** (68.7)
- `pipeline`: **Haystack** (71.1)
- `structured`: **PydanticAI** (71.2)
- `tooling`: **Composio** (68.3)
- `typescript`: **Mastra** (76.8)
- `web-agent`: **BrowserUse** (89.8)

## 🔍 Top 5 — Score Breakdown

| Framework | Star Velocity | Release Freshness | Issue Health | Commit Activity | Community | Fork Ratio |
|-----------|:---:|:---:|:---:|:---:|:---:|:---:|
| **BrowserUse** | 100 | 98.3 | 89.7 | 100 | 72.2 | 44.6 |
| **LangGraph** | 80.4 | 99.7 | 81.9 | 98.0 | 57.4 | 68.8 |
| **CrewAI** | 57.2 | 99.0 | 85.4 | 100 | 72.6 | 59.6 |
| **Mastra** | 37.3 | 99.0 | 94.5 | 100 | 93.4 | 41.9 |
| **Google ADK** | 15.3 | 97.3 | 94.2 | 100 | 85.4 | 77.6 |

## 💡 Key Insights

- **Hottest framework**: BrowserUse with a Pulse Score of 89.8
- **Fastest growing**: Claude Agent SDK gained +799 stars this week
- **Most active development**: Mastra with 1950 commits in the last 4 weeks
- **Stale releases**: AutoGen, Swarm haven't released in a while

## 📦 Recent Releases

- **Claude Agent SDK** [`v2.1.316`](https://github.com/anthropics/claude-code/releases/tag/v2.1.316) — 1 day ago
- **LangGraph** [`1.2.19`](https://github.com/langchain-ai/langgraph/releases/tag/1.2.19) — 1 day ago
- **Composio** [`@composio/cli@0.5.1-beta.523`](https://github.com/ComposioHQ/composio/releases/tag/@composio/cli@0.5.1-beta.523) — 1 day ago *(pre-release)*
- **Agno** [`v3.1.12`](https://github.com/agno-agi/agno/releases/tag/v3.1.12) — 2 days ago
- **CrewAI** [`1.15.33`](https://github.com/crewAIInc/crewAI/releases/tag/1.15.33) — 3 days ago
- **Mastra** [`@mastra/core@1.80.0`](https://github.com/mastra-ai/mastra/releases/tag/@mastra/core@1.80.0) — 3 days ago
- **Semantic Kernel** [`python-1.46.0`](https://github.com/microsoft/semantic-kernel/releases/tag/python-1.46.0) — 3 days ago
- **AG2** [`v1.2.2`](https://github.com/ag2ai/ag2/releases/tag/v1.2.2) — 4 days ago
- **BrowserUse** [`0.13.14`](https://github.com/browser-use/browser-use/releases/tag/0.13.14) — 5 days ago
- **Google ADK** [`v2.13.0`](https://github.com/google/adk-python/releases/tag/v2.13.0) — 8 days ago

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

*Powered by GitHub Actions • Data refreshed daily • Last run: 2026-11-01 12:57 UTC*