# 🔬 AI Agent Framework Pulse Tracker

[![Daily Update](https://github.com/PurpleHaze2320/ai-agent-pulse/actions/workflows/track.yml/badge.svg)](https://github.com/PurpleHaze2320/ai-agent-pulse/actions/workflows/track.yml)
[![Frameworks Tracked](https://img.shields.io/badge/frameworks-19-blue)](https://github.com/PurpleHaze2320/ai-agent-pulse)
[![License: MIT](https://img.shields.io/badge/License-MIT-green.svg)](https://opensource.org/licenses/MIT)
[![GitHub stars](https://img.shields.io/github/stars/PurpleHaze2320/ai-agent-pulse?style=social)](https://github.com/PurpleHaze2320/ai-agent-pulse/stargazers)

> Automated daily tracking of the AI agent framework ecosystem's health, momentum, and trends.
> Last updated: **2026-08-24 07:07 UTC** | Tracking **19** frameworks

## How It Works

This bot runs daily via GitHub Actions and collects metrics from the GitHub API for the most important
AI agent frameworks. It computes a **Pulse Score** (0-100) based on six weighted signals: star velocity,
release freshness, issue health, commit activity, community size, and fork engagement. The result is
a living dashboard that shows which frameworks are gaining momentum and which are losing steam.

## 🏆 Pulse Leaderboard

| Rank | Framework | Pulse | Stars | ⭐ 7d | Commits (4w) | Last Release | Category |
|------|-----------|-------|-------|-------|--------------|--------------|----------|
| 1 | [BrowserUse](https://github.com/browser-use/browser-use) | 🟢 **89.6** | 110.3k | 🚀 +822 | 105 | 7 days ago | `web-agent` |
| 2 | [CrewAI](https://github.com/crewAIInc/crewAI) | 🟢 **78.2** | 57.5k | 🚀 +347 | 75 | 4 days ago | `multi-agent` |
| 3 | [Mastra](https://github.com/mastra-ai/mastra) | 🟢 **76.7** | 27.4k | 🚀 +175 | 1428 | 4 days ago | `typescript` |
| 4 | [LangGraph](https://github.com/langchain-ai/langgraph) | 🟢 **73.6** | 40.3k | 🚀 +489 | 31 | 4 days ago | `orchestration` |
| 5 | [Composio](https://github.com/ComposioHQ/composio) | 🟡 **68.5** | 29.9k | 🚀 +124 | 249 | today | `tooling` |
| 6 | [Claude Agent SDK](https://github.com/anthropics/claude-code) | 🟡 **64.9** | 142.8k | 🚀 +1099 | 0 | 1 day ago | `orchestration` |
| 7 | [LlamaIndex](https://github.com/run-llama/llama_index) | 🟡 **62.9** | 51.8k | 🚀 +138 | 26 | 4 days ago | `data-agent` |
| 8 | [Agno](https://github.com/agno-agi/agno) | 🟡 **59.5** | 41.9k | 🚀 +133 | 36 | today | `multi-agent` |
| 9 | [OpenAI Agents SDK](https://github.com/openai/openai-agents-python) | 🟡 **58.4** | 28.9k | 🚀 +212 | 0 | 4 days ago | `orchestration` |
| 10 | [DSPy](https://github.com/stanfordnlp/dspy) | 🟡 **55.9** | 37.5k | 🚀 +225 | 0 | 2 days ago | `optimization` |
| 11 | [PydanticAI](https://github.com/pydantic/pydantic-ai) | 🟡 **53.8** | 19.5k | 🚀 +123 | 0 | 3 days ago | `structured` |
| 12 | [Google ADK](https://github.com/google/adk-python) | 🟡 **53.6** | 21.2k | 📈 +97 | 0 | 6 days ago | `orchestration` |
| 13 | [Semantic Kernel](https://github.com/microsoft/semantic-kernel) | 🟡 **52.4** | 28.5k | 📈 +26 | 10 | 5 days ago | `enterprise` |
| 14 | [Haystack](https://github.com/deepset-ai/haystack) | 🟡 **51.1** | 26.3k | 📈 +68 | 0 | 2 days ago | `pipeline` |
| 15 | [AG2](https://github.com/ag2ai/ag2) | 🟡 **49.4** | 4.9k | ↗️ +17 | 0 | 9 days ago | `multi-agent` |
| 16 | [Letta](https://github.com/letta-ai/letta) | 🟡 **41.1** | 24.4k | 🚀 +107 | 3 | 3 mo ago | `memory` |
| 17 | [Smolagents](https://github.com/huggingface/smolagents) | 🟠 **38.1** | 29.0k | 🚀 +128 | 0 | 2 mo ago | `lightweight` |
| 18 | [AutoGen](https://github.com/microsoft/autogen) | 🟠 **34.6** | 60.6k | 🚀 +142 | 0 | 10 mo ago | `multi-agent` |
| 19 | [Swarm](https://github.com/openai/swarm) | 🔴 **9.3** | 21.9k | ↗️ +14 | 0 | — | `experimental` |

## 📂 By Category

- `data-agent`: **LlamaIndex** (62.9)
- `enterprise`: **Semantic Kernel** (52.4)
- `experimental`: **Swarm** (9.3)
- `lightweight`: **Smolagents** (38.1)
- `memory`: **Letta** (41.1)
- `multi-agent`: **CrewAI** (78.2), **Agno** (59.5), **AG2** (49.4), **AutoGen** (34.6)
- `optimization`: **DSPy** (55.9)
- `orchestration`: **LangGraph** (73.6), **Claude Agent SDK** (64.9), **OpenAI Agents SDK** (58.4), **Google ADK** (53.6)
- `pipeline`: **Haystack** (51.1)
- `structured`: **PydanticAI** (53.8)
- `tooling`: **Composio** (68.5)
- `typescript`: **Mastra** (76.7)
- `web-agent`: **BrowserUse** (89.6)

## 🔍 Top 5 — Score Breakdown

| Framework | Star Velocity | Release Freshness | Issue Health | Commit Activity | Community | Fork Ratio |
|-----------|:---:|:---:|:---:|:---:|:---:|:---:|
| **BrowserUse** | 100 | 97.7 | 93.2 | 100 | 67.0 | 44.0 |
| **CrewAI** | 70.1 | 98.7 | 94.7 | 75.0 | 60.2 | 57.2 |
| **Mastra** | 37.4 | 98.7 | 95.9 | 100 | 93.0 | 39.1 |
| **LangGraph** | 100 | 98.7 | 69.1 | 31.0 | 55.6 | 67.4 |
| **Composio** | 24.7 | 100.0 | 95.2 | 100 | 17.2 | 63.4 |

## 💡 Key Insights

- **Hottest framework**: BrowserUse with a Pulse Score of 89.6
- **Fastest growing**: Claude Agent SDK gained +1099 stars this week
- **Most active development**: Mastra with 1428 commits in the last 4 weeks
- **Stale releases**: AutoGen, Swarm haven't released in a while

## 📦 Recent Releases

- **Agno** [`v3.0.0a4`](https://github.com/agno-agi/agno/releases/tag/v3.0.0a4) — today *(pre-release)*
- **Composio** [`@composio/cli@0.4.0`](https://github.com/ComposioHQ/composio/releases/tag/@composio/cli@0.4.0) — today
- **Claude Agent SDK** [`v2.1.241`](https://github.com/anthropics/claude-code/releases/tag/v2.1.241) — 1 day ago
- **DSPy** [`3.3.1`](https://github.com/stanfordnlp/dspy/releases/tag/3.3.1) — 2 days ago
- **Haystack** [`v3.1.0-rc3`](https://github.com/deepset-ai/haystack/releases/tag/v3.1.0-rc3) — 2 days ago *(pre-release)*
- **PydanticAI** [`v2.33.0`](https://github.com/pydantic/pydantic-ai/releases/tag/v2.33.0) — 3 days ago
- **CrewAI** [`1.15.17`](https://github.com/crewAIInc/crewAI/releases/tag/1.15.17) — 4 days ago
- **LlamaIndex** [`v0.14.24`](https://github.com/run-llama/llama_index/releases/tag/v0.14.24) — 4 days ago
- **LangGraph** [`sdk==0.4.3`](https://github.com/langchain-ai/langgraph/releases/tag/sdk==0.4.3) — 4 days ago
- **Mastra** [`@mastra/core@1.60.0`](https://github.com/mastra-ai/mastra/releases/tag/@mastra/core@1.60.0) — 4 days ago

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

*Powered by GitHub Actions • Data refreshed daily • Last run: 2026-08-24 07:07 UTC*