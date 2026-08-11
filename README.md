# 🔬 AI Agent Framework Pulse Tracker

[![Daily Update](https://github.com/PurpleHaze2320/ai-agent-pulse/actions/workflows/track.yml/badge.svg)](https://github.com/PurpleHaze2320/ai-agent-pulse/actions/workflows/track.yml)
[![Frameworks Tracked](https://img.shields.io/badge/frameworks-19-blue)](https://github.com/PurpleHaze2320/ai-agent-pulse)
[![License: MIT](https://img.shields.io/badge/License-MIT-green.svg)](https://opensource.org/licenses/MIT)
[![GitHub stars](https://img.shields.io/github/stars/PurpleHaze2320/ai-agent-pulse?style=social)](https://github.com/PurpleHaze2320/ai-agent-pulse/stargazers)

> Automated daily tracking of the AI agent framework ecosystem's health, momentum, and trends.
> Last updated: **2026-08-11 07:15 UTC** | Tracking **19** frameworks

## How It Works

This bot runs daily via GitHub Actions and collects metrics from the GitHub API for the most important
AI agent frameworks. It computes a **Pulse Score** (0-100) based on six weighted signals: star velocity,
release freshness, issue health, commit activity, community size, and fork engagement. The result is
a living dashboard that shows which frameworks are gaining momentum and which are losing steam.

## 🏆 Pulse Leaderboard

| Rank | Framework | Pulse | Stars | ⭐ 7d | Commits (4w) | Last Release | Category |
|------|-----------|-------|-------|-------|--------------|--------------|----------|
| 1 | [BrowserUse](https://github.com/browser-use/browser-use) | 🟢 **89.2** | 108.7k | 🚀 +904 | 147 | 14 days ago | `web-agent` |
| 2 | [Mastra](https://github.com/mastra-ai/mastra) | 🟢 **78.5** | 27.1k | 🚀 +202 | 1292 | today | `typescript` |
| 3 | [CrewAI](https://github.com/crewAIInc/crewAI) | 🟢 **77.7** | 56.9k | 🚀 +328 | 73 | 2 days ago | `multi-agent` |
| 4 | [LangGraph](https://github.com/langchain-ai/langgraph) | 🟢 **75.3** | 39.4k | 🚀 +589 | 38 | 3 days ago | `orchestration` |
| 5 | [Haystack](https://github.com/deepset-ai/haystack) | 🟡 **69.6** | 26.2k | 📈 +67 | 178 | 21 days ago | `pipeline` |
| 6 | [Claude Agent SDK](https://github.com/anthropics/claude-code) | 🟡 **67.8** | 141.0k | 🚀 +815 | 15 | today | `orchestration` |
| 7 | [Composio](https://github.com/ComposioHQ/composio) | 🟡 **67.5** | 29.6k | 📈 +100 | 253 | today | `tooling` |
| 8 | [Agno](https://github.com/agno-agi/agno) | 🟡 **64.8** | 41.7k | 📈 +91 | 69 | 4 days ago | `multi-agent` |
| 9 | [DSPy](https://github.com/stanfordnlp/dspy) | 🟡 **63.1** | 37.1k | 🚀 +456 | 0 | 7 days ago | `optimization` |
| 10 | [LlamaIndex](https://github.com/run-llama/llama_index) | 🟡 **61.5** | 51.6k | 🚀 +187 | 25 | 1 mo ago | `data-agent` |
| 11 | [OpenAI Agents SDK](https://github.com/openai/openai-agents-python) | 🟡 **56.7** | 28.6k | 🚀 +175 | 0 | today | `orchestration` |
| 12 | [PydanticAI](https://github.com/pydantic/pydantic-ai) | 🟡 **55.9** | 19.2k | 🚀 +165 | 0 | today | `structured` |
| 13 | [Semantic Kernel](https://github.com/microsoft/semantic-kernel) | 🟡 **54.2** | 28.4k | 📈 +29 | 18 | 4 days ago | `enterprise` |
| 14 | [Google ADK](https://github.com/google/adk-python) | 🟡 **53.0** | 21.1k | 📈 +73 | 0 | 3 days ago | `orchestration` |
| 15 | [AG2](https://github.com/ag2ai/ag2) | 🟡 **49.2** | 4.8k | ↗️ +17 | 0 | 13 days ago | `multi-agent` |
| 16 | [Letta](https://github.com/letta-ai/letta) | 🟡 **41.5** | 24.2k | 🚀 +102 | 2 | 2 mo ago | `memory` |
| 17 | [Smolagents](https://github.com/huggingface/smolagents) | 🟠 **37.7** | 28.8k | 📈 +90 | 0 | 2 mo ago | `lightweight` |
| 18 | [AutoGen](https://github.com/microsoft/autogen) | 🟠 **34.7** | 60.4k | 🚀 +141 | 0 | 10 mo ago | `multi-agent` |
| 19 | [Swarm](https://github.com/openai/swarm) | 🔴 **9.6** | 21.9k | ↗️ +18 | 0 | — | `experimental` |

## 📂 By Category

- `data-agent`: **LlamaIndex** (61.5)
- `enterprise`: **Semantic Kernel** (54.2)
- `experimental`: **Swarm** (9.6)
- `lightweight`: **Smolagents** (37.7)
- `memory`: **Letta** (41.5)
- `multi-agent`: **CrewAI** (77.7), **Agno** (64.8), **AG2** (49.2), **AutoGen** (34.7)
- `optimization`: **DSPy** (63.1)
- `orchestration`: **LangGraph** (75.3), **Claude Agent SDK** (67.8), **OpenAI Agents SDK** (56.7), **Google ADK** (53.0)
- `pipeline`: **Haystack** (69.6)
- `structured`: **PydanticAI** (55.9)
- `tooling`: **Composio** (67.5)
- `typescript`: **Mastra** (78.5)
- `web-agent`: **BrowserUse** (89.2)

## 🔍 Top 5 — Score Breakdown

| Framework | Star Velocity | Release Freshness | Issue Health | Commit Activity | Community | Fork Ratio |
|-----------|:---:|:---:|:---:|:---:|:---:|:---:|
| **BrowserUse** | 100 | 95.3 | 93.9 | 100 | 66.6 | 44.0 |
| **Mastra** | 43.8 | 100.0 | 96.0 | 100 | 92.6 | 38.5 |
| **CrewAI** | 69.2 | 99.3 | 95.3 | 73.0 | 59.8 | 57.1 |
| **LangGraph** | 100 | 99.0 | 70.6 | 38.0 | 55.4 | 67.2 |
| **Haystack** | 13.9 | 93.0 | 98.5 | 100 | 81.8 | 45.7 |

## 💡 Key Insights

- **Hottest framework**: BrowserUse with a Pulse Score of 89.2
- **Fastest growing**: BrowserUse gained +904 stars this week
- **Most active development**: Mastra with 1292 commits in the last 4 weeks
- **Stale releases**: AutoGen, Swarm haven't released in a while

## 📦 Recent Releases

- **OpenAI Agents SDK** [`v0.20.0`](https://github.com/openai/openai-agents-python/releases/tag/v0.20.0) — today
- **PydanticAI** [`v2.27.1`](https://github.com/pydantic/pydantic-ai/releases/tag/v2.27.1) — today
- **Claude Agent SDK** [`v2.1.227`](https://github.com/anthropics/claude-code/releases/tag/v2.1.227) — today
- **Composio** [`@composio/cli@0.3.3-beta.346`](https://github.com/ComposioHQ/composio/releases/tag/@composio/cli@0.3.3-beta.346) — today *(pre-release)*
- **Mastra** [`@mastra/core@1.57.0`](https://github.com/mastra-ai/mastra/releases/tag/@mastra/core@1.57.0) — today
- **CrewAI** [`1.15.14`](https://github.com/crewAIInc/crewAI/releases/tag/1.15.14) — 2 days ago
- **Google ADK** [`v2.6.3`](https://github.com/google/adk-python/releases/tag/v2.6.3) — 3 days ago
- **LangGraph** [`checkpointpostgres==3.1.2`](https://github.com/langchain-ai/langgraph/releases/tag/checkpointpostgres==3.1.2) — 3 days ago
- **Agno** [`v3.0.0a1`](https://github.com/agno-agi/agno/releases/tag/v3.0.0a1) — 4 days ago *(pre-release)*
- **Semantic Kernel** [`python-1.44.1`](https://github.com/microsoft/semantic-kernel/releases/tag/python-1.44.1) — 4 days ago

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

*Powered by GitHub Actions • Data refreshed daily • Last run: 2026-08-11 07:15 UTC*