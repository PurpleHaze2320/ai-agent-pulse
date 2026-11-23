# 🔬 AI Agent Framework Pulse Tracker

[![Daily Update](https://github.com/PurpleHaze2320/ai-agent-pulse/actions/workflows/track.yml/badge.svg)](https://github.com/PurpleHaze2320/ai-agent-pulse/actions/workflows/track.yml)
[![Frameworks Tracked](https://img.shields.io/badge/frameworks-19-blue)](https://github.com/PurpleHaze2320/ai-agent-pulse)
[![License: MIT](https://img.shields.io/badge/License-MIT-green.svg)](https://opensource.org/licenses/MIT)
[![GitHub stars](https://img.shields.io/github/stars/PurpleHaze2320/ai-agent-pulse?style=social)](https://github.com/PurpleHaze2320/ai-agent-pulse/stargazers)

> Automated daily tracking of the AI agent framework ecosystem's health, momentum, and trends.
> Last updated: **2026-11-23 17:46 UTC** | Tracking **19** frameworks

## How It Works

This bot runs daily via GitHub Actions and collects metrics from the GitHub API for the most important
AI agent frameworks. It computes a **Pulse Score** (0-100) based on six weighted signals: star velocity,
release freshness, issue health, commit activity, community size, and fork engagement. The result is
a living dashboard that shows which frameworks are gaining momentum and which are losing steam.

## 🏆 Pulse Leaderboard

| Rank | Framework | Pulse | Stars | ⭐ 7d | Commits (4w) | Last Release | Category |
|------|-----------|-------|-------|-------|--------------|--------------|----------|
| 1 | [BrowserUse](https://github.com/browser-use/browser-use) | 🟢 **90.1** | 121.8k | 🚀 +649 | 1195 | 1 day ago | `web-agent` |
| 2 | [Claude Agent SDK](https://github.com/anthropics/claude-code) | 🟢 **85.3** | 156.8k | 🚀 +924 | 152 | 2 days ago | `orchestration` |
| 3 | [CrewAI](https://github.com/crewAIInc/crewAI) | 🟢 **78.1** | 61.2k | 🚀 +213 | 153 | 3 days ago | `multi-agent` |
| 4 | [Mastra](https://github.com/mastra-ai/mastra) | 🟢 **77.5** | 29.8k | 🚀 +219 | 1912 | 5 days ago | `typescript` |
| 5 | [Google ADK](https://github.com/google/adk-python) | 🟢 **74.4** | 22.3k | 📈 +84 | 247 | 3 days ago | `orchestration` |
| 6 | [LangGraph](https://github.com/langchain-ai/langgraph) | 🟢 **74.2** | 45.3k | 🚀 +283 | 71 | 3 days ago | `orchestration` |
| 7 | [Haystack](https://github.com/deepset-ai/haystack) | 🟢 **71.3** | 27.1k | 📈 +65 | 231 | 13 days ago | `pipeline` |
| 8 | [AG2](https://github.com/ag2ai/ag2) | 🟢 **70.2** | 5.1k | ↗️ +12 | 103 | today | `multi-agent` |
| 9 | [Composio](https://github.com/ComposioHQ/composio) | 🟢 **70.0** | 31.3k | 🚀 +158 | 253 | today | `tooling` |
| 10 | [PydanticAI](https://github.com/pydantic/pydantic-ai) | 🟡 **69.5** | 21.4k | 🚀 +112 | 846 | 1 mo ago | `structured` |
| 11 | [OpenAI Agents SDK](https://github.com/openai/openai-agents-python) | 🟡 **68.7** | 30.8k | 🚀 +127 | 65 | 2 days ago | `orchestration` |
| 12 | [Agno](https://github.com/agno-agi/agno) | 🟡 **67.3** | 43.3k | 📈 +61 | 94 | 6 days ago | `multi-agent` |
| 13 | [DSPy](https://github.com/stanfordnlp/dspy) | 🟡 **59.6** | 39.2k | 🚀 +104 | 57 | 13 days ago | `optimization` |
| 14 | [Semantic Kernel](https://github.com/microsoft/semantic-kernel) | 🟡 **57.6** | 28.8k | ↗️ +14 | 37 | 16 days ago | `enterprise` |
| 15 | [LlamaIndex](https://github.com/run-llama/llama_index) | 🟡 **54.8** | 53.0k | 📈 +65 | 8 | 9 days ago | `data-agent` |
| 16 | [Smolagents](https://github.com/huggingface/smolagents) | 🟠 **34.2** | 30.5k | 🚀 +110 | 18 | 5 mo ago | `lightweight` |
| 17 | [AutoGen](https://github.com/microsoft/autogen) | 🟠 **32.2** | 62.0k | 📈 +93 | 1 | 1y ago | `multi-agent` |
| 18 | [Letta](https://github.com/letta-ai/letta) | 🟠 **32.2** | 25.5k | 📈 +58 | 0 | 6 mo ago | `memory` |
| 19 | [Swarm](https://github.com/openai/swarm) | 🔴 **9.1** | 22.2k | ↗️ +12 | 0 | — | `experimental` |

## 📂 By Category

- `data-agent`: **LlamaIndex** (54.8)
- `enterprise`: **Semantic Kernel** (57.6)
- `experimental`: **Swarm** (9.1)
- `lightweight`: **Smolagents** (34.2)
- `memory`: **Letta** (32.2)
- `multi-agent`: **CrewAI** (78.1), **AG2** (70.2), **Agno** (67.3), **AutoGen** (32.2)
- `optimization`: **DSPy** (59.6)
- `orchestration`: **Claude Agent SDK** (85.3), **Google ADK** (74.4), **LangGraph** (74.2), **OpenAI Agents SDK** (68.7)
- `pipeline`: **Haystack** (71.3)
- `structured`: **PydanticAI** (69.5)
- `tooling`: **Composio** (70.0)
- `typescript`: **Mastra** (77.5)
- `web-agent`: **BrowserUse** (90.1)

## 🔍 Top 5 — Score Breakdown

| Framework | Star Velocity | Release Freshness | Issue Health | Commit Activity | Community | Fork Ratio |
|-----------|:---:|:---:|:---:|:---:|:---:|:---:|
| **BrowserUse** | 100 | 99.7 | 89.9 | 100 | 72.2 | 44.7 |
| **Claude Agent SDK** | 100 | 99.3 | 85.8 | 100 | 11.2 | 64.1 |
| **CrewAI** | 47.1 | 99.0 | 84.9 | 100 | 77.8 | 60.5 |
| **Mastra** | 41.4 | 98.3 | 93.3 | 100 | 93.2 | 42.1 |
| **Google ADK** | 16.9 | 99.0 | 92.5 | 100 | 86.0 | 79.3 |

## 💡 Key Insights

- **Hottest framework**: BrowserUse with a Pulse Score of 90.1
- **Fastest growing**: Claude Agent SDK gained +924 stars this week
- **Most active development**: Mastra with 1912 commits in the last 4 weeks
- **⚠️ Archived**: AutoGen
- **Stale releases**: AutoGen, Swarm haven't released in a while

## 📦 Recent Releases

- **Composio** [`@composio/cli@0.6.4-beta.579`](https://github.com/ComposioHQ/composio/releases/tag/@composio/cli@0.6.4-beta.579) — today *(pre-release)*
- **AG2** [`v1.3.4`](https://github.com/ag2ai/ag2/releases/tag/v1.3.4) — today
- **BrowserUse** [`1.0.8`](https://github.com/browser-use/browser-use/releases/tag/1.0.8) — 1 day ago
- **Claude Agent SDK** [`v2.1.330`](https://github.com/anthropics/claude-code/releases/tag/v2.1.330) — 2 days ago
- **OpenAI Agents SDK** [`v1.0.0-alpha.1`](https://github.com/openai/openai-agents-python/releases/tag/v1.0.0-alpha.1) — 2 days ago *(pre-release)*
- **LangGraph** [`1.2.24`](https://github.com/langchain-ai/langgraph/releases/tag/1.2.24) — 3 days ago
- **Google ADK** [`v2.15.0`](https://github.com/google/adk-python/releases/tag/v2.15.0) — 3 days ago
- **CrewAI** [`1.15.44`](https://github.com/crewAIInc/crewAI/releases/tag/1.15.44) — 3 days ago
- **Mastra** [`@mastra/core@1.84.0`](https://github.com/mastra-ai/mastra/releases/tag/@mastra/core@1.84.0) — 5 days ago
- **Agno** [`v3.2.1`](https://github.com/agno-agi/agno/releases/tag/v3.2.1) — 6 days ago

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

*Powered by GitHub Actions • Data refreshed daily • Last run: 2026-11-23 17:46 UTC*