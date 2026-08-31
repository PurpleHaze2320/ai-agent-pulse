# 🔬 AI Agent Framework Pulse Tracker

[![Daily Update](https://github.com/PurpleHaze2320/ai-agent-pulse/actions/workflows/track.yml/badge.svg)](https://github.com/PurpleHaze2320/ai-agent-pulse/actions/workflows/track.yml)
[![Frameworks Tracked](https://img.shields.io/badge/frameworks-19-blue)](https://github.com/PurpleHaze2320/ai-agent-pulse)
[![License: MIT](https://img.shields.io/badge/License-MIT-green.svg)](https://opensource.org/licenses/MIT)
[![GitHub stars](https://img.shields.io/github/stars/PurpleHaze2320/ai-agent-pulse?style=social)](https://github.com/PurpleHaze2320/ai-agent-pulse/stargazers)

> Automated daily tracking of the AI agent framework ecosystem's health, momentum, and trends.
> Last updated: **2026-08-31 13:13 UTC** | Tracking **19** frameworks

## How It Works

This bot runs daily via GitHub Actions and collects metrics from the GitHub API for the most important
AI agent frameworks. It computes a **Pulse Score** (0-100) based on six weighted signals: star velocity,
release freshness, issue health, commit activity, community size, and fork engagement. The result is
a living dashboard that shows which frameworks are gaining momentum and which are losing steam.

## 🏆 Pulse Leaderboard

| Rank | Framework | Pulse | Stars | ⭐ 7d | Commits (4w) | Last Release | Category |
|------|-----------|-------|-------|-------|--------------|--------------|----------|
| 1 | [BrowserUse](https://github.com/browser-use/browser-use) | 🟢 **89.4** | 111.8k | 🚀 +1522 | 128 | 14 days ago | `web-agent` |
| 2 | [OpenAI Agents SDK](https://github.com/openai/openai-agents-python) | 🟢 **77.1** | 29.1k | 🚀 +180 | 201 | 11 days ago | `orchestration` |
| 3 | [CrewAI](https://github.com/crewAIInc/crewAI) | 🟢 **76.8** | 57.9k | 🚀 +337 | 68 | 3 days ago | `multi-agent` |
| 4 | [Mastra](https://github.com/mastra-ai/mastra) | 🟢 **76.6** | 27.6k | 🚀 +182 | 1214 | 3 days ago | `typescript` |
| 5 | [PydanticAI](https://github.com/pydantic/pydantic-ai) | 🟢 **74.4** | 19.6k | 🚀 +142 | 189 | 2 days ago | `structured` |
| 6 | [Claude Agent SDK](https://github.com/anthropics/claude-code) | 🟡 **69.2** | 143.5k | 🚀 +738 | 22 | 2 days ago | `orchestration` |
| 7 | [LangGraph](https://github.com/langchain-ai/langgraph) | 🟡 **68.8** | 40.8k | 🚀 +458 | 11 | 3 days ago | `orchestration` |
| 8 | [Composio](https://github.com/ComposioHQ/composio) | 🟡 **68.7** | 30.0k | 🚀 +126 | 206 | today | `tooling` |
| 9 | [Agno](https://github.com/agno-agi/agno) | 🟡 **64.3** | 42.0k | 🚀 +113 | 63 | today | `multi-agent` |
| 10 | [DSPy](https://github.com/stanfordnlp/dspy) | 🟡 **64.2** | 37.7k | 🚀 +132 | 60 | 9 days ago | `optimization` |
| 11 | [LlamaIndex](https://github.com/run-llama/llama_index) | 🟡 **61.7** | 51.9k | 🚀 +108 | 29 | 11 days ago | `data-agent` |
| 12 | [AG2](https://github.com/ag2ai/ag2) | 🟡 **58.7** | 4.9k | ↗️ +13 | 45 | 2 days ago | `multi-agent` |
| 13 | [Google ADK](https://github.com/google/adk-python) | 🟡 **53.7** | 21.3k | 📈 +91 | 0 | 3 days ago | `orchestration` |
| 14 | [Semantic Kernel](https://github.com/microsoft/semantic-kernel) | 🟡 **53.3** | 28.5k | 📈 +34 | 15 | 12 days ago | `enterprise` |
| 15 | [Haystack](https://github.com/deepset-ai/haystack) | 🟡 **51.2** | 26.4k | 📈 +74 | 0 | 6 days ago | `pipeline` |
| 16 | [Letta](https://github.com/letta-ai/letta) | 🟡 **41.3** | 24.5k | 🚀 +122 | 3 | 3 mo ago | `memory` |
| 17 | [Smolagents](https://github.com/huggingface/smolagents) | 🟠 **37.6** | 29.1k | 🚀 +115 | 2 | 3 mo ago | `lightweight` |
| 18 | [AutoGen](https://github.com/microsoft/autogen) | 🟠 **33.5** | 60.7k | 🚀 +117 | 0 | 11 mo ago | `multi-agent` |
| 19 | [Swarm](https://github.com/openai/swarm) | 🔴 **9.3** | 21.9k | ↗️ +13 | 0 | — | `experimental` |

## 📂 By Category

- `data-agent`: **LlamaIndex** (61.7)
- `enterprise`: **Semantic Kernel** (53.3)
- `experimental`: **Swarm** (9.3)
- `lightweight`: **Smolagents** (37.6)
- `memory`: **Letta** (41.3)
- `multi-agent`: **CrewAI** (76.8), **Agno** (64.3), **AG2** (58.7), **AutoGen** (33.5)
- `optimization`: **DSPy** (64.2)
- `orchestration`: **OpenAI Agents SDK** (77.1), **Claude Agent SDK** (69.2), **LangGraph** (68.8), **Google ADK** (53.7)
- `pipeline`: **Haystack** (51.2)
- `structured`: **PydanticAI** (74.4)
- `tooling`: **Composio** (68.7)
- `typescript`: **Mastra** (76.6)
- `web-agent`: **BrowserUse** (89.4)

## 🔍 Top 5 — Score Breakdown

| Framework | Star Velocity | Release Freshness | Issue Health | Commit Activity | Community | Fork Ratio |
|-----------|:---:|:---:|:---:|:---:|:---:|:---:|
| **BrowserUse** | 100 | 95.3 | 93.1 | 100 | 70.0 | 43.9 |
| **OpenAI Agents SDK** | 36.7 | 96.3 | 99.1 | 100 | 73.6 | 63.8 |
| **CrewAI** | 68.5 | 99.0 | 97.1 | 68.0 | 60.2 | 57.3 |
| **Mastra** | 37.4 | 99.0 | 94.9 | 100 | 93.0 | 39.4 |
| **PydanticAI** | 29.9 | 99.3 | 81.6 | 100 | 95.0 | 53.5 |

## 💡 Key Insights

- **Hottest framework**: BrowserUse with a Pulse Score of 89.4
- **Fastest growing**: BrowserUse gained +1522 stars this week
- **Most active development**: Mastra with 1214 commits in the last 4 weeks
- **Stale releases**: AutoGen, Swarm haven't released in a while

## 📦 Recent Releases

- **Composio** [`@composio/cli@0.4.1-beta.373`](https://github.com/ComposioHQ/composio/releases/tag/@composio/cli@0.4.1-beta.373) — today *(pre-release)*
- **Agno** [`v3.0.4`](https://github.com/agno-agi/agno/releases/tag/v3.0.4) — today
- **PydanticAI** [`v2.36.0`](https://github.com/pydantic/pydantic-ai/releases/tag/v2.36.0) — 2 days ago
- **AG2** [`v1.0.3`](https://github.com/ag2ai/ag2/releases/tag/v1.0.3) — 2 days ago
- **Claude Agent SDK** [`v2.1.251`](https://github.com/anthropics/claude-code/releases/tag/v2.1.251) — 2 days ago
- **Mastra** [`@mastra/core@1.63.0`](https://github.com/mastra-ai/mastra/releases/tag/@mastra/core@1.63.0) — 3 days ago
- **Google ADK** [`v1.39.1`](https://github.com/google/adk-python/releases/tag/v1.39.1) — 3 days ago
- **LangGraph** [`sdk==0.4.4`](https://github.com/langchain-ai/langgraph/releases/tag/sdk==0.4.4) — 3 days ago
- **CrewAI** [`1.15.18`](https://github.com/crewAIInc/crewAI/releases/tag/1.15.18) — 3 days ago
- **Haystack** [`v3.1.0`](https://github.com/deepset-ai/haystack/releases/tag/v3.1.0) — 6 days ago

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

*Powered by GitHub Actions • Data refreshed daily • Last run: 2026-08-31 13:13 UTC*