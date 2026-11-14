# 🔬 AI Agent Framework Pulse Tracker

[![Daily Update](https://github.com/PurpleHaze2320/ai-agent-pulse/actions/workflows/track.yml/badge.svg)](https://github.com/PurpleHaze2320/ai-agent-pulse/actions/workflows/track.yml)
[![Frameworks Tracked](https://img.shields.io/badge/frameworks-19-blue)](https://github.com/PurpleHaze2320/ai-agent-pulse)
[![License: MIT](https://img.shields.io/badge/License-MIT-green.svg)](https://opensource.org/licenses/MIT)
[![GitHub stars](https://img.shields.io/github/stars/PurpleHaze2320/ai-agent-pulse?style=social)](https://github.com/PurpleHaze2320/ai-agent-pulse/stargazers)

> Automated daily tracking of the AI agent framework ecosystem's health, momentum, and trends.
> Last updated: **2026-11-14 13:16 UTC** | Tracking **19** frameworks

## How It Works

This bot runs daily via GitHub Actions and collects metrics from the GitHub API for the most important
AI agent frameworks. It computes a **Pulse Score** (0-100) based on six weighted signals: star velocity,
release freshness, issue health, commit activity, community size, and fork engagement. The result is
a living dashboard that shows which frameworks are gaining momentum and which are losing steam.

## 🏆 Pulse Leaderboard

| Rank | Framework | Pulse | Stars | ⭐ 7d | Commits (4w) | Last Release | Category |
|------|-----------|-------|-------|-------|--------------|--------------|----------|
| 1 | [BrowserUse](https://github.com/browser-use/browser-use) | 🟢 **90.3** | 121.0k | 🚀 +752 | 1137 | today | `web-agent` |
| 2 | [LangGraph](https://github.com/langchain-ai/langgraph) | 🟢 **82.8** | 45.0k | 🚀 +340 | 125 | today | `orchestration` |
| 3 | [CrewAI](https://github.com/crewAIInc/crewAI) | 🟢 **79.9** | 60.9k | 🚀 +280 | 213 | 1 day ago | `multi-agent` |
| 4 | [Claude Agent SDK](https://github.com/anthropics/claude-code) | 🟢 **79.8** | 155.6k | 🚀 +764 | 73 | today | `orchestration` |
| 5 | [Google ADK](https://github.com/google/adk-python) | 🟢 **74.5** | 22.2k | 📈 +80 | 417 | 1 day ago | `orchestration` |
| 6 | [Mastra](https://github.com/mastra-ai/mastra) | 🟢 **74.4** | 29.5k | 🚀 +120 | 2569 | today | `typescript` |
| 7 | [Haystack](https://github.com/deepset-ai/haystack) | 🟢 **71.8** | 27.0k | 📈 +62 | 266 | 4 days ago | `pipeline` |
| 8 | [PydanticAI](https://github.com/pydantic/pydantic-ai) | 🟢 **70.6** | 21.2k | 🚀 +132 | 1259 | 1 mo ago | `structured` |
| 9 | [OpenAI Agents SDK](https://github.com/openai/openai-agents-python) | 🟢 **70.6** | 30.7k | 🚀 +131 | 74 | 6 days ago | `orchestration` |
| 10 | [Agno](https://github.com/agno-agi/agno) | 🟢 **70.4** | 43.2k | 📈 +95 | 165 | 1 day ago | `multi-agent` |
| 11 | [AG2](https://github.com/ag2ai/ag2) | 🟢 **70.0** | 5.1k | ↗️ +15 | 134 | 3 days ago | `multi-agent` |
| 12 | [Semantic Kernel](https://github.com/microsoft/semantic-kernel) | 🟡 **69.0** | 28.8k | ↗️ +19 | 90 | 7 days ago | `enterprise` |
| 13 | [Composio](https://github.com/ComposioHQ/composio) | 🟡 **68.2** | 31.1k | 🚀 +107 | 336 | today | `tooling` |
| 14 | [DSPy](https://github.com/stanfordnlp/dspy) | 🟡 **66.5** | 39.0k | 📈 +83 | 92 | 3 days ago | `optimization` |
| 15 | [LlamaIndex](https://github.com/run-llama/llama_index) | 🟡 **55.3** | 52.9k | 📈 +59 | 8 | today | `data-agent` |
| 16 | [Letta](https://github.com/letta-ai/letta) | 🟠 **33.2** | 25.4k | 📈 +61 | 1 | 6 mo ago | `memory` |
| 17 | [AutoGen](https://github.com/microsoft/autogen) | 🟠 **31.7** | 61.8k | 📈 +77 | 2 | 1y ago | `multi-agent` |
| 18 | [Smolagents](https://github.com/huggingface/smolagents) | 🟠 **31.4** | 30.4k | 🚀 +116 | 0 | 5 mo ago | `lightweight` |
| 19 | [Swarm](https://github.com/openai/swarm) | 🔴 **9.6** | 22.1k | 📈 +26 | 0 | — | `experimental` |

## 📂 By Category

- `data-agent`: **LlamaIndex** (55.3)
- `enterprise`: **Semantic Kernel** (69.0)
- `experimental`: **Swarm** (9.6)
- `lightweight`: **Smolagents** (31.4)
- `memory`: **Letta** (33.2)
- `multi-agent`: **CrewAI** (79.9), **Agno** (70.4), **AG2** (70.0), **AutoGen** (31.7)
- `optimization`: **DSPy** (66.5)
- `orchestration`: **LangGraph** (82.8), **Claude Agent SDK** (79.8), **Google ADK** (74.5), **OpenAI Agents SDK** (70.6)
- `pipeline`: **Haystack** (71.8)
- `structured`: **PydanticAI** (70.6)
- `tooling`: **Composio** (68.2)
- `typescript`: **Mastra** (74.4)
- `web-agent`: **BrowserUse** (90.3)

## 🔍 Top 5 — Score Breakdown

| Framework | Star Velocity | Release Freshness | Issue Health | Commit Activity | Community | Fork Ratio |
|-----------|:---:|:---:|:---:|:---:|:---:|:---:|
| **BrowserUse** | 100 | 100.0 | 90.3 | 100 | 72.4 | 44.7 |
| **LangGraph** | 72.3 | 100.0 | 80.1 | 100 | 57.6 | 69.0 |
| **CrewAI** | 56.6 | 99.7 | 82.9 | 100 | 73.6 | 60.3 |
| **Claude Agent SDK** | 100 | 100.0 | 84.5 | 73.0 | 11.2 | 64.2 |
| **Google ADK** | 16.5 | 99.7 | 93.7 | 100 | 86.0 | 78.4 |

## 💡 Key Insights

- **Hottest framework**: BrowserUse with a Pulse Score of 90.3
- **Fastest growing**: Claude Agent SDK gained +764 stars this week
- **Most active development**: Mastra with 2569 commits in the last 4 weeks
- **Stale releases**: AutoGen, Swarm haven't released in a while

## 📦 Recent Releases

- **BrowserUse** [`1.0.5`](https://github.com/browser-use/browser-use/releases/tag/1.0.5) — today
- **LangGraph** [`1.2.22`](https://github.com/langchain-ai/langgraph/releases/tag/1.2.22) — today
- **LlamaIndex** [`v0.14.26`](https://github.com/run-llama/llama_index/releases/tag/v0.14.26) — today
- **Claude Agent SDK** [`v2.1.325`](https://github.com/anthropics/claude-code/releases/tag/v2.1.325) — today
- **Composio** [`@composio/cli@0.6.1`](https://github.com/ComposioHQ/composio/releases/tag/@composio/cli@0.6.1) — today
- **Mastra** [`@mastra/core@1.83.0`](https://github.com/mastra-ai/mastra/releases/tag/@mastra/core@1.83.0) — today
- **Google ADK** [`v2.14.1`](https://github.com/google/adk-python/releases/tag/v2.14.1) — 1 day ago
- **CrewAI** [`1.15.41`](https://github.com/crewAIInc/crewAI/releases/tag/1.15.41) — 1 day ago
- **Agno** [`v3.2.0`](https://github.com/agno-agi/agno/releases/tag/v3.2.0) — 1 day ago
- **AG2** [`v.1.3.1`](https://github.com/ag2ai/ag2/releases/tag/v.1.3.1) — 3 days ago

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

*Powered by GitHub Actions • Data refreshed daily • Last run: 2026-11-14 13:16 UTC*