# 🔬 AI Agent Framework Pulse Tracker

[![Daily Update](https://github.com/PurpleHaze2320/ai-agent-pulse/actions/workflows/track.yml/badge.svg)](https://github.com/PurpleHaze2320/ai-agent-pulse/actions/workflows/track.yml)
[![Frameworks Tracked](https://img.shields.io/badge/frameworks-19-blue)](https://github.com/PurpleHaze2320/ai-agent-pulse)
[![License: MIT](https://img.shields.io/badge/License-MIT-green.svg)](https://opensource.org/licenses/MIT)
[![GitHub stars](https://img.shields.io/github/stars/PurpleHaze2320/ai-agent-pulse?style=social)](https://github.com/PurpleHaze2320/ai-agent-pulse/stargazers)

> Automated daily tracking of the AI agent framework ecosystem's health, momentum, and trends.
> Last updated: **2026-10-18 10:42 UTC** | Tracking **19** frameworks

## How It Works

This bot runs daily via GitHub Actions and collects metrics from the GitHub API for the most important
AI agent frameworks. It computes a **Pulse Score** (0-100) based on six weighted signals: star velocity,
release freshness, issue health, commit activity, community size, and fork engagement. The result is
a living dashboard that shows which frameworks are gaining momentum and which are losing steam.

## 🏆 Pulse Leaderboard

| Rank | Framework | Pulse | Stars | ⭐ 7d | Commits (4w) | Last Release | Category |
|------|-----------|-------|-------|-------|--------------|--------------|----------|
| 1 | [BrowserUse](https://github.com/browser-use/browser-use) | 🟢 **89.9** | 118.4k | 🚀 +759 | 142 | 2 days ago | `web-agent` |
| 2 | [LangGraph](https://github.com/langchain-ai/langgraph) | 🟢 **82.0** | 43.4k | 🚀 +381 | 96 | 1 day ago | `orchestration` |
| 3 | [OpenAI Agents SDK](https://github.com/openai/openai-agents-python) | 🟢 **76.7** | 30.1k | 🚀 +149 | 133 | 3 days ago | `orchestration` |
| 4 | [Mastra](https://github.com/mastra-ai/mastra) | 🟢 **76.5** | 28.9k | 🚀 +177 | 1677 | 2 days ago | `typescript` |
| 5 | [Google ADK](https://github.com/google/adk-python) | 🟢 **75.9** | 21.9k | 🚀 +123 | 428 | 4 days ago | `orchestration` |
| 6 | [Claude Agent SDK](https://github.com/anthropics/claude-code) | 🟢 **75.2** | 152.2k | 🚀 +2058 | 46 | 1 day ago | `orchestration` |
| 7 | [CrewAI](https://github.com/crewAIInc/crewAI) | 🟢 **74.5** | 59.8k | 🚀 +266 | 77 | 4 days ago | `multi-agent` |
| 8 | [PydanticAI](https://github.com/pydantic/pydantic-ai) | 🟢 **73.5** | 20.7k | 🚀 +155 | 737 | 12 days ago | `structured` |
| 9 | [Agno](https://github.com/agno-agi/agno) | 🟢 **71.0** | 42.8k | 🚀 +128 | 96 | 1 day ago | `multi-agent` |
| 10 | [Haystack](https://github.com/deepset-ai/haystack) | 🟢 **70.9** | 26.8k | 📈 +47 | 200 | 3 days ago | `pipeline` |
| 11 | [AG2](https://github.com/ag2ai/ag2) | 🟡 **69.3** | 5.0k | ↗️ +12 | 105 | 7 days ago | `multi-agent` |
| 12 | [Composio](https://github.com/ComposioHQ/composio) | 🟡 **68.5** | 30.6k | 🚀 +130 | 253 | 2 days ago | `tooling` |
| 13 | [DSPy](https://github.com/stanfordnlp/dspy) | 🟡 **57.9** | 38.7k | 📈 +84 | 48 | 5 days ago | `optimization` |
| 14 | [LlamaIndex](https://github.com/run-llama/llama_index) | 🟡 **55.8** | 52.5k | 📈 +85 | 15 | 26 days ago | `data-agent` |
| 15 | [Semantic Kernel](https://github.com/microsoft/semantic-kernel) | 🟡 **54.6** | 28.7k | 📈 +27 | 23 | 11 days ago | `enterprise` |
| 16 | [Letta](https://github.com/letta-ai/letta) | 🟠 **35.6** | 25.2k | 📈 +74 | 0 | 5 mo ago | `memory` |
| 17 | [Smolagents](https://github.com/huggingface/smolagents) | 🟠 **34.5** | 29.9k | 🚀 +126 | 3 | 4 mo ago | `lightweight` |
| 18 | [AutoGen](https://github.com/microsoft/autogen) | 🟠 **32.7** | 61.5k | 🚀 +108 | 1 | 1y ago | `multi-agent` |
| 19 | [Swarm](https://github.com/openai/swarm) | 🔴 **9.2** | 22.1k | ↗️ +12 | 0 | — | `experimental` |

## 📂 By Category

- `data-agent`: **LlamaIndex** (55.8)
- `enterprise`: **Semantic Kernel** (54.6)
- `experimental`: **Swarm** (9.2)
- `lightweight`: **Smolagents** (34.5)
- `memory`: **Letta** (35.6)
- `multi-agent`: **CrewAI** (74.5), **Agno** (71.0), **AG2** (69.3), **AutoGen** (32.7)
- `optimization`: **DSPy** (57.9)
- `orchestration`: **LangGraph** (82.0), **OpenAI Agents SDK** (76.7), **Google ADK** (75.9), **Claude Agent SDK** (75.2)
- `pipeline`: **Haystack** (70.9)
- `structured`: **PydanticAI** (73.5)
- `tooling`: **Composio** (68.5)
- `typescript`: **Mastra** (76.5)
- `web-agent`: **BrowserUse** (89.9)

## 🔍 Top 5 — Score Breakdown

| Framework | Star Velocity | Release Freshness | Issue Health | Commit Activity | Community | Fork Ratio |
|-----------|:---:|:---:|:---:|:---:|:---:|:---:|
| **BrowserUse** | 100 | 99.3 | 89.5 | 100 | 72.2 | 44.4 |
| **LangGraph** | 76.8 | 99.7 | 74.4 | 96.0 | 56.6 | 68.2 |
| **OpenAI Agents SDK** | 29.4 | 99.0 | 99.4 | 100 | 80.2 | 66.3 |
| **Mastra** | 35.6 | 99.3 | 95.0 | 100 | 93.4 | 41.5 |
| **Google ADK** | 22.2 | 98.7 | 94.8 | 100 | 86.0 | 78.4 |

## 💡 Key Insights

- **Hottest framework**: BrowserUse with a Pulse Score of 89.9
- **Fastest growing**: Claude Agent SDK gained +2058 stars this week
- **Most active development**: Mastra with 1677 commits in the last 4 weeks
- **Stale releases**: AutoGen, Swarm haven't released in a while

## 📦 Recent Releases

- **LangGraph** [`1.2.16`](https://github.com/langchain-ai/langgraph/releases/tag/1.2.16) — 1 day ago
- **Claude Agent SDK** [`v2.1.302`](https://github.com/anthropics/claude-code/releases/tag/v2.1.302) — 1 day ago
- **Agno** [`v3.1.4`](https://github.com/agno-agi/agno/releases/tag/v3.1.4) — 1 day ago
- **Composio** [`@composio/cli@0.4.6-beta.457`](https://github.com/ComposioHQ/composio/releases/tag/@composio/cli@0.4.6-beta.457) — 2 days ago *(pre-release)*
- **Mastra** [`@mastra/core@1.78.0`](https://github.com/mastra-ai/mastra/releases/tag/@mastra/core@1.78.0) — 2 days ago
- **BrowserUse** [`0.13.13`](https://github.com/browser-use/browser-use/releases/tag/0.13.13) — 2 days ago
- **Haystack** [`v3.4.0`](https://github.com/deepset-ai/haystack/releases/tag/v3.4.0) — 3 days ago
- **OpenAI Agents SDK** [`v0.24.0`](https://github.com/openai/openai-agents-python/releases/tag/v0.24.0) — 3 days ago
- **CrewAI** [`1.15.28`](https://github.com/crewAIInc/crewAI/releases/tag/1.15.28) — 4 days ago
- **Google ADK** [`v2.12.0`](https://github.com/google/adk-python/releases/tag/v2.12.0) — 4 days ago

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

*Powered by GitHub Actions • Data refreshed daily • Last run: 2026-10-18 10:42 UTC*