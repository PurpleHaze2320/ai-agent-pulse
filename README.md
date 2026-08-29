# 🔬 AI Agent Framework Pulse Tracker

[![Daily Update](https://github.com/PurpleHaze2320/ai-agent-pulse/actions/workflows/track.yml/badge.svg)](https://github.com/PurpleHaze2320/ai-agent-pulse/actions/workflows/track.yml)
[![Frameworks Tracked](https://img.shields.io/badge/frameworks-19-blue)](https://github.com/PurpleHaze2320/ai-agent-pulse)
[![License: MIT](https://img.shields.io/badge/License-MIT-green.svg)](https://opensource.org/licenses/MIT)
[![GitHub stars](https://img.shields.io/github/stars/PurpleHaze2320/ai-agent-pulse?style=social)](https://github.com/PurpleHaze2320/ai-agent-pulse/stargazers)

> Automated daily tracking of the AI agent framework ecosystem's health, momentum, and trends.
> Last updated: **2026-08-29 12:32 UTC** | Tracking **19** frameworks

## How It Works

This bot runs daily via GitHub Actions and collects metrics from the GitHub API for the most important
AI agent frameworks. It computes a **Pulse Score** (0-100) based on six weighted signals: star velocity,
release freshness, issue health, commit activity, community size, and fork engagement. The result is
a living dashboard that shows which frameworks are gaining momentum and which are losing steam.

## 🏆 Pulse Leaderboard

| Rank | Framework | Pulse | Stars | ⭐ 7d | Commits (4w) | Last Release | Category |
|------|-----------|-------|-------|-------|--------------|--------------|----------|
| 1 | [BrowserUse](https://github.com/browser-use/browser-use) | 🟢 **89.5** | 111.6k | 🚀 +1572 | 168 | 12 days ago | `web-agent` |
| 2 | [CrewAI](https://github.com/crewAIInc/crewAI) | 🟢 **83.3** | 57.8k | 🚀 +335 | 100 | 1 day ago | `multi-agent` |
| 3 | [OpenAI Agents SDK](https://github.com/openai/openai-agents-python) | 🟢 **78.0** | 29.1k | 🚀 +204 | 344 | 9 days ago | `orchestration` |
| 4 | [Mastra](https://github.com/mastra-ai/mastra) | 🟢 **77.5** | 27.6k | 🚀 +197 | 1749 | 1 day ago | `typescript` |
| 5 | [PydanticAI](https://github.com/pydantic/pydantic-ai) | 🟢 **74.3** | 19.6k | 🚀 +133 | 254 | today | `structured` |
| 6 | [Google ADK](https://github.com/google/adk-python) | 🟢 **74.3** | 21.3k | 🚀 +103 | 473 | 1 day ago | `orchestration` |
| 7 | [LangGraph](https://github.com/langchain-ai/langgraph) | 🟢 **73.4** | 40.7k | 🚀 +443 | 36 | 1 day ago | `orchestration` |
| 8 | [Haystack](https://github.com/deepset-ai/haystack) | 🟢 **71.4** | 26.4k | 📈 +80 | 187 | 4 days ago | `pipeline` |
| 9 | [Claude Agent SDK](https://github.com/anthropics/claude-code) | 🟢 **70.6** | 143.4k | 🚀 +1019 | 28 | today | `orchestration` |
| 10 | [DSPy](https://github.com/stanfordnlp/dspy) | 🟡 **68.2** | 37.6k | 🚀 +158 | 75 | 7 days ago | `optimization` |
| 11 | [Composio](https://github.com/ComposioHQ/composio) | 🟡 **68.2** | 29.9k | 🚀 +113 | 344 | today | `tooling` |
| 12 | [Agno](https://github.com/agno-agi/agno) | 🟡 **65.0** | 42.0k | 🚀 +133 | 64 | 3 days ago | `multi-agent` |
| 13 | [LlamaIndex](https://github.com/run-llama/llama_index) | 🟡 **63.2** | 51.9k | 🚀 +117 | 34 | 9 days ago | `data-agent` |
| 14 | [AG2](https://github.com/ag2ai/ag2) | 🟡 **61.1** | 4.9k | ↗️ +9 | 57 | today | `multi-agent` |
| 15 | [Semantic Kernel](https://github.com/microsoft/semantic-kernel) | 🟡 **54.1** | 28.5k | 📈 +38 | 18 | 10 days ago | `enterprise` |
| 16 | [Letta](https://github.com/letta-ai/letta) | 🟡 **42.2** | 24.5k | 🚀 +145 | 3 | 3 mo ago | `memory` |
| 17 | [Smolagents](https://github.com/huggingface/smolagents) | 🟠 **37.7** | 29.0k | 🚀 +115 | 2 | 3 mo ago | `lightweight` |
| 18 | [AutoGen](https://github.com/microsoft/autogen) | 🟠 **33.6** | 60.7k | 🚀 +119 | 0 | 11 mo ago | `multi-agent` |
| 19 | [Swarm](https://github.com/openai/swarm) | 🔴 **9.4** | 21.9k | ↗️ +17 | 0 | — | `experimental` |

## 📂 By Category

- `data-agent`: **LlamaIndex** (63.2)
- `enterprise`: **Semantic Kernel** (54.1)
- `experimental`: **Swarm** (9.4)
- `lightweight`: **Smolagents** (37.7)
- `memory`: **Letta** (42.2)
- `multi-agent`: **CrewAI** (83.3), **Agno** (65.0), **AG2** (61.1), **AutoGen** (33.6)
- `optimization`: **DSPy** (68.2)
- `orchestration`: **OpenAI Agents SDK** (78.0), **Google ADK** (74.3), **LangGraph** (73.4), **Claude Agent SDK** (70.6)
- `pipeline`: **Haystack** (71.4)
- `structured`: **PydanticAI** (74.3)
- `tooling`: **Composio** (68.2)
- `typescript`: **Mastra** (77.5)
- `web-agent`: **BrowserUse** (89.5)

## 🔍 Top 5 — Score Breakdown

| Framework | Star Velocity | Release Freshness | Issue Health | Commit Activity | Community | Fork Ratio |
|-----------|:---:|:---:|:---:|:---:|:---:|:---:|
| **BrowserUse** | 100 | 96.0 | 93.1 | 100 | 69.2 | 43.9 |
| **CrewAI** | 68.1 | 99.7 | 97.0 | 100 | 60.2 | 57.3 |
| **OpenAI Agents SDK** | 40.1 | 97.0 | 98.8 | 100 | 73.6 | 63.7 |
| **Mastra** | 40.1 | 99.7 | 95.4 | 100 | 93.0 | 39.3 |
| **PydanticAI** | 28.8 | 100.0 | 82.1 | 100 | 95.0 | 53.3 |

## 💡 Key Insights

- **Hottest framework**: BrowserUse with a Pulse Score of 89.5
- **Fastest growing**: BrowserUse gained +1572 stars this week
- **Most active development**: Mastra with 1749 commits in the last 4 weeks
- **Stale releases**: AutoGen, Swarm haven't released in a while

## 📦 Recent Releases

- **PydanticAI** [`v2.36.0`](https://github.com/pydantic/pydantic-ai/releases/tag/v2.36.0) — today
- **AG2** [`v1.0.3`](https://github.com/ag2ai/ag2/releases/tag/v1.0.3) — today
- **Claude Agent SDK** [`v2.1.251`](https://github.com/anthropics/claude-code/releases/tag/v2.1.251) — today
- **Composio** [`@composio/cli@0.4.1-beta.371`](https://github.com/ComposioHQ/composio/releases/tag/@composio/cli@0.4.1-beta.371) — today *(pre-release)*
- **Mastra** [`@mastra/core@1.63.0`](https://github.com/mastra-ai/mastra/releases/tag/@mastra/core@1.63.0) — 1 day ago
- **Google ADK** [`v1.39.1`](https://github.com/google/adk-python/releases/tag/v1.39.1) — 1 day ago
- **LangGraph** [`sdk==0.4.4`](https://github.com/langchain-ai/langgraph/releases/tag/sdk==0.4.4) — 1 day ago
- **CrewAI** [`1.15.18`](https://github.com/crewAIInc/crewAI/releases/tag/1.15.18) — 1 day ago
- **Agno** [`v3.0.1`](https://github.com/agno-agi/agno/releases/tag/v3.0.1) — 3 days ago
- **Haystack** [`v3.1.0`](https://github.com/deepset-ai/haystack/releases/tag/v3.1.0) — 4 days ago

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

*Powered by GitHub Actions • Data refreshed daily • Last run: 2026-08-29 12:32 UTC*