# 🔬 AI Agent Framework Pulse Tracker

[![Daily Update](https://github.com/PurpleHaze2320/ai-agent-pulse/actions/workflows/track.yml/badge.svg)](https://github.com/PurpleHaze2320/ai-agent-pulse/actions/workflows/track.yml)
[![Frameworks Tracked](https://img.shields.io/badge/frameworks-19-blue)](https://github.com/PurpleHaze2320/ai-agent-pulse)
[![License: MIT](https://img.shields.io/badge/License-MIT-green.svg)](https://opensource.org/licenses/MIT)
[![GitHub stars](https://img.shields.io/github/stars/PurpleHaze2320/ai-agent-pulse?style=social)](https://github.com/PurpleHaze2320/ai-agent-pulse/stargazers)

> Automated daily tracking of the AI agent framework ecosystem's health, momentum, and trends.
> Last updated: **2026-06-23 09:52 UTC** | Tracking **19** frameworks

## How It Works

This bot runs daily via GitHub Actions and collects metrics from the GitHub API for the most important
AI agent frameworks. It computes a **Pulse Score** (0-100) based on six weighted signals: star velocity,
release freshness, issue health, commit activity, community size, and fork engagement. The result is
a living dashboard that shows which frameworks are gaining momentum and which are losing steam.

## 🏆 Pulse Leaderboard

| Rank | Framework | Pulse | Stars | ⭐ 7d | Commits (4w) | Last Release | Category |
|------|-----------|-------|-------|-------|--------------|--------------|----------|
| 1 | [CrewAI](https://github.com/crewAIInc/crewAI) | 🟢 **90.7** | 54.2k | 🚀 +525 | 107 | 4 days ago | `multi-agent` |
| 2 | [BrowserUse](https://github.com/browser-use/browser-use) | 🟢 **89.4** | 100.2k | 🚀 +1136 | 409 | 10 days ago | `web-agent` |
| 3 | [Mastra](https://github.com/mastra-ai/mastra) | 🟢 **78.8** | 25.4k | 🚀 +224 | 756 | 3 days ago | `typescript` |
| 4 | [LangGraph](https://github.com/langchain-ai/langgraph) | 🟢 **78.7** | 35.5k | 🚀 +590 | 53 | 4 days ago | `orchestration` |
| 5 | [Google ADK](https://github.com/google/adk-python) | 🟢 **71.9** | 20.2k | 🚀 +119 | 261 | 4 days ago | `orchestration` |
| 6 | [Claude Agent SDK](https://github.com/anthropics/claude-code) | 🟢 **71.1** | 133.9k | 🚀 +1199 | 27 | today | `orchestration` |
| 7 | [Haystack](https://github.com/deepset-ai/haystack) | 🟡 **69.4** | 25.6k | 📈 +58 | 151 | 5 days ago | `pipeline` |
| 8 | [Agno](https://github.com/agno-agi/agno) | 🟡 **69.1** | 40.8k | 📈 +99 | 88 | 4 days ago | `multi-agent` |
| 9 | [PydanticAI](https://github.com/pydantic/pydantic-ai) | 🟡 **68.8** | 17.9k | 🚀 +141 | 76 | 12 days ago | `structured` |
| 10 | [OpenAI Agents SDK](https://github.com/openai/openai-agents-python) | 🟡 **63.7** | 27.4k | 🚀 +173 | 43 | 4 days ago | `orchestration` |
| 11 | [Composio](https://github.com/ComposioHQ/composio) | 🟡 **60.0** | 28.9k | 🚀 +114 | 63 | 2 days ago | `tooling` |
| 12 | [DSPy](https://github.com/stanfordnlp/dspy) | 🟡 **57.2** | 35.3k | 🚀 +254 | 18 | 26 days ago | `optimization` |
| 13 | [LlamaIndex](https://github.com/run-llama/llama_index) | 🟡 **56.8** | 50.3k | 🚀 +141 | 9 | 1 mo ago | `data-agent` |
| 14 | [Semantic Kernel](https://github.com/microsoft/semantic-kernel) | 🟡 **56.2** | 28.2k | 📈 +43 | 26 | 6 days ago | `enterprise` |
| 15 | [AG2](https://github.com/ag2ai/ag2) | 🟡 **48.2** | 4.7k | 📈 +27 | 0 | 10 days ago | `multi-agent` |
| 16 | [Letta](https://github.com/letta-ai/letta) | 🟡 **45.1** | 23.5k | 🚀 +116 | 0 | 1 mo ago | `memory` |
| 17 | [Smolagents](https://github.com/huggingface/smolagents) | 🟡 **41.4** | 28.0k | 📈 +93 | 0 | 25 days ago | `lightweight` |
| 18 | [AutoGen](https://github.com/microsoft/autogen) | 🟠 **39.2** | 59.2k | 🚀 +185 | 0 | 8 mo ago | `multi-agent` |
| 19 | [Swarm](https://github.com/openai/swarm) | 🔴 **10.1** | 21.7k | 📈 +61 | 0 | — | `experimental` |

## 📂 By Category

- `data-agent`: **LlamaIndex** (56.8)
- `enterprise`: **Semantic Kernel** (56.2)
- `experimental`: **Swarm** (10.1)
- `lightweight`: **Smolagents** (41.4)
- `memory`: **Letta** (45.1)
- `multi-agent`: **CrewAI** (90.7), **Agno** (69.1), **AG2** (48.2), **AutoGen** (39.2)
- `optimization`: **DSPy** (57.2)
- `orchestration`: **LangGraph** (78.7), **Google ADK** (71.9), **Claude Agent SDK** (71.1), **OpenAI Agents SDK** (63.7)
- `pipeline`: **Haystack** (69.4)
- `structured`: **PydanticAI** (68.8)
- `tooling`: **Composio** (60.0)
- `typescript`: **Mastra** (78.8)
- `web-agent`: **BrowserUse** (89.4)

## 🔍 Top 5 — Score Breakdown

| Framework | Star Velocity | Release Freshness | Issue Health | Commit Activity | Community | Fork Ratio |
|-----------|:---:|:---:|:---:|:---:|:---:|:---:|
| **CrewAI** | 100 | 98.7 | 96.5 | 100 | 59.4 | 56.0 |
| **BrowserUse** | 100 | 96.7 | 95.4 | 100 | 63.0 | 44.6 |
| **Mastra** | 48.0 | 99.0 | 94.9 | 100 | 91.8 | 35.9 |
| **LangGraph** | 100 | 98.7 | 74.5 | 53.0 | 55.0 | 67.1 |
| **Google ADK** | 23.1 | 98.7 | 84.4 | 100 | 66.2 | 71.2 |

## 💡 Key Insights

- **Hottest framework**: CrewAI with a Pulse Score of 90.7
- **Fastest growing**: Claude Agent SDK gained +1199 stars this week
- **Most active development**: Mastra with 756 commits in the last 4 weeks
- **Stale releases**: Swarm haven't released in a while

## 📦 Recent Releases

- **Claude Agent SDK** [`v2.1.186`](https://github.com/anthropics/claude-code/releases/tag/v2.1.186) — today
- **Composio** [`@composio/cli@0.2.32-beta.270`](https://github.com/ComposioHQ/composio/releases/tag/@composio/cli@0.2.32-beta.270) — 2 days ago *(pre-release)*
- **Mastra** [`@mastra/core@1.45.0`](https://github.com/mastra-ai/mastra/releases/tag/@mastra/core@1.45.0) — 3 days ago
- **OpenAI Agents SDK** [`v0.17.6`](https://github.com/openai/openai-agents-python/releases/tag/v0.17.6) — 4 days ago
- **CrewAI** [`1.14.8a2`](https://github.com/crewAIInc/crewAI/releases/tag/1.14.8a2) — 4 days ago *(pre-release)*
- **LangGraph** [`1.2.6`](https://github.com/langchain-ai/langgraph/releases/tag/1.2.6) — 4 days ago
- **Agno** [`v2.6.18`](https://github.com/agno-agi/agno/releases/tag/v2.6.18) — 4 days ago
- **Google ADK** [`v2.3.0`](https://github.com/google/adk-python/releases/tag/v2.3.0) — 4 days ago
- **Haystack** [`v2.30.2`](https://github.com/deepset-ai/haystack/releases/tag/v2.30.2) — 5 days ago
- **Semantic Kernel** [`python-1.43.1`](https://github.com/microsoft/semantic-kernel/releases/tag/python-1.43.1) — 6 days ago

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

*Powered by GitHub Actions • Data refreshed daily • Last run: 2026-06-23 09:52 UTC*