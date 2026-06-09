# 🔬 AI Agent Framework Pulse Tracker

[![Daily Update](https://github.com/PurpleHaze2320/ai-agent-pulse/actions/workflows/track.yml/badge.svg)](https://github.com/PurpleHaze2320/ai-agent-pulse/actions/workflows/track.yml)
[![Frameworks Tracked](https://img.shields.io/badge/frameworks-19-blue)](https://github.com/PurpleHaze2320/ai-agent-pulse)
[![License: MIT](https://img.shields.io/badge/License-MIT-green.svg)](https://opensource.org/licenses/MIT)
[![GitHub stars](https://img.shields.io/github/stars/PurpleHaze2320/ai-agent-pulse?style=social)](https://github.com/PurpleHaze2320/ai-agent-pulse/stargazers)

> Automated daily tracking of the AI agent framework ecosystem's health, momentum, and trends.
> Last updated: **2026-06-09 09:55 UTC** | Tracking **19** frameworks

## How It Works

This bot runs daily via GitHub Actions and collects metrics from the GitHub API for the most important
AI agent frameworks. It computes a **Pulse Score** (0-100) based on six weighted signals: star velocity,
release freshness, issue health, commit activity, community size, and fork engagement. The result is
a living dashboard that shows which frameworks are gaining momentum and which are losing steam.

## 🏆 Pulse Leaderboard

| Rank | Framework | Pulse | Stars | ⭐ 7d | Commits (4w) | Last Release | Category |
|------|-----------|-------|-------|-------|--------------|--------------|----------|
| 1 | [CrewAI](https://github.com/crewAIInc/crewAI) | 🟢 **87.7** | 53.1k | 🚀 +466 | 87 | today | `multi-agent` |
| 2 | [Mastra](https://github.com/mastra-ai/mastra) | 🟢 **79.4** | 24.9k | 🚀 +236 | 788 | 4 days ago | `typescript` |
| 3 | [Agno](https://github.com/agno-agi/agno) | 🟢 **73.4** | 40.6k | 🚀 +140 | 115 | 3 days ago | `multi-agent` |
| 4 | [Claude Agent SDK](https://github.com/anthropics/claude-code) | 🟢 **71.6** | 131.2k | 🚀 +1729 | 30 | today | `orchestration` |
| 5 | [PydanticAI](https://github.com/pydantic/pydantic-ai) | 🟢 **70.6** | 17.6k | 🚀 +181 | 77 | 4 days ago | `structured` |
| 6 | [BrowserUse](https://github.com/browser-use/browser-use) | 🟢 **70.1** | 97.9k | 🚀 +1232 | 0 | today | `web-agent` |
| 7 | [Google ADK](https://github.com/google/adk-python) | 🟡 **69.5** | 20.0k | 📈 +77 | 147 | 4 days ago | `orchestration` |
| 8 | [LangGraph](https://github.com/langchain-ai/langgraph) | 🟡 **68.2** | 34.2k | 🚀 +611 | 0 | 6 days ago | `orchestration` |
| 9 | [LlamaIndex](https://github.com/run-llama/llama_index) | 🟡 **66.6** | 50.0k | 🚀 +180 | 45 | 25 days ago | `data-agent` |
| 10 | [OpenAI Agents SDK](https://github.com/openai/openai-agents-python) | 🟡 **60.7** | 27.0k | 🚀 +167 | 31 | 14 days ago | `orchestration` |
| 11 | [DSPy](https://github.com/stanfordnlp/dspy) | 🟡 **57.7** | 34.9k | 🚀 +165 | 33 | 12 days ago | `optimization` |
| 12 | [Semantic Kernel](https://github.com/microsoft/semantic-kernel) | 🟡 **52.8** | 28.1k | 📈 +53 | 7 | 5 days ago | `enterprise` |
| 13 | [Haystack](https://github.com/deepset-ai/haystack) | 🟡 **49.6** | 25.5k | 📈 +64 | 0 | 5 days ago | `pipeline` |
| 14 | [AG2](https://github.com/ag2ai/ag2) | 🟡 **48.7** | 4.7k | 📈 +27 | 0 | 4 days ago | `multi-agent` |
| 15 | [Composio](https://github.com/ComposioHQ/composio) | 🟡 **48.0** | 28.7k | 🚀 +121 | 0 | today | `tooling` |
| 16 | [Letta](https://github.com/letta-ai/letta) | 🟡 **47.1** | 23.2k | 🚀 +132 | 0 | 25 days ago | `memory` |
| 17 | [Smolagents](https://github.com/huggingface/smolagents) | 🟡 **44.2** | 27.8k | 🚀 +104 | 6 | 11 days ago | `lightweight` |
| 18 | [AutoGen](https://github.com/microsoft/autogen) | 🟠 **39.8** | 58.8k | 🚀 +166 | 0 | 8 mo ago | `multi-agent` |
| 19 | [Swarm](https://github.com/openai/swarm) | 🔴 **10.0** | 21.6k | 📈 +38 | 0 | — | `experimental` |

## 📂 By Category

- `data-agent`: **LlamaIndex** (66.6)
- `enterprise`: **Semantic Kernel** (52.8)
- `experimental`: **Swarm** (10.0)
- `lightweight`: **Smolagents** (44.2)
- `memory`: **Letta** (47.1)
- `multi-agent`: **CrewAI** (87.7), **Agno** (73.4), **AG2** (48.7), **AutoGen** (39.8)
- `optimization`: **DSPy** (57.7)
- `orchestration`: **Claude Agent SDK** (71.6), **Google ADK** (69.5), **LangGraph** (68.2), **OpenAI Agents SDK** (60.7)
- `pipeline`: **Haystack** (49.6)
- `structured`: **PydanticAI** (70.6)
- `tooling`: **Composio** (48.0)
- `typescript`: **Mastra** (79.4)
- `web-agent`: **BrowserUse** (70.1)

## 🔍 Top 5 — Score Breakdown

| Framework | Star Velocity | Release Freshness | Issue Health | Commit Activity | Community | Fork Ratio |
|-----------|:---:|:---:|:---:|:---:|:---:|:---:|
| **CrewAI** | 96.4 | 100.0 | 97.7 | 87.0 | 59.4 | 55.9 |
| **Mastra** | 50.5 | 98.7 | 95.5 | 100 | 92.2 | 35.4 |
| **Agno** | 28.1 | 99.0 | 81.8 | 100 | 89.0 | 54.1 |
| **Claude Agent SDK** | 100 | 100.0 | 87.5 | 30.0 | 10.2 | 64.8 |
| **PydanticAI** | 35.5 | 98.7 | 82.4 | 77.0 | 92.2 | 49.8 |

## 💡 Key Insights

- **Hottest framework**: CrewAI with a Pulse Score of 87.7
- **Fastest growing**: Claude Agent SDK gained +1729 stars this week
- **Most active development**: Mastra with 788 commits in the last 4 weeks
- **Stale releases**: Swarm haven't released in a while

## 📦 Recent Releases

- **Composio** [`@composio/cli@0.2.31`](https://github.com/ComposioHQ/composio/releases/tag/@composio/cli@0.2.31) — today
- **CrewAI** [`1.14.7a3`](https://github.com/crewAIInc/crewAI/releases/tag/1.14.7a3) — today *(pre-release)*
- **BrowserUse** [`0.13.0`](https://github.com/browser-use/browser-use/releases/tag/0.13.0) — today
- **Claude Agent SDK** [`v2.1.169`](https://github.com/anthropics/claude-code/releases/tag/v2.1.169) — today
- **Agno** [`v2.6.12`](https://github.com/agno-agi/agno/releases/tag/v2.6.12) — 3 days ago
- **Mastra** [`@mastra/core@1.41.0`](https://github.com/mastra-ai/mastra/releases/tag/@mastra/core@1.41.0) — 4 days ago
- **AG2** [`v0.13.3`](https://github.com/ag2ai/ag2/releases/tag/v0.13.3) — 4 days ago
- **PydanticAI** [`v2.0.0b6`](https://github.com/pydantic/pydantic-ai/releases/tag/v2.0.0b6) — 4 days ago *(pre-release)*
- **Google ADK** [`v2.2.0`](https://github.com/google/adk-python/releases/tag/v2.2.0) — 4 days ago
- **Semantic Kernel** [`python-1.43.0`](https://github.com/microsoft/semantic-kernel/releases/tag/python-1.43.0) — 5 days ago

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

*Powered by GitHub Actions • Data refreshed daily • Last run: 2026-06-09 09:55 UTC*