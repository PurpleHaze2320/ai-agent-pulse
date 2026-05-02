# 🔬 AI Agent Framework Pulse Tracker

[![Daily Update](https://github.com/PurpleHaze2320/ai-agent-pulse/actions/workflows/track.yml/badge.svg)](https://github.com/PurpleHaze2320/ai-agent-pulse/actions/workflows/track.yml)
[![Frameworks Tracked](https://img.shields.io/badge/frameworks-19-blue)](https://github.com/PurpleHaze2320/ai-agent-pulse)
[![License: MIT](https://img.shields.io/badge/License-MIT-green.svg)](https://opensource.org/licenses/MIT)
[![GitHub stars](https://img.shields.io/github/stars/PurpleHaze2320/ai-agent-pulse?style=social)](https://github.com/PurpleHaze2320/ai-agent-pulse/stargazers)

> Automated daily tracking of the AI agent framework ecosystem's health, momentum, and trends.
> Last updated: **2026-05-02 07:52 UTC** | Tracking **19** frameworks

## How It Works

This bot runs daily via GitHub Actions and collects metrics from the GitHub API for the most important
AI agent frameworks. It computes a **Pulse Score** (0-100) based on six weighted signals: star velocity,
release freshness, issue health, commit activity, community size, and fork engagement. The result is
a living dashboard that shows which frameworks are gaining momentum and which are losing steam.

## 🏆 Pulse Leaderboard

| Rank | Framework | Pulse | Stars | ⭐ 7d | Commits (4w) | Last Release | Category |
|------|-----------|-------|-------|-------|--------------|--------------|----------|
| 1 | [Mastra](https://github.com/mastra-ai/mastra) | 🟢 **75.4** | 23.5k | 🚀 +172 | 922 | today | `typescript` |
| 2 | [CrewAI](https://github.com/crewAIInc/crewAI) | 🟢 **70.9** | 50.5k | 🚀 +622 | 0 | today | `multi-agent` |
| 3 | [OpenAI Agents SDK](https://github.com/openai/openai-agents-python) | 🟢 **70.8** | 25.7k | 🚀 +696 | 0 | today | `orchestration` |
| 4 | [LangGraph](https://github.com/langchain-ai/langgraph) | 🟡 **69.1** | 31.0k | 🚀 +719 | 0 | today | `orchestration` |
| 5 | [BrowserUse](https://github.com/browser-use/browser-use) | 🟡 **68.4** | 91.6k | 🚀 +1525 | 0 | 29 days ago | `web-agent` |
| 6 | [Claude Agent SDK](https://github.com/anthropics/claude-code) | 🟡 **64.6** | 119.8k | 🚀 +2060 | 0 | 1 day ago | `orchestration` |
| 7 | [LlamaIndex](https://github.com/run-llama/llama_index) | 🟡 **59.3** | 49.1k | 🚀 +191 | 0 | 11 days ago | `data-agent` |
| 8 | [Agno](https://github.com/agno-agi/agno) | 🟡 **55.7** | 39.9k | 🚀 +197 | 0 | 3 days ago | `multi-agent` |
| 9 | [PydanticAI](https://github.com/pydantic/pydantic-ai) | 🟡 **55.1** | 16.8k | 🚀 +182 | 0 | today | `structured` |
| 10 | [Google ADK](https://github.com/google/adk-python) | 🟡 **52.0** | 19.4k | 🚀 +137 | 0 | 1 day ago | `orchestration` |
| 11 | [Semantic Kernel](https://github.com/microsoft/semantic-kernel) | 🟡 **51.4** | 27.8k | 📈 +50 | 0 | 2 days ago | `enterprise` |
| 12 | [DSPy](https://github.com/stanfordnlp/dspy) | 🟡 **51.1** | 34.2k | 🚀 +160 | 0 | 10 days ago | `optimization` |
| 13 | [Haystack](https://github.com/deepset-ai/haystack) | 🟡 **49.2** | 25.1k | 📈 +74 | 0 | 11 days ago | `pipeline` |
| 14 | [AG2](https://github.com/ag2ai/ag2) | 🟡 **48.4** | 4.5k | 📈 +22 | 0 | 1 day ago | `multi-agent` |
| 15 | [Letta](https://github.com/letta-ai/letta) | 🟡 **46.1** | 22.4k | 🚀 +132 | 0 | 1 mo ago | `memory` |
| 16 | [AutoGen](https://github.com/microsoft/autogen) | 🟡 **45.3** | 57.7k | 🚀 +235 | 0 | 7 mo ago | `multi-agent` |
| 17 | [Composio](https://github.com/ComposioHQ/composio) | 🟡 **44.8** | 28.0k | 📈 +80 | 0 | today | `tooling` |
| 18 | [Smolagents](https://github.com/huggingface/smolagents) | 🟠 **38.5** | 27.0k | 🚀 +157 | 0 | 3 mo ago | `lightweight` |
| 19 | [Swarm](https://github.com/openai/swarm) | 🔴 **10.0** | 21.4k | 📈 +45 | 0 | — | `experimental` |

## 📂 By Category

- `data-agent`: **LlamaIndex** (59.3)
- `enterprise`: **Semantic Kernel** (51.4)
- `experimental`: **Swarm** (10.0)
- `lightweight`: **Smolagents** (38.5)
- `memory`: **Letta** (46.1)
- `multi-agent`: **CrewAI** (70.9), **Agno** (55.7), **AG2** (48.4), **AutoGen** (45.3)
- `optimization`: **DSPy** (51.1)
- `orchestration`: **OpenAI Agents SDK** (70.8), **LangGraph** (69.1), **Claude Agent SDK** (64.6), **Google ADK** (52.0)
- `pipeline`: **Haystack** (49.2)
- `structured`: **PydanticAI** (55.1)
- `tooling`: **Composio** (44.8)
- `typescript`: **Mastra** (75.4)
- `web-agent`: **BrowserUse** (68.4)

## 🔍 Top 5 — Score Breakdown

| Framework | Star Velocity | Release Freshness | Issue Health | Commit Activity | Community | Fork Ratio |
|-----------|:---:|:---:|:---:|:---:|:---:|:---:|
| **Mastra** | 37.5 | 100.0 | 94.7 | 100 | 83.8 | 34.0 |
| **CrewAI** | 100 | 100.0 | 97.1 | 0.0 | 58.2 | 55.1 |
| **OpenAI Agents SDK** | 100 | 100.0 | 96.5 | 0.0 | 52.4 | 61.0 |
| **LangGraph** | 100 | 100.0 | 78.7 | 0.0 | 54.8 | 68.2 |
| **BrowserUse** | 100 | 90.3 | 97.1 | 0.0 | 62.6 | 45.5 |

## 💡 Key Insights

- **Hottest framework**: Mastra with a Pulse Score of 75.4
- **Fastest growing**: Claude Agent SDK gained +2060 stars this week
- **Most active development**: Mastra with 922 commits in the last 4 weeks
- **Stale releases**: Swarm haven't released in a while

## 📦 Recent Releases

- **OpenAI Agents SDK** [`v0.15.1`](https://github.com/openai/openai-agents-python/releases/tag/v0.15.1) — today
- **Composio** [`@composio/cli@0.2.28`](https://github.com/ComposioHQ/composio/releases/tag/@composio/cli@0.2.28) — today
- **CrewAI** [`1.14.5a1`](https://github.com/crewAIInc/crewAI/releases/tag/1.14.5a1) — today *(pre-release)*
- **PydanticAI** [`v1.89.1`](https://github.com/pydantic/pydantic-ai/releases/tag/v1.89.1) — today
- **LangGraph** [`1.2.0a5`](https://github.com/langchain-ai/langgraph/releases/tag/1.2.0a5) — today
- **Mastra** [`@mastra/core@1.30.0`](https://github.com/mastra-ai/mastra/releases/tag/@mastra/core@1.30.0) — today
- **Claude Agent SDK** [`v2.1.126`](https://github.com/anthropics/claude-code/releases/tag/v2.1.126) — 1 day ago
- **Google ADK** [`v1.32.0`](https://github.com/google/adk-python/releases/tag/v1.32.0) — 1 day ago
- **AG2** [`v0.12.2`](https://github.com/ag2ai/ag2/releases/tag/v0.12.2) — 1 day ago
- **Semantic Kernel** [`dotnet-1.75.0`](https://github.com/microsoft/semantic-kernel/releases/tag/dotnet-1.75.0) — 2 days ago

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

*Powered by GitHub Actions • Data refreshed daily • Last run: 2026-05-02 07:52 UTC*