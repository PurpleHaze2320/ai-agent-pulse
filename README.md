# 🔬 AI Agent Framework Pulse Tracker

[![Daily Update](https://github.com/PurpleHaze2320/ai-agent-pulse/actions/workflows/track.yml/badge.svg)](https://github.com/PurpleHaze2320/ai-agent-pulse/actions/workflows/track.yml)
[![Frameworks Tracked](https://img.shields.io/badge/frameworks-19-blue)](https://github.com/PurpleHaze2320/ai-agent-pulse)
[![License: MIT](https://img.shields.io/badge/License-MIT-green.svg)](https://opensource.org/licenses/MIT)
[![GitHub stars](https://img.shields.io/github/stars/PurpleHaze2320/ai-agent-pulse?style=social)](https://github.com/PurpleHaze2320/ai-agent-pulse/stargazers)

> Automated daily tracking of the AI agent framework ecosystem's health, momentum, and trends.
> Last updated: **2026-10-24 10:38 UTC** | Tracking **19** frameworks

## How It Works

This bot runs daily via GitHub Actions and collects metrics from the GitHub API for the most important
AI agent frameworks. It computes a **Pulse Score** (0-100) based on six weighted signals: star velocity,
release freshness, issue health, commit activity, community size, and fork engagement. The result is
a living dashboard that shows which frameworks are gaining momentum and which are losing steam.

## 🏆 Pulse Leaderboard

| Rank | Framework | Pulse | Stars | ⭐ 7d | Commits (4w) | Last Release | Category |
|------|-----------|-------|-------|-------|--------------|--------------|----------|
| 1 | [BrowserUse](https://github.com/browser-use/browser-use) | 🟢 **89.5** | 119.0k | 🚀 +748 | 147 | 8 days ago | `web-agent` |
| 2 | [LangGraph](https://github.com/langchain-ai/langgraph) | 🟢 **85.1** | 43.8k | 🚀 +421 | 120 | today | `orchestration` |
| 3 | [CrewAI](https://github.com/crewAIInc/crewAI) | 🟢 **79.4** | 60.1k | 🚀 +264 | 137 | today | `multi-agent` |
| 4 | [Claude Agent SDK](https://github.com/anthropics/claude-code) | 🟢 **77.7** | 153.2k | 🚀 +1907 | 59 | today | `orchestration` |
| 5 | [Mastra](https://github.com/mastra-ai/mastra) | 🟢 **76.9** | 29.0k | 🚀 +184 | 2372 | 2 days ago | `typescript` |
| 6 | [OpenAI Agents SDK](https://github.com/openai/openai-agents-python) | 🟢 **76.5** | 30.3k | 🚀 +158 | 144 | 9 days ago | `orchestration` |
| 7 | [Google ADK](https://github.com/google/adk-python) | 🟢 **75.1** | 22.0k | 📈 +94 | 534 | today | `orchestration` |
| 8 | [PydanticAI](https://github.com/pydantic/pydantic-ai) | 🟢 **74.4** | 20.8k | 🚀 +154 | 1120 | today | `structured` |
| 9 | [Haystack](https://github.com/deepset-ai/haystack) | 🟢 **71.8** | 26.8k | 📈 +68 | 266 | 2 days ago | `pipeline` |
| 10 | [Agno](https://github.com/agno-agi/agno) | 🟢 **70.9** | 42.9k | 🚀 +104 | 152 | today | `multi-agent` |
| 11 | [AG2](https://github.com/ag2ai/ag2) | 🟡 **69.7** | 5.0k | ↗️ +15 | 131 | 2 days ago | `multi-agent` |
| 12 | [Composio](https://github.com/ComposioHQ/composio) | 🟡 **68.0** | 30.7k | 🚀 +114 | 369 | today | `tooling` |
| 13 | [DSPy](https://github.com/stanfordnlp/dspy) | 🟡 **61.0** | 38.8k | 📈 +98 | 64 | 11 days ago | `optimization` |
| 14 | [LlamaIndex](https://github.com/run-llama/llama_index) | 🟡 **56.1** | 52.6k | 🚀 +105 | 15 | 1 mo ago | `data-agent` |
| 15 | [Semantic Kernel](https://github.com/microsoft/semantic-kernel) | 🟡 **55.8** | 28.7k | 📈 +25 | 31 | 17 days ago | `enterprise` |
| 16 | [Letta](https://github.com/letta-ai/letta) | 🟠 **35.3** | 25.2k | 📈 +72 | 1 | 5 mo ago | `memory` |
| 17 | [Smolagents](https://github.com/huggingface/smolagents) | 🟠 **34.2** | 30.0k | 🚀 +129 | 3 | 4 mo ago | `lightweight` |
| 18 | [AutoGen](https://github.com/microsoft/autogen) | 🟠 **32.3** | 61.5k | 📈 +98 | 1 | 1y ago | `multi-agent` |
| 19 | [Swarm](https://github.com/openai/swarm) | 🔴 **9.0** | 22.1k | ↗️ +12 | 0 | — | `experimental` |

## 📂 By Category

- `data-agent`: **LlamaIndex** (56.1)
- `enterprise`: **Semantic Kernel** (55.8)
- `experimental`: **Swarm** (9.0)
- `lightweight`: **Smolagents** (34.2)
- `memory`: **Letta** (35.3)
- `multi-agent`: **CrewAI** (79.4), **Agno** (70.9), **AG2** (69.7), **AutoGen** (32.3)
- `optimization`: **DSPy** (61.0)
- `orchestration`: **LangGraph** (85.1), **Claude Agent SDK** (77.7), **OpenAI Agents SDK** (76.5), **Google ADK** (75.1)
- `pipeline`: **Haystack** (71.8)
- `structured`: **PydanticAI** (74.4)
- `tooling`: **Composio** (68.0)
- `typescript`: **Mastra** (76.9)
- `web-agent`: **BrowserUse** (89.5)

## 🔍 Top 5 — Score Breakdown

| Framework | Star Velocity | Release Freshness | Issue Health | Commit Activity | Community | Fork Ratio |
|-----------|:---:|:---:|:---:|:---:|:---:|:---:|
| **BrowserUse** | 100 | 97.3 | 89.4 | 100 | 72.0 | 44.4 |
| **LangGraph** | 82.8 | 100.0 | 79.0 | 100 | 57.0 | 68.7 |
| **CrewAI** | 53.1 | 100.0 | 87.3 | 100 | 71.6 | 59.0 |
| **Claude Agent SDK** | 100 | 100.0 | 85.4 | 59.0 | 11.4 | 69.6 |
| **Mastra** | 36.9 | 99.3 | 95.1 | 100 | 93.6 | 41.8 |

## 💡 Key Insights

- **Hottest framework**: BrowserUse with a Pulse Score of 89.5
- **Fastest growing**: Claude Agent SDK gained +1907 stars this week
- **Most active development**: Mastra with 2372 commits in the last 4 weeks
- **Stale releases**: AutoGen, Swarm haven't released in a while

## 📦 Recent Releases

- **PydanticAI** [`v2.61.0`](https://github.com/pydantic/pydantic-ai/releases/tag/v2.61.0) — today
- **CrewAI** [`1.15.30`](https://github.com/crewAIInc/crewAI/releases/tag/1.15.30) — today
- **LangGraph** [`1.2.17`](https://github.com/langchain-ai/langgraph/releases/tag/1.2.17) — today
- **Claude Agent SDK** [`v2.1.310`](https://github.com/anthropics/claude-code/releases/tag/v2.1.310) — today
- **Composio** [`@composio/cli@0.5.1-beta.500`](https://github.com/ComposioHQ/composio/releases/tag/@composio/cli@0.5.1-beta.500) — today *(pre-release)*
- **Google ADK** [`v2.13.0`](https://github.com/google/adk-python/releases/tag/v2.13.0) — today
- **Agno** [`v3.1.10`](https://github.com/agno-agi/agno/releases/tag/v3.1.10) — today
- **AG2** [`v1.2.1`](https://github.com/ag2ai/ag2/releases/tag/v1.2.1) — 2 days ago
- **Haystack** [`v3.4.1`](https://github.com/deepset-ai/haystack/releases/tag/v3.4.1) — 2 days ago
- **Mastra** [`@mastra/core@1.79.0`](https://github.com/mastra-ai/mastra/releases/tag/@mastra/core@1.79.0) — 2 days ago

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

*Powered by GitHub Actions • Data refreshed daily • Last run: 2026-10-24 10:38 UTC*