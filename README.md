# 🔬 AI Agent Framework Pulse Tracker

[![Daily Update](https://github.com/PurpleHaze2320/ai-agent-pulse/actions/workflows/track.yml/badge.svg)](https://github.com/PurpleHaze2320/ai-agent-pulse/actions/workflows/track.yml)
[![Frameworks Tracked](https://img.shields.io/badge/frameworks-19-blue)](https://github.com/PurpleHaze2320/ai-agent-pulse)
[![License: MIT](https://img.shields.io/badge/License-MIT-green.svg)](https://opensource.org/licenses/MIT)
[![GitHub stars](https://img.shields.io/github/stars/PurpleHaze2320/ai-agent-pulse?style=social)](https://github.com/PurpleHaze2320/ai-agent-pulse/stargazers)

> Automated daily tracking of the AI agent framework ecosystem's health, momentum, and trends.
> Last updated: **2026-06-02 10:46 UTC** | Tracking **19** frameworks

## How It Works

This bot runs daily via GitHub Actions and collects metrics from the GitHub API for the most important
AI agent frameworks. It computes a **Pulse Score** (0-100) based on six weighted signals: star velocity,
release freshness, issue health, commit activity, community size, and fork engagement. The result is
a living dashboard that shows which frameworks are gaining momentum and which are losing steam.

## 🏆 Pulse Leaderboard

| Rank | Framework | Pulse | Stars | ⭐ 7d | Commits (4w) | Last Release | Category |
|------|-----------|-------|-------|-------|--------------|--------------|----------|
| 1 | [Mastra](https://github.com/mastra-ai/mastra) | 🟢 **83.0** | 24.7k | 🚀 +340 | 818 | 5 days ago | `typescript` |
| 2 | [CrewAI](https://github.com/crewAIInc/crewAI) | 🟡 **69.9** | 52.7k | 🚀 +453 | 0 | 4 days ago | `multi-agent` |
| 3 | [BrowserUse](https://github.com/browser-use/browser-use) | 🟡 **69.7** | 96.7k | 🚀 +1069 | 0 | 7 days ago | `web-agent` |
| 4 | [LangGraph](https://github.com/langchain-ai/langgraph) | 🟡 **68.7** | 33.6k | 🚀 +627 | 0 | today | `orchestration` |
| 5 | [Claude Agent SDK](https://github.com/anthropics/claude-code) | 🟡 **65.6** | 129.5k | 🚀 +2856 | 0 | today | `orchestration` |
| 6 | [LlamaIndex](https://github.com/run-llama/llama_index) | 🟡 **57.9** | 49.8k | 🚀 +176 | 0 | 18 days ago | `data-agent` |
| 7 | [OpenAI Agents SDK](https://github.com/openai/openai-agents-python) | 🟡 **56.2** | 26.9k | 🚀 +188 | 0 | 7 days ago | `orchestration` |
| 8 | [PydanticAI](https://github.com/pydantic/pydantic-ai) | 🟡 **54.4** | 17.5k | 🚀 +153 | 0 | today | `structured` |
| 9 | [Agno](https://github.com/agno-agi/agno) | 🟡 **52.3** | 40.5k | 🚀 +102 | 0 | today | `multi-agent` |
| 10 | [Semantic Kernel](https://github.com/microsoft/semantic-kernel) | 🟡 **51.2** | 28.0k | 📈 +48 | 0 | 5 days ago | `enterprise` |
| 11 | [Google ADK](https://github.com/google/adk-python) | 🟡 **50.5** | 20.0k | 🚀 +101 | 0 | today | `orchestration` |
| 12 | [DSPy](https://github.com/stanfordnlp/dspy) | 🟡 **50.0** | 34.8k | 🚀 +125 | 0 | 5 days ago | `optimization` |
| 13 | [AG2](https://github.com/ag2ai/ag2) | 🟡 **48.6** | 4.6k | 📈 +22 | 0 | 4 days ago | `multi-agent` |
| 14 | [Haystack](https://github.com/deepset-ai/haystack) | 🟡 **48.4** | 25.4k | 📈 +64 | 0 | 20 days ago | `pipeline` |
| 15 | [Letta](https://github.com/letta-ai/letta) | 🟡 **47.6** | 23.1k | 🚀 +129 | 0 | 18 days ago | `memory` |
| 16 | [Composio](https://github.com/ComposioHQ/composio) | 🟡 **47.3** | 28.6k | 🚀 +125 | 0 | 13 days ago | `tooling` |
| 17 | [Smolagents](https://github.com/huggingface/smolagents) | 🟡 **44.9** | 27.7k | 🚀 +141 | 0 | 4 days ago | `lightweight` |
| 18 | [AutoGen](https://github.com/microsoft/autogen) | 🟡 **42.5** | 58.6k | 🚀 +224 | 0 | 8 mo ago | `multi-agent` |
| 19 | [Swarm](https://github.com/openai/swarm) | 🔴 **9.4** | 21.6k | 📈 +36 | 0 | — | `experimental` |

## 📂 By Category

- `data-agent`: **LlamaIndex** (57.9)
- `enterprise`: **Semantic Kernel** (51.2)
- `experimental`: **Swarm** (9.4)
- `lightweight`: **Smolagents** (44.9)
- `memory`: **Letta** (47.6)
- `multi-agent`: **CrewAI** (69.9), **Agno** (52.3), **AG2** (48.6), **AutoGen** (42.5)
- `optimization`: **DSPy** (50.0)
- `orchestration`: **LangGraph** (68.7), **Claude Agent SDK** (65.6), **OpenAI Agents SDK** (56.2), **Google ADK** (50.5)
- `pipeline`: **Haystack** (48.4)
- `structured`: **PydanticAI** (54.4)
- `tooling`: **Composio** (47.3)
- `typescript`: **Mastra** (83.0)
- `web-agent`: **BrowserUse** (69.7)

## 🔍 Top 5 — Score Breakdown

| Framework | Star Velocity | Release Freshness | Issue Health | Commit Activity | Community | Fork Ratio |
|-----------|:---:|:---:|:---:|:---:|:---:|:---:|
| **Mastra** | 65.1 | 98.3 | 95.8 | 100 | 91.2 | 35.4 |
| **CrewAI** | 95.7 | 98.7 | 98.1 | 0.0 | 59.4 | 55.8 |
| **BrowserUse** | 100 | 97.7 | 95.9 | 0.0 | 63.0 | 44.8 |
| **LangGraph** | 100 | 100.0 | 76.2 | 0.0 | 55.0 | 67.4 |
| **Claude Agent SDK** | 100 | 100.0 | 87.3 | 0.0 | 10.2 | 65.1 |

## 💡 Key Insights

- **Hottest framework**: Mastra with a Pulse Score of 83.0
- **Fastest growing**: Claude Agent SDK gained +2856 stars this week
- **Most active development**: Mastra with 818 commits in the last 4 weeks
- **Stale releases**: Swarm haven't released in a while

## 📦 Recent Releases

- **PydanticAI** [`v2.0.0b5`](https://github.com/pydantic/pydantic-ai/releases/tag/v2.0.0b5) — today *(pre-release)*
- **Agno** [`v2.6.10`](https://github.com/agno-agi/agno/releases/tag/v2.6.10) — today
- **Claude Agent SDK** [`v2.1.160`](https://github.com/anthropics/claude-code/releases/tag/v2.1.160) — today
- **Google ADK** [`v1.34.2`](https://github.com/google/adk-python/releases/tag/v1.34.2) — today
- **LangGraph** [`1.2.3`](https://github.com/langchain-ai/langgraph/releases/tag/1.2.3) — today
- **Smolagents** [`v1.26.0`](https://github.com/huggingface/smolagents/releases/tag/v1.26.0) — 4 days ago
- **AG2** [`v0.13.2`](https://github.com/ag2ai/ag2/releases/tag/v0.13.2) — 4 days ago
- **CrewAI** [`1.14.6`](https://github.com/crewAIInc/crewAI/releases/tag/1.14.6) — 4 days ago
- **Semantic Kernel** [`dotnet-1.77.0`](https://github.com/microsoft/semantic-kernel/releases/tag/dotnet-1.77.0) — 5 days ago
- **DSPy** [`3.3.0b1`](https://github.com/stanfordnlp/dspy/releases/tag/3.3.0b1) — 5 days ago *(pre-release)*

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

*Powered by GitHub Actions • Data refreshed daily • Last run: 2026-06-02 10:46 UTC*