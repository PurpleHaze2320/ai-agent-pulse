# 🔬 AI Agent Framework Pulse Tracker

[![Daily Update](https://github.com/PurpleHaze2320/ai-agent-pulse/actions/workflows/track.yml/badge.svg)](https://github.com/PurpleHaze2320/ai-agent-pulse/actions/workflows/track.yml)
[![Frameworks Tracked](https://img.shields.io/badge/frameworks-19-blue)](https://github.com/PurpleHaze2320/ai-agent-pulse)
[![License: MIT](https://img.shields.io/badge/License-MIT-green.svg)](https://opensource.org/licenses/MIT)
[![GitHub stars](https://img.shields.io/github/stars/PurpleHaze2320/ai-agent-pulse?style=social)](https://github.com/PurpleHaze2320/ai-agent-pulse/stargazers)

> Automated daily tracking of the AI agent framework ecosystem's health, momentum, and trends.
> Last updated: **2026-06-24 09:40 UTC** | Tracking **19** frameworks

## How It Works

This bot runs daily via GitHub Actions and collects metrics from the GitHub API for the most important
AI agent frameworks. It computes a **Pulse Score** (0-100) based on six weighted signals: star velocity,
release freshness, issue health, commit activity, community size, and fork engagement. The result is
a living dashboard that shows which frameworks are gaining momentum and which are losing steam.

## 🏆 Pulse Leaderboard

| Rank | Framework | Pulse | Stars | ⭐ 7d | Commits (4w) | Last Release | Category |
|------|-----------|-------|-------|-------|--------------|--------------|----------|
| 1 | [CrewAI](https://github.com/crewAIInc/crewAI) | 🟢 **91.0** | 54.3k | 🚀 +501 | 113 | today | `multi-agent` |
| 2 | [Mastra](https://github.com/mastra-ai/mastra) | 🟢 **79.5** | 25.4k | 🚀 +244 | 851 | 4 days ago | `typescript` |
| 3 | [LangGraph](https://github.com/langchain-ai/langgraph) | 🟢 **78.8** | 35.6k | 🚀 +602 | 54 | 5 days ago | `orchestration` |
| 4 | [PydanticAI](https://github.com/pydantic/pydantic-ai) | 🟢 **72.2** | 18.0k | 🚀 +157 | 86 | today | `structured` |
| 5 | [Google ADK](https://github.com/google/adk-python) | 🟢 **72.0** | 20.3k | 🚀 +121 | 274 | 5 days ago | `orchestration` |
| 6 | [Claude Agent SDK](https://github.com/anthropics/claude-code) | 🟢 **71.3** | 134.1k | 🚀 +1162 | 28 | today | `orchestration` |
| 7 | [Haystack](https://github.com/deepset-ai/haystack) | 🟡 **69.6** | 25.7k | 📈 +65 | 164 | 6 days ago | `pipeline` |
| 8 | [BrowserUse](https://github.com/browser-use/browser-use) | 🟡 **69.3** | 100.4k | 🚀 +1176 | 0 | 11 days ago | `web-agent` |
| 9 | [OpenAI Agents SDK](https://github.com/openai/openai-agents-python) | 🟡 **65.5** | 27.4k | 🚀 +187 | 48 | today | `orchestration` |
| 10 | [Composio](https://github.com/ComposioHQ/composio) | 🟡 **59.9** | 28.9k | 🚀 +113 | 63 | 3 days ago | `tooling` |
| 11 | [LlamaIndex](https://github.com/run-llama/llama_index) | 🟡 **57.2** | 50.3k | 🚀 +152 | 9 | 1 mo ago | `data-agent` |
| 12 | [DSPy](https://github.com/stanfordnlp/dspy) | 🟡 **57.2** | 35.3k | 🚀 +257 | 18 | 27 days ago | `optimization` |
| 13 | [Semantic Kernel](https://github.com/microsoft/semantic-kernel) | 🟡 **56.0** | 28.2k | 📈 +34 | 27 | 7 days ago | `enterprise` |
| 14 | [Agno](https://github.com/agno-agi/agno) | 🟡 **51.4** | 40.8k | 📈 +89 | 0 | today | `multi-agent` |
| 15 | [AG2](https://github.com/ag2ai/ag2) | 🟡 **48.1** | 4.7k | 📈 +27 | 0 | 11 days ago | `multi-agent` |
| 16 | [Letta](https://github.com/letta-ai/letta) | 🟡 **45.2** | 23.5k | 🚀 +121 | 0 | 1 mo ago | `memory` |
| 17 | [Smolagents](https://github.com/huggingface/smolagents) | 🟡 **41.9** | 28.0k | 📈 +98 | 2 | 26 days ago | `lightweight` |
| 18 | [AutoGen](https://github.com/microsoft/autogen) | 🟠 **38.4** | 59.2k | 🚀 +168 | 0 | 8 mo ago | `multi-agent` |
| 19 | [Swarm](https://github.com/openai/swarm) | 🔴 **10.4** | 21.7k | 📈 +69 | 0 | — | `experimental` |

## 📂 By Category

- `data-agent`: **LlamaIndex** (57.2)
- `enterprise`: **Semantic Kernel** (56.0)
- `experimental`: **Swarm** (10.4)
- `lightweight`: **Smolagents** (41.9)
- `memory`: **Letta** (45.2)
- `multi-agent`: **CrewAI** (91.0), **Agno** (51.4), **AG2** (48.1), **AutoGen** (38.4)
- `optimization`: **DSPy** (57.2)
- `orchestration`: **LangGraph** (78.8), **Google ADK** (72.0), **Claude Agent SDK** (71.3), **OpenAI Agents SDK** (65.5)
- `pipeline`: **Haystack** (69.6)
- `structured`: **PydanticAI** (72.2)
- `tooling`: **Composio** (59.9)
- `typescript`: **Mastra** (79.5)
- `web-agent`: **BrowserUse** (69.3)

## 🔍 Top 5 — Score Breakdown

| Framework | Star Velocity | Release Freshness | Issue Health | Commit Activity | Community | Fork Ratio |
|-----------|:---:|:---:|:---:|:---:|:---:|:---:|
| **CrewAI** | 100 | 100.0 | 96.3 | 100 | 59.4 | 56.0 |
| **Mastra** | 51.0 | 98.7 | 95.1 | 100 | 91.8 | 35.9 |
| **LangGraph** | 100 | 98.3 | 74.5 | 54.0 | 55.0 | 67.0 |
| **PydanticAI** | 32.3 | 100.0 | 82.7 | 86.0 | 95.4 | 50.1 |
| **Google ADK** | 23.4 | 98.3 | 84.3 | 100 | 67.0 | 71.3 |

## 💡 Key Insights

- **Hottest framework**: CrewAI with a Pulse Score of 91.0
- **Fastest growing**: BrowserUse gained +1176 stars this week
- **Most active development**: Mastra with 851 commits in the last 4 weeks
- **Stale releases**: Swarm haven't released in a while

## 📦 Recent Releases

- **OpenAI Agents SDK** [`v0.17.7`](https://github.com/openai/openai-agents-python/releases/tag/v0.17.7) — today
- **CrewAI** [`1.14.8a3`](https://github.com/crewAIInc/crewAI/releases/tag/1.14.8a3) — today *(pre-release)*
- **Claude Agent SDK** [`v2.1.187`](https://github.com/anthropics/claude-code/releases/tag/v2.1.187) — today
- **PydanticAI** [`v2.0.0`](https://github.com/pydantic/pydantic-ai/releases/tag/v2.0.0) — today
- **Agno** [`v2.6.19`](https://github.com/agno-agi/agno/releases/tag/v2.6.19) — today
- **Composio** [`@composio/cli@0.2.32-beta.270`](https://github.com/ComposioHQ/composio/releases/tag/@composio/cli@0.2.32-beta.270) — 3 days ago *(pre-release)*
- **Mastra** [`@mastra/core@1.45.0`](https://github.com/mastra-ai/mastra/releases/tag/@mastra/core@1.45.0) — 4 days ago
- **LangGraph** [`1.2.6`](https://github.com/langchain-ai/langgraph/releases/tag/1.2.6) — 5 days ago
- **Google ADK** [`v2.3.0`](https://github.com/google/adk-python/releases/tag/v2.3.0) — 5 days ago
- **Haystack** [`v2.30.2`](https://github.com/deepset-ai/haystack/releases/tag/v2.30.2) — 6 days ago

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

*Powered by GitHub Actions • Data refreshed daily • Last run: 2026-06-24 09:40 UTC*