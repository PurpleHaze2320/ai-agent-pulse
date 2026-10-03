# 🔬 AI Agent Framework Pulse Tracker

[![Daily Update](https://github.com/PurpleHaze2320/ai-agent-pulse/actions/workflows/track.yml/badge.svg)](https://github.com/PurpleHaze2320/ai-agent-pulse/actions/workflows/track.yml)
[![Frameworks Tracked](https://img.shields.io/badge/frameworks-19-blue)](https://github.com/PurpleHaze2320/ai-agent-pulse)
[![License: MIT](https://img.shields.io/badge/License-MIT-green.svg)](https://opensource.org/licenses/MIT)
[![GitHub stars](https://img.shields.io/github/stars/PurpleHaze2320/ai-agent-pulse?style=social)](https://github.com/PurpleHaze2320/ai-agent-pulse/stargazers)

> Automated daily tracking of the AI agent framework ecosystem's health, momentum, and trends.
> Last updated: **2026-10-03 11:22 UTC** | Tracking **19** frameworks

## How It Works

This bot runs daily via GitHub Actions and collects metrics from the GitHub API for the most important
AI agent frameworks. It computes a **Pulse Score** (0-100) based on six weighted signals: star velocity,
release freshness, issue health, commit activity, community size, and fork engagement. The result is
a living dashboard that shows which frameworks are gaining momentum and which are losing steam.

## 🏆 Pulse Leaderboard

| Rank | Framework | Pulse | Stars | ⭐ 7d | Commits (4w) | Last Release | Category |
|------|-----------|-------|-------|-------|--------------|--------------|----------|
| 1 | [Claude Agent SDK](https://github.com/anthropics/claude-code) | 🟢 **85.8** | 149.0k | 🚀 +875 | 141 | today | `orchestration` |
| 2 | [BrowserUse](https://github.com/browser-use/browser-use) | 🟢 **84.0** | 117.0k | 🚀 +686 | 79 | 29 days ago | `web-agent` |
| 3 | [CrewAI](https://github.com/crewAIInc/crewAI) | 🟢 **79.6** | 59.3k | 🚀 +260 | 99 | 4 days ago | `multi-agent` |
| 4 | [Mastra](https://github.com/mastra-ai/mastra) | 🟢 **77.2** | 28.5k | 🚀 +184 | 2191 | 3 days ago | `typescript` |
| 5 | [OpenAI Agents SDK](https://github.com/openai/openai-agents-python) | 🟢 **76.0** | 29.8k | 🚀 +118 | 243 | today | `orchestration` |
| 6 | [PydanticAI](https://github.com/pydantic/pydantic-ai) | 🟢 **75.5** | 20.4k | 🚀 +191 | 715 | today | `structured` |
| 7 | [Agno](https://github.com/agno-agi/agno) | 🟢 **73.5** | 42.5k | 🚀 +177 | 113 | today | `multi-agent` |
| 8 | [Google ADK](https://github.com/google/adk-python) | 🟢 **72.6** | 21.7k | 📈 +47 | 444 | 1 day ago | `orchestration` |
| 9 | [LangGraph](https://github.com/langchain-ai/langgraph) | 🟢 **71.0** | 42.7k | 🚀 +350 | 55 | 9 days ago | `orchestration` |
| 10 | [Haystack](https://github.com/deepset-ai/haystack) | 🟢 **70.6** | 26.6k | 📈 +39 | 239 | 2 days ago | `pipeline` |
| 11 | [AG2](https://github.com/ag2ai/ag2) | 🟡 **68.4** | 5.0k | ↗️ +12 | 93 | today | `multi-agent` |
| 12 | [Composio](https://github.com/ComposioHQ/composio) | 🟡 **67.2** | 30.4k | 📈 +87 | 333 | 1 day ago | `tooling` |
| 13 | [DSPy](https://github.com/stanfordnlp/dspy) | 🟡 **62.7** | 38.5k | 🚀 +162 | 56 | 8 days ago | `optimization` |
| 14 | [LlamaIndex](https://github.com/run-llama/llama_index) | 🟡 **58.6** | 52.4k | 📈 +72 | 25 | 11 days ago | `data-agent` |
| 15 | [Semantic Kernel](https://github.com/microsoft/semantic-kernel) | 🟡 **50.8** | 28.6k | ↗️ +12 | 13 | 29 days ago | `enterprise` |
| 16 | [Letta](https://github.com/letta-ai/letta) | 🟠 **38.8** | 25.0k | 🚀 +120 | 2 | 4 mo ago | `memory` |
| 17 | [Smolagents](https://github.com/huggingface/smolagents) | 🟠 **37.3** | 29.7k | 🚀 +162 | 4 | 4 mo ago | `lightweight` |
| 18 | [AutoGen](https://github.com/microsoft/autogen) | 🟠 **31.6** | 61.2k | 📈 +76 | 0 | 1y ago | `multi-agent` |
| 19 | [Swarm](https://github.com/openai/swarm) | 🔴 **9.7** | 22.0k | 📈 +24 | 0 | — | `experimental` |

## 📂 By Category

- `data-agent`: **LlamaIndex** (58.6)
- `enterprise`: **Semantic Kernel** (50.8)
- `experimental`: **Swarm** (9.7)
- `lightweight`: **Smolagents** (37.3)
- `memory`: **Letta** (38.8)
- `multi-agent`: **CrewAI** (79.6), **Agno** (73.5), **AG2** (68.4), **AutoGen** (31.6)
- `optimization`: **DSPy** (62.7)
- `orchestration`: **Claude Agent SDK** (85.8), **OpenAI Agents SDK** (76.0), **Google ADK** (72.6), **LangGraph** (71.0)
- `pipeline`: **Haystack** (70.6)
- `structured`: **PydanticAI** (75.5)
- `tooling`: **Composio** (67.2)
- `typescript`: **Mastra** (77.2)
- `web-agent`: **BrowserUse** (84.0)

## 🔍 Top 5 — Score Breakdown

| Framework | Star Velocity | Release Freshness | Issue Health | Commit Activity | Community | Fork Ratio |
|-----------|:---:|:---:|:---:|:---:|:---:|:---:|
| **Claude Agent SDK** | 100 | 100.0 | 86.1 | 100 | 11.4 | 67.9 |
| **BrowserUse** | 100 | 90.3 | 90.2 | 79.0 | 72.0 | 44.1 |
| **CrewAI** | 55.5 | 98.7 | 91.3 | 99.0 | 67.2 | 58.2 |
| **Mastra** | 38.7 | 99.0 | 95.5 | 100 | 93.6 | 40.8 |
| **OpenAI Agents SDK** | 26.3 | 100.0 | 99.7 | 100 | 79.4 | 64.9 |

## 💡 Key Insights

- **Hottest framework**: Claude Agent SDK with a Pulse Score of 85.8
- **Fastest growing**: Claude Agent SDK gained +875 stars this week
- **Most active development**: Mastra with 2191 commits in the last 4 weeks
- **Stale releases**: AutoGen, Swarm haven't released in a while

## 📦 Recent Releases

- **AG2** [`v1.1.2`](https://github.com/ag2ai/ag2/releases/tag/v1.1.2) — today
- **PydanticAI** [`v2.54.0`](https://github.com/pydantic/pydantic-ai/releases/tag/v2.54.0) — today
- **Claude Agent SDK** [`v2.1.288`](https://github.com/anthropics/claude-code/releases/tag/v2.1.288) — today
- **OpenAI Agents SDK** [`v0.23.1`](https://github.com/openai/openai-agents-python/releases/tag/v0.23.1) — today
- **Agno** [`v3.1.1`](https://github.com/agno-agi/agno/releases/tag/v3.1.1) — today
- **Google ADK** [`v2.11.0`](https://github.com/google/adk-python/releases/tag/v2.11.0) — 1 day ago
- **Composio** [`@composio/cli@0.4.3-beta.411`](https://github.com/ComposioHQ/composio/releases/tag/@composio/cli@0.4.3-beta.411) — 1 day ago *(pre-release)*
- **Haystack** [`v3.3.0`](https://github.com/deepset-ai/haystack/releases/tag/v3.3.0) — 2 days ago
- **Mastra** [`@mastra/core@1.72.0`](https://github.com/mastra-ai/mastra/releases/tag/@mastra/core@1.72.0) — 3 days ago
- **CrewAI** [`1.15.23`](https://github.com/crewAIInc/crewAI/releases/tag/1.15.23) — 4 days ago

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

*Powered by GitHub Actions • Data refreshed daily • Last run: 2026-10-03 11:22 UTC*