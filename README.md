# 🔬 AI Agent Framework Pulse Tracker

[![Daily Update](https://github.com/PurpleHaze2320/ai-agent-pulse/actions/workflows/track.yml/badge.svg)](https://github.com/PurpleHaze2320/ai-agent-pulse/actions/workflows/track.yml)
[![Frameworks Tracked](https://img.shields.io/badge/frameworks-19-blue)](https://github.com/PurpleHaze2320/ai-agent-pulse)
[![License: MIT](https://img.shields.io/badge/License-MIT-green.svg)](https://opensource.org/licenses/MIT)
[![GitHub stars](https://img.shields.io/github/stars/PurpleHaze2320/ai-agent-pulse?style=social)](https://github.com/PurpleHaze2320/ai-agent-pulse/stargazers)

> Automated daily tracking of the AI agent framework ecosystem's health, momentum, and trends.
> Last updated: **2026-09-13 11:27 UTC** | Tracking **19** frameworks

## How It Works

This bot runs daily via GitHub Actions and collects metrics from the GitHub API for the most important
AI agent frameworks. It computes a **Pulse Score** (0-100) based on six weighted signals: star velocity,
release freshness, issue health, commit activity, community size, and fork engagement. The result is
a living dashboard that shows which frameworks are gaining momentum and which are losing steam.

## 🏆 Pulse Leaderboard

| Rank | Framework | Pulse | Stars | ⭐ 7d | Commits (4w) | Last Release | Category |
|------|-----------|-------|-------|-------|--------------|--------------|----------|
| 1 | [BrowserUse](https://github.com/browser-use/browser-use) | 🟢 **89.8** | 114.4k | 🚀 +1936 | 185 | 9 days ago | `web-agent` |
| 2 | [Claude Agent SDK](https://github.com/anthropics/claude-code) | 🟢 **80.9** | 144.9k | 🚀 +673 | 77 | today | `orchestration` |
| 3 | [Mastra](https://github.com/mastra-ai/mastra) | 🟢 **79.6** | 28.0k | 🚀 +262 | 1199 | 2 days ago | `typescript` |
| 4 | [CrewAI](https://github.com/crewAIInc/crewAI) | 🟢 **79.3** | 58.4k | 🚀 +294 | 88 | 3 days ago | `multi-agent` |
| 5 | [OpenAI Agents SDK](https://github.com/openai/openai-agents-python) | 🟢 **75.3** | 29.4k | 🚀 +183 | 87 | 3 days ago | `orchestration` |
| 6 | [PydanticAI](https://github.com/pydantic/pydantic-ai) | 🟢 **74.6** | 19.9k | 🚀 +150 | 196 | 1 day ago | `structured` |
| 7 | [Google ADK](https://github.com/google/adk-python) | 🟢 **74.4** | 21.5k | 📈 +97 | 328 | 2 days ago | `orchestration` |
| 8 | [Haystack](https://github.com/deepset-ai/haystack) | 🟢 **70.8** | 26.5k | 📈 +61 | 162 | 10 days ago | `pipeline` |
| 9 | [LangGraph](https://github.com/langchain-ai/langgraph) | 🟡 **69.2** | 41.6k | 🚀 +431 | 29 | 16 days ago | `orchestration` |
| 10 | [Agno](https://github.com/agno-agi/agno) | 🟡 **68.7** | 42.1k | 📈 +82 | 93 | 4 days ago | `multi-agent` |
| 11 | [Composio](https://github.com/ComposioHQ/composio) | 🟡 **67.0** | 30.2k | 📈 +80 | 204 | 1 day ago | `tooling` |
| 12 | [DSPy](https://github.com/stanfordnlp/dspy) | 🟡 **60.7** | 38.0k | 🚀 +195 | 36 | 1 day ago | `optimization` |
| 13 | [LlamaIndex](https://github.com/run-llama/llama_index) | 🟡 **60.0** | 52.1k | 🚀 +109 | 28 | 24 days ago | `data-agent` |
| 14 | [AG2](https://github.com/ag2ai/ag2) | 🟡 **57.9** | 4.9k | ↗️ +16 | 40 | 1 day ago | `multi-agent` |
| 15 | [Semantic Kernel](https://github.com/microsoft/semantic-kernel) | 🟡 **53.8** | 28.6k | ↗️ +16 | 20 | 9 days ago | `enterprise` |
| 16 | [Letta](https://github.com/letta-ai/letta) | 🟠 **39.5** | 24.7k | 📈 +89 | 3 | 4 mo ago | `memory` |
| 17 | [Smolagents](https://github.com/huggingface/smolagents) | 🟠 **36.3** | 29.3k | 🚀 +114 | 0 | 3 mo ago | `lightweight` |
| 18 | [AutoGen](https://github.com/microsoft/autogen) | 🟠 **33.7** | 61.0k | 🚀 +127 | 0 | 11 mo ago | `multi-agent` |
| 19 | [Swarm](https://github.com/openai/swarm) | 🔴 **9.7** | 22.0k | 📈 +28 | 0 | — | `experimental` |

## 📂 By Category

- `data-agent`: **LlamaIndex** (60.0)
- `enterprise`: **Semantic Kernel** (53.8)
- `experimental`: **Swarm** (9.7)
- `lightweight`: **Smolagents** (36.3)
- `memory`: **Letta** (39.5)
- `multi-agent`: **CrewAI** (79.3), **Agno** (68.7), **AG2** (57.9), **AutoGen** (33.7)
- `optimization`: **DSPy** (60.7)
- `orchestration`: **Claude Agent SDK** (80.9), **OpenAI Agents SDK** (75.3), **Google ADK** (74.4), **LangGraph** (69.2)
- `pipeline`: **Haystack** (70.8)
- `structured`: **PydanticAI** (74.6)
- `tooling`: **Composio** (67.0)
- `typescript`: **Mastra** (79.6)
- `web-agent`: **BrowserUse** (89.8)

## 🔍 Top 5 — Score Breakdown

| Framework | Star Velocity | Release Freshness | Issue Health | Commit Activity | Community | Fork Ratio |
|-----------|:---:|:---:|:---:|:---:|:---:|:---:|
| **BrowserUse** | 100 | 97.0 | 92.3 | 100 | 72.0 | 44.0 |
| **Claude Agent SDK** | 100 | 100.0 | 87.1 | 77.0 | 10.8 | 63.9 |
| **Mastra** | 48.8 | 99.3 | 95.0 | 100 | 93.0 | 39.7 |
| **CrewAI** | 61.7 | 99.0 | 95.0 | 88.0 | 64.2 | 57.7 |
| **OpenAI Agents SDK** | 37.1 | 99.0 | 99.0 | 87.0 | 75.0 | 64.2 |

## 💡 Key Insights

- **Hottest framework**: BrowserUse with a Pulse Score of 89.8
- **Fastest growing**: BrowserUse gained +1936 stars this week
- **Most active development**: Mastra with 1199 commits in the last 4 weeks
- **Stale releases**: AutoGen, Swarm haven't released in a while

## 📦 Recent Releases

- **Claude Agent SDK** [`v2.1.270`](https://github.com/anthropics/claude-code/releases/tag/v2.1.270) — today
- **PydanticAI** [`v2.43.0`](https://github.com/pydantic/pydantic-ai/releases/tag/v2.43.0) — 1 day ago
- **DSPy** [`3.4.0b1`](https://github.com/stanfordnlp/dspy/releases/tag/3.4.0b1) — 1 day ago *(pre-release)*
- **AG2** [`v1.0.5`](https://github.com/ag2ai/ag2/releases/tag/v1.0.5) — 1 day ago
- **Composio** [`versioning-example@0.1.1-beta.1`](https://github.com/ComposioHQ/composio/releases/tag/versioning-example@0.1.1-beta.1) — 1 day ago *(pre-release)*
- **Mastra** [`@mastra/core@1.66.0`](https://github.com/mastra-ai/mastra/releases/tag/@mastra/core@1.66.0) — 2 days ago
- **Google ADK** [`v2.9.0`](https://github.com/google/adk-python/releases/tag/v2.9.0) — 2 days ago
- **CrewAI** [`1.15.21`](https://github.com/crewAIInc/crewAI/releases/tag/1.15.21) — 3 days ago
- **OpenAI Agents SDK** [`v0.22.2`](https://github.com/openai/openai-agents-python/releases/tag/v0.22.2) — 3 days ago
- **Agno** [`v3.0.9`](https://github.com/agno-agi/agno/releases/tag/v3.0.9) — 4 days ago

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

*Powered by GitHub Actions • Data refreshed daily • Last run: 2026-09-13 11:27 UTC*