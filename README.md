# 🔬 AI Agent Framework Pulse Tracker

[![Daily Update](https://github.com/PurpleHaze2320/ai-agent-pulse/actions/workflows/track.yml/badge.svg)](https://github.com/PurpleHaze2320/ai-agent-pulse/actions/workflows/track.yml)
[![Frameworks Tracked](https://img.shields.io/badge/frameworks-19-blue)](https://github.com/PurpleHaze2320/ai-agent-pulse)
[![License: MIT](https://img.shields.io/badge/License-MIT-green.svg)](https://opensource.org/licenses/MIT)
[![GitHub stars](https://img.shields.io/github/stars/PurpleHaze2320/ai-agent-pulse?style=social)](https://github.com/PurpleHaze2320/ai-agent-pulse/stargazers)

> Automated daily tracking of the AI agent framework ecosystem's health, momentum, and trends.
> Last updated: **2026-06-07 09:23 UTC** | Tracking **19** frameworks

## How It Works

This bot runs daily via GitHub Actions and collects metrics from the GitHub API for the most important
AI agent frameworks. It computes a **Pulse Score** (0-100) based on six weighted signals: star velocity,
release freshness, issue health, commit activity, community size, and fork engagement. The result is
a living dashboard that shows which frameworks are gaining momentum and which are losing steam.

## 🏆 Pulse Leaderboard

| Rank | Framework | Pulse | Stars | ⭐ 7d | Commits (4w) | Last Release | Category |
|------|-----------|-------|-------|-------|--------------|--------------|----------|
| 1 | [BrowserUse](https://github.com/browser-use/browser-use) | 🟢 **89.3** | 97.5k | 🚀 +1187 | 414 | 12 days ago | `web-agent` |
| 2 | [CrewAI](https://github.com/crewAIInc/crewAI) | 🟢 **86.2** | 53.0k | 🚀 +458 | 81 | 1 day ago | `multi-agent` |
| 3 | [LangGraph](https://github.com/langchain-ai/langgraph) | 🟢 **85.2** | 34.1k | 🚀 +635 | 84 | 4 days ago | `orchestration` |
| 4 | [Mastra](https://github.com/mastra-ai/mastra) | 🟢 **80.7** | 24.8k | 🚀 +266 | 752 | 2 days ago | `typescript` |
| 5 | [Agno](https://github.com/agno-agi/agno) | 🟢 **72.9** | 40.6k | 🚀 +122 | 113 | 1 day ago | `multi-agent` |
| 6 | [Claude Agent SDK](https://github.com/anthropics/claude-code) | 🟢 **71.4** | 130.8k | 🚀 +2208 | 29 | today | `orchestration` |
| 7 | [PydanticAI](https://github.com/pydantic/pydantic-ai) | 🟢 **70.0** | 17.6k | 🚀 +169 | 76 | 2 days ago | `structured` |
| 8 | [Google ADK](https://github.com/google/adk-python) | 🟡 **69.5** | 20.0k | 📈 +75 | 140 | 2 days ago | `orchestration` |
| 9 | [Haystack](https://github.com/deepset-ai/haystack) | 🟡 **68.3** | 25.5k | 📈 +55 | 95 | 3 days ago | `pipeline` |
| 10 | [LlamaIndex](https://github.com/run-llama/llama_index) | 🟡 **66.4** | 50.0k | 🚀 +174 | 45 | 23 days ago | `data-agent` |
| 11 | [OpenAI Agents SDK](https://github.com/openai/openai-agents-python) | 🟡 **61.0** | 27.0k | 🚀 +181 | 29 | 12 days ago | `orchestration` |
| 12 | [DSPy](https://github.com/stanfordnlp/dspy) | 🟡 **57.3** | 34.9k | 🚀 +151 | 33 | 10 days ago | `optimization` |
| 13 | [Semantic Kernel](https://github.com/microsoft/semantic-kernel) | 🟡 **52.7** | 28.1k | 📈 +53 | 6 | 3 days ago | `enterprise` |
| 14 | [Composio](https://github.com/ComposioHQ/composio) | 🟡 **51.8** | 28.7k | 🚀 +133 | 23 | 18 days ago | `tooling` |
| 15 | [AG2](https://github.com/ag2ai/ag2) | 🟡 **48.7** | 4.6k | 📈 +25 | 0 | 2 days ago | `multi-agent` |
| 16 | [Letta](https://github.com/letta-ai/letta) | 🟡 **47.3** | 23.2k | 🚀 +133 | 0 | 23 days ago | `memory` |
| 17 | [Smolagents](https://github.com/huggingface/smolagents) | 🟡 **45.0** | 27.7k | 🚀 +123 | 6 | 9 days ago | `lightweight` |
| 18 | [AutoGen](https://github.com/microsoft/autogen) | 🟡 **40.7** | 58.7k | 🚀 +188 | 0 | 8 mo ago | `multi-agent` |
| 19 | [Swarm](https://github.com/openai/swarm) | 🔴 **9.2** | 21.6k | 📈 +31 | 0 | — | `experimental` |

## 📂 By Category

- `data-agent`: **LlamaIndex** (66.4)
- `enterprise`: **Semantic Kernel** (52.7)
- `experimental`: **Swarm** (9.2)
- `lightweight`: **Smolagents** (45.0)
- `memory`: **Letta** (47.3)
- `multi-agent`: **CrewAI** (86.2), **Agno** (72.9), **AG2** (48.7), **AutoGen** (40.7)
- `optimization`: **DSPy** (57.3)
- `orchestration`: **LangGraph** (85.2), **Claude Agent SDK** (71.4), **Google ADK** (69.5), **OpenAI Agents SDK** (61.0)
- `pipeline`: **Haystack** (68.3)
- `structured`: **PydanticAI** (70.0)
- `tooling`: **Composio** (51.8)
- `typescript`: **Mastra** (80.7)
- `web-agent`: **BrowserUse** (89.3)

## 🔍 Top 5 — Score Breakdown

| Framework | Star Velocity | Release Freshness | Issue Health | Commit Activity | Community | Fork Ratio |
|-----------|:---:|:---:|:---:|:---:|:---:|:---:|
| **BrowserUse** | 100 | 96.0 | 95.8 | 100 | 63.0 | 44.7 |
| **CrewAI** | 95.4 | 99.7 | 97.9 | 81.0 | 59.4 | 55.9 |
| **LangGraph** | 100 | 98.7 | 76.0 | 84.0 | 55.0 | 67.3 |
| **Mastra** | 54.9 | 99.3 | 95.6 | 100 | 92.2 | 35.5 |
| **Agno** | 25.6 | 99.7 | 82.0 | 100 | 89.0 | 54.1 |

## 💡 Key Insights

- **Hottest framework**: BrowserUse with a Pulse Score of 89.3
- **Fastest growing**: Claude Agent SDK gained +2208 stars this week
- **Most active development**: Mastra with 752 commits in the last 4 weeks
- **Stale releases**: Swarm haven't released in a while

## 📦 Recent Releases

- **Claude Agent SDK** [`v2.1.168`](https://github.com/anthropics/claude-code/releases/tag/v2.1.168) — today
- **CrewAI** [`1.14.7a2`](https://github.com/crewAIInc/crewAI/releases/tag/1.14.7a2) — 1 day ago *(pre-release)*
- **Agno** [`v2.6.12`](https://github.com/agno-agi/agno/releases/tag/v2.6.12) — 1 day ago
- **Mastra** [`@mastra/core@1.41.0`](https://github.com/mastra-ai/mastra/releases/tag/@mastra/core@1.41.0) — 2 days ago
- **AG2** [`v0.13.3`](https://github.com/ag2ai/ag2/releases/tag/v0.13.3) — 2 days ago
- **PydanticAI** [`v2.0.0b6`](https://github.com/pydantic/pydantic-ai/releases/tag/v2.0.0b6) — 2 days ago *(pre-release)*
- **Google ADK** [`v2.2.0`](https://github.com/google/adk-python/releases/tag/v2.2.0) — 2 days ago
- **Semantic Kernel** [`python-1.43.0`](https://github.com/microsoft/semantic-kernel/releases/tag/python-1.43.0) — 3 days ago
- **Haystack** [`v2.30.0`](https://github.com/deepset-ai/haystack/releases/tag/v2.30.0) — 3 days ago
- **LangGraph** [`1.2.4`](https://github.com/langchain-ai/langgraph/releases/tag/1.2.4) — 4 days ago

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

*Powered by GitHub Actions • Data refreshed daily • Last run: 2026-06-07 09:23 UTC*