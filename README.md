# 🔬 AI Agent Framework Pulse Tracker

[![Daily Update](https://github.com/PurpleHaze2320/ai-agent-pulse/actions/workflows/track.yml/badge.svg)](https://github.com/PurpleHaze2320/ai-agent-pulse/actions/workflows/track.yml)
[![Frameworks Tracked](https://img.shields.io/badge/frameworks-19-blue)](https://github.com/PurpleHaze2320/ai-agent-pulse)
[![License: MIT](https://img.shields.io/badge/License-MIT-green.svg)](https://opensource.org/licenses/MIT)
[![GitHub stars](https://img.shields.io/github/stars/PurpleHaze2320/ai-agent-pulse?style=social)](https://github.com/PurpleHaze2320/ai-agent-pulse/stargazers)

> Automated daily tracking of the AI agent framework ecosystem's health, momentum, and trends.
> Last updated: **2026-08-20 06:53 UTC** | Tracking **19** frameworks

## How It Works

This bot runs daily via GitHub Actions and collects metrics from the GitHub API for the most important
AI agent frameworks. It computes a **Pulse Score** (0-100) based on six weighted signals: star velocity,
release freshness, issue health, commit activity, community size, and fork engagement. The result is
a living dashboard that shows which frameworks are gaining momentum and which are losing steam.

## 🏆 Pulse Leaderboard

| Rank | Framework | Pulse | Stars | ⭐ 7d | Commits (4w) | Last Release | Category |
|------|-----------|-------|-------|-------|--------------|--------------|----------|
| 1 | [BrowserUse](https://github.com/browser-use/browser-use) | 🟢 **89.9** | 109.8k | 🚀 +782 | 118 | 3 days ago | `web-agent` |
| 2 | [CrewAI](https://github.com/crewAIInc/crewAI) | 🟢 **82.5** | 57.4k | 🚀 +344 | 95 | today | `multi-agent` |
| 3 | [OpenAI Agents SDK](https://github.com/openai/openai-agents-python) | 🟢 **77.4** | 28.8k | 🚀 +181 | 361 | today | `orchestration` |
| 4 | [Mastra](https://github.com/mastra-ai/mastra) | 🟢 **76.7** | 27.3k | 🚀 +161 | 1517 | today | `typescript` |
| 5 | [LangGraph](https://github.com/langchain-ai/langgraph) | 🟢 **74.5** | 40.1k | 🚀 +481 | 34 | today | `orchestration` |
| 6 | [Haystack](https://github.com/deepset-ai/haystack) | 🟢 **71.0** | 26.3k | 📈 +66 | 183 | 1 day ago | `pipeline` |
| 7 | [Composio](https://github.com/ComposioHQ/composio) | 🟡 **68.3** | 29.8k | 🚀 +120 | 299 | 1 day ago | `tooling` |
| 8 | [Claude Agent SDK](https://github.com/anthropics/claude-code) | 🟡 **68.2** | 142.1k | 🚀 +779 | 16 | today | `orchestration` |
| 9 | [DSPy](https://github.com/stanfordnlp/dspy) | 🟡 **66.4** | 37.4k | 🚀 +283 | 47 | 16 days ago | `optimization` |
| 10 | [LlamaIndex](https://github.com/run-llama/llama_index) | 🟡 **63.3** | 51.8k | 🚀 +140 | 26 | today | `data-agent` |
| 11 | [AG2](https://github.com/ag2ai/ag2) | 🟡 **62.9** | 4.9k | 📈 +23 | 65 | 5 days ago | `multi-agent` |
| 12 | [Agno](https://github.com/agno-agi/agno) | 🟡 **60.0** | 41.8k | 🚀 +110 | 44 | 6 days ago | `multi-agent` |
| 13 | [PydanticAI](https://github.com/pydantic/pydantic-ai) | 🟡 **55.0** | 19.4k | 🚀 +146 | 0 | today | `structured` |
| 14 | [Google ADK](https://github.com/google/adk-python) | 🟡 **54.3** | 21.2k | 🚀 +108 | 0 | 2 days ago | `orchestration` |
| 15 | [Semantic Kernel](https://github.com/microsoft/semantic-kernel) | 🟡 **54.2** | 28.5k | 📈 +22 | 18 | 1 day ago | `enterprise` |
| 16 | [Letta](https://github.com/letta-ai/letta) | 🟡 **40.7** | 24.3k | 📈 +85 | 4 | 3 mo ago | `memory` |
| 17 | [Smolagents](https://github.com/huggingface/smolagents) | 🟠 **37.6** | 28.9k | 🚀 +105 | 0 | 2 mo ago | `lightweight` |
| 18 | [AutoGen](https://github.com/microsoft/autogen) | 🟠 **34.6** | 60.5k | 🚀 +141 | 0 | 10 mo ago | `multi-agent` |
| 19 | [Swarm](https://github.com/openai/swarm) | 🔴 **9.1** | 21.9k | ↗️ +7 | 0 | — | `experimental` |

## 📂 By Category

- `data-agent`: **LlamaIndex** (63.3)
- `enterprise`: **Semantic Kernel** (54.2)
- `experimental`: **Swarm** (9.1)
- `lightweight`: **Smolagents** (37.6)
- `memory`: **Letta** (40.7)
- `multi-agent`: **CrewAI** (82.5), **AG2** (62.9), **Agno** (60.0), **AutoGen** (34.6)
- `optimization`: **DSPy** (66.4)
- `orchestration`: **OpenAI Agents SDK** (77.4), **LangGraph** (74.5), **Claude Agent SDK** (68.2), **Google ADK** (54.3)
- `pipeline`: **Haystack** (71.0)
- `structured`: **PydanticAI** (55.0)
- `tooling`: **Composio** (68.3)
- `typescript`: **Mastra** (76.7)
- `web-agent`: **BrowserUse** (89.9)

## 🔍 Top 5 — Score Breakdown

| Framework | Star Velocity | Release Freshness | Issue Health | Commit Activity | Community | Fork Ratio |
|-----------|:---:|:---:|:---:|:---:|:---:|:---:|
| **BrowserUse** | 100 | 99.0 | 93.6 | 100 | 67.0 | 44.0 |
| **CrewAI** | 70.3 | 100.0 | 94.6 | 95.0 | 60.0 | 57.2 |
| **OpenAI Agents SDK** | 36.2 | 100.0 | 99.3 | 100 | 71.4 | 63.1 |
| **Mastra** | 36.5 | 100.0 | 95.7 | 100 | 93.0 | 38.9 |
| **LangGraph** | 100 | 100.0 | 69.6 | 34.0 | 55.6 | 67.3 |

## 💡 Key Insights

- **Hottest framework**: BrowserUse with a Pulse Score of 89.9
- **Fastest growing**: BrowserUse gained +782 stars this week
- **Most active development**: Mastra with 1517 commits in the last 4 weeks
- **Stale releases**: AutoGen, Swarm haven't released in a while

## 📦 Recent Releases

- **PydanticAI** [`v2.32.1`](https://github.com/pydantic/pydantic-ai/releases/tag/v2.32.1) — today
- **Claude Agent SDK** [`v2.1.237`](https://github.com/anthropics/claude-code/releases/tag/v2.1.237) — today
- **CrewAI** [`1.15.17`](https://github.com/crewAIInc/crewAI/releases/tag/1.15.17) — today
- **LlamaIndex** [`v0.14.24`](https://github.com/run-llama/llama_index/releases/tag/v0.14.24) — today
- **LangGraph** [`sdk==0.4.3`](https://github.com/langchain-ai/langgraph/releases/tag/sdk==0.4.3) — today
- **Mastra** [`@mastra/core@1.60.0`](https://github.com/mastra-ai/mastra/releases/tag/@mastra/core@1.60.0) — today
- **OpenAI Agents SDK** [`v0.22.0`](https://github.com/openai/openai-agents-python/releases/tag/v0.22.0) — today
- **Composio** [`@composio/slim@0.17.0`](https://github.com/ComposioHQ/composio/releases/tag/@composio/slim@0.17.0) — 1 day ago
- **Semantic Kernel** [`dotnet-1.80.0`](https://github.com/microsoft/semantic-kernel/releases/tag/dotnet-1.80.0) — 1 day ago
- **Haystack** [`v3.1.0-rc1`](https://github.com/deepset-ai/haystack/releases/tag/v3.1.0-rc1) — 1 day ago *(pre-release)*

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

*Powered by GitHub Actions • Data refreshed daily • Last run: 2026-08-20 06:53 UTC*