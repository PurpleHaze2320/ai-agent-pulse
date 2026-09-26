# 🔬 AI Agent Framework Pulse Tracker

[![Daily Update](https://github.com/PurpleHaze2320/ai-agent-pulse/actions/workflows/track.yml/badge.svg)](https://github.com/PurpleHaze2320/ai-agent-pulse/actions/workflows/track.yml)
[![Frameworks Tracked](https://img.shields.io/badge/frameworks-19-blue)](https://github.com/PurpleHaze2320/ai-agent-pulse)
[![License: MIT](https://img.shields.io/badge/License-MIT-green.svg)](https://opensource.org/licenses/MIT)
[![GitHub stars](https://img.shields.io/github/stars/PurpleHaze2320/ai-agent-pulse?style=social)](https://github.com/PurpleHaze2320/ai-agent-pulse/stargazers)

> Automated daily tracking of the AI agent framework ecosystem's health, momentum, and trends.
> Last updated: **2026-09-26 11:07 UTC** | Tracking **19** frameworks

## How It Works

This bot runs daily via GitHub Actions and collects metrics from the GitHub API for the most important
AI agent frameworks. It computes a **Pulse Score** (0-100) based on six weighted signals: star velocity,
release freshness, issue health, commit activity, community size, and fork engagement. The result is
a living dashboard that shows which frameworks are gaining momentum and which are losing steam.

## 🏆 Pulse Leaderboard

| Rank | Framework | Pulse | Stars | ⭐ 7d | Commits (4w) | Last Release | Category |
|------|-----------|-------|-------|-------|--------------|--------------|----------|
| 1 | [BrowserUse](https://github.com/browser-use/browser-use) | 🟢 **88.8** | 116.4k | 🚀 +1106 | 135 | 22 days ago | `web-agent` |
| 2 | [Claude Agent SDK](https://github.com/anthropics/claude-code) | 🟢 **85.8** | 148.2k | 🚀 +1663 | 126 | today | `orchestration` |
| 3 | [CrewAI](https://github.com/crewAIInc/crewAI) | 🟢 **81.2** | 59.0k | 🚀 +294 | 111 | 9 days ago | `multi-agent` |
| 4 | [Mastra](https://github.com/mastra-ai/mastra) | 🟢 **76.4** | 28.3k | 🚀 +163 | 2097 | 1 day ago | `typescript` |
| 5 | [OpenAI Agents SDK](https://github.com/openai/openai-agents-python) | 🟢 **76.4** | 29.7k | 🚀 +147 | 170 | 8 days ago | `orchestration` |
| 6 | [PydanticAI](https://github.com/pydantic/pydantic-ai) | 🟢 **74.6** | 20.2k | 🚀 +148 | 523 | today | `structured` |
| 7 | [Google ADK](https://github.com/google/adk-python) | 🟢 **73.5** | 21.6k | 📈 +73 | 425 | today | `orchestration` |
| 8 | [Haystack](https://github.com/deepset-ai/haystack) | 🟢 **71.3** | 26.6k | 📈 +58 | 248 | 2 days ago | `pipeline` |
| 9 | [Agno](https://github.com/agno-agi/agno) | 🟢 **70.7** | 42.3k | 🚀 +104 | 133 | 2 days ago | `multi-agent` |
| 10 | [LangGraph](https://github.com/langchain-ai/langgraph) | 🟢 **70.1** | 42.3k | 🚀 +383 | 41 | 2 days ago | `orchestration` |
| 11 | [Composio](https://github.com/ComposioHQ/composio) | 🟡 **67.2** | 30.3k | 📈 +85 | 294 | 1 day ago | `tooling` |
| 12 | [AG2](https://github.com/ag2ai/ag2) | 🟡 **62.3** | 5.0k | 📈 +21 | 61 | 1 day ago | `multi-agent` |
| 13 | [DSPy](https://github.com/stanfordnlp/dspy) | 🟡 **61.8** | 38.3k | 🚀 +177 | 47 | 1 day ago | `optimization` |
| 14 | [LlamaIndex](https://github.com/run-llama/llama_index) | 🟡 **61.3** | 52.3k | 📈 +93 | 32 | 4 days ago | `data-agent` |
| 15 | [Semantic Kernel](https://github.com/microsoft/semantic-kernel) | 🟡 **51.7** | 28.6k | 📈 +29 | 12 | 22 days ago | `enterprise` |
| 16 | [Letta](https://github.com/letta-ai/letta) | 🟠 **38.5** | 24.9k | 📈 +97 | 2 | 4 mo ago | `memory` |
| 17 | [Smolagents](https://github.com/huggingface/smolagents) | 🟠 **35.2** | 29.5k | 🚀 +103 | 2 | 4 mo ago | `lightweight` |
| 18 | [AutoGen](https://github.com/microsoft/autogen) | 🟠 **33.1** | 61.2k | 🚀 +114 | 0 | 12 mo ago | `multi-agent` |
| 19 | [Swarm](https://github.com/openai/swarm) | 🔴 **9.5** | 22.0k | 📈 +22 | 0 | — | `experimental` |

## 📂 By Category

- `data-agent`: **LlamaIndex** (61.3)
- `enterprise`: **Semantic Kernel** (51.7)
- `experimental`: **Swarm** (9.5)
- `lightweight`: **Smolagents** (35.2)
- `memory`: **Letta** (38.5)
- `multi-agent`: **CrewAI** (81.2), **Agno** (70.7), **AG2** (62.3), **AutoGen** (33.1)
- `optimization`: **DSPy** (61.8)
- `orchestration`: **Claude Agent SDK** (85.8), **OpenAI Agents SDK** (76.4), **Google ADK** (73.5), **LangGraph** (70.1)
- `pipeline`: **Haystack** (71.3)
- `structured`: **PydanticAI** (74.6)
- `tooling`: **Composio** (67.2)
- `typescript`: **Mastra** (76.4)
- `web-agent`: **BrowserUse** (88.8)

## 🔍 Top 5 — Score Breakdown

| Framework | Star Velocity | Release Freshness | Issue Health | Commit Activity | Community | Fork Ratio |
|-----------|:---:|:---:|:---:|:---:|:---:|:---:|
| **BrowserUse** | 100 | 92.7 | 90.8 | 100 | 72.2 | 44.1 |
| **Claude Agent SDK** | 100 | 100.0 | 86.9 | 100 | 11.2 | 66.6 |
| **CrewAI** | 61.7 | 97.0 | 92.0 | 100 | 67.2 | 58.1 |
| **Mastra** | 35.1 | 99.7 | 95.4 | 100 | 93.2 | 40.4 |
| **OpenAI Agents SDK** | 31.0 | 97.3 | 99.3 | 100 | 78.2 | 64.8 |

## 💡 Key Insights

- **Hottest framework**: BrowserUse with a Pulse Score of 88.8
- **Fastest growing**: Claude Agent SDK gained +1663 stars this week
- **Most active development**: Mastra with 2097 commits in the last 4 weeks
- **Stale releases**: AutoGen, Swarm haven't released in a while

## 📦 Recent Releases

- **PydanticAI** [`v2.51.0`](https://github.com/pydantic/pydantic-ai/releases/tag/v2.51.0) — today
- **Claude Agent SDK** [`v2.1.283`](https://github.com/anthropics/claude-code/releases/tag/v2.1.283) — today
- **Google ADK** [`v2.10.0`](https://github.com/google/adk-python/releases/tag/v2.10.0) — today
- **Mastra** [`@mastra/core@1.71.0`](https://github.com/mastra-ai/mastra/releases/tag/@mastra/core@1.71.0) — 1 day ago
- **DSPy** [`3.4.0`](https://github.com/stanfordnlp/dspy/releases/tag/3.4.0) — 1 day ago
- **AG2** [`v1.1.0`](https://github.com/ag2ai/ag2/releases/tag/v1.1.0) — 1 day ago
- **Composio** [`versioning-example@0.1.5`](https://github.com/ComposioHQ/composio/releases/tag/versioning-example@0.1.5) — 1 day ago
- **Haystack** [`v3.2.0`](https://github.com/deepset-ai/haystack/releases/tag/v3.2.0) — 2 days ago
- **LangGraph** [`cli==0.4.32.dev0`](https://github.com/langchain-ai/langgraph/releases/tag/cli==0.4.32.dev0) — 2 days ago
- **Agno** [`v3.0.11`](https://github.com/agno-agi/agno/releases/tag/v3.0.11) — 2 days ago

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

*Powered by GitHub Actions • Data refreshed daily • Last run: 2026-09-26 11:07 UTC*