# 🔬 AI Agent Framework Pulse Tracker

[![Daily Update](https://github.com/PurpleHaze2320/ai-agent-pulse/actions/workflows/track.yml/badge.svg)](https://github.com/PurpleHaze2320/ai-agent-pulse/actions/workflows/track.yml)
[![Frameworks Tracked](https://img.shields.io/badge/frameworks-19-blue)](https://github.com/PurpleHaze2320/ai-agent-pulse)
[![License: MIT](https://img.shields.io/badge/License-MIT-green.svg)](https://opensource.org/licenses/MIT)
[![GitHub stars](https://img.shields.io/github/stars/PurpleHaze2320/ai-agent-pulse?style=social)](https://github.com/PurpleHaze2320/ai-agent-pulse/stargazers)

> Automated daily tracking of the AI agent framework ecosystem's health, momentum, and trends.
> Last updated: **2026-04-08 07:44 UTC** | Tracking **19** frameworks

## How It Works

This bot runs daily via GitHub Actions and collects metrics from the GitHub API for the most important
AI agent frameworks. It computes a **Pulse Score** (0-100) based on six weighted signals: star velocity,
release freshness, issue health, commit activity, community size, and fork engagement. The result is
a living dashboard that shows which frameworks are gaining momentum and which are losing steam.

## 🏆 Pulse Leaderboard

| Rank | Framework | Pulse | Stars | ⭐ 7d | Commits (4w) | Last Release | Category |
|------|-----------|-------|-------|-------|--------------|--------------|----------|
| 1 | [CrewAI](https://github.com/crewAIInc/crewAI) | 🟢 **84.9** | 48.3k | 🚀 +504 | 160 | today | `multi-agent` |
| 2 | [Mastra](https://github.com/mastra-ai/mastra) | 🟢 **72.4** | 22.8k | 🚀 +212 | 748 | 12 days ago | `typescript` |
| 3 | [BrowserUse](https://github.com/browser-use/browser-use) | 🟢 **70.0** | 86.5k | 🚀 +906 | 0 | 5 days ago | `web-agent` |
| 4 | [Claude Agent SDK](https://github.com/anthropics/claude-code) | 🟡 **64.5** | 110.8k | 🚀 +8729 | 0 | today | `orchestration` |
| 5 | [LangGraph](https://github.com/langchain-ai/langgraph) | 🟡 **63.6** | 28.7k | 🚀 +498 | 0 | today | `orchestration` |
| 6 | [LlamaIndex](https://github.com/run-llama/llama_index) | 🟡 **56.6** | 48.4k | 🚀 +176 | 0 | 4 days ago | `data-agent` |
| 7 | [Agno](https://github.com/agno-agi/agno) | 🟡 **51.7** | 39.2k | 🚀 +152 | 0 | 5 days ago | `multi-agent` |
| 8 | [OpenAI Agents SDK](https://github.com/openai/openai-agents-python) | 🟡 **50.9** | 20.6k | 🚀 +144 | 0 | 2 days ago | `orchestration` |
| 9 | [PydanticAI](https://github.com/pydantic/pydantic-ai) | 🟡 **50.7** | 16.2k | 🚀 +146 | 0 | today | `structured` |
| 10 | [Semantic Kernel](https://github.com/microsoft/semantic-kernel) | 🟡 **50.3** | 27.7k | 📈 +53 | 0 | today | `enterprise` |
| 11 | [Haystack](https://github.com/deepset-ai/haystack) | 🟡 **48.4** | 24.8k | 📈 +80 | 0 | 6 days ago | `pipeline` |
| 12 | [Google ADK](https://github.com/google/adk-python) | 🟡 **48.2** | 18.8k | 🚀 +110 | 0 | 5 days ago | `orchestration` |
| 13 | [AG2](https://github.com/ag2ai/ag2) | 🟡 **47.3** | 4.4k | 📈 +32 | 0 | 3 days ago | `multi-agent` |
| 14 | [DSPy](https://github.com/stanfordnlp/dspy) | 🟡 **45.3** | 33.5k | 🚀 +159 | 0 | 2 mo ago | `optimization` |
| 15 | [Letta](https://github.com/letta-ai/letta) | 🟡 **44.2** | 21.9k | 📈 +91 | 0 | 7 days ago | `memory` |
| 16 | [AutoGen](https://github.com/microsoft/autogen) | 🟡 **43.7** | 56.8k | 🚀 +230 | 0 | 6 mo ago | `multi-agent` |
| 17 | [Composio](https://github.com/ComposioHQ/composio) | 🟡 **43.5** | 27.7k | 📈 +73 | 0 | today | `tooling` |
| 18 | [Smolagents](https://github.com/huggingface/smolagents) | 🟠 **36.2** | 26.5k | 🚀 +101 | 0 | 2 mo ago | `lightweight` |
| 19 | [Swarm](https://github.com/openai/swarm) | 🔴 **9.1** | 21.3k | ↗️ +12 | 0 | — | `experimental` |

## 📂 By Category

- `data-agent`: **LlamaIndex** (56.6)
- `enterprise`: **Semantic Kernel** (50.3)
- `experimental`: **Swarm** (9.1)
- `lightweight`: **Smolagents** (36.2)
- `memory`: **Letta** (44.2)
- `multi-agent`: **CrewAI** (84.9), **Agno** (51.7), **AG2** (47.3), **AutoGen** (43.7)
- `optimization`: **DSPy** (45.3)
- `orchestration`: **Claude Agent SDK** (64.5), **LangGraph** (63.6), **OpenAI Agents SDK** (50.9), **Google ADK** (48.2)
- `pipeline`: **Haystack** (48.4)
- `structured`: **PydanticAI** (50.7)
- `tooling`: **Composio** (43.5)
- `typescript`: **Mastra** (72.4)
- `web-agent`: **BrowserUse** (70.0)

## 🔍 Top 5 — Score Breakdown

| Framework | Star Velocity | Release Freshness | Issue Health | Commit Activity | Community | Fork Ratio |
|-----------|:---:|:---:|:---:|:---:|:---:|:---:|
| **CrewAI** | 78.1 | 100.0 | 94.6 | 100 | 56.8 | 54.5 |
| **Mastra** | 32.9 | 96.0 | 94.2 | 100 | 75.6 | 32.5 |
| **BrowserUse** | 100 | 98.3 | 97.3 | 0.0 | 61.2 | 46.3 |
| **Claude Agent SDK** | 100 | 100.0 | 79.1 | 0.0 | 9.4 | 66.6 |
| **LangGraph** | 77.2 | 100.0 | 80.4 | 0.0 | 54.4 | 68.3 |

## 💡 Key Insights

- **Hottest framework**: CrewAI with a Pulse Score of 84.9
- **Fastest growing**: Claude Agent SDK gained +8729 stars this week
- **Most active development**: Mastra with 748 commits in the last 4 weeks
- **Stale releases**: Swarm haven't released in a while

## 📦 Recent Releases

- **Semantic Kernel** [`python-1.41.2`](https://github.com/microsoft/semantic-kernel/releases/tag/python-1.41.2) — today
- **Composio** [`@composio/cli@0.2.20`](https://github.com/ComposioHQ/composio/releases/tag/@composio/cli@0.2.20) — today
- **PydanticAI** [`v1.78.0`](https://github.com/pydantic/pydantic-ai/releases/tag/v1.78.0) — today
- **Claude Agent SDK** [`v2.1.96`](https://github.com/anthropics/claude-code/releases/tag/v2.1.96) — today
- **LangGraph** [`cli==0.4.21`](https://github.com/langchain-ai/langgraph/releases/tag/cli==0.4.21) — today
- **CrewAI** [`1.14.0`](https://github.com/crewAIInc/crewAI/releases/tag/1.14.0) — today
- **OpenAI Agents SDK** [`v0.13.5`](https://github.com/openai/openai-agents-python/releases/tag/v0.13.5) — 2 days ago
- **AG2** [`v0.11.5`](https://github.com/ag2ai/ag2/releases/tag/v0.11.5) — 3 days ago
- **LlamaIndex** [`v0.14.20`](https://github.com/run-llama/llama_index/releases/tag/v0.14.20) — 4 days ago
- **Google ADK** [`v1.28.1`](https://github.com/google/adk-python/releases/tag/v1.28.1) — 5 days ago

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

*Powered by GitHub Actions • Data refreshed daily • Last run: 2026-04-08 07:44 UTC*