# 🔬 AI Agent Framework Pulse Tracker

[![Daily Update](https://github.com/PurpleHaze2320/ai-agent-pulse/actions/workflows/track.yml/badge.svg)](https://github.com/PurpleHaze2320/ai-agent-pulse/actions/workflows/track.yml)
[![Frameworks Tracked](https://img.shields.io/badge/frameworks-19-blue)](https://github.com/PurpleHaze2320/ai-agent-pulse)
[![License: MIT](https://img.shields.io/badge/License-MIT-green.svg)](https://opensource.org/licenses/MIT)
[![GitHub stars](https://img.shields.io/github/stars/PurpleHaze2320/ai-agent-pulse?style=social)](https://github.com/PurpleHaze2320/ai-agent-pulse/stargazers)

> Automated daily tracking of the AI agent framework ecosystem's health, momentum, and trends.
> Last updated: **2026-09-28 13:25 UTC** | Tracking **19** frameworks

## How It Works

This bot runs daily via GitHub Actions and collects metrics from the GitHub API for the most important
AI agent frameworks. It computes a **Pulse Score** (0-100) based on six weighted signals: star velocity,
release freshness, issue health, commit activity, community size, and fork engagement. The result is
a living dashboard that shows which frameworks are gaining momentum and which are losing steam.

## 🏆 Pulse Leaderboard

| Rank | Framework | Pulse | Stars | ⭐ 7d | Commits (4w) | Last Release | Category |
|------|-----------|-------|-------|-------|--------------|--------------|----------|
| 1 | [Claude Agent SDK](https://github.com/anthropics/claude-code) | 🟢 **85.7** | 148.4k | 🚀 +1050 | 119 | 2 days ago | `orchestration` |
| 2 | [BrowserUse](https://github.com/browser-use/browser-use) | 🟢 **77.5** | 116.6k | 🚀 +888 | 44 | 24 days ago | `web-agent` |
| 3 | [CrewAI](https://github.com/crewAIInc/crewAI) | 🟢 **77.0** | 59.1k | 🚀 +280 | 83 | 11 days ago | `multi-agent` |
| 4 | [OpenAI Agents SDK](https://github.com/openai/openai-agents-python) | 🟢 **76.0** | 29.7k | 🚀 +135 | 189 | 10 days ago | `orchestration` |
| 5 | [Mastra](https://github.com/mastra-ai/mastra) | 🟢 **75.8** | 28.4k | 🚀 +149 | 1828 | 3 days ago | `typescript` |
| 6 | [PydanticAI](https://github.com/pydantic/pydantic-ai) | 🟢 **74.4** | 20.2k | 🚀 +147 | 426 | 2 days ago | `structured` |
| 7 | [Google ADK](https://github.com/google/adk-python) | 🟢 **73.7** | 21.7k | 📈 +85 | 317 | 2 days ago | `orchestration` |
| 8 | [Haystack](https://github.com/deepset-ai/haystack) | 🟢 **71.0** | 26.6k | 📈 +54 | 192 | 4 days ago | `pipeline` |
| 9 | [Agno](https://github.com/agno-agi/agno) | 🟡 **69.7** | 42.4k | 📈 +89 | 99 | 5 days ago | `multi-agent` |
| 10 | [Composio](https://github.com/ComposioHQ/composio) | 🟡 **66.9** | 30.3k | 📈 +77 | 261 | today | `tooling` |
| 11 | [LangGraph](https://github.com/langchain-ai/langgraph) | 🟡 **64.8** | 42.4k | 🚀 +337 | 23 | 4 days ago | `orchestration` |
| 12 | [DSPy](https://github.com/stanfordnlp/dspy) | 🟡 **63.2** | 38.4k | 🚀 +221 | 46 | 3 days ago | `optimization` |
| 13 | [AG2](https://github.com/ag2ai/ag2) | 🟡 **60.6** | 5.0k | ↗️ +20 | 53 | 3 days ago | `multi-agent` |
| 14 | [LlamaIndex](https://github.com/run-llama/llama_index) | 🟡 **58.0** | 52.3k | 📈 +76 | 19 | 6 days ago | `data-agent` |
| 15 | [Semantic Kernel](https://github.com/microsoft/semantic-kernel) | 🟡 **50.0** | 28.6k | 📈 +23 | 5 | 24 days ago | `enterprise` |
| 16 | [Letta](https://github.com/letta-ai/letta) | 🟠 **39.4** | 24.9k | 🚀 +125 | 2 | 4 mo ago | `memory` |
| 17 | [Smolagents](https://github.com/huggingface/smolagents) | 🟠 **35.7** | 29.5k | 🚀 +118 | 2 | 4 mo ago | `lightweight` |
| 18 | [AutoGen](https://github.com/microsoft/autogen) | 🟠 **33.0** | 61.2k | 🚀 +111 | 0 | 12 mo ago | `multi-agent` |
| 19 | [Swarm](https://github.com/openai/swarm) | 🔴 **9.4** | 22.0k | ↗️ +17 | 0 | — | `experimental` |

## 📂 By Category

- `data-agent`: **LlamaIndex** (58.0)
- `enterprise`: **Semantic Kernel** (50.0)
- `experimental`: **Swarm** (9.4)
- `lightweight`: **Smolagents** (35.7)
- `memory`: **Letta** (39.4)
- `multi-agent`: **CrewAI** (77.0), **Agno** (69.7), **AG2** (60.6), **AutoGen** (33.0)
- `optimization`: **DSPy** (63.2)
- `orchestration`: **Claude Agent SDK** (85.7), **OpenAI Agents SDK** (76.0), **Google ADK** (73.7), **LangGraph** (64.8)
- `pipeline`: **Haystack** (71.0)
- `structured`: **PydanticAI** (74.4)
- `tooling`: **Composio** (66.9)
- `typescript`: **Mastra** (75.8)
- `web-agent`: **BrowserUse** (77.5)

## 🔍 Top 5 — Score Breakdown

| Framework | Star Velocity | Release Freshness | Issue Health | Commit Activity | Community | Fork Ratio |
|-----------|:---:|:---:|:---:|:---:|:---:|:---:|
| **Claude Agent SDK** | 100 | 99.3 | 86.6 | 100 | 11.2 | 67.1 |
| **BrowserUse** | 100 | 92.0 | 90.9 | 44.0 | 72.2 | 44.1 |
| **CrewAI** | 59.5 | 96.3 | 91.7 | 83.0 | 67.2 | 58.1 |
| **OpenAI Agents SDK** | 29.2 | 96.7 | 99.6 | 100 | 79.0 | 64.8 |
| **Mastra** | 33.3 | 99.0 | 95.5 | 100 | 93.2 | 40.5 |

## 💡 Key Insights

- **Hottest framework**: Claude Agent SDK with a Pulse Score of 85.7
- **Fastest growing**: Claude Agent SDK gained +1050 stars this week
- **Most active development**: Mastra with 1828 commits in the last 4 weeks
- **Stale releases**: AutoGen, Swarm haven't released in a while

## 📦 Recent Releases

- **Composio** [`@composio/cli@0.4.2-beta.406`](https://github.com/ComposioHQ/composio/releases/tag/@composio/cli@0.4.2-beta.406) — today *(pre-release)*
- **PydanticAI** [`v2.51.0`](https://github.com/pydantic/pydantic-ai/releases/tag/v2.51.0) — 2 days ago
- **Claude Agent SDK** [`v2.1.283`](https://github.com/anthropics/claude-code/releases/tag/v2.1.283) — 2 days ago
- **Google ADK** [`v2.10.0`](https://github.com/google/adk-python/releases/tag/v2.10.0) — 2 days ago
- **Mastra** [`@mastra/core@1.71.0`](https://github.com/mastra-ai/mastra/releases/tag/@mastra/core@1.71.0) — 3 days ago
- **DSPy** [`3.4.0`](https://github.com/stanfordnlp/dspy/releases/tag/3.4.0) — 3 days ago
- **AG2** [`v1.1.0`](https://github.com/ag2ai/ag2/releases/tag/v1.1.0) — 3 days ago
- **Haystack** [`v3.2.0`](https://github.com/deepset-ai/haystack/releases/tag/v3.2.0) — 4 days ago
- **LangGraph** [`cli==0.4.32.dev0`](https://github.com/langchain-ai/langgraph/releases/tag/cli==0.4.32.dev0) — 4 days ago
- **Agno** [`v3.0.11`](https://github.com/agno-agi/agno/releases/tag/v3.0.11) — 5 days ago

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

*Powered by GitHub Actions • Data refreshed daily • Last run: 2026-09-28 13:25 UTC*