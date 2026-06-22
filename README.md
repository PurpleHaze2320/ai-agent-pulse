# 🔬 AI Agent Framework Pulse Tracker

[![Daily Update](https://github.com/PurpleHaze2320/ai-agent-pulse/actions/workflows/track.yml/badge.svg)](https://github.com/PurpleHaze2320/ai-agent-pulse/actions/workflows/track.yml)
[![Frameworks Tracked](https://img.shields.io/badge/frameworks-19-blue)](https://github.com/PurpleHaze2320/ai-agent-pulse)
[![License: MIT](https://img.shields.io/badge/License-MIT-green.svg)](https://opensource.org/licenses/MIT)
[![GitHub stars](https://img.shields.io/github/stars/PurpleHaze2320/ai-agent-pulse?style=social)](https://github.com/PurpleHaze2320/ai-agent-pulse/stargazers)

> Automated daily tracking of the AI agent framework ecosystem's health, momentum, and trends.
> Last updated: **2026-06-22 12:14 UTC** | Tracking **19** frameworks

## How It Works

This bot runs daily via GitHub Actions and collects metrics from the GitHub API for the most important
AI agent frameworks. It computes a **Pulse Score** (0-100) based on six weighted signals: star velocity,
release freshness, issue health, commit activity, community size, and fork engagement. The result is
a living dashboard that shows which frameworks are gaining momentum and which are losing steam.

## 🏆 Pulse Leaderboard

| Rank | Framework | Pulse | Stars | ⭐ 7d | Commits (4w) | Last Release | Category |
|------|-----------|-------|-------|-------|--------------|--------------|----------|
| 1 | [CrewAI](https://github.com/crewAIInc/crewAI) | 🟢 **90.8** | 54.1k | 🚀 +528 | 101 | 3 days ago | `multi-agent` |
| 2 | [BrowserUse](https://github.com/browser-use/browser-use) | 🟢 **89.5** | 100.1k | 🚀 +1144 | 409 | 9 days ago | `web-agent` |
| 3 | [Mastra](https://github.com/mastra-ai/mastra) | 🟢 **79.2** | 25.3k | 🚀 +234 | 722 | 2 days ago | `typescript` |
| 4 | [LangGraph](https://github.com/langchain-ai/langgraph) | 🟢 **78.8** | 35.4k | 🚀 +622 | 53 | 3 days ago | `orchestration` |
| 5 | [Google ADK](https://github.com/google/adk-python) | 🟢 **71.5** | 20.2k | 🚀 +109 | 245 | 3 days ago | `orchestration` |
| 6 | [Claude Agent SDK](https://github.com/anthropics/claude-code) | 🟢 **70.9** | 133.7k | 🚀 +1217 | 26 | 1 day ago | `orchestration` |
| 7 | [Haystack](https://github.com/deepset-ai/haystack) | 🟡 **69.3** | 25.6k | 📈 +57 | 142 | 4 days ago | `pipeline` |
| 8 | [Agno](https://github.com/agno-agi/agno) | 🟡 **67.9** | 40.8k | 🚀 +109 | 80 | 3 days ago | `multi-agent` |
| 9 | [PydanticAI](https://github.com/pydantic/pydantic-ai) | 🟡 **66.7** | 17.9k | 🚀 +142 | 65 | 11 days ago | `structured` |
| 10 | [OpenAI Agents SDK](https://github.com/openai/openai-agents-python) | 🟡 **62.7** | 27.3k | 🚀 +163 | 40 | 3 days ago | `orchestration` |
| 11 | [Composio](https://github.com/ComposioHQ/composio) | 🟡 **59.2** | 28.9k | 🚀 +120 | 58 | 1 day ago | `tooling` |
| 12 | [AG2](https://github.com/ag2ai/ag2) | 🟡 **57.1** | 4.7k | 📈 +23 | 45 | 9 days ago | `multi-agent` |
| 13 | [Semantic Kernel](https://github.com/microsoft/semantic-kernel) | 🟡 **56.7** | 28.2k | 📈 +54 | 26 | 5 days ago | `enterprise` |
| 14 | [LlamaIndex](https://github.com/run-llama/llama_index) | 🟡 **56.6** | 50.3k | 🚀 +136 | 9 | 1 mo ago | `data-agent` |
| 15 | [DSPy](https://github.com/stanfordnlp/dspy) | 🟡 **56.6** | 35.3k | 🚀 +238 | 18 | 25 days ago | `optimization` |
| 16 | [Letta](https://github.com/letta-ai/letta) | 🟡 **45.1** | 23.5k | 🚀 +115 | 0 | 1 mo ago | `memory` |
| 17 | [Smolagents](https://github.com/huggingface/smolagents) | 🟡 **41.3** | 28.0k | 📈 +89 | 0 | 24 days ago | `lightweight` |
| 18 | [AutoGen](https://github.com/microsoft/autogen) | 🟠 **38.7** | 59.1k | 🚀 +172 | 0 | 8 mo ago | `multi-agent` |
| 19 | [Swarm](https://github.com/openai/swarm) | 🔴 **8.8** | 21.7k | 📈 +27 | 0 | — | `experimental` |

## 📂 By Category

- `data-agent`: **LlamaIndex** (56.6)
- `enterprise`: **Semantic Kernel** (56.7)
- `experimental`: **Swarm** (8.8)
- `lightweight`: **Smolagents** (41.3)
- `memory`: **Letta** (45.1)
- `multi-agent`: **CrewAI** (90.8), **Agno** (67.9), **AG2** (57.1), **AutoGen** (38.7)
- `optimization`: **DSPy** (56.6)
- `orchestration`: **LangGraph** (78.8), **Google ADK** (71.5), **Claude Agent SDK** (70.9), **OpenAI Agents SDK** (62.7)
- `pipeline`: **Haystack** (69.3)
- `structured`: **PydanticAI** (66.7)
- `tooling`: **Composio** (59.2)
- `typescript`: **Mastra** (79.2)
- `web-agent`: **BrowserUse** (89.5)

## 🔍 Top 5 — Score Breakdown

| Framework | Star Velocity | Release Freshness | Issue Health | Commit Activity | Community | Fork Ratio |
|-----------|:---:|:---:|:---:|:---:|:---:|:---:|
| **CrewAI** | 100 | 99.0 | 96.6 | 100 | 59.4 | 56.0 |
| **BrowserUse** | 100 | 97.0 | 95.4 | 100 | 63.0 | 44.6 |
| **Mastra** | 49.3 | 99.3 | 94.9 | 100 | 91.8 | 35.9 |
| **LangGraph** | 100 | 99.0 | 74.5 | 53.0 | 55.0 | 67.1 |
| **Google ADK** | 21.3 | 99.0 | 84.4 | 100 | 65.6 | 71.2 |

## 💡 Key Insights

- **Hottest framework**: CrewAI with a Pulse Score of 90.8
- **Fastest growing**: Claude Agent SDK gained +1217 stars this week
- **Most active development**: Mastra with 722 commits in the last 4 weeks
- **Stale releases**: Swarm haven't released in a while

## 📦 Recent Releases

- **Composio** [`@composio/cli@0.2.32-beta.270`](https://github.com/ComposioHQ/composio/releases/tag/@composio/cli@0.2.32-beta.270) — 1 day ago *(pre-release)*
- **Claude Agent SDK** [`v2.1.185`](https://github.com/anthropics/claude-code/releases/tag/v2.1.185) — 1 day ago
- **Mastra** [`@mastra/core@1.45.0`](https://github.com/mastra-ai/mastra/releases/tag/@mastra/core@1.45.0) — 2 days ago
- **OpenAI Agents SDK** [`v0.17.6`](https://github.com/openai/openai-agents-python/releases/tag/v0.17.6) — 3 days ago
- **CrewAI** [`1.14.8a2`](https://github.com/crewAIInc/crewAI/releases/tag/1.14.8a2) — 3 days ago *(pre-release)*
- **LangGraph** [`1.2.6`](https://github.com/langchain-ai/langgraph/releases/tag/1.2.6) — 3 days ago
- **Agno** [`v2.6.18`](https://github.com/agno-agi/agno/releases/tag/v2.6.18) — 3 days ago
- **Google ADK** [`v2.3.0`](https://github.com/google/adk-python/releases/tag/v2.3.0) — 3 days ago
- **Haystack** [`v2.30.2`](https://github.com/deepset-ai/haystack/releases/tag/v2.30.2) — 4 days ago
- **Semantic Kernel** [`python-1.43.1`](https://github.com/microsoft/semantic-kernel/releases/tag/python-1.43.1) — 5 days ago

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

*Powered by GitHub Actions • Data refreshed daily • Last run: 2026-06-22 12:14 UTC*