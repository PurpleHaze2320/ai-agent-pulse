# 🔬 AI Agent Framework Pulse Tracker

[![Daily Update](https://github.com/PurpleHaze2320/ai-agent-pulse/actions/workflows/track.yml/badge.svg)](https://github.com/PurpleHaze2320/ai-agent-pulse/actions/workflows/track.yml)
[![Frameworks Tracked](https://img.shields.io/badge/frameworks-19-blue)](https://github.com/PurpleHaze2320/ai-agent-pulse)
[![License: MIT](https://img.shields.io/badge/License-MIT-green.svg)](https://opensource.org/licenses/MIT)
[![GitHub stars](https://img.shields.io/github/stars/PurpleHaze2320/ai-agent-pulse?style=social)](https://github.com/PurpleHaze2320/ai-agent-pulse/stargazers)

> Automated daily tracking of the AI agent framework ecosystem's health, momentum, and trends.
> Last updated: **2026-10-06 13:05 UTC** | Tracking **19** frameworks

## How It Works

This bot runs daily via GitHub Actions and collects metrics from the GitHub API for the most important
AI agent frameworks. It computes a **Pulse Score** (0-100) based on six weighted signals: star velocity,
release freshness, issue health, commit activity, community size, and fork engagement. The result is
a living dashboard that shows which frameworks are gaining momentum and which are losing steam.

## 🏆 Pulse Leaderboard

| Rank | Framework | Pulse | Stars | ⭐ 7d | Commits (4w) | Last Release | Category |
|------|-----------|-------|-------|-------|--------------|--------------|----------|
| 1 | [Claude Agent SDK](https://github.com/anthropics/claude-code) | 🟢 **81.1** | 149.6k | 🚀 +1021 | 76 | today | `orchestration` |
| 2 | [BrowserUse](https://github.com/browser-use/browser-use) | 🟢 **77.2** | 117.3k | 🚀 +557 | 46 | 1 mo ago | `web-agent` |
| 3 | [Mastra](https://github.com/mastra-ai/mastra) | 🟢 **77.0** | 28.6k | 🚀 +175 | 1863 | 1 day ago | `typescript` |
| 4 | [OpenAI Agents SDK](https://github.com/openai/openai-agents-python) | 🟢 **75.0** | 29.9k | 📈 +97 | 214 | 3 days ago | `orchestration` |
| 5 | [Google ADK](https://github.com/google/adk-python) | 🟢 **72.4** | 21.7k | 📈 +49 | 397 | 4 days ago | `orchestration` |
| 6 | [Agno](https://github.com/agno-agi/agno) | 🟢 **72.3** | 42.6k | 🚀 +190 | 93 | 4 days ago | `multi-agent` |
| 7 | [CrewAI](https://github.com/crewAIInc/crewAI) | 🟢 **71.3** | 59.4k | 🚀 +222 | 66 | 7 days ago | `multi-agent` |
| 8 | [Haystack](https://github.com/deepset-ai/haystack) | 🟢 **70.9** | 26.7k | 📈 +52 | 210 | 5 days ago | `pipeline` |
| 9 | [LangGraph](https://github.com/langchain-ai/langgraph) | 🟢 **70.5** | 42.8k | 🚀 +315 | 56 | today | `orchestration` |
| 10 | [AG2](https://github.com/ag2ai/ag2) | 🟡 **67.7** | 5.0k | ↗️ +9 | 91 | 3 days ago | `multi-agent` |
| 11 | [Composio](https://github.com/ComposioHQ/composio) | 🟡 **67.2** | 30.5k | 📈 +91 | 268 | today | `tooling` |
| 12 | [DSPy](https://github.com/stanfordnlp/dspy) | 🟡 **60.2** | 38.5k | 📈 +98 | 56 | 11 days ago | `optimization` |
| 13 | [LlamaIndex](https://github.com/run-llama/llama_index) | 🟡 **57.9** | 52.4k | 📈 +72 | 23 | 14 days ago | `data-agent` |
| 14 | [PydanticAI](https://github.com/pydantic/pydantic-ai) | 🟡 **54.8** | 20.4k | 🚀 +171 | 0 | today | `structured` |
| 15 | [Semantic Kernel](https://github.com/microsoft/semantic-kernel) | 🟡 **50.4** | 28.6k | ↗️ +18 | 0 | today | `enterprise` |
| 16 | [Letta](https://github.com/letta-ai/letta) | 🟠 **36.5** | 25.0k | 📈 +73 | 0 | 4 mo ago | `memory` |
| 17 | [Smolagents](https://github.com/huggingface/smolagents) | 🟠 **35.6** | 29.7k | 🚀 +115 | 5 | 4 mo ago | `lightweight` |
| 18 | [AutoGen](https://github.com/microsoft/autogen) | 🟠 **30.9** | 61.3k | 📈 +60 | 0 | 1y ago | `multi-agent` |
| 19 | [Swarm](https://github.com/openai/swarm) | 🔴 **9.4** | 22.0k | ↗️ +16 | 0 | — | `experimental` |

## 📂 By Category

- `data-agent`: **LlamaIndex** (57.9)
- `enterprise`: **Semantic Kernel** (50.4)
- `experimental`: **Swarm** (9.4)
- `lightweight`: **Smolagents** (35.6)
- `memory`: **Letta** (36.5)
- `multi-agent`: **Agno** (72.3), **CrewAI** (71.3), **AG2** (67.7), **AutoGen** (30.9)
- `optimization`: **DSPy** (60.2)
- `orchestration`: **Claude Agent SDK** (81.1), **OpenAI Agents SDK** (75.0), **Google ADK** (72.4), **LangGraph** (70.5)
- `pipeline`: **Haystack** (70.9)
- `structured`: **PydanticAI** (54.8)
- `tooling`: **Composio** (67.2)
- `typescript`: **Mastra** (77.0)
- `web-agent`: **BrowserUse** (77.2)

## 🔍 Top 5 — Score Breakdown

| Framework | Star Velocity | Release Freshness | Issue Health | Commit Activity | Community | Fork Ratio |
|-----------|:---:|:---:|:---:|:---:|:---:|:---:|
| **Claude Agent SDK** | 100 | 100.0 | 86.0 | 76.0 | 11.4 | 68.6 |
| **BrowserUse** | 100 | 89.3 | 90.2 | 46.0 | 72.0 | 44.1 |
| **Mastra** | 37.4 | 99.7 | 95.1 | 100 | 93.6 | 40.9 |
| **OpenAI Agents SDK** | 23.2 | 99.0 | 99.7 | 100 | 79.4 | 64.9 |
| **Google ADK** | 11.4 | 98.7 | 92.7 | 100 | 84.0 | 75.6 |

## 💡 Key Insights

- **Hottest framework**: Claude Agent SDK with a Pulse Score of 81.1
- **Fastest growing**: Claude Agent SDK gained +1021 stars this week
- **Most active development**: Mastra with 1863 commits in the last 4 weeks
- **Stale releases**: AutoGen, Swarm haven't released in a while

## 📦 Recent Releases

- **Semantic Kernel** [`python-1.45.0`](https://github.com/microsoft/semantic-kernel/releases/tag/python-1.45.0) — today
- **Claude Agent SDK** [`v2.1.291`](https://github.com/anthropics/claude-code/releases/tag/v2.1.291) — today
- **PydanticAI** [`clai2-bleeding`](https://github.com/pydantic/pydantic-ai/releases/tag/clai2-bleeding) — today *(pre-release)*
- **Composio** [`@composio/cli@0.4.3-beta.412`](https://github.com/ComposioHQ/composio/releases/tag/@composio/cli@0.4.3-beta.412) — today *(pre-release)*
- **LangGraph** [`1.2.13`](https://github.com/langchain-ai/langgraph/releases/tag/1.2.13) — today
- **Mastra** [`@mastra/core@1.74.0`](https://github.com/mastra-ai/mastra/releases/tag/@mastra/core@1.74.0) — 1 day ago
- **AG2** [`v1.1.2`](https://github.com/ag2ai/ag2/releases/tag/v1.1.2) — 3 days ago
- **OpenAI Agents SDK** [`v0.23.1`](https://github.com/openai/openai-agents-python/releases/tag/v0.23.1) — 3 days ago
- **Agno** [`v3.1.1`](https://github.com/agno-agi/agno/releases/tag/v3.1.1) — 4 days ago
- **Google ADK** [`v2.11.0`](https://github.com/google/adk-python/releases/tag/v2.11.0) — 4 days ago

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

*Powered by GitHub Actions • Data refreshed daily • Last run: 2026-10-06 13:05 UTC*