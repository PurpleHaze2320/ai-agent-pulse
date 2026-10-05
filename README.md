# 🔬 AI Agent Framework Pulse Tracker

[![Daily Update](https://github.com/PurpleHaze2320/ai-agent-pulse/actions/workflows/track.yml/badge.svg)](https://github.com/PurpleHaze2320/ai-agent-pulse/actions/workflows/track.yml)
[![Frameworks Tracked](https://img.shields.io/badge/frameworks-19-blue)](https://github.com/PurpleHaze2320/ai-agent-pulse)
[![License: MIT](https://img.shields.io/badge/License-MIT-green.svg)](https://opensource.org/licenses/MIT)
[![GitHub stars](https://img.shields.io/github/stars/PurpleHaze2320/ai-agent-pulse?style=social)](https://github.com/PurpleHaze2320/ai-agent-pulse/stargazers)

> Automated daily tracking of the AI agent framework ecosystem's health, momentum, and trends.
> Last updated: **2026-10-05 14:08 UTC** | Tracking **19** frameworks

## How It Works

This bot runs daily via GitHub Actions and collects metrics from the GitHub API for the most important
AI agent frameworks. It computes a **Pulse Score** (0-100) based on six weighted signals: star velocity,
release freshness, issue health, commit activity, community size, and fork engagement. The result is
a living dashboard that shows which frameworks are gaining momentum and which are losing steam.

## 🏆 Pulse Leaderboard

| Rank | Framework | Pulse | Stars | ⭐ 7d | Commits (4w) | Last Release | Category |
|------|-----------|-------|-------|-------|--------------|--------------|----------|
| 1 | [Claude Agent SDK](https://github.com/anthropics/claude-code) | 🟢 **80.6** | 149.5k | 🚀 +1037 | 74 | 1 day ago | `orchestration` |
| 2 | [BrowserUse](https://github.com/browser-use/browser-use) | 🟢 **77.3** | 117.2k | 🚀 +586 | 46 | 1 mo ago | `web-agent` |
| 3 | [Mastra](https://github.com/mastra-ai/mastra) | 🟢 **77.1** | 28.6k | 🚀 +178 | 1784 | today | `typescript` |
| 4 | [OpenAI Agents SDK](https://github.com/openai/openai-agents-python) | 🟢 **75.2** | 29.8k | 🚀 +102 | 212 | 2 days ago | `orchestration` |
| 5 | [PydanticAI](https://github.com/pydantic/pydantic-ai) | 🟢 **74.9** | 20.4k | 🚀 +179 | 668 | 2 days ago | `structured` |
| 6 | [Google ADK](https://github.com/google/adk-python) | 🟢 **72.1** | 21.7k | 📈 +39 | 363 | 3 days ago | `orchestration` |
| 7 | [Agno](https://github.com/agno-agi/agno) | 🟢 **71.6** | 42.6k | 🚀 +195 | 88 | 3 days ago | `multi-agent` |
| 8 | [CrewAI](https://github.com/crewAIInc/crewAI) | 🟢 **71.3** | 59.4k | 🚀 +225 | 65 | 6 days ago | `multi-agent` |
| 9 | [LangGraph](https://github.com/langchain-ai/langgraph) | 🟡 **69.2** | 42.7k | 🚀 +327 | 51 | 11 days ago | `orchestration` |
| 10 | [Composio](https://github.com/ComposioHQ/composio) | 🟡 **67.1** | 30.4k | 📈 +91 | 266 | 3 days ago | `tooling` |
| 11 | [AG2](https://github.com/ag2ai/ag2) | 🟡 **67.0** | 5.0k | ↗️ +10 | 87 | 2 days ago | `multi-agent` |
| 12 | [LlamaIndex](https://github.com/run-llama/llama_index) | 🟡 **57.9** | 52.4k | 📈 +76 | 22 | 13 days ago | `data-agent` |
| 13 | [Haystack](https://github.com/deepset-ai/haystack) | 🟡 **50.5** | 26.7k | 📈 +39 | 0 | 4 days ago | `pipeline` |
| 14 | [Semantic Kernel](https://github.com/microsoft/semantic-kernel) | 🟡 **50.5** | 28.6k | 📈 +22 | 10 | 1 mo ago | `enterprise` |
| 15 | [DSPy](https://github.com/stanfordnlp/dspy) | 🟡 **49.4** | 38.5k | 🚀 +107 | 0 | 10 days ago | `optimization` |
| 16 | [Letta](https://github.com/letta-ai/letta) | 🟠 **36.7** | 25.0k | 📈 +78 | 0 | 4 mo ago | `memory` |
| 17 | [Smolagents](https://github.com/huggingface/smolagents) | 🟠 **36.2** | 29.7k | 🚀 +136 | 4 | 4 mo ago | `lightweight` |
| 18 | [AutoGen](https://github.com/microsoft/autogen) | 🟠 **30.9** | 61.3k | 📈 +57 | 0 | 1y ago | `multi-agent` |
| 19 | [Swarm](https://github.com/openai/swarm) | 🔴 **9.4** | 22.0k | ↗️ +16 | 0 | — | `experimental` |

## 📂 By Category

- `data-agent`: **LlamaIndex** (57.9)
- `enterprise`: **Semantic Kernel** (50.5)
- `experimental`: **Swarm** (9.4)
- `lightweight`: **Smolagents** (36.2)
- `memory`: **Letta** (36.7)
- `multi-agent`: **Agno** (71.6), **CrewAI** (71.3), **AG2** (67.0), **AutoGen** (30.9)
- `optimization`: **DSPy** (49.4)
- `orchestration`: **Claude Agent SDK** (80.6), **OpenAI Agents SDK** (75.2), **Google ADK** (72.1), **LangGraph** (69.2)
- `pipeline`: **Haystack** (50.5)
- `structured`: **PydanticAI** (74.9)
- `tooling`: **Composio** (67.1)
- `typescript`: **Mastra** (77.1)
- `web-agent`: **BrowserUse** (77.3)

## 🔍 Top 5 — Score Breakdown

| Framework | Star Velocity | Release Freshness | Issue Health | Commit Activity | Community | Fork Ratio |
|-----------|:---:|:---:|:---:|:---:|:---:|:---:|
| **Claude Agent SDK** | 100 | 99.7 | 86.0 | 74.0 | 11.4 | 68.4 |
| **BrowserUse** | 100 | 89.7 | 90.2 | 46.0 | 72.0 | 44.1 |
| **Mastra** | 37.6 | 100.0 | 95.1 | 100 | 93.6 | 40.8 |
| **OpenAI Agents SDK** | 23.9 | 99.3 | 99.8 | 100 | 79.4 | 64.9 |
| **PydanticAI** | 35.3 | 99.3 | 74.2 | 100 | 95.0 | 56.1 |

## 💡 Key Insights

- **Hottest framework**: Claude Agent SDK with a Pulse Score of 80.6
- **Fastest growing**: Claude Agent SDK gained +1037 stars this week
- **Most active development**: Mastra with 1784 commits in the last 4 weeks
- **Stale releases**: AutoGen, Swarm haven't released in a while

## 📦 Recent Releases

- **Mastra** [`@mastra/core@1.74.0`](https://github.com/mastra-ai/mastra/releases/tag/@mastra/core@1.74.0) — today
- **Claude Agent SDK** [`v2.1.289`](https://github.com/anthropics/claude-code/releases/tag/v2.1.289) — 1 day ago
- **AG2** [`v1.1.2`](https://github.com/ag2ai/ag2/releases/tag/v1.1.2) — 2 days ago
- **PydanticAI** [`v2.54.0`](https://github.com/pydantic/pydantic-ai/releases/tag/v2.54.0) — 2 days ago
- **OpenAI Agents SDK** [`v0.23.1`](https://github.com/openai/openai-agents-python/releases/tag/v0.23.1) — 2 days ago
- **Agno** [`v3.1.1`](https://github.com/agno-agi/agno/releases/tag/v3.1.1) — 3 days ago
- **Google ADK** [`v2.11.0`](https://github.com/google/adk-python/releases/tag/v2.11.0) — 3 days ago
- **Composio** [`@composio/cli@0.4.3-beta.411`](https://github.com/ComposioHQ/composio/releases/tag/@composio/cli@0.4.3-beta.411) — 3 days ago *(pre-release)*
- **Haystack** [`v3.3.0`](https://github.com/deepset-ai/haystack/releases/tag/v3.3.0) — 4 days ago
- **CrewAI** [`1.15.23`](https://github.com/crewAIInc/crewAI/releases/tag/1.15.23) — 6 days ago

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

*Powered by GitHub Actions • Data refreshed daily • Last run: 2026-10-05 14:08 UTC*