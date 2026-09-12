# 🔬 AI Agent Framework Pulse Tracker

[![Daily Update](https://github.com/PurpleHaze2320/ai-agent-pulse/actions/workflows/track.yml/badge.svg)](https://github.com/PurpleHaze2320/ai-agent-pulse/actions/workflows/track.yml)
[![Frameworks Tracked](https://img.shields.io/badge/frameworks-19-blue)](https://github.com/PurpleHaze2320/ai-agent-pulse)
[![License: MIT](https://img.shields.io/badge/License-MIT-green.svg)](https://opensource.org/licenses/MIT)
[![GitHub stars](https://img.shields.io/github/stars/PurpleHaze2320/ai-agent-pulse?style=social)](https://github.com/PurpleHaze2320/ai-agent-pulse/stargazers)

> Automated daily tracking of the AI agent framework ecosystem's health, momentum, and trends.
> Last updated: **2026-09-12 10:24 UTC** | Tracking **19** frameworks

## How It Works

This bot runs daily via GitHub Actions and collects metrics from the GitHub API for the most important
AI agent frameworks. It computes a **Pulse Score** (0-100) based on six weighted signals: star velocity,
release freshness, issue health, commit activity, community size, and fork engagement. The result is
a living dashboard that shows which frameworks are gaining momentum and which are losing steam.

## 🏆 Pulse Leaderboard

| Rank | Framework | Pulse | Stars | ⭐ 7d | Commits (4w) | Last Release | Category |
|------|-----------|-------|-------|-------|--------------|--------------|----------|
| 1 | [BrowserUse](https://github.com/browser-use/browser-use) | 🟢 **89.9** | 114.3k | 🚀 +1956 | 206 | 8 days ago | `web-agent` |
| 2 | [CrewAI](https://github.com/crewAIInc/crewAI) | 🟢 **82.0** | 58.4k | 🚀 +299 | 110 | 2 days ago | `multi-agent` |
| 3 | [Mastra](https://github.com/mastra-ai/mastra) | 🟢 **79.2** | 28.0k | 🚀 +249 | 1587 | 1 day ago | `typescript` |
| 4 | [OpenAI Agents SDK](https://github.com/openai/openai-agents-python) | 🟢 **77.8** | 29.4k | 🚀 +178 | 158 | 2 days ago | `orchestration` |
| 5 | [PydanticAI](https://github.com/pydantic/pydantic-ai) | 🟢 **74.3** | 19.9k | 🚀 +142 | 252 | today | `structured` |
| 6 | [Google ADK](https://github.com/google/adk-python) | 🟢 **74.3** | 21.5k | 📈 +92 | 425 | 1 day ago | `orchestration` |
| 7 | [Claude Agent SDK](https://github.com/anthropics/claude-code) | 🟢 **72.5** | 144.8k | 🚀 +695 | 35 | today | `orchestration` |
| 8 | [Haystack](https://github.com/deepset-ai/haystack) | 🟢 **71.0** | 26.5k | 📈 +66 | 220 | 9 days ago | `pipeline` |
| 9 | [Agno](https://github.com/agno-agi/agno) | 🟢 **70.4** | 42.1k | 📈 +86 | 104 | 3 days ago | `multi-agent` |
| 10 | [LangGraph](https://github.com/langchain-ai/langgraph) | 🟢 **70.2** | 41.5k | 🚀 +432 | 33 | 15 days ago | `orchestration` |
| 11 | [Composio](https://github.com/ComposioHQ/composio) | 🟡 **67.2** | 30.1k | 📈 +85 | 266 | today | `tooling` |
| 12 | [DSPy](https://github.com/stanfordnlp/dspy) | 🟡 **65.3** | 38.0k | 🚀 +191 | 59 | today | `optimization` |
| 13 | [LlamaIndex](https://github.com/run-llama/llama_index) | 🟡 **61.4** | 52.1k | 🚀 +105 | 35 | 23 days ago | `data-agent` |
| 14 | [AG2](https://github.com/ag2ai/ag2) | 🟡 **59.8** | 4.9k | ↗️ +17 | 49 | today | `multi-agent` |
| 15 | [Semantic Kernel](https://github.com/microsoft/semantic-kernel) | 🟡 **54.7** | 28.6k | ↗️ +18 | 24 | 8 days ago | `enterprise` |
| 16 | [Letta](https://github.com/letta-ai/letta) | 🟠 **39.4** | 24.7k | 📈 +86 | 3 | 4 mo ago | `memory` |
| 17 | [Smolagents](https://github.com/huggingface/smolagents) | 🟠 **37.2** | 29.3k | 🚀 +128 | 2 | 3 mo ago | `lightweight` |
| 18 | [AutoGen](https://github.com/microsoft/autogen) | 🟠 **34.1** | 60.9k | 🚀 +136 | 0 | 11 mo ago | `multi-agent` |
| 19 | [Swarm](https://github.com/openai/swarm) | 🔴 **9.7** | 22.0k | 📈 +28 | 0 | — | `experimental` |

## 📂 By Category

- `data-agent`: **LlamaIndex** (61.4)
- `enterprise`: **Semantic Kernel** (54.7)
- `experimental`: **Swarm** (9.7)
- `lightweight`: **Smolagents** (37.2)
- `memory`: **Letta** (39.4)
- `multi-agent`: **CrewAI** (82.0), **Agno** (70.4), **AG2** (59.8), **AutoGen** (34.1)
- `optimization`: **DSPy** (65.3)
- `orchestration`: **OpenAI Agents SDK** (77.8), **Google ADK** (74.3), **Claude Agent SDK** (72.5), **LangGraph** (70.2)
- `pipeline`: **Haystack** (71.0)
- `structured`: **PydanticAI** (74.3)
- `tooling`: **Composio** (67.2)
- `typescript`: **Mastra** (79.2)
- `web-agent`: **BrowserUse** (89.9)

## 🔍 Top 5 — Score Breakdown

| Framework | Star Velocity | Release Freshness | Issue Health | Commit Activity | Community | Fork Ratio |
|-----------|:---:|:---:|:---:|:---:|:---:|:---:|
| **BrowserUse** | 100 | 97.3 | 92.3 | 100 | 72.0 | 44.0 |
| **CrewAI** | 62.7 | 99.3 | 95.2 | 100 | 64.2 | 57.6 |
| **Mastra** | 47.0 | 99.7 | 95.3 | 100 | 93.0 | 39.6 |
| **OpenAI Agents SDK** | 36.7 | 99.3 | 99.1 | 100 | 75.0 | 64.2 |
| **PydanticAI** | 29.1 | 100.0 | 80.8 | 100 | 95.2 | 54.4 |

## 💡 Key Insights

- **Hottest framework**: BrowserUse with a Pulse Score of 89.9
- **Fastest growing**: BrowserUse gained +1956 stars this week
- **Most active development**: Mastra with 1587 commits in the last 4 weeks
- **Stale releases**: AutoGen, Swarm haven't released in a while

## 📦 Recent Releases

- **PydanticAI** [`v2.43.0`](https://github.com/pydantic/pydantic-ai/releases/tag/v2.43.0) — today
- **DSPy** [`3.4.0b1`](https://github.com/stanfordnlp/dspy/releases/tag/3.4.0b1) — today *(pre-release)*
- **AG2** [`v1.0.5`](https://github.com/ag2ai/ag2/releases/tag/v1.0.5) — today
- **Claude Agent SDK** [`v2.1.269`](https://github.com/anthropics/claude-code/releases/tag/v2.1.269) — today
- **Composio** [`versioning-example@0.1.1-beta.1`](https://github.com/ComposioHQ/composio/releases/tag/versioning-example@0.1.1-beta.1) — today *(pre-release)*
- **Mastra** [`@mastra/core@1.66.0`](https://github.com/mastra-ai/mastra/releases/tag/@mastra/core@1.66.0) — 1 day ago
- **Google ADK** [`v2.9.0`](https://github.com/google/adk-python/releases/tag/v2.9.0) — 1 day ago
- **CrewAI** [`1.15.21`](https://github.com/crewAIInc/crewAI/releases/tag/1.15.21) — 2 days ago
- **OpenAI Agents SDK** [`v0.22.2`](https://github.com/openai/openai-agents-python/releases/tag/v0.22.2) — 2 days ago
- **Agno** [`v3.0.9`](https://github.com/agno-agi/agno/releases/tag/v3.0.9) — 3 days ago

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

*Powered by GitHub Actions • Data refreshed daily • Last run: 2026-09-12 10:24 UTC*