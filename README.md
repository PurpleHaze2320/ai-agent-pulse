# 🔬 AI Agent Framework Pulse Tracker

[![Daily Update](https://github.com/PurpleHaze2320/ai-agent-pulse/actions/workflows/track.yml/badge.svg)](https://github.com/PurpleHaze2320/ai-agent-pulse/actions/workflows/track.yml)
[![Frameworks Tracked](https://img.shields.io/badge/frameworks-19-blue)](https://github.com/PurpleHaze2320/ai-agent-pulse)
[![License: MIT](https://img.shields.io/badge/License-MIT-green.svg)](https://opensource.org/licenses/MIT)
[![GitHub stars](https://img.shields.io/github/stars/PurpleHaze2320/ai-agent-pulse?style=social)](https://github.com/PurpleHaze2320/ai-agent-pulse/stargazers)

> Automated daily tracking of the AI agent framework ecosystem's health, momentum, and trends.
> Last updated: **2026-04-22 07:58 UTC** | Tracking **19** frameworks

## How It Works

This bot runs daily via GitHub Actions and collects metrics from the GitHub API for the most important
AI agent frameworks. It computes a **Pulse Score** (0-100) based on six weighted signals: star velocity,
release freshness, issue health, commit activity, community size, and fork engagement. The result is
a living dashboard that shows which frameworks are gaining momentum and which are losing steam.

## 🏆 Pulse Leaderboard

| Rank | Framework | Pulse | Stars | ⭐ 7d | Commits (4w) | Last Release | Category |
|------|-----------|-------|-------|-------|--------------|--------------|----------|
| 1 | [Mastra](https://github.com/mastra-ai/mastra) | 🟢 **73.8** | 23.2k | 🚀 +198 | 737 | 13 days ago | `typescript` |
| 2 | [CrewAI](https://github.com/crewAIInc/crewAI) | 🟢 **70.6** | 49.5k | 🚀 +568 | 0 | today | `multi-agent` |
| 3 | [OpenAI Agents SDK](https://github.com/openai/openai-agents-python) | 🟢 **70.6** | 24.5k | 🚀 +3689 | 0 | today | `orchestration` |
| 4 | [LangGraph](https://github.com/langchain-ai/langgraph) | 🟡 **69.3** | 30.0k | 🚀 +651 | 0 | today | `orchestration` |
| 5 | [BrowserUse](https://github.com/browser-use/browser-use) | 🟡 **69.1** | 89.4k | 🚀 +1479 | 0 | 20 days ago | `web-agent` |
| 6 | [Claude Agent SDK](https://github.com/anthropics/claude-code) | 🟡 **64.6** | 116.7k | 🚀 +2590 | 0 | today | `orchestration` |
| 7 | [LlamaIndex](https://github.com/run-llama/llama_index) | 🟡 **58.8** | 48.8k | 🚀 +191 | 0 | 1 day ago | `data-agent` |
| 8 | [PydanticAI](https://github.com/pydantic/pydantic-ai) | 🟡 **53.9** | 16.5k | 🚀 +179 | 0 | today | `structured` |
| 9 | [Agno](https://github.com/agno-agi/agno) | 🟡 **52.8** | 39.6k | 🚀 +149 | 0 | 7 days ago | `multi-agent` |
| 10 | [Google ADK](https://github.com/google/adk-python) | 🟡 **52.6** | 19.2k | 🚀 +186 | 0 | 1 day ago | `orchestration` |
| 11 | [DSPy](https://github.com/stanfordnlp/dspy) | 🟡 **52.5** | 33.9k | 🚀 +207 | 0 | today | `optimization` |
| 12 | [Haystack](https://github.com/deepset-ai/haystack) | 🟡 **50.7** | 24.9k | 🚀 +112 | 0 | 1 day ago | `pipeline` |
| 13 | [Semantic Kernel](https://github.com/microsoft/semantic-kernel) | 🟡 **49.6** | 27.8k | 📈 +48 | 0 | 14 days ago | `enterprise` |
| 14 | [AG2](https://github.com/ag2ai/ag2) | 🟡 **47.4** | 4.4k | 📈 +29 | 0 | 4 days ago | `multi-agent` |
| 15 | [Letta](https://github.com/letta-ai/letta) | 🟡 **46.7** | 22.2k | 🚀 +153 | 0 | 21 days ago | `memory` |
| 16 | [AutoGen](https://github.com/microsoft/autogen) | 🟡 **44.1** | 57.3k | 🚀 +216 | 0 | 6 mo ago | `multi-agent` |
| 17 | [Composio](https://github.com/ComposioHQ/composio) | 🟡 **43.9** | 27.9k | 📈 +72 | 0 | 4 days ago | `tooling` |
| 18 | [Smolagents](https://github.com/huggingface/smolagents) | 🟠 **39.3** | 26.8k | 🚀 +183 | 0 | 3 mo ago | `lightweight` |
| 19 | [Swarm](https://github.com/openai/swarm) | 🔴 **10.3** | 21.4k | 📈 +52 | 0 | — | `experimental` |

## 📂 By Category

- `data-agent`: **LlamaIndex** (58.8)
- `enterprise`: **Semantic Kernel** (49.6)
- `experimental`: **Swarm** (10.3)
- `lightweight`: **Smolagents** (39.3)
- `memory`: **Letta** (46.7)
- `multi-agent`: **CrewAI** (70.6), **Agno** (52.8), **AG2** (47.4), **AutoGen** (44.1)
- `optimization`: **DSPy** (52.5)
- `orchestration`: **OpenAI Agents SDK** (70.6), **LangGraph** (69.3), **Claude Agent SDK** (64.6), **Google ADK** (52.6)
- `pipeline`: **Haystack** (50.7)
- `structured`: **PydanticAI** (53.9)
- `tooling`: **Composio** (43.9)
- `typescript`: **Mastra** (73.8)
- `web-agent`: **BrowserUse** (69.1)

## 🔍 Top 5 — Score Breakdown

| Framework | Star Velocity | Release Freshness | Issue Health | Commit Activity | Community | Fork Ratio |
|-----------|:---:|:---:|:---:|:---:|:---:|:---:|
| **Mastra** | 37.3 | 95.7 | 94.5 | 100 | 78.6 | 33.3 |
| **CrewAI** | 100 | 100.0 | 95.6 | 0.0 | 57.4 | 54.8 |
| **OpenAI Agents SDK** | 100 | 100.0 | 96.3 | 0.0 | 50.6 | 61.3 |
| **LangGraph** | 100 | 100.0 | 79.7 | 0.0 | 54.8 | 68.3 |
| **BrowserUse** | 100 | 93.3 | 97.7 | 0.0 | 61.8 | 45.7 |

## 💡 Key Insights

- **Hottest framework**: Mastra with a Pulse Score of 73.8
- **Fastest growing**: OpenAI Agents SDK gained +3689 stars this week
- **Most active development**: Mastra with 737 commits in the last 4 weeks
- **Stale releases**: Swarm haven't released in a while

## 📦 Recent Releases

- **Claude Agent SDK** [`v2.1.117`](https://github.com/anthropics/claude-code/releases/tag/v2.1.117) — today
- **PydanticAI** [`v1.85.1`](https://github.com/pydantic/pydantic-ai/releases/tag/v1.85.1) — today
- **OpenAI Agents SDK** [`v0.14.4`](https://github.com/openai/openai-agents-python/releases/tag/v0.14.4) — today
- **CrewAI** [`1.14.3a2`](https://github.com/crewAIInc/crewAI/releases/tag/1.14.3a2) — today *(pre-release)*
- **DSPy** [`3.2.0`](https://github.com/stanfordnlp/dspy/releases/tag/3.2.0) — today
- **LangGraph** [`1.1.9`](https://github.com/langchain-ai/langgraph/releases/tag/1.1.9) — today
- **Google ADK** [`v1.31.1`](https://github.com/google/adk-python/releases/tag/v1.31.1) — 1 day ago
- **LlamaIndex** [`v0.14.21`](https://github.com/run-llama/llama_index/releases/tag/v0.14.21) — 1 day ago
- **Haystack** [`v2.28.0`](https://github.com/deepset-ai/haystack/releases/tag/v2.28.0) — 1 day ago
- **Composio** [`@composio/cli@0.2.25-beta.215`](https://github.com/ComposioHQ/composio/releases/tag/@composio/cli@0.2.25-beta.215) — 4 days ago *(pre-release)*

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

*Powered by GitHub Actions • Data refreshed daily • Last run: 2026-04-22 07:58 UTC*