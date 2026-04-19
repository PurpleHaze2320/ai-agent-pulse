# 🔬 AI Agent Framework Pulse Tracker

[![Daily Update](https://github.com/PurpleHaze2320/ai-agent-pulse/actions/workflows/track.yml/badge.svg)](https://github.com/PurpleHaze2320/ai-agent-pulse/actions/workflows/track.yml)
[![Frameworks Tracked](https://img.shields.io/badge/frameworks-19-blue)](https://github.com/PurpleHaze2320/ai-agent-pulse)
[![License: MIT](https://img.shields.io/badge/License-MIT-green.svg)](https://opensource.org/licenses/MIT)
[![GitHub stars](https://img.shields.io/github/stars/PurpleHaze2320/ai-agent-pulse?style=social)](https://github.com/PurpleHaze2320/ai-agent-pulse/stargazers)

> Automated daily tracking of the AI agent framework ecosystem's health, momentum, and trends.
> Last updated: **2026-04-19 07:28 UTC** | Tracking **19** frameworks

## How It Works

This bot runs daily via GitHub Actions and collects metrics from the GitHub API for the most important
AI agent frameworks. It computes a **Pulse Score** (0-100) based on six weighted signals: star velocity,
release freshness, issue health, commit activity, community size, and fork engagement. The result is
a living dashboard that shows which frameworks are gaining momentum and which are losing steam.

## 🏆 Pulse Leaderboard

| Rank | Framework | Pulse | Stars | ⭐ 7d | Commits (4w) | Last Release | Category |
|------|-----------|-------|-------|-------|--------------|--------------|----------|
| 1 | [Mastra](https://github.com/mastra-ai/mastra) | 🟢 **75.0** | 23.1k | 🚀 +239 | 632 | 10 days ago | `typescript` |
| 2 | [OpenAI Agents SDK](https://github.com/openai/openai-agents-python) | 🟢 **70.7** | 22.6k | 🚀 +1853 | 0 | 1 day ago | `orchestration` |
| 3 | [CrewAI](https://github.com/crewAIInc/crewAI) | 🟢 **70.1** | 49.2k | 🚀 +554 | 0 | 1 day ago | `multi-agent` |
| 4 | [BrowserUse](https://github.com/browser-use/browser-use) | 🟡 **69.4** | 88.5k | 🚀 +1186 | 0 | 16 days ago | `web-agent` |
| 5 | [LangGraph](https://github.com/langchain-ai/langgraph) | 🟡 **69.2** | 29.6k | 🚀 +623 | 0 | 1 day ago | `orchestration` |
| 6 | [Claude Agent SDK](https://github.com/anthropics/claude-code) | 🟡 **64.5** | 115.7k | 🚀 +2937 | 0 | 1 day ago | `orchestration` |
| 7 | [LlamaIndex](https://github.com/run-llama/llama_index) | 🟡 **56.7** | 48.7k | 🚀 +169 | 0 | 15 days ago | `data-agent` |
| 8 | [Google ADK](https://github.com/google/adk-python) | 🟡 **53.5** | 19.1k | 🚀 +220 | 0 | 2 days ago | `orchestration` |
| 9 | [Agno](https://github.com/agno-agi/agno) | 🟡 **53.4** | 39.5k | 🚀 +166 | 0 | 4 days ago | `multi-agent` |
| 10 | [PydanticAI](https://github.com/pydantic/pydantic-ai) | 🟡 **53.2** | 16.5k | 🚀 +172 | 0 | 1 day ago | `structured` |
| 11 | [Semantic Kernel](https://github.com/microsoft/semantic-kernel) | 🟡 **49.8** | 27.7k | 📈 +51 | 0 | 11 days ago | `enterprise` |
| 12 | [Haystack](https://github.com/deepset-ai/haystack) | 🟡 **48.4** | 24.9k | 📈 +83 | 0 | 17 days ago | `pipeline` |
| 13 | [AG2](https://github.com/ag2ai/ag2) | 🟡 **47.7** | 4.4k | 📈 +34 | 0 | 1 day ago | `multi-agent` |
| 14 | [DSPy](https://github.com/stanfordnlp/dspy) | 🟡 **46.7** | 33.8k | 🚀 +192 | 0 | 2 mo ago | `optimization` |
| 15 | [Letta](https://github.com/letta-ai/letta) | 🟡 **46.0** | 22.1k | 🚀 +134 | 0 | 18 days ago | `memory` |
| 16 | [AutoGen](https://github.com/microsoft/autogen) | 🟡 **44.1** | 57.2k | 🚀 +221 | 0 | 6 mo ago | `multi-agent` |
| 17 | [Composio](https://github.com/ComposioHQ/composio) | 🟡 **44.0** | 27.8k | 📈 +75 | 0 | 1 day ago | `tooling` |
| 18 | [Smolagents](https://github.com/huggingface/smolagents) | 🟠 **38.7** | 26.7k | 🚀 +166 | 0 | 3 mo ago | `lightweight` |
| 19 | [Swarm](https://github.com/openai/swarm) | 🔴 **10.0** | 21.3k | 📈 +45 | 0 | — | `experimental` |

## 📂 By Category

- `data-agent`: **LlamaIndex** (56.7)
- `enterprise`: **Semantic Kernel** (49.8)
- `experimental`: **Swarm** (10.0)
- `lightweight`: **Smolagents** (38.7)
- `memory`: **Letta** (46.0)
- `multi-agent`: **CrewAI** (70.1), **Agno** (53.4), **AG2** (47.7), **AutoGen** (44.1)
- `optimization`: **DSPy** (46.7)
- `orchestration`: **OpenAI Agents SDK** (70.7), **LangGraph** (69.2), **Claude Agent SDK** (64.5), **Google ADK** (53.5)
- `pipeline`: **Haystack** (48.4)
- `structured`: **PydanticAI** (53.2)
- `tooling`: **Composio** (44.0)
- `typescript`: **Mastra** (75.0)
- `web-agent`: **BrowserUse** (69.4)

## 🔍 Top 5 — Score Breakdown

| Framework | Star Velocity | Release Freshness | Issue Health | Commit Activity | Community | Fork Ratio |
|-----------|:---:|:---:|:---:|:---:|:---:|:---:|
| **Mastra** | 42.1 | 96.7 | 94.4 | 100 | 77.2 | 33.1 |
| **OpenAI Agents SDK** | 100 | 99.7 | 96.5 | 0.0 | 50.0 | 63.3 |
| **CrewAI** | 98.5 | 99.7 | 95.8 | 0.0 | 57.0 | 54.7 |
| **BrowserUse** | 100 | 94.7 | 97.8 | 0.0 | 61.6 | 45.9 |
| **LangGraph** | 100 | 99.7 | 80.0 | 0.0 | 54.6 | 68.4 |

## 💡 Key Insights

- **Hottest framework**: Mastra with a Pulse Score of 75.0
- **Fastest growing**: Claude Agent SDK gained +2937 stars this week
- **Most active development**: Mastra with 632 commits in the last 4 weeks
- **Stale releases**: Swarm haven't released in a while

## 📦 Recent Releases

- **Composio** [`@composio/cli@0.2.25-beta.215`](https://github.com/ComposioHQ/composio/releases/tag/@composio/cli@0.2.25-beta.215) — 1 day ago *(pre-release)*
- **Claude Agent SDK** [`v2.1.114`](https://github.com/anthropics/claude-code/releases/tag/v2.1.114) — 1 day ago
- **PydanticAI** [`v1.84.1`](https://github.com/pydantic/pydantic-ai/releases/tag/v1.84.1) — 1 day ago
- **OpenAI Agents SDK** [`v0.14.2`](https://github.com/openai/openai-agents-python/releases/tag/v0.14.2) — 1 day ago
- **AG2** [`v0.12.0`](https://github.com/ag2ai/ag2/releases/tag/v0.12.0) — 1 day ago
- **LangGraph** [`1.1.8`](https://github.com/langchain-ai/langgraph/releases/tag/1.1.8) — 1 day ago
- **CrewAI** [`1.14.2`](https://github.com/crewAIInc/crewAI/releases/tag/1.14.2) — 1 day ago
- **Google ADK** [`v1.31.0`](https://github.com/google/adk-python/releases/tag/v1.31.0) — 2 days ago
- **Agno** [`v2.5.17`](https://github.com/agno-agi/agno/releases/tag/v2.5.17) — 4 days ago
- **Mastra** [`@mastra/core@1.24.0`](https://github.com/mastra-ai/mastra/releases/tag/@mastra/core@1.24.0) — 10 days ago

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

*Powered by GitHub Actions • Data refreshed daily • Last run: 2026-04-19 07:28 UTC*