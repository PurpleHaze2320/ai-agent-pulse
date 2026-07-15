# 🔬 AI Agent Framework Pulse Tracker

[![Daily Update](https://github.com/PurpleHaze2320/ai-agent-pulse/actions/workflows/track.yml/badge.svg)](https://github.com/PurpleHaze2320/ai-agent-pulse/actions/workflows/track.yml)
[![Frameworks Tracked](https://img.shields.io/badge/frameworks-19-blue)](https://github.com/PurpleHaze2320/ai-agent-pulse)
[![License: MIT](https://img.shields.io/badge/License-MIT-green.svg)](https://opensource.org/licenses/MIT)
[![GitHub stars](https://img.shields.io/github/stars/PurpleHaze2320/ai-agent-pulse?style=social)](https://github.com/PurpleHaze2320/ai-agent-pulse/stargazers)

> Automated daily tracking of the AI agent framework ecosystem's health, momentum, and trends.
> Last updated: **2026-07-15 08:23 UTC** | Tracking **19** frameworks

## How It Works

This bot runs daily via GitHub Actions and collects metrics from the GitHub API for the most important
AI agent frameworks. It computes a **Pulse Score** (0-100) based on six weighted signals: star velocity,
release freshness, issue health, commit activity, community size, and fork engagement. The result is
a living dashboard that shows which frameworks are gaining momentum and which are losing steam.

## 🏆 Pulse Leaderboard

| Rank | Framework | Pulse | Stars | ⭐ 7d | Commits (4w) | Last Release | Category |
|------|-----------|-------|-------|-------|--------------|--------------|----------|
| 1 | [CrewAI](https://github.com/crewAIInc/crewAI) | 🟢 **84.7** | 55.6k | 🚀 +420 | 86 | 7 days ago | `multi-agent` |
| 2 | [BrowserUse](https://github.com/browser-use/browser-use) | 🟢 **84.1** | 104.8k | 🚀 +1387 | 72 | 3 days ago | `web-agent` |
| 3 | [PydanticAI](https://github.com/pydantic/pydantic-ai) | 🟢 **79.7** | 18.5k | 🚀 +266 | 234 | today | `structured` |
| 4 | [Mastra](https://github.com/mastra-ai/mastra) | 🟢 **79.6** | 26.2k | 🚀 +247 | 1062 | 6 days ago | `typescript` |
| 5 | [OpenAI Agents SDK](https://github.com/openai/openai-agents-python) | 🟢 **76.2** | 27.9k | 🚀 +190 | 110 | 4 days ago | `orchestration` |
| 6 | [LangGraph](https://github.com/langchain-ai/langgraph) | 🟢 **75.6** | 37.3k | 🚀 +558 | 39 | 5 days ago | `orchestration` |
| 7 | [Agno](https://github.com/agno-agi/agno) | 🟢 **72.4** | 41.2k | 🚀 +120 | 130 | today | `multi-agent` |
| 8 | [Google ADK](https://github.com/google/adk-python) | 🟢 **72.4** | 20.6k | 📈 +99 | 302 | 7 days ago | `orchestration` |
| 9 | [Claude Agent SDK](https://github.com/anthropics/claude-code) | 🟢 **70.3** | 137.9k | 🚀 +1136 | 25 | today | `orchestration` |
| 10 | [Haystack](https://github.com/deepset-ai/haystack) | 🟡 **69.7** | 25.9k | 📈 +53 | 211 | 6 days ago | `pipeline` |
| 11 | [Composio](https://github.com/ComposioHQ/composio) | 🟡 **67.5** | 29.2k | 🚀 +105 | 154 | today | `tooling` |
| 12 | [AG2](https://github.com/ag2ai/ag2) | 🟡 **62.5** | 4.8k | 📈 +26 | 64 | 11 days ago | `multi-agent` |
| 13 | [LlamaIndex](https://github.com/run-llama/llama_index) | 🟡 **56.4** | 50.9k | 🚀 +138 | 0 | 20 days ago | `data-agent` |
| 14 | [Semantic Kernel](https://github.com/microsoft/semantic-kernel) | 🟡 **53.9** | 28.3k | 📈 +30 | 17 | 7 days ago | `enterprise` |
| 15 | [DSPy](https://github.com/stanfordnlp/dspy) | 🟡 **52.3** | 36.1k | 🚀 +218 | 0 | 1 mo ago | `optimization` |
| 16 | [Letta](https://github.com/letta-ai/letta) | 🟡 **42.8** | 23.8k | 📈 +99 | 0 | 2 mo ago | `memory` |
| 17 | [Smolagents](https://github.com/huggingface/smolagents) | 🟡 **41.5** | 28.4k | 🚀 +115 | 4 | 1 mo ago | `lightweight` |
| 18 | [AutoGen](https://github.com/microsoft/autogen) | 🟠 **36.7** | 59.7k | 🚀 +167 | 0 | 9 mo ago | `multi-agent` |
| 19 | [Swarm](https://github.com/openai/swarm) | 🔴 **9.2** | 21.8k | 📈 +25 | 0 | — | `experimental` |

## 📂 By Category

- `data-agent`: **LlamaIndex** (56.4)
- `enterprise`: **Semantic Kernel** (53.9)
- `experimental`: **Swarm** (9.2)
- `lightweight`: **Smolagents** (41.5)
- `memory`: **Letta** (42.8)
- `multi-agent`: **CrewAI** (84.7), **Agno** (72.4), **AG2** (62.5), **AutoGen** (36.7)
- `optimization`: **DSPy** (52.3)
- `orchestration`: **OpenAI Agents SDK** (76.2), **LangGraph** (75.6), **Google ADK** (72.4), **Claude Agent SDK** (70.3)
- `pipeline`: **Haystack** (69.7)
- `structured`: **PydanticAI** (79.7)
- `tooling`: **Composio** (67.5)
- `typescript`: **Mastra** (79.6)
- `web-agent`: **BrowserUse** (84.1)

## 🔍 Top 5 — Score Breakdown

| Framework | Star Velocity | Release Freshness | Issue Health | Commit Activity | Community | Fork Ratio |
|-----------|:---:|:---:|:---:|:---:|:---:|:---:|
| **CrewAI** | 88.1 | 97.7 | 95.8 | 86.0 | 59.6 | 56.4 |
| **BrowserUse** | 100 | 99.0 | 94.8 | 72.0 | 63.0 | 44.1 |
| **PydanticAI** | 48.8 | 100.0 | 85.9 | 100 | 94.8 | 51.0 |
| **Mastra** | 51.0 | 98.0 | 95.2 | 100 | 92.6 | 37.0 |
| **OpenAI Agents SDK** | 37.9 | 98.7 | 98.1 | 100 | 60.6 | 62.0 |

## 💡 Key Insights

- **Hottest framework**: CrewAI with a Pulse Score of 84.7
- **Fastest growing**: BrowserUse gained +1387 stars this week
- **Most active development**: Mastra with 1062 commits in the last 4 weeks
- **Stale releases**: AutoGen, Swarm haven't released in a while

## 📦 Recent Releases

- **Composio** [`@composio/cli@0.2.32`](https://github.com/ComposioHQ/composio/releases/tag/@composio/cli@0.2.32) — today
- **PydanticAI** [`v2.10.0`](https://github.com/pydantic/pydantic-ai/releases/tag/v2.10.0) — today
- **Claude Agent SDK** [`v2.1.210`](https://github.com/anthropics/claude-code/releases/tag/v2.1.210) — today
- **Agno** [`v2.7.3`](https://github.com/agno-agi/agno/releases/tag/v2.7.3) — today
- **BrowserUse** [`0.13.4`](https://github.com/browser-use/browser-use/releases/tag/0.13.4) — 3 days ago
- **OpenAI Agents SDK** [`v0.18.2`](https://github.com/openai/openai-agents-python/releases/tag/v0.18.2) — 4 days ago
- **LangGraph** [`1.2.9`](https://github.com/langchain-ai/langgraph/releases/tag/1.2.9) — 5 days ago
- **Mastra** [`@mastra/core@1.50.0`](https://github.com/mastra-ai/mastra/releases/tag/@mastra/core@1.50.0) — 6 days ago
- **Haystack** [`v2.31.0`](https://github.com/deepset-ai/haystack/releases/tag/v2.31.0) — 6 days ago
- **CrewAI** [`1.15.2`](https://github.com/crewAIInc/crewAI/releases/tag/1.15.2) — 7 days ago

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

*Powered by GitHub Actions • Data refreshed daily • Last run: 2026-07-15 08:23 UTC*