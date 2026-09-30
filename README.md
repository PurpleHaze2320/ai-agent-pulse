# 🔬 AI Agent Framework Pulse Tracker

[![Daily Update](https://github.com/PurpleHaze2320/ai-agent-pulse/actions/workflows/track.yml/badge.svg)](https://github.com/PurpleHaze2320/ai-agent-pulse/actions/workflows/track.yml)
[![Frameworks Tracked](https://img.shields.io/badge/frameworks-19-blue)](https://github.com/PurpleHaze2320/ai-agent-pulse)
[![License: MIT](https://img.shields.io/badge/License-MIT-green.svg)](https://opensource.org/licenses/MIT)
[![GitHub stars](https://img.shields.io/github/stars/PurpleHaze2320/ai-agent-pulse?style=social)](https://github.com/PurpleHaze2320/ai-agent-pulse/stargazers)

> Automated daily tracking of the AI agent framework ecosystem's health, momentum, and trends.
> Last updated: **2026-09-30 12:14 UTC** | Tracking **19** frameworks

## How It Works

This bot runs daily via GitHub Actions and collects metrics from the GitHub API for the most important
AI agent frameworks. It computes a **Pulse Score** (0-100) based on six weighted signals: star velocity,
release freshness, issue health, commit activity, community size, and fork engagement. The result is
a living dashboard that shows which frameworks are gaining momentum and which are losing steam.

## 🏆 Pulse Leaderboard

| Rank | Framework | Pulse | Stars | ⭐ 7d | Commits (4w) | Last Release | Category |
|------|-----------|-------|-------|-------|--------------|--------------|----------|
| 1 | [Claude Agent SDK](https://github.com/anthropics/claude-code) | 🟢 **85.8** | 148.7k | 🚀 +920 | 133 | today | `orchestration` |
| 2 | [CrewAI](https://github.com/crewAIInc/crewAI) | 🟢 **79.3** | 59.2k | 🚀 +281 | 91 | 1 day ago | `multi-agent` |
| 3 | [BrowserUse](https://github.com/browser-use/browser-use) | 🟢 **77.3** | 116.8k | 🚀 +759 | 44 | 26 days ago | `web-agent` |
| 4 | [Mastra](https://github.com/mastra-ai/mastra) | 🟢 **76.8** | 28.4k | 🚀 +168 | 1925 | today | `typescript` |
| 5 | [OpenAI Agents SDK](https://github.com/openai/openai-agents-python) | 🟢 **75.8** | 29.8k | 🚀 +132 | 212 | 12 days ago | `orchestration` |
| 6 | [PydanticAI](https://github.com/pydantic/pydantic-ai) | 🟢 **74.0** | 20.3k | 🚀 +154 | 565 | today | `structured` |
| 7 | [Google ADK](https://github.com/google/adk-python) | 🟢 **73.4** | 21.7k | 📈 +77 | 358 | 4 days ago | `orchestration` |
| 8 | [Haystack](https://github.com/deepset-ai/haystack) | 🟢 **70.8** | 26.6k | 📈 +51 | 210 | 6 days ago | `pipeline` |
| 9 | [Agno](https://github.com/agno-agi/agno) | 🟡 **69.5** | 42.4k | 📈 +80 | 103 | 6 days ago | `multi-agent` |
| 10 | [Composio](https://github.com/ComposioHQ/composio) | 🟡 **66.9** | 30.4k | 📈 +74 | 322 | today | `tooling` |
| 11 | [LangGraph](https://github.com/langchain-ai/langgraph) | 🟡 **64.5** | 42.5k | 🚀 +337 | 23 | 6 days ago | `orchestration` |
| 12 | [AG2](https://github.com/ag2ai/ag2) | 🟡 **63.2** | 5.0k | ↗️ +17 | 66 | today | `multi-agent` |
| 13 | [DSPy](https://github.com/stanfordnlp/dspy) | 🟡 **62.7** | 38.4k | 🚀 +210 | 46 | 5 days ago | `optimization` |
| 14 | [LlamaIndex](https://github.com/run-llama/llama_index) | 🟡 **58.7** | 52.4k | 📈 +79 | 23 | 8 days ago | `data-agent` |
| 15 | [Semantic Kernel](https://github.com/microsoft/semantic-kernel) | 🟡 **50.1** | 28.6k | ↗️ +20 | 7 | 26 days ago | `enterprise` |
| 16 | [Letta](https://github.com/letta-ai/letta) | 🟠 **39.4** | 25.0k | 🚀 +126 | 2 | 4 mo ago | `memory` |
| 17 | [Smolagents](https://github.com/huggingface/smolagents) | 🟠 **37.1** | 29.6k | 🚀 +148 | 4 | 4 mo ago | `lightweight` |
| 18 | [AutoGen](https://github.com/microsoft/autogen) | 🟠 **33.4** | 61.2k | 🚀 +122 | 0 | 1y ago | `multi-agent` |
| 19 | [Swarm](https://github.com/openai/swarm) | 🔴 **9.6** | 22.0k | 📈 +23 | 0 | — | `experimental` |

## 📂 By Category

- `data-agent`: **LlamaIndex** (58.7)
- `enterprise`: **Semantic Kernel** (50.1)
- `experimental`: **Swarm** (9.6)
- `lightweight`: **Smolagents** (37.1)
- `memory`: **Letta** (39.4)
- `multi-agent`: **CrewAI** (79.3), **Agno** (69.5), **AG2** (63.2), **AutoGen** (33.4)
- `optimization`: **DSPy** (62.7)
- `orchestration`: **Claude Agent SDK** (85.8), **OpenAI Agents SDK** (75.8), **Google ADK** (73.4), **LangGraph** (64.5)
- `pipeline`: **Haystack** (70.8)
- `structured`: **PydanticAI** (74.0)
- `tooling`: **Composio** (66.9)
- `typescript`: **Mastra** (76.8)
- `web-agent`: **BrowserUse** (77.3)

## 🔍 Top 5 — Score Breakdown

| Framework | Star Velocity | Release Freshness | Issue Health | Commit Activity | Community | Fork Ratio |
|-----------|:---:|:---:|:---:|:---:|:---:|:---:|
| **Claude Agent SDK** | 100 | 100.0 | 86.3 | 100 | 11.4 | 67.5 |
| **CrewAI** | 59.5 | 99.7 | 91.7 | 91.0 | 67.2 | 58.2 |
| **BrowserUse** | 100 | 91.3 | 90.6 | 44.0 | 72.0 | 44.1 |
| **Mastra** | 36.4 | 100.0 | 95.5 | 100 | 93.4 | 40.6 |
| **OpenAI Agents SDK** | 28.8 | 96.0 | 99.9 | 100 | 79.2 | 65.0 |

## 💡 Key Insights

- **Hottest framework**: Claude Agent SDK with a Pulse Score of 85.8
- **Fastest growing**: Claude Agent SDK gained +920 stars this week
- **Most active development**: Mastra with 1925 commits in the last 4 weeks
- **Stale releases**: AutoGen, Swarm haven't released in a while

## 📦 Recent Releases

- **Composio** [`@composio/cli@0.4.3-beta.409`](https://github.com/ComposioHQ/composio/releases/tag/@composio/cli@0.4.3-beta.409) — today *(pre-release)*
- **Mastra** [`@mastra/core@1.72.0`](https://github.com/mastra-ai/mastra/releases/tag/@mastra/core@1.72.0) — today
- **PydanticAI** [`v2.52.0`](https://github.com/pydantic/pydantic-ai/releases/tag/v2.52.0) — today
- **AG2** [`v1.1.1`](https://github.com/ag2ai/ag2/releases/tag/v1.1.1) — today
- **Claude Agent SDK** [`v2.1.285`](https://github.com/anthropics/claude-code/releases/tag/v2.1.285) — today
- **CrewAI** [`1.15.23`](https://github.com/crewAIInc/crewAI/releases/tag/1.15.23) — 1 day ago
- **Google ADK** [`v2.10.0`](https://github.com/google/adk-python/releases/tag/v2.10.0) — 4 days ago
- **DSPy** [`3.4.0`](https://github.com/stanfordnlp/dspy/releases/tag/3.4.0) — 5 days ago
- **Haystack** [`v3.2.0`](https://github.com/deepset-ai/haystack/releases/tag/v3.2.0) — 6 days ago
- **LangGraph** [`cli==0.4.32.dev0`](https://github.com/langchain-ai/langgraph/releases/tag/cli==0.4.32.dev0) — 6 days ago

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

*Powered by GitHub Actions • Data refreshed daily • Last run: 2026-09-30 12:14 UTC*