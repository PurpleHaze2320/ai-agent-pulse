# 🔬 AI Agent Framework Pulse Tracker

[![Daily Update](https://github.com/PurpleHaze2320/ai-agent-pulse/actions/workflows/track.yml/badge.svg)](https://github.com/PurpleHaze2320/ai-agent-pulse/actions/workflows/track.yml)
[![Frameworks Tracked](https://img.shields.io/badge/frameworks-19-blue)](https://github.com/PurpleHaze2320/ai-agent-pulse)
[![License: MIT](https://img.shields.io/badge/License-MIT-green.svg)](https://opensource.org/licenses/MIT)
[![GitHub stars](https://img.shields.io/github/stars/PurpleHaze2320/ai-agent-pulse?style=social)](https://github.com/PurpleHaze2320/ai-agent-pulse/stargazers)

> Automated daily tracking of the AI agent framework ecosystem's health, momentum, and trends.
> Last updated: **2026-07-17 08:18 UTC** | Tracking **19** frameworks

## How It Works

This bot runs daily via GitHub Actions and collects metrics from the GitHub API for the most important
AI agent frameworks. It computes a **Pulse Score** (0-100) based on six weighted signals: star velocity,
release freshness, issue health, commit activity, community size, and fork engagement. The result is
a living dashboard that shows which frameworks are gaining momentum and which are losing steam.

## 🏆 Pulse Leaderboard

| Rank | Framework | Pulse | Stars | ⭐ 7d | Commits (4w) | Last Release | Category |
|------|-----------|-------|-------|-------|--------------|--------------|----------|
| 1 | [CrewAI](https://github.com/crewAIInc/crewAI) | 🟢 **86.5** | 55.7k | 🚀 +394 | 98 | today | `multi-agent` |
| 2 | [BrowserUse](https://github.com/browser-use/browser-use) | 🟢 **85.1** | 105.2k | 🚀 +1105 | 76 | today | `web-agent` |
| 3 | [PydanticAI](https://github.com/pydantic/pydantic-ai) | 🟢 **80.9** | 18.6k | 🚀 +299 | 257 | today | `structured` |
| 4 | [Mastra](https://github.com/mastra-ai/mastra) | 🟢 **80.4** | 26.3k | 🚀 +258 | 1160 | 1 day ago | `typescript` |
| 5 | [OpenAI Agents SDK](https://github.com/openai/openai-agents-python) | 🟢 **75.9** | 28.0k | 🚀 +173 | 122 | today | `orchestration` |
| 6 | [LangGraph](https://github.com/langchain-ai/langgraph) | 🟢 **75.5** | 37.5k | 🚀 +531 | 39 | 7 days ago | `orchestration` |
| 7 | [Agno](https://github.com/agno-agi/agno) | 🟢 **72.2** | 41.2k | 🚀 +119 | 150 | 2 days ago | `multi-agent` |
| 8 | [Google ADK](https://github.com/google/adk-python) | 🟢 **71.9** | 20.6k | 📈 +88 | 333 | 9 days ago | `orchestration` |
| 9 | [Claude Agent SDK](https://github.com/anthropics/claude-code) | 🟢 **70.6** | 138.0k | 🚀 +811 | 27 | today | `orchestration` |
| 10 | [Composio](https://github.com/ComposioHQ/composio) | 🟡 **67.3** | 29.3k | 🚀 +101 | 168 | today | `tooling` |
| 11 | [LlamaIndex](https://github.com/run-llama/llama_index) | 🟡 **61.4** | 50.9k | 🚀 +138 | 26 | 22 days ago | `data-agent` |
| 12 | [Semantic Kernel](https://github.com/microsoft/semantic-kernel) | 🟡 **50.4** | 28.3k | 📈 +32 | 0 | 9 days ago | `enterprise` |
| 13 | [DSPy](https://github.com/stanfordnlp/dspy) | 🟡 **50.2** | 36.2k | 🚀 +164 | 0 | 1 mo ago | `optimization` |
| 14 | [Haystack](https://github.com/deepset-ai/haystack) | 🟡 **49.8** | 25.9k | 📈 +61 | 0 | 8 days ago | `pipeline` |
| 15 | [AG2](https://github.com/ag2ai/ag2) | 🟡 **49.6** | 4.8k | 📈 +28 | 0 | 13 days ago | `multi-agent` |
| 16 | [Letta](https://github.com/letta-ai/letta) | 🟡 **42.7** | 23.8k | 📈 +100 | 0 | 2 mo ago | `memory` |
| 17 | [Smolagents](https://github.com/huggingface/smolagents) | 🟡 **41.7** | 28.4k | 🚀 +124 | 4 | 1 mo ago | `lightweight` |
| 18 | [AutoGen](https://github.com/microsoft/autogen) | 🟠 **36.3** | 59.8k | 🚀 +161 | 0 | 9 mo ago | `multi-agent` |
| 19 | [Swarm](https://github.com/openai/swarm) | 🔴 **9.1** | 21.8k | 📈 +22 | 0 | — | `experimental` |

## 📂 By Category

- `data-agent`: **LlamaIndex** (61.4)
- `enterprise`: **Semantic Kernel** (50.4)
- `experimental`: **Swarm** (9.1)
- `lightweight`: **Smolagents** (41.7)
- `memory`: **Letta** (42.7)
- `multi-agent`: **CrewAI** (86.5), **Agno** (72.2), **AG2** (49.6), **AutoGen** (36.3)
- `optimization`: **DSPy** (50.2)
- `orchestration`: **OpenAI Agents SDK** (75.9), **LangGraph** (75.5), **Google ADK** (71.9), **Claude Agent SDK** (70.6)
- `pipeline`: **Haystack** (49.8)
- `structured`: **PydanticAI** (80.9)
- `tooling`: **Composio** (67.3)
- `typescript`: **Mastra** (80.4)
- `web-agent`: **BrowserUse** (85.1)

## 🔍 Top 5 — Score Breakdown

| Framework | Star Velocity | Release Freshness | Issue Health | Commit Activity | Community | Fork Ratio |
|-----------|:---:|:---:|:---:|:---:|:---:|:---:|
| **CrewAI** | 83.7 | 100.0 | 96.0 | 98.0 | 59.6 | 56.5 |
| **BrowserUse** | 100 | 100.0 | 94.8 | 76.0 | 63.0 | 44.0 |
| **PydanticAI** | 53.9 | 100.0 | 85.9 | 100 | 94.8 | 51.1 |
| **Mastra** | 52.8 | 99.7 | 95.2 | 100 | 92.8 | 37.2 |
| **OpenAI Agents SDK** | 35.6 | 100.0 | 98.2 | 100 | 60.6 | 62.1 |

## 💡 Key Insights

- **Hottest framework**: CrewAI with a Pulse Score of 86.5
- **Fastest growing**: BrowserUse gained +1105 stars this week
- **Most active development**: Mastra with 1160 commits in the last 4 weeks
- **Stale releases**: AutoGen, Swarm haven't released in a while

## 📦 Recent Releases

- **BrowserUse** [`0.13.6`](https://github.com/browser-use/browser-use/releases/tag/0.13.6) — today
- **OpenAI Agents SDK** [`v0.18.3`](https://github.com/openai/openai-agents-python/releases/tag/v0.18.3) — today
- **PydanticAI** [`v2.12.0`](https://github.com/pydantic/pydantic-ai/releases/tag/v2.12.0) — today
- **Claude Agent SDK** [`v2.1.212`](https://github.com/anthropics/claude-code/releases/tag/v2.1.212) — today
- **CrewAI** [`1.15.3`](https://github.com/crewAIInc/crewAI/releases/tag/1.15.3) — today
- **Composio** [`@composio/vercel@0.11.1`](https://github.com/ComposioHQ/composio/releases/tag/@composio/vercel@0.11.1) — today
- **Mastra** [`@mastra/core@1.51.0`](https://github.com/mastra-ai/mastra/releases/tag/@mastra/core@1.51.0) — 1 day ago
- **Agno** [`v2.7.3`](https://github.com/agno-agi/agno/releases/tag/v2.7.3) — 2 days ago
- **LangGraph** [`1.2.9`](https://github.com/langchain-ai/langgraph/releases/tag/1.2.9) — 7 days ago
- **Haystack** [`v2.31.0`](https://github.com/deepset-ai/haystack/releases/tag/v2.31.0) — 8 days ago

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

*Powered by GitHub Actions • Data refreshed daily • Last run: 2026-07-17 08:18 UTC*