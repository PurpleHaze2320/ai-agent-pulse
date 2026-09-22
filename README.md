# 🔬 AI Agent Framework Pulse Tracker

[![Daily Update](https://github.com/PurpleHaze2320/ai-agent-pulse/actions/workflows/track.yml/badge.svg)](https://github.com/PurpleHaze2320/ai-agent-pulse/actions/workflows/track.yml)
[![Frameworks Tracked](https://img.shields.io/badge/frameworks-19-blue)](https://github.com/PurpleHaze2320/ai-agent-pulse)
[![License: MIT](https://img.shields.io/badge/License-MIT-green.svg)](https://opensource.org/licenses/MIT)
[![GitHub stars](https://img.shields.io/github/stars/PurpleHaze2320/ai-agent-pulse?style=social)](https://github.com/PurpleHaze2320/ai-agent-pulse/stargazers)

> Automated daily tracking of the AI agent framework ecosystem's health, momentum, and trends.
> Last updated: **2026-09-22 11:17 UTC** | Tracking **19** frameworks

## How It Works

This bot runs daily via GitHub Actions and collects metrics from the GitHub API for the most important
AI agent frameworks. It computes a **Pulse Score** (0-100) based on six weighted signals: star velocity,
release freshness, issue health, commit activity, community size, and fork engagement. The result is
a living dashboard that shows which frameworks are gaining momentum and which are losing steam.

## 🏆 Pulse Leaderboard

| Rank | Framework | Pulse | Stars | ⭐ 7d | Commits (4w) | Last Release | Category |
|------|-----------|-------|-------|-------|--------------|--------------|----------|
| 1 | [BrowserUse](https://github.com/browser-use/browser-use) | 🟢 **89.1** | 115.9k | 🚀 +1180 | 131 | 18 days ago | `web-agent` |
| 2 | [Claude Agent SDK](https://github.com/anthropics/claude-code) | 🟢 **85.6** | 147.6k | 🚀 +2444 | 111 | 3 days ago | `orchestration` |
| 3 | [CrewAI](https://github.com/crewAIInc/crewAI) | 🟢 **82.1** | 58.9k | 🚀 +310 | 105 | 5 days ago | `multi-agent` |
| 4 | [OpenAI Agents SDK](https://github.com/openai/openai-agents-python) | 🟢 **77.9** | 29.6k | 🚀 +180 | 140 | 4 days ago | `orchestration` |
| 5 | [Mastra](https://github.com/mastra-ai/mastra) | 🟢 **77.7** | 28.3k | 🚀 +202 | 1590 | 6 days ago | `typescript` |
| 6 | [PydanticAI](https://github.com/pydantic/pydantic-ai) | 🟢 **75.1** | 20.1k | 🚀 +162 | 233 | today | `structured` |
| 7 | [Google ADK](https://github.com/google/adk-python) | 🟢 **72.7** | 21.6k | 📈 +55 | 339 | 3 days ago | `orchestration` |
| 8 | [LangGraph](https://github.com/langchain-ai/langgraph) | 🟢 **71.7** | 42.1k | 🚀 +440 | 36 | today | `orchestration` |
| 9 | [Agno](https://github.com/agno-agi/agno) | 🟢 **71.1** | 42.3k | 🚀 +113 | 111 | 5 days ago | `multi-agent` |
| 10 | [Composio](https://github.com/ComposioHQ/composio) | 🟡 **67.8** | 30.3k | 🚀 +102 | 231 | today | `tooling` |
| 11 | [LlamaIndex](https://github.com/run-llama/llama_index) | 🟡 **61.0** | 52.3k | 🚀 +107 | 26 | today | `data-agent` |
| 12 | [AG2](https://github.com/ag2ai/ag2) | 🟡 **59.5** | 5.0k | 📈 +25 | 46 | today | `multi-agent` |
| 13 | [DSPy](https://github.com/stanfordnlp/dspy) | 🟡 **59.0** | 38.2k | 🚀 +165 | 38 | 10 days ago | `optimization` |
| 14 | [Semantic Kernel](https://github.com/microsoft/semantic-kernel) | 🟡 **52.1** | 28.6k | 📈 +30 | 12 | 18 days ago | `enterprise` |
| 15 | [Haystack](https://github.com/deepset-ai/haystack) | 🟡 **50.5** | 26.6k | 📈 +67 | 0 | 19 days ago | `pipeline` |
| 16 | [Letta](https://github.com/letta-ai/letta) | 🟠 **38.8** | 24.8k | 📈 +92 | 2 | 4 mo ago | `memory` |
| 17 | [Smolagents](https://github.com/huggingface/smolagents) | 🟠 **35.2** | 29.4k | 🚀 +102 | 0 | 3 mo ago | `lightweight` |
| 18 | [AutoGen](https://github.com/microsoft/autogen) | 🟠 **33.3** | 61.1k | 🚀 +117 | 0 | 11 mo ago | `multi-agent` |
| 19 | [Swarm](https://github.com/openai/swarm) | 🔴 **9.6** | 22.0k | 📈 +23 | 0 | — | `experimental` |

## 📂 By Category

- `data-agent`: **LlamaIndex** (61.0)
- `enterprise`: **Semantic Kernel** (52.1)
- `experimental`: **Swarm** (9.6)
- `lightweight`: **Smolagents** (35.2)
- `memory`: **Letta** (38.8)
- `multi-agent`: **CrewAI** (82.1), **Agno** (71.1), **AG2** (59.5), **AutoGen** (33.3)
- `optimization`: **DSPy** (59.0)
- `orchestration`: **Claude Agent SDK** (85.6), **OpenAI Agents SDK** (77.9), **Google ADK** (72.7), **LangGraph** (71.7)
- `pipeline`: **Haystack** (50.5)
- `structured`: **PydanticAI** (75.1)
- `tooling`: **Composio** (67.8)
- `typescript`: **Mastra** (77.7)
- `web-agent`: **BrowserUse** (89.1)

## 🔍 Top 5 — Score Breakdown

| Framework | Star Velocity | Release Freshness | Issue Health | Commit Activity | Community | Fork Ratio |
|-----------|:---:|:---:|:---:|:---:|:---:|:---:|
| **BrowserUse** | 100 | 94.0 | 91.4 | 100 | 72.2 | 44.0 |
| **Claude Agent SDK** | 100 | 99.0 | 87.7 | 100 | 11.0 | 65.4 |
| **CrewAI** | 64.5 | 98.3 | 92.3 | 100 | 67.0 | 58.0 |
| **OpenAI Agents SDK** | 36.5 | 98.7 | 99.0 | 100 | 76.8 | 64.7 |
| **Mastra** | 41.6 | 98.0 | 95.5 | 100 | 93.2 | 40.2 |

## 💡 Key Insights

- **Hottest framework**: BrowserUse with a Pulse Score of 89.1
- **Fastest growing**: Claude Agent SDK gained +2444 stars this week
- **Most active development**: Mastra with 1590 commits in the last 4 weeks
- **Stale releases**: AutoGen, Swarm haven't released in a while

## 📦 Recent Releases

- **PydanticAI** [`v2.47.0`](https://github.com/pydantic/pydantic-ai/releases/tag/v2.47.0) — today
- **AG2** [`v1.0.6`](https://github.com/ag2ai/ag2/releases/tag/v1.0.6) — today
- **Composio** [`versioning-example@0.1.3`](https://github.com/ComposioHQ/composio/releases/tag/versioning-example@0.1.3) — today
- **LlamaIndex** [`v0.14.25`](https://github.com/run-llama/llama_index/releases/tag/v0.14.25) — today
- **LangGraph** [`1.2.12`](https://github.com/langchain-ai/langgraph/releases/tag/1.2.12) — today
- **Claude Agent SDK** [`v2.1.278`](https://github.com/anthropics/claude-code/releases/tag/v2.1.278) — 3 days ago
- **Google ADK** [`v2.9.2`](https://github.com/google/adk-python/releases/tag/v2.9.2) — 3 days ago
- **OpenAI Agents SDK** [`v0.22.3`](https://github.com/openai/openai-agents-python/releases/tag/v0.22.3) — 4 days ago
- **CrewAI** [`1.15.22`](https://github.com/crewAIInc/crewAI/releases/tag/1.15.22) — 5 days ago
- **Agno** [`v3.0.10`](https://github.com/agno-agi/agno/releases/tag/v3.0.10) — 5 days ago

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

*Powered by GitHub Actions • Data refreshed daily • Last run: 2026-09-22 11:17 UTC*