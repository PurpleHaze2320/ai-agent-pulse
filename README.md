# 🔬 AI Agent Framework Pulse Tracker

[![Daily Update](https://github.com/PurpleHaze2320/ai-agent-pulse/actions/workflows/track.yml/badge.svg)](https://github.com/PurpleHaze2320/ai-agent-pulse/actions/workflows/track.yml)
[![Frameworks Tracked](https://img.shields.io/badge/frameworks-19-blue)](https://github.com/PurpleHaze2320/ai-agent-pulse)
[![License: MIT](https://img.shields.io/badge/License-MIT-green.svg)](https://opensource.org/licenses/MIT)
[![GitHub stars](https://img.shields.io/github/stars/PurpleHaze2320/ai-agent-pulse?style=social)](https://github.com/PurpleHaze2320/ai-agent-pulse/stargazers)

> Automated daily tracking of the AI agent framework ecosystem's health, momentum, and trends.
> Last updated: **2026-10-26 12:35 UTC** | Tracking **19** frameworks

## How It Works

This bot runs daily via GitHub Actions and collects metrics from the GitHub API for the most important
AI agent frameworks. It computes a **Pulse Score** (0-100) based on six weighted signals: star velocity,
release freshness, issue health, commit activity, community size, and fork engagement. The result is
a living dashboard that shows which frameworks are gaining momentum and which are losing steam.

## 🏆 Pulse Leaderboard

| Rank | Framework | Pulse | Stars | ⭐ 7d | Commits (4w) | Last Release | Category |
|------|-----------|-------|-------|-------|--------------|--------------|----------|
| 1 | [BrowserUse](https://github.com/browser-use/browser-use) | 🟢 **89.4** | 119.2k | 🚀 +696 | 112 | 10 days ago | `web-agent` |
| 2 | [LangGraph](https://github.com/langchain-ai/langgraph) | 🟢 **83.9** | 43.9k | 🚀 +427 | 93 | 2 days ago | `orchestration` |
| 3 | [CrewAI](https://github.com/crewAIInc/crewAI) | 🟢 **78.8** | 60.1k | 🚀 +251 | 129 | 2 days ago | `multi-agent` |
| 4 | [Mastra](https://github.com/mastra-ai/mastra) | 🟢 **76.6** | 29.1k | 🚀 +182 | 1945 | 5 days ago | `typescript` |
| 5 | [Google ADK](https://github.com/google/adk-python) | 🟢 **75.1** | 22.0k | 🚀 +101 | 407 | 2 days ago | `orchestration` |
| 6 | [Claude Agent SDK](https://github.com/anthropics/claude-code) | 🟢 **73.4** | 153.4k | 🚀 +1045 | 39 | 2 days ago | `orchestration` |
| 7 | [Agno](https://github.com/agno-agi/agno) | 🟢 **70.4** | 42.9k | 📈 +91 | 146 | 2 days ago | `multi-agent` |
| 8 | [OpenAI Agents SDK](https://github.com/openai/openai-agents-python) | 🟡 **68.2** | 30.3k | 🚀 +158 | 59 | 11 days ago | `orchestration` |
| 9 | [AG2](https://github.com/ag2ai/ag2) | 🟡 **68.2** | 5.0k | ↗️ +14 | 93 | 4 days ago | `multi-agent` |
| 10 | [Composio](https://github.com/ComposioHQ/composio) | 🟡 **68.1** | 30.8k | 🚀 +121 | 294 | 2 days ago | `tooling` |
| 11 | [DSPy](https://github.com/stanfordnlp/dspy) | 🟡 **58.9** | 38.8k | 🚀 +107 | 53 | 13 days ago | `optimization` |
| 12 | [LlamaIndex](https://github.com/run-llama/llama_index) | 🟡 **54.7** | 52.7k | 🚀 +102 | 9 | 1 mo ago | `data-agent` |
| 13 | [PydanticAI](https://github.com/pydantic/pydantic-ai) | 🟡 **53.2** | 20.9k | 🚀 +154 | 0 | 20 days ago | `structured` |
| 14 | [Haystack](https://github.com/deepset-ai/haystack) | 🟡 **51.9** | 26.8k | 📈 +74 | 0 | 4 days ago | `pipeline` |
| 15 | [Semantic Kernel](https://github.com/microsoft/semantic-kernel) | 🟡 **49.4** | 28.7k | 📈 +24 | 0 | 19 days ago | `enterprise` |
| 16 | [Letta](https://github.com/letta-ai/letta) | 🟠 **35.2** | 25.3k | 📈 +73 | 1 | 5 mo ago | `memory` |
| 17 | [Smolagents](https://github.com/huggingface/smolagents) | 🟠 **34.2** | 30.1k | 🚀 +143 | 1 | 5 mo ago | `lightweight` |
| 18 | [AutoGen](https://github.com/microsoft/autogen) | 🟠 **32.1** | 61.6k | 📈 +93 | 1 | 1y ago | `multi-agent` |
| 19 | [Swarm](https://github.com/openai/swarm) | 🔴 **9.3** | 22.1k | ↗️ +19 | 0 | — | `experimental` |

## 📂 By Category

- `data-agent`: **LlamaIndex** (54.7)
- `enterprise`: **Semantic Kernel** (49.4)
- `experimental`: **Swarm** (9.3)
- `lightweight`: **Smolagents** (34.2)
- `memory`: **Letta** (35.2)
- `multi-agent`: **CrewAI** (78.8), **Agno** (70.4), **AG2** (68.2), **AutoGen** (32.1)
- `optimization`: **DSPy** (58.9)
- `orchestration`: **LangGraph** (83.9), **Google ADK** (75.1), **Claude Agent SDK** (73.4), **OpenAI Agents SDK** (68.2)
- `pipeline`: **Haystack** (51.9)
- `structured`: **PydanticAI** (53.2)
- `tooling`: **Composio** (68.1)
- `typescript`: **Mastra** (76.6)
- `web-agent`: **BrowserUse** (89.4)

## 🔍 Top 5 — Score Breakdown

| Framework | Star Velocity | Release Freshness | Issue Health | Commit Activity | Community | Fork Ratio |
|-----------|:---:|:---:|:---:|:---:|:---:|:---:|
| **BrowserUse** | 100 | 96.7 | 89.3 | 100 | 72.0 | 44.5 |
| **LangGraph** | 84.1 | 99.3 | 79.0 | 93.0 | 57.0 | 68.7 |
| **CrewAI** | 51.2 | 99.3 | 86.6 | 100 | 72.0 | 59.2 |
| **Mastra** | 36.7 | 98.3 | 95.0 | 100 | 93.6 | 41.9 |
| **Google ADK** | 19.6 | 99.3 | 94.0 | 100 | 85.6 | 77.2 |

## 💡 Key Insights

- **Hottest framework**: BrowserUse with a Pulse Score of 89.4
- **Fastest growing**: Claude Agent SDK gained +1045 stars this week
- **Most active development**: Mastra with 1945 commits in the last 4 weeks
- **Stale releases**: AutoGen, Swarm haven't released in a while

## 📦 Recent Releases

- **CrewAI** [`1.15.30`](https://github.com/crewAIInc/crewAI/releases/tag/1.15.30) — 2 days ago
- **LangGraph** [`1.2.17`](https://github.com/langchain-ai/langgraph/releases/tag/1.2.17) — 2 days ago
- **Claude Agent SDK** [`v2.1.310`](https://github.com/anthropics/claude-code/releases/tag/v2.1.310) — 2 days ago
- **Composio** [`@composio/cli@0.5.1-beta.500`](https://github.com/ComposioHQ/composio/releases/tag/@composio/cli@0.5.1-beta.500) — 2 days ago *(pre-release)*
- **Google ADK** [`v2.13.0`](https://github.com/google/adk-python/releases/tag/v2.13.0) — 2 days ago
- **Agno** [`v3.1.10`](https://github.com/agno-agi/agno/releases/tag/v3.1.10) — 2 days ago
- **AG2** [`v1.2.1`](https://github.com/ag2ai/ag2/releases/tag/v1.2.1) — 4 days ago
- **Haystack** [`v3.4.1`](https://github.com/deepset-ai/haystack/releases/tag/v3.4.1) — 4 days ago
- **Mastra** [`@mastra/core@1.79.0`](https://github.com/mastra-ai/mastra/releases/tag/@mastra/core@1.79.0) — 5 days ago
- **BrowserUse** [`0.13.13`](https://github.com/browser-use/browser-use/releases/tag/0.13.13) — 10 days ago

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

*Powered by GitHub Actions • Data refreshed daily • Last run: 2026-10-26 12:35 UTC*