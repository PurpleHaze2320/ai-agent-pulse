# 🔬 AI Agent Framework Pulse Tracker

[![Daily Update](https://github.com/PurpleHaze2320/ai-agent-pulse/actions/workflows/track.yml/badge.svg)](https://github.com/PurpleHaze2320/ai-agent-pulse/actions/workflows/track.yml)
[![Frameworks Tracked](https://img.shields.io/badge/frameworks-19-blue)](https://github.com/PurpleHaze2320/ai-agent-pulse)
[![License: MIT](https://img.shields.io/badge/License-MIT-green.svg)](https://opensource.org/licenses/MIT)
[![GitHub stars](https://img.shields.io/github/stars/PurpleHaze2320/ai-agent-pulse?style=social)](https://github.com/PurpleHaze2320/ai-agent-pulse/stargazers)

> Automated daily tracking of the AI agent framework ecosystem's health, momentum, and trends.
> Last updated: **2026-09-10 10:58 UTC** | Tracking **19** frameworks

## How It Works

This bot runs daily via GitHub Actions and collects metrics from the GitHub API for the most important
AI agent frameworks. It computes a **Pulse Score** (0-100) based on six weighted signals: star velocity,
release freshness, issue health, commit activity, community size, and fork engagement. The result is
a living dashboard that shows which frameworks are gaining momentum and which are losing steam.

## 🏆 Pulse Leaderboard

| Rank | Framework | Pulse | Stars | ⭐ 7d | Commits (4w) | Last Release | Category |
|------|-----------|-------|-------|-------|--------------|--------------|----------|
| 1 | [BrowserUse](https://github.com/browser-use/browser-use) | 🟢 **90.0** | 114.0k | 🚀 +1884 | 206 | 6 days ago | `web-agent` |
| 2 | [CrewAI](https://github.com/crewAIInc/crewAI) | 🟢 **81.7** | 58.3k | 🚀 +284 | 103 | today | `multi-agent` |
| 3 | [Mastra](https://github.com/mastra-ai/mastra) | 🟢 **78.8** | 27.9k | 🚀 +239 | 1361 | 1 day ago | `typescript` |
| 4 | [OpenAI Agents SDK](https://github.com/openai/openai-agents-python) | 🟢 **77.0** | 29.3k | 🚀 +153 | 153 | today | `orchestration` |
| 5 | [PydanticAI](https://github.com/pydantic/pydantic-ai) | 🟢 **74.4** | 19.8k | 🚀 +145 | 245 | 1 day ago | `structured` |
| 6 | [Google ADK](https://github.com/google/adk-python) | 🟢 **73.3** | 21.5k | 📈 +89 | 395 | 13 days ago | `orchestration` |
| 7 | [Haystack](https://github.com/deepset-ai/haystack) | 🟢 **71.1** | 26.5k | 📈 +64 | 206 | 7 days ago | `pipeline` |
| 8 | [Claude Agent SDK](https://github.com/anthropics/claude-code) | 🟢 **71.1** | 144.6k | 🚀 +737 | 28 | today | `orchestration` |
| 9 | [Agno](https://github.com/agno-agi/agno) | 🟢 **70.4** | 42.1k | 🚀 +105 | 96 | 1 day ago | `multi-agent` |
| 10 | [LangGraph](https://github.com/langchain-ai/langgraph) | 🟡 **69.3** | 41.4k | 🚀 +396 | 33 | 13 days ago | `orchestration` |
| 11 | [Composio](https://github.com/ComposioHQ/composio) | 🟡 **67.4** | 30.1k | 📈 +88 | 232 | 1 day ago | `tooling` |
| 12 | [LlamaIndex](https://github.com/run-llama/llama_index) | 🟡 **61.8** | 52.1k | 🚀 +119 | 33 | 21 days ago | `data-agent` |
| 13 | [DSPy](https://github.com/stanfordnlp/dspy) | 🟡 **61.2** | 37.9k | 🚀 +149 | 52 | 19 days ago | `optimization` |
| 14 | [AG2](https://github.com/ag2ai/ag2) | 🟡 **58.4** | 4.9k | ↗️ +16 | 43 | 3 days ago | `multi-agent` |
| 15 | [Semantic Kernel](https://github.com/microsoft/semantic-kernel) | 🟡 **54.9** | 28.6k | 📈 +24 | 23 | 6 days ago | `enterprise` |
| 16 | [Letta](https://github.com/letta-ai/letta) | 🟠 **39.6** | 24.7k | 📈 +90 | 2 | 3 mo ago | `memory` |
| 17 | [Smolagents](https://github.com/huggingface/smolagents) | 🟠 **37.6** | 29.3k | 🚀 +132 | 2 | 3 mo ago | `lightweight` |
| 18 | [AutoGen](https://github.com/microsoft/autogen) | 🟠 **33.9** | 60.9k | 🚀 +129 | 0 | 11 mo ago | `multi-agent` |
| 19 | [Swarm](https://github.com/openai/swarm) | 🔴 **9.6** | 22.0k | 📈 +26 | 0 | — | `experimental` |

## 📂 By Category

- `data-agent`: **LlamaIndex** (61.8)
- `enterprise`: **Semantic Kernel** (54.9)
- `experimental`: **Swarm** (9.6)
- `lightweight`: **Smolagents** (37.6)
- `memory`: **Letta** (39.6)
- `multi-agent`: **CrewAI** (81.7), **Agno** (70.4), **AG2** (58.4), **AutoGen** (33.9)
- `optimization`: **DSPy** (61.2)
- `orchestration`: **OpenAI Agents SDK** (77.0), **Google ADK** (73.3), **Claude Agent SDK** (71.1), **LangGraph** (69.3)
- `pipeline`: **Haystack** (71.1)
- `structured`: **PydanticAI** (74.4)
- `tooling`: **Composio** (67.4)
- `typescript`: **Mastra** (78.8)
- `web-agent`: **BrowserUse** (90.0)

## 🔍 Top 5 — Score Breakdown

| Framework | Star Velocity | Release Freshness | Issue Health | Commit Activity | Community | Fork Ratio |
|-----------|:---:|:---:|:---:|:---:|:---:|:---:|
| **BrowserUse** | 100 | 98.0 | 92.3 | 100 | 72.0 | 43.9 |
| **CrewAI** | 60.7 | 100.0 | 95.7 | 100 | 64.2 | 57.6 |
| **Mastra** | 45.6 | 99.7 | 94.9 | 100 | 93.0 | 39.5 |
| **OpenAI Agents SDK** | 33.0 | 100.0 | 99.0 | 100 | 74.6 | 64.0 |
| **PydanticAI** | 29.8 | 99.7 | 80.8 | 100 | 95.0 | 54.2 |

## 💡 Key Insights

- **Hottest framework**: BrowserUse with a Pulse Score of 90.0
- **Fastest growing**: BrowserUse gained +1884 stars this week
- **Most active development**: Mastra with 1361 commits in the last 4 weeks
- **Stale releases**: AutoGen, Swarm haven't released in a while

## 📦 Recent Releases

- **CrewAI** [`1.15.21`](https://github.com/crewAIInc/crewAI/releases/tag/1.15.21) — today
- **Claude Agent SDK** [`v2.1.267`](https://github.com/anthropics/claude-code/releases/tag/v2.1.267) — today
- **OpenAI Agents SDK** [`v0.22.2`](https://github.com/openai/openai-agents-python/releases/tag/v0.22.2) — today
- **Mastra** [`@mastra/core@1.65.0`](https://github.com/mastra-ai/mastra/releases/tag/@mastra/core@1.65.0) — 1 day ago
- **PydanticAI** [`v2.42.0`](https://github.com/pydantic/pydantic-ai/releases/tag/v2.42.0) — 1 day ago
- **Agno** [`v3.0.9`](https://github.com/agno-agi/agno/releases/tag/v3.0.9) — 1 day ago
- **Composio** [`@composio/cli@0.4.2-beta.384`](https://github.com/ComposioHQ/composio/releases/tag/@composio/cli@0.4.2-beta.384) — 1 day ago *(pre-release)*
- **AG2** [`v1.0.4`](https://github.com/ag2ai/ag2/releases/tag/v1.0.4) — 3 days ago
- **BrowserUse** [`0.13.10`](https://github.com/browser-use/browser-use/releases/tag/0.13.10) — 6 days ago
- **Semantic Kernel** [`dotnet-1.80.1`](https://github.com/microsoft/semantic-kernel/releases/tag/dotnet-1.80.1) — 6 days ago

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

*Powered by GitHub Actions • Data refreshed daily • Last run: 2026-09-10 10:58 UTC*