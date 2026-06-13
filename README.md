# 🔬 AI Agent Framework Pulse Tracker

[![Daily Update](https://github.com/PurpleHaze2320/ai-agent-pulse/actions/workflows/track.yml/badge.svg)](https://github.com/PurpleHaze2320/ai-agent-pulse/actions/workflows/track.yml)
[![Frameworks Tracked](https://img.shields.io/badge/frameworks-19-blue)](https://github.com/PurpleHaze2320/ai-agent-pulse)
[![License: MIT](https://img.shields.io/badge/License-MIT-green.svg)](https://opensource.org/licenses/MIT)
[![GitHub stars](https://img.shields.io/github/stars/PurpleHaze2320/ai-agent-pulse?style=social)](https://github.com/PurpleHaze2320/ai-agent-pulse/stargazers)

> Automated daily tracking of the AI agent framework ecosystem's health, momentum, and trends.
> Last updated: **2026-06-13 09:24 UTC** | Tracking **19** frameworks

## How It Works

This bot runs daily via GitHub Actions and collects metrics from the GitHub API for the most important
AI agent frameworks. It computes a **Pulse Score** (0-100) based on six weighted signals: star velocity,
release freshness, issue health, commit activity, community size, and fork engagement. The result is
a living dashboard that shows which frameworks are gaining momentum and which are losing steam.

## 🏆 Pulse Leaderboard

| Rank | Framework | Pulse | Stars | ⭐ 7d | Commits (4w) | Last Release | Category |
|------|-----------|-------|-------|-------|--------------|--------------|----------|
| 1 | [CrewAI](https://github.com/crewAIInc/crewAI) | 🟢 **90.7** | 53.4k | 🚀 +487 | 118 | 1 day ago | `multi-agent` |
| 2 | [BrowserUse](https://github.com/browser-use/browser-use) | 🟢 **90.1** | 98.6k | 🚀 +1153 | 444 | today | `web-agent` |
| 3 | [LangGraph](https://github.com/langchain-ai/langgraph) | 🟢 **87.5** | 34.6k | 🚀 +582 | 95 | today | `orchestration` |
| 4 | [Mastra](https://github.com/mastra-ai/mastra) | 🟢 **77.8** | 25.0k | 🚀 +185 | 925 | today | `typescript` |
| 5 | [PydanticAI](https://github.com/pydantic/pydantic-ai) | 🟢 **75.4** | 17.7k | 🚀 +181 | 100 | 2 days ago | `structured` |
| 6 | [Agno](https://github.com/agno-agi/agno) | 🟢 **73.2** | 40.7k | 🚀 +130 | 132 | today | `multi-agent` |
| 7 | [Claude Agent SDK](https://github.com/anthropics/claude-code) | 🟢 **72.9** | 132.1k | 🚀 +1626 | 37 | today | `orchestration` |
| 8 | [Haystack](https://github.com/deepset-ai/haystack) | 🟢 **70.6** | 25.6k | 📈 +93 | 126 | 3 days ago | `pipeline` |
| 9 | [Google ADK](https://github.com/google/adk-python) | 🟢 **70.1** | 20.1k | 📈 +92 | 235 | 3 days ago | `orchestration` |
| 10 | [LlamaIndex](https://github.com/run-llama/llama_index) | 🟡 **66.9** | 50.1k | 🚀 +155 | 53 | 29 days ago | `data-agent` |
| 11 | [OpenAI Agents SDK](https://github.com/openai/openai-agents-python) | 🟡 **62.5** | 27.1k | 🚀 +171 | 37 | 2 days ago | `orchestration` |
| 12 | [DSPy](https://github.com/stanfordnlp/dspy) | 🟡 **58.0** | 35.0k | 🚀 +130 | 43 | 16 days ago | `optimization` |
| 13 | [Composio](https://github.com/ComposioHQ/composio) | 🟡 **53.4** | 28.7k | 📈 +93 | 34 | 3 days ago | `tooling` |
| 14 | [Semantic Kernel](https://github.com/microsoft/semantic-kernel) | 🟡 **52.4** | 28.1k | 📈 +48 | 7 | 9 days ago | `enterprise` |
| 15 | [AG2](https://github.com/ag2ai/ag2) | 🟡 **49.1** | 4.7k | 📈 +29 | 0 | today | `multi-agent` |
| 16 | [Letta](https://github.com/letta-ai/letta) | 🟡 **46.9** | 23.3k | 🚀 +137 | 0 | 29 days ago | `memory` |
| 17 | [Smolagents](https://github.com/huggingface/smolagents) | 🟡 **44.0** | 27.8k | 🚀 +108 | 6 | 15 days ago | `lightweight` |
| 18 | [AutoGen](https://github.com/microsoft/autogen) | 🟡 **40.2** | 58.9k | 🚀 +189 | 0 | 8 mo ago | `multi-agent` |
| 19 | [Swarm](https://github.com/openai/swarm) | 🔴 **9.8** | 21.6k | 📈 +38 | 0 | — | `experimental` |

## 📂 By Category

- `data-agent`: **LlamaIndex** (66.9)
- `enterprise`: **Semantic Kernel** (52.4)
- `experimental`: **Swarm** (9.8)
- `lightweight`: **Smolagents** (44.0)
- `memory`: **Letta** (46.9)
- `multi-agent`: **CrewAI** (90.7), **Agno** (73.2), **AG2** (49.1), **AutoGen** (40.2)
- `optimization`: **DSPy** (58.0)
- `orchestration`: **LangGraph** (87.5), **Claude Agent SDK** (72.9), **Google ADK** (70.1), **OpenAI Agents SDK** (62.5)
- `pipeline`: **Haystack** (70.6)
- `structured`: **PydanticAI** (75.4)
- `tooling`: **Composio** (53.4)
- `typescript`: **Mastra** (77.8)
- `web-agent`: **BrowserUse** (90.1)

## 🔍 Top 5 — Score Breakdown

| Framework | Star Velocity | Release Freshness | Issue Health | Commit Activity | Community | Fork Ratio |
|-----------|:---:|:---:|:---:|:---:|:---:|:---:|
| **CrewAI** | 98.6 | 99.7 | 97.1 | 100 | 59.4 | 56.0 |
| **BrowserUse** | 100 | 100.0 | 95.9 | 100 | 63.0 | 44.6 |
| **LangGraph** | 100 | 100.0 | 75.4 | 95.0 | 55.0 | 67.2 |
| **Mastra** | 42.9 | 100.0 | 95.2 | 100 | 92.0 | 35.6 |
| **PydanticAI** | 35.5 | 99.3 | 82.5 | 100 | 93.2 | 49.9 |

## 💡 Key Insights

- **Hottest framework**: CrewAI with a Pulse Score of 90.7
- **Fastest growing**: Claude Agent SDK gained +1626 stars this week
- **Most active development**: Mastra with 925 commits in the last 4 weeks
- **Stale releases**: Swarm haven't released in a while

## 📦 Recent Releases

- **Claude Agent SDK** [`v2.1.177`](https://github.com/anthropics/claude-code/releases/tag/v2.1.177) — today
- **BrowserUse** [`0.13.2`](https://github.com/browser-use/browser-use/releases/tag/0.13.2) — today
- **AG2** [`v0.13.4`](https://github.com/ag2ai/ag2/releases/tag/v0.13.4) — today
- **LangGraph** [`1.2.5`](https://github.com/langchain-ai/langgraph/releases/tag/1.2.5) — today
- **Agno** [`v2.6.14`](https://github.com/agno-agi/agno/releases/tag/v2.6.14) — today
- **Mastra** [`@mastra/core@1.42.0`](https://github.com/mastra-ai/mastra/releases/tag/@mastra/core@1.42.0) — today
- **CrewAI** [`1.14.7`](https://github.com/crewAIInc/crewAI/releases/tag/1.14.7) — 1 day ago
- **OpenAI Agents SDK** [`v0.17.5`](https://github.com/openai/openai-agents-python/releases/tag/v0.17.5) — 2 days ago
- **PydanticAI** [`v2.0.0b7`](https://github.com/pydantic/pydantic-ai/releases/tag/v2.0.0b7) — 2 days ago *(pre-release)*
- **Google ADK** [`v1.35.0`](https://github.com/google/adk-python/releases/tag/v1.35.0) — 3 days ago

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

*Powered by GitHub Actions • Data refreshed daily • Last run: 2026-06-13 09:24 UTC*