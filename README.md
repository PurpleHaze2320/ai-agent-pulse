# 🔬 AI Agent Framework Pulse Tracker

[![Daily Update](https://github.com/PurpleHaze2320/ai-agent-pulse/actions/workflows/track.yml/badge.svg)](https://github.com/PurpleHaze2320/ai-agent-pulse/actions/workflows/track.yml)
[![Frameworks Tracked](https://img.shields.io/badge/frameworks-19-blue)](https://github.com/PurpleHaze2320/ai-agent-pulse)
[![License: MIT](https://img.shields.io/badge/License-MIT-green.svg)](https://opensource.org/licenses/MIT)
[![GitHub stars](https://img.shields.io/github/stars/PurpleHaze2320/ai-agent-pulse?style=social)](https://github.com/PurpleHaze2320/ai-agent-pulse/stargazers)

> Automated daily tracking of the AI agent framework ecosystem's health, momentum, and trends.
> Last updated: **2026-08-09 07:03 UTC** | Tracking **19** frameworks

## How It Works

This bot runs daily via GitHub Actions and collects metrics from the GitHub API for the most important
AI agent frameworks. It computes a **Pulse Score** (0-100) based on six weighted signals: star velocity,
release freshness, issue health, commit activity, community size, and fork engagement. The result is
a living dashboard that shows which frameworks are gaining momentum and which are losing steam.

## 🏆 Pulse Leaderboard

| Rank | Framework | Pulse | Stars | ⭐ 7d | Commits (4w) | Last Release | Category |
|------|-----------|-------|-------|-------|--------------|--------------|----------|
| 1 | [BrowserUse](https://github.com/browser-use/browser-use) | 🟢 **89.4** | 108.4k | 🚀 +859 | 147 | 12 days ago | `web-agent` |
| 2 | [Mastra](https://github.com/mastra-ai/mastra) | 🟢 **79.2** | 27.1k | 🚀 +227 | 1191 | 2 days ago | `typescript` |
| 3 | [LangGraph](https://github.com/langchain-ai/langgraph) | 🟡 **67.8** | 39.3k | 🚀 +609 | 0 | 1 day ago | `orchestration` |
| 4 | [Composio](https://github.com/ComposioHQ/composio) | 🟡 **67.1** | 29.6k | 📈 +93 | 246 | 1 day ago | `tooling` |
| 5 | [Claude Agent SDK](https://github.com/anthropics/claude-code) | 🟡 **64.7** | 140.8k | 🚀 +797 | 0 | 1 day ago | `orchestration` |
| 6 | [CrewAI](https://github.com/crewAIInc/crewAI) | 🟡 **63.3** | 56.8k | 🚀 +332 | 0 | today | `multi-agent` |
| 7 | [PydanticAI](https://github.com/pydantic/pydantic-ai) | 🟡 **56.6** | 19.2k | 🚀 +181 | 0 | 1 day ago | `structured` |
| 8 | [LlamaIndex](https://github.com/run-llama/llama_index) | 🟡 **56.3** | 51.5k | 🚀 +183 | 0 | 1 mo ago | `data-agent` |
| 9 | [OpenAI Agents SDK](https://github.com/openai/openai-agents-python) | 🟡 **55.9** | 28.5k | 🚀 +162 | 0 | 4 days ago | `orchestration` |
| 10 | [DSPy](https://github.com/stanfordnlp/dspy) | 🟡 **55.7** | 36.8k | 🚀 +268 | 0 | 5 days ago | `optimization` |
| 11 | [Semantic Kernel](https://github.com/microsoft/semantic-kernel) | 🟡 **54.2** | 28.4k | 📈 +31 | 17 | 2 days ago | `enterprise` |
| 12 | [Google ADK](https://github.com/google/adk-python) | 🟡 **53.2** | 21.0k | 📈 +73 | 0 | 1 day ago | `orchestration` |
| 13 | [Agno](https://github.com/agno-agi/agno) | 🟡 **51.4** | 41.6k | 📈 +98 | 0 | 2 days ago | `multi-agent` |
| 14 | [Haystack](https://github.com/deepset-ai/haystack) | 🟡 **49.7** | 26.2k | 📈 +69 | 0 | 19 days ago | `pipeline` |
| 15 | [AG2](https://github.com/ag2ai/ag2) | 🟡 **49.5** | 4.8k | 📈 +21 | 0 | 11 days ago | `multi-agent` |
| 16 | [Letta](https://github.com/letta-ai/letta) | 🟡 **41.3** | 24.2k | 🚀 +103 | 0 | 2 mo ago | `memory` |
| 17 | [Smolagents](https://github.com/huggingface/smolagents) | 🟠 **38.0** | 28.7k | 📈 +93 | 0 | 2 mo ago | `lightweight` |
| 18 | [AutoGen](https://github.com/microsoft/autogen) | 🟠 **35.4** | 60.3k | 🚀 +159 | 0 | 10 mo ago | `multi-agent` |
| 19 | [Swarm](https://github.com/openai/swarm) | 🔴 **9.7** | 21.9k | ↗️ +20 | 0 | — | `experimental` |

## 📂 By Category

- `data-agent`: **LlamaIndex** (56.3)
- `enterprise`: **Semantic Kernel** (54.2)
- `experimental`: **Swarm** (9.7)
- `lightweight`: **Smolagents** (38.0)
- `memory`: **Letta** (41.3)
- `multi-agent`: **CrewAI** (63.3), **Agno** (51.4), **AG2** (49.5), **AutoGen** (35.4)
- `optimization`: **DSPy** (55.7)
- `orchestration`: **LangGraph** (67.8), **Claude Agent SDK** (64.7), **OpenAI Agents SDK** (55.9), **Google ADK** (53.2)
- `pipeline`: **Haystack** (49.7)
- `structured`: **PydanticAI** (56.6)
- `tooling`: **Composio** (67.1)
- `typescript`: **Mastra** (79.2)
- `web-agent`: **BrowserUse** (89.4)

## 🔍 Top 5 — Score Breakdown

| Framework | Star Velocity | Release Freshness | Issue Health | Commit Activity | Community | Fork Ratio |
|-----------|:---:|:---:|:---:|:---:|:---:|:---:|
| **BrowserUse** | 100 | 96.0 | 94.1 | 100 | 66.6 | 44.0 |
| **Mastra** | 47.3 | 99.3 | 95.7 | 100 | 92.6 | 38.4 |
| **LangGraph** | 100 | 99.7 | 70.9 | 0.0 | 55.4 | 67.2 |
| **Composio** | 19.5 | 99.7 | 95.1 | 100 | 16.8 | 63.5 |
| **Claude Agent SDK** | 100 | 99.7 | 82.2 | 0.0 | 10.4 | 64.3 |

## 💡 Key Insights

- **Hottest framework**: BrowserUse with a Pulse Score of 89.4
- **Fastest growing**: BrowserUse gained +859 stars this week
- **Most active development**: Mastra with 1191 commits in the last 4 weeks
- **Stale releases**: AutoGen, Swarm haven't released in a while

## 📦 Recent Releases

- **CrewAI** [`1.15.14`](https://github.com/crewAIInc/crewAI/releases/tag/1.15.14) — today
- **PydanticAI** [`v2.27.0`](https://github.com/pydantic/pydantic-ai/releases/tag/v2.27.0) — 1 day ago
- **Claude Agent SDK** [`v2.1.226`](https://github.com/anthropics/claude-code/releases/tag/v2.1.226) — 1 day ago
- **Google ADK** [`v2.6.3`](https://github.com/google/adk-python/releases/tag/v2.6.3) — 1 day ago
- **LangGraph** [`checkpointpostgres==3.1.2`](https://github.com/langchain-ai/langgraph/releases/tag/checkpointpostgres==3.1.2) — 1 day ago
- **Composio** [`@composio/slim@0.15.0`](https://github.com/ComposioHQ/composio/releases/tag/@composio/slim@0.15.0) — 1 day ago
- **Agno** [`v3.0.0a1`](https://github.com/agno-agi/agno/releases/tag/v3.0.0a1) — 2 days ago *(pre-release)*
- **Semantic Kernel** [`python-1.44.1`](https://github.com/microsoft/semantic-kernel/releases/tag/python-1.44.1) — 2 days ago
- **Mastra** [`@mastra/core@1.56.0`](https://github.com/mastra-ai/mastra/releases/tag/@mastra/core@1.56.0) — 2 days ago
- **OpenAI Agents SDK** [`v0.19.4`](https://github.com/openai/openai-agents-python/releases/tag/v0.19.4) — 4 days ago

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

*Powered by GitHub Actions • Data refreshed daily • Last run: 2026-08-09 07:03 UTC*