# 🔬 AI Agent Framework Pulse Tracker

[![Daily Update](https://github.com/PurpleHaze2320/ai-agent-pulse/actions/workflows/track.yml/badge.svg)](https://github.com/PurpleHaze2320/ai-agent-pulse/actions/workflows/track.yml)
[![Frameworks Tracked](https://img.shields.io/badge/frameworks-19-blue)](https://github.com/PurpleHaze2320/ai-agent-pulse)
[![License: MIT](https://img.shields.io/badge/License-MIT-green.svg)](https://opensource.org/licenses/MIT)
[![GitHub stars](https://img.shields.io/github/stars/PurpleHaze2320/ai-agent-pulse?style=social)](https://github.com/PurpleHaze2320/ai-agent-pulse/stargazers)

> Automated daily tracking of the AI agent framework ecosystem's health, momentum, and trends.
> Last updated: **2026-10-01 12:49 UTC** | Tracking **19** frameworks

## How It Works

This bot runs daily via GitHub Actions and collects metrics from the GitHub API for the most important
AI agent frameworks. It computes a **Pulse Score** (0-100) based on six weighted signals: star velocity,
release freshness, issue health, commit activity, community size, and fork engagement. The result is
a living dashboard that shows which frameworks are gaining momentum and which are losing steam.

## 🏆 Pulse Leaderboard

| Rank | Framework | Pulse | Stars | ⭐ 7d | Commits (4w) | Last Release | Category |
|------|-----------|-------|-------|-------|--------------|--------------|----------|
| 1 | [Claude Agent SDK](https://github.com/anthropics/claude-code) | 🟢 **85.8** | 148.8k | 🚀 +912 | 138 | today | `orchestration` |
| 2 | [CrewAI](https://github.com/crewAIInc/crewAI) | 🟢 **80.0** | 59.3k | 🚀 +278 | 96 | 2 days ago | `multi-agent` |
| 3 | [BrowserUse](https://github.com/browser-use/browser-use) | 🟢 **77.2** | 116.9k | 🚀 +742 | 44 | 27 days ago | `web-agent` |
| 4 | [Mastra](https://github.com/mastra-ai/mastra) | 🟢 **76.5** | 28.5k | 🚀 +160 | 2005 | 1 day ago | `typescript` |
| 5 | [OpenAI Agents SDK](https://github.com/openai/openai-agents-python) | 🟢 **75.5** | 29.8k | 🚀 +126 | 235 | 13 days ago | `orchestration` |
| 6 | [Google ADK](https://github.com/google/adk-python) | 🟢 **72.9** | 21.7k | 📈 +65 | 376 | 5 days ago | `orchestration` |
| 7 | [Agno](https://github.com/agno-agi/agno) | 🟢 **71.4** | 42.5k | 🚀 +120 | 108 | today | `multi-agent` |
| 8 | [Haystack](https://github.com/deepset-ai/haystack) | 🟢 **71.1** | 26.6k | 📈 +50 | 219 | today | `pipeline` |
| 9 | [LangGraph](https://github.com/langchain-ai/langgraph) | 🟡 **69.0** | 42.6k | 🚀 +332 | 47 | 7 days ago | `orchestration` |
| 10 | [AG2](https://github.com/ag2ai/ag2) | 🟡 **63.2** | 5.0k | ↗️ +16 | 67 | 1 day ago | `multi-agent` |
| 11 | [DSPy](https://github.com/stanfordnlp/dspy) | 🟡 **63.1** | 38.4k | 🚀 +195 | 51 | 6 days ago | `optimization` |
| 12 | [LlamaIndex](https://github.com/run-llama/llama_index) | 🟡 **58.4** | 52.4k | 📈 +73 | 23 | 9 days ago | `data-agent` |
| 13 | [PydanticAI](https://github.com/pydantic/pydantic-ai) | 🟡 **54.4** | 20.3k | 🚀 +167 | 0 | 1 day ago | `structured` |
| 14 | [Semantic Kernel](https://github.com/microsoft/semantic-kernel) | 🟡 **51.2** | 28.6k | 📈 +24 | 12 | 27 days ago | `enterprise` |
| 15 | [Composio](https://github.com/ComposioHQ/composio) | 🟡 **47.0** | 30.4k | 📈 +81 | 0 | 1 day ago | `tooling` |
| 16 | [Letta](https://github.com/letta-ai/letta) | 🟠 **39.4** | 25.0k | 🚀 +128 | 2 | 4 mo ago | `memory` |
| 17 | [Smolagents](https://github.com/huggingface/smolagents) | 🟠 **36.9** | 29.6k | 🚀 +147 | 4 | 4 mo ago | `lightweight` |
| 18 | [AutoGen](https://github.com/microsoft/autogen) | 🟠 **32.9** | 61.2k | 🚀 +108 | 0 | 1y ago | `multi-agent` |
| 19 | [Swarm](https://github.com/openai/swarm) | 🔴 **9.5** | 22.0k | ↗️ +20 | 0 | — | `experimental` |

## 📂 By Category

- `data-agent`: **LlamaIndex** (58.4)
- `enterprise`: **Semantic Kernel** (51.2)
- `experimental`: **Swarm** (9.5)
- `lightweight`: **Smolagents** (36.9)
- `memory`: **Letta** (39.4)
- `multi-agent`: **CrewAI** (80.0), **Agno** (71.4), **AG2** (63.2), **AutoGen** (32.9)
- `optimization`: **DSPy** (63.1)
- `orchestration`: **Claude Agent SDK** (85.8), **OpenAI Agents SDK** (75.5), **Google ADK** (72.9), **LangGraph** (69.0)
- `pipeline`: **Haystack** (71.1)
- `structured`: **PydanticAI** (54.4)
- `tooling`: **Composio** (47.0)
- `typescript`: **Mastra** (76.5)
- `web-agent`: **BrowserUse** (77.2)

## 🔍 Top 5 — Score Breakdown

| Framework | Star Velocity | Release Freshness | Issue Health | Commit Activity | Community | Fork Ratio |
|-----------|:---:|:---:|:---:|:---:|:---:|:---:|
| **Claude Agent SDK** | 100 | 100.0 | 86.2 | 100 | 11.4 | 67.5 |
| **CrewAI** | 58.7 | 99.3 | 91.6 | 96.0 | 67.2 | 58.2 |
| **BrowserUse** | 100 | 91.0 | 90.6 | 44.0 | 72.0 | 44.1 |
| **Mastra** | 35.3 | 99.7 | 95.8 | 100 | 93.4 | 40.7 |
| **OpenAI Agents SDK** | 27.9 | 95.7 | 99.9 | 100 | 79.2 | 65.0 |

## 💡 Key Insights

- **Hottest framework**: Claude Agent SDK with a Pulse Score of 85.8
- **Fastest growing**: Claude Agent SDK gained +912 stars this week
- **Most active development**: Mastra with 2005 commits in the last 4 weeks
- **Stale releases**: AutoGen, Swarm haven't released in a while

## 📦 Recent Releases

- **Haystack** [`v3.3.0`](https://github.com/deepset-ai/haystack/releases/tag/v3.3.0) — today
- **Agno** [`v3.1.0`](https://github.com/agno-agi/agno/releases/tag/v3.1.0) — today
- **Claude Agent SDK** [`v2.1.286`](https://github.com/anthropics/claude-code/releases/tag/v2.1.286) — today
- **Composio** [`@composio/cli@0.4.3-beta.409`](https://github.com/ComposioHQ/composio/releases/tag/@composio/cli@0.4.3-beta.409) — 1 day ago *(pre-release)*
- **Mastra** [`@mastra/core@1.72.0`](https://github.com/mastra-ai/mastra/releases/tag/@mastra/core@1.72.0) — 1 day ago
- **PydanticAI** [`v2.52.0`](https://github.com/pydantic/pydantic-ai/releases/tag/v2.52.0) — 1 day ago
- **AG2** [`v1.1.1`](https://github.com/ag2ai/ag2/releases/tag/v1.1.1) — 1 day ago
- **CrewAI** [`1.15.23`](https://github.com/crewAIInc/crewAI/releases/tag/1.15.23) — 2 days ago
- **Google ADK** [`v2.10.0`](https://github.com/google/adk-python/releases/tag/v2.10.0) — 5 days ago
- **DSPy** [`3.4.0`](https://github.com/stanfordnlp/dspy/releases/tag/3.4.0) — 6 days ago

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

*Powered by GitHub Actions • Data refreshed daily • Last run: 2026-10-01 12:49 UTC*