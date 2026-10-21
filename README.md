# 🔬 AI Agent Framework Pulse Tracker

[![Daily Update](https://github.com/PurpleHaze2320/ai-agent-pulse/actions/workflows/track.yml/badge.svg)](https://github.com/PurpleHaze2320/ai-agent-pulse/actions/workflows/track.yml)
[![Frameworks Tracked](https://img.shields.io/badge/frameworks-19-blue)](https://github.com/PurpleHaze2320/ai-agent-pulse)
[![License: MIT](https://img.shields.io/badge/License-MIT-green.svg)](https://opensource.org/licenses/MIT)
[![GitHub stars](https://img.shields.io/github/stars/PurpleHaze2320/ai-agent-pulse?style=social)](https://github.com/PurpleHaze2320/ai-agent-pulse/stargazers)

> Automated daily tracking of the AI agent framework ecosystem's health, momentum, and trends.
> Last updated: **2026-10-21 11:28 UTC** | Tracking **19** frameworks

## How It Works

This bot runs daily via GitHub Actions and collects metrics from the GitHub API for the most important
AI agent frameworks. It computes a **Pulse Score** (0-100) based on six weighted signals: star velocity,
release freshness, issue health, commit activity, community size, and fork engagement. The result is
a living dashboard that shows which frameworks are gaining momentum and which are losing steam.

## 🏆 Pulse Leaderboard

| Rank | Framework | Pulse | Stars | ⭐ 7d | Commits (4w) | Last Release | Category |
|------|-----------|-------|-------|-------|--------------|--------------|----------|
| 1 | [BrowserUse](https://github.com/browser-use/browser-use) | 🟢 **89.7** | 118.7k | 🚀 +797 | 142 | 5 days ago | `web-agent` |
| 2 | [CrewAI](https://github.com/crewAIInc/crewAI) | 🟢 **79.2** | 59.9k | 🚀 +269 | 101 | 7 days ago | `multi-agent` |
| 3 | [OpenAI Agents SDK](https://github.com/openai/openai-agents-python) | 🟢 **77.2** | 30.2k | 🚀 +169 | 136 | 6 days ago | `orchestration` |
| 4 | [Claude Agent SDK](https://github.com/anthropics/claude-code) | 🟢 **76.3** | 152.7k | 🚀 +1917 | 52 | today | `orchestration` |
| 5 | [Mastra](https://github.com/mastra-ai/mastra) | 🟢 **75.9** | 29.0k | 🚀 +161 | 2087 | 5 days ago | `typescript` |
| 6 | [Google ADK](https://github.com/google/adk-python) | 🟢 **74.9** | 21.9k | 🚀 +103 | 486 | 7 days ago | `orchestration` |
| 7 | [PydanticAI](https://github.com/pydantic/pydantic-ai) | 🟢 **74.5** | 20.8k | 🚀 +159 | 876 | today | `structured` |
| 8 | [AG2](https://github.com/ag2ai/ag2) | 🟡 **69.2** | 5.0k | ↗️ +13 | 122 | 10 days ago | `multi-agent` |
| 9 | [Composio](https://github.com/ComposioHQ/composio) | 🟡 **68.0** | 30.7k | 🚀 +116 | 285 | today | `tooling` |
| 10 | [LangGraph](https://github.com/langchain-ai/langgraph) | 🟡 **63.7** | 43.6k | 🚀 +388 | 0 | 1 day ago | `orchestration` |
| 11 | [DSPy](https://github.com/stanfordnlp/dspy) | 🟡 **59.3** | 38.7k | 📈 +81 | 57 | 8 days ago | `optimization` |
| 12 | [LlamaIndex](https://github.com/run-llama/llama_index) | 🟡 **56.3** | 52.6k | 🚀 +105 | 15 | 29 days ago | `data-agent` |
| 13 | [Semantic Kernel](https://github.com/microsoft/semantic-kernel) | 🟡 **54.3** | 28.7k | 📈 +23 | 23 | 14 days ago | `enterprise` |
| 14 | [Agno](https://github.com/agno-agi/agno) | 🟡 **51.8** | 42.8k | 🚀 +125 | 0 | today | `multi-agent` |
| 15 | [Haystack](https://github.com/deepset-ai/haystack) | 🟡 **51.3** | 26.8k | 📈 +64 | 0 | 6 days ago | `pipeline` |
| 16 | [Letta](https://github.com/letta-ai/letta) | 🟠 **36.0** | 25.2k | 📈 +85 | 1 | 5 mo ago | `memory` |
| 17 | [Smolagents](https://github.com/huggingface/smolagents) | 🟠 **34.0** | 30.0k | 🚀 +119 | 3 | 4 mo ago | `lightweight` |
| 18 | [AutoGen](https://github.com/microsoft/autogen) | 🟠 **32.8** | 61.5k | 🚀 +110 | 1 | 1y ago | `multi-agent` |
| 19 | [Swarm](https://github.com/openai/swarm) | 🔴 **9.0** | 22.1k | ↗️ +8 | 0 | — | `experimental` |

## 📂 By Category

- `data-agent`: **LlamaIndex** (56.3)
- `enterprise`: **Semantic Kernel** (54.3)
- `experimental`: **Swarm** (9.0)
- `lightweight`: **Smolagents** (34.0)
- `memory`: **Letta** (36.0)
- `multi-agent`: **CrewAI** (79.2), **AG2** (69.2), **Agno** (51.8), **AutoGen** (32.8)
- `optimization`: **DSPy** (59.3)
- `orchestration`: **OpenAI Agents SDK** (77.2), **Claude Agent SDK** (76.3), **Google ADK** (74.9), **LangGraph** (63.7)
- `pipeline`: **Haystack** (51.3)
- `structured`: **PydanticAI** (74.5)
- `tooling`: **Composio** (68.0)
- `typescript`: **Mastra** (75.9)
- `web-agent`: **BrowserUse** (89.7)

## 🔍 Top 5 — Score Breakdown

| Framework | Star Velocity | Release Freshness | Issue Health | Commit Activity | Community | Fork Ratio |
|-----------|:---:|:---:|:---:|:---:|:---:|:---:|
| **BrowserUse** | 100 | 98.3 | 89.4 | 100 | 72.0 | 44.4 |
| **CrewAI** | 54.1 | 97.7 | 87.8 | 100 | 70.8 | 58.8 |
| **OpenAI Agents SDK** | 32.5 | 98.0 | 99.3 | 100 | 80.4 | 65.1 |
| **Claude Agent SDK** | 100 | 100.0 | 85.4 | 52.0 | 11.4 | 69.7 |
| **Mastra** | 33.6 | 98.3 | 95.4 | 100 | 93.6 | 41.8 |

## 💡 Key Insights

- **Hottest framework**: BrowserUse with a Pulse Score of 89.7
- **Fastest growing**: Claude Agent SDK gained +1917 stars this week
- **Most active development**: Mastra with 2087 commits in the last 4 weeks
- **Stale releases**: AutoGen, Swarm haven't released in a while

## 📦 Recent Releases

- **PydanticAI** [`v2.59.0`](https://github.com/pydantic/pydantic-ai/releases/tag/v2.59.0) — today
- **Claude Agent SDK** [`v2.1.306`](https://github.com/anthropics/claude-code/releases/tag/v2.1.306) — today
- **Composio** [`@composio/cli@0.4.6-beta.480`](https://github.com/ComposioHQ/composio/releases/tag/@composio/cli@0.4.6-beta.480) — today *(pre-release)*
- **Agno** [`v3.1.7`](https://github.com/agno-agi/agno/releases/tag/v3.1.7) — today
- **LangGraph** [`cli==0.4.37`](https://github.com/langchain-ai/langgraph/releases/tag/cli==0.4.37) — 1 day ago
- **Mastra** [`@mastra/core@1.78.0`](https://github.com/mastra-ai/mastra/releases/tag/@mastra/core@1.78.0) — 5 days ago
- **BrowserUse** [`0.13.13`](https://github.com/browser-use/browser-use/releases/tag/0.13.13) — 5 days ago
- **Haystack** [`v3.4.0`](https://github.com/deepset-ai/haystack/releases/tag/v3.4.0) — 6 days ago
- **OpenAI Agents SDK** [`v0.24.0`](https://github.com/openai/openai-agents-python/releases/tag/v0.24.0) — 6 days ago
- **CrewAI** [`1.15.28`](https://github.com/crewAIInc/crewAI/releases/tag/1.15.28) — 7 days ago

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

*Powered by GitHub Actions • Data refreshed daily • Last run: 2026-10-21 11:28 UTC*