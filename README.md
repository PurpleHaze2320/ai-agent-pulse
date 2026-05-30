# 🔬 AI Agent Framework Pulse Tracker

[![Daily Update](https://github.com/PurpleHaze2320/ai-agent-pulse/actions/workflows/track.yml/badge.svg)](https://github.com/PurpleHaze2320/ai-agent-pulse/actions/workflows/track.yml)
[![Frameworks Tracked](https://img.shields.io/badge/frameworks-19-blue)](https://github.com/PurpleHaze2320/ai-agent-pulse)
[![License: MIT](https://img.shields.io/badge/License-MIT-green.svg)](https://opensource.org/licenses/MIT)
[![GitHub stars](https://img.shields.io/github/stars/PurpleHaze2320/ai-agent-pulse?style=social)](https://github.com/PurpleHaze2320/ai-agent-pulse/stargazers)

> Automated daily tracking of the AI agent framework ecosystem's health, momentum, and trends.
> Last updated: **2026-05-30 08:34 UTC** | Tracking **19** frameworks

## How It Works

This bot runs daily via GitHub Actions and collects metrics from the GitHub API for the most important
AI agent frameworks. It computes a **Pulse Score** (0-100) based on six weighted signals: star velocity,
release freshness, issue health, commit activity, community size, and fork engagement. The result is
a living dashboard that shows which frameworks are gaining momentum and which are losing steam.

## 🏆 Pulse Leaderboard

| Rank | Framework | Pulse | Stars | ⭐ 7d | Commits (4w) | Last Release | Category |
|------|-----------|-------|-------|-------|--------------|--------------|----------|
| 1 | [Mastra](https://github.com/mastra-ai/mastra) | 🟢 **82.0** | 24.5k | 🚀 +324 | 925 | 2 days ago | `typescript` |
| 2 | [CrewAI](https://github.com/crewAIInc/crewAI) | 🟢 **70.2** | 52.5k | 🚀 +460 | 0 | 1 day ago | `multi-agent` |
| 3 | [BrowserUse](https://github.com/browser-use/browser-use) | 🟡 **69.9** | 96.2k | 🚀 +1071 | 0 | 4 days ago | `web-agent` |
| 4 | [LangGraph](https://github.com/langchain-ai/langgraph) | 🟡 **68.6** | 33.4k | 🚀 +627 | 0 | 1 day ago | `orchestration` |
| 5 | [Claude Agent SDK](https://github.com/anthropics/claude-code) | 🟡 **65.5** | 128.1k | 🚀 +2188 | 0 | today | `orchestration` |
| 6 | [LlamaIndex](https://github.com/run-llama/llama_index) | 🟡 **58.4** | 49.8k | 🚀 +188 | 0 | 15 days ago | `data-agent` |
| 7 | [OpenAI Agents SDK](https://github.com/openai/openai-agents-python) | 🟡 **57.0** | 26.8k | 🚀 +191 | 0 | 3 days ago | `orchestration` |
| 8 | [PydanticAI](https://github.com/pydantic/pydantic-ai) | 🟡 **54.8** | 17.4k | 🚀 +167 | 0 | 1 day ago | `structured` |
| 9 | [Agno](https://github.com/agno-agi/agno) | 🟡 **52.2** | 40.4k | 🚀 +112 | 0 | 8 days ago | `multi-agent` |
| 10 | [Semantic Kernel](https://github.com/microsoft/semantic-kernel) | 🟡 **51.4** | 28.0k | 📈 +49 | 0 | 1 day ago | `enterprise` |
| 11 | [Google ADK](https://github.com/google/adk-python) | 🟡 **50.9** | 19.9k | 🚀 +125 | 0 | 7 days ago | `orchestration` |
| 12 | [DSPy](https://github.com/stanfordnlp/dspy) | 🟡 **50.6** | 34.7k | 🚀 +135 | 0 | 2 days ago | `optimization` |
| 13 | [AG2](https://github.com/ag2ai/ag2) | 🟡 **48.9** | 4.6k | 📈 +25 | 0 | 1 day ago | `multi-agent` |
| 14 | [Letta](https://github.com/letta-ai/letta) | 🟡 **48.8** | 23.0k | 🚀 +160 | 0 | 15 days ago | `memory` |
| 15 | [Haystack](https://github.com/deepset-ai/haystack) | 🟡 **48.6** | 25.4k | 📈 +63 | 0 | 17 days ago | `pipeline` |
| 16 | [Composio](https://github.com/ComposioHQ/composio) | 🟡 **47.7** | 28.5k | 🚀 +127 | 0 | 9 days ago | `tooling` |
| 17 | [Smolagents](https://github.com/huggingface/smolagents) | 🟡 **44.8** | 27.6k | 🚀 +132 | 0 | 1 day ago | `lightweight` |
| 18 | [AutoGen](https://github.com/microsoft/autogen) | 🟡 **42.7** | 58.5k | 🚀 +229 | 0 | 8 mo ago | `multi-agent` |
| 19 | [Swarm](https://github.com/openai/swarm) | 🔴 **9.1** | 21.5k | 📈 +28 | 0 | — | `experimental` |

## 📂 By Category

- `data-agent`: **LlamaIndex** (58.4)
- `enterprise`: **Semantic Kernel** (51.4)
- `experimental`: **Swarm** (9.1)
- `lightweight`: **Smolagents** (44.8)
- `memory`: **Letta** (48.8)
- `multi-agent`: **CrewAI** (70.2), **Agno** (52.2), **AG2** (48.9), **AutoGen** (42.7)
- `optimization`: **DSPy** (50.6)
- `orchestration`: **LangGraph** (68.6), **Claude Agent SDK** (65.5), **OpenAI Agents SDK** (57.0), **Google ADK** (50.9)
- `pipeline`: **Haystack** (48.6)
- `structured`: **PydanticAI** (54.8)
- `tooling`: **Composio** (47.7)
- `typescript`: **Mastra** (82.0)
- `web-agent`: **BrowserUse** (69.9)

## 🔍 Top 5 — Score Breakdown

| Framework | Star Velocity | Release Freshness | Issue Health | Commit Activity | Community | Fork Ratio |
|-----------|:---:|:---:|:---:|:---:|:---:|:---:|
| **Mastra** | 62.0 | 99.3 | 95.0 | 100 | 88.4 | 35.2 |
| **CrewAI** | 96.4 | 99.7 | 97.9 | 0.0 | 59.4 | 55.6 |
| **BrowserUse** | 100 | 98.7 | 95.8 | 0.0 | 63.0 | 44.9 |
| **LangGraph** | 100 | 99.7 | 76.4 | 0.0 | 55.0 | 67.5 |
| **Claude Agent SDK** | 100 | 100.0 | 86.2 | 0.0 | 10.2 | 65.4 |

## 💡 Key Insights

- **Hottest framework**: Mastra with a Pulse Score of 82.0
- **Fastest growing**: Claude Agent SDK gained +2188 stars this week
- **Most active development**: Mastra with 925 commits in the last 4 weeks
- **Stale releases**: Swarm haven't released in a while

## 📦 Recent Releases

- **Claude Agent SDK** [`v2.1.158`](https://github.com/anthropics/claude-code/releases/tag/v2.1.158) — today
- **Smolagents** [`v1.26.0`](https://github.com/huggingface/smolagents/releases/tag/v1.26.0) — 1 day ago
- **PydanticAI** [`v2.0.0b4`](https://github.com/pydantic/pydantic-ai/releases/tag/v2.0.0b4) — 1 day ago *(pre-release)*
- **AG2** [`v0.13.2`](https://github.com/ag2ai/ag2/releases/tag/v0.13.2) — 1 day ago
- **CrewAI** [`1.14.6`](https://github.com/crewAIInc/crewAI/releases/tag/1.14.6) — 1 day ago
- **LangGraph** [`sdk==0.4.0`](https://github.com/langchain-ai/langgraph/releases/tag/sdk==0.4.0) — 1 day ago
- **Semantic Kernel** [`dotnet-1.77.0`](https://github.com/microsoft/semantic-kernel/releases/tag/dotnet-1.77.0) — 1 day ago
- **DSPy** [`3.3.0b1`](https://github.com/stanfordnlp/dspy/releases/tag/3.3.0b1) — 2 days ago *(pre-release)*
- **Mastra** [`@mastra/core@1.37.0`](https://github.com/mastra-ai/mastra/releases/tag/@mastra/core@1.37.0) — 2 days ago
- **OpenAI Agents SDK** [`v0.17.4`](https://github.com/openai/openai-agents-python/releases/tag/v0.17.4) — 3 days ago

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

*Powered by GitHub Actions • Data refreshed daily • Last run: 2026-05-30 08:34 UTC*