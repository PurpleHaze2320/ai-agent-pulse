# 🔬 AI Agent Framework Pulse Tracker

[![Daily Update](https://github.com/PurpleHaze2320/ai-agent-pulse/actions/workflows/track.yml/badge.svg)](https://github.com/PurpleHaze2320/ai-agent-pulse/actions/workflows/track.yml)
[![Frameworks Tracked](https://img.shields.io/badge/frameworks-19-blue)](https://github.com/PurpleHaze2320/ai-agent-pulse)
[![License: MIT](https://img.shields.io/badge/License-MIT-green.svg)](https://opensource.org/licenses/MIT)
[![GitHub stars](https://img.shields.io/github/stars/PurpleHaze2320/ai-agent-pulse?style=social)](https://github.com/PurpleHaze2320/ai-agent-pulse/stargazers)

> Automated daily tracking of the AI agent framework ecosystem's health, momentum, and trends.
> Last updated: **2026-04-21 08:02 UTC** | Tracking **19** frameworks

## How It Works

This bot runs daily via GitHub Actions and collects metrics from the GitHub API for the most important
AI agent frameworks. It computes a **Pulse Score** (0-100) based on six weighted signals: star velocity,
release freshness, issue health, commit activity, community size, and fork engagement. The result is
a living dashboard that shows which frameworks are gaining momentum and which are losing steam.

## 🏆 Pulse Leaderboard

| Rank | Framework | Pulse | Stars | ⭐ 7d | Commits (4w) | Last Release | Category |
|------|-----------|-------|-------|-------|--------------|--------------|----------|
| 1 | [Mastra](https://github.com/mastra-ai/mastra) | 🟢 **73.8** | 23.2k | 🚀 +200 | 683 | 12 days ago | `typescript` |
| 2 | [OpenAI Agents SDK](https://github.com/openai/openai-agents-python) | 🟢 **70.6** | 24.2k | 🚀 +3404 | 0 | today | `orchestration` |
| 3 | [CrewAI](https://github.com/crewAIInc/crewAI) | 🟢 **70.5** | 49.4k | 🚀 +547 | 0 | today | `multi-agent` |
| 4 | [BrowserUse](https://github.com/browser-use/browser-use) | 🟡 **69.2** | 89.1k | 🚀 +1364 | 0 | 19 days ago | `web-agent` |
| 5 | [LangGraph](https://github.com/langchain-ai/langgraph) | 🟡 **69.1** | 29.8k | 🚀 +618 | 0 | 3 days ago | `orchestration` |
| 6 | [Claude Agent SDK](https://github.com/anthropics/claude-code) | 🟡 **64.6** | 116.4k | 🚀 +2710 | 0 | today | `orchestration` |
| 7 | [LlamaIndex](https://github.com/run-llama/llama_index) | 🟡 **58.1** | 48.7k | 🚀 +173 | 0 | today | `data-agent` |
| 8 | [PydanticAI](https://github.com/pydantic/pydantic-ai) | 🟡 **53.3** | 16.5k | 🚀 +173 | 0 | 3 days ago | `structured` |
| 9 | [Agno](https://github.com/agno-agi/agno) | 🟡 **52.8** | 39.6k | 🚀 +150 | 0 | 6 days ago | `multi-agent` |
| 10 | [Google ADK](https://github.com/google/adk-python) | 🟡 **52.6** | 19.1k | 🚀 +188 | 0 | today | `orchestration` |
| 11 | [Haystack](https://github.com/deepset-ai/haystack) | 🟡 **50.1** | 24.9k | 📈 +95 | 0 | today | `pipeline` |
| 12 | [Semantic Kernel](https://github.com/microsoft/semantic-kernel) | 🟡 **49.7** | 27.7k | 📈 +49 | 0 | 13 days ago | `enterprise` |
| 13 | [AG2](https://github.com/ag2ai/ag2) | 🟡 **47.6** | 4.4k | 📈 +32 | 0 | 3 days ago | `multi-agent` |
| 14 | [DSPy](https://github.com/stanfordnlp/dspy) | 🟡 **47.4** | 33.9k | 🚀 +205 | 0 | 2 mo ago | `optimization` |
| 15 | [Letta](https://github.com/letta-ai/letta) | 🟡 **46.7** | 22.2k | 🚀 +152 | 0 | 20 days ago | `memory` |
| 16 | [Composio](https://github.com/ComposioHQ/composio) | 🟡 **43.8** | 27.8k | 📈 +68 | 0 | 3 days ago | `tooling` |
| 17 | [AutoGen](https://github.com/microsoft/autogen) | 🟡 **43.5** | 57.3k | 🚀 +202 | 0 | 6 mo ago | `multi-agent` |
| 18 | [Smolagents](https://github.com/huggingface/smolagents) | 🟠 **39.0** | 26.8k | 🚀 +174 | 0 | 3 mo ago | `lightweight` |
| 19 | [Swarm](https://github.com/openai/swarm) | 🔴 **10.6** | 21.4k | 📈 +61 | 0 | — | `experimental` |

## 📂 By Category

- `data-agent`: **LlamaIndex** (58.1)
- `enterprise`: **Semantic Kernel** (49.7)
- `experimental`: **Swarm** (10.6)
- `lightweight`: **Smolagents** (39.0)
- `memory`: **Letta** (46.7)
- `multi-agent`: **CrewAI** (70.5), **Agno** (52.8), **AG2** (47.6), **AutoGen** (43.5)
- `optimization`: **DSPy** (47.4)
- `orchestration`: **OpenAI Agents SDK** (70.6), **LangGraph** (69.1), **Claude Agent SDK** (64.6), **Google ADK** (52.6)
- `pipeline`: **Haystack** (50.1)
- `structured`: **PydanticAI** (53.3)
- `tooling`: **Composio** (43.8)
- `typescript`: **Mastra** (73.8)
- `web-agent`: **BrowserUse** (69.2)

## 🔍 Top 5 — Score Breakdown

| Framework | Star Velocity | Release Freshness | Issue Health | Commit Activity | Community | Fork Ratio |
|-----------|:---:|:---:|:---:|:---:|:---:|:---:|
| **Mastra** | 37.1 | 96.0 | 94.4 | 100 | 77.8 | 33.3 |
| **OpenAI Agents SDK** | 100 | 100.0 | 96.3 | 0.0 | 50.6 | 61.4 |
| **CrewAI** | 100 | 100.0 | 95.5 | 0.0 | 57.0 | 54.8 |
| **BrowserUse** | 100 | 93.7 | 97.8 | 0.0 | 61.8 | 45.7 |
| **LangGraph** | 100 | 99.0 | 79.8 | 0.0 | 54.8 | 68.4 |

## 💡 Key Insights

- **Hottest framework**: Mastra with a Pulse Score of 73.8
- **Fastest growing**: OpenAI Agents SDK gained +3404 stars this week
- **Most active development**: Mastra with 683 commits in the last 4 weeks
- **Stale releases**: Swarm haven't released in a while

## 📦 Recent Releases

- **Google ADK** [`v1.31.1`](https://github.com/google/adk-python/releases/tag/v1.31.1) — today
- **LlamaIndex** [`v0.14.21`](https://github.com/run-llama/llama_index/releases/tag/v0.14.21) — today
- **OpenAI Agents SDK** [`v0.14.3`](https://github.com/openai/openai-agents-python/releases/tag/v0.14.3) — today
- **Claude Agent SDK** [`v2.1.116`](https://github.com/anthropics/claude-code/releases/tag/v2.1.116) — today
- **CrewAI** [`1.14.3a1`](https://github.com/crewAIInc/crewAI/releases/tag/1.14.3a1) — today *(pre-release)*
- **Haystack** [`v2.28.0`](https://github.com/deepset-ai/haystack/releases/tag/v2.28.0) — today
- **Composio** [`@composio/cli@0.2.25-beta.215`](https://github.com/ComposioHQ/composio/releases/tag/@composio/cli@0.2.25-beta.215) — 3 days ago *(pre-release)*
- **PydanticAI** [`v1.84.1`](https://github.com/pydantic/pydantic-ai/releases/tag/v1.84.1) — 3 days ago
- **AG2** [`v0.12.0`](https://github.com/ag2ai/ag2/releases/tag/v0.12.0) — 3 days ago
- **LangGraph** [`1.1.8`](https://github.com/langchain-ai/langgraph/releases/tag/1.1.8) — 3 days ago

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

*Powered by GitHub Actions • Data refreshed daily • Last run: 2026-04-21 08:02 UTC*