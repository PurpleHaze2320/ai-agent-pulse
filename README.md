# 🔬 AI Agent Framework Pulse Tracker

[![Daily Update](https://github.com/PurpleHaze2320/ai-agent-pulse/actions/workflows/track.yml/badge.svg)](https://github.com/PurpleHaze2320/ai-agent-pulse/actions/workflows/track.yml)
[![Frameworks Tracked](https://img.shields.io/badge/frameworks-19-blue)](https://github.com/PurpleHaze2320/ai-agent-pulse)
[![License: MIT](https://img.shields.io/badge/License-MIT-green.svg)](https://opensource.org/licenses/MIT)
[![GitHub stars](https://img.shields.io/github/stars/PurpleHaze2320/ai-agent-pulse?style=social)](https://github.com/PurpleHaze2320/ai-agent-pulse/stargazers)

> Automated daily tracking of the AI agent framework ecosystem's health, momentum, and trends.
> Last updated: **2026-11-26 16:40 UTC** | Tracking **19** frameworks

## How It Works

This bot runs daily via GitHub Actions and collects metrics from the GitHub API for the most important
AI agent frameworks. It computes a **Pulse Score** (0-100) based on six weighted signals: star velocity,
release freshness, issue health, commit activity, community size, and fork engagement. The result is
a living dashboard that shows which frameworks are gaining momentum and which are losing steam.

## 🏆 Pulse Leaderboard

| Rank | Framework | Pulse | Stars | ⭐ 7d | Commits (4w) | Last Release | Category |
|------|-----------|-------|-------|-------|--------------|--------------|----------|
| 1 | [BrowserUse](https://github.com/browser-use/browser-use) | 🟢 **89.9** | 122.1k | 🚀 +643 | 1198 | 4 days ago | `web-agent` |
| 2 | [Claude Agent SDK](https://github.com/anthropics/claude-code) | 🟢 **85.3** | 157.2k | 🚀 +893 | 218 | 1 day ago | `orchestration` |
| 3 | [CrewAI](https://github.com/crewAIInc/crewAI) | 🟢 **77.5** | 61.3k | 🚀 +192 | 177 | 2 days ago | `multi-agent` |
| 4 | [Mastra](https://github.com/mastra-ai/mastra) | 🟢 **76.6** | 29.8k | 🚀 +185 | 2335 | 1 day ago | `typescript` |
| 5 | [LangGraph](https://github.com/langchain-ai/langgraph) | 🟢 **76.3** | 45.5k | 🚀 +306 | 77 | today | `orchestration` |
| 6 | [Google ADK](https://github.com/google/adk-python) | 🟢 **74.8** | 22.4k | 📈 +91 | 272 | 1 day ago | `orchestration` |
| 7 | [OpenAI Agents SDK](https://github.com/openai/openai-agents-python) | 🟢 **73.1** | 30.9k | 🚀 +119 | 89 | 2 days ago | `orchestration` |
| 8 | [Haystack](https://github.com/deepset-ai/haystack) | 🟢 **71.1** | 27.1k | 📈 +66 | 270 | 16 days ago | `pipeline` |
| 9 | [AG2](https://github.com/ag2ai/ag2) | 🟢 **70.1** | 5.1k | ↗️ +16 | 107 | 3 days ago | `multi-agent` |
| 10 | [PydanticAI](https://github.com/pydantic/pydantic-ai) | 🟡 **69.4** | 21.4k | 🚀 +120 | 1001 | 1 mo ago | `structured` |
| 11 | [Composio](https://github.com/ComposioHQ/composio) | 🟡 **69.0** | 31.3k | 🚀 +131 | 319 | today | `tooling` |
| 12 | [DSPy](https://github.com/stanfordnlp/dspy) | 🟡 **60.0** | 39.2k | 🚀 +110 | 59 | 16 days ago | `optimization` |
| 13 | [Semantic Kernel](https://github.com/microsoft/semantic-kernel) | 🟡 **57.8** | 28.8k | ↗️ +19 | 38 | 19 days ago | `enterprise` |
| 14 | [LlamaIndex](https://github.com/run-llama/llama_index) | 🟡 **56.9** | 53.0k | 📈 +53 | 22 | 12 days ago | `data-agent` |
| 15 | [Agno](https://github.com/agno-agi/agno) | 🟡 **48.9** | 43.3k | 📈 +76 | 0 | 8 days ago | `multi-agent` |
| 16 | [Smolagents](https://github.com/huggingface/smolagents) | 🟠 **34.9** | 30.6k | 🚀 +107 | 23 | 6 mo ago | `lightweight` |
| 17 | [Letta](https://github.com/letta-ai/letta) | 🟠 **32.6** | 25.6k | 📈 +71 | 0 | 6 mo ago | `memory` |
| 18 | [AutoGen](https://github.com/microsoft/autogen) | 🟠 **29.7** | 62.0k | 📈 +25 | 1 | 1y ago | `multi-agent` |
| 19 | [Swarm](https://github.com/openai/swarm) | 🔴 **9.5** | 22.2k | ↗️ +20 | 0 | — | `experimental` |

## 📂 By Category

- `data-agent`: **LlamaIndex** (56.9)
- `enterprise`: **Semantic Kernel** (57.8)
- `experimental`: **Swarm** (9.5)
- `lightweight`: **Smolagents** (34.9)
- `memory`: **Letta** (32.6)
- `multi-agent`: **CrewAI** (77.5), **AG2** (70.1), **Agno** (48.9), **AutoGen** (29.7)
- `optimization`: **DSPy** (60.0)
- `orchestration`: **Claude Agent SDK** (85.3), **LangGraph** (76.3), **Google ADK** (74.8), **OpenAI Agents SDK** (73.1)
- `pipeline`: **Haystack** (71.1)
- `structured`: **PydanticAI** (69.4)
- `tooling`: **Composio** (69.0)
- `typescript`: **Mastra** (76.6)
- `web-agent`: **BrowserUse** (89.9)

## 🔍 Top 5 — Score Breakdown

| Framework | Star Velocity | Release Freshness | Issue Health | Commit Activity | Community | Fork Ratio |
|-----------|:---:|:---:|:---:|:---:|:---:|:---:|
| **BrowserUse** | 100 | 98.7 | 89.7 | 100 | 72.2 | 44.7 |
| **Claude Agent SDK** | 100 | 99.7 | 85.5 | 100 | 11.2 | 64.0 |
| **CrewAI** | 43.8 | 99.3 | 85.1 | 100 | 78.4 | 60.7 |
| **Mastra** | 36.7 | 99.7 | 92.9 | 100 | 93.2 | 42.1 |
| **LangGraph** | 65.0 | 100.0 | 79.4 | 77.0 | 57.6 | 69.3 |

## 💡 Key Insights

- **Hottest framework**: BrowserUse with a Pulse Score of 89.9
- **Fastest growing**: Claude Agent SDK gained +893 stars this week
- **Most active development**: Mastra with 2335 commits in the last 4 weeks
- **⚠️ Archived**: AutoGen
- **Stale releases**: AutoGen, Swarm haven't released in a while

## 📦 Recent Releases

- **Composio** [`@composio/cli@0.6.5-beta.584`](https://github.com/ComposioHQ/composio/releases/tag/@composio/cli@0.6.5-beta.584) — today *(pre-release)*
- **LangGraph** [`cli==0.4.44`](https://github.com/langchain-ai/langgraph/releases/tag/cli==0.4.44) — today
- **Mastra** [`@mastra/core@1.86.0`](https://github.com/mastra-ai/mastra/releases/tag/@mastra/core@1.86.0) — 1 day ago
- **Claude Agent SDK** [`v2.1.332`](https://github.com/anthropics/claude-code/releases/tag/v2.1.332) — 1 day ago
- **Google ADK** [`v2.15.1`](https://github.com/google/adk-python/releases/tag/v2.15.1) — 1 day ago
- **CrewAI** [`1.15.45`](https://github.com/crewAIInc/crewAI/releases/tag/1.15.45) — 2 days ago
- **OpenAI Agents SDK** [`v0.26.0`](https://github.com/openai/openai-agents-python/releases/tag/v0.26.0) — 2 days ago
- **AG2** [`v1.3.4`](https://github.com/ag2ai/ag2/releases/tag/v1.3.4) — 3 days ago
- **BrowserUse** [`1.0.8`](https://github.com/browser-use/browser-use/releases/tag/1.0.8) — 4 days ago
- **Agno** [`v3.2.1`](https://github.com/agno-agi/agno/releases/tag/v3.2.1) — 8 days ago

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

*Powered by GitHub Actions • Data refreshed daily • Last run: 2026-11-26 16:40 UTC*