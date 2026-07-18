# 🔬 AI Agent Framework Pulse Tracker

[![Daily Update](https://github.com/PurpleHaze2320/ai-agent-pulse/actions/workflows/track.yml/badge.svg)](https://github.com/PurpleHaze2320/ai-agent-pulse/actions/workflows/track.yml)
[![Frameworks Tracked](https://img.shields.io/badge/frameworks-19-blue)](https://github.com/PurpleHaze2320/ai-agent-pulse)
[![License: MIT](https://img.shields.io/badge/License-MIT-green.svg)](https://opensource.org/licenses/MIT)
[![GitHub stars](https://img.shields.io/github/stars/PurpleHaze2320/ai-agent-pulse?style=social)](https://github.com/PurpleHaze2320/ai-agent-pulse/stargazers)

> Automated daily tracking of the AI agent framework ecosystem's health, momentum, and trends.
> Last updated: **2026-07-18 08:00 UTC** | Tracking **19** frameworks

## How It Works

This bot runs daily via GitHub Actions and collects metrics from the GitHub API for the most important
AI agent frameworks. It computes a **Pulse Score** (0-100) based on six weighted signals: star velocity,
release freshness, issue health, commit activity, community size, and fork engagement. The result is
a living dashboard that shows which frameworks are gaining momentum and which are losing steam.

## 🏆 Pulse Leaderboard

| Rank | Framework | Pulse | Stars | ⭐ 7d | Commits (4w) | Last Release | Category |
|------|-----------|-------|-------|-------|--------------|--------------|----------|
| 1 | [CrewAI](https://github.com/crewAIInc/crewAI) | 🟢 **86.3** | 55.7k | 🚀 +382 | 102 | today | `multi-agent` |
| 2 | [BrowserUse](https://github.com/browser-use/browser-use) | 🟢 **85.1** | 105.3k | 🚀 +1146 | 76 | 1 day ago | `web-agent` |
| 3 | [Mastra](https://github.com/mastra-ai/mastra) | 🟢 **80.8** | 26.3k | 🚀 +269 | 1219 | 2 days ago | `typescript` |
| 4 | [OpenAI Agents SDK](https://github.com/openai/openai-agents-python) | 🟢 **76.1** | 28.0k | 🚀 +181 | 129 | 1 day ago | `orchestration` |
| 5 | [Agno](https://github.com/agno-agi/agno) | 🟢 **72.6** | 41.2k | 🚀 +126 | 154 | today | `multi-agent` |
| 6 | [Google ADK](https://github.com/google/adk-python) | 🟢 **71.9** | 20.6k | 📈 +88 | 339 | 10 days ago | `orchestration` |
| 7 | [Claude Agent SDK](https://github.com/anthropics/claude-code) | 🟢 **70.8** | 138.1k | 🚀 +772 | 28 | today | `orchestration` |
| 8 | [Haystack](https://github.com/deepset-ai/haystack) | 🟡 **69.8** | 25.9k | 📈 +62 | 256 | 9 days ago | `pipeline` |
| 9 | [LangGraph](https://github.com/langchain-ai/langgraph) | 🟡 **67.6** | 37.5k | 🚀 +521 | 0 | 8 days ago | `orchestration` |
| 10 | [Composio](https://github.com/ComposioHQ/composio) | 🟡 **67.2** | 29.3k | 📈 +99 | 168 | 1 day ago | `tooling` |
| 11 | [LlamaIndex](https://github.com/run-llama/llama_index) | 🟡 **61.3** | 50.9k | 🚀 +136 | 26 | 23 days ago | `data-agent` |
| 12 | [PydanticAI](https://github.com/pydantic/pydantic-ai) | 🟡 **59.0** | 18.6k | 🚀 +244 | 0 | today | `structured` |
| 13 | [Semantic Kernel](https://github.com/microsoft/semantic-kernel) | 🟡 **50.4** | 28.3k | 📈 +33 | 0 | 10 days ago | `enterprise` |
| 14 | [DSPy](https://github.com/stanfordnlp/dspy) | 🟡 **50.3** | 36.2k | 🚀 +168 | 0 | 1 mo ago | `optimization` |
| 15 | [AG2](https://github.com/ag2ai/ag2) | 🟡 **49.5** | 4.8k | 📈 +28 | 0 | 14 days ago | `multi-agent` |
| 16 | [Letta](https://github.com/letta-ai/letta) | 🟡 **42.7** | 23.8k | 🚀 +101 | 0 | 2 mo ago | `memory` |
| 17 | [Smolagents](https://github.com/huggingface/smolagents) | 🟡 **41.7** | 28.4k | 🚀 +127 | 4 | 1 mo ago | `lightweight` |
| 18 | [AutoGen](https://github.com/microsoft/autogen) | 🟠 **35.9** | 59.8k | 🚀 +153 | 0 | 9 mo ago | `multi-agent` |
| 19 | [Swarm](https://github.com/openai/swarm) | 🔴 **9.1** | 21.8k | 📈 +21 | 0 | — | `experimental` |

## 📂 By Category

- `data-agent`: **LlamaIndex** (61.3)
- `enterprise`: **Semantic Kernel** (50.4)
- `experimental`: **Swarm** (9.1)
- `lightweight`: **Smolagents** (41.7)
- `memory`: **Letta** (42.7)
- `multi-agent`: **CrewAI** (86.3), **Agno** (72.6), **AG2** (49.5), **AutoGen** (35.9)
- `optimization`: **DSPy** (50.3)
- `orchestration`: **OpenAI Agents SDK** (76.1), **Google ADK** (71.9), **Claude Agent SDK** (70.8), **LangGraph** (67.6)
- `pipeline`: **Haystack** (69.8)
- `structured`: **PydanticAI** (59.0)
- `tooling`: **Composio** (67.2)
- `typescript`: **Mastra** (80.8)
- `web-agent`: **BrowserUse** (85.1)

## 🔍 Top 5 — Score Breakdown

| Framework | Star Velocity | Release Freshness | Issue Health | Commit Activity | Community | Fork Ratio |
|-----------|:---:|:---:|:---:|:---:|:---:|:---:|
| **CrewAI** | 81.1 | 100.0 | 96.1 | 100 | 59.6 | 56.5 |
| **BrowserUse** | 100 | 99.7 | 94.8 | 76.0 | 63.0 | 44.1 |
| **Mastra** | 54.3 | 99.3 | 95.4 | 100 | 93.0 | 37.4 |
| **OpenAI Agents SDK** | 36.6 | 99.7 | 98.2 | 100 | 61.2 | 62.1 |
| **Agno** | 24.5 | 100.0 | 80.7 | 100 | 89.0 | 54.8 |

## 💡 Key Insights

- **Hottest framework**: CrewAI with a Pulse Score of 86.3
- **Fastest growing**: BrowserUse gained +1146 stars this week
- **Most active development**: Mastra with 1219 commits in the last 4 weeks
- **Stale releases**: AutoGen, Swarm haven't released in a while

## 📦 Recent Releases

- **PydanticAI** [`v2.13.0`](https://github.com/pydantic/pydantic-ai/releases/tag/v2.13.0) — today
- **Claude Agent SDK** [`v2.1.214`](https://github.com/anthropics/claude-code/releases/tag/v2.1.214) — today
- **CrewAI** [`1.15.4`](https://github.com/crewAIInc/crewAI/releases/tag/1.15.4) — today
- **Agno** [`v2.7.4`](https://github.com/agno-agi/agno/releases/tag/v2.7.4) — today
- **BrowserUse** [`0.13.6`](https://github.com/browser-use/browser-use/releases/tag/0.13.6) — 1 day ago
- **OpenAI Agents SDK** [`v0.18.3`](https://github.com/openai/openai-agents-python/releases/tag/v0.18.3) — 1 day ago
- **Composio** [`@composio/vercel@0.11.1`](https://github.com/ComposioHQ/composio/releases/tag/@composio/vercel@0.11.1) — 1 day ago
- **Mastra** [`@mastra/core@1.51.0`](https://github.com/mastra-ai/mastra/releases/tag/@mastra/core@1.51.0) — 2 days ago
- **LangGraph** [`1.2.9`](https://github.com/langchain-ai/langgraph/releases/tag/1.2.9) — 8 days ago
- **Haystack** [`v2.31.0`](https://github.com/deepset-ai/haystack/releases/tag/v2.31.0) — 9 days ago

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

*Powered by GitHub Actions • Data refreshed daily • Last run: 2026-07-18 08:00 UTC*