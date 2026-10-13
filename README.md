# 🔬 AI Agent Framework Pulse Tracker

[![Daily Update](https://github.com/PurpleHaze2320/ai-agent-pulse/actions/workflows/track.yml/badge.svg)](https://github.com/PurpleHaze2320/ai-agent-pulse/actions/workflows/track.yml)
[![Frameworks Tracked](https://img.shields.io/badge/frameworks-19-blue)](https://github.com/PurpleHaze2320/ai-agent-pulse)
[![License: MIT](https://img.shields.io/badge/License-MIT-green.svg)](https://opensource.org/licenses/MIT)
[![GitHub stars](https://img.shields.io/github/stars/PurpleHaze2320/ai-agent-pulse?style=social)](https://github.com/PurpleHaze2320/ai-agent-pulse/stargazers)

> Automated daily tracking of the AI agent framework ecosystem's health, momentum, and trends.
> Last updated: **2026-10-13 13:54 UTC** | Tracking **19** frameworks

## How It Works

This bot runs daily via GitHub Actions and collects metrics from the GitHub API for the most important
AI agent frameworks. It computes a **Pulse Score** (0-100) based on six weighted signals: star velocity,
release freshness, issue health, commit activity, community size, and fork engagement. The result is
a living dashboard that shows which frameworks are gaining momentum and which are losing steam.

## 🏆 Pulse Leaderboard

| Rank | Framework | Pulse | Stars | ⭐ 7d | Commits (4w) | Last Release | Category |
|------|-----------|-------|-------|-------|--------------|--------------|----------|
| 1 | [BrowserUse](https://github.com/browser-use/browser-use) | 🟢 **79.9** | 117.8k | 🚀 +595 | 51 | 6 days ago | `web-agent` |
| 2 | [LangGraph](https://github.com/langchain-ai/langgraph) | 🟢 **79.1** | 43.2k | 🚀 +422 | 80 | today | `orchestration` |
| 3 | [Claude Agent SDK](https://github.com/anthropics/claude-code) | 🟢 **77.4** | 150.6k | 🚀 +1002 | 58 | 3 days ago | `orchestration` |
| 4 | [Mastra](https://github.com/mastra-ai/mastra) | 🟢 **77.2** | 28.8k | 🚀 +184 | 1854 | today | `typescript` |
| 5 | [OpenAI Agents SDK](https://github.com/openai/openai-agents-python) | 🟢 **76.4** | 30.0k | 🚀 +154 | 205 | 10 days ago | `orchestration` |
| 6 | [CrewAI](https://github.com/crewAIInc/crewAI) | 🟢 **73.1** | 59.6k | 🚀 +251 | 69 | 3 days ago | `multi-agent` |
| 7 | [Agno](https://github.com/agno-agi/agno) | 🟢 **72.0** | 42.7k | 🚀 +133 | 106 | 1 day ago | `multi-agent` |
| 8 | [Haystack](https://github.com/deepset-ai/haystack) | 🟢 **70.4** | 26.7k | 📈 +51 | 246 | 12 days ago | `pipeline` |
| 9 | [AG2](https://github.com/ag2ai/ag2) | 🟡 **69.8** | 5.0k | ↗️ +16 | 110 | 2 days ago | `multi-agent` |
| 10 | [Composio](https://github.com/ComposioHQ/composio) | 🟡 **66.5** | 30.5k | 📈 +71 | 213 | today | `tooling` |
| 11 | [DSPy](https://github.com/stanfordnlp/dspy) | 🟡 **58.2** | 38.6k | 📈 +96 | 45 | today | `optimization` |
| 12 | [LlamaIndex](https://github.com/run-llama/llama_index) | 🟡 **55.9** | 52.5k | 📈 +55 | 19 | 21 days ago | `data-agent` |
| 13 | [Semantic Kernel](https://github.com/microsoft/semantic-kernel) | 🟡 **54.4** | 28.7k | 📈 +31 | 20 | 7 days ago | `enterprise` |
| 14 | [PydanticAI](https://github.com/pydantic/pydantic-ai) | 🟡 **54.1** | 20.6k | 🚀 +159 | 0 | 7 days ago | `structured` |
| 15 | [Google ADK](https://github.com/google/adk-python) | 🟡 **52.9** | 21.8k | 📈 +71 | 0 | 11 days ago | `orchestration` |
| 16 | [Letta](https://github.com/letta-ai/letta) | 🟠 **36.1** | 25.1k | 📈 +77 | 0 | 5 mo ago | `memory` |
| 17 | [Smolagents](https://github.com/huggingface/smolagents) | 🟠 **34.9** | 29.8k | 🚀 +115 | 5 | 4 mo ago | `lightweight` |
| 18 | [AutoGen](https://github.com/microsoft/autogen) | 🟠 **32.9** | 61.4k | 🚀 +118 | 0 | 1y ago | `multi-agent` |
| 19 | [Swarm](https://github.com/openai/swarm) | 🔴 **9.4** | 22.1k | ↗️ +19 | 0 | — | `experimental` |

## 📂 By Category

- `data-agent`: **LlamaIndex** (55.9)
- `enterprise`: **Semantic Kernel** (54.4)
- `experimental`: **Swarm** (9.4)
- `lightweight`: **Smolagents** (34.9)
- `memory`: **Letta** (36.1)
- `multi-agent`: **CrewAI** (73.1), **Agno** (72.0), **AG2** (69.8), **AutoGen** (32.9)
- `optimization`: **DSPy** (58.2)
- `orchestration`: **LangGraph** (79.1), **Claude Agent SDK** (77.4), **OpenAI Agents SDK** (76.4), **Google ADK** (52.9)
- `pipeline`: **Haystack** (70.4)
- `structured`: **PydanticAI** (54.1)
- `tooling`: **Composio** (66.5)
- `typescript`: **Mastra** (77.2)
- `web-agent`: **BrowserUse** (79.9)

## 🔍 Top 5 — Score Breakdown

| Framework | Star Velocity | Release Freshness | Issue Health | Commit Activity | Community | Fork Ratio |
|-----------|:---:|:---:|:---:|:---:|:---:|:---:|
| **BrowserUse** | 100 | 98.0 | 89.8 | 51.0 | 72.0 | 44.3 |
| **LangGraph** | 83.8 | 100.0 | 65.1 | 80.0 | 56.4 | 68.0 |
| **Claude Agent SDK** | 100 | 99.0 | 85.8 | 58.0 | 11.4 | 70.1 |
| **Mastra** | 37.5 | 100.0 | 95.6 | 100 | 93.4 | 41.2 |
| **OpenAI Agents SDK** | 30.7 | 96.7 | 99.1 | 100 | 80.2 | 65.0 |

## 💡 Key Insights

- **Hottest framework**: BrowserUse with a Pulse Score of 79.9
- **Fastest growing**: Claude Agent SDK gained +1002 stars this week
- **Most active development**: Mastra with 1854 commits in the last 4 weeks
- **Stale releases**: AutoGen, Swarm haven't released in a while

## 📦 Recent Releases

- **Composio** [`@composio/cli@0.4.4-beta.424`](https://github.com/ComposioHQ/composio/releases/tag/@composio/cli@0.4.4-beta.424) — today *(pre-release)*
- **Mastra** [`@mastra/core@1.76.0`](https://github.com/mastra-ai/mastra/releases/tag/@mastra/core@1.76.0) — today
- **DSPy** [`3.4.1`](https://github.com/stanfordnlp/dspy/releases/tag/3.4.1) — today
- **LangGraph** [`1.2.15`](https://github.com/langchain-ai/langgraph/releases/tag/1.2.15) — today
- **Agno** [`v3.1.3`](https://github.com/agno-agi/agno/releases/tag/v3.1.3) — 1 day ago
- **AG2** [`v1.2.0`](https://github.com/ag2ai/ag2/releases/tag/v1.2.0) — 2 days ago
- **CrewAI** [`1.15.27`](https://github.com/crewAIInc/crewAI/releases/tag/1.15.27) — 3 days ago
- **Claude Agent SDK** [`v2.1.296`](https://github.com/anthropics/claude-code/releases/tag/v2.1.296) — 3 days ago
- **BrowserUse** [`0.13.11`](https://github.com/browser-use/browser-use/releases/tag/0.13.11) — 6 days ago
- **Semantic Kernel** [`python-1.45.0`](https://github.com/microsoft/semantic-kernel/releases/tag/python-1.45.0) — 7 days ago

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

*Powered by GitHub Actions • Data refreshed daily • Last run: 2026-10-13 13:54 UTC*