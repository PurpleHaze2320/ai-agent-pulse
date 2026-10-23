# 🔬 AI Agent Framework Pulse Tracker

[![Daily Update](https://github.com/PurpleHaze2320/ai-agent-pulse/actions/workflows/track.yml/badge.svg)](https://github.com/PurpleHaze2320/ai-agent-pulse/actions/workflows/track.yml)
[![Frameworks Tracked](https://img.shields.io/badge/frameworks-19-blue)](https://github.com/PurpleHaze2320/ai-agent-pulse)
[![License: MIT](https://img.shields.io/badge/License-MIT-green.svg)](https://opensource.org/licenses/MIT)
[![GitHub stars](https://img.shields.io/github/stars/PurpleHaze2320/ai-agent-pulse?style=social)](https://github.com/PurpleHaze2320/ai-agent-pulse/stargazers)

> Automated daily tracking of the AI agent framework ecosystem's health, momentum, and trends.
> Last updated: **2026-10-23 11:18 UTC** | Tracking **19** frameworks

## How It Works

This bot runs daily via GitHub Actions and collects metrics from the GitHub API for the most important
AI agent frameworks. It computes a **Pulse Score** (0-100) based on six weighted signals: star velocity,
release freshness, issue health, commit activity, community size, and fork engagement. The result is
a living dashboard that shows which frameworks are gaining momentum and which are losing steam.

## 🏆 Pulse Leaderboard

| Rank | Framework | Pulse | Stars | ⭐ 7d | Commits (4w) | Last Release | Category |
|------|-----------|-------|-------|-------|--------------|--------------|----------|
| 1 | [BrowserUse](https://github.com/browser-use/browser-use) | 🟢 **89.6** | 118.9k | 🚀 +776 | 147 | 7 days ago | `web-agent` |
| 2 | [LangGraph](https://github.com/langchain-ai/langgraph) | 🟢 **84.7** | 43.8k | 🚀 +415 | 115 | 3 days ago | `orchestration` |
| 3 | [CrewAI](https://github.com/crewAIInc/crewAI) | 🟢 **78.8** | 60.0k | 🚀 +264 | 117 | 9 days ago | `multi-agent` |
| 4 | [Mastra](https://github.com/mastra-ai/mastra) | 🟢 **77.0** | 29.0k | 🚀 +183 | 2293 | 1 day ago | `typescript` |
| 5 | [Claude Agent SDK](https://github.com/anthropics/claude-code) | 🟢 **77.0** | 153.0k | 🚀 +1802 | 55 | today | `orchestration` |
| 6 | [OpenAI Agents SDK](https://github.com/openai/openai-agents-python) | 🟢 **76.8** | 30.2k | 🚀 +162 | 144 | 8 days ago | `orchestration` |
| 7 | [Google ADK](https://github.com/google/adk-python) | 🟢 **74.6** | 22.0k | 📈 +98 | 524 | 9 days ago | `orchestration` |
| 8 | [PydanticAI](https://github.com/pydantic/pydantic-ai) | 🟢 **74.2** | 20.8k | 🚀 +149 | 1059 | today | `structured` |
| 9 | [Agno](https://github.com/agno-agi/agno) | 🟢 **71.1** | 42.9k | 🚀 +107 | 147 | today | `multi-agent` |
| 10 | [AG2](https://github.com/ag2ai/ag2) | 🟡 **69.8** | 5.0k | ↗️ +14 | 125 | 1 day ago | `multi-agent` |
| 11 | [Composio](https://github.com/ComposioHQ/composio) | 🟡 **67.8** | 30.7k | 🚀 +110 | 355 | today | `tooling` |
| 12 | [DSPy](https://github.com/stanfordnlp/dspy) | 🟡 **61.1** | 38.8k | 📈 +96 | 64 | 10 days ago | `optimization` |
| 13 | [LlamaIndex](https://github.com/run-llama/llama_index) | 🟡 **56.6** | 52.6k | 🚀 +116 | 15 | 1 mo ago | `data-agent` |
| 14 | [Semantic Kernel](https://github.com/microsoft/semantic-kernel) | 🟡 **54.5** | 28.7k | 📈 +27 | 24 | 16 days ago | `enterprise` |
| 15 | [Haystack](https://github.com/deepset-ai/haystack) | 🟡 **51.9** | 26.8k | 📈 +71 | 0 | 1 day ago | `pipeline` |
| 16 | [Letta](https://github.com/letta-ai/letta) | 🟠 **35.4** | 25.2k | 📈 +72 | 1 | 5 mo ago | `memory` |
| 17 | [Smolagents](https://github.com/huggingface/smolagents) | 🟠 **34.3** | 30.0k | 🚀 +131 | 3 | 4 mo ago | `lightweight` |
| 18 | [AutoGen](https://github.com/microsoft/autogen) | 🟠 **32.2** | 61.5k | 📈 +94 | 1 | 1y ago | `multi-agent` |
| 19 | [Swarm](https://github.com/openai/swarm) | 🔴 **9.0** | 22.1k | ↗️ +11 | 0 | — | `experimental` |

## 📂 By Category

- `data-agent`: **LlamaIndex** (56.6)
- `enterprise`: **Semantic Kernel** (54.5)
- `experimental`: **Swarm** (9.0)
- `lightweight`: **Smolagents** (34.3)
- `memory`: **Letta** (35.4)
- `multi-agent`: **CrewAI** (78.8), **Agno** (71.1), **AG2** (69.8), **AutoGen** (32.2)
- `optimization`: **DSPy** (61.1)
- `orchestration`: **LangGraph** (84.7), **Claude Agent SDK** (77.0), **OpenAI Agents SDK** (76.8), **Google ADK** (74.6)
- `pipeline`: **Haystack** (51.9)
- `structured`: **PydanticAI** (74.2)
- `tooling`: **Composio** (67.8)
- `typescript`: **Mastra** (77.0)
- `web-agent`: **BrowserUse** (89.6)

## 🔍 Top 5 — Score Breakdown

| Framework | Star Velocity | Release Freshness | Issue Health | Commit Activity | Community | Fork Ratio |
|-----------|:---:|:---:|:---:|:---:|:---:|:---:|
| **BrowserUse** | 100 | 97.7 | 89.5 | 100 | 72.0 | 44.4 |
| **LangGraph** | 82.1 | 99.0 | 78.8 | 100 | 57.0 | 68.6 |
| **CrewAI** | 53.3 | 97.0 | 87.3 | 100 | 71.2 | 59.0 |
| **Mastra** | 36.8 | 99.7 | 95.3 | 100 | 93.6 | 41.9 |
| **Claude Agent SDK** | 100 | 100.0 | 85.4 | 55.0 | 11.4 | 70.0 |

## 💡 Key Insights

- **Hottest framework**: BrowserUse with a Pulse Score of 89.6
- **Fastest growing**: Claude Agent SDK gained +1802 stars this week
- **Most active development**: Mastra with 2293 commits in the last 4 weeks
- **Stale releases**: AutoGen, Swarm haven't released in a while

## 📦 Recent Releases

- **Composio** [`@composio/cli@0.5.1-beta.498`](https://github.com/ComposioHQ/composio/releases/tag/@composio/cli@0.5.1-beta.498) — today *(pre-release)*
- **PydanticAI** [`v2.60.0`](https://github.com/pydantic/pydantic-ai/releases/tag/v2.60.0) — today
- **Claude Agent SDK** [`v2.1.309`](https://github.com/anthropics/claude-code/releases/tag/v2.1.309) — today
- **Agno** [`v3.1.9`](https://github.com/agno-agi/agno/releases/tag/v3.1.9) — today
- **AG2** [`v1.2.1`](https://github.com/ag2ai/ag2/releases/tag/v1.2.1) — 1 day ago
- **Haystack** [`v3.4.1`](https://github.com/deepset-ai/haystack/releases/tag/v3.4.1) — 1 day ago
- **Mastra** [`@mastra/core@1.79.0`](https://github.com/mastra-ai/mastra/releases/tag/@mastra/core@1.79.0) — 1 day ago
- **LangGraph** [`cli==0.4.37`](https://github.com/langchain-ai/langgraph/releases/tag/cli==0.4.37) — 3 days ago
- **BrowserUse** [`0.13.13`](https://github.com/browser-use/browser-use/releases/tag/0.13.13) — 7 days ago
- **OpenAI Agents SDK** [`v0.24.0`](https://github.com/openai/openai-agents-python/releases/tag/v0.24.0) — 8 days ago

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

*Powered by GitHub Actions • Data refreshed daily • Last run: 2026-10-23 11:18 UTC*