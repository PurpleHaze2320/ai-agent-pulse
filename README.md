# 🔬 AI Agent Framework Pulse Tracker

[![Daily Update](https://github.com/PurpleHaze2320/ai-agent-pulse/actions/workflows/track.yml/badge.svg)](https://github.com/PurpleHaze2320/ai-agent-pulse/actions/workflows/track.yml)
[![Frameworks Tracked](https://img.shields.io/badge/frameworks-19-blue)](https://github.com/PurpleHaze2320/ai-agent-pulse)
[![License: MIT](https://img.shields.io/badge/License-MIT-green.svg)](https://opensource.org/licenses/MIT)
[![GitHub stars](https://img.shields.io/github/stars/PurpleHaze2320/ai-agent-pulse?style=social)](https://github.com/PurpleHaze2320/ai-agent-pulse/stargazers)

> Automated daily tracking of the AI agent framework ecosystem's health, momentum, and trends.
> Last updated: **2026-10-12 14:56 UTC** | Tracking **19** frameworks

## How It Works

This bot runs daily via GitHub Actions and collects metrics from the GitHub API for the most important
AI agent frameworks. It computes a **Pulse Score** (0-100) based on six weighted signals: star velocity,
release freshness, issue health, commit activity, community size, and fork engagement. The result is
a living dashboard that shows which frameworks are gaining momentum and which are losing steam.

## 🏆 Pulse Leaderboard

| Rank | Framework | Pulse | Stars | ⭐ 7d | Commits (4w) | Last Release | Category |
|------|-----------|-------|-------|-------|--------------|--------------|----------|
| 1 | [BrowserUse](https://github.com/browser-use/browser-use) | 🟢 **80.0** | 117.7k | 🚀 +551 | 51 | 5 days ago | `web-agent` |
| 2 | [Claude Agent SDK](https://github.com/anthropics/claude-code) | 🟢 **76.7** | 150.4k | 🚀 +883 | 54 | 2 days ago | `orchestration` |
| 3 | [LangGraph](https://github.com/langchain-ai/langgraph) | 🟢 **76.6** | 43.1k | 🚀 +400 | 73 | 5 days ago | `orchestration` |
| 4 | [Mastra](https://github.com/mastra-ai/mastra) | 🟢 **76.6** | 28.7k | 🚀 +174 | 1792 | 4 days ago | `typescript` |
| 5 | [OpenAI Agents SDK](https://github.com/openai/openai-agents-python) | 🟢 **76.0** | 30.0k | 🚀 +144 | 201 | 9 days ago | `orchestration` |
| 6 | [PydanticAI](https://github.com/pydantic/pydantic-ai) | 🟢 **74.2** | 20.6k | 🚀 +162 | 685 | 6 days ago | `structured` |
| 7 | [Agno](https://github.com/agno-agi/agno) | 🟢 **71.7** | 42.7k | 🚀 +125 | 104 | today | `multi-agent` |
| 8 | [CrewAI](https://github.com/crewAIInc/crewAI) | 🟢 **71.0** | 59.6k | 🚀 +241 | 60 | 2 days ago | `multi-agent` |
| 9 | [Composio](https://github.com/ComposioHQ/composio) | 🟡 **66.2** | 30.5k | 📈 +66 | 201 | today | `tooling` |
| 10 | [LlamaIndex](https://github.com/run-llama/llama_index) | 🟡 **55.5** | 52.5k | 📈 +59 | 16 | 20 days ago | `data-agent` |
| 11 | [DSPy](https://github.com/stanfordnlp/dspy) | 🟡 **54.7** | 38.6k | 📈 +96 | 33 | 17 days ago | `optimization` |
| 12 | [Semantic Kernel](https://github.com/microsoft/semantic-kernel) | 🟡 **54.3** | 28.7k | 📈 +25 | 20 | 6 days ago | `enterprise` |
| 13 | [Google ADK](https://github.com/google/adk-python) | 🟡 **53.1** | 21.8k | 📈 +75 | 0 | 10 days ago | `orchestration` |
| 14 | [Haystack](https://github.com/deepset-ai/haystack) | 🟡 **50.9** | 26.7k | 📈 +64 | 0 | 11 days ago | `pipeline` |
| 15 | [AG2](https://github.com/ag2ai/ag2) | 🟡 **49.9** | 5.0k | ↗️ +16 | 0 | 1 day ago | `multi-agent` |
| 16 | [Letta](https://github.com/letta-ai/letta) | 🟠 **36.6** | 25.1k | 📈 +88 | 0 | 5 mo ago | `memory` |
| 17 | [Smolagents](https://github.com/huggingface/smolagents) | 🟠 **34.9** | 29.8k | 🚀 +115 | 5 | 4 mo ago | `lightweight` |
| 18 | [AutoGen](https://github.com/microsoft/autogen) | 🟠 **32.7** | 61.4k | 🚀 +110 | 0 | 1y ago | `multi-agent` |
| 19 | [Swarm](https://github.com/openai/swarm) | 🔴 **9.3** | 22.0k | ↗️ +15 | 0 | — | `experimental` |

## 📂 By Category

- `data-agent`: **LlamaIndex** (55.5)
- `enterprise`: **Semantic Kernel** (54.3)
- `experimental`: **Swarm** (9.3)
- `lightweight`: **Smolagents** (34.9)
- `memory`: **Letta** (36.6)
- `multi-agent`: **Agno** (71.7), **CrewAI** (71.0), **AG2** (49.9), **AutoGen** (32.7)
- `optimization`: **DSPy** (54.7)
- `orchestration`: **Claude Agent SDK** (76.7), **LangGraph** (76.6), **OpenAI Agents SDK** (76.0), **Google ADK** (53.1)
- `pipeline`: **Haystack** (50.9)
- `structured`: **PydanticAI** (74.2)
- `tooling`: **Composio** (66.2)
- `typescript`: **Mastra** (76.6)
- `web-agent`: **BrowserUse** (80.0)

## 🔍 Top 5 — Score Breakdown

| Framework | Star Velocity | Release Freshness | Issue Health | Commit Activity | Community | Fork Ratio |
|-----------|:---:|:---:|:---:|:---:|:---:|:---:|
| **BrowserUse** | 100 | 98.3 | 90.0 | 51.0 | 72.0 | 44.3 |
| **Claude Agent SDK** | 100 | 99.3 | 85.8 | 54.0 | 11.4 | 70.0 |
| **LangGraph** | 80.4 | 98.3 | 65.3 | 73.0 | 56.4 | 68.0 |
| **Mastra** | 36.0 | 98.7 | 95.8 | 100 | 93.4 | 41.2 |
| **OpenAI Agents SDK** | 29.2 | 97.0 | 98.8 | 100 | 80.2 | 65.0 |

## 💡 Key Insights

- **Hottest framework**: BrowserUse with a Pulse Score of 80.0
- **Fastest growing**: Claude Agent SDK gained +883 stars this week
- **Most active development**: Mastra with 1792 commits in the last 4 weeks
- **Stale releases**: AutoGen, Swarm haven't released in a while

## 📦 Recent Releases

- **Composio** [`versioning-example@0.1.7`](https://github.com/ComposioHQ/composio/releases/tag/versioning-example@0.1.7) — today
- **Agno** [`v3.1.3`](https://github.com/agno-agi/agno/releases/tag/v3.1.3) — today
- **AG2** [`v1.2.0`](https://github.com/ag2ai/ag2/releases/tag/v1.2.0) — 1 day ago
- **CrewAI** [`1.15.27`](https://github.com/crewAIInc/crewAI/releases/tag/1.15.27) — 2 days ago
- **Claude Agent SDK** [`v2.1.296`](https://github.com/anthropics/claude-code/releases/tag/v2.1.296) — 2 days ago
- **Mastra** [`@mastra/core@1.75.0`](https://github.com/mastra-ai/mastra/releases/tag/@mastra/core@1.75.0) — 4 days ago
- **LangGraph** [`cli==0.4.33`](https://github.com/langchain-ai/langgraph/releases/tag/cli==0.4.33) — 5 days ago
- **BrowserUse** [`0.13.11`](https://github.com/browser-use/browser-use/releases/tag/0.13.11) — 5 days ago
- **Semantic Kernel** [`python-1.45.0`](https://github.com/microsoft/semantic-kernel/releases/tag/python-1.45.0) — 6 days ago
- **PydanticAI** [`clai2-bleeding`](https://github.com/pydantic/pydantic-ai/releases/tag/clai2-bleeding) — 6 days ago *(pre-release)*

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

*Powered by GitHub Actions • Data refreshed daily • Last run: 2026-10-12 14:56 UTC*