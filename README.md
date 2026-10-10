# 🔬 AI Agent Framework Pulse Tracker

[![Daily Update](https://github.com/PurpleHaze2320/ai-agent-pulse/actions/workflows/track.yml/badge.svg)](https://github.com/PurpleHaze2320/ai-agent-pulse/actions/workflows/track.yml)
[![Frameworks Tracked](https://img.shields.io/badge/frameworks-19-blue)](https://github.com/PurpleHaze2320/ai-agent-pulse)
[![License: MIT](https://img.shields.io/badge/License-MIT-green.svg)](https://opensource.org/licenses/MIT)
[![GitHub stars](https://img.shields.io/github/stars/PurpleHaze2320/ai-agent-pulse?style=social)](https://github.com/PurpleHaze2320/ai-agent-pulse/stargazers)

> Automated daily tracking of the AI agent framework ecosystem's health, momentum, and trends.
> Last updated: **2026-10-10 12:12 UTC** | Tracking **19** frameworks

## How It Works

This bot runs daily via GitHub Actions and collects metrics from the GitHub API for the most important
AI agent frameworks. It computes a **Pulse Score** (0-100) based on six weighted signals: star velocity,
release freshness, issue health, commit activity, community size, and fork engagement. The result is
a living dashboard that shows which frameworks are gaining momentum and which are losing steam.

## 🏆 Pulse Leaderboard

| Rank | Framework | Pulse | Stars | ⭐ 7d | Commits (4w) | Last Release | Category |
|------|-----------|-------|-------|-------|--------------|--------------|----------|
| 1 | [Claude Agent SDK](https://github.com/anthropics/claude-code) | 🟢 **83.0** | 150.0k | 🚀 +950 | 85 | today | `orchestration` |
| 2 | [BrowserUse](https://github.com/browser-use/browser-use) | 🟢 **81.5** | 117.5k | 🚀 +469 | 58 | 3 days ago | `web-agent` |
| 3 | [CrewAI](https://github.com/crewAIInc/crewAI) | 🟢 **76.8** | 59.5k | 🚀 +219 | 92 | today | `multi-agent` |
| 4 | [Mastra](https://github.com/mastra-ai/mastra) | 🟢 **75.9** | 28.7k | 🚀 +155 | 2288 | 2 days ago | `typescript` |
| 5 | [OpenAI Agents SDK](https://github.com/openai/openai-agents-python) | 🟢 **75.7** | 29.9k | 🚀 +126 | 232 | 7 days ago | `orchestration` |
| 6 | [PydanticAI](https://github.com/pydantic/pydantic-ai) | 🟢 **73.9** | 20.5k | 🚀 +150 | 837 | 4 days ago | `structured` |
| 7 | [Google ADK](https://github.com/google/adk-python) | 🟢 **73.1** | 21.8k | 📈 +71 | 493 | 8 days ago | `orchestration` |
| 8 | [Agno](https://github.com/agno-agi/agno) | 🟢 **71.5** | 42.6k | 🚀 +124 | 121 | 1 day ago | `multi-agent` |
| 9 | [Haystack](https://github.com/deepset-ai/haystack) | 🟢 **71.3** | 26.7k | 📈 +70 | 253 | 9 days ago | `pipeline` |
| 10 | [AG2](https://github.com/ag2ai/ag2) | 🟡 **69.1** | 5.0k | ↗️ +14 | 98 | 7 days ago | `multi-agent` |
| 11 | [Composio](https://github.com/ComposioHQ/composio) | 🟡 **66.3** | 30.5k | 📈 +68 | 295 | 1 day ago | `tooling` |
| 12 | [LangGraph](https://github.com/langchain-ai/langgraph) | 🟡 **60.8** | 43.0k | 🚀 +356 | 0 | 2 days ago | `orchestration` |
| 13 | [LlamaIndex](https://github.com/run-llama/llama_index) | 🟡 **57.7** | 52.5k | 📈 +66 | 25 | 18 days ago | `data-agent` |
| 14 | [Semantic Kernel](https://github.com/microsoft/semantic-kernel) | 🟡 **54.0** | 28.6k | ↗️ +19 | 19 | 3 days ago | `enterprise` |
| 15 | [DSPy](https://github.com/stanfordnlp/dspy) | 🟡 **48.6** | 38.6k | 📈 +99 | 0 | 15 days ago | `optimization` |
| 16 | [Letta](https://github.com/letta-ai/letta) | 🟠 **36.6** | 25.1k | 📈 +83 | 0 | 4 mo ago | `memory` |
| 17 | [Smolagents](https://github.com/huggingface/smolagents) | 🟠 **34.7** | 29.8k | 🚀 +103 | 5 | 4 mo ago | `lightweight` |
| 18 | [AutoGen](https://github.com/microsoft/autogen) | 🟠 **32.0** | 61.3k | 📈 +91 | 0 | 1y ago | `multi-agent` |
| 19 | [Swarm](https://github.com/openai/swarm) | 🔴 **9.2** | 22.0k | ↗️ +13 | 0 | — | `experimental` |

## 📂 By Category

- `data-agent`: **LlamaIndex** (57.7)
- `enterprise`: **Semantic Kernel** (54.0)
- `experimental`: **Swarm** (9.2)
- `lightweight`: **Smolagents** (34.7)
- `memory`: **Letta** (36.6)
- `multi-agent`: **CrewAI** (76.8), **Agno** (71.5), **AG2** (69.1), **AutoGen** (32.0)
- `optimization`: **DSPy** (48.6)
- `orchestration`: **Claude Agent SDK** (83.0), **OpenAI Agents SDK** (75.7), **Google ADK** (73.1), **LangGraph** (60.8)
- `pipeline`: **Haystack** (71.3)
- `structured`: **PydanticAI** (73.9)
- `tooling`: **Composio** (66.3)
- `typescript`: **Mastra** (75.9)
- `web-agent`: **BrowserUse** (81.5)

## 🔍 Top 5 — Score Breakdown

| Framework | Star Velocity | Release Freshness | Issue Health | Commit Activity | Community | Fork Ratio |
|-----------|:---:|:---:|:---:|:---:|:---:|:---:|
| **Claude Agent SDK** | 100 | 100.0 | 85.8 | 85.0 | 11.4 | 69.4 |
| **BrowserUse** | 100 | 99.0 | 90.1 | 58.0 | 72.0 | 44.2 |
| **CrewAI** | 48.8 | 100.0 | 90.0 | 92.0 | 68.4 | 58.3 |
| **Mastra** | 33.4 | 99.3 | 95.3 | 100 | 93.4 | 41.1 |
| **OpenAI Agents SDK** | 27.0 | 97.7 | 99.2 | 100 | 80.2 | 64.9 |

## 💡 Key Insights

- **Hottest framework**: Claude Agent SDK with a Pulse Score of 83.0
- **Fastest growing**: Claude Agent SDK gained +950 stars this week
- **Most active development**: Mastra with 2288 commits in the last 4 weeks
- **Stale releases**: AutoGen, Swarm haven't released in a while

## 📦 Recent Releases

- **CrewAI** [`1.15.27`](https://github.com/crewAIInc/crewAI/releases/tag/1.15.27) — today
- **Claude Agent SDK** [`v2.1.296`](https://github.com/anthropics/claude-code/releases/tag/v2.1.296) — today
- **Agno** [`v3.1.2`](https://github.com/agno-agi/agno/releases/tag/v3.1.2) — 1 day ago
- **Composio** [`@composio/cli@0.4.3-beta.418`](https://github.com/ComposioHQ/composio/releases/tag/@composio/cli@0.4.3-beta.418) — 1 day ago *(pre-release)*
- **Mastra** [`@mastra/core@1.75.0`](https://github.com/mastra-ai/mastra/releases/tag/@mastra/core@1.75.0) — 2 days ago
- **LangGraph** [`cli==0.4.33`](https://github.com/langchain-ai/langgraph/releases/tag/cli==0.4.33) — 2 days ago
- **BrowserUse** [`0.13.11`](https://github.com/browser-use/browser-use/releases/tag/0.13.11) — 3 days ago
- **Semantic Kernel** [`python-1.45.0`](https://github.com/microsoft/semantic-kernel/releases/tag/python-1.45.0) — 3 days ago
- **PydanticAI** [`clai2-bleeding`](https://github.com/pydantic/pydantic-ai/releases/tag/clai2-bleeding) — 4 days ago *(pre-release)*
- **AG2** [`v1.1.2`](https://github.com/ag2ai/ag2/releases/tag/v1.1.2) — 7 days ago

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

*Powered by GitHub Actions • Data refreshed daily • Last run: 2026-10-10 12:12 UTC*