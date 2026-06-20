# 🔬 AI Agent Framework Pulse Tracker

[![Daily Update](https://github.com/PurpleHaze2320/ai-agent-pulse/actions/workflows/track.yml/badge.svg)](https://github.com/PurpleHaze2320/ai-agent-pulse/actions/workflows/track.yml)
[![Frameworks Tracked](https://img.shields.io/badge/frameworks-19-blue)](https://github.com/PurpleHaze2320/ai-agent-pulse)
[![License: MIT](https://img.shields.io/badge/License-MIT-green.svg)](https://opensource.org/licenses/MIT)
[![GitHub stars](https://img.shields.io/github/stars/PurpleHaze2320/ai-agent-pulse?style=social)](https://github.com/PurpleHaze2320/ai-agent-pulse/stargazers)

> Automated daily tracking of the AI agent framework ecosystem's health, momentum, and trends.
> Last updated: **2026-06-20 09:26 UTC** | Tracking **19** frameworks

## How It Works

This bot runs daily via GitHub Actions and collects metrics from the GitHub API for the most important
AI agent frameworks. It computes a **Pulse Score** (0-100) based on six weighted signals: star velocity,
release freshness, issue health, commit activity, community size, and fork engagement. The result is
a living dashboard that shows which frameworks are gaining momentum and which are losing steam.

## 🏆 Pulse Leaderboard

| Rank | Framework | Pulse | Stars | ⭐ 7d | Commits (4w) | Last Release | Category |
|------|-----------|-------|-------|-------|--------------|--------------|----------|
| 1 | [CrewAI](https://github.com/crewAIInc/crewAI) | 🟢 **91.0** | 54.0k | 🚀 +607 | 124 | 1 day ago | `multi-agent` |
| 2 | [BrowserUse](https://github.com/browser-use/browser-use) | 🟢 **89.6** | 99.7k | 🚀 +1100 | 408 | 7 days ago | `web-agent` |
| 3 | [LangGraph](https://github.com/langchain-ai/langgraph) | 🟢 **84.7** | 35.3k | 🚀 +659 | 82 | 1 day ago | `orchestration` |
| 4 | [Mastra](https://github.com/mastra-ai/mastra) | 🟢 **80.3** | 25.3k | 🚀 +262 | 892 | today | `typescript` |
| 5 | [Claude Agent SDK](https://github.com/anthropics/claude-code) | 🟢 **72.2** | 133.4k | 🚀 +1268 | 33 | 1 day ago | `orchestration` |
| 6 | [Agno](https://github.com/agno-agi/agno) | 🟢 **72.0** | 40.8k | 🚀 +104 | 112 | 1 day ago | `multi-agent` |
| 7 | [Google ADK](https://github.com/google/adk-python) | 🟢 **71.2** | 20.2k | 📈 +97 | 288 | 1 day ago | `orchestration` |
| 8 | [Haystack](https://github.com/deepset-ai/haystack) | 🟡 **69.5** | 25.6k | 📈 +56 | 159 | 2 days ago | `pipeline` |
| 9 | [PydanticAI](https://github.com/pydantic/pydantic-ai) | 🟡 **69.0** | 17.9k | 🚀 +131 | 78 | 9 days ago | `structured` |
| 10 | [OpenAI Agents SDK](https://github.com/openai/openai-agents-python) | 🟡 **60.8** | 27.3k | 🚀 +158 | 32 | 1 day ago | `orchestration` |
| 11 | [LlamaIndex](https://github.com/run-llama/llama_index) | 🟡 **59.7** | 50.2k | 🚀 +132 | 24 | 1 mo ago | `data-agent` |
| 12 | [Composio](https://github.com/ComposioHQ/composio) | 🟡 **59.6** | 28.9k | 🚀 +123 | 59 | today | `tooling` |
| 13 | [DSPy](https://github.com/stanfordnlp/dspy) | 🟡 **57.7** | 35.2k | 🚀 +162 | 38 | 23 days ago | `optimization` |
| 14 | [Semantic Kernel](https://github.com/microsoft/semantic-kernel) | 🟡 **57.5** | 28.2k | 📈 +56 | 29 | 3 days ago | `enterprise` |
| 15 | [AG2](https://github.com/ag2ai/ag2) | 🟡 **48.3** | 4.7k | 📈 +25 | 0 | 7 days ago | `multi-agent` |
| 16 | [Letta](https://github.com/letta-ai/letta) | 🟡 **45.4** | 23.4k | 🚀 +118 | 0 | 1 mo ago | `memory` |
| 17 | [Smolagents](https://github.com/huggingface/smolagents) | 🟡 **43.1** | 27.9k | 🚀 +104 | 5 | 22 days ago | `lightweight` |
| 18 | [AutoGen](https://github.com/microsoft/autogen) | 🟠 **38.8** | 59.1k | 🚀 +169 | 0 | 8 mo ago | `multi-agent` |
| 19 | [Swarm](https://github.com/openai/swarm) | 🔴 **9.1** | 21.7k | 📈 +31 | 0 | — | `experimental` |

## 📂 By Category

- `data-agent`: **LlamaIndex** (59.7)
- `enterprise`: **Semantic Kernel** (57.5)
- `experimental`: **Swarm** (9.1)
- `lightweight`: **Smolagents** (43.1)
- `memory`: **Letta** (45.4)
- `multi-agent`: **CrewAI** (91.0), **Agno** (72.0), **AG2** (48.3), **AutoGen** (38.8)
- `optimization`: **DSPy** (57.7)
- `orchestration`: **LangGraph** (84.7), **Claude Agent SDK** (72.2), **Google ADK** (71.2), **OpenAI Agents SDK** (60.8)
- `pipeline`: **Haystack** (69.5)
- `structured`: **PydanticAI** (69.0)
- `tooling`: **Composio** (59.6)
- `typescript`: **Mastra** (80.3)
- `web-agent`: **BrowserUse** (89.6)

## 🔍 Top 5 — Score Breakdown

| Framework | Star Velocity | Release Freshness | Issue Health | Commit Activity | Community | Fork Ratio |
|-----------|:---:|:---:|:---:|:---:|:---:|:---:|
| **CrewAI** | 100 | 99.7 | 96.6 | 100 | 59.4 | 56.0 |
| **BrowserUse** | 100 | 97.7 | 95.4 | 100 | 63.0 | 44.6 |
| **LangGraph** | 100 | 99.7 | 74.6 | 82.0 | 55.0 | 67.1 |
| **Mastra** | 53.5 | 100.0 | 94.7 | 100 | 91.8 | 35.7 |
| **Claude Agent SDK** | 100 | 99.7 | 87.7 | 33.0 | 10.4 | 64.7 |

## 💡 Key Insights

- **Hottest framework**: CrewAI with a Pulse Score of 91.0
- **Fastest growing**: Claude Agent SDK gained +1268 stars this week
- **Most active development**: Mastra with 892 commits in the last 4 weeks
- **Stale releases**: Swarm haven't released in a while

## 📦 Recent Releases

- **Mastra** [`@mastra/core@1.45.0`](https://github.com/mastra-ai/mastra/releases/tag/@mastra/core@1.45.0) — today
- **Composio** [`@composio/vercel@0.9.3`](https://github.com/ComposioHQ/composio/releases/tag/@composio/vercel@0.9.3) — today
- **OpenAI Agents SDK** [`v0.17.6`](https://github.com/openai/openai-agents-python/releases/tag/v0.17.6) — 1 day ago
- **Claude Agent SDK** [`v2.1.183`](https://github.com/anthropics/claude-code/releases/tag/v2.1.183) — 1 day ago
- **CrewAI** [`1.14.8a2`](https://github.com/crewAIInc/crewAI/releases/tag/1.14.8a2) — 1 day ago *(pre-release)*
- **LangGraph** [`1.2.6`](https://github.com/langchain-ai/langgraph/releases/tag/1.2.6) — 1 day ago
- **Agno** [`v2.6.18`](https://github.com/agno-agi/agno/releases/tag/v2.6.18) — 1 day ago
- **Google ADK** [`v2.3.0`](https://github.com/google/adk-python/releases/tag/v2.3.0) — 1 day ago
- **Haystack** [`v2.30.2`](https://github.com/deepset-ai/haystack/releases/tag/v2.30.2) — 2 days ago
- **Semantic Kernel** [`python-1.43.1`](https://github.com/microsoft/semantic-kernel/releases/tag/python-1.43.1) — 3 days ago

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

*Powered by GitHub Actions • Data refreshed daily • Last run: 2026-06-20 09:26 UTC*