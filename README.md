# 🔬 AI Agent Framework Pulse Tracker

[![Daily Update](https://github.com/PurpleHaze2320/ai-agent-pulse/actions/workflows/track.yml/badge.svg)](https://github.com/PurpleHaze2320/ai-agent-pulse/actions/workflows/track.yml)
[![Frameworks Tracked](https://img.shields.io/badge/frameworks-19-blue)](https://github.com/PurpleHaze2320/ai-agent-pulse)
[![License: MIT](https://img.shields.io/badge/License-MIT-green.svg)](https://opensource.org/licenses/MIT)
[![GitHub stars](https://img.shields.io/github/stars/PurpleHaze2320/ai-agent-pulse?style=social)](https://github.com/PurpleHaze2320/ai-agent-pulse/stargazers)

> Automated daily tracking of the AI agent framework ecosystem's health, momentum, and trends.
> Last updated: **2026-05-19 09:56 UTC** | Tracking **19** frameworks

## How It Works

This bot runs daily via GitHub Actions and collects metrics from the GitHub API for the most important
AI agent frameworks. It computes a **Pulse Score** (0-100) based on six weighted signals: star velocity,
release freshness, issue health, commit activity, community size, and fork engagement. The result is
a living dashboard that shows which frameworks are gaining momentum and which are losing steam.

## 🏆 Pulse Leaderboard

| Rank | Framework | Pulse | Stars | ⭐ 7d | Commits (4w) | Last Release | Category |
|------|-----------|-------|-------|-------|--------------|--------------|----------|
| 1 | [Mastra](https://github.com/mastra-ai/mastra) | 🟢 **77.8** | 24.0k | 🚀 +231 | 870 | today | `typescript` |
| 2 | [CrewAI](https://github.com/crewAIInc/crewAI) | 🟢 **71.2** | 51.7k | 🚀 +484 | 0 | today | `multi-agent` |
| 3 | [BrowserUse](https://github.com/browser-use/browser-use) | 🟢 **70.2** | 94.6k | 🚀 +1094 | 0 | today | `web-agent` |
| 4 | [OpenAI Agents SDK](https://github.com/openai/openai-agents-python) | 🟡 **69.1** | 26.5k | 🚀 +241 | 0 | today | `orchestration` |
| 5 | [LangGraph](https://github.com/langchain-ai/langgraph) | 🟡 **68.3** | 32.4k | 🚀 +567 | 0 | 7 days ago | `orchestration` |
| 6 | [Claude Agent SDK](https://github.com/anthropics/claude-code) | 🟡 **64.8** | 124.8k | 🚀 +2093 | 0 | today | `orchestration` |
| 7 | [LlamaIndex](https://github.com/run-llama/llama_index) | 🟡 **58.0** | 49.5k | 🚀 +147 | 0 | 4 days ago | `data-agent` |
| 8 | [PydanticAI](https://github.com/pydantic/pydantic-ai) | 🟡 **53.2** | 17.1k | 🚀 +126 | 0 | today | `structured` |
| 9 | [Agno](https://github.com/agno-agi/agno) | 🟡 **53.2** | 40.2k | 🚀 +136 | 0 | 3 days ago | `multi-agent` |
| 10 | [DSPy](https://github.com/stanfordnlp/dspy) | 🟡 **51.6** | 34.5k | 🚀 +175 | 0 | 13 days ago | `optimization` |
| 11 | [Google ADK](https://github.com/google/adk-python) | 🟡 **51.5** | 19.7k | 🚀 +129 | 0 | today | `orchestration` |
| 12 | [Haystack](https://github.com/deepset-ai/haystack) | 🟡 **50.8** | 25.3k | 🚀 +105 | 0 | 6 days ago | `pipeline` |
| 13 | [Semantic Kernel](https://github.com/microsoft/semantic-kernel) | 🟡 **50.8** | 27.9k | 📈 +40 | 0 | 5 days ago | `enterprise` |
| 14 | [Composio](https://github.com/ComposioHQ/composio) | 🟡 **49.5** | 28.3k | 🚀 +162 | 0 | today | `tooling` |
| 15 | [Letta](https://github.com/letta-ai/letta) | 🟡 **49.1** | 22.8k | 🚀 +153 | 0 | 4 days ago | `memory` |
| 16 | [AG2](https://github.com/ag2ai/ag2) | 🟡 **49.0** | 4.6k | 📈 +41 | 0 | 6 days ago | `multi-agent` |
| 17 | [Smolagents](https://github.com/huggingface/smolagents) | 🟡 **45.2** | 27.4k | 🚀 +143 | 0 | 4 days ago | `lightweight` |
| 18 | [AutoGen](https://github.com/microsoft/autogen) | 🟡 **42.9** | 58.2k | 🚀 +210 | 0 | 7 mo ago | `multi-agent` |
| 19 | [Swarm](https://github.com/openai/swarm) | 🔴 **9.1** | 21.5k | 📈 +30 | 0 | — | `experimental` |

## 📂 By Category

- `data-agent`: **LlamaIndex** (58.0)
- `enterprise`: **Semantic Kernel** (50.8)
- `experimental`: **Swarm** (9.1)
- `lightweight`: **Smolagents** (45.2)
- `memory`: **Letta** (49.1)
- `multi-agent`: **CrewAI** (71.2), **Agno** (53.2), **AG2** (49.0), **AutoGen** (42.9)
- `optimization`: **DSPy** (51.6)
- `orchestration`: **OpenAI Agents SDK** (69.1), **LangGraph** (68.3), **Claude Agent SDK** (64.8), **Google ADK** (51.5)
- `pipeline`: **Haystack** (50.8)
- `structured`: **PydanticAI** (53.2)
- `tooling`: **Composio** (49.5)
- `typescript`: **Mastra** (77.8)
- `web-agent`: **BrowserUse** (70.2)

## 🔍 Top 5 — Score Breakdown

| Framework | Star Velocity | Release Freshness | Issue Health | Commit Activity | Community | Fork Ratio |
|-----------|:---:|:---:|:---:|:---:|:---:|:---:|
| **Mastra** | 45.5 | 100.0 | 94.6 | 100 | 87.2 | 34.8 |
| **CrewAI** | 100 | 100.0 | 98.3 | 0.0 | 59.4 | 55.4 |
| **BrowserUse** | 100 | 100.0 | 96.1 | 0.0 | 62.8 | 45.1 |
| **OpenAI Agents SDK** | 92.1 | 100.0 | 96.2 | 0.0 | 54.6 | 61.4 |
| **LangGraph** | 100 | 97.7 | 76.8 | 0.0 | 54.6 | 67.8 |

## 💡 Key Insights

- **Hottest framework**: Mastra with a Pulse Score of 77.8
- **Fastest growing**: Claude Agent SDK gained +2093 stars this week
- **Most active development**: Mastra with 870 commits in the last 4 weeks
- **Stale releases**: Swarm haven't released in a while

## 📦 Recent Releases

- **Composio** [`@composio/cli@0.2.31-beta.255`](https://github.com/ComposioHQ/composio/releases/tag/@composio/cli@0.2.31-beta.255) — today *(pre-release)*
- **OpenAI Agents SDK** [`v0.17.3`](https://github.com/openai/openai-agents-python/releases/tag/v0.17.3) — today
- **BrowserUse** [`0.12.7`](https://github.com/browser-use/browser-use/releases/tag/0.12.7) — today
- **PydanticAI** [`v1.98.0`](https://github.com/pydantic/pydantic-ai/releases/tag/v1.98.0) — today
- **Claude Agent SDK** [`v2.1.144`](https://github.com/anthropics/claude-code/releases/tag/v2.1.144) — today
- **Google ADK** [`v1.34.0`](https://github.com/google/adk-python/releases/tag/v1.34.0) — today
- **CrewAI** [`1.14.5`](https://github.com/crewAIInc/crewAI/releases/tag/1.14.5) — today
- **Mastra** [`@mastra/core@1.35.0`](https://github.com/mastra-ai/mastra/releases/tag/@mastra/core@1.35.0) — today
- **Agno** [`v2.6.7`](https://github.com/agno-agi/agno/releases/tag/v2.6.7) — 3 days ago
- **LlamaIndex** [`v0.14.22`](https://github.com/run-llama/llama_index/releases/tag/v0.14.22) — 4 days ago

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

*Powered by GitHub Actions • Data refreshed daily • Last run: 2026-05-19 09:56 UTC*