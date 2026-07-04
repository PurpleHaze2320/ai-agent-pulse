# 🔬 AI Agent Framework Pulse Tracker

[![Daily Update](https://github.com/PurpleHaze2320/ai-agent-pulse/actions/workflows/track.yml/badge.svg)](https://github.com/PurpleHaze2320/ai-agent-pulse/actions/workflows/track.yml)
[![Frameworks Tracked](https://img.shields.io/badge/frameworks-19-blue)](https://github.com/PurpleHaze2320/ai-agent-pulse)
[![License: MIT](https://img.shields.io/badge/License-MIT-green.svg)](https://opensource.org/licenses/MIT)
[![GitHub stars](https://img.shields.io/github/stars/PurpleHaze2320/ai-agent-pulse?style=social)](https://github.com/PurpleHaze2320/ai-agent-pulse/stargazers)

> Automated daily tracking of the AI agent framework ecosystem's health, momentum, and trends.
> Last updated: **2026-07-04 08:44 UTC** | Tracking **19** frameworks

## How It Works

This bot runs daily via GitHub Actions and collects metrics from the GitHub API for the most important
AI agent frameworks. It computes a **Pulse Score** (0-100) based on six weighted signals: star velocity,
release freshness, issue health, commit activity, community size, and fork engagement. The result is
a living dashboard that shows which frameworks are gaining momentum and which are losing steam.

## 🏆 Pulse Leaderboard

| Rank | Framework | Pulse | Stars | ⭐ 7d | Commits (4w) | Last Release | Category |
|------|-----------|-------|-------|-------|--------------|--------------|----------|
| 1 | [CrewAI](https://github.com/crewAIInc/crewAI) | 🟢 **88.6** | 54.9k | 🚀 +431 | 130 | 2 days ago | `multi-agent` |
| 2 | [BrowserUse](https://github.com/browser-use/browser-use) | 🟢 **83.7** | 102.6k | 🚀 +1691 | 69 | 2 days ago | `web-agent` |
| 3 | [Mastra](https://github.com/mastra-ai/mastra) | 🟢 **81.7** | 25.8k | 🚀 +305 | 1015 | 2 days ago | `typescript` |
| 4 | [LangGraph](https://github.com/langchain-ai/langgraph) | 🟢 **79.4** | 36.4k | 🚀 +577 | 57 | 4 days ago | `orchestration` |
| 5 | [PydanticAI](https://github.com/pydantic/pydantic-ai) | 🟢 **76.1** | 18.2k | 🚀 +178 | 190 | today | `structured` |
| 6 | [Agno](https://github.com/agno-agi/agno) | 🟢 **72.7** | 41.0k | 🚀 +129 | 113 | today | `multi-agent` |
| 7 | [Google ADK](https://github.com/google/adk-python) | 🟢 **72.2** | 20.4k | 🚀 +130 | 358 | 15 days ago | `orchestration` |
| 8 | [Claude Agent SDK](https://github.com/anthropics/claude-code) | 🟢 **72.0** | 136.0k | 🚀 +1338 | 32 | today | `orchestration` |
| 9 | [Haystack](https://github.com/deepset-ai/haystack) | 🟡 **69.7** | 25.8k | 📈 +73 | 181 | 16 days ago | `pipeline` |
| 10 | [OpenAI Agents SDK](https://github.com/openai/openai-agents-python) | 🟡 **67.6** | 27.6k | 🚀 +177 | 63 | 10 days ago | `orchestration` |
| 11 | [LlamaIndex](https://github.com/run-llama/llama_index) | 🟡 **65.8** | 50.6k | 🚀 +196 | 33 | 9 days ago | `data-agent` |
| 12 | [Semantic Kernel](https://github.com/microsoft/semantic-kernel) | 🟡 **57.8** | 28.3k | 📈 +56 | 35 | 17 days ago | `enterprise` |
| 13 | [DSPy](https://github.com/stanfordnlp/dspy) | 🟡 **57.8** | 35.8k | 🚀 +370 | 0 | 1 mo ago | `optimization` |
| 14 | [AG2](https://github.com/ag2ai/ag2) | 🟡 **50.2** | 4.7k | ↗️ +19 | 0 | today | `multi-agent` |
| 15 | [Composio](https://github.com/ComposioHQ/composio) | 🟡 **47.4** | 29.1k | 🚀 +102 | 0 | today | `tooling` |
| 16 | [Letta](https://github.com/letta-ai/letta) | 🟡 **43.7** | 23.6k | 📈 +99 | 0 | 1 mo ago | `memory` |
| 17 | [Smolagents](https://github.com/huggingface/smolagents) | 🟡 **41.8** | 28.2k | 🚀 +130 | 0 | 1 mo ago | `lightweight` |
| 18 | [AutoGen](https://github.com/microsoft/autogen) | 🟠 **38.5** | 59.5k | 🚀 +193 | 0 | 9 mo ago | `multi-agent` |
| 19 | [Swarm](https://github.com/openai/swarm) | 🔴 **9.4** | 21.8k | 📈 +28 | 0 | — | `experimental` |

## 📂 By Category

- `data-agent`: **LlamaIndex** (65.8)
- `enterprise`: **Semantic Kernel** (57.8)
- `experimental`: **Swarm** (9.4)
- `lightweight`: **Smolagents** (41.8)
- `memory`: **Letta** (43.7)
- `multi-agent`: **CrewAI** (88.6), **Agno** (72.7), **AG2** (50.2), **AutoGen** (38.5)
- `optimization`: **DSPy** (57.8)
- `orchestration`: **LangGraph** (79.4), **Google ADK** (72.2), **Claude Agent SDK** (72.0), **OpenAI Agents SDK** (67.6)
- `pipeline`: **Haystack** (69.7)
- `structured`: **PydanticAI** (76.1)
- `tooling`: **Composio** (47.4)
- `typescript`: **Mastra** (81.7)
- `web-agent`: **BrowserUse** (83.7)

## 🔍 Top 5 — Score Breakdown

| Framework | Star Velocity | Release Freshness | Issue Health | Commit Activity | Community | Fork Ratio |
|-----------|:---:|:---:|:---:|:---:|:---:|:---:|
| **CrewAI** | 91.2 | 99.3 | 95.6 | 100 | 59.6 | 56.1 |
| **BrowserUse** | 100 | 99.3 | 95.1 | 69.0 | 63.0 | 44.3 |
| **Mastra** | 58.5 | 99.3 | 95.6 | 100 | 92.6 | 36.5 |
| **LangGraph** | 100 | 98.7 | 73.5 | 57.0 | 55.0 | 67.0 |
| **PydanticAI** | 35.2 | 100.0 | 85.2 | 100 | 95.0 | 50.5 |

## 💡 Key Insights

- **Hottest framework**: CrewAI with a Pulse Score of 88.6
- **Fastest growing**: BrowserUse gained +1691 stars this week
- **Most active development**: Mastra with 1015 commits in the last 4 weeks
- **Stale releases**: AutoGen, Swarm haven't released in a while

## 📦 Recent Releases

- **PydanticAI** [`v2.5.0`](https://github.com/pydantic/pydantic-ai/releases/tag/v2.5.0) — today
- **Claude Agent SDK** [`v2.1.201`](https://github.com/anthropics/claude-code/releases/tag/v2.1.201) — today
- **AG2** [`v1.0.0b0`](https://github.com/ag2ai/ag2/releases/tag/v1.0.0b0) — today *(pre-release)*
- **Composio** [`@composio/cli@0.2.32-beta.281`](https://github.com/ComposioHQ/composio/releases/tag/@composio/cli@0.2.32-beta.281) — today *(pre-release)*
- **Agno** [`v2.6.22`](https://github.com/agno-agi/agno/releases/tag/v2.6.22) — today
- **CrewAI** [`1.15.2a2`](https://github.com/crewAIInc/crewAI/releases/tag/1.15.2a2) — 2 days ago *(pre-release)*
- **Mastra** [`@mastra/core@1.48.0`](https://github.com/mastra-ai/mastra/releases/tag/@mastra/core@1.48.0) — 2 days ago
- **BrowserUse** [`0.13.3`](https://github.com/browser-use/browser-use/releases/tag/0.13.3) — 2 days ago
- **LangGraph** [`1.2.7`](https://github.com/langchain-ai/langgraph/releases/tag/1.2.7) — 4 days ago
- **LlamaIndex** [`v0.14.23`](https://github.com/run-llama/llama_index/releases/tag/v0.14.23) — 9 days ago

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

*Powered by GitHub Actions • Data refreshed daily • Last run: 2026-07-04 08:44 UTC*