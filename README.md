# 🔬 AI Agent Framework Pulse Tracker

[![Daily Update](https://github.com/PurpleHaze2320/ai-agent-pulse/actions/workflows/track.yml/badge.svg)](https://github.com/PurpleHaze2320/ai-agent-pulse/actions/workflows/track.yml)
[![Frameworks Tracked](https://img.shields.io/badge/frameworks-19-blue)](https://github.com/PurpleHaze2320/ai-agent-pulse)
[![License: MIT](https://img.shields.io/badge/License-MIT-green.svg)](https://opensource.org/licenses/MIT)
[![GitHub stars](https://img.shields.io/github/stars/PurpleHaze2320/ai-agent-pulse?style=social)](https://github.com/PurpleHaze2320/ai-agent-pulse/stargazers)

> Automated daily tracking of the AI agent framework ecosystem's health, momentum, and trends.
> Last updated: **2026-08-28 18:26 UTC** | Tracking **19** frameworks

## How It Works

This bot runs daily via GitHub Actions and collects metrics from the GitHub API for the most important
AI agent frameworks. It computes a **Pulse Score** (0-100) based on six weighted signals: star velocity,
release freshness, issue health, commit activity, community size, and fork engagement. The result is
a living dashboard that shows which frameworks are gaining momentum and which are losing steam.

## 🏆 Pulse Leaderboard

| Rank | Framework | Pulse | Stars | ⭐ 7d | Commits (4w) | Last Release | Category |
|------|-----------|-------|-------|-------|--------------|--------------|----------|
| 1 | [BrowserUse](https://github.com/browser-use/browser-use) | 🟢 **89.5** | 111.6k | 🚀 +1640 | 145 | 11 days ago | `web-agent` |
| 2 | [CrewAI](https://github.com/crewAIInc/crewAI) | 🟢 **83.5** | 57.7k | 🚀 +345 | 99 | 1 day ago | `multi-agent` |
| 3 | [OpenAI Agents SDK](https://github.com/openai/openai-agents-python) | 🟢 **78.9** | 29.0k | 🚀 +229 | 344 | 9 days ago | `orchestration` |
| 4 | [Mastra](https://github.com/mastra-ai/mastra) | 🟢 **77.8** | 27.5k | 🚀 +201 | 1733 | today | `typescript` |
| 5 | [LangGraph](https://github.com/langchain-ai/langgraph) | 🟢 **74.8** | 40.6k | 🚀 +486 | 36 | today | `orchestration` |
| 6 | [PydanticAI](https://github.com/pydantic/pydantic-ai) | 🟢 **74.5** | 19.6k | 🚀 +138 | 243 | today | `structured` |
| 7 | [Haystack](https://github.com/deepset-ai/haystack) | 🟢 **71.6** | 26.3k | 📈 +83 | 186 | 4 days ago | `pipeline` |
| 8 | [DSPy](https://github.com/stanfordnlp/dspy) | 🟡 **68.6** | 37.6k | 🚀 +171 | 74 | 6 days ago | `optimization` |
| 9 | [Composio](https://github.com/ComposioHQ/composio) | 🟡 **68.5** | 29.9k | 🚀 +121 | 343 | today | `tooling` |
| 10 | [Agno](https://github.com/agno-agi/agno) | 🟡 **65.4** | 42.0k | 🚀 +142 | 64 | 2 days ago | `multi-agent` |
| 11 | [Claude Agent SDK](https://github.com/anthropics/claude-code) | 🟡 **65.0** | 143.3k | 🚀 +1093 | 0 | today | `orchestration` |
| 12 | [LlamaIndex](https://github.com/run-llama/llama_index) | 🟡 **63.7** | 51.9k | 🚀 +125 | 34 | 8 days ago | `data-agent` |
| 13 | [AG2](https://github.com/ag2ai/ag2) | 🟡 **59.6** | 4.9k | ↗️ +9 | 54 | 13 days ago | `multi-agent` |
| 14 | [Google ADK](https://github.com/google/adk-python) | 🟡 **54.4** | 21.3k | 🚀 +105 | 0 | today | `orchestration` |
| 15 | [Semantic Kernel](https://github.com/microsoft/semantic-kernel) | 🟡 **54.1** | 28.5k | 📈 +36 | 18 | 10 days ago | `enterprise` |
| 16 | [Letta](https://github.com/letta-ai/letta) | 🟡 **42.5** | 24.5k | 🚀 +152 | 3 | 3 mo ago | `memory` |
| 17 | [Smolagents](https://github.com/huggingface/smolagents) | 🟠 **37.9** | 29.0k | 🚀 +120 | 2 | 3 mo ago | `lightweight` |
| 18 | [AutoGen](https://github.com/microsoft/autogen) | 🟠 **33.8** | 60.7k | 🚀 +122 | 0 | 11 mo ago | `multi-agent` |
| 19 | [Swarm](https://github.com/openai/swarm) | 🔴 **9.4** | 21.9k | ↗️ +16 | 0 | — | `experimental` |

## 📂 By Category

- `data-agent`: **LlamaIndex** (63.7)
- `enterprise`: **Semantic Kernel** (54.1)
- `experimental`: **Swarm** (9.4)
- `lightweight`: **Smolagents** (37.9)
- `memory`: **Letta** (42.5)
- `multi-agent`: **CrewAI** (83.5), **Agno** (65.4), **AG2** (59.6), **AutoGen** (33.8)
- `optimization`: **DSPy** (68.6)
- `orchestration`: **OpenAI Agents SDK** (78.9), **LangGraph** (74.8), **Claude Agent SDK** (65.0), **Google ADK** (54.4)
- `pipeline`: **Haystack** (71.6)
- `structured`: **PydanticAI** (74.5)
- `tooling`: **Composio** (68.5)
- `typescript`: **Mastra** (77.8)
- `web-agent`: **BrowserUse** (89.5)

## 🔍 Top 5 — Score Breakdown

| Framework | Star Velocity | Release Freshness | Issue Health | Commit Activity | Community | Fork Ratio |
|-----------|:---:|:---:|:---:|:---:|:---:|:---:|
| **BrowserUse** | 100 | 96.3 | 93.0 | 100 | 68.6 | 43.9 |
| **CrewAI** | 69.9 | 99.7 | 96.9 | 99.0 | 60.2 | 57.3 |
| **OpenAI Agents SDK** | 43.8 | 97.0 | 99.1 | 100 | 73.6 | 63.6 |
| **Mastra** | 41.1 | 100.0 | 95.5 | 100 | 93.0 | 39.3 |
| **LangGraph** | 100 | 100.0 | 68.8 | 36.0 | 55.8 | 67.4 |

## 💡 Key Insights

- **Hottest framework**: BrowserUse with a Pulse Score of 89.5
- **Fastest growing**: BrowserUse gained +1640 stars this week
- **Most active development**: Mastra with 1733 commits in the last 4 weeks
- **Stale releases**: AutoGen, Swarm haven't released in a while

## 📦 Recent Releases

- **Claude Agent SDK** [`v2.1.251`](https://github.com/anthropics/claude-code/releases/tag/v2.1.251) — today
- **Composio** [`@composio/cli@0.4.1-beta.371`](https://github.com/ComposioHQ/composio/releases/tag/@composio/cli@0.4.1-beta.371) — today *(pre-release)*
- **Mastra** [`@mastra/core@1.63.0`](https://github.com/mastra-ai/mastra/releases/tag/@mastra/core@1.63.0) — today
- **PydanticAI** [`v2.35.3`](https://github.com/pydantic/pydantic-ai/releases/tag/v2.35.3) — today
- **Google ADK** [`v1.39.1`](https://github.com/google/adk-python/releases/tag/v1.39.1) — today
- **LangGraph** [`sdk==0.4.4`](https://github.com/langchain-ai/langgraph/releases/tag/sdk==0.4.4) — today
- **CrewAI** [`1.15.18`](https://github.com/crewAIInc/crewAI/releases/tag/1.15.18) — 1 day ago
- **Agno** [`v3.0.1`](https://github.com/agno-agi/agno/releases/tag/v3.0.1) — 2 days ago
- **Haystack** [`v3.1.0`](https://github.com/deepset-ai/haystack/releases/tag/v3.1.0) — 4 days ago
- **DSPy** [`3.3.1`](https://github.com/stanfordnlp/dspy/releases/tag/3.3.1) — 6 days ago

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

*Powered by GitHub Actions • Data refreshed daily • Last run: 2026-08-28 18:26 UTC*