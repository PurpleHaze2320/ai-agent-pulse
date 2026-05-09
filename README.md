# 🔬 AI Agent Framework Pulse Tracker

[![Daily Update](https://github.com/PurpleHaze2320/ai-agent-pulse/actions/workflows/track.yml/badge.svg)](https://github.com/PurpleHaze2320/ai-agent-pulse/actions/workflows/track.yml)
[![Frameworks Tracked](https://img.shields.io/badge/frameworks-19-blue)](https://github.com/PurpleHaze2320/ai-agent-pulse)
[![License: MIT](https://img.shields.io/badge/License-MIT-green.svg)](https://opensource.org/licenses/MIT)
[![GitHub stars](https://img.shields.io/github/stars/PurpleHaze2320/ai-agent-pulse?style=social)](https://github.com/PurpleHaze2320/ai-agent-pulse/stargazers)

> Automated daily tracking of the AI agent framework ecosystem's health, momentum, and trends.
> Last updated: **2026-05-09 08:03 UTC** | Tracking **19** frameworks

## How It Works

This bot runs daily via GitHub Actions and collects metrics from the GitHub API for the most important
AI agent frameworks. It computes a **Pulse Score** (0-100) based on six weighted signals: star velocity,
release freshness, issue health, commit activity, community size, and fork engagement. The result is
a living dashboard that shows which frameworks are gaining momentum and which are losing steam.

## 🏆 Pulse Leaderboard

| Rank | Framework | Pulse | Stars | ⭐ 7d | Commits (4w) | Last Release | Category |
|------|-----------|-------|-------|-------|--------------|--------------|----------|
| 1 | [Mastra](https://github.com/mastra-ai/mastra) | 🟢 **77.4** | 23.7k | 🚀 +229 | 1003 | 2 days ago | `typescript` |
| 2 | [CrewAI](https://github.com/crewAIInc/crewAI) | 🟢 **71.3** | 51.0k | 🚀 +508 | 0 | today | `multi-agent` |
| 3 | [OpenAI Agents SDK](https://github.com/openai/openai-agents-python) | 🟢 **70.9** | 26.1k | 🚀 +368 | 0 | today | `orchestration` |
| 4 | [LangGraph](https://github.com/langchain-ai/langgraph) | 🟡 **68.9** | 31.6k | 🚀 +562 | 0 | 1 day ago | `orchestration` |
| 5 | [BrowserUse](https://github.com/browser-use/browser-use) | 🟡 **67.8** | 93.0k | 🚀 +1401 | 0 | 1 mo ago | `web-agent` |
| 6 | [Claude Agent SDK](https://github.com/anthropics/claude-code) | 🟡 **64.8** | 121.8k | 🚀 +2036 | 0 | today | `orchestration` |
| 7 | [LlamaIndex](https://github.com/run-llama/llama_index) | 🟡 **57.8** | 49.3k | 🚀 +164 | 0 | 18 days ago | `data-agent` |
| 8 | [PydanticAI](https://github.com/pydantic/pydantic-ai) | 🟡 **54.3** | 16.9k | 🚀 +152 | 0 | today | `structured` |
| 9 | [Agno](https://github.com/agno-agi/agno) | 🟡 **54.3** | 40.0k | 🚀 +158 | 0 | 2 days ago | `multi-agent` |
| 10 | [Google ADK](https://github.com/google/adk-python) | 🟡 **52.7** | 19.5k | 🚀 +155 | 0 | today | `orchestration` |
| 11 | [DSPy](https://github.com/stanfordnlp/dspy) | 🟡 **50.8** | 34.3k | 🚀 +137 | 0 | 3 days ago | `optimization` |
| 12 | [Semantic Kernel](https://github.com/microsoft/semantic-kernel) | 🟡 **50.3** | 27.9k | 📈 +35 | 0 | 9 days ago | `enterprise` |
| 13 | [AG2](https://github.com/ag2ai/ag2) | 🟡 **49.6** | 4.5k | 📈 +56 | 0 | 3 days ago | `multi-agent` |
| 14 | [Haystack](https://github.com/deepset-ai/haystack) | 🟡 **48.8** | 25.1k | 📈 +78 | 0 | 18 days ago | `pipeline` |
| 15 | [Composio](https://github.com/ComposioHQ/composio) | 🟡 **47.3** | 28.1k | 🚀 +142 | 0 | 1 day ago | `tooling` |
| 16 | [Letta](https://github.com/letta-ai/letta) | 🟡 **46.8** | 22.6k | 🚀 +159 | 0 | 1 mo ago | `memory` |
| 17 | [AutoGen](https://github.com/microsoft/autogen) | 🟡 **43.3** | 57.8k | 🚀 +198 | 0 | 7 mo ago | `multi-agent` |
| 18 | [Smolagents](https://github.com/huggingface/smolagents) | 🟠 **37.8** | 27.2k | 🚀 +145 | 0 | 3 mo ago | `lightweight` |
| 19 | [Swarm](https://github.com/openai/swarm) | 🔴 **9.8** | 21.5k | 📈 +38 | 0 | — | `experimental` |

## 📂 By Category

- `data-agent`: **LlamaIndex** (57.8)
- `enterprise`: **Semantic Kernel** (50.3)
- `experimental`: **Swarm** (9.8)
- `lightweight`: **Smolagents** (37.8)
- `memory`: **Letta** (46.8)
- `multi-agent`: **CrewAI** (71.3), **Agno** (54.3), **AG2** (49.6), **AutoGen** (43.3)
- `optimization`: **DSPy** (50.8)
- `orchestration`: **OpenAI Agents SDK** (70.9), **LangGraph** (68.9), **Claude Agent SDK** (64.8), **Google ADK** (52.7)
- `pipeline`: **Haystack** (48.8)
- `structured`: **PydanticAI** (54.3)
- `tooling`: **Composio** (47.3)
- `typescript`: **Mastra** (77.4)
- `web-agent`: **BrowserUse** (67.8)

## 🔍 Top 5 — Score Breakdown

| Framework | Star Velocity | Release Freshness | Issue Health | Commit Activity | Community | Fork Ratio |
|-----------|:---:|:---:|:---:|:---:|:---:|:---:|
| **Mastra** | 45.3 | 99.3 | 94.7 | 100 | 85.8 | 34.3 |
| **CrewAI** | 100 | 100.0 | 98.7 | 0.0 | 59.2 | 55.3 |
| **OpenAI Agents SDK** | 100 | 100.0 | 96.6 | 0.0 | 53.2 | 61.4 |
| **LangGraph** | 100 | 99.7 | 78.1 | 0.0 | 54.8 | 67.9 |
| **BrowserUse** | 100 | 87.7 | 96.4 | 0.0 | 62.8 | 45.3 |

## 💡 Key Insights

- **Hottest framework**: Mastra with a Pulse Score of 77.4
- **Fastest growing**: Claude Agent SDK gained +2036 stars this week
- **Most active development**: Mastra with 1003 commits in the last 4 weeks
- **Stale releases**: Swarm haven't released in a while

## 📦 Recent Releases

- **Claude Agent SDK** [`v2.1.138`](https://github.com/anthropics/claude-code/releases/tag/v2.1.138) — today
- **PydanticAI** [`v1.93.0`](https://github.com/pydantic/pydantic-ai/releases/tag/v1.93.0) — today
- **Google ADK** [`v1.33.0`](https://github.com/google/adk-python/releases/tag/v1.33.0) — today
- **CrewAI** [`1.14.5a4`](https://github.com/crewAIInc/crewAI/releases/tag/1.14.5a4) — today *(pre-release)*
- **OpenAI Agents SDK** [`v0.17.0`](https://github.com/openai/openai-agents-python/releases/tag/v0.17.0) — today
- **LangGraph** [`cli==0.4.25`](https://github.com/langchain-ai/langgraph/releases/tag/cli==0.4.25) — 1 day ago
- **Composio** [`py@0.13.0`](https://github.com/ComposioHQ/composio/releases/tag/py@0.13.0) — 1 day ago
- **Agno** [`v2.6.5`](https://github.com/agno-agi/agno/releases/tag/v2.6.5) — 2 days ago
- **Mastra** [`@mastra/core@1.32.0`](https://github.com/mastra-ai/mastra/releases/tag/@mastra/core@1.32.0) — 2 days ago
- **AG2** [`v0.12.3`](https://github.com/ag2ai/ag2/releases/tag/v0.12.3) — 3 days ago

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

*Powered by GitHub Actions • Data refreshed daily • Last run: 2026-05-09 08:03 UTC*