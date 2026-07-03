# 🔬 AI Agent Framework Pulse Tracker

[![Daily Update](https://github.com/PurpleHaze2320/ai-agent-pulse/actions/workflows/track.yml/badge.svg)](https://github.com/PurpleHaze2320/ai-agent-pulse/actions/workflows/track.yml)
[![Frameworks Tracked](https://img.shields.io/badge/frameworks-19-blue)](https://github.com/PurpleHaze2320/ai-agent-pulse)
[![License: MIT](https://img.shields.io/badge/License-MIT-green.svg)](https://opensource.org/licenses/MIT)
[![GitHub stars](https://img.shields.io/github/stars/PurpleHaze2320/ai-agent-pulse?style=social)](https://github.com/PurpleHaze2320/ai-agent-pulse/stargazers)

> Automated daily tracking of the AI agent framework ecosystem's health, momentum, and trends.
> Last updated: **2026-07-03 09:27 UTC** | Tracking **19** frameworks

## How It Works

This bot runs daily via GitHub Actions and collects metrics from the GitHub API for the most important
AI agent frameworks. It computes a **Pulse Score** (0-100) based on six weighted signals: star velocity,
release freshness, issue health, commit activity, community size, and fork engagement. The result is
a living dashboard that shows which frameworks are gaining momentum and which are losing steam.

## 🏆 Pulse Leaderboard

| Rank | Framework | Pulse | Stars | ⭐ 7d | Commits (4w) | Last Release | Category |
|------|-----------|-------|-------|-------|--------------|--------------|----------|
| 1 | [CrewAI](https://github.com/crewAIInc/crewAI) | 🟢 **88.1** | 54.8k | 🚀 +413 | 130 | 1 day ago | `multi-agent` |
| 2 | [BrowserUse](https://github.com/browser-use/browser-use) | 🟢 **83.7** | 102.3k | 🚀 +1559 | 69 | 1 day ago | `web-agent` |
| 3 | [Mastra](https://github.com/mastra-ai/mastra) | 🟢 **81.7** | 25.8k | 🚀 +300 | 992 | 1 day ago | `typescript` |
| 4 | [LangGraph](https://github.com/langchain-ai/langgraph) | 🟢 **76.8** | 36.4k | 🚀 +580 | 44 | 3 days ago | `orchestration` |
| 5 | [Agno](https://github.com/agno-agi/agno) | 🟢 **72.4** | 41.0k | 🚀 +122 | 103 | today | `multi-agent` |
| 6 | [Google ADK](https://github.com/google/adk-python) | 🟢 **72.3** | 20.4k | 🚀 +130 | 356 | 14 days ago | `orchestration` |
| 7 | [Claude Agent SDK](https://github.com/anthropics/claude-code) | 🟢 **71.5** | 135.6k | 🚀 +1098 | 30 | today | `orchestration` |
| 8 | [Haystack](https://github.com/deepset-ai/haystack) | 🟢 **70.2** | 25.8k | 📈 +87 | 181 | 15 days ago | `pipeline` |
| 9 | [Composio](https://github.com/ComposioHQ/composio) | 🟡 **67.2** | 29.1k | 🚀 +104 | 125 | 3 days ago | `tooling` |
| 10 | [LlamaIndex](https://github.com/run-llama/llama_index) | 🟡 **66.3** | 50.6k | 🚀 +206 | 33 | 8 days ago | `data-agent` |
| 11 | [OpenAI Agents SDK](https://github.com/openai/openai-agents-python) | 🟡 **66.2** | 27.6k | 🚀 +181 | 55 | 9 days ago | `orchestration` |
| 12 | [DSPy](https://github.com/stanfordnlp/dspy) | 🟡 **60.3** | 35.8k | 🚀 +371 | 12 | 1 mo ago | `optimization` |
| 13 | [PydanticAI](https://github.com/pydantic/pydantic-ai) | 🟡 **55.9** | 18.2k | 🚀 +171 | 0 | today | `structured` |
| 14 | [Semantic Kernel](https://github.com/microsoft/semantic-kernel) | 🟡 **50.7** | 28.2k | 📈 +51 | 0 | 16 days ago | `enterprise` |
| 15 | [AG2](https://github.com/ag2ai/ag2) | 🟡 **49.6** | 4.7k | ↗️ +17 | 0 | 7 days ago | `multi-agent` |
| 16 | [Letta](https://github.com/letta-ai/letta) | 🟡 **44.2** | 23.6k | 🚀 +103 | 1 | 1 mo ago | `memory` |
| 17 | [Smolagents](https://github.com/huggingface/smolagents) | 🟡 **42.3** | 28.2k | 🚀 +135 | 1 | 1 mo ago | `lightweight` |
| 18 | [AutoGen](https://github.com/microsoft/autogen) | 🟠 **38.4** | 59.5k | 🚀 +188 | 0 | 9 mo ago | `multi-agent` |
| 19 | [Swarm](https://github.com/openai/swarm) | 🔴 **9.6** | 21.8k | 📈 +34 | 0 | — | `experimental` |

## 📂 By Category

- `data-agent`: **LlamaIndex** (66.3)
- `enterprise`: **Semantic Kernel** (50.7)
- `experimental`: **Swarm** (9.6)
- `lightweight`: **Smolagents** (42.3)
- `memory`: **Letta** (44.2)
- `multi-agent`: **CrewAI** (88.1), **Agno** (72.4), **AG2** (49.6), **AutoGen** (38.4)
- `optimization`: **DSPy** (60.3)
- `orchestration`: **LangGraph** (76.8), **Google ADK** (72.3), **Claude Agent SDK** (71.5), **OpenAI Agents SDK** (66.2)
- `pipeline`: **Haystack** (70.2)
- `structured`: **PydanticAI** (55.9)
- `tooling`: **Composio** (67.2)
- `typescript`: **Mastra** (81.7)
- `web-agent`: **BrowserUse** (83.7)

## 🔍 Top 5 — Score Breakdown

| Framework | Star Velocity | Release Freshness | Issue Health | Commit Activity | Community | Fork Ratio |
|-----------|:---:|:---:|:---:|:---:|:---:|:---:|
| **CrewAI** | 89.0 | 99.7 | 95.6 | 100 | 59.6 | 56.1 |
| **BrowserUse** | 100 | 99.7 | 95.2 | 69.0 | 63.0 | 44.4 |
| **Mastra** | 58.0 | 99.7 | 95.6 | 100 | 92.6 | 36.4 |
| **LangGraph** | 100 | 99.0 | 73.7 | 44.0 | 55.0 | 66.9 |
| **Agno** | 24.4 | 100.0 | 79.9 | 100 | 88.8 | 54.5 |

## 💡 Key Insights

- **Hottest framework**: CrewAI with a Pulse Score of 88.1
- **Fastest growing**: BrowserUse gained +1559 stars this week
- **Most active development**: Mastra with 992 commits in the last 4 weeks
- **Stale releases**: AutoGen, Swarm haven't released in a while

## 📦 Recent Releases

- **PydanticAI** [`v2.4.0`](https://github.com/pydantic/pydantic-ai/releases/tag/v2.4.0) — today
- **Claude Agent SDK** [`v2.1.199`](https://github.com/anthropics/claude-code/releases/tag/v2.1.199) — today
- **Agno** [`v2.6.21`](https://github.com/agno-agi/agno/releases/tag/v2.6.21) — today
- **CrewAI** [`1.15.2a2`](https://github.com/crewAIInc/crewAI/releases/tag/1.15.2a2) — 1 day ago *(pre-release)*
- **Mastra** [`@mastra/core@1.48.0`](https://github.com/mastra-ai/mastra/releases/tag/@mastra/core@1.48.0) — 1 day ago
- **BrowserUse** [`0.13.3`](https://github.com/browser-use/browser-use/releases/tag/0.13.3) — 1 day ago
- **LangGraph** [`1.2.7`](https://github.com/langchain-ai/langgraph/releases/tag/1.2.7) — 3 days ago
- **Composio** [`@composio/cli@0.2.32-beta.280`](https://github.com/ComposioHQ/composio/releases/tag/@composio/cli@0.2.32-beta.280) — 3 days ago *(pre-release)*
- **AG2** [`v0.14.0`](https://github.com/ag2ai/ag2/releases/tag/v0.14.0) — 7 days ago
- **LlamaIndex** [`v0.14.23`](https://github.com/run-llama/llama_index/releases/tag/v0.14.23) — 8 days ago

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

*Powered by GitHub Actions • Data refreshed daily • Last run: 2026-07-03 09:27 UTC*