# 🔬 AI Agent Framework Pulse Tracker

[![Daily Update](https://github.com/PurpleHaze2320/ai-agent-pulse/actions/workflows/track.yml/badge.svg)](https://github.com/PurpleHaze2320/ai-agent-pulse/actions/workflows/track.yml)
[![Frameworks Tracked](https://img.shields.io/badge/frameworks-19-blue)](https://github.com/PurpleHaze2320/ai-agent-pulse)
[![License: MIT](https://img.shields.io/badge/License-MIT-green.svg)](https://opensource.org/licenses/MIT)
[![GitHub stars](https://img.shields.io/github/stars/PurpleHaze2320/ai-agent-pulse?style=social)](https://github.com/PurpleHaze2320/ai-agent-pulse/stargazers)

> Automated daily tracking of the AI agent framework ecosystem's health, momentum, and trends.
> Last updated: **2026-07-20 09:24 UTC** | Tracking **19** frameworks

## How It Works

This bot runs daily via GitHub Actions and collects metrics from the GitHub API for the most important
AI agent frameworks. It computes a **Pulse Score** (0-100) based on six weighted signals: star velocity,
release freshness, issue health, commit activity, community size, and fork engagement. The result is
a living dashboard that shows which frameworks are gaining momentum and which are losing steam.

## 🏆 Pulse Leaderboard

| Rank | Framework | Pulse | Stars | ⭐ 7d | Commits (4w) | Last Release | Category |
|------|-----------|-------|-------|-------|--------------|--------------|----------|
| 1 | [BrowserUse](https://github.com/browser-use/browser-use) | 🟢 **83.9** | 105.7k | 🚀 +1169 | 71 | 3 days ago | `web-agent` |
| 2 | [CrewAI](https://github.com/crewAIInc/crewAI) | 🟢 **79.2** | 55.8k | 🚀 +403 | 62 | 2 days ago | `multi-agent` |
| 3 | [Mastra](https://github.com/mastra-ai/mastra) | 🟢 **79.2** | 26.4k | 🚀 +231 | 879 | 4 days ago | `typescript` |
| 4 | [PydanticAI](https://github.com/pydantic/pydantic-ai) | 🟢 **77.2** | 18.7k | 🚀 +197 | 226 | 2 days ago | `structured` |
| 5 | [Google ADK](https://github.com/google/adk-python) | 🟢 **75.8** | 20.8k | 🚀 +193 | 258 | 12 days ago | `orchestration` |
| 6 | [OpenAI Agents SDK](https://github.com/openai/openai-agents-python) | 🟢 **75.5** | 28.0k | 🚀 +167 | 108 | 3 days ago | `orchestration` |
| 7 | [Agno](https://github.com/agno-agi/agno) | 🟢 **74.5** | 41.3k | 🚀 +180 | 126 | 3 days ago | `multi-agent` |
| 8 | [LangGraph](https://github.com/langchain-ai/langgraph) | 🟢 **72.4** | 37.7k | 🚀 +503 | 25 | 10 days ago | `orchestration` |
| 9 | [Claude Agent SDK](https://github.com/anthropics/claude-code) | 🟡 **69.7** | 138.4k | 🚀 +757 | 23 | 1 day ago | `orchestration` |
| 10 | [Composio](https://github.com/ComposioHQ/composio) | 🟡 **66.3** | 29.3k | 📈 +79 | 110 | 3 days ago | `tooling` |
| 11 | [LlamaIndex](https://github.com/run-llama/llama_index) | 🟡 **60.8** | 51.0k | 🚀 +141 | 23 | 25 days ago | `data-agent` |
| 12 | [DSPy](https://github.com/stanfordnlp/dspy) | 🟡 **54.4** | 36.2k | 🚀 +154 | 24 | 1 mo ago | `optimization` |
| 13 | [Semantic Kernel](https://github.com/microsoft/semantic-kernel) | 🟡 **52.4** | 28.3k | 📈 +33 | 11 | 13 days ago | `enterprise` |
| 14 | [Haystack](https://github.com/deepset-ai/haystack) | 🟡 **50.8** | 26.0k | 📈 +72 | 0 | today | `pipeline` |
| 15 | [AG2](https://github.com/ag2ai/ag2) | 🟡 **49.0** | 4.8k | ↗️ +20 | 0 | 16 days ago | `multi-agent` |
| 16 | [Letta](https://github.com/letta-ai/letta) | 🟡 **43.0** | 23.9k | 🚀 +109 | 1 | 2 mo ago | `memory` |
| 17 | [Smolagents](https://github.com/huggingface/smolagents) | 🟡 **41.5** | 28.4k | 🚀 +125 | 4 | 1 mo ago | `lightweight` |
| 18 | [AutoGen](https://github.com/microsoft/autogen) | 🟠 **35.2** | 59.8k | 🚀 +137 | 0 | 9 mo ago | `multi-agent` |
| 19 | [Swarm](https://github.com/openai/swarm) | 🔴 **10.2** | 21.8k | 📈 +51 | 0 | — | `experimental` |

## 📂 By Category

- `data-agent`: **LlamaIndex** (60.8)
- `enterprise`: **Semantic Kernel** (52.4)
- `experimental`: **Swarm** (10.2)
- `lightweight`: **Smolagents** (41.5)
- `memory`: **Letta** (43.0)
- `multi-agent`: **CrewAI** (79.2), **Agno** (74.5), **AG2** (49.0), **AutoGen** (35.2)
- `optimization`: **DSPy** (54.4)
- `orchestration`: **Google ADK** (75.8), **OpenAI Agents SDK** (75.5), **LangGraph** (72.4), **Claude Agent SDK** (69.7)
- `pipeline`: **Haystack** (50.8)
- `structured`: **PydanticAI** (77.2)
- `tooling`: **Composio** (66.3)
- `typescript`: **Mastra** (79.2)
- `web-agent`: **BrowserUse** (83.9)

## 🔍 Top 5 — Score Breakdown

| Framework | Star Velocity | Release Freshness | Issue Health | Commit Activity | Community | Fork Ratio |
|-----------|:---:|:---:|:---:|:---:|:---:|:---:|
| **BrowserUse** | 100 | 99.0 | 94.8 | 71.0 | 63.0 | 44.0 |
| **CrewAI** | 83.6 | 99.3 | 96.1 | 62.0 | 59.6 | 56.5 |
| **Mastra** | 48.7 | 98.7 | 95.2 | 100 | 93.0 | 37.5 |
| **PydanticAI** | 39.6 | 99.3 | 85.7 | 100 | 94.8 | 51.2 |
| **Google ADK** | 35.8 | 96.0 | 86.7 | 100 | 74.6 | 71.6 |

## 💡 Key Insights

- **Hottest framework**: BrowserUse with a Pulse Score of 83.9
- **Fastest growing**: BrowserUse gained +1169 stars this week
- **Most active development**: Mastra with 879 commits in the last 4 weeks
- **Stale releases**: AutoGen, Swarm haven't released in a while

## 📦 Recent Releases

- **Haystack** [`v3.0.0-rc1`](https://github.com/deepset-ai/haystack/releases/tag/v3.0.0-rc1) — today *(pre-release)*
- **Claude Agent SDK** [`v2.1.215`](https://github.com/anthropics/claude-code/releases/tag/v2.1.215) — 1 day ago
- **PydanticAI** [`v2.13.0`](https://github.com/pydantic/pydantic-ai/releases/tag/v2.13.0) — 2 days ago
- **CrewAI** [`1.15.4`](https://github.com/crewAIInc/crewAI/releases/tag/1.15.4) — 2 days ago
- **Agno** [`v2.7.4`](https://github.com/agno-agi/agno/releases/tag/v2.7.4) — 3 days ago
- **BrowserUse** [`0.13.6`](https://github.com/browser-use/browser-use/releases/tag/0.13.6) — 3 days ago
- **OpenAI Agents SDK** [`v0.18.3`](https://github.com/openai/openai-agents-python/releases/tag/v0.18.3) — 3 days ago
- **Composio** [`@composio/vercel@0.11.1`](https://github.com/ComposioHQ/composio/releases/tag/@composio/vercel@0.11.1) — 3 days ago
- **Mastra** [`@mastra/core@1.51.0`](https://github.com/mastra-ai/mastra/releases/tag/@mastra/core@1.51.0) — 4 days ago
- **LangGraph** [`1.2.9`](https://github.com/langchain-ai/langgraph/releases/tag/1.2.9) — 10 days ago

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

*Powered by GitHub Actions • Data refreshed daily • Last run: 2026-07-20 09:24 UTC*