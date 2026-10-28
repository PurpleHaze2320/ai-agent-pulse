# 🔬 AI Agent Framework Pulse Tracker

[![Daily Update](https://github.com/PurpleHaze2320/ai-agent-pulse/actions/workflows/track.yml/badge.svg)](https://github.com/PurpleHaze2320/ai-agent-pulse/actions/workflows/track.yml)
[![Frameworks Tracked](https://img.shields.io/badge/frameworks-19-blue)](https://github.com/PurpleHaze2320/ai-agent-pulse)
[![License: MIT](https://img.shields.io/badge/License-MIT-green.svg)](https://opensource.org/licenses/MIT)
[![GitHub stars](https://img.shields.io/github/stars/PurpleHaze2320/ai-agent-pulse?style=social)](https://github.com/PurpleHaze2320/ai-agent-pulse/stargazers)

> Automated daily tracking of the AI agent framework ecosystem's health, momentum, and trends.
> Last updated: **2026-10-28 12:28 UTC** | Tracking **19** frameworks

## How It Works

This bot runs daily via GitHub Actions and collects metrics from the GitHub API for the most important
AI agent frameworks. It computes a **Pulse Score** (0-100) based on six weighted signals: star velocity,
release freshness, issue health, commit activity, community size, and fork engagement. The result is
a living dashboard that shows which frameworks are gaining momentum and which are losing steam.

## 🏆 Pulse Leaderboard

| Rank | Framework | Pulse | Stars | ⭐ 7d | Commits (4w) | Last Release | Category |
|------|-----------|-------|-------|-------|--------------|--------------|----------|
| 1 | [BrowserUse](https://github.com/browser-use/browser-use) | 🟢 **90.0** | 119.4k | 🚀 +621 | 116 | 1 day ago | `web-agent` |
| 2 | [LangGraph](https://github.com/langchain-ai/langgraph) | 🟢 **84.8** | 44.0k | 🚀 +405 | 116 | 1 day ago | `orchestration` |
| 3 | [CrewAI](https://github.com/crewAIInc/crewAI) | 🟢 **79.3** | 60.2k | 🚀 +261 | 170 | today | `multi-agent` |
| 4 | [Mastra](https://github.com/mastra-ai/mastra) | 🟢 **76.2** | 29.1k | 🚀 +172 | 2163 | 6 days ago | `typescript` |
| 5 | [Claude Agent SDK](https://github.com/anthropics/claude-code) | 🟢 **74.9** | 153.7k | 🚀 +1013 | 46 | today | `orchestration` |
| 6 | [OpenAI Agents SDK](https://github.com/openai/openai-agents-python) | 🟢 **73.6** | 30.4k | 🚀 +157 | 86 | 13 days ago | `orchestration` |
| 7 | [PydanticAI](https://github.com/pydantic/pydantic-ai) | 🟢 **73.1** | 20.9k | 🚀 +157 | 1063 | 22 days ago | `structured` |
| 8 | [Haystack](https://github.com/deepset-ai/haystack) | 🟢 **71.4** | 26.9k | 📈 +65 | 221 | 6 days ago | `pipeline` |
| 9 | [Agno](https://github.com/agno-agi/agno) | 🟢 **70.2** | 42.9k | 📈 +82 | 159 | today | `multi-agent` |
| 10 | [AG2](https://github.com/ag2ai/ag2) | 🟢 **70.1** | 5.0k | ↗️ +17 | 104 | today | `multi-agent` |
| 11 | [Composio](https://github.com/ComposioHQ/composio) | 🟡 **68.4** | 30.8k | 🚀 +122 | 324 | today | `tooling` |
| 12 | [Semantic Kernel](https://github.com/microsoft/semantic-kernel) | 🟡 **63.3** | 28.7k | 📈 +29 | 66 | 21 days ago | `enterprise` |
| 13 | [DSPy](https://github.com/stanfordnlp/dspy) | 🟡 **61.5** | 38.8k | 🚀 +116 | 66 | 15 days ago | `optimization` |
| 14 | [LlamaIndex](https://github.com/run-llama/llama_index) | 🟡 **55.0** | 52.7k | 🚀 +111 | 9 | 1 mo ago | `data-agent` |
| 15 | [Google ADK](https://github.com/google/adk-python) | 🟡 **54.8** | 22.0k | 📈 +91 | 0 | 4 days ago | `orchestration` |
| 16 | [Smolagents](https://github.com/huggingface/smolagents) | 🟠 **34.7** | 30.1k | 🚀 +160 | 1 | 5 mo ago | `lightweight` |
| 17 | [Letta](https://github.com/letta-ai/letta) | 🟠 **34.3** | 25.3k | 📈 +57 | 1 | 5 mo ago | `memory` |
| 18 | [AutoGen](https://github.com/microsoft/autogen) | 🟠 **32.3** | 61.6k | 📈 +98 | 1 | 1y ago | `multi-agent` |
| 19 | [Swarm](https://github.com/openai/swarm) | 🔴 **9.4** | 22.1k | 📈 +21 | 0 | — | `experimental` |

## 📂 By Category

- `data-agent`: **LlamaIndex** (55.0)
- `enterprise`: **Semantic Kernel** (63.3)
- `experimental`: **Swarm** (9.4)
- `lightweight`: **Smolagents** (34.7)
- `memory`: **Letta** (34.3)
- `multi-agent`: **CrewAI** (79.3), **Agno** (70.2), **AG2** (70.1), **AutoGen** (32.3)
- `optimization`: **DSPy** (61.5)
- `orchestration`: **LangGraph** (84.8), **Claude Agent SDK** (74.9), **OpenAI Agents SDK** (73.6), **Google ADK** (54.8)
- `pipeline`: **Haystack** (71.4)
- `structured`: **PydanticAI** (73.1)
- `tooling`: **Composio** (68.4)
- `typescript`: **Mastra** (76.2)
- `web-agent`: **BrowserUse** (90.0)

## 🔍 Top 5 — Score Breakdown

| Framework | Star Velocity | Release Freshness | Issue Health | Commit Activity | Community | Fork Ratio |
|-----------|:---:|:---:|:---:|:---:|:---:|:---:|
| **BrowserUse** | 100 | 99.7 | 89.1 | 100 | 72.2 | 44.5 |
| **LangGraph** | 81.2 | 99.7 | 79.7 | 100 | 57.4 | 68.7 |
| **CrewAI** | 52.6 | 100.0 | 86.3 | 100 | 72.6 | 59.3 |
| **Mastra** | 35.5 | 98.0 | 94.8 | 100 | 93.6 | 41.9 |
| **Claude Agent SDK** | 100 | 100.0 | 85.2 | 46.0 | 11.4 | 67.8 |

## 💡 Key Insights

- **Hottest framework**: BrowserUse with a Pulse Score of 90.0
- **Fastest growing**: Claude Agent SDK gained +1013 stars this week
- **Most active development**: Mastra with 2163 commits in the last 4 weeks
- **Stale releases**: AutoGen, Swarm haven't released in a while

## 📦 Recent Releases

- **Composio** [`@composio/cli@0.5.1-beta.512`](https://github.com/ComposioHQ/composio/releases/tag/@composio/cli@0.5.1-beta.512) — today *(pre-release)*
- **CrewAI** [`1.15.32`](https://github.com/crewAIInc/crewAI/releases/tag/1.15.32) — today
- **AG2** [`v1.2.2`](https://github.com/ag2ai/ag2/releases/tag/v1.2.2) — today
- **Claude Agent SDK** [`v2.1.312`](https://github.com/anthropics/claude-code/releases/tag/v2.1.312) — today
- **Agno** [`v3.1.11`](https://github.com/agno-agi/agno/releases/tag/v3.1.11) — today
- **BrowserUse** [`0.13.14`](https://github.com/browser-use/browser-use/releases/tag/0.13.14) — 1 day ago
- **LangGraph** [`1.2.18`](https://github.com/langchain-ai/langgraph/releases/tag/1.2.18) — 1 day ago
- **Google ADK** [`v2.13.0`](https://github.com/google/adk-python/releases/tag/v2.13.0) — 4 days ago
- **Haystack** [`v3.4.1`](https://github.com/deepset-ai/haystack/releases/tag/v3.4.1) — 6 days ago
- **Mastra** [`@mastra/core@1.79.0`](https://github.com/mastra-ai/mastra/releases/tag/@mastra/core@1.79.0) — 6 days ago

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

*Powered by GitHub Actions • Data refreshed daily • Last run: 2026-10-28 12:28 UTC*