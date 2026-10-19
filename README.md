# 🔬 AI Agent Framework Pulse Tracker

[![Daily Update](https://github.com/PurpleHaze2320/ai-agent-pulse/actions/workflows/track.yml/badge.svg)](https://github.com/PurpleHaze2320/ai-agent-pulse/actions/workflows/track.yml)
[![Frameworks Tracked](https://img.shields.io/badge/frameworks-19-blue)](https://github.com/PurpleHaze2320/ai-agent-pulse)
[![License: MIT](https://img.shields.io/badge/License-MIT-green.svg)](https://opensource.org/licenses/MIT)
[![GitHub stars](https://img.shields.io/github/stars/PurpleHaze2320/ai-agent-pulse?style=social)](https://github.com/PurpleHaze2320/ai-agent-pulse/stargazers)

> Automated daily tracking of the AI agent framework ecosystem's health, momentum, and trends.
> Last updated: **2026-10-19 12:41 UTC** | Tracking **19** frameworks

## How It Works

This bot runs daily via GitHub Actions and collects metrics from the GitHub API for the most important
AI agent frameworks. It computes a **Pulse Score** (0-100) based on six weighted signals: star velocity,
release freshness, issue health, commit activity, community size, and fork engagement. The result is
a living dashboard that shows which frameworks are gaining momentum and which are losing steam.

## 🏆 Pulse Leaderboard

| Rank | Framework | Pulse | Stars | ⭐ 7d | Commits (4w) | Last Release | Category |
|------|-----------|-------|-------|-------|--------------|--------------|----------|
| 1 | [BrowserUse](https://github.com/browser-use/browser-use) | 🟢 **89.9** | 118.5k | 🚀 +759 | 142 | 3 days ago | `web-agent` |
| 2 | [LangGraph](https://github.com/langchain-ai/langgraph) | 🟢 **81.7** | 43.5k | 🚀 +363 | 97 | 2 days ago | `orchestration` |
| 3 | [OpenAI Agents SDK](https://github.com/openai/openai-agents-python) | 🟢 **76.8** | 30.1k | 🚀 +151 | 133 | 4 days ago | `orchestration` |
| 4 | [Mastra](https://github.com/mastra-ai/mastra) | 🟢 **76.2** | 28.9k | 🚀 +168 | 1794 | 3 days ago | `typescript` |
| 5 | [Google ADK](https://github.com/google/adk-python) | 🟢 **76.1** | 21.9k | 🚀 +127 | 435 | 5 days ago | `orchestration` |
| 6 | [Claude Agent SDK](https://github.com/anthropics/claude-code) | 🟢 **75.5** | 152.4k | 🚀 +2019 | 47 | today | `orchestration` |
| 7 | [CrewAI](https://github.com/crewAIInc/crewAI) | 🟢 **75.2** | 59.9k | 🚀 +267 | 80 | 5 days ago | `multi-agent` |
| 8 | [PydanticAI](https://github.com/pydantic/pydantic-ai) | 🟢 **73.4** | 20.7k | 🚀 +152 | 744 | 13 days ago | `structured` |
| 9 | [Haystack](https://github.com/deepset-ai/haystack) | 🟢 **70.8** | 26.8k | 📈 +47 | 225 | 4 days ago | `pipeline` |
| 10 | [AG2](https://github.com/ag2ai/ag2) | 🟡 **69.2** | 5.0k | ↗️ +13 | 113 | 8 days ago | `multi-agent` |
| 11 | [Composio](https://github.com/ComposioHQ/composio) | 🟡 **68.5** | 30.6k | 🚀 +132 | 253 | 3 days ago | `tooling` |
| 12 | [DSPy](https://github.com/stanfordnlp/dspy) | 🟡 **58.3** | 38.7k | 📈 +93 | 49 | 6 days ago | `optimization` |
| 13 | [LlamaIndex](https://github.com/run-llama/llama_index) | 🟡 **56.2** | 52.6k | 📈 +98 | 15 | 27 days ago | `data-agent` |
| 14 | [Semantic Kernel](https://github.com/microsoft/semantic-kernel) | 🟡 **54.3** | 28.7k | ↗️ +19 | 23 | 12 days ago | `enterprise` |
| 15 | [Agno](https://github.com/agno-agi/agno) | 🟡 **51.7** | 42.8k | 🚀 +122 | 0 | today | `multi-agent` |
| 16 | [Letta](https://github.com/letta-ai/letta) | 🟠 **35.8** | 25.2k | 📈 +74 | 1 | 5 mo ago | `memory` |
| 17 | [Smolagents](https://github.com/huggingface/smolagents) | 🟠 **34.4** | 29.9k | 🚀 +127 | 3 | 4 mo ago | `lightweight` |
| 18 | [AutoGen](https://github.com/microsoft/autogen) | 🟠 **32.8** | 61.5k | 🚀 +109 | 1 | 1y ago | `multi-agent` |
| 19 | [Swarm](https://github.com/openai/swarm) | 🔴 **9.2** | 22.1k | ↗️ +12 | 0 | — | `experimental` |

## 📂 By Category

- `data-agent`: **LlamaIndex** (56.2)
- `enterprise`: **Semantic Kernel** (54.3)
- `experimental`: **Swarm** (9.2)
- `lightweight`: **Smolagents** (34.4)
- `memory`: **Letta** (35.8)
- `multi-agent`: **CrewAI** (75.2), **AG2** (69.2), **Agno** (51.7), **AutoGen** (32.8)
- `optimization`: **DSPy** (58.3)
- `orchestration`: **LangGraph** (81.7), **OpenAI Agents SDK** (76.8), **Google ADK** (76.1), **Claude Agent SDK** (75.5)
- `pipeline`: **Haystack** (70.8)
- `structured`: **PydanticAI** (73.4)
- `tooling`: **Composio** (68.5)
- `typescript`: **Mastra** (76.2)
- `web-agent`: **BrowserUse** (89.9)

## 🔍 Top 5 — Score Breakdown

| Framework | Star Velocity | Release Freshness | Issue Health | Commit Activity | Community | Fork Ratio |
|-----------|:---:|:---:|:---:|:---:|:---:|:---:|
| **BrowserUse** | 100 | 99.0 | 89.5 | 100 | 72.2 | 44.4 |
| **LangGraph** | 74.4 | 99.3 | 75.3 | 97.0 | 56.6 | 68.3 |
| **OpenAI Agents SDK** | 29.8 | 98.7 | 99.4 | 100 | 80.2 | 66.8 |
| **Mastra** | 34.4 | 99.0 | 95.0 | 100 | 93.4 | 41.7 |
| **Google ADK** | 22.8 | 98.3 | 94.8 | 100 | 86.0 | 79.1 |

## 💡 Key Insights

- **Hottest framework**: BrowserUse with a Pulse Score of 89.9
- **Fastest growing**: Claude Agent SDK gained +2019 stars this week
- **Most active development**: Mastra with 1794 commits in the last 4 weeks
- **Stale releases**: AutoGen, Swarm haven't released in a while

## 📦 Recent Releases

- **Agno** [`v3.1.5`](https://github.com/agno-agi/agno/releases/tag/v3.1.5) — today
- **Claude Agent SDK** [`v2.1.303`](https://github.com/anthropics/claude-code/releases/tag/v2.1.303) — today
- **LangGraph** [`1.2.16`](https://github.com/langchain-ai/langgraph/releases/tag/1.2.16) — 2 days ago
- **Composio** [`@composio/cli@0.4.6-beta.457`](https://github.com/ComposioHQ/composio/releases/tag/@composio/cli@0.4.6-beta.457) — 3 days ago *(pre-release)*
- **Mastra** [`@mastra/core@1.78.0`](https://github.com/mastra-ai/mastra/releases/tag/@mastra/core@1.78.0) — 3 days ago
- **BrowserUse** [`0.13.13`](https://github.com/browser-use/browser-use/releases/tag/0.13.13) — 3 days ago
- **Haystack** [`v3.4.0`](https://github.com/deepset-ai/haystack/releases/tag/v3.4.0) — 4 days ago
- **OpenAI Agents SDK** [`v0.24.0`](https://github.com/openai/openai-agents-python/releases/tag/v0.24.0) — 4 days ago
- **CrewAI** [`1.15.28`](https://github.com/crewAIInc/crewAI/releases/tag/1.15.28) — 5 days ago
- **Google ADK** [`v2.12.0`](https://github.com/google/adk-python/releases/tag/v2.12.0) — 5 days ago

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

*Powered by GitHub Actions • Data refreshed daily • Last run: 2026-10-19 12:41 UTC*