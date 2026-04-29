# 🔬 AI Agent Framework Pulse Tracker

[![Daily Update](https://github.com/PurpleHaze2320/ai-agent-pulse/actions/workflows/track.yml/badge.svg)](https://github.com/PurpleHaze2320/ai-agent-pulse/actions/workflows/track.yml)
[![Frameworks Tracked](https://img.shields.io/badge/frameworks-19-blue)](https://github.com/PurpleHaze2320/ai-agent-pulse)
[![License: MIT](https://img.shields.io/badge/License-MIT-green.svg)](https://opensource.org/licenses/MIT)
[![GitHub stars](https://img.shields.io/github/stars/PurpleHaze2320/ai-agent-pulse?style=social)](https://github.com/PurpleHaze2320/ai-agent-pulse/stargazers)

> Automated daily tracking of the AI agent framework ecosystem's health, momentum, and trends.
> Last updated: **2026-04-29 08:27 UTC** | Tracking **19** frameworks

## How It Works

This bot runs daily via GitHub Actions and collects metrics from the GitHub API for the most important
AI agent frameworks. It computes a **Pulse Score** (0-100) based on six weighted signals: star velocity,
release freshness, issue health, commit activity, community size, and fork engagement. The result is
a living dashboard that shows which frameworks are gaining momentum and which are losing steam.

## 🏆 Pulse Leaderboard

| Rank | Framework | Pulse | Stars | ⭐ 7d | Commits (4w) | Last Release | Category |
|------|-----------|-------|-------|-------|--------------|--------------|----------|
| 1 | [Mastra](https://github.com/mastra-ai/mastra) | 🟢 **75.9** | 23.4k | 🚀 +200 | 716 | today | `typescript` |
| 2 | [OpenAI Agents SDK](https://github.com/openai/openai-agents-python) | 🟢 **70.8** | 25.5k | 🚀 +1058 | 0 | today | `orchestration` |
| 3 | [Claude Agent SDK](https://github.com/anthropics/claude-code) | 🟢 **70.7** | 119.0k | 🚀 +2277 | 30 | today | `orchestration` |
| 4 | [CrewAI](https://github.com/crewAIInc/crewAI) | 🟢 **70.5** | 50.2k | 🚀 +746 | 0 | 4 days ago | `multi-agent` |
| 5 | [LangGraph](https://github.com/langchain-ai/langgraph) | 🟡 **69.1** | 30.7k | 🚀 +786 | 0 | 1 day ago | `orchestration` |
| 6 | [BrowserUse](https://github.com/browser-use/browser-use) | 🟡 **68.6** | 91.1k | 🚀 +1720 | 0 | 27 days ago | `web-agent` |
| 7 | [Composio](https://github.com/ComposioHQ/composio) | 🟡 **65.3** | 28.0k | 📈 +99 | 229 | 1 day ago | `tooling` |
| 8 | [LlamaIndex](https://github.com/run-llama/llama_index) | 🟡 **60.8** | 49.0k | 🚀 +235 | 0 | 8 days ago | `data-agent` |
| 9 | [Agno](https://github.com/agno-agi/agno) | 🟡 **55.0** | 39.8k | 🚀 +181 | 0 | today | `multi-agent` |
| 10 | [PydanticAI](https://github.com/pydantic/pydantic-ai) | 🟡 **54.6** | 16.7k | 🚀 +175 | 0 | today | `structured` |
| 11 | [Google ADK](https://github.com/google/adk-python) | 🟡 **52.6** | 19.3k | 🚀 +170 | 0 | 6 days ago | `orchestration` |
| 12 | [DSPy](https://github.com/stanfordnlp/dspy) | 🟡 **51.3** | 34.1k | 🚀 +168 | 0 | 7 days ago | `optimization` |
| 13 | [Semantic Kernel](https://github.com/microsoft/semantic-kernel) | 🟡 **51.0** | 27.8k | 📈 +53 | 0 | 1 day ago | `enterprise` |
| 14 | [Haystack](https://github.com/deepset-ai/haystack) | 🟡 **49.0** | 25.0k | 📈 +69 | 0 | 8 days ago | `pipeline` |
| 15 | [AG2](https://github.com/ag2ai/ag2) | 🟡 **48.5** | 4.5k | 📈 +34 | 0 | 4 days ago | `multi-agent` |
| 16 | [Letta](https://github.com/letta-ai/letta) | 🟡 **46.7** | 22.4k | 🚀 +150 | 0 | 28 days ago | `memory` |
| 17 | [AutoGen](https://github.com/microsoft/autogen) | 🟡 **45.4** | 57.6k | 🚀 +241 | 0 | 7 mo ago | `multi-agent` |
| 18 | [Smolagents](https://github.com/huggingface/smolagents) | 🟠 **39.0** | 27.0k | 🚀 +169 | 0 | 3 mo ago | `lightweight` |
| 19 | [Swarm](https://github.com/openai/swarm) | 🔴 **9.9** | 21.4k | 📈 +44 | 0 | — | `experimental` |

## 📂 By Category

- `data-agent`: **LlamaIndex** (60.8)
- `enterprise`: **Semantic Kernel** (51.0)
- `experimental`: **Swarm** (9.9)
- `lightweight`: **Smolagents** (39.0)
- `memory`: **Letta** (46.7)
- `multi-agent`: **CrewAI** (70.5), **Agno** (55.0), **AG2** (48.5), **AutoGen** (45.4)
- `optimization`: **DSPy** (51.3)
- `orchestration`: **OpenAI Agents SDK** (70.8), **Claude Agent SDK** (70.7), **LangGraph** (69.1), **Google ADK** (52.6)
- `pipeline`: **Haystack** (49.0)
- `structured`: **PydanticAI** (54.6)
- `tooling`: **Composio** (65.3)
- `typescript`: **Mastra** (75.9)
- `web-agent`: **BrowserUse** (68.6)

## 🔍 Top 5 — Score Breakdown

| Framework | Star Velocity | Release Freshness | Issue Health | Commit Activity | Community | Fork Ratio |
|-----------|:---:|:---:|:---:|:---:|:---:|:---:|
| **Mastra** | 40.6 | 100.0 | 94.5 | 100 | 81.8 | 33.8 |
| **OpenAI Agents SDK** | 100 | 100.0 | 96.5 | 0.0 | 52.0 | 61.0 |
| **Claude Agent SDK** | 100 | 100.0 | 80.4 | 30.0 | 9.6 | 66.4 |
| **CrewAI** | 100 | 98.7 | 96.3 | 0.0 | 57.8 | 55.1 |
| **LangGraph** | 100 | 99.7 | 79.0 | 0.0 | 55.0 | 68.3 |

## 💡 Key Insights

- **Hottest framework**: Mastra with a Pulse Score of 75.9
- **Fastest growing**: Claude Agent SDK gained +2277 stars this week
- **Most active development**: Mastra with 716 commits in the last 4 weeks
- **Stale releases**: Swarm haven't released in a while

## 📦 Recent Releases

- **PydanticAI** [`v1.88.0`](https://github.com/pydantic/pydantic-ai/releases/tag/v1.88.0) — today
- **OpenAI Agents SDK** [`v0.14.8`](https://github.com/openai/openai-agents-python/releases/tag/v0.14.8) — today
- **Claude Agent SDK** [`v2.1.123`](https://github.com/anthropics/claude-code/releases/tag/v2.1.123) — today
- **Agno** [`v2.6.4`](https://github.com/agno-agi/agno/releases/tag/v2.6.4) — today
- **Mastra** [`@mastra/core@1.28.0`](https://github.com/mastra-ai/mastra/releases/tag/@mastra/core@1.28.0) — today
- **Composio** [`py@0.12.0`](https://github.com/ComposioHQ/composio/releases/tag/py@0.12.0) — 1 day ago
- **Semantic Kernel** [`python-1.41.3`](https://github.com/microsoft/semantic-kernel/releases/tag/python-1.41.3) — 1 day ago
- **LangGraph** [`1.1.10`](https://github.com/langchain-ai/langgraph/releases/tag/1.1.10) — 1 day ago
- **AG2** [`v0.12.1`](https://github.com/ag2ai/ag2/releases/tag/v0.12.1) — 4 days ago
- **CrewAI** [`1.14.3`](https://github.com/crewAIInc/crewAI/releases/tag/1.14.3) — 4 days ago

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

*Powered by GitHub Actions • Data refreshed daily • Last run: 2026-04-29 08:27 UTC*