# 🔬 AI Agent Framework Pulse Tracker

[![Daily Update](https://github.com/PurpleHaze2320/ai-agent-pulse/actions/workflows/track.yml/badge.svg)](https://github.com/PurpleHaze2320/ai-agent-pulse/actions/workflows/track.yml)
[![Frameworks Tracked](https://img.shields.io/badge/frameworks-19-blue)](https://github.com/PurpleHaze2320/ai-agent-pulse)
[![License: MIT](https://img.shields.io/badge/License-MIT-green.svg)](https://opensource.org/licenses/MIT)
[![GitHub stars](https://img.shields.io/github/stars/PurpleHaze2320/ai-agent-pulse?style=social)](https://github.com/PurpleHaze2320/ai-agent-pulse/stargazers)

> Automated daily tracking of the AI agent framework ecosystem's health, momentum, and trends.
> Last updated: **2026-07-23 08:38 UTC** | Tracking **19** frameworks

## How It Works

This bot runs daily via GitHub Actions and collects metrics from the GitHub API for the most important
AI agent frameworks. It computes a **Pulse Score** (0-100) based on six weighted signals: star velocity,
release freshness, issue health, commit activity, community size, and fork engagement. The result is
a living dashboard that shows which frameworks are gaining momentum and which are losing steam.

## 🏆 Pulse Leaderboard

| Rank | Framework | Pulse | Stars | ⭐ 7d | Commits (4w) | Last Release | Category |
|------|-----------|-------|-------|-------|--------------|--------------|----------|
| 1 | [BrowserUse](https://github.com/browser-use/browser-use) | 🟢 **86.5** | 106.2k | 🚀 +1218 | 85 | 6 days ago | `web-agent` |
| 2 | [CrewAI](https://github.com/crewAIInc/crewAI) | 🟢 **80.2** | 56.0k | 🚀 +394 | 69 | 2 days ago | `multi-agent` |
| 3 | [Mastra](https://github.com/mastra-ai/mastra) | 🟢 **80.2** | 26.5k | 🚀 +264 | 1135 | 7 days ago | `typescript` |
| 4 | [PydanticAI](https://github.com/pydantic/pydantic-ai) | 🟢 **77.1** | 18.7k | 🚀 +186 | 264 | today | `structured` |
| 5 | [OpenAI Agents SDK](https://github.com/openai/openai-agents-python) | 🟢 **75.4** | 28.1k | 🚀 +167 | 124 | 6 days ago | `orchestration` |
| 6 | [Agno](https://github.com/agno-agi/agno) | 🟢 **75.0** | 41.4k | 🚀 +186 | 146 | 2 days ago | `multi-agent` |
| 7 | [LangGraph](https://github.com/langchain-ai/langgraph) | 🟢 **73.0** | 37.9k | 🚀 +503 | 29 | 13 days ago | `orchestration` |
| 8 | [Haystack](https://github.com/deepset-ai/haystack) | 🟢 **71.1** | 26.0k | 📈 +79 | 233 | 2 days ago | `pipeline` |
| 9 | [Claude Agent SDK](https://github.com/anthropics/claude-code) | 🟢 **70.7** | 138.8k | 🚀 +746 | 28 | today | `orchestration` |
| 10 | [Composio](https://github.com/ComposioHQ/composio) | 🟡 **66.6** | 29.3k | 📈 +85 | 129 | 2 days ago | `tooling` |
| 11 | [Google ADK](https://github.com/google/adk-python) | 🟡 **57.7** | 20.8k | 🚀 +218 | 0 | 1 day ago | `orchestration` |
| 12 | [LlamaIndex](https://github.com/run-llama/llama_index) | 🟡 **56.2** | 51.0k | 🚀 +149 | 0 | 28 days ago | `data-agent` |
| 13 | [Semantic Kernel](https://github.com/microsoft/semantic-kernel) | 🟡 **52.8** | 28.3k | 📈 +30 | 14 | 15 days ago | `enterprise` |
| 14 | [DSPy](https://github.com/stanfordnlp/dspy) | 🟡 **49.3** | 36.3k | 🚀 +158 | 0 | 1 mo ago | `optimization` |
| 15 | [AG2](https://github.com/ag2ai/ag2) | 🟡 **48.5** | 4.8k | ↗️ +10 | 0 | 19 days ago | `multi-agent` |
| 16 | [Letta](https://github.com/letta-ai/letta) | 🟡 **43.0** | 23.9k | 🚀 +114 | 1 | 2 mo ago | `memory` |
| 17 | [Smolagents](https://github.com/huggingface/smolagents) | 🟡 **41.2** | 28.5k | 🚀 +119 | 4 | 1 mo ago | `lightweight` |
| 18 | [AutoGen](https://github.com/microsoft/autogen) | 🟠 **35.3** | 59.9k | 🚀 +146 | 0 | 9 mo ago | `multi-agent` |
| 19 | [Swarm](https://github.com/openai/swarm) | 🔴 **11.2** | 21.9k | 📈 +61 | 0 | — | `experimental` |

## 📂 By Category

- `data-agent`: **LlamaIndex** (56.2)
- `enterprise`: **Semantic Kernel** (52.8)
- `experimental`: **Swarm** (11.2)
- `lightweight`: **Smolagents** (41.2)
- `memory`: **Letta** (43.0)
- `multi-agent`: **CrewAI** (80.2), **Agno** (75.0), **AG2** (48.5), **AutoGen** (35.3)
- `optimization`: **DSPy** (49.3)
- `orchestration`: **OpenAI Agents SDK** (75.4), **LangGraph** (73.0), **Claude Agent SDK** (70.7), **Google ADK** (57.7)
- `pipeline`: **Haystack** (71.1)
- `structured`: **PydanticAI** (77.1)
- `tooling`: **Composio** (66.6)
- `typescript`: **Mastra** (80.2)
- `web-agent`: **BrowserUse** (86.5)

## 🔍 Top 5 — Score Breakdown

| Framework | Star Velocity | Release Freshness | Issue Health | Commit Activity | Community | Fork Ratio |
|-----------|:---:|:---:|:---:|:---:|:---:|:---:|
| **BrowserUse** | 100 | 98.0 | 94.7 | 85.0 | 63.0 | 44.0 |
| **CrewAI** | 82.0 | 99.3 | 96.3 | 69.0 | 59.6 | 56.6 |
| **Mastra** | 53.7 | 97.7 | 94.4 | 100 | 93.0 | 37.8 |
| **PydanticAI** | 38.4 | 100.0 | 86.0 | 100 | 94.8 | 51.2 |
| **OpenAI Agents SDK** | 34.6 | 98.0 | 98.2 | 100 | 62.2 | 62.1 |

## 💡 Key Insights

- **Hottest framework**: BrowserUse with a Pulse Score of 86.5
- **Fastest growing**: BrowserUse gained +1218 stars this week
- **Most active development**: Mastra with 1135 commits in the last 4 weeks
- **Stale releases**: AutoGen, Swarm haven't released in a while

## 📦 Recent Releases

- **PydanticAI** [`v2.16.0`](https://github.com/pydantic/pydantic-ai/releases/tag/v2.16.0) — today
- **Claude Agent SDK** [`v2.1.218`](https://github.com/anthropics/claude-code/releases/tag/v2.1.218) — today
- **Google ADK** [`v1.36.2`](https://github.com/google/adk-python/releases/tag/v1.36.2) — 1 day ago
- **Composio** [`@composio/cli@0.2.33-beta.298`](https://github.com/ComposioHQ/composio/releases/tag/@composio/cli@0.2.33-beta.298) — 2 days ago *(pre-release)*
- **CrewAI** [`1.15.5`](https://github.com/crewAIInc/crewAI/releases/tag/1.15.5) — 2 days ago
- **Agno** [`v2.8.0`](https://github.com/agno-agi/agno/releases/tag/v2.8.0) — 2 days ago
- **Haystack** [`v3.0.0`](https://github.com/deepset-ai/haystack/releases/tag/v3.0.0) — 2 days ago
- **BrowserUse** [`0.13.6`](https://github.com/browser-use/browser-use/releases/tag/0.13.6) — 6 days ago
- **OpenAI Agents SDK** [`v0.18.3`](https://github.com/openai/openai-agents-python/releases/tag/v0.18.3) — 6 days ago
- **Mastra** [`@mastra/core@1.51.0`](https://github.com/mastra-ai/mastra/releases/tag/@mastra/core@1.51.0) — 7 days ago

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

*Powered by GitHub Actions • Data refreshed daily • Last run: 2026-07-23 08:38 UTC*