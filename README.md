# 🔬 AI Agent Framework Pulse Tracker

[![Daily Update](https://github.com/PurpleHaze2320/ai-agent-pulse/actions/workflows/track.yml/badge.svg)](https://github.com/PurpleHaze2320/ai-agent-pulse/actions/workflows/track.yml)
[![Frameworks Tracked](https://img.shields.io/badge/frameworks-19-blue)](https://github.com/PurpleHaze2320/ai-agent-pulse)
[![License: MIT](https://img.shields.io/badge/License-MIT-green.svg)](https://opensource.org/licenses/MIT)
[![GitHub stars](https://img.shields.io/github/stars/PurpleHaze2320/ai-agent-pulse?style=social)](https://github.com/PurpleHaze2320/ai-agent-pulse/stargazers)

> Automated daily tracking of the AI agent framework ecosystem's health, momentum, and trends.
> Last updated: **2026-06-17 11:07 UTC** | Tracking **19** frameworks

## How It Works

This bot runs daily via GitHub Actions and collects metrics from the GitHub API for the most important
AI agent frameworks. It computes a **Pulse Score** (0-100) based on six weighted signals: star velocity,
release freshness, issue health, commit activity, community size, and fork engagement. The result is
a living dashboard that shows which frameworks are gaining momentum and which are losing steam.

## 🏆 Pulse Leaderboard

| Rank | Framework | Pulse | Stars | ⭐ 7d | Commits (4w) | Last Release | Category |
|------|-----------|-------|-------|-------|--------------|--------------|----------|
| 1 | [CrewAI](https://github.com/crewAIInc/crewAI) | 🟢 **90.7** | 53.8k | 🚀 +577 | 104 | 5 days ago | `multi-agent` |
| 2 | [BrowserUse](https://github.com/browser-use/browser-use) | 🟢 **89.8** | 99.2k | 🚀 +1191 | 408 | 4 days ago | `web-agent` |
| 3 | [LangGraph](https://github.com/langchain-ai/langgraph) | 🟢 **82.0** | 35.0k | 🚀 +672 | 68 | today | `orchestration` |
| 4 | [Mastra](https://github.com/mastra-ai/mastra) | 🟢 **79.6** | 25.2k | 🚀 +241 | 805 | 4 days ago | `typescript` |
| 5 | [Agno](https://github.com/agno-agi/agno) | 🟢 **72.7** | 40.7k | 🚀 +125 | 99 | 1 day ago | `multi-agent` |
| 6 | [Claude Agent SDK](https://github.com/anthropics/claude-code) | 🟢 **71.2** | 132.9k | 🚀 +1478 | 28 | today | `orchestration` |
| 7 | [PydanticAI](https://github.com/pydantic/pydantic-ai) | 🟡 **69.0** | 17.8k | 🚀 +133 | 77 | 6 days ago | `structured` |
| 8 | [AG2](https://github.com/ag2ai/ag2) | 🟡 **60.7** | 4.7k | 📈 +23 | 61 | 4 days ago | `multi-agent` |
| 9 | [LlamaIndex](https://github.com/run-llama/llama_index) | 🟡 **59.8** | 50.2k | 🚀 +131 | 23 | 1 mo ago | `data-agent` |
| 10 | [OpenAI Agents SDK](https://github.com/openai/openai-agents-python) | 🟡 **58.6** | 27.2k | 🚀 +151 | 23 | 6 days ago | `orchestration` |
| 11 | [DSPy](https://github.com/stanfordnlp/dspy) | 🟡 **56.6** | 35.1k | 🚀 +124 | 38 | 20 days ago | `optimization` |
| 12 | [Composio](https://github.com/ComposioHQ/composio) | 🟡 **55.0** | 28.8k | 🚀 +112 | 38 | today | `tooling` |
| 13 | [Semantic Kernel](https://github.com/microsoft/semantic-kernel) | 🟡 **52.0** | 28.1k | 📈 +58 | 0 | today | `enterprise` |
| 14 | [Google ADK](https://github.com/google/adk-python) | 🟡 **50.9** | 20.1k | 🚀 +101 | 0 | 1 day ago | `orchestration` |
| 15 | [Haystack](https://github.com/deepset-ai/haystack) | 🟡 **49.9** | 25.6k | 📈 +75 | 0 | 7 days ago | `pipeline` |
| 16 | [Letta](https://github.com/letta-ai/letta) | 🟡 **46.6** | 23.4k | 🚀 +142 | 0 | 1 mo ago | `memory` |
| 17 | [Smolagents](https://github.com/huggingface/smolagents) | 🟡 **43.5** | 27.9k | 🚀 +108 | 5 | 19 days ago | `lightweight` |
| 18 | [AutoGen](https://github.com/microsoft/autogen) | 🟡 **40.3** | 59.0k | 🚀 +199 | 0 | 8 mo ago | `multi-agent` |
| 19 | [Swarm](https://github.com/openai/swarm) | 🔴 **9.2** | 21.6k | 📈 +33 | 0 | — | `experimental` |

## 📂 By Category

- `data-agent`: **LlamaIndex** (59.8)
- `enterprise`: **Semantic Kernel** (52.0)
- `experimental`: **Swarm** (9.2)
- `lightweight`: **Smolagents** (43.5)
- `memory`: **Letta** (46.6)
- `multi-agent`: **CrewAI** (90.7), **Agno** (72.7), **AG2** (60.7), **AutoGen** (40.3)
- `optimization`: **DSPy** (56.6)
- `orchestration`: **LangGraph** (82.0), **Claude Agent SDK** (71.2), **OpenAI Agents SDK** (58.6), **Google ADK** (50.9)
- `pipeline`: **Haystack** (49.9)
- `structured`: **PydanticAI** (69.0)
- `tooling`: **Composio** (55.0)
- `typescript`: **Mastra** (79.6)
- `web-agent`: **BrowserUse** (89.8)

## 🔍 Top 5 — Score Breakdown

| Framework | Star Velocity | Release Freshness | Issue Health | Commit Activity | Community | Fork Ratio |
|-----------|:---:|:---:|:---:|:---:|:---:|:---:|
| **CrewAI** | 100 | 98.3 | 96.9 | 100 | 59.4 | 56.0 |
| **BrowserUse** | 100 | 98.7 | 95.6 | 100 | 63.0 | 44.7 |
| **LangGraph** | 100 | 100.0 | 74.6 | 68.0 | 55.0 | 66.9 |
| **Mastra** | 51.4 | 98.7 | 95.0 | 100 | 92.0 | 35.6 |
| **Agno** | 26.1 | 99.7 | 80.9 | 99.0 | 89.0 | 54.3 |

## 💡 Key Insights

- **Hottest framework**: CrewAI with a Pulse Score of 90.7
- **Fastest growing**: Claude Agent SDK gained +1478 stars this week
- **Most active development**: Mastra with 805 commits in the last 4 weeks
- **Stale releases**: Swarm haven't released in a while

## 📦 Recent Releases

- **Semantic Kernel** [`python-1.43.1`](https://github.com/microsoft/semantic-kernel/releases/tag/python-1.43.1) — today
- **Claude Agent SDK** [`v2.1.179`](https://github.com/anthropics/claude-code/releases/tag/v2.1.179) — today
- **LangGraph** [`cli==0.4.30`](https://github.com/langchain-ai/langgraph/releases/tag/cli==0.4.30) — today
- **Composio** [`@composio/cli@0.2.32-beta.265`](https://github.com/ComposioHQ/composio/releases/tag/@composio/cli@0.2.32-beta.265) — today *(pre-release)*
- **Google ADK** [`v1.35.1`](https://github.com/google/adk-python/releases/tag/v1.35.1) — 1 day ago
- **Agno** [`v2.6.16`](https://github.com/agno-agi/agno/releases/tag/v2.6.16) — 1 day ago
- **BrowserUse** [`0.13.2`](https://github.com/browser-use/browser-use/releases/tag/0.13.2) — 4 days ago
- **AG2** [`v0.13.4`](https://github.com/ag2ai/ag2/releases/tag/v0.13.4) — 4 days ago
- **Mastra** [`@mastra/core@1.42.0`](https://github.com/mastra-ai/mastra/releases/tag/@mastra/core@1.42.0) — 4 days ago
- **CrewAI** [`1.14.7`](https://github.com/crewAIInc/crewAI/releases/tag/1.14.7) — 5 days ago

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

*Powered by GitHub Actions • Data refreshed daily • Last run: 2026-06-17 11:07 UTC*