# 🔬 AI Agent Framework Pulse Tracker

[![Daily Update](https://github.com/PurpleHaze2320/ai-agent-pulse/actions/workflows/track.yml/badge.svg)](https://github.com/PurpleHaze2320/ai-agent-pulse/actions/workflows/track.yml)
[![Frameworks Tracked](https://img.shields.io/badge/frameworks-19-blue)](https://github.com/PurpleHaze2320/ai-agent-pulse)
[![License: MIT](https://img.shields.io/badge/License-MIT-green.svg)](https://opensource.org/licenses/MIT)
[![GitHub stars](https://img.shields.io/github/stars/PurpleHaze2320/ai-agent-pulse?style=social)](https://github.com/PurpleHaze2320/ai-agent-pulse/stargazers)

> Automated daily tracking of the AI agent framework ecosystem's health, momentum, and trends.
> Last updated: **2026-09-05 10:18 UTC** | Tracking **19** frameworks

## How It Works

This bot runs daily via GitHub Actions and collects metrics from the GitHub API for the most important
AI agent frameworks. It computes a **Pulse Score** (0-100) based on six weighted signals: star velocity,
release freshness, issue health, commit activity, community size, and fork engagement. The result is
a living dashboard that shows which frameworks are gaining momentum and which are losing steam.

## 🏆 Pulse Leaderboard

| Rank | Framework | Pulse | Stars | ⭐ 7d | Commits (4w) | Last Release | Category |
|------|-----------|-------|-------|-------|--------------|--------------|----------|
| 1 | [BrowserUse](https://github.com/browser-use/browser-use) | 🟢 **90.5** | 112.3k | 🚀 +720 | 196 | 1 day ago | `web-agent` |
| 2 | [CrewAI](https://github.com/crewAIInc/crewAI) | 🟢 **82.0** | 58.1k | 🚀 +320 | 96 | today | `multi-agent` |
| 3 | [Mastra](https://github.com/mastra-ai/mastra) | 🟢 **76.0** | 27.7k | 🚀 +161 | 1503 | today | `typescript` |
| 4 | [OpenAI Agents SDK](https://github.com/openai/openai-agents-python) | 🟢 **75.6** | 29.2k | 🚀 +149 | 212 | 16 days ago | `orchestration` |
| 5 | [PydanticAI](https://github.com/pydantic/pydantic-ai) | 🟢 **75.2** | 19.7k | 🚀 +163 | 274 | today | `structured` |
| 6 | [Google ADK](https://github.com/google/adk-python) | 🟢 **73.7** | 21.4k | 📈 +94 | 475 | 8 days ago | `orchestration` |
| 7 | [Haystack](https://github.com/deepset-ai/haystack) | 🟢 **71.3** | 26.4k | 📈 +67 | 210 | 2 days ago | `pipeline` |
| 8 | [Claude Agent SDK](https://github.com/anthropics/claude-code) | 🟢 **71.0** | 144.1k | 🚀 +767 | 29 | today | `orchestration` |
| 9 | [LangGraph](https://github.com/langchain-ai/langgraph) | 🟢 **70.6** | 41.1k | 🚀 +427 | 30 | 8 days ago | `orchestration` |
| 10 | [Composio](https://github.com/ComposioHQ/composio) | 🟡 **69.0** | 30.1k | 🚀 +132 | 237 | today | `tooling` |
| 11 | [Agno](https://github.com/agno-agi/agno) | 🟡 **67.7** | 42.1k | 📈 +93 | 84 | today | `multi-agent` |
| 12 | [DSPy](https://github.com/stanfordnlp/dspy) | 🟡 **64.4** | 37.8k | 🚀 +137 | 63 | 14 days ago | `optimization` |
| 13 | [LlamaIndex](https://github.com/run-llama/llama_index) | 🟡 **64.0** | 52.0k | 🚀 +117 | 42 | 16 days ago | `data-agent` |
| 14 | [AG2](https://github.com/ag2ai/ag2) | 🟡 **60.1** | 4.9k | ↗️ +11 | 54 | 7 days ago | `multi-agent` |
| 15 | [Semantic Kernel](https://github.com/microsoft/semantic-kernel) | 🟡 **54.8** | 28.5k | ↗️ +19 | 22 | 1 day ago | `enterprise` |
| 16 | [Letta](https://github.com/letta-ai/letta) | 🟡 **41.6** | 24.6k | 🚀 +137 | 3 | 3 mo ago | `memory` |
| 17 | [Smolagents](https://github.com/huggingface/smolagents) | 🟠 **37.5** | 29.2k | 🚀 +124 | 2 | 3 mo ago | `lightweight` |
| 18 | [AutoGen](https://github.com/microsoft/autogen) | 🟠 **33.3** | 60.8k | 🚀 +116 | 0 | 11 mo ago | `multi-agent` |
| 19 | [Swarm](https://github.com/openai/swarm) | 🔴 **9.2** | 21.9k | ↗️ +13 | 0 | — | `experimental` |

## 📂 By Category

- `data-agent`: **LlamaIndex** (64.0)
- `enterprise`: **Semantic Kernel** (54.8)
- `experimental`: **Swarm** (9.2)
- `lightweight`: **Smolagents** (37.5)
- `memory`: **Letta** (41.6)
- `multi-agent`: **CrewAI** (82.0), **Agno** (67.7), **AG2** (60.1), **AutoGen** (33.3)
- `optimization`: **DSPy** (64.4)
- `orchestration`: **OpenAI Agents SDK** (75.6), **Google ADK** (73.7), **Claude Agent SDK** (71.0), **LangGraph** (70.6)
- `pipeline`: **Haystack** (71.3)
- `structured`: **PydanticAI** (75.2)
- `tooling`: **Composio** (69.0)
- `typescript`: **Mastra** (76.0)
- `web-agent`: **BrowserUse** (90.5)

## 🔍 Top 5 — Score Breakdown

| Framework | Star Velocity | Release Freshness | Issue Health | Commit Activity | Community | Fork Ratio |
|-----------|:---:|:---:|:---:|:---:|:---:|:---:|
| **BrowserUse** | 100 | 99.7 | 93.1 | 100 | 71.8 | 44.0 |
| **CrewAI** | 66.1 | 100.0 | 96.2 | 96.0 | 61.2 | 57.4 |
| **Mastra** | 33.8 | 100.0 | 95.2 | 100 | 93.2 | 39.5 |
| **OpenAI Agents SDK** | 32.5 | 94.7 | 98.5 | 100 | 73.6 | 63.9 |
| **PydanticAI** | 32.5 | 100.0 | 81.5 | 100 | 95.0 | 53.6 |

## 💡 Key Insights

- **Hottest framework**: BrowserUse with a Pulse Score of 90.5
- **Fastest growing**: Claude Agent SDK gained +767 stars this week
- **Most active development**: Mastra with 1503 commits in the last 4 weeks
- **Stale releases**: AutoGen, Swarm haven't released in a while

## 📦 Recent Releases

- **PydanticAI** [`v2.40.0`](https://github.com/pydantic/pydantic-ai/releases/tag/v2.40.0) — today
- **Claude Agent SDK** [`v2.1.261`](https://github.com/anthropics/claude-code/releases/tag/v2.1.261) — today
- **Composio** [`versioning-example@0.1.2`](https://github.com/ComposioHQ/composio/releases/tag/versioning-example@0.1.2) — today
- **Mastra** [`@mastra/core@1.64.0`](https://github.com/mastra-ai/mastra/releases/tag/@mastra/core@1.64.0) — today
- **Agno** [`v3.0.6`](https://github.com/agno-agi/agno/releases/tag/v3.0.6) — today
- **CrewAI** [`1.15.20`](https://github.com/crewAIInc/crewAI/releases/tag/1.15.20) — today
- **BrowserUse** [`0.13.10`](https://github.com/browser-use/browser-use/releases/tag/0.13.10) — 1 day ago
- **Semantic Kernel** [`dotnet-1.80.1`](https://github.com/microsoft/semantic-kernel/releases/tag/dotnet-1.80.1) — 1 day ago
- **Haystack** [`v3.1.1`](https://github.com/deepset-ai/haystack/releases/tag/v3.1.1) — 2 days ago
- **AG2** [`v1.0.3`](https://github.com/ag2ai/ag2/releases/tag/v1.0.3) — 7 days ago

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

*Powered by GitHub Actions • Data refreshed daily • Last run: 2026-09-05 10:18 UTC*