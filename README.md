# 🔬 AI Agent Framework Pulse Tracker

[![Daily Update](https://github.com/PurpleHaze2320/ai-agent-pulse/actions/workflows/track.yml/badge.svg)](https://github.com/PurpleHaze2320/ai-agent-pulse/actions/workflows/track.yml)
[![Frameworks Tracked](https://img.shields.io/badge/frameworks-19-blue)](https://github.com/PurpleHaze2320/ai-agent-pulse)
[![License: MIT](https://img.shields.io/badge/License-MIT-green.svg)](https://opensource.org/licenses/MIT)
[![GitHub stars](https://img.shields.io/github/stars/PurpleHaze2320/ai-agent-pulse?style=social)](https://github.com/PurpleHaze2320/ai-agent-pulse/stargazers)

> Automated daily tracking of the AI agent framework ecosystem's health, momentum, and trends.
> Last updated: **2026-08-21 06:54 UTC** | Tracking **19** frameworks

## How It Works

This bot runs daily via GitHub Actions and collects metrics from the GitHub API for the most important
AI agent frameworks. It computes a **Pulse Score** (0-100) based on six weighted signals: star velocity,
release freshness, issue health, commit activity, community size, and fork engagement. The result is
a living dashboard that shows which frameworks are gaining momentum and which are losing steam.

## 🏆 Pulse Leaderboard

| Rank | Framework | Pulse | Stars | ⭐ 7d | Commits (4w) | Last Release | Category |
|------|-----------|-------|-------|-------|--------------|--------------|----------|
| 1 | [BrowserUse](https://github.com/browser-use/browser-use) | 🟢 **89.9** | 109.9k | 🚀 +769 | 118 | 4 days ago | `web-agent` |
| 2 | [CrewAI](https://github.com/crewAIInc/crewAI) | 🟢 **82.5** | 57.4k | 🚀 +338 | 97 | 1 day ago | `multi-agent` |
| 3 | [OpenAI Agents SDK](https://github.com/openai/openai-agents-python) | 🟢 **77.4** | 28.8k | 🚀 +182 | 367 | 1 day ago | `orchestration` |
| 4 | [Mastra](https://github.com/mastra-ai/mastra) | 🟢 **76.3** | 27.3k | 🚀 +156 | 1571 | 1 day ago | `typescript` |
| 5 | [LangGraph](https://github.com/langchain-ai/langgraph) | 🟢 **74.7** | 40.1k | 🚀 +488 | 35 | 1 day ago | `orchestration` |
| 6 | [PydanticAI](https://github.com/pydantic/pydantic-ai) | 🟢 **74.7** | 19.4k | 🚀 +142 | 266 | today | `structured` |
| 7 | [Google ADK](https://github.com/google/adk-python) | 🟢 **74.2** | 21.2k | 🚀 +108 | 456 | 3 days ago | `orchestration` |
| 8 | [Haystack](https://github.com/deepset-ai/haystack) | 🟢 **70.8** | 26.3k | 📈 +61 | 191 | 2 days ago | `pipeline` |
| 9 | [Claude Agent SDK](https://github.com/anthropics/claude-code) | 🟡 **68.4** | 142.2k | 🚀 +792 | 17 | today | `orchestration` |
| 10 | [DSPy](https://github.com/stanfordnlp/dspy) | 🟡 **68.4** | 37.5k | 🚀 +281 | 58 | 17 days ago | `optimization` |
| 11 | [Composio](https://github.com/ComposioHQ/composio) | 🟡 **68.3** | 29.8k | 🚀 +115 | 317 | today | `tooling` |
| 12 | [LlamaIndex](https://github.com/run-llama/llama_index) | 🟡 **63.8** | 51.8k | 🚀 +145 | 28 | 1 day ago | `data-agent` |
| 13 | [AG2](https://github.com/ag2ai/ag2) | 🟡 **63.0** | 4.9k | 📈 +26 | 65 | 6 days ago | `multi-agent` |
| 14 | [Agno](https://github.com/agno-agi/agno) | 🟡 **60.6** | 41.8k | 🚀 +111 | 45 | today | `multi-agent` |
| 15 | [Semantic Kernel](https://github.com/microsoft/semantic-kernel) | 🟡 **54.4** | 28.5k | 📈 +26 | 19 | 2 days ago | `enterprise` |
| 16 | [Letta](https://github.com/letta-ai/letta) | 🟡 **40.9** | 24.3k | 📈 +92 | 4 | 3 mo ago | `memory` |
| 17 | [Smolagents](https://github.com/huggingface/smolagents) | 🟠 **37.8** | 28.9k | 🚀 +114 | 0 | 2 mo ago | `lightweight` |
| 18 | [AutoGen](https://github.com/microsoft/autogen) | 🟠 **34.4** | 60.6k | 🚀 +136 | 0 | 10 mo ago | `multi-agent` |
| 19 | [Swarm](https://github.com/openai/swarm) | 🔴 **9.1** | 21.9k | ↗️ +6 | 0 | — | `experimental` |

## 📂 By Category

- `data-agent`: **LlamaIndex** (63.8)
- `enterprise`: **Semantic Kernel** (54.4)
- `experimental`: **Swarm** (9.1)
- `lightweight`: **Smolagents** (37.8)
- `memory`: **Letta** (40.9)
- `multi-agent`: **CrewAI** (82.5), **AG2** (63.0), **Agno** (60.6), **AutoGen** (34.4)
- `optimization`: **DSPy** (68.4)
- `orchestration`: **OpenAI Agents SDK** (77.4), **LangGraph** (74.7), **Google ADK** (74.2), **Claude Agent SDK** (68.4)
- `pipeline`: **Haystack** (70.8)
- `structured`: **PydanticAI** (74.7)
- `tooling`: **Composio** (68.3)
- `typescript`: **Mastra** (76.3)
- `web-agent`: **BrowserUse** (89.9)

## 🔍 Top 5 — Score Breakdown

| Framework | Star Velocity | Release Freshness | Issue Health | Commit Activity | Community | Fork Ratio |
|-----------|:---:|:---:|:---:|:---:|:---:|:---:|
| **BrowserUse** | 100 | 98.7 | 93.6 | 100 | 67.0 | 44.0 |
| **CrewAI** | 69.2 | 99.7 | 94.6 | 97.0 | 60.2 | 57.1 |
| **OpenAI Agents SDK** | 36.5 | 99.7 | 99.4 | 100 | 71.2 | 63.1 |
| **Mastra** | 35.6 | 99.7 | 95.4 | 100 | 93.0 | 39.0 |
| **LangGraph** | 100 | 99.7 | 69.6 | 35.0 | 55.6 | 67.3 |

## 💡 Key Insights

- **Hottest framework**: BrowserUse with a Pulse Score of 89.9
- **Fastest growing**: Claude Agent SDK gained +792 stars this week
- **Most active development**: Mastra with 1571 commits in the last 4 weeks
- **Stale releases**: AutoGen, Swarm haven't released in a while

## 📦 Recent Releases

- **PydanticAI** [`v2.33.0`](https://github.com/pydantic/pydantic-ai/releases/tag/v2.33.0) — today
- **Composio** [`@composio/cli@0.3.4-beta.360`](https://github.com/ComposioHQ/composio/releases/tag/@composio/cli@0.3.4-beta.360) — today *(pre-release)*
- **Claude Agent SDK** [`v2.1.238`](https://github.com/anthropics/claude-code/releases/tag/v2.1.238) — today
- **Agno** [`v3.0.0a2`](https://github.com/agno-agi/agno/releases/tag/v3.0.0a2) — today *(pre-release)*
- **CrewAI** [`1.15.17`](https://github.com/crewAIInc/crewAI/releases/tag/1.15.17) — 1 day ago
- **LlamaIndex** [`v0.14.24`](https://github.com/run-llama/llama_index/releases/tag/v0.14.24) — 1 day ago
- **LangGraph** [`sdk==0.4.3`](https://github.com/langchain-ai/langgraph/releases/tag/sdk==0.4.3) — 1 day ago
- **Mastra** [`@mastra/core@1.60.0`](https://github.com/mastra-ai/mastra/releases/tag/@mastra/core@1.60.0) — 1 day ago
- **OpenAI Agents SDK** [`v0.22.0`](https://github.com/openai/openai-agents-python/releases/tag/v0.22.0) — 1 day ago
- **Semantic Kernel** [`dotnet-1.80.0`](https://github.com/microsoft/semantic-kernel/releases/tag/dotnet-1.80.0) — 2 days ago

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

*Powered by GitHub Actions • Data refreshed daily • Last run: 2026-08-21 06:54 UTC*