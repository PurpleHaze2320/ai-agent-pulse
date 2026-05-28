# 🔬 AI Agent Framework Pulse Tracker

[![Daily Update](https://github.com/PurpleHaze2320/ai-agent-pulse/actions/workflows/track.yml/badge.svg)](https://github.com/PurpleHaze2320/ai-agent-pulse/actions/workflows/track.yml)
[![Frameworks Tracked](https://img.shields.io/badge/frameworks-19-blue)](https://github.com/PurpleHaze2320/ai-agent-pulse)
[![License: MIT](https://img.shields.io/badge/License-MIT-green.svg)](https://opensource.org/licenses/MIT)
[![GitHub stars](https://img.shields.io/github/stars/PurpleHaze2320/ai-agent-pulse?style=social)](https://github.com/PurpleHaze2320/ai-agent-pulse/stargazers)

> Automated daily tracking of the AI agent framework ecosystem's health, momentum, and trends.
> Last updated: **2026-05-28 10:14 UTC** | Tracking **19** frameworks

## How It Works

This bot runs daily via GitHub Actions and collects metrics from the GitHub API for the most important
AI agent frameworks. It computes a **Pulse Score** (0-100) based on six weighted signals: star velocity,
release freshness, issue health, commit activity, community size, and fork engagement. The result is
a living dashboard that shows which frameworks are gaining momentum and which are losing steam.

## 🏆 Pulse Leaderboard

| Rank | Framework | Pulse | Stars | ⭐ 7d | Commits (4w) | Last Release | Category |
|------|-----------|-------|-------|-------|--------------|--------------|----------|
| 1 | [Mastra](https://github.com/mastra-ai/mastra) | 🟢 **81.1** | 24.4k | 🚀 +303 | 893 | today | `typescript` |
| 2 | [CrewAI](https://github.com/crewAIInc/crewAI) | 🟢 **71.2** | 52.4k | 🚀 +491 | 0 | today | `multi-agent` |
| 3 | [BrowserUse](https://github.com/browser-use/browser-use) | 🟢 **70.0** | 96.0k | 🚀 +1040 | 0 | 2 days ago | `web-agent` |
| 4 | [LangGraph](https://github.com/langchain-ai/langgraph) | 🟡 **68.6** | 33.2k | 🚀 +646 | 0 | 1 day ago | `orchestration` |
| 5 | [Claude Agent SDK](https://github.com/anthropics/claude-code) | 🟡 **65.4** | 127.2k | 🚀 +1801 | 0 | today | `orchestration` |
| 6 | [LlamaIndex](https://github.com/run-llama/llama_index) | 🟡 **57.9** | 49.7k | 🚀 +171 | 0 | 13 days ago | `data-agent` |
| 7 | [OpenAI Agents SDK](https://github.com/openai/openai-agents-python) | 🟡 **57.1** | 26.7k | 🚀 +183 | 0 | 2 days ago | `orchestration` |
| 8 | [PydanticAI](https://github.com/pydantic/pydantic-ai) | 🟡 **55.4** | 17.4k | 🚀 +182 | 0 | 1 day ago | `structured` |
| 9 | [Agno](https://github.com/agno-agi/agno) | 🟡 **53.1** | 40.4k | 🚀 +129 | 0 | 6 days ago | `multi-agent` |
| 10 | [Semantic Kernel](https://github.com/microsoft/semantic-kernel) | 🟡 **51.4** | 28.0k | 📈 +47 | 0 | today | `enterprise` |
| 11 | [DSPy](https://github.com/stanfordnlp/dspy) | 🟡 **51.1** | 34.7k | 🚀 +141 | 0 | today | `optimization` |
| 12 | [Google ADK](https://github.com/google/adk-python) | 🟡 **51.0** | 19.9k | 🚀 +125 | 0 | 5 days ago | `orchestration` |
| 13 | [Haystack](https://github.com/deepset-ai/haystack) | 🟡 **49.5** | 25.4k | 📈 +83 | 0 | 15 days ago | `pipeline` |
| 14 | [Letta](https://github.com/letta-ai/letta) | 🟡 **48.7** | 23.0k | 🚀 +153 | 0 | 13 days ago | `memory` |
| 15 | [AG2](https://github.com/ag2ai/ag2) | 🟡 **48.5** | 4.6k | ↗️ +20 | 0 | 5 days ago | `multi-agent` |
| 16 | [Composio](https://github.com/ComposioHQ/composio) | 🟡 **47.6** | 28.5k | 🚀 +123 | 0 | 8 days ago | `tooling` |
| 17 | [Smolagents](https://github.com/huggingface/smolagents) | 🟡 **44.3** | 27.6k | 🚀 +139 | 0 | 13 days ago | `lightweight` |
| 18 | [AutoGen](https://github.com/microsoft/autogen) | 🟡 **43.4** | 58.5k | 🚀 +242 | 0 | 8 mo ago | `multi-agent` |
| 19 | [Swarm](https://github.com/openai/swarm) | 🔴 **9.0** | 21.5k | 📈 +24 | 0 | — | `experimental` |

## 📂 By Category

- `data-agent`: **LlamaIndex** (57.9)
- `enterprise`: **Semantic Kernel** (51.4)
- `experimental`: **Swarm** (9.0)
- `lightweight`: **Smolagents** (44.3)
- `memory`: **Letta** (48.7)
- `multi-agent`: **CrewAI** (71.2), **Agno** (53.1), **AG2** (48.5), **AutoGen** (43.4)
- `optimization`: **DSPy** (51.1)
- `orchestration`: **LangGraph** (68.6), **Claude Agent SDK** (65.4), **OpenAI Agents SDK** (57.1), **Google ADK** (51.0)
- `pipeline`: **Haystack** (49.5)
- `structured`: **PydanticAI** (55.4)
- `tooling`: **Composio** (47.6)
- `typescript`: **Mastra** (81.1)
- `web-agent`: **BrowserUse** (70.0)

## 🔍 Top 5 — Score Breakdown

| Framework | Star Velocity | Release Freshness | Issue Health | Commit Activity | Community | Fork Ratio |
|-----------|:---:|:---:|:---:|:---:|:---:|:---:|
| **Mastra** | 58.4 | 100.0 | 94.5 | 100 | 88.2 | 35.1 |
| **CrewAI** | 100 | 100.0 | 98.0 | 0.0 | 59.2 | 55.6 |
| **BrowserUse** | 100 | 99.3 | 95.8 | 0.0 | 63.0 | 44.9 |
| **LangGraph** | 100 | 99.7 | 76.4 | 0.0 | 54.8 | 67.4 |
| **Claude Agent SDK** | 100 | 100.0 | 85.7 | 0.0 | 10.2 | 65.6 |

## 💡 Key Insights

- **Hottest framework**: Mastra with a Pulse Score of 81.1
- **Fastest growing**: Claude Agent SDK gained +1801 stars this week
- **Most active development**: Mastra with 893 commits in the last 4 weeks
- **Stale releases**: Swarm haven't released in a while

## 📦 Recent Releases

- **Semantic Kernel** [`dotnet-1.77.0`](https://github.com/microsoft/semantic-kernel/releases/tag/dotnet-1.77.0) — today
- **DSPy** [`3.3.0b1`](https://github.com/stanfordnlp/dspy/releases/tag/3.3.0b1) — today *(pre-release)*
- **Claude Agent SDK** [`v2.1.153`](https://github.com/anthropics/claude-code/releases/tag/v2.1.153) — today
- **CrewAI** [`1.14.6a2`](https://github.com/crewAIInc/crewAI/releases/tag/1.14.6a2) — today *(pre-release)*
- **Mastra** [`@mastra/core@1.37.0`](https://github.com/mastra-ai/mastra/releases/tag/@mastra/core@1.37.0) — today
- **PydanticAI** [`v1.103.0`](https://github.com/pydantic/pydantic-ai/releases/tag/v1.103.0) — 1 day ago
- **LangGraph** [`1.2.2`](https://github.com/langchain-ai/langgraph/releases/tag/1.2.2) — 1 day ago
- **OpenAI Agents SDK** [`v0.17.4`](https://github.com/openai/openai-agents-python/releases/tag/v0.17.4) — 2 days ago
- **BrowserUse** [`0.12.9`](https://github.com/browser-use/browser-use/releases/tag/0.12.9) — 2 days ago
- **AG2** [`v0.13.1`](https://github.com/ag2ai/ag2/releases/tag/v0.13.1) — 5 days ago

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

*Powered by GitHub Actions • Data refreshed daily • Last run: 2026-05-28 10:14 UTC*