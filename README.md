# 🔬 AI Agent Framework Pulse Tracker

[![Daily Update](https://github.com/PurpleHaze2320/ai-agent-pulse/actions/workflows/track.yml/badge.svg)](https://github.com/PurpleHaze2320/ai-agent-pulse/actions/workflows/track.yml)
[![Frameworks Tracked](https://img.shields.io/badge/frameworks-19-blue)](https://github.com/PurpleHaze2320/ai-agent-pulse)
[![License: MIT](https://img.shields.io/badge/License-MIT-green.svg)](https://opensource.org/licenses/MIT)
[![GitHub stars](https://img.shields.io/github/stars/PurpleHaze2320/ai-agent-pulse?style=social)](https://github.com/PurpleHaze2320/ai-agent-pulse/stargazers)

> Automated daily tracking of the AI agent framework ecosystem's health, momentum, and trends.
> Last updated: **2026-07-19 08:26 UTC** | Tracking **19** frameworks

## How It Works

This bot runs daily via GitHub Actions and collects metrics from the GitHub API for the most important
AI agent frameworks. It computes a **Pulse Score** (0-100) based on six weighted signals: star velocity,
release freshness, issue health, commit activity, community size, and fork engagement. The result is
a living dashboard that shows which frameworks are gaining momentum and which are losing steam.

## 🏆 Pulse Leaderboard

| Rank | Framework | Pulse | Stars | ⭐ 7d | Commits (4w) | Last Release | Category |
|------|-----------|-------|-------|-------|--------------|--------------|----------|
| 1 | [BrowserUse](https://github.com/browser-use/browser-use) | 🟢 **84.0** | 105.5k | 🚀 +1180 | 71 | 2 days ago | `web-agent` |
| 2 | [Mastra](https://github.com/mastra-ai/mastra) | 🟢 **80.5** | 26.3k | 🚀 +266 | 871 | 3 days ago | `typescript` |
| 3 | [CrewAI](https://github.com/crewAIInc/crewAI) | 🟢 **78.6** | 55.8k | 🚀 +386 | 62 | 1 day ago | `multi-agent` |
| 4 | [PydanticAI](https://github.com/pydantic/pydantic-ai) | 🟢 **77.9** | 18.6k | 🚀 +216 | 224 | 1 day ago | `structured` |
| 5 | [OpenAI Agents SDK](https://github.com/openai/openai-agents-python) | 🟢 **76.0** | 28.0k | 🚀 +179 | 106 | 2 days ago | `orchestration` |
| 6 | [Agno](https://github.com/agno-agi/agno) | 🟢 **74.3** | 41.3k | 🚀 +170 | 121 | 1 day ago | `multi-agent` |
| 7 | [LangGraph](https://github.com/langchain-ai/langgraph) | 🟢 **72.5** | 37.6k | 🚀 +507 | 25 | 9 days ago | `orchestration` |
| 8 | [Google ADK](https://github.com/google/adk-python) | 🟢 **71.8** | 20.7k | 📈 +88 | 258 | 11 days ago | `orchestration` |
| 9 | [Haystack](https://github.com/deepset-ai/haystack) | 🟢 **70.0** | 25.9k | 📈 +68 | 181 | 10 days ago | `pipeline` |
| 10 | [Claude Agent SDK](https://github.com/anthropics/claude-code) | 🟡 **69.8** | 138.2k | 🚀 +737 | 23 | today | `orchestration` |
| 11 | [Composio](https://github.com/ComposioHQ/composio) | 🟡 **66.9** | 29.3k | 📈 +92 | 110 | 2 days ago | `tooling` |
| 12 | [LlamaIndex](https://github.com/run-llama/llama_index) | 🟡 **61.0** | 50.9k | 🚀 +147 | 23 | 24 days ago | `data-agent` |
| 13 | [Semantic Kernel](https://github.com/microsoft/semantic-kernel) | 🟡 **52.5** | 28.3k | 📈 +32 | 11 | 11 days ago | `enterprise` |
| 14 | [DSPy](https://github.com/stanfordnlp/dspy) | 🟡 **49.8** | 36.2k | 🚀 +160 | 0 | 1 mo ago | `optimization` |
| 15 | [AG2](https://github.com/ag2ai/ag2) | 🟡 **49.3** | 4.8k | 📈 +23 | 0 | 15 days ago | `multi-agent` |
| 16 | [Letta](https://github.com/letta-ai/letta) | 🟡 **43.2** | 23.9k | 🚀 +112 | 1 | 2 mo ago | `memory` |
| 17 | [Smolagents](https://github.com/huggingface/smolagents) | 🟡 **41.7** | 28.4k | 🚀 +128 | 4 | 1 mo ago | `lightweight` |
| 18 | [AutoGen](https://github.com/microsoft/autogen) | 🟠 **35.3** | 59.8k | 🚀 +138 | 0 | 9 mo ago | `multi-agent` |
| 19 | [Swarm](https://github.com/openai/swarm) | 🔴 **9.6** | 21.8k | 📈 +36 | 0 | — | `experimental` |

## 📂 By Category

- `data-agent`: **LlamaIndex** (61.0)
- `enterprise`: **Semantic Kernel** (52.5)
- `experimental`: **Swarm** (9.6)
- `lightweight`: **Smolagents** (41.7)
- `memory`: **Letta** (43.2)
- `multi-agent`: **CrewAI** (78.6), **Agno** (74.3), **AG2** (49.3), **AutoGen** (35.3)
- `optimization`: **DSPy** (49.8)
- `orchestration`: **OpenAI Agents SDK** (76.0), **LangGraph** (72.5), **Google ADK** (71.8), **Claude Agent SDK** (69.8)
- `pipeline`: **Haystack** (70.0)
- `structured`: **PydanticAI** (77.9)
- `tooling`: **Composio** (66.9)
- `typescript`: **Mastra** (80.5)
- `web-agent`: **BrowserUse** (84.0)

## 🔍 Top 5 — Score Breakdown

| Framework | Star Velocity | Release Freshness | Issue Health | Commit Activity | Community | Fork Ratio |
|-----------|:---:|:---:|:---:|:---:|:---:|:---:|
| **BrowserUse** | 100 | 99.3 | 94.8 | 71.0 | 63.0 | 44.1 |
| **Mastra** | 53.6 | 99.0 | 95.4 | 100 | 93.0 | 37.5 |
| **CrewAI** | 81.1 | 99.7 | 96.0 | 62.0 | 59.6 | 56.5 |
| **PydanticAI** | 42.1 | 99.7 | 85.8 | 100 | 94.8 | 51.1 |
| **OpenAI Agents SDK** | 36.3 | 99.3 | 98.2 | 100 | 61.2 | 62.1 |

## 💡 Key Insights

- **Hottest framework**: BrowserUse with a Pulse Score of 84.0
- **Fastest growing**: BrowserUse gained +1180 stars this week
- **Most active development**: Mastra with 871 commits in the last 4 weeks
- **Stale releases**: AutoGen, Swarm haven't released in a while

## 📦 Recent Releases

- **Claude Agent SDK** [`v2.1.215`](https://github.com/anthropics/claude-code/releases/tag/v2.1.215) — today
- **PydanticAI** [`v2.13.0`](https://github.com/pydantic/pydantic-ai/releases/tag/v2.13.0) — 1 day ago
- **CrewAI** [`1.15.4`](https://github.com/crewAIInc/crewAI/releases/tag/1.15.4) — 1 day ago
- **Agno** [`v2.7.4`](https://github.com/agno-agi/agno/releases/tag/v2.7.4) — 1 day ago
- **BrowserUse** [`0.13.6`](https://github.com/browser-use/browser-use/releases/tag/0.13.6) — 2 days ago
- **OpenAI Agents SDK** [`v0.18.3`](https://github.com/openai/openai-agents-python/releases/tag/v0.18.3) — 2 days ago
- **Composio** [`@composio/vercel@0.11.1`](https://github.com/ComposioHQ/composio/releases/tag/@composio/vercel@0.11.1) — 2 days ago
- **Mastra** [`@mastra/core@1.51.0`](https://github.com/mastra-ai/mastra/releases/tag/@mastra/core@1.51.0) — 3 days ago
- **LangGraph** [`1.2.9`](https://github.com/langchain-ai/langgraph/releases/tag/1.2.9) — 9 days ago
- **Haystack** [`v2.31.0`](https://github.com/deepset-ai/haystack/releases/tag/v2.31.0) — 10 days ago

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

*Powered by GitHub Actions • Data refreshed daily • Last run: 2026-07-19 08:26 UTC*