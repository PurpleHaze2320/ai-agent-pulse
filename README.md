# 🔬 AI Agent Framework Pulse Tracker

[![Daily Update](https://github.com/PurpleHaze2320/ai-agent-pulse/actions/workflows/track.yml/badge.svg)](https://github.com/PurpleHaze2320/ai-agent-pulse/actions/workflows/track.yml)
[![Frameworks Tracked](https://img.shields.io/badge/frameworks-19-blue)](https://github.com/PurpleHaze2320/ai-agent-pulse)
[![License: MIT](https://img.shields.io/badge/License-MIT-green.svg)](https://opensource.org/licenses/MIT)
[![GitHub stars](https://img.shields.io/github/stars/PurpleHaze2320/ai-agent-pulse?style=social)](https://github.com/PurpleHaze2320/ai-agent-pulse/stargazers)

> Automated daily tracking of the AI agent framework ecosystem's health, momentum, and trends.
> Last updated: **2026-09-24 11:26 UTC** | Tracking **19** frameworks

## How It Works

This bot runs daily via GitHub Actions and collects metrics from the GitHub API for the most important
AI agent frameworks. It computes a **Pulse Score** (0-100) based on six weighted signals: star velocity,
release freshness, issue health, commit activity, community size, and fork engagement. The result is
a living dashboard that shows which frameworks are gaining momentum and which are losing steam.

## 🏆 Pulse Leaderboard

| Rank | Framework | Pulse | Stars | ⭐ 7d | Commits (4w) | Last Release | Category |
|------|-----------|-------|-------|-------|--------------|--------------|----------|
| 1 | [BrowserUse](https://github.com/browser-use/browser-use) | 🟢 **89.0** | 116.2k | 🚀 +1257 | 131 | 20 days ago | `web-agent` |
| 2 | [Claude Agent SDK](https://github.com/anthropics/claude-code) | 🟢 **85.8** | 147.9k | 🚀 +2130 | 113 | today | `orchestration` |
| 3 | [CrewAI](https://github.com/crewAIInc/crewAI) | 🟢 **81.3** | 59.0k | 🚀 +289 | 107 | 7 days ago | `multi-agent` |
| 4 | [Mastra](https://github.com/mastra-ai/mastra) | 🟢 **77.1** | 28.3k | 🚀 +178 | 1863 | today | `typescript` |
| 5 | [OpenAI Agents SDK](https://github.com/openai/openai-agents-python) | 🟢 **76.9** | 29.7k | 🚀 +157 | 142 | 6 days ago | `orchestration` |
| 6 | [PydanticAI](https://github.com/pydantic/pydantic-ai) | 🟢 **74.3** | 20.1k | 🚀 +138 | 270 | today | `structured` |
| 7 | [Google ADK](https://github.com/google/adk-python) | 🟢 **72.8** | 21.6k | 📈 +62 | 392 | 5 days ago | `orchestration` |
| 8 | [LangGraph](https://github.com/langchain-ai/langgraph) | 🟢 **71.5** | 42.2k | 🚀 +409 | 41 | today | `orchestration` |
| 9 | [Agno](https://github.com/agno-agi/agno) | 🟢 **71.5** | 42.3k | 🚀 +119 | 125 | today | `multi-agent` |
| 10 | [Composio](https://github.com/ComposioHQ/composio) | 🟡 **67.4** | 30.3k | 📈 +93 | 283 | 1 day ago | `tooling` |
| 11 | [LlamaIndex](https://github.com/run-llama/llama_index) | 🟡 **61.3** | 52.3k | 🚀 +110 | 28 | 2 days ago | `data-agent` |
| 12 | [AG2](https://github.com/ag2ai/ag2) | 🟡 **59.4** | 5.0k | 📈 +21 | 47 | 2 days ago | `multi-agent` |
| 13 | [DSPy](https://github.com/stanfordnlp/dspy) | 🟡 **59.0** | 38.3k | 🚀 +166 | 39 | 12 days ago | `optimization` |
| 14 | [Semantic Kernel](https://github.com/microsoft/semantic-kernel) | 🟡 **51.9** | 28.6k | 📈 +29 | 12 | 20 days ago | `enterprise` |
| 15 | [Haystack](https://github.com/deepset-ai/haystack) | 🟡 **51.5** | 26.6k | 📈 +60 | 0 | today | `pipeline` |
| 16 | [Letta](https://github.com/letta-ai/letta) | 🟠 **38.6** | 24.9k | 📈 +94 | 2 | 4 mo ago | `memory` |
| 17 | [Smolagents](https://github.com/huggingface/smolagents) | 🟠 **35.8** | 29.5k | 🚀 +111 | 2 | 3 mo ago | `lightweight` |
| 18 | [AutoGen](https://github.com/microsoft/autogen) | 🟠 **33.6** | 61.1k | 🚀 +127 | 0 | 11 mo ago | `multi-agent` |
| 19 | [Swarm](https://github.com/openai/swarm) | 🔴 **9.5** | 22.0k | ↗️ +20 | 0 | — | `experimental` |

## 📂 By Category

- `data-agent`: **LlamaIndex** (61.3)
- `enterprise`: **Semantic Kernel** (51.9)
- `experimental`: **Swarm** (9.5)
- `lightweight`: **Smolagents** (35.8)
- `memory`: **Letta** (38.6)
- `multi-agent`: **CrewAI** (81.3), **Agno** (71.5), **AG2** (59.4), **AutoGen** (33.6)
- `optimization`: **DSPy** (59.0)
- `orchestration`: **Claude Agent SDK** (85.8), **OpenAI Agents SDK** (76.9), **Google ADK** (72.8), **LangGraph** (71.5)
- `pipeline`: **Haystack** (51.5)
- `structured`: **PydanticAI** (74.3)
- `tooling`: **Composio** (67.4)
- `typescript`: **Mastra** (77.1)
- `web-agent`: **BrowserUse** (89.0)

## 🔍 Top 5 — Score Breakdown

| Framework | Star Velocity | Release Freshness | Issue Health | Commit Activity | Community | Fork Ratio |
|-----------|:---:|:---:|:---:|:---:|:---:|:---:|
| **BrowserUse** | 100 | 93.3 | 91.2 | 100 | 72.2 | 44.0 |
| **Claude Agent SDK** | 100 | 100.0 | 87.4 | 100 | 11.0 | 65.7 |
| **CrewAI** | 61.5 | 97.7 | 92.4 | 100 | 67.2 | 58.1 |
| **Mastra** | 37.8 | 100.0 | 95.3 | 100 | 93.2 | 40.2 |
| **OpenAI Agents SDK** | 32.9 | 98.0 | 99.0 | 100 | 77.0 | 64.7 |

## 💡 Key Insights

- **Hottest framework**: BrowserUse with a Pulse Score of 89.0
- **Fastest growing**: Claude Agent SDK gained +2130 stars this week
- **Most active development**: Mastra with 1863 commits in the last 4 weeks
- **Stale releases**: AutoGen, Swarm haven't released in a while

## 📦 Recent Releases

- **Haystack** [`v3.2.0`](https://github.com/deepset-ai/haystack/releases/tag/v3.2.0) — today
- **Mastra** [`@mastra/core@1.69.0`](https://github.com/mastra-ai/mastra/releases/tag/@mastra/core@1.69.0) — today
- **PydanticAI** [`v2.49.0`](https://github.com/pydantic/pydantic-ai/releases/tag/v2.49.0) — today
- **LangGraph** [`cli==0.4.32.dev0`](https://github.com/langchain-ai/langgraph/releases/tag/cli==0.4.32.dev0) — today
- **Claude Agent SDK** [`v2.1.281`](https://github.com/anthropics/claude-code/releases/tag/v2.1.281) — today
- **Agno** [`v3.0.11`](https://github.com/agno-agi/agno/releases/tag/v3.0.11) — today
- **Composio** [`versioning-example@0.1.4`](https://github.com/ComposioHQ/composio/releases/tag/versioning-example@0.1.4) — 1 day ago
- **AG2** [`v1.0.6`](https://github.com/ag2ai/ag2/releases/tag/v1.0.6) — 2 days ago
- **LlamaIndex** [`v0.14.25`](https://github.com/run-llama/llama_index/releases/tag/v0.14.25) — 2 days ago
- **Google ADK** [`v2.9.2`](https://github.com/google/adk-python/releases/tag/v2.9.2) — 5 days ago

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

*Powered by GitHub Actions • Data refreshed daily • Last run: 2026-09-24 11:26 UTC*