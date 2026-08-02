# 🔬 AI Agent Framework Pulse Tracker

[![Daily Update](https://github.com/PurpleHaze2320/ai-agent-pulse/actions/workflows/track.yml/badge.svg)](https://github.com/PurpleHaze2320/ai-agent-pulse/actions/workflows/track.yml)
[![Frameworks Tracked](https://img.shields.io/badge/frameworks-19-blue)](https://github.com/PurpleHaze2320/ai-agent-pulse)
[![License: MIT](https://img.shields.io/badge/License-MIT-green.svg)](https://opensource.org/licenses/MIT)
[![GitHub stars](https://img.shields.io/github/stars/PurpleHaze2320/ai-agent-pulse?style=social)](https://github.com/PurpleHaze2320/ai-agent-pulse/stargazers)

> Automated daily tracking of the AI agent framework ecosystem's health, momentum, and trends.
> Last updated: **2026-08-02 08:30 UTC** | Tracking **19** frameworks

## How It Works

This bot runs daily via GitHub Actions and collects metrics from the GitHub API for the most important
AI agent frameworks. It computes a **Pulse Score** (0-100) based on six weighted signals: star velocity,
release freshness, issue health, commit activity, community size, and fork engagement. The result is
a living dashboard that shows which frameworks are gaining momentum and which are losing steam.

## 🏆 Pulse Leaderboard

| Rank | Framework | Pulse | Stars | ⭐ 7d | Commits (4w) | Last Release | Category |
|------|-----------|-------|-------|-------|--------------|--------------|----------|
| 1 | [Mastra](https://github.com/mastra-ai/mastra) | 🟢 **79.8** | 26.8k | 🚀 +250 | 979 | 1 day ago | `typescript` |
| 2 | [BrowserUse](https://github.com/browser-use/browser-use) | 🟢 **77.1** | 107.5k | 🚀 +744 | 38 | 5 days ago | `web-agent` |
| 3 | [CrewAI](https://github.com/crewAIInc/crewAI) | 🟢 **76.8** | 56.5k | 🚀 +356 | 61 | 1 day ago | `multi-agent` |
| 4 | [OpenAI Agents SDK](https://github.com/openai/openai-agents-python) | 🟢 **75.9** | 28.3k | 🚀 +166 | 156 | 1 day ago | `orchestration` |
| 5 | [Google ADK](https://github.com/google/adk-python) | 🟢 **73.4** | 21.0k | 📈 +89 | 262 | 1 day ago | `orchestration` |
| 6 | [Agno](https://github.com/agno-agi/agno) | 🟢 **72.2** | 41.5k | 🚀 +111 | 107 | 2 days ago | `multi-agent` |
| 7 | [LangGraph](https://github.com/langchain-ai/langgraph) | 🟢 **71.3** | 38.7k | 🚀 +496 | 17 | 2 days ago | `orchestration` |
| 8 | [Haystack](https://github.com/deepset-ai/haystack) | 🟡 **69.8** | 26.1k | 📈 +67 | 189 | 12 days ago | `pipeline` |
| 9 | [Composio](https://github.com/ComposioHQ/composio) | 🟡 **67.8** | 29.5k | 🚀 +115 | 171 | 2 days ago | `tooling` |
| 10 | [Claude Agent SDK](https://github.com/anthropics/claude-code) | 🟡 **67.4** | 140.0k | 🚀 +836 | 15 | 8 days ago | `orchestration` |
| 11 | [LlamaIndex](https://github.com/run-llama/llama_index) | 🟡 **56.9** | 51.3k | 🚀 +192 | 0 | 1 mo ago | `data-agent` |
| 12 | [PydanticAI](https://github.com/pydantic/pydantic-ai) | 🟡 **55.9** | 19.0k | 🚀 +161 | 0 | 1 day ago | `structured` |
| 13 | [AG2](https://github.com/ag2ai/ag2) | 🟡 **50.2** | 4.8k | 📈 +26 | 0 | 4 days ago | `multi-agent` |
| 14 | [Semantic Kernel](https://github.com/microsoft/semantic-kernel) | 🟡 **49.2** | 28.4k | 📈 +29 | 0 | 25 days ago | `enterprise` |
| 15 | [DSPy](https://github.com/stanfordnlp/dspy) | 🟡 **46.9** | 36.5k | 🚀 +137 | 0 | 2 mo ago | `optimization` |
| 16 | [Letta](https://github.com/letta-ai/letta) | 🟡 **41.6** | 24.1k | 📈 +91 | 2 | 2 mo ago | `memory` |
| 17 | [Smolagents](https://github.com/huggingface/smolagents) | 🟠 **38.8** | 28.6k | 📈 +100 | 0 | 2 mo ago | `lightweight` |
| 18 | [AutoGen](https://github.com/microsoft/autogen) | 🟠 **36.6** | 60.2k | 🚀 +193 | 0 | 10 mo ago | `multi-agent` |
| 19 | [Swarm](https://github.com/openai/swarm) | 🔴 **9.5** | 21.9k | ↗️ +13 | 0 | — | `experimental` |

## 📂 By Category

- `data-agent`: **LlamaIndex** (56.9)
- `enterprise`: **Semantic Kernel** (49.2)
- `experimental`: **Swarm** (9.5)
- `lightweight`: **Smolagents** (38.8)
- `memory`: **Letta** (41.6)
- `multi-agent`: **CrewAI** (76.8), **Agno** (72.2), **AG2** (50.2), **AutoGen** (36.6)
- `optimization`: **DSPy** (46.9)
- `orchestration`: **OpenAI Agents SDK** (75.9), **Google ADK** (73.4), **LangGraph** (71.3), **Claude Agent SDK** (67.4)
- `pipeline`: **Haystack** (69.8)
- `structured`: **PydanticAI** (55.9)
- `tooling`: **Composio** (67.8)
- `typescript`: **Mastra** (79.8)
- `web-agent`: **BrowserUse** (77.1)

## 🔍 Top 5 — Score Breakdown

| Framework | Star Velocity | Release Freshness | Issue Health | Commit Activity | Community | Fork Ratio |
|-----------|:---:|:---:|:---:|:---:|:---:|:---:|
| **Mastra** | 50.8 | 99.7 | 93.7 | 100 | 93.0 | 38.1 |
| **BrowserUse** | 100 | 98.3 | 94.4 | 38.0 | 63.0 | 44.0 |
| **CrewAI** | 74.9 | 99.7 | 95.2 | 61.0 | 59.8 | 56.9 |
| **OpenAI Agents SDK** | 34.0 | 99.7 | 98.4 | 100 | 64.4 | 62.5 |
| **Google ADK** | 20.6 | 99.7 | 88.2 | 100 | 79.2 | 72.1 |

## 💡 Key Insights

- **Hottest framework**: Mastra with a Pulse Score of 79.8
- **Fastest growing**: Claude Agent SDK gained +836 stars this week
- **Most active development**: Mastra with 979 commits in the last 4 weeks
- **Stale releases**: AutoGen, Swarm haven't released in a while

## 📦 Recent Releases

- **PydanticAI** [`v2.22.0`](https://github.com/pydantic/pydantic-ai/releases/tag/v2.22.0) — 1 day ago
- **OpenAI Agents SDK** [`v0.19.2`](https://github.com/openai/openai-agents-python/releases/tag/v0.19.2) — 1 day ago
- **Google ADK** [`v2.6.1`](https://github.com/google/adk-python/releases/tag/v2.6.1) — 1 day ago
- **CrewAI** [`1.15.10`](https://github.com/crewAIInc/crewAI/releases/tag/1.15.10) — 1 day ago
- **Mastra** [`@mastra/core@1.55.0`](https://github.com/mastra-ai/mastra/releases/tag/@mastra/core@1.55.0) — 1 day ago
- **LangGraph** [`checkpointsqlite==3.1.1`](https://github.com/langchain-ai/langgraph/releases/tag/checkpointsqlite==3.1.1) — 2 days ago
- **Agno** [`v2.8.6`](https://github.com/agno-agi/agno/releases/tag/v2.8.6) — 2 days ago
- **Composio** [`@composio/slim@0.14.1`](https://github.com/ComposioHQ/composio/releases/tag/@composio/slim@0.14.1) — 2 days ago
- **AG2** [`v1.0.1`](https://github.com/ag2ai/ag2/releases/tag/v1.0.1) — 4 days ago
- **BrowserUse** [`0.13.7`](https://github.com/browser-use/browser-use/releases/tag/0.13.7) — 5 days ago

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

*Powered by GitHub Actions • Data refreshed daily • Last run: 2026-08-02 08:30 UTC*