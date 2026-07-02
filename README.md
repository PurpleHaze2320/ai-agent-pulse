# 🔬 AI Agent Framework Pulse Tracker

[![Daily Update](https://github.com/PurpleHaze2320/ai-agent-pulse/actions/workflows/track.yml/badge.svg)](https://github.com/PurpleHaze2320/ai-agent-pulse/actions/workflows/track.yml)
[![Frameworks Tracked](https://img.shields.io/badge/frameworks-19-blue)](https://github.com/PurpleHaze2320/ai-agent-pulse)
[![License: MIT](https://img.shields.io/badge/License-MIT-green.svg)](https://opensource.org/licenses/MIT)
[![GitHub stars](https://img.shields.io/github/stars/PurpleHaze2320/ai-agent-pulse?style=social)](https://github.com/PurpleHaze2320/ai-agent-pulse/stargazers)

> Automated daily tracking of the AI agent framework ecosystem's health, momentum, and trends.
> Last updated: **2026-07-02 09:21 UTC** | Tracking **19** frameworks

## How It Works

This bot runs daily via GitHub Actions and collects metrics from the GitHub API for the most important
AI agent frameworks. It computes a **Pulse Score** (0-100) based on six weighted signals: star velocity,
release freshness, issue health, commit activity, community size, and fork engagement. The result is
a living dashboard that shows which frameworks are gaining momentum and which are losing steam.

## 🏆 Pulse Leaderboard

| Rank | Framework | Pulse | Stars | ⭐ 7d | Commits (4w) | Last Release | Category |
|------|-----------|-------|-------|-------|--------------|--------------|----------|
| 1 | [CrewAI](https://github.com/crewAIInc/crewAI) | 🟢 **88.1** | 54.8k | 🚀 +409 | 128 | today | `multi-agent` |
| 2 | [BrowserUse](https://github.com/browser-use/browser-use) | 🟢 **83.8** | 102.1k | 🚀 +1504 | 69 | today | `web-agent` |
| 3 | [Mastra](https://github.com/mastra-ai/mastra) | 🟢 **80.5** | 25.7k | 🚀 +266 | 915 | today | `typescript` |
| 4 | [LangGraph](https://github.com/langchain-ai/langgraph) | 🟢 **76.9** | 36.3k | 🚀 +592 | 44 | 2 days ago | `orchestration` |
| 5 | [Google ADK](https://github.com/google/adk-python) | 🟢 **71.8** | 20.4k | 🚀 +115 | 354 | 13 days ago | `orchestration` |
| 6 | [Claude Agent SDK](https://github.com/anthropics/claude-code) | 🟢 **71.2** | 135.4k | 🚀 +1114 | 28 | today | `orchestration` |
| 7 | [Agno](https://github.com/agno-agi/agno) | 🟢 **70.9** | 41.0k | 🚀 +116 | 96 | 8 days ago | `multi-agent` |
| 8 | [Haystack](https://github.com/deepset-ai/haystack) | 🟢 **70.6** | 25.8k | 📈 +95 | 177 | 14 days ago | `pipeline` |
| 9 | [Composio](https://github.com/ComposioHQ/composio) | 🟡 **67.4** | 29.1k | 🚀 +106 | 122 | 2 days ago | `tooling` |
| 10 | [LlamaIndex](https://github.com/run-llama/llama_index) | 🟡 **65.4** | 50.6k | 🚀 +216 | 27 | 7 days ago | `data-agent` |
| 11 | [OpenAI Agents SDK](https://github.com/openai/openai-agents-python) | 🟡 **65.3** | 27.6k | 🚀 +169 | 53 | 8 days ago | `orchestration` |
| 12 | [DSPy](https://github.com/stanfordnlp/dspy) | 🟡 **59.7** | 35.7k | 🚀 +354 | 12 | 1 mo ago | `optimization` |
| 13 | [Semantic Kernel](https://github.com/microsoft/semantic-kernel) | 🟡 **57.4** | 28.2k | 📈 +46 | 34 | 15 days ago | `enterprise` |
| 14 | [PydanticAI](https://github.com/pydantic/pydantic-ai) | 🟡 **54.8** | 18.1k | 🚀 +147 | 0 | today | `structured` |
| 15 | [AG2](https://github.com/ag2ai/ag2) | 🟡 **49.7** | 4.7k | ↗️ +17 | 0 | 6 days ago | `multi-agent` |
| 16 | [Letta](https://github.com/letta-ai/letta) | 🟡 **44.1** | 23.6k | 🚀 +108 | 0 | 1 mo ago | `memory` |
| 17 | [Smolagents](https://github.com/huggingface/smolagents) | 🟡 **42.3** | 28.1k | 🚀 +138 | 0 | 1 mo ago | `lightweight` |
| 18 | [AutoGen](https://github.com/microsoft/autogen) | 🟠 **38.3** | 59.4k | 🚀 +185 | 0 | 9 mo ago | `multi-agent` |
| 19 | [Swarm](https://github.com/openai/swarm) | 🔴 **9.5** | 21.8k | 📈 +32 | 0 | — | `experimental` |

## 📂 By Category

- `data-agent`: **LlamaIndex** (65.4)
- `enterprise`: **Semantic Kernel** (57.4)
- `experimental`: **Swarm** (9.5)
- `lightweight`: **Smolagents** (42.3)
- `memory`: **Letta** (44.1)
- `multi-agent`: **CrewAI** (88.1), **Agno** (70.9), **AG2** (49.7), **AutoGen** (38.3)
- `optimization`: **DSPy** (59.7)
- `orchestration`: **LangGraph** (76.9), **Google ADK** (71.8), **Claude Agent SDK** (71.2), **OpenAI Agents SDK** (65.3)
- `pipeline`: **Haystack** (70.6)
- `structured`: **PydanticAI** (54.8)
- `tooling`: **Composio** (67.4)
- `typescript`: **Mastra** (80.5)
- `web-agent`: **BrowserUse** (83.8)

## 🔍 Top 5 — Score Breakdown

| Framework | Star Velocity | Release Freshness | Issue Health | Commit Activity | Community | Fork Ratio |
|-----------|:---:|:---:|:---:|:---:|:---:|:---:|
| **CrewAI** | 88.6 | 100.0 | 95.8 | 100 | 59.6 | 56.1 |
| **BrowserUse** | 100 | 100.0 | 95.4 | 69.0 | 63.0 | 44.4 |
| **Mastra** | 52.9 | 100.0 | 95.6 | 100 | 92.6 | 36.4 |
| **LangGraph** | 100 | 99.3 | 73.7 | 44.0 | 55.0 | 66.9 |
| **Google ADK** | 22.7 | 95.7 | 85.3 | 100 | 70.4 | 71.1 |

## 💡 Key Insights

- **Hottest framework**: CrewAI with a Pulse Score of 88.1
- **Fastest growing**: BrowserUse gained +1504 stars this week
- **Most active development**: Mastra with 915 commits in the last 4 weeks
- **Stale releases**: AutoGen, Swarm haven't released in a while

## 📦 Recent Releases

- **PydanticAI** [`v2.3.0`](https://github.com/pydantic/pydantic-ai/releases/tag/v2.3.0) — today
- **CrewAI** [`1.15.2a2`](https://github.com/crewAIInc/crewAI/releases/tag/1.15.2a2) — today *(pre-release)*
- **Claude Agent SDK** [`v2.1.198`](https://github.com/anthropics/claude-code/releases/tag/v2.1.198) — today
- **Mastra** [`@mastra/core@1.48.0`](https://github.com/mastra-ai/mastra/releases/tag/@mastra/core@1.48.0) — today
- **BrowserUse** [`0.13.3`](https://github.com/browser-use/browser-use/releases/tag/0.13.3) — today
- **LangGraph** [`1.2.7`](https://github.com/langchain-ai/langgraph/releases/tag/1.2.7) — 2 days ago
- **Composio** [`@composio/cli@0.2.32-beta.280`](https://github.com/ComposioHQ/composio/releases/tag/@composio/cli@0.2.32-beta.280) — 2 days ago *(pre-release)*
- **AG2** [`v0.14.0`](https://github.com/ag2ai/ag2/releases/tag/v0.14.0) — 6 days ago
- **LlamaIndex** [`v0.14.23`](https://github.com/run-llama/llama_index/releases/tag/v0.14.23) — 7 days ago
- **OpenAI Agents SDK** [`v0.17.7`](https://github.com/openai/openai-agents-python/releases/tag/v0.17.7) — 8 days ago

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

*Powered by GitHub Actions • Data refreshed daily • Last run: 2026-07-02 09:21 UTC*