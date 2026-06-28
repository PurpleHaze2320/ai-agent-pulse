# 🔬 AI Agent Framework Pulse Tracker

[![Daily Update](https://github.com/PurpleHaze2320/ai-agent-pulse/actions/workflows/track.yml/badge.svg)](https://github.com/PurpleHaze2320/ai-agent-pulse/actions/workflows/track.yml)
[![Frameworks Tracked](https://img.shields.io/badge/frameworks-19-blue)](https://github.com/PurpleHaze2320/ai-agent-pulse)
[![License: MIT](https://img.shields.io/badge/License-MIT-green.svg)](https://opensource.org/licenses/MIT)
[![GitHub stars](https://img.shields.io/github/stars/PurpleHaze2320/ai-agent-pulse?style=social)](https://github.com/PurpleHaze2320/ai-agent-pulse/stargazers)

> Automated daily tracking of the AI agent framework ecosystem's health, momentum, and trends.
> Last updated: **2026-06-28 09:18 UTC** | Tracking **19** frameworks

## How It Works

This bot runs daily via GitHub Actions and collects metrics from the GitHub API for the most important
AI agent frameworks. It computes a **Pulse Score** (0-100) based on six weighted signals: star velocity,
release freshness, issue health, commit activity, community size, and fork engagement. The result is
a living dashboard that shows which frameworks are gaining momentum and which are losing steam.

## 🏆 Pulse Leaderboard

| Rank | Framework | Pulse | Stars | ⭐ 7d | Commits (4w) | Last Release | Category |
|------|-----------|-------|-------|-------|--------------|--------------|----------|
| 1 | [CrewAI](https://github.com/crewAIInc/crewAI) | 🟢 **88.5** | 54.5k | 🚀 +425 | 109 | 1 day ago | `multi-agent` |
| 2 | [Mastra](https://github.com/mastra-ai/mastra) | 🟢 **78.8** | 25.5k | 🚀 +231 | 741 | 3 days ago | `typescript` |
| 3 | [LangGraph](https://github.com/langchain-ai/langgraph) | 🟢 **75.9** | 35.9k | 🚀 +599 | 41 | 9 days ago | `orchestration` |
| 4 | [Haystack](https://github.com/deepset-ai/haystack) | 🟢 **72.5** | 25.8k | 🚀 +147 | 150 | 10 days ago | `pipeline` |
| 5 | [PydanticAI](https://github.com/pydantic/pydantic-ai) | 🟢 **72.4** | 18.0k | 🚀 +160 | 88 | 4 days ago | `structured` |
| 6 | [Google ADK](https://github.com/google/adk-python) | 🟢 **71.6** | 20.3k | 🚀 +113 | 284 | 9 days ago | `orchestration` |
| 7 | [Claude Agent SDK](https://github.com/anthropics/claude-code) | 🟢 **70.2** | 134.8k | 🚀 +1210 | 23 | 1 day ago | `orchestration` |
| 8 | [BrowserUse](https://github.com/browser-use/browser-use) | 🟡 **69.1** | 101.0k | 🚀 +1224 | 0 | 15 days ago | `web-agent` |
| 9 | [Composio](https://github.com/ComposioHQ/composio) | 🟡 **67.6** | 29.0k | 🚀 +110 | 105 | 1 day ago | `tooling` |
| 10 | [Agno](https://github.com/agno-agi/agno) | 🟡 **66.9** | 40.9k | 📈 +86 | 80 | 4 days ago | `multi-agent` |
| 11 | [OpenAI Agents SDK](https://github.com/openai/openai-agents-python) | 🟡 **64.5** | 27.5k | 🚀 +190 | 44 | 4 days ago | `orchestration` |
| 12 | [LlamaIndex](https://github.com/run-llama/llama_index) | 🟡 **62.3** | 50.5k | 🚀 +208 | 12 | 3 days ago | `data-agent` |
| 13 | [DSPy](https://github.com/stanfordnlp/dspy) | 🟡 **57.6** | 35.5k | 🚀 +299 | 12 | 1 mo ago | `optimization` |
| 14 | [Semantic Kernel](https://github.com/microsoft/semantic-kernel) | 🟡 **56.8** | 28.2k | 📈 +40 | 31 | 11 days ago | `enterprise` |
| 15 | [AG2](https://github.com/ag2ai/ag2) | 🟡 **50.2** | 4.7k | 📈 +22 | 0 | 2 days ago | `multi-agent` |
| 16 | [Letta](https://github.com/letta-ai/letta) | 🟡 **44.5** | 23.6k | 🚀 +111 | 0 | 1 mo ago | `memory` |
| 17 | [Smolagents](https://github.com/huggingface/smolagents) | 🟡 **41.9** | 28.1k | 🚀 +113 | 1 | 1 mo ago | `lightweight` |
| 18 | [AutoGen](https://github.com/microsoft/autogen) | 🟠 **39.3** | 59.3k | 🚀 +204 | 0 | 9 mo ago | `multi-agent` |
| 19 | [Swarm](https://github.com/openai/swarm) | 🔴 **11.1** | 21.7k | 📈 +88 | 0 | — | `experimental` |

## 📂 By Category

- `data-agent`: **LlamaIndex** (62.3)
- `enterprise`: **Semantic Kernel** (56.8)
- `experimental`: **Swarm** (11.1)
- `lightweight`: **Smolagents** (41.9)
- `memory`: **Letta** (44.5)
- `multi-agent`: **CrewAI** (88.5), **Agno** (66.9), **AG2** (50.2), **AutoGen** (39.3)
- `optimization`: **DSPy** (57.6)
- `orchestration`: **LangGraph** (75.9), **Google ADK** (71.6), **Claude Agent SDK** (70.2), **OpenAI Agents SDK** (64.5)
- `pipeline`: **Haystack** (72.5)
- `structured`: **PydanticAI** (72.4)
- `tooling`: **Composio** (67.6)
- `typescript`: **Mastra** (78.8)
- `web-agent`: **BrowserUse** (69.1)

## 🔍 Top 5 — Score Breakdown

| Framework | Star Velocity | Release Freshness | Issue Health | Commit Activity | Community | Fork Ratio |
|-----------|:---:|:---:|:---:|:---:|:---:|:---:|
| **CrewAI** | 90.5 | 99.7 | 96.2 | 100 | 59.6 | 56.0 |
| **Mastra** | 47.4 | 99.0 | 95.4 | 100 | 92.2 | 36.1 |
| **LangGraph** | 100 | 97.0 | 74.3 | 41.0 | 55.0 | 67.0 |
| **Haystack** | 25.9 | 96.7 | 98.1 | 100 | 75.2 | 44.8 |
| **PydanticAI** | 32.4 | 98.7 | 82.4 | 88.0 | 95.4 | 50.2 |

## 💡 Key Insights

- **Hottest framework**: CrewAI with a Pulse Score of 88.5
- **Fastest growing**: BrowserUse gained +1224 stars this week
- **Most active development**: Mastra with 741 commits in the last 4 weeks
- **Stale releases**: AutoGen, Swarm haven't released in a while

## 📦 Recent Releases

- **Composio** [`@composio/slim@0.13.1`](https://github.com/ComposioHQ/composio/releases/tag/@composio/slim@0.13.1) — 1 day ago
- **CrewAI** [`1.15.1`](https://github.com/crewAIInc/crewAI/releases/tag/1.15.1) — 1 day ago
- **Claude Agent SDK** [`v2.1.195`](https://github.com/anthropics/claude-code/releases/tag/v2.1.195) — 1 day ago
- **AG2** [`v0.14.0`](https://github.com/ag2ai/ag2/releases/tag/v0.14.0) — 2 days ago
- **LlamaIndex** [`v0.14.23`](https://github.com/run-llama/llama_index/releases/tag/v0.14.23) — 3 days ago
- **Mastra** [`@mastra/core@1.46.0`](https://github.com/mastra-ai/mastra/releases/tag/@mastra/core@1.46.0) — 3 days ago
- **OpenAI Agents SDK** [`v0.17.7`](https://github.com/openai/openai-agents-python/releases/tag/v0.17.7) — 4 days ago
- **PydanticAI** [`v2.0.0`](https://github.com/pydantic/pydantic-ai/releases/tag/v2.0.0) — 4 days ago
- **Agno** [`v2.6.19`](https://github.com/agno-agi/agno/releases/tag/v2.6.19) — 4 days ago
- **LangGraph** [`1.2.6`](https://github.com/langchain-ai/langgraph/releases/tag/1.2.6) — 9 days ago

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

*Powered by GitHub Actions • Data refreshed daily • Last run: 2026-06-28 09:18 UTC*