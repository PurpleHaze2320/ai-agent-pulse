# 🔬 AI Agent Framework Pulse Tracker

[![Daily Update](https://github.com/PurpleHaze2320/ai-agent-pulse/actions/workflows/track.yml/badge.svg)](https://github.com/PurpleHaze2320/ai-agent-pulse/actions/workflows/track.yml)
[![Frameworks Tracked](https://img.shields.io/badge/frameworks-19-blue)](https://github.com/PurpleHaze2320/ai-agent-pulse)
[![License: MIT](https://img.shields.io/badge/License-MIT-green.svg)](https://opensource.org/licenses/MIT)
[![GitHub stars](https://img.shields.io/github/stars/PurpleHaze2320/ai-agent-pulse?style=social)](https://github.com/PurpleHaze2320/ai-agent-pulse/stargazers)

> Automated daily tracking of the AI agent framework ecosystem's health, momentum, and trends.
> Last updated: **2026-07-11 08:04 UTC** | Tracking **19** frameworks

## How It Works

This bot runs daily via GitHub Actions and collects metrics from the GitHub API for the most important
AI agent frameworks. It computes a **Pulse Score** (0-100) based on six weighted signals: star velocity,
release freshness, issue health, commit activity, community size, and fork engagement. The result is
a living dashboard that shows which frameworks are gaining momentum and which are losing steam.

## 🏆 Pulse Leaderboard

| Rank | Framework | Pulse | Stars | ⭐ 7d | Commits (4w) | Last Release | Category |
|------|-----------|-------|-------|-------|--------------|--------------|----------|
| 1 | [CrewAI](https://github.com/crewAIInc/crewAI) | 🟢 **89.7** | 55.3k | 🚀 +462 | 112 | 3 days ago | `multi-agent` |
| 2 | [BrowserUse](https://github.com/browser-use/browser-use) | 🟢 **84.4** | 104.2k | 🚀 +1589 | 72 | today | `web-agent` |
| 3 | [Mastra](https://github.com/mastra-ai/mastra) | 🟢 **79.5** | 26.0k | 🚀 +239 | 1075 | 2 days ago | `typescript` |
| 4 | [LangGraph](https://github.com/langchain-ai/langgraph) | 🟢 **78.3** | 37.0k | 🚀 +571 | 51 | 1 day ago | `orchestration` |
| 5 | [OpenAI Agents SDK](https://github.com/openai/openai-agents-python) | 🟢 **75.4** | 27.8k | 🚀 +166 | 110 | today | `orchestration` |
| 6 | [Google ADK](https://github.com/google/adk-python) | 🟢 **73.2** | 20.6k | 🚀 +122 | 373 | 3 days ago | `orchestration` |
| 7 | [Claude Agent SDK](https://github.com/anthropics/claude-code) | 🟢 **71.4** | 137.4k | 🚀 +1395 | 30 | today | `orchestration` |
| 8 | [Composio](https://github.com/ComposioHQ/composio) | 🟡 **66.6** | 29.2k | 📈 +86 | 146 | 3 days ago | `tooling` |
| 9 | [LlamaIndex](https://github.com/run-llama/llama_index) | 🟡 **62.0** | 50.8k | 🚀 +143 | 26 | 16 days ago | `data-agent` |
| 10 | [PydanticAI](https://github.com/pydantic/pydantic-ai) | 🟡 **56.6** | 18.4k | 🚀 +188 | 0 | today | `structured` |
| 11 | [DSPy](https://github.com/stanfordnlp/dspy) | 🟡 **52.4** | 36.0k | 🚀 +219 | 0 | 1 mo ago | `optimization` |
| 12 | [Agno](https://github.com/agno-agi/agno) | 🟡 **51.6** | 41.1k | 🚀 +101 | 0 | 1 day ago | `multi-agent` |
| 13 | [Semantic Kernel](https://github.com/microsoft/semantic-kernel) | 🟡 **51.1** | 28.3k | 📈 +38 | 0 | 3 days ago | `enterprise` |
| 14 | [AG2](https://github.com/ag2ai/ag2) | 🟡 **49.8** | 4.8k | 📈 +24 | 0 | 7 days ago | `multi-agent` |
| 15 | [Haystack](https://github.com/deepset-ai/haystack) | 🟡 **49.6** | 25.9k | 📈 +44 | 0 | 2 days ago | `pipeline` |
| 16 | [Letta](https://github.com/letta-ai/letta) | 🟡 **43.0** | 23.7k | 📈 +95 | 0 | 1 mo ago | `memory` |
| 17 | [Smolagents](https://github.com/huggingface/smolagents) | 🟡 **41.7** | 28.3k | 🚀 +116 | 4 | 1 mo ago | `lightweight` |
| 18 | [AutoGen](https://github.com/microsoft/autogen) | 🟠 **37.1** | 59.6k | 🚀 +168 | 0 | 9 mo ago | `multi-agent` |
| 19 | [Swarm](https://github.com/openai/swarm) | 🔴 **9.2** | 21.8k | 📈 +23 | 0 | — | `experimental` |

## 📂 By Category

- `data-agent`: **LlamaIndex** (62.0)
- `enterprise`: **Semantic Kernel** (51.1)
- `experimental`: **Swarm** (9.2)
- `lightweight`: **Smolagents** (41.7)
- `memory`: **Letta** (43.0)
- `multi-agent`: **CrewAI** (89.7), **Agno** (51.6), **AG2** (49.8), **AutoGen** (37.1)
- `optimization`: **DSPy** (52.4)
- `orchestration`: **LangGraph** (78.3), **OpenAI Agents SDK** (75.4), **Google ADK** (73.2), **Claude Agent SDK** (71.4)
- `pipeline`: **Haystack** (49.6)
- `structured`: **PydanticAI** (56.6)
- `tooling`: **Composio** (66.6)
- `typescript`: **Mastra** (79.5)
- `web-agent`: **BrowserUse** (84.4)

## 🔍 Top 5 — Score Breakdown

| Framework | Star Velocity | Release Freshness | Issue Health | Commit Activity | Community | Fork Ratio |
|-----------|:---:|:---:|:---:|:---:|:---:|:---:|
| **CrewAI** | 95.8 | 99.0 | 95.8 | 100 | 59.6 | 56.3 |
| **BrowserUse** | 100 | 100.0 | 95.0 | 72.0 | 63.0 | 44.1 |
| **Mastra** | 49.6 | 99.3 | 95.1 | 100 | 92.6 | 36.8 |
| **LangGraph** | 100 | 99.7 | 73.1 | 51.0 | 55.0 | 67.1 |
| **OpenAI Agents SDK** | 34.1 | 100.0 | 98.0 | 100 | 59.8 | 61.8 |

## 💡 Key Insights

- **Hottest framework**: CrewAI with a Pulse Score of 89.7
- **Fastest growing**: BrowserUse gained +1589 stars this week
- **Most active development**: Mastra with 1075 commits in the last 4 weeks
- **Stale releases**: AutoGen, Swarm haven't released in a while

## 📦 Recent Releases

- **PydanticAI** [`v2.9.0`](https://github.com/pydantic/pydantic-ai/releases/tag/v2.9.0) — today
- **OpenAI Agents SDK** [`v0.18.2`](https://github.com/openai/openai-agents-python/releases/tag/v0.18.2) — today
- **Claude Agent SDK** [`v2.1.207`](https://github.com/anthropics/claude-code/releases/tag/v2.1.207) — today
- **BrowserUse** [`0.13.4`](https://github.com/browser-use/browser-use/releases/tag/0.13.4) — today
- **LangGraph** [`1.2.9`](https://github.com/langchain-ai/langgraph/releases/tag/1.2.9) — 1 day ago
- **Agno** [`v2.7.2`](https://github.com/agno-agi/agno/releases/tag/v2.7.2) — 1 day ago
- **Mastra** [`@mastra/core@1.50.0`](https://github.com/mastra-ai/mastra/releases/tag/@mastra/core@1.50.0) — 2 days ago
- **Haystack** [`v2.31.0`](https://github.com/deepset-ai/haystack/releases/tag/v2.31.0) — 2 days ago
- **CrewAI** [`1.15.2`](https://github.com/crewAIInc/crewAI/releases/tag/1.15.2) — 3 days ago
- **Google ADK** [`v2.4.0`](https://github.com/google/adk-python/releases/tag/v2.4.0) — 3 days ago

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

*Powered by GitHub Actions • Data refreshed daily • Last run: 2026-07-11 08:04 UTC*