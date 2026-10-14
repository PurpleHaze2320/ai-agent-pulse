# 🔬 AI Agent Framework Pulse Tracker

[![Daily Update](https://github.com/PurpleHaze2320/ai-agent-pulse/actions/workflows/track.yml/badge.svg)](https://github.com/PurpleHaze2320/ai-agent-pulse/actions/workflows/track.yml)
[![Frameworks Tracked](https://img.shields.io/badge/frameworks-19-blue)](https://github.com/PurpleHaze2320/ai-agent-pulse)
[![License: MIT](https://img.shields.io/badge/License-MIT-green.svg)](https://opensource.org/licenses/MIT)
[![GitHub stars](https://img.shields.io/github/stars/PurpleHaze2320/ai-agent-pulse?style=social)](https://github.com/PurpleHaze2320/ai-agent-pulse/stargazers)

> Automated daily tracking of the AI agent framework ecosystem's health, momentum, and trends.
> Last updated: **2026-10-14 11:31 UTC** | Tracking **19** frameworks

## How It Works

This bot runs daily via GitHub Actions and collects metrics from the GitHub API for the most important
AI agent frameworks. It computes a **Pulse Score** (0-100) based on six weighted signals: star velocity,
release freshness, issue health, commit activity, community size, and fork engagement. The result is
a living dashboard that shows which frameworks are gaining momentum and which are losing steam.

## 🏆 Pulse Leaderboard

| Rank | Framework | Pulse | Stars | ⭐ 7d | Commits (4w) | Last Release | Category |
|------|-----------|-------|-------|-------|--------------|--------------|----------|
| 1 | [LangGraph](https://github.com/langchain-ai/langgraph) | 🟢 **80.2** | 43.2k | 🚀 +432 | 84 | today | `orchestration` |
| 2 | [BrowserUse](https://github.com/browser-use/browser-use) | 🟢 **79.8** | 117.9k | 🚀 +586 | 51 | 7 days ago | `web-agent` |
| 3 | [Claude Agent SDK](https://github.com/anthropics/claude-code) | 🟢 **78.2** | 150.7k | 🚀 +1040 | 61 | today | `orchestration` |
| 4 | [Mastra](https://github.com/mastra-ai/mastra) | 🟢 **77.7** | 28.8k | 🚀 +198 | 1950 | today | `typescript` |
| 5 | [OpenAI Agents SDK](https://github.com/openai/openai-agents-python) | 🟢 **76.2** | 30.0k | 🚀 +147 | 213 | 11 days ago | `orchestration` |
| 6 | [Google ADK](https://github.com/google/adk-python) | 🟢 **75.0** | 21.8k | 🚀 +104 | 469 | today | `orchestration` |
| 7 | [CrewAI](https://github.com/crewAIInc/crewAI) | 🟢 **74.6** | 59.7k | 🚀 +263 | 75 | today | `multi-agent` |
| 8 | [PydanticAI](https://github.com/pydantic/pydantic-ai) | 🟢 **73.4** | 20.6k | 🚀 +141 | 754 | 8 days ago | `structured` |
| 9 | [Agno](https://github.com/agno-agi/agno) | 🟢 **71.8** | 42.7k | 🚀 +129 | 107 | 2 days ago | `multi-agent` |
| 10 | [Haystack](https://github.com/deepset-ai/haystack) | 🟢 **71.2** | 26.7k | 📈 +50 | 253 | today | `pipeline` |
| 11 | [AG2](https://github.com/ag2ai/ag2) | 🟡 **69.6** | 5.0k | ↗️ +12 | 112 | 3 days ago | `multi-agent` |
| 12 | [Composio](https://github.com/ComposioHQ/composio) | 🟡 **67.0** | 30.5k | 📈 +86 | 220 | today | `tooling` |
| 13 | [DSPy](https://github.com/stanfordnlp/dspy) | 🟡 **58.5** | 38.6k | 📈 +92 | 47 | 1 day ago | `optimization` |
| 14 | [LlamaIndex](https://github.com/run-llama/llama_index) | 🟡 **56.0** | 52.5k | 📈 +59 | 19 | 22 days ago | `data-agent` |
| 15 | [Semantic Kernel](https://github.com/microsoft/semantic-kernel) | 🟡 **54.5** | 28.7k | 📈 +30 | 21 | 7 days ago | `enterprise` |
| 16 | [Letta](https://github.com/letta-ai/letta) | 🟠 **35.6** | 25.1k | 📈 +64 | 0 | 5 mo ago | `memory` |
| 17 | [Smolagents](https://github.com/huggingface/smolagents) | 🟠 **34.9** | 29.8k | 🚀 +117 | 5 | 4 mo ago | `lightweight` |
| 18 | [AutoGen](https://github.com/microsoft/autogen) | 🟠 **32.7** | 61.4k | 🚀 +114 | 0 | 1y ago | `multi-agent` |
| 19 | [Swarm](https://github.com/openai/swarm) | 🔴 **9.4** | 22.1k | ↗️ +18 | 0 | — | `experimental` |

## 📂 By Category

- `data-agent`: **LlamaIndex** (56.0)
- `enterprise`: **Semantic Kernel** (54.5)
- `experimental`: **Swarm** (9.4)
- `lightweight`: **Smolagents** (34.9)
- `memory`: **Letta** (35.6)
- `multi-agent`: **CrewAI** (74.6), **Agno** (71.8), **AG2** (69.6), **AutoGen** (32.7)
- `optimization`: **DSPy** (58.5)
- `orchestration`: **LangGraph** (80.2), **Claude Agent SDK** (78.2), **OpenAI Agents SDK** (76.2), **Google ADK** (75.0)
- `pipeline`: **Haystack** (71.2)
- `structured`: **PydanticAI** (73.4)
- `tooling`: **Composio** (67.0)
- `typescript`: **Mastra** (77.7)
- `web-agent`: **BrowserUse** (79.8)

## 🔍 Top 5 — Score Breakdown

| Framework | Star Velocity | Release Freshness | Issue Health | Commit Activity | Community | Fork Ratio |
|-----------|:---:|:---:|:---:|:---:|:---:|:---:|
| **LangGraph** | 85.0 | 100.0 | 65.0 | 84.0 | 56.4 | 68.0 |
| **BrowserUse** | 100 | 97.7 | 89.8 | 51.0 | 72.0 | 44.3 |
| **Claude Agent SDK** | 100 | 100.0 | 85.8 | 61.0 | 11.4 | 70.4 |
| **Mastra** | 39.5 | 100.0 | 95.7 | 100 | 93.4 | 41.3 |
| **OpenAI Agents SDK** | 29.7 | 96.3 | 99.7 | 100 | 80.2 | 65.1 |

## 💡 Key Insights

- **Hottest framework**: LangGraph with a Pulse Score of 80.2
- **Fastest growing**: Claude Agent SDK gained +1040 stars this week
- **Most active development**: Mastra with 1950 commits in the last 4 weeks
- **Stale releases**: AutoGen, Swarm haven't released in a while

## 📦 Recent Releases

- **Haystack** [`v3.4.0-rc1`](https://github.com/deepset-ai/haystack/releases/tag/v3.4.0-rc1) — today *(pre-release)*
- **Mastra** [`@mastra/core@1.77.0`](https://github.com/mastra-ai/mastra/releases/tag/@mastra/core@1.77.0) — today
- **CrewAI** [`1.15.28`](https://github.com/crewAIInc/crewAI/releases/tag/1.15.28) — today
- **Claude Agent SDK** [`v2.1.299`](https://github.com/anthropics/claude-code/releases/tag/v2.1.299) — today
- **Composio** [`@composio/cli@0.4.4-beta.426`](https://github.com/ComposioHQ/composio/releases/tag/@composio/cli@0.4.4-beta.426) — today *(pre-release)*
- **LangGraph** [`cli==0.4.34`](https://github.com/langchain-ai/langgraph/releases/tag/cli==0.4.34) — today
- **Google ADK** [`v2.12.0`](https://github.com/google/adk-python/releases/tag/v2.12.0) — today
- **DSPy** [`3.4.1`](https://github.com/stanfordnlp/dspy/releases/tag/3.4.1) — 1 day ago
- **Agno** [`v3.1.3`](https://github.com/agno-agi/agno/releases/tag/v3.1.3) — 2 days ago
- **AG2** [`v1.2.0`](https://github.com/ag2ai/ag2/releases/tag/v1.2.0) — 3 days ago

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

*Powered by GitHub Actions • Data refreshed daily • Last run: 2026-10-14 11:31 UTC*