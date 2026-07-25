# 🔬 AI Agent Framework Pulse Tracker

[![Daily Update](https://github.com/PurpleHaze2320/ai-agent-pulse/actions/workflows/track.yml/badge.svg)](https://github.com/PurpleHaze2320/ai-agent-pulse/actions/workflows/track.yml)
[![Frameworks Tracked](https://img.shields.io/badge/frameworks-19-blue)](https://github.com/PurpleHaze2320/ai-agent-pulse)
[![License: MIT](https://img.shields.io/badge/License-MIT-green.svg)](https://opensource.org/licenses/MIT)
[![GitHub stars](https://img.shields.io/github/stars/PurpleHaze2320/ai-agent-pulse?style=social)](https://github.com/PurpleHaze2320/ai-agent-pulse/stargazers)

> Automated daily tracking of the AI agent framework ecosystem's health, momentum, and trends.
> Last updated: **2026-07-25 08:13 UTC** | Tracking **19** frameworks

## How It Works

This bot runs daily via GitHub Actions and collects metrics from the GitHub API for the most important
AI agent frameworks. It computes a **Pulse Score** (0-100) based on six weighted signals: star velocity,
release freshness, issue health, commit activity, community size, and fork engagement. The result is
a living dashboard that shows which frameworks are gaining momentum and which are losing steam.

## 🏆 Pulse Leaderboard

| Rank | Framework | Pulse | Stars | ⭐ 7d | Commits (4w) | Last Release | Category |
|------|-----------|-------|-------|-------|--------------|--------------|----------|
| 1 | [BrowserUse](https://github.com/browser-use/browser-use) | 🟢 **89.4** | 106.7k | 🚀 +1360 | 104 | 8 days ago | `web-agent` |
| 2 | [CrewAI](https://github.com/crewAIInc/crewAI) | 🟢 **80.8** | 56.1k | 🚀 +386 | 73 | today | `multi-agent` |
| 3 | [Mastra](https://github.com/mastra-ai/mastra) | 🟢 **79.3** | 26.5k | 🚀 +244 | 1186 | 9 days ago | `typescript` |
| 4 | [Google ADK](https://github.com/google/adk-python) | 🟢 **77.7** | 20.9k | 🚀 +224 | 325 | 3 days ago | `orchestration` |
| 5 | [Agno](https://github.com/agno-agi/agno) | 🟢 **75.6** | 41.4k | 🚀 +198 | 152 | today | `multi-agent` |
| 6 | [OpenAI Agents SDK](https://github.com/openai/openai-agents-python) | 🟢 **75.5** | 28.2k | 🚀 +172 | 144 | 8 days ago | `orchestration` |
| 7 | [Claude Agent SDK](https://github.com/anthropics/claude-code) | 🟢 **71.0** | 139.0k | 🚀 +860 | 30 | today | `orchestration` |
| 8 | [Haystack](https://github.com/deepset-ai/haystack) | 🟢 **70.7** | 26.0k | 📈 +79 | 248 | 4 days ago | `pipeline` |
| 9 | [LangGraph](https://github.com/langchain-ai/langgraph) | 🟡 **67.0** | 38.1k | 🚀 +558 | 0 | 15 days ago | `orchestration` |
| 10 | [Composio](https://github.com/ComposioHQ/composio) | 🟡 **66.8** | 29.4k | 📈 +94 | 135 | 4 days ago | `tooling` |
| 11 | [LlamaIndex](https://github.com/run-llama/llama_index) | 🟡 **63.7** | 51.1k | 🚀 +162 | 36 | 1 mo ago | `data-agent` |
| 12 | [PydanticAI](https://github.com/pydantic/pydantic-ai) | 🟡 **56.5** | 18.8k | 🚀 +172 | 0 | today | `structured` |
| 13 | [Semantic Kernel](https://github.com/microsoft/semantic-kernel) | 🟡 **50.0** | 28.4k | 📈 +35 | 0 | 17 days ago | `enterprise` |
| 14 | [DSPy](https://github.com/stanfordnlp/dspy) | 🟡 **49.2** | 36.4k | 🚀 +161 | 0 | 1 mo ago | `optimization` |
| 15 | [AG2](https://github.com/ag2ai/ag2) | 🟡 **48.6** | 4.8k | ↗️ +15 | 0 | 21 days ago | `multi-agent` |
| 16 | [Letta](https://github.com/letta-ai/letta) | 🟡 **42.8** | 23.9k | 🚀 +112 | 1 | 2 mo ago | `memory` |
| 17 | [Smolagents](https://github.com/huggingface/smolagents) | 🟡 **40.7** | 28.5k | 🚀 +109 | 4 | 1 mo ago | `lightweight` |
| 18 | [AutoGen](https://github.com/microsoft/autogen) | 🟠 **35.5** | 60.0k | 🚀 +155 | 0 | 9 mo ago | `multi-agent` |
| 19 | [Swarm](https://github.com/openai/swarm) | 🔴 **10.8** | 21.9k | 📈 +52 | 0 | — | `experimental` |

## 📂 By Category

- `data-agent`: **LlamaIndex** (63.7)
- `enterprise`: **Semantic Kernel** (50.0)
- `experimental`: **Swarm** (10.8)
- `lightweight`: **Smolagents** (40.7)
- `memory`: **Letta** (42.8)
- `multi-agent`: **CrewAI** (80.8), **Agno** (75.6), **AG2** (48.6), **AutoGen** (35.5)
- `optimization`: **DSPy** (49.2)
- `orchestration`: **Google ADK** (77.7), **OpenAI Agents SDK** (75.5), **Claude Agent SDK** (71.0), **LangGraph** (67.0)
- `pipeline`: **Haystack** (70.7)
- `structured`: **PydanticAI** (56.5)
- `tooling`: **Composio** (66.8)
- `typescript`: **Mastra** (79.3)
- `web-agent`: **BrowserUse** (89.4)

## 🔍 Top 5 — Score Breakdown

| Framework | Star Velocity | Release Freshness | Issue Health | Commit Activity | Community | Fork Ratio |
|-----------|:---:|:---:|:---:|:---:|:---:|:---:|
| **BrowserUse** | 100 | 97.3 | 94.6 | 100 | 63.0 | 44.0 |
| **CrewAI** | 80.4 | 100.0 | 96.1 | 73.0 | 59.6 | 56.7 |
| **Mastra** | 50.8 | 97.0 | 94.1 | 100 | 93.0 | 37.8 |
| **Google ADK** | 40.2 | 99.0 | 87.5 | 100 | 75.8 | 72.0 |
| **Agno** | 36.3 | 100.0 | 80.7 | 100 | 89.2 | 55.0 |

## 💡 Key Insights

- **Hottest framework**: BrowserUse with a Pulse Score of 89.4
- **Fastest growing**: BrowserUse gained +1360 stars this week
- **Most active development**: Mastra with 1186 commits in the last 4 weeks
- **Stale releases**: AutoGen, Swarm haven't released in a while

## 📦 Recent Releases

- **Claude Agent SDK** [`v2.1.220`](https://github.com/anthropics/claude-code/releases/tag/v2.1.220) — today
- **PydanticAI** [`v2.18.0`](https://github.com/pydantic/pydantic-ai/releases/tag/v2.18.0) — today
- **CrewAI** [`1.15.6`](https://github.com/crewAIInc/crewAI/releases/tag/1.15.6) — today
- **Agno** [`v2.8.2`](https://github.com/agno-agi/agno/releases/tag/v2.8.2) — today
- **Google ADK** [`v1.36.2`](https://github.com/google/adk-python/releases/tag/v1.36.2) — 3 days ago
- **Composio** [`@composio/cli@0.2.33-beta.298`](https://github.com/ComposioHQ/composio/releases/tag/@composio/cli@0.2.33-beta.298) — 4 days ago *(pre-release)*
- **Haystack** [`v3.0.0`](https://github.com/deepset-ai/haystack/releases/tag/v3.0.0) — 4 days ago
- **BrowserUse** [`0.13.6`](https://github.com/browser-use/browser-use/releases/tag/0.13.6) — 8 days ago
- **OpenAI Agents SDK** [`v0.18.3`](https://github.com/openai/openai-agents-python/releases/tag/v0.18.3) — 8 days ago
- **Mastra** [`@mastra/core@1.51.0`](https://github.com/mastra-ai/mastra/releases/tag/@mastra/core@1.51.0) — 9 days ago

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

*Powered by GitHub Actions • Data refreshed daily • Last run: 2026-07-25 08:13 UTC*