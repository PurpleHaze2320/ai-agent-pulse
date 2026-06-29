# 🔬 AI Agent Framework Pulse Tracker

[![Daily Update](https://github.com/PurpleHaze2320/ai-agent-pulse/actions/workflows/track.yml/badge.svg)](https://github.com/PurpleHaze2320/ai-agent-pulse/actions/workflows/track.yml)
[![Frameworks Tracked](https://img.shields.io/badge/frameworks-19-blue)](https://github.com/PurpleHaze2320/ai-agent-pulse)
[![License: MIT](https://img.shields.io/badge/License-MIT-green.svg)](https://opensource.org/licenses/MIT)
[![GitHub stars](https://img.shields.io/github/stars/PurpleHaze2320/ai-agent-pulse?style=social)](https://github.com/PurpleHaze2320/ai-agent-pulse/stargazers)

> Automated daily tracking of the AI agent framework ecosystem's health, momentum, and trends.
> Last updated: **2026-06-29 11:10 UTC** | Tracking **19** frameworks

## How It Works

This bot runs daily via GitHub Actions and collects metrics from the GitHub API for the most important
AI agent frameworks. It computes a **Pulse Score** (0-100) based on six weighted signals: star velocity,
release freshness, issue health, commit activity, community size, and fork engagement. The result is
a living dashboard that shows which frameworks are gaining momentum and which are losing steam.

## 🏆 Pulse Leaderboard

| Rank | Framework | Pulse | Stars | ⭐ 7d | Commits (4w) | Last Release | Category |
|------|-----------|-------|-------|-------|--------------|--------------|----------|
| 1 | [CrewAI](https://github.com/crewAIInc/crewAI) | 🟢 **88.4** | 54.5k | 🚀 +421 | 109 | 2 days ago | `multi-agent` |
| 2 | [Mastra](https://github.com/mastra-ai/mastra) | 🟢 **78.9** | 25.6k | 🚀 +235 | 769 | 4 days ago | `typescript` |
| 3 | [BrowserUse](https://github.com/browser-use/browser-use) | 🟢 **77.2** | 101.3k | 🚀 +1241 | 41 | 16 days ago | `web-agent` |
| 4 | [LangGraph](https://github.com/langchain-ai/langgraph) | 🟢 **75.8** | 36.0k | 🚀 +584 | 41 | 10 days ago | `orchestration` |
| 5 | [PydanticAI](https://github.com/pydantic/pydantic-ai) | 🟢 **72.5** | 18.1k | 🚀 +157 | 88 | today | `structured` |
| 6 | [Haystack](https://github.com/deepset-ai/haystack) | 🟢 **72.4** | 25.8k | 🚀 +145 | 153 | 11 days ago | `pipeline` |
| 7 | [Google ADK](https://github.com/google/adk-python) | 🟢 **71.3** | 20.3k | 🚀 +105 | 285 | 10 days ago | `orchestration` |
| 8 | [Claude Agent SDK](https://github.com/anthropics/claude-code) | 🟢 **70.2** | 134.9k | 🚀 +1179 | 23 | 2 days ago | `orchestration` |
| 9 | [OpenAI Agents SDK](https://github.com/openai/openai-agents-python) | 🟡 **64.3** | 27.5k | 🚀 +172 | 46 | 5 days ago | `orchestration` |
| 10 | [LlamaIndex](https://github.com/run-llama/llama_index) | 🟡 **62.5** | 50.5k | 🚀 +215 | 12 | 4 days ago | `data-agent` |
| 11 | [AG2](https://github.com/ag2ai/ag2) | 🟡 **60.4** | 4.7k | ↗️ +20 | 52 | 3 days ago | `multi-agent` |
| 12 | [DSPy](https://github.com/stanfordnlp/dspy) | 🟡 **58.7** | 35.6k | 🚀 +327 | 12 | 1 mo ago | `optimization` |
| 13 | [Semantic Kernel](https://github.com/microsoft/semantic-kernel) | 🟡 **56.7** | 28.2k | 📈 +39 | 31 | 12 days ago | `enterprise` |
| 14 | [Agno](https://github.com/agno-agi/agno) | 🟡 **51.1** | 40.9k | 📈 +92 | 0 | 5 days ago | `multi-agent` |
| 15 | [Composio](https://github.com/ComposioHQ/composio) | 🟡 **47.4** | 29.0k | 🚀 +109 | 0 | 2 days ago | `tooling` |
| 16 | [Letta](https://github.com/letta-ai/letta) | 🟡 **44.8** | 23.6k | 🚀 +115 | 1 | 1 mo ago | `memory` |
| 17 | [Smolagents](https://github.com/huggingface/smolagents) | 🟡 **42.2** | 28.1k | 🚀 +124 | 1 | 1 mo ago | `lightweight` |
| 18 | [AutoGen](https://github.com/microsoft/autogen) | 🟠 **39.5** | 59.3k | 🚀 +209 | 0 | 9 mo ago | `multi-agent` |
| 19 | [Swarm](https://github.com/openai/swarm) | 🔴 **11.2** | 21.7k | 📈 +89 | 0 | — | `experimental` |

## 📂 By Category

- `data-agent`: **LlamaIndex** (62.5)
- `enterprise`: **Semantic Kernel** (56.7)
- `experimental`: **Swarm** (11.2)
- `lightweight`: **Smolagents** (42.2)
- `memory`: **Letta** (44.8)
- `multi-agent`: **CrewAI** (88.4), **AG2** (60.4), **Agno** (51.1), **AutoGen** (39.5)
- `optimization`: **DSPy** (58.7)
- `orchestration`: **LangGraph** (75.8), **Google ADK** (71.3), **Claude Agent SDK** (70.2), **OpenAI Agents SDK** (64.3)
- `pipeline`: **Haystack** (72.4)
- `structured`: **PydanticAI** (72.5)
- `tooling`: **Composio** (47.4)
- `typescript`: **Mastra** (78.9)
- `web-agent`: **BrowserUse** (77.2)

## 🔍 Top 5 — Score Breakdown

| Framework | Star Velocity | Release Freshness | Issue Health | Commit Activity | Community | Fork Ratio |
|-----------|:---:|:---:|:---:|:---:|:---:|:---:|
| **CrewAI** | 90.2 | 99.3 | 96.0 | 100 | 59.6 | 56.0 |
| **Mastra** | 48.1 | 98.7 | 95.5 | 100 | 92.2 | 36.2 |
| **BrowserUse** | 100 | 94.7 | 95.4 | 41.0 | 63.0 | 44.4 |
| **LangGraph** | 100 | 96.7 | 74.0 | 41.0 | 55.0 | 67.0 |
| **PydanticAI** | 32.1 | 100.0 | 82.1 | 88.0 | 95.4 | 50.3 |

## 💡 Key Insights

- **Hottest framework**: CrewAI with a Pulse Score of 88.4
- **Fastest growing**: BrowserUse gained +1241 stars this week
- **Most active development**: Mastra with 769 commits in the last 4 weeks
- **Stale releases**: AutoGen, Swarm haven't released in a while

## 📦 Recent Releases

- **PydanticAI** [`v2.1.0`](https://github.com/pydantic/pydantic-ai/releases/tag/v2.1.0) — today
- **Composio** [`@composio/slim@0.13.1`](https://github.com/ComposioHQ/composio/releases/tag/@composio/slim@0.13.1) — 2 days ago
- **CrewAI** [`1.15.1`](https://github.com/crewAIInc/crewAI/releases/tag/1.15.1) — 2 days ago
- **Claude Agent SDK** [`v2.1.195`](https://github.com/anthropics/claude-code/releases/tag/v2.1.195) — 2 days ago
- **AG2** [`v0.14.0`](https://github.com/ag2ai/ag2/releases/tag/v0.14.0) — 3 days ago
- **LlamaIndex** [`v0.14.23`](https://github.com/run-llama/llama_index/releases/tag/v0.14.23) — 4 days ago
- **Mastra** [`@mastra/core@1.46.0`](https://github.com/mastra-ai/mastra/releases/tag/@mastra/core@1.46.0) — 4 days ago
- **OpenAI Agents SDK** [`v0.17.7`](https://github.com/openai/openai-agents-python/releases/tag/v0.17.7) — 5 days ago
- **Agno** [`v2.6.19`](https://github.com/agno-agi/agno/releases/tag/v2.6.19) — 5 days ago
- **LangGraph** [`1.2.6`](https://github.com/langchain-ai/langgraph/releases/tag/1.2.6) — 10 days ago

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

*Powered by GitHub Actions • Data refreshed daily • Last run: 2026-06-29 11:10 UTC*