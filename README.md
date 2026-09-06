# 🔬 AI Agent Framework Pulse Tracker

[![Daily Update](https://github.com/PurpleHaze2320/ai-agent-pulse/actions/workflows/track.yml/badge.svg)](https://github.com/PurpleHaze2320/ai-agent-pulse/actions/workflows/track.yml)
[![Frameworks Tracked](https://img.shields.io/badge/frameworks-19-blue)](https://github.com/PurpleHaze2320/ai-agent-pulse)
[![License: MIT](https://img.shields.io/badge/License-MIT-green.svg)](https://opensource.org/licenses/MIT)
[![GitHub stars](https://img.shields.io/github/stars/PurpleHaze2320/ai-agent-pulse?style=social)](https://github.com/PurpleHaze2320/ai-agent-pulse/stargazers)

> Automated daily tracking of the AI agent framework ecosystem's health, momentum, and trends.
> Last updated: **2026-09-06 10:38 UTC** | Tracking **19** frameworks

## How It Works

This bot runs daily via GitHub Actions and collects metrics from the GitHub API for the most important
AI agent frameworks. It computes a **Pulse Score** (0-100) based on six weighted signals: star velocity,
release freshness, issue health, commit activity, community size, and fork engagement. The result is
a living dashboard that shows which frameworks are gaining momentum and which are losing steam.

## 🏆 Pulse Leaderboard

| Rank | Framework | Pulse | Stars | ⭐ 7d | Commits (4w) | Last Release | Category |
|------|-----------|-------|-------|-------|--------------|--------------|----------|
| 1 | [BrowserUse](https://github.com/browser-use/browser-use) | 🟢 **90.4** | 112.5k | 🚀 +780 | 179 | 2 days ago | `web-agent` |
| 2 | [CrewAI](https://github.com/crewAIInc/crewAI) | 🟢 **78.0** | 58.1k | 🚀 +321 | 76 | 1 day ago | `multi-agent` |
| 3 | [Mastra](https://github.com/mastra-ai/mastra) | 🟢 **76.0** | 27.7k | 🚀 +165 | 1147 | 1 day ago | `typescript` |
| 4 | [OpenAI Agents SDK](https://github.com/openai/openai-agents-python) | 🟢 **75.4** | 29.2k | 🚀 +149 | 122 | 17 days ago | `orchestration` |
| 5 | [PydanticAI](https://github.com/pydantic/pydantic-ai) | 🟢 **75.1** | 19.7k | 🚀 +162 | 219 | 1 day ago | `structured` |
| 6 | [Google ADK](https://github.com/google/adk-python) | 🟢 **73.6** | 21.4k | 📈 +94 | 339 | 9 days ago | `orchestration` |
| 7 | [Haystack](https://github.com/deepset-ai/haystack) | 🟢 **71.4** | 26.4k | 📈 +70 | 168 | 3 days ago | `pipeline` |
| 8 | [Claude Agent SDK](https://github.com/anthropics/claude-code) | 🟢 **70.1** | 144.2k | 🚀 +784 | 24 | today | `orchestration` |
| 9 | [LangGraph](https://github.com/langchain-ai/langgraph) | 🟡 **69.8** | 41.1k | 🚀 +420 | 28 | 9 days ago | `orchestration` |
| 10 | [Composio](https://github.com/ComposioHQ/composio) | 🟡 **68.9** | 30.1k | 🚀 +131 | 203 | 1 day ago | `tooling` |
| 11 | [Agno](https://github.com/agno-agi/agno) | 🟡 **66.2** | 42.1k | 📈 +99 | 76 | 1 day ago | `multi-agent` |
| 12 | [DSPy](https://github.com/stanfordnlp/dspy) | 🟡 **62.1** | 37.8k | 🚀 +142 | 51 | 15 days ago | `optimization` |
| 13 | [LlamaIndex](https://github.com/run-llama/llama_index) | 🟡 **61.9** | 52.0k | 🚀 +116 | 32 | 17 days ago | `data-agent` |
| 14 | [AG2](https://github.com/ag2ai/ag2) | 🟡 **55.9** | 4.9k | ↗️ +13 | 33 | 8 days ago | `multi-agent` |
| 15 | [Semantic Kernel](https://github.com/microsoft/semantic-kernel) | 🟡 **54.1** | 28.5k | ↗️ +19 | 19 | 2 days ago | `enterprise` |
| 16 | [Letta](https://github.com/letta-ai/letta) | 🟡 **41.1** | 24.6k | 🚀 +136 | 1 | 3 mo ago | `memory` |
| 17 | [Smolagents](https://github.com/huggingface/smolagents) | 🟠 **38.0** | 29.2k | 🚀 +139 | 2 | 3 mo ago | `lightweight` |
| 18 | [AutoGen](https://github.com/microsoft/autogen) | 🟠 **34.0** | 60.8k | 🚀 +134 | 0 | 11 mo ago | `multi-agent` |
| 19 | [Swarm](https://github.com/openai/swarm) | 🔴 **9.1** | 21.9k | ↗️ +13 | 0 | — | `experimental` |

## 📂 By Category

- `data-agent`: **LlamaIndex** (61.9)
- `enterprise`: **Semantic Kernel** (54.1)
- `experimental`: **Swarm** (9.1)
- `lightweight`: **Smolagents** (38.0)
- `memory`: **Letta** (41.1)
- `multi-agent`: **CrewAI** (78.0), **Agno** (66.2), **AG2** (55.9), **AutoGen** (34.0)
- `optimization`: **DSPy** (62.1)
- `orchestration`: **OpenAI Agents SDK** (75.4), **Google ADK** (73.6), **Claude Agent SDK** (70.1), **LangGraph** (69.8)
- `pipeline`: **Haystack** (71.4)
- `structured`: **PydanticAI** (75.1)
- `tooling`: **Composio** (68.9)
- `typescript`: **Mastra** (76.0)
- `web-agent`: **BrowserUse** (90.4)

## 🔍 Top 5 — Score Breakdown

| Framework | Star Velocity | Release Freshness | Issue Health | Commit Activity | Community | Fork Ratio |
|-----------|:---:|:---:|:---:|:---:|:---:|:---:|
| **BrowserUse** | 100 | 99.3 | 92.9 | 100 | 71.8 | 44.0 |
| **CrewAI** | 66.2 | 99.7 | 96.0 | 76.0 | 61.2 | 57.5 |
| **Mastra** | 34.0 | 99.7 | 95.4 | 100 | 93.2 | 39.5 |
| **OpenAI Agents SDK** | 32.2 | 94.3 | 98.5 | 100 | 73.6 | 63.9 |
| **PydanticAI** | 32.2 | 99.7 | 81.4 | 100 | 95.0 | 53.8 |

## 💡 Key Insights

- **Hottest framework**: BrowserUse with a Pulse Score of 90.4
- **Fastest growing**: Claude Agent SDK gained +784 stars this week
- **Most active development**: Mastra with 1147 commits in the last 4 weeks
- **Stale releases**: AutoGen, Swarm haven't released in a while

## 📦 Recent Releases

- **Claude Agent SDK** [`v2.1.263`](https://github.com/anthropics/claude-code/releases/tag/v2.1.263) — today
- **PydanticAI** [`v2.40.0`](https://github.com/pydantic/pydantic-ai/releases/tag/v2.40.0) — 1 day ago
- **Composio** [`versioning-example@0.1.2`](https://github.com/ComposioHQ/composio/releases/tag/versioning-example@0.1.2) — 1 day ago
- **Mastra** [`@mastra/core@1.64.0`](https://github.com/mastra-ai/mastra/releases/tag/@mastra/core@1.64.0) — 1 day ago
- **Agno** [`v3.0.6`](https://github.com/agno-agi/agno/releases/tag/v3.0.6) — 1 day ago
- **CrewAI** [`1.15.20`](https://github.com/crewAIInc/crewAI/releases/tag/1.15.20) — 1 day ago
- **BrowserUse** [`0.13.10`](https://github.com/browser-use/browser-use/releases/tag/0.13.10) — 2 days ago
- **Semantic Kernel** [`dotnet-1.80.1`](https://github.com/microsoft/semantic-kernel/releases/tag/dotnet-1.80.1) — 2 days ago
- **Haystack** [`v3.1.1`](https://github.com/deepset-ai/haystack/releases/tag/v3.1.1) — 3 days ago
- **AG2** [`v1.0.3`](https://github.com/ag2ai/ag2/releases/tag/v1.0.3) — 8 days ago

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

*Powered by GitHub Actions • Data refreshed daily • Last run: 2026-09-06 10:38 UTC*