# 🔬 AI Agent Framework Pulse Tracker

[![Daily Update](https://github.com/PurpleHaze2320/ai-agent-pulse/actions/workflows/track.yml/badge.svg)](https://github.com/PurpleHaze2320/ai-agent-pulse/actions/workflows/track.yml)
[![Frameworks Tracked](https://img.shields.io/badge/frameworks-19-blue)](https://github.com/PurpleHaze2320/ai-agent-pulse)
[![License: MIT](https://img.shields.io/badge/License-MIT-green.svg)](https://opensource.org/licenses/MIT)
[![GitHub stars](https://img.shields.io/github/stars/PurpleHaze2320/ai-agent-pulse?style=social)](https://github.com/PurpleHaze2320/ai-agent-pulse/stargazers)

> Automated daily tracking of the AI agent framework ecosystem's health, momentum, and trends.
> Last updated: **2026-04-20 08:19 UTC** | Tracking **19** frameworks

## How It Works

This bot runs daily via GitHub Actions and collects metrics from the GitHub API for the most important
AI agent frameworks. It computes a **Pulse Score** (0-100) based on six weighted signals: star velocity,
release freshness, issue health, commit activity, community size, and fork engagement. The result is
a living dashboard that shows which frameworks are gaining momentum and which are losing steam.

## 🏆 Pulse Leaderboard

| Rank | Framework | Pulse | Stars | ⭐ 7d | Commits (4w) | Last Release | Category |
|------|-----------|-------|-------|-------|--------------|--------------|----------|
| 1 | [Mastra](https://github.com/mastra-ai/mastra) | 🟢 **74.6** | 23.2k | 🚀 +227 | 642 | 11 days ago | `typescript` |
| 2 | [OpenAI Agents SDK](https://github.com/openai/openai-agents-python) | 🟢 **70.6** | 23.5k | 🚀 +2801 | 0 | 2 days ago | `orchestration` |
| 3 | [CrewAI](https://github.com/crewAIInc/crewAI) | 🟢 **70.0** | 49.3k | 🚀 +543 | 0 | 2 days ago | `multi-agent` |
| 4 | [LangGraph](https://github.com/langchain-ai/langgraph) | 🟡 **69.2** | 29.7k | 🚀 +599 | 0 | 2 days ago | `orchestration` |
| 5 | [BrowserUse](https://github.com/browser-use/browser-use) | 🟡 **69.2** | 88.8k | 🚀 +1265 | 0 | 18 days ago | `web-agent` |
| 6 | [Claude Agent SDK](https://github.com/anthropics/claude-code) | 🟡 **64.5** | 116.1k | 🚀 +2866 | 0 | 2 days ago | `orchestration` |
| 7 | [LlamaIndex](https://github.com/run-llama/llama_index) | 🟡 **56.5** | 48.7k | 🚀 +165 | 0 | 16 days ago | `data-agent` |
| 8 | [PydanticAI](https://github.com/pydantic/pydantic-ai) | 🟡 **53.3** | 16.5k | 🚀 +175 | 0 | 2 days ago | `structured` |
| 9 | [Google ADK](https://github.com/google/adk-python) | 🟡 **52.7** | 19.1k | 🚀 +197 | 0 | 3 days ago | `orchestration` |
| 10 | [Agno](https://github.com/agno-agi/agno) | 🟡 **52.5** | 39.5k | 🚀 +142 | 0 | 5 days ago | `multi-agent` |
| 11 | [Semantic Kernel](https://github.com/microsoft/semantic-kernel) | 🟡 **49.8** | 27.7k | 📈 +51 | 0 | 12 days ago | `enterprise` |
| 12 | [Haystack](https://github.com/deepset-ai/haystack) | 🟡 **48.6** | 24.9k | 📈 +88 | 0 | 18 days ago | `pipeline` |
| 13 | [AG2](https://github.com/ag2ai/ag2) | 🟡 **47.7** | 4.4k | 📈 +33 | 0 | 2 days ago | `multi-agent` |
| 14 | [DSPy](https://github.com/stanfordnlp/dspy) | 🟡 **47.2** | 33.8k | 🚀 +202 | 0 | 2 mo ago | `optimization` |
| 15 | [Letta](https://github.com/letta-ai/letta) | 🟡 **46.3** | 22.2k | 🚀 +143 | 0 | 19 days ago | `memory` |
| 16 | [Composio](https://github.com/ComposioHQ/composio) | 🟡 **43.9** | 27.8k | 📈 +71 | 0 | 2 days ago | `tooling` |
| 17 | [AutoGen](https://github.com/microsoft/autogen) | 🟡 **43.5** | 57.2k | 🚀 +205 | 0 | 6 mo ago | `multi-agent` |
| 18 | [Smolagents](https://github.com/huggingface/smolagents) | 🟠 **38.8** | 26.7k | 🚀 +170 | 0 | 3 mo ago | `lightweight` |
| 19 | [Swarm](https://github.com/openai/swarm) | 🔴 **10.3** | 21.4k | 📈 +52 | 0 | — | `experimental` |

## 📂 By Category

- `data-agent`: **LlamaIndex** (56.5)
- `enterprise`: **Semantic Kernel** (49.8)
- `experimental`: **Swarm** (10.3)
- `lightweight`: **Smolagents** (38.8)
- `memory`: **Letta** (46.3)
- `multi-agent`: **CrewAI** (70.0), **Agno** (52.5), **AG2** (47.7), **AutoGen** (43.5)
- `optimization`: **DSPy** (47.2)
- `orchestration`: **OpenAI Agents SDK** (70.6), **LangGraph** (69.2), **Claude Agent SDK** (64.5), **Google ADK** (52.7)
- `pipeline`: **Haystack** (48.6)
- `structured`: **PydanticAI** (53.3)
- `tooling`: **Composio** (43.9)
- `typescript`: **Mastra** (74.6)
- `web-agent`: **BrowserUse** (69.2)

## 🔍 Top 5 — Score Breakdown

| Framework | Star Velocity | Release Freshness | Issue Health | Commit Activity | Community | Fork Ratio |
|-----------|:---:|:---:|:---:|:---:|:---:|:---:|
| **Mastra** | 40.6 | 96.3 | 94.4 | 100 | 77.4 | 33.2 |
| **OpenAI Agents SDK** | 100 | 99.3 | 96.4 | 0.0 | 50.0 | 62.2 |
| **CrewAI** | 98.3 | 99.3 | 95.6 | 0.0 | 57.0 | 54.7 |
| **LangGraph** | 100 | 99.3 | 80.0 | 0.0 | 54.6 | 68.3 |
| **BrowserUse** | 100 | 94.0 | 97.8 | 0.0 | 61.6 | 45.8 |

## 💡 Key Insights

- **Hottest framework**: Mastra with a Pulse Score of 74.6
- **Fastest growing**: Claude Agent SDK gained +2866 stars this week
- **Most active development**: Mastra with 642 commits in the last 4 weeks
- **Stale releases**: Swarm haven't released in a while

## 📦 Recent Releases

- **Composio** [`@composio/cli@0.2.25-beta.215`](https://github.com/ComposioHQ/composio/releases/tag/@composio/cli@0.2.25-beta.215) — 2 days ago *(pre-release)*
- **Claude Agent SDK** [`v2.1.114`](https://github.com/anthropics/claude-code/releases/tag/v2.1.114) — 2 days ago
- **PydanticAI** [`v1.84.1`](https://github.com/pydantic/pydantic-ai/releases/tag/v1.84.1) — 2 days ago
- **OpenAI Agents SDK** [`v0.14.2`](https://github.com/openai/openai-agents-python/releases/tag/v0.14.2) — 2 days ago
- **AG2** [`v0.12.0`](https://github.com/ag2ai/ag2/releases/tag/v0.12.0) — 2 days ago
- **LangGraph** [`1.1.8`](https://github.com/langchain-ai/langgraph/releases/tag/1.1.8) — 2 days ago
- **CrewAI** [`1.14.2`](https://github.com/crewAIInc/crewAI/releases/tag/1.14.2) — 2 days ago
- **Google ADK** [`v1.31.0`](https://github.com/google/adk-python/releases/tag/v1.31.0) — 3 days ago
- **Agno** [`v2.5.17`](https://github.com/agno-agi/agno/releases/tag/v2.5.17) — 5 days ago
- **Mastra** [`@mastra/core@1.24.0`](https://github.com/mastra-ai/mastra/releases/tag/@mastra/core@1.24.0) — 11 days ago

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

*Powered by GitHub Actions • Data refreshed daily • Last run: 2026-04-20 08:19 UTC*