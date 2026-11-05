# 🔬 AI Agent Framework Pulse Tracker

[![Daily Update](https://github.com/PurpleHaze2320/ai-agent-pulse/actions/workflows/track.yml/badge.svg)](https://github.com/PurpleHaze2320/ai-agent-pulse/actions/workflows/track.yml)
[![Frameworks Tracked](https://img.shields.io/badge/frameworks-19-blue)](https://github.com/PurpleHaze2320/ai-agent-pulse)
[![License: MIT](https://img.shields.io/badge/License-MIT-green.svg)](https://opensource.org/licenses/MIT)
[![GitHub stars](https://img.shields.io/github/stars/PurpleHaze2320/ai-agent-pulse?style=social)](https://github.com/PurpleHaze2320/ai-agent-pulse/stargazers)

> Automated daily tracking of the AI agent framework ecosystem's health, momentum, and trends.
> Last updated: **2026-11-05 14:24 UTC** | Tracking **19** frameworks

## How It Works

This bot runs daily via GitHub Actions and collects metrics from the GitHub API for the most important
AI agent frameworks. It computes a **Pulse Score** (0-100) based on six weighted signals: star velocity,
release freshness, issue health, commit activity, community size, and fork engagement. The result is
a living dashboard that shows which frameworks are gaining momentum and which are losing steam.

## 🏆 Pulse Leaderboard

| Rank | Framework | Pulse | Stars | ⭐ 7d | Commits (4w) | Last Release | Category |
|------|-----------|-------|-------|-------|--------------|--------------|----------|
| 1 | [BrowserUse](https://github.com/browser-use/browser-use) | 🟢 **89.5** | 120.1k | 🚀 +644 | 107 | 9 days ago | `web-agent` |
| 2 | [LangGraph](https://github.com/langchain-ai/langgraph) | 🟢 **86.1** | 44.5k | 🚀 +422 | 123 | today | `orchestration` |
| 3 | [CrewAI](https://github.com/crewAIInc/crewAI) | 🟢 **80.1** | 60.5k | 🚀 +287 | 181 | 1 day ago | `multi-agent` |
| 4 | [Mastra](https://github.com/mastra-ai/mastra) | 🟢 **76.3** | 29.4k | 🚀 +169 | 2306 | 1 day ago | `typescript` |
| 5 | [Claude Agent SDK](https://github.com/anthropics/claude-code) | 🟢 **74.4** | 154.6k | 🚀 +815 | 45 | 1 day ago | `orchestration` |
| 6 | [Google ADK](https://github.com/google/adk-python) | 🟢 **73.6** | 22.1k | 📈 +72 | 477 | 12 days ago | `orchestration` |
| 7 | [OpenAI Agents SDK](https://github.com/openai/openai-agents-python) | 🟢 **71.7** | 30.5k | 🚀 +143 | 75 | 1 day ago | `orchestration` |
| 8 | [Agno](https://github.com/agno-agi/agno) | 🟢 **70.8** | 43.1k | 🚀 +122 | 156 | 7 days ago | `multi-agent` |
| 9 | [AG2](https://github.com/ag2ai/ag2) | 🟢 **70.1** | 5.0k | ↗️ +14 | 124 | 1 day ago | `multi-agent` |
| 10 | [PydanticAI](https://github.com/pydantic/pydantic-ai) | 🟢 **70.0** | 21.0k | 📈 +94 | 1215 | 1 mo ago | `structured` |
| 11 | [Semantic Kernel](https://github.com/microsoft/semantic-kernel) | 🟡 **69.4** | 28.7k | 📈 +22 | 89 | today | `enterprise` |
| 12 | [Composio](https://github.com/ComposioHQ/composio) | 🟡 **69.0** | 30.9k | 🚀 +130 | 370 | today | `tooling` |
| 13 | [LlamaIndex](https://github.com/run-llama/llama_index) | 🟡 **53.4** | 52.8k | 📈 +90 | 7 | 1 mo ago | `data-agent` |
| 14 | [Haystack](https://github.com/deepset-ai/haystack) | 🟡 **51.4** | 26.9k | 📈 +55 | 0 | 2 days ago | `pipeline` |
| 15 | [DSPy](https://github.com/stanfordnlp/dspy) | 🟡 **47.1** | 38.9k | 📈 +91 | 0 | 23 days ago | `optimization` |
| 16 | [Letta](https://github.com/letta-ai/letta) | 🟠 **34.3** | 25.4k | 📈 +72 | 1 | 5 mo ago | `memory` |
| 17 | [AutoGen](https://github.com/microsoft/autogen) | 🟠 **32.4** | 61.7k | 📈 +90 | 2 | 1y ago | `multi-agent` |
| 18 | [Smolagents](https://github.com/huggingface/smolagents) | 🟠 **31.1** | 30.2k | 📈 +86 | 0 | 5 mo ago | `lightweight` |
| 19 | [Swarm](https://github.com/openai/swarm) | 🔴 **9.5** | 22.1k | 📈 +25 | 0 | — | `experimental` |

## 📂 By Category

- `data-agent`: **LlamaIndex** (53.4)
- `enterprise`: **Semantic Kernel** (69.4)
- `experimental`: **Swarm** (9.5)
- `lightweight`: **Smolagents** (31.1)
- `memory`: **Letta** (34.3)
- `multi-agent`: **CrewAI** (80.1), **Agno** (70.8), **AG2** (70.1), **AutoGen** (32.4)
- `optimization`: **DSPy** (47.1)
- `orchestration`: **LangGraph** (86.1), **Claude Agent SDK** (74.4), **Google ADK** (73.6), **OpenAI Agents SDK** (71.7)
- `pipeline`: **Haystack** (51.4)
- `structured`: **PydanticAI** (70.0)
- `tooling`: **Composio** (69.0)
- `typescript`: **Mastra** (76.3)
- `web-agent`: **BrowserUse** (89.5)

## 🔍 Top 5 — Score Breakdown

| Framework | Star Velocity | Release Freshness | Issue Health | Commit Activity | Community | Fork Ratio |
|-----------|:---:|:---:|:---:|:---:|:---:|:---:|
| **BrowserUse** | 100 | 97.0 | 89.5 | 100 | 72.2 | 44.6 |
| **LangGraph** | 85.1 | 100.0 | 81.0 | 100 | 57.4 | 68.8 |
| **CrewAI** | 57.3 | 99.7 | 83.8 | 100 | 72.6 | 59.9 |
| **Mastra** | 35.0 | 99.7 | 94.1 | 100 | 93.2 | 41.9 |
| **Claude Agent SDK** | 100 | 99.7 | 84.8 | 45.0 | 11.2 | 66.1 |

## 💡 Key Insights

- **Hottest framework**: BrowserUse with a Pulse Score of 89.5
- **Fastest growing**: Claude Agent SDK gained +815 stars this week
- **Most active development**: Mastra with 2306 commits in the last 4 weeks
- **Stale releases**: AutoGen, Swarm haven't released in a while

## 📦 Recent Releases

- **Semantic Kernel** [`python-1.47.0`](https://github.com/microsoft/semantic-kernel/releases/tag/python-1.47.0) — today
- **LangGraph** [`1.2.20`](https://github.com/langchain-ai/langgraph/releases/tag/1.2.20) — today
- **Composio** [`@composio/cli@0.6.1-beta.534`](https://github.com/ComposioHQ/composio/releases/tag/@composio/cli@0.6.1-beta.534) — today *(pre-release)*
- **Mastra** [`@mastra/core@1.82.0`](https://github.com/mastra-ai/mastra/releases/tag/@mastra/core@1.82.0) — 1 day ago
- **AG2** [`v1.3.0`](https://github.com/ag2ai/ag2/releases/tag/v1.3.0) — 1 day ago
- **Claude Agent SDK** [`v2.1.318`](https://github.com/anthropics/claude-code/releases/tag/v2.1.318) — 1 day ago
- **CrewAI** [`1.15.35`](https://github.com/crewAIInc/crewAI/releases/tag/1.15.35) — 1 day ago
- **OpenAI Agents SDK** [`v0.24.0-alpha.6`](https://github.com/openai/openai-agents-python/releases/tag/v0.24.0-alpha.6) — 1 day ago *(pre-release)*
- **Haystack** [`v2.31.1`](https://github.com/deepset-ai/haystack/releases/tag/v2.31.1) — 2 days ago
- **Agno** [`v3.1.12`](https://github.com/agno-agi/agno/releases/tag/v3.1.12) — 7 days ago

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

*Powered by GitHub Actions • Data refreshed daily • Last run: 2026-11-05 14:24 UTC*