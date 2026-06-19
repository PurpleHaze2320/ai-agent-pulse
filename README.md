# 🔬 AI Agent Framework Pulse Tracker

[![Daily Update](https://github.com/PurpleHaze2320/ai-agent-pulse/actions/workflows/track.yml/badge.svg)](https://github.com/PurpleHaze2320/ai-agent-pulse/actions/workflows/track.yml)
[![Frameworks Tracked](https://img.shields.io/badge/frameworks-19-blue)](https://github.com/PurpleHaze2320/ai-agent-pulse)
[![License: MIT](https://img.shields.io/badge/License-MIT-green.svg)](https://opensource.org/licenses/MIT)
[![GitHub stars](https://img.shields.io/github/stars/PurpleHaze2320/ai-agent-pulse?style=social)](https://github.com/PurpleHaze2320/ai-agent-pulse/stargazers)

> Automated daily tracking of the AI agent framework ecosystem's health, momentum, and trends.
> Last updated: **2026-06-19 10:46 UTC** | Tracking **19** frameworks

## How It Works

This bot runs daily via GitHub Actions and collects metrics from the GitHub API for the most important
AI agent frameworks. It computes a **Pulse Score** (0-100) based on six weighted signals: star velocity,
release freshness, issue health, commit activity, community size, and fork engagement. The result is
a living dashboard that shows which frameworks are gaining momentum and which are losing steam.

## 🏆 Pulse Leaderboard

| Rank | Framework | Pulse | Stars | ⭐ 7d | Commits (4w) | Last Release | Category |
|------|-----------|-------|-------|-------|--------------|--------------|----------|
| 1 | [CrewAI](https://github.com/crewAIInc/crewAI) | 🟢 **91.0** | 54.0k | 🚀 +641 | 122 | today | `multi-agent` |
| 2 | [BrowserUse](https://github.com/browser-use/browser-use) | 🟢 **89.7** | 99.5k | 🚀 +1122 | 408 | 6 days ago | `web-agent` |
| 3 | [LangGraph](https://github.com/langchain-ai/langgraph) | 🟢 **84.8** | 35.2k | 🚀 +686 | 82 | today | `orchestration` |
| 4 | [Mastra](https://github.com/mastra-ai/mastra) | 🟢 **80.0** | 25.2k | 🚀 +258 | 872 | 6 days ago | `typescript` |
| 5 | [Agno](https://github.com/agno-agi/agno) | 🟢 **72.2** | 40.8k | 🚀 +108 | 106 | today | `multi-agent` |
| 6 | [Claude Agent SDK](https://github.com/anthropics/claude-code) | 🟢 **72.2** | 133.3k | 🚀 +1337 | 33 | today | `orchestration` |
| 7 | [Google ADK](https://github.com/google/adk-python) | 🟢 **71.2** | 20.2k | 📈 +92 | 283 | today | `orchestration` |
| 8 | [Haystack](https://github.com/deepset-ai/haystack) | 🟡 **69.7** | 25.6k | 📈 +59 | 155 | 1 day ago | `pipeline` |
| 9 | [PydanticAI](https://github.com/pydantic/pydantic-ai) | 🟡 **69.1** | 17.9k | 🚀 +132 | 78 | 8 days ago | `structured` |
| 10 | [AG2](https://github.com/ag2ai/ag2) | 🟡 **62.0** | 4.7k | 📈 +24 | 68 | 6 days ago | `multi-agent` |
| 11 | [OpenAI Agents SDK](https://github.com/openai/openai-agents-python) | 🟡 **60.8** | 27.3k | 🚀 +153 | 32 | today | `orchestration` |
| 12 | [LlamaIndex](https://github.com/run-llama/llama_index) | 🟡 **59.7** | 50.2k | 🚀 +129 | 24 | 1 mo ago | `data-agent` |
| 13 | [DSPy](https://github.com/stanfordnlp/dspy) | 🟡 **57.6** | 35.2k | 🚀 +155 | 38 | 22 days ago | `optimization` |
| 14 | [Semantic Kernel](https://github.com/microsoft/semantic-kernel) | 🟡 **57.3** | 28.2k | 📈 +55 | 28 | 2 days ago | `enterprise` |
| 15 | [Composio](https://github.com/ComposioHQ/composio) | 🟡 **57.0** | 28.9k | 🚀 +116 | 48 | 2 days ago | `tooling` |
| 16 | [Letta](https://github.com/letta-ai/letta) | 🟡 **45.6** | 23.4k | 🚀 +120 | 0 | 1 mo ago | `memory` |
| 17 | [Smolagents](https://github.com/huggingface/smolagents) | 🟡 **43.2** | 27.9k | 🚀 +106 | 5 | 21 days ago | `lightweight` |
| 18 | [AutoGen](https://github.com/microsoft/autogen) | 🟠 **39.0** | 59.1k | 🚀 +172 | 0 | 8 mo ago | `multi-agent` |
| 19 | [Swarm](https://github.com/openai/swarm) | 🔴 **9.2** | 21.6k | 📈 +33 | 0 | — | `experimental` |

## 📂 By Category

- `data-agent`: **LlamaIndex** (59.7)
- `enterprise`: **Semantic Kernel** (57.3)
- `experimental`: **Swarm** (9.2)
- `lightweight`: **Smolagents** (43.2)
- `memory`: **Letta** (45.6)
- `multi-agent`: **CrewAI** (91.0), **Agno** (72.2), **AG2** (62.0), **AutoGen** (39.0)
- `optimization`: **DSPy** (57.6)
- `orchestration`: **LangGraph** (84.8), **Claude Agent SDK** (72.2), **Google ADK** (71.2), **OpenAI Agents SDK** (60.8)
- `pipeline`: **Haystack** (69.7)
- `structured`: **PydanticAI** (69.1)
- `tooling`: **Composio** (57.0)
- `typescript`: **Mastra** (80.0)
- `web-agent`: **BrowserUse** (89.7)

## 🔍 Top 5 — Score Breakdown

| Framework | Star Velocity | Release Freshness | Issue Health | Commit Activity | Community | Fork Ratio |
|-----------|:---:|:---:|:---:|:---:|:---:|:---:|
| **CrewAI** | 100 | 100.0 | 96.7 | 100 | 59.4 | 56.0 |
| **BrowserUse** | 100 | 98.0 | 95.5 | 100 | 63.0 | 44.6 |
| **LangGraph** | 100 | 100.0 | 74.6 | 82.0 | 55.0 | 67.0 |
| **Mastra** | 53.8 | 98.0 | 94.8 | 100 | 91.8 | 35.7 |
| **Agno** | 23.0 | 100.0 | 80.8 | 100 | 89.0 | 54.4 |

## 💡 Key Insights

- **Hottest framework**: CrewAI with a Pulse Score of 91.0
- **Fastest growing**: Claude Agent SDK gained +1337 stars this week
- **Most active development**: Mastra with 872 commits in the last 4 weeks
- **Stale releases**: Swarm haven't released in a while

## 📦 Recent Releases

- **OpenAI Agents SDK** [`v0.17.6`](https://github.com/openai/openai-agents-python/releases/tag/v0.17.6) — today
- **Claude Agent SDK** [`v2.1.183`](https://github.com/anthropics/claude-code/releases/tag/v2.1.183) — today
- **CrewAI** [`1.14.8a2`](https://github.com/crewAIInc/crewAI/releases/tag/1.14.8a2) — today *(pre-release)*
- **LangGraph** [`1.2.6`](https://github.com/langchain-ai/langgraph/releases/tag/1.2.6) — today
- **Agno** [`v2.6.18`](https://github.com/agno-agi/agno/releases/tag/v2.6.18) — today
- **Google ADK** [`v2.3.0`](https://github.com/google/adk-python/releases/tag/v2.3.0) — today
- **Haystack** [`v2.30.2`](https://github.com/deepset-ai/haystack/releases/tag/v2.30.2) — 1 day ago
- **Semantic Kernel** [`python-1.43.1`](https://github.com/microsoft/semantic-kernel/releases/tag/python-1.43.1) — 2 days ago
- **Composio** [`@composio/cli@0.2.32-beta.265`](https://github.com/ComposioHQ/composio/releases/tag/@composio/cli@0.2.32-beta.265) — 2 days ago *(pre-release)*
- **BrowserUse** [`0.13.2`](https://github.com/browser-use/browser-use/releases/tag/0.13.2) — 6 days ago

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

*Powered by GitHub Actions • Data refreshed daily • Last run: 2026-06-19 10:46 UTC*