# 🔬 AI Agent Framework Pulse Tracker

[![Daily Update](https://github.com/PurpleHaze2320/ai-agent-pulse/actions/workflows/track.yml/badge.svg)](https://github.com/PurpleHaze2320/ai-agent-pulse/actions/workflows/track.yml)
[![Frameworks Tracked](https://img.shields.io/badge/frameworks-19-blue)](https://github.com/PurpleHaze2320/ai-agent-pulse)
[![License: MIT](https://img.shields.io/badge/License-MIT-green.svg)](https://opensource.org/licenses/MIT)
[![GitHub stars](https://img.shields.io/github/stars/PurpleHaze2320/ai-agent-pulse?style=social)](https://github.com/PurpleHaze2320/ai-agent-pulse/stargazers)

> Automated daily tracking of the AI agent framework ecosystem's health, momentum, and trends.
> Last updated: **2026-09-04 10:58 UTC** | Tracking **19** frameworks

## How It Works

This bot runs daily via GitHub Actions and collects metrics from the GitHub API for the most important
AI agent frameworks. It computes a **Pulse Score** (0-100) based on six weighted signals: star velocity,
release freshness, issue health, commit activity, community size, and fork engagement. The result is
a living dashboard that shows which frameworks are gaining momentum and which are losing steam.

## 🏆 Pulse Leaderboard

| Rank | Framework | Pulse | Stars | ⭐ 7d | Commits (4w) | Last Release | Category |
|------|-----------|-------|-------|-------|--------------|--------------|----------|
| 1 | [BrowserUse](https://github.com/browser-use/browser-use) | 🟢 **90.4** | 112.2k | 🚀 +670 | 170 | today | `web-agent` |
| 2 | [CrewAI](https://github.com/crewAIInc/crewAI) | 🟢 **80.3** | 58.1k | 🚀 +330 | 88 | 7 days ago | `multi-agent` |
| 3 | [OpenAI Agents SDK](https://github.com/openai/openai-agents-python) | 🟢 **75.7** | 29.2k | 🚀 +148 | 201 | 15 days ago | `orchestration` |
| 4 | [Mastra](https://github.com/mastra-ai/mastra) | 🟢 **75.1** | 27.7k | 🚀 +146 | 1457 | 6 days ago | `typescript` |
| 5 | [PydanticAI](https://github.com/pydantic/pydantic-ai) | 🟢 **75.0** | 19.7k | 🚀 +155 | 255 | today | `structured` |
| 6 | [Google ADK](https://github.com/google/adk-python) | 🟢 **73.5** | 21.4k | 📈 +88 | 469 | 7 days ago | `orchestration` |
| 7 | [Haystack](https://github.com/deepset-ai/haystack) | 🟢 **71.3** | 26.4k | 📈 +63 | 203 | 1 day ago | `pipeline` |
| 8 | [Claude Agent SDK](https://github.com/anthropics/claude-code) | 🟢 **70.8** | 144.0k | 🚀 +718 | 28 | today | `orchestration` |
| 9 | [LangGraph](https://github.com/langchain-ai/langgraph) | 🟢 **70.2** | 41.0k | 🚀 +408 | 30 | 7 days ago | `orchestration` |
| 10 | [Composio](https://github.com/ComposioHQ/composio) | 🟡 **68.5** | 30.0k | 🚀 +121 | 230 | 1 day ago | `tooling` |
| 11 | [Agno](https://github.com/agno-agi/agno) | 🟡 **67.0** | 42.0k | 📈 +89 | 82 | 3 days ago | `multi-agent` |
| 12 | [DSPy](https://github.com/stanfordnlp/dspy) | 🟡 **63.8** | 37.8k | 🚀 +128 | 61 | 13 days ago | `optimization` |
| 13 | [LlamaIndex](https://github.com/run-llama/llama_index) | 🟡 **63.7** | 52.0k | 🚀 +106 | 42 | 15 days ago | `data-agent` |
| 14 | [AG2](https://github.com/ag2ai/ag2) | 🟡 **60.1** | 4.9k | ↗️ +10 | 54 | 6 days ago | `multi-agent` |
| 15 | [Semantic Kernel](https://github.com/microsoft/semantic-kernel) | 🟡 **54.9** | 28.5k | ↗️ +19 | 22 | today | `enterprise` |
| 16 | [Letta](https://github.com/letta-ai/letta) | 🟡 **41.7** | 24.6k | 🚀 +136 | 3 | 3 mo ago | `memory` |
| 17 | [Smolagents](https://github.com/huggingface/smolagents) | 🟠 **37.4** | 29.1k | 🚀 +117 | 2 | 3 mo ago | `lightweight` |
| 18 | [AutoGen](https://github.com/microsoft/autogen) | 🟠 **33.7** | 60.8k | 🚀 +124 | 0 | 11 mo ago | `multi-agent` |
| 19 | [Swarm](https://github.com/openai/swarm) | 🔴 **9.2** | 21.9k | ↗️ +12 | 0 | — | `experimental` |

## 📂 By Category

- `data-agent`: **LlamaIndex** (63.7)
- `enterprise`: **Semantic Kernel** (54.9)
- `experimental`: **Swarm** (9.2)
- `lightweight`: **Smolagents** (37.4)
- `memory`: **Letta** (41.7)
- `multi-agent`: **CrewAI** (80.3), **Agno** (67.0), **AG2** (60.1), **AutoGen** (33.7)
- `optimization`: **DSPy** (63.8)
- `orchestration`: **OpenAI Agents SDK** (75.7), **Google ADK** (73.5), **Claude Agent SDK** (70.8), **LangGraph** (70.2)
- `pipeline`: **Haystack** (71.3)
- `structured`: **PydanticAI** (75.0)
- `tooling`: **Composio** (68.5)
- `typescript`: **Mastra** (75.1)
- `web-agent`: **BrowserUse** (90.4)

## 🔍 Top 5 — Score Breakdown

| Framework | Star Velocity | Release Freshness | Issue Health | Commit Activity | Community | Fork Ratio |
|-----------|:---:|:---:|:---:|:---:|:---:|:---:|
| **BrowserUse** | 100 | 100.0 | 92.7 | 100 | 71.0 | 44.0 |
| **CrewAI** | 67.7 | 97.7 | 96.3 | 88.0 | 61.0 | 57.4 |
| **OpenAI Agents SDK** | 32.6 | 95.0 | 98.3 | 100 | 73.6 | 63.8 |
| **Mastra** | 31.8 | 98.0 | 95.1 | 100 | 93.2 | 39.4 |
| **PydanticAI** | 31.5 | 100.0 | 81.7 | 100 | 95.0 | 53.5 |

## 💡 Key Insights

- **Hottest framework**: BrowserUse with a Pulse Score of 90.4
- **Fastest growing**: Claude Agent SDK gained +718 stars this week
- **Most active development**: Mastra with 1457 commits in the last 4 weeks
- **Stale releases**: AutoGen, Swarm haven't released in a while

## 📦 Recent Releases

- **PydanticAI** [`v2.39.0`](https://github.com/pydantic/pydantic-ai/releases/tag/v2.39.0) — today
- **BrowserUse** [`0.13.10`](https://github.com/browser-use/browser-use/releases/tag/0.13.10) — today
- **Claude Agent SDK** [`v2.1.260`](https://github.com/anthropics/claude-code/releases/tag/v2.1.260) — today
- **Semantic Kernel** [`dotnet-1.80.1`](https://github.com/microsoft/semantic-kernel/releases/tag/dotnet-1.80.1) — today
- **Haystack** [`v3.1.1`](https://github.com/deepset-ai/haystack/releases/tag/v3.1.1) — 1 day ago
- **Composio** [`@composio/cli@0.4.1-beta.374`](https://github.com/ComposioHQ/composio/releases/tag/@composio/cli@0.4.1-beta.374) — 1 day ago *(pre-release)*
- **Agno** [`v3.0.5`](https://github.com/agno-agi/agno/releases/tag/v3.0.5) — 3 days ago
- **AG2** [`v1.0.3`](https://github.com/ag2ai/ag2/releases/tag/v1.0.3) — 6 days ago
- **Mastra** [`@mastra/core@1.63.0`](https://github.com/mastra-ai/mastra/releases/tag/@mastra/core@1.63.0) — 6 days ago
- **Google ADK** [`v1.39.1`](https://github.com/google/adk-python/releases/tag/v1.39.1) — 7 days ago

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

*Powered by GitHub Actions • Data refreshed daily • Last run: 2026-09-04 10:58 UTC*