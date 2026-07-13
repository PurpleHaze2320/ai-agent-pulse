# 🔬 AI Agent Framework Pulse Tracker

[![Daily Update](https://github.com/PurpleHaze2320/ai-agent-pulse/actions/workflows/track.yml/badge.svg)](https://github.com/PurpleHaze2320/ai-agent-pulse/actions/workflows/track.yml)
[![Frameworks Tracked](https://img.shields.io/badge/frameworks-19-blue)](https://github.com/PurpleHaze2320/ai-agent-pulse)
[![License: MIT](https://img.shields.io/badge/License-MIT-green.svg)](https://opensource.org/licenses/MIT)
[![GitHub stars](https://img.shields.io/github/stars/PurpleHaze2320/ai-agent-pulse?style=social)](https://github.com/PurpleHaze2320/ai-agent-pulse/stargazers)

> Automated daily tracking of the AI agent framework ecosystem's health, momentum, and trends.
> Last updated: **2026-07-13 09:37 UTC** | Tracking **19** frameworks

## How It Works

This bot runs daily via GitHub Actions and collects metrics from the GitHub API for the most important
AI agent frameworks. It computes a **Pulse Score** (0-100) based on six weighted signals: star velocity,
release freshness, issue health, commit activity, community size, and fork engagement. The result is
a living dashboard that shows which frameworks are gaining momentum and which are losing steam.

## 🏆 Pulse Leaderboard

| Rank | Framework | Pulse | Stars | ⭐ 7d | Commits (4w) | Last Release | Category |
|------|-----------|-------|-------|-------|--------------|--------------|----------|
| 1 | [BrowserUse](https://github.com/browser-use/browser-use) | 🟢 **84.1** | 104.5k | 🚀 +1444 | 71 | 1 day ago | `web-agent` |
| 2 | [CrewAI](https://github.com/crewAIInc/crewAI) | 🟢 **84.0** | 55.4k | 🚀 +423 | 80 | 5 days ago | `multi-agent` |
| 3 | [Mastra](https://github.com/mastra-ai/mastra) | 🟢 **80.4** | 26.1k | 🚀 +265 | 894 | 4 days ago | `typescript` |
| 4 | [LangGraph](https://github.com/langchain-ai/langgraph) | 🟢 **75.0** | 37.2k | 🚀 +541 | 35 | 3 days ago | `orchestration` |
| 5 | [Google ADK](https://github.com/google/adk-python) | 🟢 **72.1** | 20.6k | 📈 +92 | 266 | 5 days ago | `orchestration` |
| 6 | [Agno](https://github.com/agno-agi/agno) | 🟢 **71.7** | 41.1k | 🚀 +109 | 104 | 3 days ago | `multi-agent` |
| 7 | [Claude Agent SDK](https://github.com/anthropics/claude-code) | 🟡 **69.5** | 137.6k | 🚀 +1175 | 21 | 2 days ago | `orchestration` |
| 8 | [AG2](https://github.com/ag2ai/ag2) | 🟡 **61.6** | 4.8k | 📈 +21 | 60 | 9 days ago | `multi-agent` |
| 9 | [LlamaIndex](https://github.com/run-llama/llama_index) | 🟡 **61.3** | 50.8k | 🚀 +133 | 25 | 18 days ago | `data-agent` |
| 10 | [PydanticAI](https://github.com/pydantic/pydantic-ai) | 🟡 **57.9** | 18.5k | 🚀 +224 | 0 | 2 days ago | `structured` |
| 11 | [OpenAI Agents SDK](https://github.com/openai/openai-agents-python) | 🟡 **55.9** | 27.9k | 🚀 +179 | 0 | 2 days ago | `orchestration` |
| 12 | [DSPy](https://github.com/stanfordnlp/dspy) | 🟡 **52.4** | 36.1k | 🚀 +221 | 0 | 1 mo ago | `optimization` |
| 13 | [Semantic Kernel](https://github.com/microsoft/semantic-kernel) | 🟡 **50.8** | 28.3k | 📈 +35 | 0 | 6 days ago | `enterprise` |
| 14 | [Haystack](https://github.com/deepset-ai/haystack) | 🟡 **49.4** | 25.9k | 📈 +44 | 0 | 4 days ago | `pipeline` |
| 15 | [Composio](https://github.com/ComposioHQ/composio) | 🟡 **47.2** | 29.2k | 🚀 +106 | 0 | 5 days ago | `tooling` |
| 16 | [Letta](https://github.com/letta-ai/letta) | 🟡 **43.5** | 23.8k | 🚀 +102 | 2 | 1 mo ago | `memory` |
| 17 | [Smolagents](https://github.com/huggingface/smolagents) | 🟡 **41.3** | 28.3k | 🚀 +107 | 4 | 1 mo ago | `lightweight` |
| 18 | [AutoGen](https://github.com/microsoft/autogen) | 🟠 **37.1** | 59.7k | 🚀 +173 | 0 | 9 mo ago | `multi-agent` |
| 19 | [Swarm](https://github.com/openai/swarm) | 🔴 **9.3** | 21.8k | 📈 +26 | 0 | — | `experimental` |

## 📂 By Category

- `data-agent`: **LlamaIndex** (61.3)
- `enterprise`: **Semantic Kernel** (50.8)
- `experimental`: **Swarm** (9.3)
- `lightweight`: **Smolagents** (41.3)
- `memory`: **Letta** (43.5)
- `multi-agent`: **CrewAI** (84.0), **Agno** (71.7), **AG2** (61.6), **AutoGen** (37.1)
- `optimization`: **DSPy** (52.4)
- `orchestration`: **LangGraph** (75.0), **Google ADK** (72.1), **Claude Agent SDK** (69.5), **OpenAI Agents SDK** (55.9)
- `pipeline`: **Haystack** (49.4)
- `structured`: **PydanticAI** (57.9)
- `tooling`: **Composio** (47.2)
- `typescript`: **Mastra** (80.4)
- `web-agent`: **BrowserUse** (84.1)

## 🔍 Top 5 — Score Breakdown

| Framework | Star Velocity | Release Freshness | Issue Health | Commit Activity | Community | Fork Ratio |
|-----------|:---:|:---:|:---:|:---:|:---:|:---:|
| **BrowserUse** | 100 | 99.7 | 94.9 | 71.0 | 63.0 | 44.1 |
| **CrewAI** | 89.5 | 98.3 | 95.7 | 80.0 | 59.6 | 56.4 |
| **Mastra** | 53.9 | 98.7 | 94.9 | 100 | 92.6 | 36.9 |
| **LangGraph** | 100 | 99.0 | 73.0 | 35.0 | 55.0 | 67.2 |
| **Google ADK** | 20.2 | 98.3 | 86.1 | 100 | 72.8 | 71.7 |

## 💡 Key Insights

- **Hottest framework**: BrowserUse with a Pulse Score of 84.1
- **Fastest growing**: BrowserUse gained +1444 stars this week
- **Most active development**: Mastra with 894 commits in the last 4 weeks
- **Stale releases**: AutoGen, Swarm haven't released in a while

## 📦 Recent Releases

- **BrowserUse** [`0.13.4`](https://github.com/browser-use/browser-use/releases/tag/0.13.4) — 1 day ago
- **PydanticAI** [`v2.9.0`](https://github.com/pydantic/pydantic-ai/releases/tag/v2.9.0) — 2 days ago
- **OpenAI Agents SDK** [`v0.18.2`](https://github.com/openai/openai-agents-python/releases/tag/v0.18.2) — 2 days ago
- **Claude Agent SDK** [`v2.1.207`](https://github.com/anthropics/claude-code/releases/tag/v2.1.207) — 2 days ago
- **LangGraph** [`1.2.9`](https://github.com/langchain-ai/langgraph/releases/tag/1.2.9) — 3 days ago
- **Agno** [`v2.7.2`](https://github.com/agno-agi/agno/releases/tag/v2.7.2) — 3 days ago
- **Mastra** [`@mastra/core@1.50.0`](https://github.com/mastra-ai/mastra/releases/tag/@mastra/core@1.50.0) — 4 days ago
- **Haystack** [`v2.31.0`](https://github.com/deepset-ai/haystack/releases/tag/v2.31.0) — 4 days ago
- **CrewAI** [`1.15.2`](https://github.com/crewAIInc/crewAI/releases/tag/1.15.2) — 5 days ago
- **Google ADK** [`v2.4.0`](https://github.com/google/adk-python/releases/tag/v2.4.0) — 5 days ago

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

*Powered by GitHub Actions • Data refreshed daily • Last run: 2026-07-13 09:37 UTC*