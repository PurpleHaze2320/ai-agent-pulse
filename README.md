# 🔬 AI Agent Framework Pulse Tracker

[![Daily Update](https://github.com/PurpleHaze2320/ai-agent-pulse/actions/workflows/track.yml/badge.svg)](https://github.com/PurpleHaze2320/ai-agent-pulse/actions/workflows/track.yml)
[![Frameworks Tracked](https://img.shields.io/badge/frameworks-19-blue)](https://github.com/PurpleHaze2320/ai-agent-pulse)
[![License: MIT](https://img.shields.io/badge/License-MIT-green.svg)](https://opensource.org/licenses/MIT)
[![GitHub stars](https://img.shields.io/github/stars/PurpleHaze2320/ai-agent-pulse?style=social)](https://github.com/PurpleHaze2320/ai-agent-pulse/stargazers)

> Automated daily tracking of the AI agent framework ecosystem's health, momentum, and trends.
> Last updated: **2026-09-29 12:29 UTC** | Tracking **19** frameworks

## How It Works

This bot runs daily via GitHub Actions and collects metrics from the GitHub API for the most important
AI agent frameworks. It computes a **Pulse Score** (0-100) based on six weighted signals: star velocity,
release freshness, issue health, commit activity, community size, and fork engagement. The result is
a living dashboard that shows which frameworks are gaining momentum and which are losing steam.

## 🏆 Pulse Leaderboard

| Rank | Framework | Pulse | Stars | ⭐ 7d | Commits (4w) | Last Release | Category |
|------|-----------|-------|-------|-------|--------------|--------------|----------|
| 1 | [Claude Agent SDK](https://github.com/anthropics/claude-code) | 🟢 **85.8** | 148.6k | 🚀 +985 | 121 | today | `orchestration` |
| 2 | [CrewAI](https://github.com/crewAIInc/crewAI) | 🟢 **79.1** | 59.2k | 🚀 +278 | 90 | today | `multi-agent` |
| 3 | [BrowserUse](https://github.com/browser-use/browser-use) | 🟢 **77.4** | 116.7k | 🚀 +823 | 44 | 25 days ago | `web-agent` |
| 4 | [Mastra](https://github.com/mastra-ai/mastra) | 🟢 **76.1** | 28.4k | 🚀 +158 | 1885 | 4 days ago | `typescript` |
| 5 | [OpenAI Agents SDK](https://github.com/openai/openai-agents-python) | 🟢 **75.7** | 29.8k | 🚀 +128 | 204 | 11 days ago | `orchestration` |
| 6 | [PydanticAI](https://github.com/pydantic/pydantic-ai) | 🟢 **74.3** | 20.3k | 🚀 +150 | 473 | 3 days ago | `structured` |
| 7 | [Google ADK](https://github.com/google/adk-python) | 🟢 **73.5** | 21.7k | 📈 +77 | 336 | 3 days ago | `orchestration` |
| 8 | [Haystack](https://github.com/deepset-ai/haystack) | 🟢 **70.9** | 26.6k | 📈 +52 | 207 | 5 days ago | `pipeline` |
| 9 | [Agno](https://github.com/agno-agi/agno) | 🟡 **69.8** | 42.4k | 📈 +86 | 100 | 5 days ago | `multi-agent` |
| 10 | [Composio](https://github.com/ComposioHQ/composio) | 🟡 **67.1** | 30.4k | 📈 +78 | 269 | today | `tooling` |
| 11 | [LangGraph](https://github.com/langchain-ai/langgraph) | 🟡 **64.6** | 42.5k | 🚀 +333 | 23 | 5 days ago | `orchestration` |
| 12 | [DSPy](https://github.com/stanfordnlp/dspy) | 🟡 **63.0** | 38.4k | 🚀 +216 | 46 | 4 days ago | `optimization` |
| 13 | [AG2](https://github.com/ag2ai/ag2) | 🟡 **62.2** | 5.0k | ↗️ +17 | 62 | 4 days ago | `multi-agent` |
| 14 | [LlamaIndex](https://github.com/run-llama/llama_index) | 🟡 **58.6** | 52.3k | 📈 +74 | 23 | 7 days ago | `data-agent` |
| 15 | [Semantic Kernel](https://github.com/microsoft/semantic-kernel) | 🟡 **50.1** | 28.6k | 📈 +22 | 6 | 25 days ago | `enterprise` |
| 16 | [Letta](https://github.com/letta-ai/letta) | 🟠 **39.7** | 25.0k | 🚀 +132 | 2 | 4 mo ago | `memory` |
| 17 | [Smolagents](https://github.com/huggingface/smolagents) | 🟠 **36.8** | 29.6k | 🚀 +148 | 2 | 4 mo ago | `lightweight` |
| 18 | [AutoGen](https://github.com/microsoft/autogen) | 🟠 **32.9** | 61.2k | 🚀 +108 | 0 | 12 mo ago | `multi-agent` |
| 19 | [Swarm](https://github.com/openai/swarm) | 🔴 **9.3** | 22.0k | ↗️ +15 | 0 | — | `experimental` |

## 📂 By Category

- `data-agent`: **LlamaIndex** (58.6)
- `enterprise`: **Semantic Kernel** (50.1)
- `experimental`: **Swarm** (9.3)
- `lightweight`: **Smolagents** (36.8)
- `memory`: **Letta** (39.7)
- `multi-agent`: **CrewAI** (79.1), **Agno** (69.8), **AG2** (62.2), **AutoGen** (32.9)
- `optimization`: **DSPy** (63.0)
- `orchestration`: **Claude Agent SDK** (85.8), **OpenAI Agents SDK** (75.7), **Google ADK** (73.5), **LangGraph** (64.6)
- `pipeline`: **Haystack** (70.9)
- `structured`: **PydanticAI** (74.3)
- `tooling`: **Composio** (67.1)
- `typescript`: **Mastra** (76.1)
- `web-agent`: **BrowserUse** (77.4)

## 🔍 Top 5 — Score Breakdown

| Framework | Star Velocity | Release Freshness | Issue Health | Commit Activity | Community | Fork Ratio |
|-----------|:---:|:---:|:---:|:---:|:---:|:---:|
| **Claude Agent SDK** | 100 | 100.0 | 86.4 | 100 | 11.2 | 67.4 |
| **CrewAI** | 59.2 | 100.0 | 91.9 | 90.0 | 67.2 | 58.2 |
| **BrowserUse** | 100 | 91.7 | 90.8 | 44.0 | 72.2 | 44.1 |
| **Mastra** | 34.9 | 98.7 | 95.5 | 100 | 93.2 | 40.6 |
| **OpenAI Agents SDK** | 28.3 | 96.3 | 99.9 | 100 | 79.2 | 64.9 |

## 💡 Key Insights

- **Hottest framework**: Claude Agent SDK with a Pulse Score of 85.8
- **Fastest growing**: Claude Agent SDK gained +985 stars this week
- **Most active development**: Mastra with 1885 commits in the last 4 weeks
- **Stale releases**: AutoGen, Swarm haven't released in a while

## 📦 Recent Releases

- **Composio** [`@composio/cli@0.4.3-beta.408`](https://github.com/ComposioHQ/composio/releases/tag/@composio/cli@0.4.3-beta.408) — today *(pre-release)*
- **CrewAI** [`1.15.23`](https://github.com/crewAIInc/crewAI/releases/tag/1.15.23) — today
- **Claude Agent SDK** [`v2.1.284`](https://github.com/anthropics/claude-code/releases/tag/v2.1.284) — today
- **PydanticAI** [`v2.51.0`](https://github.com/pydantic/pydantic-ai/releases/tag/v2.51.0) — 3 days ago
- **Google ADK** [`v2.10.0`](https://github.com/google/adk-python/releases/tag/v2.10.0) — 3 days ago
- **Mastra** [`@mastra/core@1.71.0`](https://github.com/mastra-ai/mastra/releases/tag/@mastra/core@1.71.0) — 4 days ago
- **DSPy** [`3.4.0`](https://github.com/stanfordnlp/dspy/releases/tag/3.4.0) — 4 days ago
- **AG2** [`v1.1.0`](https://github.com/ag2ai/ag2/releases/tag/v1.1.0) — 4 days ago
- **Haystack** [`v3.2.0`](https://github.com/deepset-ai/haystack/releases/tag/v3.2.0) — 5 days ago
- **LangGraph** [`cli==0.4.32.dev0`](https://github.com/langchain-ai/langgraph/releases/tag/cli==0.4.32.dev0) — 5 days ago

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

*Powered by GitHub Actions • Data refreshed daily • Last run: 2026-09-29 12:29 UTC*