# 🔬 AI Agent Framework Pulse Tracker

[![Daily Update](https://github.com/PurpleHaze2320/ai-agent-pulse/actions/workflows/track.yml/badge.svg)](https://github.com/PurpleHaze2320/ai-agent-pulse/actions/workflows/track.yml)
[![Frameworks Tracked](https://img.shields.io/badge/frameworks-19-blue)](https://github.com/PurpleHaze2320/ai-agent-pulse)
[![License: MIT](https://img.shields.io/badge/License-MIT-green.svg)](https://opensource.org/licenses/MIT)
[![GitHub stars](https://img.shields.io/github/stars/PurpleHaze2320/ai-agent-pulse?style=social)](https://github.com/PurpleHaze2320/ai-agent-pulse/stargazers)

> Automated daily tracking of the AI agent framework ecosystem's health, momentum, and trends.
> Last updated: **2026-08-25 06:56 UTC** | Tracking **19** frameworks

## How It Works

This bot runs daily via GitHub Actions and collects metrics from the GitHub API for the most important
AI agent frameworks. It computes a **Pulse Score** (0-100) based on six weighted signals: star velocity,
release freshness, issue health, commit activity, community size, and fork engagement. The result is
a living dashboard that shows which frameworks are gaining momentum and which are losing steam.

## 🏆 Pulse Leaderboard

| Rank | Framework | Pulse | Stars | ⭐ 7d | Commits (4w) | Last Release | Category |
|------|-----------|-------|-------|-------|--------------|--------------|----------|
| 1 | [BrowserUse](https://github.com/browser-use/browser-use) | 🟢 **89.6** | 110.4k | 🚀 +861 | 111 | 8 days ago | `web-agent` |
| 2 | [CrewAI](https://github.com/crewAIInc/crewAI) | 🟢 **79.7** | 57.6k | 🚀 +345 | 83 | 5 days ago | `multi-agent` |
| 3 | [OpenAI Agents SDK](https://github.com/openai/openai-agents-python) | 🟢 **78.3** | 28.9k | 🚀 +208 | 325 | 5 days ago | `orchestration` |
| 4 | [Mastra](https://github.com/mastra-ai/mastra) | 🟢 **77.4** | 27.4k | 🚀 +186 | 1552 | today | `typescript` |
| 5 | [LangGraph](https://github.com/langchain-ai/langgraph) | 🟢 **73.7** | 40.4k | 🚀 +504 | 32 | 5 days ago | `orchestration` |
| 6 | [Claude Agent SDK](https://github.com/anthropics/claude-code) | 🟡 **69.5** | 142.9k | 🚀 +1111 | 23 | today | `orchestration` |
| 7 | [Composio](https://github.com/ComposioHQ/composio) | 🟡 **68.4** | 29.9k | 🚀 +122 | 260 | today | `tooling` |
| 8 | [DSPy](https://github.com/stanfordnlp/dspy) | 🟡 **66.1** | 37.6k | 🚀 +215 | 53 | 3 days ago | `optimization` |
| 9 | [LlamaIndex](https://github.com/run-llama/llama_index) | 🟡 **62.9** | 51.9k | 🚀 +141 | 26 | 5 days ago | `data-agent` |
| 10 | [Agno](https://github.com/agno-agi/agno) | 🟡 **60.7** | 41.9k | 🚀 +142 | 40 | today | `multi-agent` |
| 11 | [PydanticAI](https://github.com/pydantic/pydantic-ai) | 🟡 **54.2** | 19.5k | 🚀 +129 | 0 | today | `structured` |
| 12 | [Google ADK](https://github.com/google/adk-python) | 🟡 **53.8** | 21.3k | 🚀 +103 | 0 | 7 days ago | `orchestration` |
| 13 | [Semantic Kernel](https://github.com/microsoft/semantic-kernel) | 🟡 **52.6** | 28.5k | 📈 +33 | 10 | 6 days ago | `enterprise` |
| 14 | [Haystack](https://github.com/deepset-ai/haystack) | 🟡 **51.3** | 26.3k | 📈 +70 | 0 | today | `pipeline` |
| 15 | [AG2](https://github.com/ag2ai/ag2) | 🟡 **49.2** | 4.9k | ↗️ +13 | 0 | 10 days ago | `multi-agent` |
| 16 | [Letta](https://github.com/letta-ai/letta) | 🟡 **42.0** | 24.4k | 🚀 +131 | 3 | 3 mo ago | `memory` |
| 17 | [Smolagents](https://github.com/huggingface/smolagents) | 🟠 **38.5** | 29.0k | 🚀 +130 | 2 | 2 mo ago | `lightweight` |
| 18 | [AutoGen](https://github.com/microsoft/autogen) | 🟠 **34.4** | 60.6k | 🚀 +136 | 0 | 10 mo ago | `multi-agent` |
| 19 | [Swarm](https://github.com/openai/swarm) | 🔴 **9.3** | 21.9k | ↗️ +13 | 0 | — | `experimental` |

## 📂 By Category

- `data-agent`: **LlamaIndex** (62.9)
- `enterprise`: **Semantic Kernel** (52.6)
- `experimental`: **Swarm** (9.3)
- `lightweight`: **Smolagents** (38.5)
- `memory`: **Letta** (42.0)
- `multi-agent`: **CrewAI** (79.7), **Agno** (60.7), **AG2** (49.2), **AutoGen** (34.4)
- `optimization`: **DSPy** (66.1)
- `orchestration`: **OpenAI Agents SDK** (78.3), **LangGraph** (73.7), **Claude Agent SDK** (69.5), **Google ADK** (53.8)
- `pipeline`: **Haystack** (51.3)
- `structured`: **PydanticAI** (54.2)
- `tooling`: **Composio** (68.4)
- `typescript`: **Mastra** (77.4)
- `web-agent`: **BrowserUse** (89.6)

## 🔍 Top 5 — Score Breakdown

| Framework | Star Velocity | Release Freshness | Issue Health | Commit Activity | Community | Fork Ratio |
|-----------|:---:|:---:|:---:|:---:|:---:|:---:|
| **BrowserUse** | 100 | 97.3 | 93.1 | 100 | 67.2 | 44.0 |
| **CrewAI** | 69.9 | 98.3 | 94.6 | 83.0 | 60.2 | 57.2 |
| **OpenAI Agents SDK** | 40.7 | 98.3 | 99.4 | 100 | 72.0 | 63.4 |
| **Mastra** | 39.2 | 100.0 | 96.2 | 100 | 93.0 | 39.2 |
| **LangGraph** | 100 | 98.3 | 68.8 | 32.0 | 55.6 | 67.4 |

## 💡 Key Insights

- **Hottest framework**: BrowserUse with a Pulse Score of 89.6
- **Fastest growing**: Claude Agent SDK gained +1111 stars this week
- **Most active development**: Mastra with 1552 commits in the last 4 weeks
- **Stale releases**: AutoGen, Swarm haven't released in a while

## 📦 Recent Releases

- **Claude Agent SDK** [`v2.1.245`](https://github.com/anthropics/claude-code/releases/tag/v2.1.245) — today
- **PydanticAI** [`v2.34.0`](https://github.com/pydantic/pydantic-ai/releases/tag/v2.34.0) — today
- **Composio** [`@composio/cli@0.4.1-beta.368`](https://github.com/ComposioHQ/composio/releases/tag/@composio/cli@0.4.1-beta.368) — today *(pre-release)*
- **Haystack** [`v3.1.0`](https://github.com/deepset-ai/haystack/releases/tag/v3.1.0) — today
- **Agno** [`v3.0.0`](https://github.com/agno-agi/agno/releases/tag/v3.0.0) — today
- **Mastra** [`@mastra/core@1.61.0`](https://github.com/mastra-ai/mastra/releases/tag/@mastra/core@1.61.0) — today
- **DSPy** [`3.3.1`](https://github.com/stanfordnlp/dspy/releases/tag/3.3.1) — 3 days ago
- **CrewAI** [`1.15.17`](https://github.com/crewAIInc/crewAI/releases/tag/1.15.17) — 5 days ago
- **LlamaIndex** [`v0.14.24`](https://github.com/run-llama/llama_index/releases/tag/v0.14.24) — 5 days ago
- **LangGraph** [`sdk==0.4.3`](https://github.com/langchain-ai/langgraph/releases/tag/sdk==0.4.3) — 5 days ago

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

*Powered by GitHub Actions • Data refreshed daily • Last run: 2026-08-25 06:56 UTC*