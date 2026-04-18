# 🔬 AI Agent Framework Pulse Tracker

[![Daily Update](https://github.com/PurpleHaze2320/ai-agent-pulse/actions/workflows/track.yml/badge.svg)](https://github.com/PurpleHaze2320/ai-agent-pulse/actions/workflows/track.yml)
[![Frameworks Tracked](https://img.shields.io/badge/frameworks-19-blue)](https://github.com/PurpleHaze2320/ai-agent-pulse)
[![License: MIT](https://img.shields.io/badge/License-MIT-green.svg)](https://opensource.org/licenses/MIT)
[![GitHub stars](https://img.shields.io/github/stars/PurpleHaze2320/ai-agent-pulse?style=social)](https://github.com/PurpleHaze2320/ai-agent-pulse/stargazers)

> Automated daily tracking of the AI agent framework ecosystem's health, momentum, and trends.
> Last updated: **2026-04-18 07:18 UTC** | Tracking **19** frameworks

## How It Works

This bot runs daily via GitHub Actions and collects metrics from the GitHub API for the most important
AI agent frameworks. It computes a **Pulse Score** (0-100) based on six weighted signals: star velocity,
release freshness, issue health, commit activity, community size, and fork engagement. The result is
a living dashboard that shows which frameworks are gaining momentum and which are losing steam.

## 🏆 Pulse Leaderboard

| Rank | Framework | Pulse | Stars | ⭐ 7d | Commits (4w) | Last Release | Category |
|------|-----------|-------|-------|-------|--------------|--------------|----------|
| 1 | [Mastra](https://github.com/mastra-ai/mastra) | 🟢 **74.4** | 23.1k | 🚀 +222 | 787 | 9 days ago | `typescript` |
| 2 | [OpenAI Agents SDK](https://github.com/openai/openai-agents-python) | 🟢 **70.8** | 21.9k | 🚀 +1250 | 0 | today | `orchestration` |
| 3 | [CrewAI](https://github.com/crewAIInc/crewAI) | 🟢 **70.4** | 49.1k | 🚀 +568 | 0 | today | `multi-agent` |
| 4 | [BrowserUse](https://github.com/browser-use/browser-use) | 🟡 **69.4** | 88.3k | 🚀 +1259 | 0 | 15 days ago | `web-agent` |
| 5 | [LangGraph](https://github.com/langchain-ai/langgraph) | 🟡 **69.3** | 29.5k | 🚀 +617 | 0 | today | `orchestration` |
| 6 | [Claude Agent SDK](https://github.com/anthropics/claude-code) | 🟡 **64.6** | 115.4k | 🚀 +3024 | 0 | today | `orchestration` |
| 7 | [LlamaIndex](https://github.com/run-llama/llama_index) | 🟡 **56.6** | 48.7k | 🚀 +167 | 0 | 14 days ago | `data-agent` |
| 8 | [Agno](https://github.com/agno-agi/agno) | 🟡 **53.6** | 39.5k | 🚀 +171 | 0 | 3 days ago | `multi-agent` |
| 9 | [PydanticAI](https://github.com/pydantic/pydantic-ai) | 🟡 **53.5** | 16.4k | 🚀 +181 | 0 | today | `structured` |
| 10 | [Google ADK](https://github.com/google/adk-python) | 🟡 **53.5** | 19.1k | 🚀 +221 | 0 | 1 day ago | `orchestration` |
| 11 | [Semantic Kernel](https://github.com/microsoft/semantic-kernel) | 🟡 **49.8** | 27.7k | 📈 +49 | 0 | 10 days ago | `enterprise` |
| 12 | [Haystack](https://github.com/deepset-ai/haystack) | 🟡 **48.3** | 24.9k | 📈 +81 | 0 | 16 days ago | `pipeline` |
| 13 | [AG2](https://github.com/ag2ai/ag2) | 🟡 **47.8** | 4.4k | 📈 +33 | 0 | today | `multi-agent` |
| 14 | [DSPy](https://github.com/stanfordnlp/dspy) | 🟡 **46.5** | 33.8k | 🚀 +187 | 0 | 2 mo ago | `optimization` |
| 15 | [Letta](https://github.com/letta-ai/letta) | 🟡 **46.4** | 22.1k | 🚀 +146 | 0 | 17 days ago | `memory` |
| 16 | [Composio](https://github.com/ComposioHQ/composio) | 🟡 **44.5** | 27.8k | 📈 +88 | 0 | today | `tooling` |
| 17 | [AutoGen](https://github.com/microsoft/autogen) | 🟡 **44.2** | 57.2k | 🚀 +227 | 0 | 6 mo ago | `multi-agent` |
| 18 | [Smolagents](https://github.com/huggingface/smolagents) | 🟠 **38.3** | 26.7k | 🚀 +155 | 0 | 3 mo ago | `lightweight` |
| 19 | [Swarm](https://github.com/openai/swarm) | 🔴 **9.9** | 21.3k | 📈 +42 | 0 | — | `experimental` |

## 📂 By Category

- `data-agent`: **LlamaIndex** (56.6)
- `enterprise`: **Semantic Kernel** (49.8)
- `experimental`: **Swarm** (9.9)
- `lightweight`: **Smolagents** (38.3)
- `memory`: **Letta** (46.4)
- `multi-agent`: **CrewAI** (70.4), **Agno** (53.6), **AG2** (47.8), **AutoGen** (44.2)
- `optimization`: **DSPy** (46.5)
- `orchestration`: **OpenAI Agents SDK** (70.8), **LangGraph** (69.3), **Claude Agent SDK** (64.6), **Google ADK** (53.5)
- `pipeline`: **Haystack** (48.3)
- `structured`: **PydanticAI** (53.5)
- `tooling`: **Composio** (44.5)
- `typescript`: **Mastra** (74.4)
- `web-agent`: **BrowserUse** (69.4)

## 🔍 Top 5 — Score Breakdown

| Framework | Star Velocity | Release Freshness | Issue Health | Commit Activity | Community | Fork Ratio |
|-----------|:---:|:---:|:---:|:---:|:---:|:---:|
| **Mastra** | 39.2 | 97.0 | 94.4 | 100 | 77.0 | 33.1 |
| **OpenAI Agents SDK** | 100 | 100.0 | 96.5 | 0.0 | 49.8 | 63.9 |
| **CrewAI** | 99.5 | 100.0 | 95.9 | 0.0 | 57.0 | 54.6 |
| **BrowserUse** | 100 | 95.0 | 97.7 | 0.0 | 61.8 | 45.9 |
| **LangGraph** | 100 | 100.0 | 80.0 | 0.0 | 54.6 | 68.4 |

## 💡 Key Insights

- **Hottest framework**: Mastra with a Pulse Score of 74.4
- **Fastest growing**: Claude Agent SDK gained +3024 stars this week
- **Most active development**: Mastra with 787 commits in the last 4 weeks
- **Stale releases**: Swarm haven't released in a while

## 📦 Recent Releases

- **Composio** [`@composio/cli@0.2.25-beta.215`](https://github.com/ComposioHQ/composio/releases/tag/@composio/cli@0.2.25-beta.215) — today *(pre-release)*
- **Claude Agent SDK** [`v2.1.114`](https://github.com/anthropics/claude-code/releases/tag/v2.1.114) — today
- **PydanticAI** [`v1.84.1`](https://github.com/pydantic/pydantic-ai/releases/tag/v1.84.1) — today
- **OpenAI Agents SDK** [`v0.14.2`](https://github.com/openai/openai-agents-python/releases/tag/v0.14.2) — today
- **AG2** [`v0.12.0`](https://github.com/ag2ai/ag2/releases/tag/v0.12.0) — today
- **LangGraph** [`1.1.8`](https://github.com/langchain-ai/langgraph/releases/tag/1.1.8) — today
- **CrewAI** [`1.14.2`](https://github.com/crewAIInc/crewAI/releases/tag/1.14.2) — today
- **Google ADK** [`v1.31.0`](https://github.com/google/adk-python/releases/tag/v1.31.0) — 1 day ago
- **Agno** [`v2.5.17`](https://github.com/agno-agi/agno/releases/tag/v2.5.17) — 3 days ago
- **Mastra** [`@mastra/core@1.24.0`](https://github.com/mastra-ai/mastra/releases/tag/@mastra/core@1.24.0) — 9 days ago

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

*Powered by GitHub Actions • Data refreshed daily • Last run: 2026-04-18 07:18 UTC*