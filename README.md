# 🔬 AI Agent Framework Pulse Tracker

[![Daily Update](https://github.com/PurpleHaze2320/ai-agent-pulse/actions/workflows/track.yml/badge.svg)](https://github.com/PurpleHaze2320/ai-agent-pulse/actions/workflows/track.yml)
[![Frameworks Tracked](https://img.shields.io/badge/frameworks-19-blue)](https://github.com/PurpleHaze2320/ai-agent-pulse)
[![License: MIT](https://img.shields.io/badge/License-MIT-green.svg)](https://opensource.org/licenses/MIT)
[![GitHub stars](https://img.shields.io/github/stars/PurpleHaze2320/ai-agent-pulse?style=social)](https://github.com/PurpleHaze2320/ai-agent-pulse/stargazers)

> Automated daily tracking of the AI agent framework ecosystem's health, momentum, and trends.
> Last updated: **2026-11-03 13:54 UTC** | Tracking **19** frameworks

## How It Works

This bot runs daily via GitHub Actions and collects metrics from the GitHub API for the most important
AI agent frameworks. It computes a **Pulse Score** (0-100) based on six weighted signals: star velocity,
release freshness, issue health, commit activity, community size, and fork engagement. The result is
a living dashboard that shows which frameworks are gaining momentum and which are losing steam.

## 🏆 Pulse Leaderboard

| Rank | Framework | Pulse | Stars | ⭐ 7d | Commits (4w) | Last Release | Category |
|------|-----------|-------|-------|-------|--------------|--------------|----------|
| 1 | [BrowserUse](https://github.com/browser-use/browser-use) | 🟢 **89.7** | 119.9k | 🚀 +663 | 107 | 7 days ago | `web-agent` |
| 2 | [LangGraph](https://github.com/langchain-ai/langgraph) | 🟢 **85.3** | 44.4k | 🚀 +409 | 111 | 3 days ago | `orchestration` |
| 3 | [CrewAI](https://github.com/crewAIInc/crewAI) | 🟢 **80.0** | 60.5k | 🚀 +285 | 172 | 1 day ago | `multi-agent` |
| 4 | [Mastra](https://github.com/mastra-ai/mastra) | 🟢 **77.2** | 29.3k | 🚀 +192 | 2074 | 1 day ago | `typescript` |
| 5 | [Claude Agent SDK](https://github.com/anthropics/claude-code) | 🟢 **74.1** | 154.4k | 🚀 +856 | 43 | today | `orchestration` |
| 6 | [Google ADK](https://github.com/google/adk-python) | 🟢 **73.6** | 22.1k | 📈 +68 | 427 | 10 days ago | `orchestration` |
| 7 | [Haystack](https://github.com/deepset-ai/haystack) | 🟢 **72.0** | 26.9k | 📈 +65 | 180 | today | `pipeline` |
| 8 | [Agno](https://github.com/agno-agi/agno) | 🟢 **70.8** | 43.0k | 🚀 +116 | 144 | 4 days ago | `multi-agent` |
| 9 | [AG2](https://github.com/ag2ai/ag2) | 🟡 **69.9** | 5.0k | ↗️ +20 | 115 | 6 days ago | `multi-agent` |
| 10 | [Composio](https://github.com/ComposioHQ/composio) | 🟡 **68.6** | 30.9k | 🚀 +122 | 353 | today | `tooling` |
| 11 | [OpenAI Agents SDK](https://github.com/openai/openai-agents-python) | 🟡 **68.0** | 30.5k | 🚀 +147 | 62 | 19 days ago | `orchestration` |
| 12 | [Semantic Kernel](https://github.com/microsoft/semantic-kernel) | 🟡 **67.0** | 28.7k | 📈 +23 | 79 | 5 days ago | `enterprise` |
| 13 | [DSPy](https://github.com/stanfordnlp/dspy) | 🟡 **60.6** | 38.9k | 📈 +86 | 68 | 21 days ago | `optimization` |
| 14 | [LlamaIndex](https://github.com/run-llama/llama_index) | 🟡 **54.0** | 52.8k | 🚀 +110 | 6 | 1 mo ago | `data-agent` |
| 15 | [PydanticAI](https://github.com/pydantic/pydantic-ai) | 🟡 **52.2** | 21.0k | 🚀 +104 | 0 | today | `structured` |
| 16 | [Letta](https://github.com/letta-ai/letta) | 🟠 **34.2** | 25.3k | 📈 +66 | 1 | 5 mo ago | `memory` |
| 17 | [AutoGen](https://github.com/microsoft/autogen) | 🟠 **32.9** | 61.7k | 🚀 +104 | 2 | 1y ago | `multi-agent` |
| 18 | [Smolagents](https://github.com/huggingface/smolagents) | 🟠 **32.0** | 30.2k | 🚀 +107 | 0 | 5 mo ago | `lightweight` |
| 19 | [Swarm](https://github.com/openai/swarm) | 🔴 **9.4** | 22.1k | 📈 +21 | 0 | — | `experimental` |

## 📂 By Category

- `data-agent`: **LlamaIndex** (54.0)
- `enterprise`: **Semantic Kernel** (67.0)
- `experimental`: **Swarm** (9.4)
- `lightweight`: **Smolagents** (32.0)
- `memory`: **Letta** (34.2)
- `multi-agent`: **CrewAI** (80.0), **Agno** (70.8), **AG2** (69.9), **AutoGen** (32.9)
- `optimization`: **DSPy** (60.6)
- `orchestration`: **LangGraph** (85.3), **Claude Agent SDK** (74.1), **Google ADK** (73.6), **OpenAI Agents SDK** (68.0)
- `pipeline`: **Haystack** (72.0)
- `structured`: **PydanticAI** (52.2)
- `tooling`: **Composio** (68.6)
- `typescript`: **Mastra** (77.2)
- `web-agent`: **BrowserUse** (89.7)

## 🔍 Top 5 — Score Breakdown

| Framework | Star Velocity | Release Freshness | Issue Health | Commit Activity | Community | Fork Ratio |
|-----------|:---:|:---:|:---:|:---:|:---:|:---:|
| **BrowserUse** | 100 | 97.7 | 89.7 | 100 | 72.2 | 44.6 |
| **LangGraph** | 82.7 | 99.0 | 81.4 | 100 | 57.4 | 68.7 |
| **CrewAI** | 56.7 | 99.7 | 84.4 | 100 | 72.6 | 59.7 |
| **Mastra** | 38.3 | 99.7 | 94.3 | 100 | 93.4 | 41.9 |
| **Claude Agent SDK** | 100 | 100.0 | 84.9 | 43.0 | 11.2 | 66.2 |

## 💡 Key Insights

- **Hottest framework**: BrowserUse with a Pulse Score of 89.7
- **Fastest growing**: Claude Agent SDK gained +856 stars this week
- **Most active development**: Mastra with 2074 commits in the last 4 weeks
- **Stale releases**: AutoGen, Swarm haven't released in a while

## 📦 Recent Releases

- **Composio** [`@composio/cli@0.6.1-beta.533`](https://github.com/ComposioHQ/composio/releases/tag/@composio/cli@0.6.1-beta.533) — today *(pre-release)*
- **Haystack** [`v2.31.1`](https://github.com/deepset-ai/haystack/releases/tag/v2.31.1) — today
- **Claude Agent SDK** [`v2.1.317`](https://github.com/anthropics/claude-code/releases/tag/v2.1.317) — today
- **PydanticAI** [`v2.65.0`](https://github.com/pydantic/pydantic-ai/releases/tag/v2.65.0) — today
- **Mastra** [`@mastra/core@1.81.0`](https://github.com/mastra-ai/mastra/releases/tag/@mastra/core@1.81.0) — 1 day ago
- **CrewAI** [`1.15.34`](https://github.com/crewAIInc/crewAI/releases/tag/1.15.34) — 1 day ago
- **LangGraph** [`1.2.19`](https://github.com/langchain-ai/langgraph/releases/tag/1.2.19) — 3 days ago
- **Agno** [`v3.1.12`](https://github.com/agno-agi/agno/releases/tag/v3.1.12) — 4 days ago
- **Semantic Kernel** [`python-1.46.0`](https://github.com/microsoft/semantic-kernel/releases/tag/python-1.46.0) — 5 days ago
- **AG2** [`v1.2.2`](https://github.com/ag2ai/ag2/releases/tag/v1.2.2) — 6 days ago

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

*Powered by GitHub Actions • Data refreshed daily • Last run: 2026-11-03 13:54 UTC*