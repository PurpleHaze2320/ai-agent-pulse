# 🔬 AI Agent Framework Pulse Tracker

[![Daily Update](https://github.com/PurpleHaze2320/ai-agent-pulse/actions/workflows/track.yml/badge.svg)](https://github.com/PurpleHaze2320/ai-agent-pulse/actions/workflows/track.yml)
[![Frameworks Tracked](https://img.shields.io/badge/frameworks-19-blue)](https://github.com/PurpleHaze2320/ai-agent-pulse)
[![License: MIT](https://img.shields.io/badge/License-MIT-green.svg)](https://opensource.org/licenses/MIT)
[![GitHub stars](https://img.shields.io/github/stars/PurpleHaze2320/ai-agent-pulse?style=social)](https://github.com/PurpleHaze2320/ai-agent-pulse/stargazers)

> Automated daily tracking of the AI agent framework ecosystem's health, momentum, and trends.
> Last updated: **2026-09-02 10:58 UTC** | Tracking **19** frameworks

## How It Works

This bot runs daily via GitHub Actions and collects metrics from the GitHub API for the most important
AI agent frameworks. It computes a **Pulse Score** (0-100) based on six weighted signals: star velocity,
release freshness, issue health, commit activity, community size, and fork engagement. The result is
a living dashboard that shows which frameworks are gaining momentum and which are losing steam.

## 🏆 Pulse Leaderboard

| Rank | Framework | Pulse | Stars | ⭐ 7d | Commits (4w) | Last Release | Category |
|------|-----------|-------|-------|-------|--------------|--------------|----------|
| 1 | [BrowserUse](https://github.com/browser-use/browser-use) | 🟢 **89.2** | 112.0k | 🚀 +1485 | 136 | 16 days ago | `web-agent` |
| 2 | [CrewAI](https://github.com/crewAIInc/crewAI) | 🟢 **81.0** | 58.0k | 🚀 +373 | 83 | 5 days ago | `multi-agent` |
| 3 | [OpenAI Agents SDK](https://github.com/openai/openai-agents-python) | 🟢 **76.4** | 29.1k | 🚀 +166 | 201 | 13 days ago | `orchestration` |
| 4 | [Mastra](https://github.com/mastra-ai/mastra) | 🟢 **75.8** | 27.6k | 🚀 +161 | 1347 | 4 days ago | `typescript` |
| 5 | [PydanticAI](https://github.com/pydantic/pydantic-ai) | 🟢 **75.2** | 19.7k | 🚀 +165 | 215 | 1 day ago | `structured` |
| 6 | [Google ADK](https://github.com/google/adk-python) | 🟢 **73.3** | 21.4k | 📈 +81 | 434 | 5 days ago | `orchestration` |
| 7 | [Haystack](https://github.com/deepset-ai/haystack) | 🟢 **71.2** | 26.4k | 📈 +77 | 185 | 8 days ago | `pipeline` |
| 8 | [Claude Agent SDK](https://github.com/anthropics/claude-code) | 🟢 **70.0** | 143.8k | 🚀 +722 | 25 | today | `orchestration` |
| 9 | [Composio](https://github.com/ComposioHQ/composio) | 🟡 **68.8** | 30.0k | 🚀 +131 | 210 | 1 day ago | `tooling` |
| 10 | [LangGraph](https://github.com/langchain-ai/langgraph) | 🟡 **65.8** | 40.9k | 🚀 +442 | 0 | 5 days ago | `orchestration` |
| 11 | [Agno](https://github.com/agno-agi/agno) | 🟡 **64.9** | 42.0k | 📈 +80 | 72 | 1 day ago | `multi-agent` |
| 12 | [DSPy](https://github.com/stanfordnlp/dspy) | 🟡 **63.7** | 37.7k | 🚀 +121 | 61 | 11 days ago | `optimization` |
| 13 | [LlamaIndex](https://github.com/run-llama/llama_index) | 🟡 **63.0** | 52.0k | 🚀 +101 | 38 | 13 days ago | `data-agent` |
| 14 | [AG2](https://github.com/ag2ai/ag2) | 🟡 **60.0** | 4.9k | ↗️ +8 | 53 | 4 days ago | `multi-agent` |
| 15 | [Semantic Kernel](https://github.com/microsoft/semantic-kernel) | 🟡 **53.2** | 28.5k | 📈 +21 | 18 | 14 days ago | `enterprise` |
| 16 | [Letta](https://github.com/letta-ai/letta) | 🟡 **41.2** | 24.6k | 🚀 +121 | 3 | 3 mo ago | `memory` |
| 17 | [Smolagents](https://github.com/huggingface/smolagents) | 🟠 **37.6** | 29.1k | 🚀 +121 | 2 | 3 mo ago | `lightweight` |
| 18 | [AutoGen](https://github.com/microsoft/autogen) | 🟠 **33.7** | 60.8k | 🚀 +123 | 0 | 11 mo ago | `multi-agent` |
| 19 | [Swarm](https://github.com/openai/swarm) | 🔴 **9.2** | 21.9k | ↗️ +11 | 0 | — | `experimental` |

## 📂 By Category

- `data-agent`: **LlamaIndex** (63.0)
- `enterprise`: **Semantic Kernel** (53.2)
- `experimental`: **Swarm** (9.2)
- `lightweight`: **Smolagents** (37.6)
- `memory`: **Letta** (41.2)
- `multi-agent`: **CrewAI** (81.0), **Agno** (64.9), **AG2** (60.0), **AutoGen** (33.7)
- `optimization`: **DSPy** (63.7)
- `orchestration`: **OpenAI Agents SDK** (76.4), **Google ADK** (73.3), **Claude Agent SDK** (70.0), **LangGraph** (65.8)
- `pipeline`: **Haystack** (71.2)
- `structured`: **PydanticAI** (75.2)
- `tooling`: **Composio** (68.8)
- `typescript`: **Mastra** (75.8)
- `web-agent`: **BrowserUse** (89.2)

## 🔍 Top 5 — Score Breakdown

| Framework | Star Velocity | Release Freshness | Issue Health | Commit Activity | Community | Fork Ratio |
|-----------|:---:|:---:|:---:|:---:|:---:|:---:|
| **BrowserUse** | 100 | 94.7 | 92.6 | 100 | 70.2 | 44.0 |
| **CrewAI** | 73.8 | 98.3 | 96.9 | 83.0 | 60.4 | 57.3 |
| **OpenAI Agents SDK** | 35.0 | 95.7 | 98.7 | 100 | 73.6 | 63.9 |
| **Mastra** | 34.3 | 98.7 | 95.2 | 100 | 93.0 | 39.4 |
| **PydanticAI** | 32.8 | 99.7 | 81.5 | 100 | 94.8 | 53.4 |

## 💡 Key Insights

- **Hottest framework**: BrowserUse with a Pulse Score of 89.2
- **Fastest growing**: BrowserUse gained +1485 stars this week
- **Most active development**: Mastra with 1347 commits in the last 4 weeks
- **Stale releases**: AutoGen, Swarm haven't released in a while

## 📦 Recent Releases

- **Claude Agent SDK** [`v2.1.258`](https://github.com/anthropics/claude-code/releases/tag/v2.1.258) — today
- **Agno** [`v3.0.5`](https://github.com/agno-agi/agno/releases/tag/v3.0.5) — 1 day ago
- **PydanticAI** [`v2.37.0`](https://github.com/pydantic/pydantic-ai/releases/tag/v2.37.0) — 1 day ago
- **Composio** [`@composio/cli@0.4.1-beta.373`](https://github.com/ComposioHQ/composio/releases/tag/@composio/cli@0.4.1-beta.373) — 1 day ago *(pre-release)*
- **AG2** [`v1.0.3`](https://github.com/ag2ai/ag2/releases/tag/v1.0.3) — 4 days ago
- **Mastra** [`@mastra/core@1.63.0`](https://github.com/mastra-ai/mastra/releases/tag/@mastra/core@1.63.0) — 4 days ago
- **Google ADK** [`v1.39.1`](https://github.com/google/adk-python/releases/tag/v1.39.1) — 5 days ago
- **LangGraph** [`sdk==0.4.4`](https://github.com/langchain-ai/langgraph/releases/tag/sdk==0.4.4) — 5 days ago
- **CrewAI** [`1.15.18`](https://github.com/crewAIInc/crewAI/releases/tag/1.15.18) — 5 days ago
- **Haystack** [`v3.1.0`](https://github.com/deepset-ai/haystack/releases/tag/v3.1.0) — 8 days ago

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

*Powered by GitHub Actions • Data refreshed daily • Last run: 2026-09-02 10:58 UTC*