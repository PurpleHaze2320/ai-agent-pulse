# 🔬 AI Agent Framework Pulse Tracker

[![Daily Update](https://github.com/PurpleHaze2320/ai-agent-pulse/actions/workflows/track.yml/badge.svg)](https://github.com/PurpleHaze2320/ai-agent-pulse/actions/workflows/track.yml)
[![Frameworks Tracked](https://img.shields.io/badge/frameworks-19-blue)](https://github.com/PurpleHaze2320/ai-agent-pulse)
[![License: MIT](https://img.shields.io/badge/License-MIT-green.svg)](https://opensource.org/licenses/MIT)
[![GitHub stars](https://img.shields.io/github/stars/PurpleHaze2320/ai-agent-pulse?style=social)](https://github.com/PurpleHaze2320/ai-agent-pulse/stargazers)

> Automated daily tracking of the AI agent framework ecosystem's health, momentum, and trends.
> Last updated: **2026-05-14 08:45 UTC** | Tracking **19** frameworks

## How It Works

This bot runs daily via GitHub Actions and collects metrics from the GitHub API for the most important
AI agent frameworks. It computes a **Pulse Score** (0-100) based on six weighted signals: star velocity,
release freshness, issue health, commit activity, community size, and fork engagement. The result is
a living dashboard that shows which frameworks are gaining momentum and which are losing steam.

## 🏆 Pulse Leaderboard

| Rank | Framework | Pulse | Stars | ⭐ 7d | Commits (4w) | Last Release | Category |
|------|-----------|-------|-------|-------|--------------|--------------|----------|
| 1 | [Mastra](https://github.com/mastra-ai/mastra) | 🟢 **77.8** | 23.9k | 🚀 +234 | 970 | today | `typescript` |
| 2 | [CrewAI](https://github.com/crewAIInc/crewAI) | 🟢 **71.2** | 51.4k | 🚀 +586 | 0 | 1 day ago | `multi-agent` |
| 3 | [OpenAI Agents SDK](https://github.com/openai/openai-agents-python) | 🟢 **70.8** | 26.3k | 🚀 +316 | 0 | 2 days ago | `orchestration` |
| 4 | [Claude Agent SDK](https://github.com/anthropics/claude-code) | 🟢 **70.2** | 123.4k | 🚀 +2266 | 27 | today | `orchestration` |
| 5 | [LangGraph](https://github.com/langchain-ai/langgraph) | 🟡 **68.8** | 32.0k | 🚀 +634 | 0 | 2 days ago | `orchestration` |
| 6 | [BrowserUse](https://github.com/browser-use/browser-use) | 🟡 **67.5** | 93.8k | 🚀 +1228 | 0 | 1 mo ago | `web-agent` |
| 7 | [LlamaIndex](https://github.com/run-llama/llama_index) | 🟡 **59.1** | 49.4k | 🚀 +214 | 0 | 23 days ago | `data-agent` |
| 8 | [PydanticAI](https://github.com/pydantic/pydantic-ai) | 🟡 **54.9** | 17.1k | 🚀 +172 | 0 | today | `structured` |
| 9 | [Agno](https://github.com/agno-agi/agno) | 🟡 **54.1** | 40.1k | 🚀 +153 | 0 | today | `multi-agent` |
| 10 | [Haystack](https://github.com/deepset-ai/haystack) | 🟡 **51.6** | 25.2k | 🚀 +119 | 0 | 1 day ago | `pipeline` |
| 11 | [Google ADK](https://github.com/google/adk-python) | 🟡 **51.5** | 19.6k | 🚀 +135 | 0 | 5 days ago | `orchestration` |
| 12 | [Semantic Kernel](https://github.com/microsoft/semantic-kernel) | 🟡 **51.5** | 27.9k | 📈 +51 | 0 | today | `enterprise` |
| 13 | [DSPy](https://github.com/stanfordnlp/dspy) | 🟡 **51.1** | 34.4k | 🚀 +154 | 0 | 8 days ago | `optimization` |
| 14 | [Letta](https://github.com/letta-ai/letta) | 🟡 **48.8** | 22.7k | 🚀 +219 | 0 | 1 mo ago | `memory` |
| 15 | [AG2](https://github.com/ag2ai/ag2) | 🟡 **48.5** | 4.5k | ↗️ +19 | 0 | 1 day ago | `multi-agent` |
| 16 | [Composio](https://github.com/ComposioHQ/composio) | 🟡 **47.9** | 28.2k | 🚀 +120 | 0 | today | `tooling` |
| 17 | [AutoGen](https://github.com/microsoft/autogen) | 🟡 **44.3** | 58.0k | 🚀 +240 | 0 | 7 mo ago | `multi-agent` |
| 18 | [Smolagents](https://github.com/huggingface/smolagents) | 🟠 **38.8** | 27.3k | 🚀 +179 | 0 | 3 mo ago | `lightweight` |
| 19 | [Swarm](https://github.com/openai/swarm) | 🔴 **9.8** | 21.5k | 📈 +44 | 0 | — | `experimental` |

## 📂 By Category

- `data-agent`: **LlamaIndex** (59.1)
- `enterprise`: **Semantic Kernel** (51.5)
- `experimental`: **Swarm** (9.8)
- `lightweight`: **Smolagents** (38.8)
- `memory`: **Letta** (48.8)
- `multi-agent`: **CrewAI** (71.2), **Agno** (54.1), **AG2** (48.5), **AutoGen** (44.3)
- `optimization`: **DSPy** (51.1)
- `orchestration`: **OpenAI Agents SDK** (70.8), **Claude Agent SDK** (70.2), **LangGraph** (68.8), **Google ADK** (51.5)
- `pipeline`: **Haystack** (51.6)
- `structured`: **PydanticAI** (54.9)
- `tooling`: **Composio** (47.9)
- `typescript`: **Mastra** (77.8)
- `web-agent`: **BrowserUse** (67.5)

## 🔍 Top 5 — Score Breakdown

| Framework | Star Velocity | Release Freshness | Issue Health | Commit Activity | Community | Fork Ratio |
|-----------|:---:|:---:|:---:|:---:|:---:|:---:|
| **Mastra** | 46.0 | 100.0 | 94.5 | 100 | 87.0 | 34.7 |
| **CrewAI** | 100 | 99.7 | 98.5 | 0.0 | 59.2 | 55.3 |
| **OpenAI Agents SDK** | 100 | 99.3 | 96.4 | 0.0 | 53.8 | 61.3 |
| **Claude Agent SDK** | 100 | 100.0 | 81.5 | 27.0 | 10.0 | 66.0 |
| **LangGraph** | 100 | 99.3 | 77.6 | 0.0 | 54.6 | 67.8 |

## 💡 Key Insights

- **Hottest framework**: Mastra with a Pulse Score of 77.8
- **Fastest growing**: Claude Agent SDK gained +2266 stars this week
- **Most active development**: Mastra with 970 commits in the last 4 weeks
- **Stale releases**: Swarm haven't released in a while

## 📦 Recent Releases

- **Agno** [`v2.6.6`](https://github.com/agno-agi/agno/releases/tag/v2.6.6) — today
- **Semantic Kernel** [`python-1.42.0`](https://github.com/microsoft/semantic-kernel/releases/tag/python-1.42.0) — today
- **PydanticAI** [`v1.96.0`](https://github.com/pydantic/pydantic-ai/releases/tag/v1.96.0) — today
- **Composio** [`@composio/cli@0.2.31-beta.251`](https://github.com/ComposioHQ/composio/releases/tag/@composio/cli@0.2.31-beta.251) — today *(pre-release)*
- **Claude Agent SDK** [`v2.1.141`](https://github.com/anthropics/claude-code/releases/tag/v2.1.141) — today
- **Mastra** [`@mastra/core@1.33.0`](https://github.com/mastra-ai/mastra/releases/tag/@mastra/core@1.33.0) — today
- **AG2** [`v0.13.0`](https://github.com/ag2ai/ag2/releases/tag/v0.13.0) — 1 day ago
- **CrewAI** [`1.14.5a5`](https://github.com/crewAIInc/crewAI/releases/tag/1.14.5a5) — 1 day ago *(pre-release)*
- **Haystack** [`v2.29.0`](https://github.com/deepset-ai/haystack/releases/tag/v2.29.0) — 1 day ago
- **LangGraph** [`1.2.0`](https://github.com/langchain-ai/langgraph/releases/tag/1.2.0) — 2 days ago

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

*Powered by GitHub Actions • Data refreshed daily • Last run: 2026-05-14 08:45 UTC*