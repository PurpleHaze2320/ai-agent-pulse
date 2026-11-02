# 🔬 AI Agent Framework Pulse Tracker

[![Daily Update](https://github.com/PurpleHaze2320/ai-agent-pulse/actions/workflows/track.yml/badge.svg)](https://github.com/PurpleHaze2320/ai-agent-pulse/actions/workflows/track.yml)
[![Frameworks Tracked](https://img.shields.io/badge/frameworks-19-blue)](https://github.com/PurpleHaze2320/ai-agent-pulse)
[![License: MIT](https://img.shields.io/badge/License-MIT-green.svg)](https://opensource.org/licenses/MIT)
[![GitHub stars](https://img.shields.io/github/stars/PurpleHaze2320/ai-agent-pulse?style=social)](https://github.com/PurpleHaze2320/ai-agent-pulse/stargazers)

> Automated daily tracking of the AI agent framework ecosystem's health, momentum, and trends.
> Last updated: **2026-11-02 15:15 UTC** | Tracking **19** frameworks

## How It Works

This bot runs daily via GitHub Actions and collects metrics from the GitHub API for the most important
AI agent frameworks. It computes a **Pulse Score** (0-100) based on six weighted signals: star velocity,
release freshness, issue health, commit activity, community size, and fork engagement. The result is
a living dashboard that shows which frameworks are gaining momentum and which are losing steam.

## 🏆 Pulse Leaderboard

| Rank | Framework | Pulse | Stars | ⭐ 7d | Commits (4w) | Last Release | Category |
|------|-----------|-------|-------|-------|--------------|--------------|----------|
| 1 | [BrowserUse](https://github.com/browser-use/browser-use) | 🟢 **89.7** | 119.8k | 🚀 +655 | 107 | 6 days ago | `web-agent` |
| 2 | [LangGraph](https://github.com/langchain-ai/langgraph) | 🟢 **85.3** | 44.3k | 🚀 +408 | 109 | 2 days ago | `orchestration` |
| 3 | [CrewAI](https://github.com/crewAIInc/crewAI) | 🟢 **80.9** | 60.4k | 🚀 +305 | 172 | today | `multi-agent` |
| 4 | [Mastra](https://github.com/mastra-ai/mastra) | 🟢 **77.2** | 29.3k | 🚀 +192 | 1991 | today | `typescript` |
| 5 | [Claude Agent SDK](https://github.com/anthropics/claude-code) | 🟢 **73.4** | 154.3k | 🚀 +838 | 40 | 2 days ago | `orchestration` |
| 6 | [Haystack](https://github.com/deepset-ai/haystack) | 🟢 **71.2** | 26.9k | 📈 +64 | 173 | 11 days ago | `pipeline` |
| 7 | [Agno](https://github.com/agno-agi/agno) | 🟢 **70.9** | 43.0k | 🚀 +117 | 142 | 4 days ago | `multi-agent` |
| 8 | [AG2](https://github.com/ag2ai/ag2) | 🟢 **70.0** | 5.0k | 📈 +22 | 106 | 5 days ago | `multi-agent` |
| 9 | [OpenAI Agents SDK](https://github.com/openai/openai-agents-python) | 🟡 **68.6** | 30.5k | 🚀 +164 | 62 | 18 days ago | `orchestration` |
| 10 | [Composio](https://github.com/ComposioHQ/composio) | 🟡 **68.4** | 30.9k | 🚀 +118 | 342 | today | `tooling` |
| 11 | [Semantic Kernel](https://github.com/microsoft/semantic-kernel) | 🟡 **65.7** | 28.7k | 📈 +27 | 72 | 5 days ago | `enterprise` |
| 12 | [LlamaIndex](https://github.com/run-llama/llama_index) | 🟡 **53.9** | 52.8k | 🚀 +107 | 6 | 1 mo ago | `data-agent` |
| 13 | [Google ADK](https://github.com/google/adk-python) | 🟡 **53.8** | 22.1k | 📈 +71 | 0 | 9 days ago | `orchestration` |
| 14 | [PydanticAI](https://github.com/pydantic/pydantic-ai) | 🟡 **50.8** | 21.0k | 🚀 +115 | 0 | 27 days ago | `structured` |
| 15 | [DSPy](https://github.com/stanfordnlp/dspy) | 🟡 **47.1** | 38.9k | 📈 +86 | 0 | 20 days ago | `optimization` |
| 16 | [Letta](https://github.com/letta-ai/letta) | 🟠 **34.1** | 25.3k | 📈 +61 | 1 | 5 mo ago | `memory` |
| 17 | [AutoGen](https://github.com/microsoft/autogen) | 🟠 **32.9** | 61.7k | 🚀 +106 | 2 | 1y ago | `multi-agent` |
| 18 | [Smolagents](https://github.com/huggingface/smolagents) | 🟠 **32.6** | 30.2k | 🚀 +122 | 0 | 5 mo ago | `lightweight` |
| 19 | [Swarm](https://github.com/openai/swarm) | 🔴 **9.0** | 22.1k | ↗️ +13 | 0 | — | `experimental` |

## 📂 By Category

- `data-agent`: **LlamaIndex** (53.9)
- `enterprise`: **Semantic Kernel** (65.7)
- `experimental`: **Swarm** (9.0)
- `lightweight`: **Smolagents** (32.6)
- `memory`: **Letta** (34.1)
- `multi-agent`: **CrewAI** (80.9), **Agno** (70.9), **AG2** (70.0), **AutoGen** (32.9)
- `optimization`: **DSPy** (47.1)
- `orchestration`: **LangGraph** (85.3), **Claude Agent SDK** (73.4), **OpenAI Agents SDK** (68.6), **Google ADK** (53.8)
- `pipeline`: **Haystack** (71.2)
- `structured`: **PydanticAI** (50.8)
- `tooling`: **Composio** (68.4)
- `typescript`: **Mastra** (77.2)
- `web-agent`: **BrowserUse** (89.7)

## 🔍 Top 5 — Score Breakdown

| Framework | Star Velocity | Release Freshness | Issue Health | Commit Activity | Community | Fork Ratio |
|-----------|:---:|:---:|:---:|:---:|:---:|:---:|
| **BrowserUse** | 100 | 98.0 | 89.7 | 100 | 72.2 | 44.6 |
| **LangGraph** | 82.3 | 99.3 | 81.6 | 100 | 57.4 | 68.8 |
| **CrewAI** | 59.4 | 100.0 | 85.3 | 100 | 72.6 | 59.6 |
| **Mastra** | 38.2 | 100.0 | 94.3 | 100 | 93.4 | 41.9 |
| **Claude Agent SDK** | 100 | 99.3 | 85.0 | 40.0 | 11.4 | 66.2 |

## 💡 Key Insights

- **Hottest framework**: BrowserUse with a Pulse Score of 89.7
- **Fastest growing**: Claude Agent SDK gained +838 stars this week
- **Most active development**: Mastra with 1991 commits in the last 4 weeks
- **Stale releases**: AutoGen, Swarm haven't released in a while

## 📦 Recent Releases

- **Mastra** [`@mastra/core@1.81.0`](https://github.com/mastra-ai/mastra/releases/tag/@mastra/core@1.81.0) — today
- **Composio** [`@composio/cli@0.6.0`](https://github.com/ComposioHQ/composio/releases/tag/@composio/cli@0.6.0) — today
- **CrewAI** [`1.15.34`](https://github.com/crewAIInc/crewAI/releases/tag/1.15.34) — today
- **Claude Agent SDK** [`v2.1.316`](https://github.com/anthropics/claude-code/releases/tag/v2.1.316) — 2 days ago
- **LangGraph** [`1.2.19`](https://github.com/langchain-ai/langgraph/releases/tag/1.2.19) — 2 days ago
- **Agno** [`v3.1.12`](https://github.com/agno-agi/agno/releases/tag/v3.1.12) — 4 days ago
- **Semantic Kernel** [`python-1.46.0`](https://github.com/microsoft/semantic-kernel/releases/tag/python-1.46.0) — 5 days ago
- **AG2** [`v1.2.2`](https://github.com/ag2ai/ag2/releases/tag/v1.2.2) — 5 days ago
- **BrowserUse** [`0.13.14`](https://github.com/browser-use/browser-use/releases/tag/0.13.14) — 6 days ago
- **Google ADK** [`v2.13.0`](https://github.com/google/adk-python/releases/tag/v2.13.0) — 9 days ago

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

*Powered by GitHub Actions • Data refreshed daily • Last run: 2026-11-02 15:15 UTC*