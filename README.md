# 🔬 AI Agent Framework Pulse Tracker

[![Daily Update](https://github.com/PurpleHaze2320/ai-agent-pulse/actions/workflows/track.yml/badge.svg)](https://github.com/PurpleHaze2320/ai-agent-pulse/actions/workflows/track.yml)
[![Frameworks Tracked](https://img.shields.io/badge/frameworks-19-blue)](https://github.com/PurpleHaze2320/ai-agent-pulse)
[![License: MIT](https://img.shields.io/badge/License-MIT-green.svg)](https://opensource.org/licenses/MIT)
[![GitHub stars](https://img.shields.io/github/stars/PurpleHaze2320/ai-agent-pulse?style=social)](https://github.com/PurpleHaze2320/ai-agent-pulse/stargazers)

> Automated daily tracking of the AI agent framework ecosystem's health, momentum, and trends.
> Last updated: **2026-07-01 09:59 UTC** | Tracking **19** frameworks

## How It Works

This bot runs daily via GitHub Actions and collects metrics from the GitHub API for the most important
AI agent frameworks. It computes a **Pulse Score** (0-100) based on six weighted signals: star velocity,
release freshness, issue health, commit activity, community size, and fork engagement. The result is
a living dashboard that shows which frameworks are gaining momentum and which are losing steam.

## 🏆 Pulse Leaderboard

| Rank | Framework | Pulse | Stars | ⭐ 7d | Commits (4w) | Last Release | Category |
|------|-----------|-------|-------|-------|--------------|--------------|----------|
| 1 | [CrewAI](https://github.com/crewAIInc/crewAI) | 🟢 **88.0** | 54.7k | 🚀 +405 | 123 | today | `multi-agent` |
| 2 | [Mastra](https://github.com/mastra-ai/mastra) | 🟢 **79.5** | 25.6k | 🚀 +241 | 866 | today | `typescript` |
| 3 | [LangGraph](https://github.com/langchain-ai/langgraph) | 🟢 **77.0** | 36.2k | 🚀 +587 | 44 | 1 day ago | `orchestration` |
| 4 | [Claude Agent SDK](https://github.com/anthropics/claude-code) | 🟢 **71.1** | 135.2k | 🚀 +1147 | 27 | today | `orchestration` |
| 5 | [BrowserUse](https://github.com/browser-use/browser-use) | 🟡 **68.8** | 101.9k | 🚀 +1479 | 0 | 18 days ago | `web-agent` |
| 6 | [Agno](https://github.com/agno-agi/agno) | 🟡 **68.6** | 40.9k | 🚀 +107 | 86 | 7 days ago | `multi-agent` |
| 7 | [Composio](https://github.com/ComposioHQ/composio) | 🟡 **67.5** | 29.0k | 🚀 +108 | 117 | 1 day ago | `tooling` |
| 8 | [OpenAI Agents SDK](https://github.com/openai/openai-agents-python) | 🟡 **63.9** | 27.5k | 🚀 +155 | 48 | 7 days ago | `orchestration` |
| 9 | [LlamaIndex](https://github.com/run-llama/llama_index) | 🟡 **62.9** | 50.6k | 🚀 +218 | 14 | 6 days ago | `data-agent` |
| 10 | [DSPy](https://github.com/stanfordnlp/dspy) | 🟡 **60.0** | 35.7k | 🚀 +361 | 12 | 1 mo ago | `optimization` |
| 11 | [Semantic Kernel](https://github.com/microsoft/semantic-kernel) | 🟡 **57.4** | 28.2k | 📈 +50 | 33 | 14 days ago | `enterprise` |
| 12 | [PydanticAI](https://github.com/pydantic/pydantic-ai) | 🟡 **55.2** | 18.1k | 🚀 +158 | 0 | today | `structured` |
| 13 | [Haystack](https://github.com/deepset-ai/haystack) | 🟡 **52.1** | 25.8k | 🚀 +139 | 0 | 13 days ago | `pipeline` |
| 14 | [Google ADK](https://github.com/google/adk-python) | 🟡 **51.3** | 20.4k | 🚀 +106 | 0 | 12 days ago | `orchestration` |
| 15 | [AG2](https://github.com/ag2ai/ag2) | 🟡 **49.6** | 4.7k | ↗️ +14 | 0 | 5 days ago | `multi-agent` |
| 16 | [Letta](https://github.com/letta-ai/letta) | 🟡 **44.4** | 23.6k | 🚀 +112 | 0 | 1 mo ago | `memory` |
| 17 | [Smolagents](https://github.com/huggingface/smolagents) | 🟡 **42.1** | 28.1k | 🚀 +130 | 0 | 1 mo ago | `lightweight` |
| 18 | [AutoGen](https://github.com/microsoft/autogen) | 🟠 **38.7** | 59.4k | 🚀 +193 | 0 | 9 mo ago | `multi-agent` |
| 19 | [Swarm](https://github.com/openai/swarm) | 🔴 **9.9** | 21.8k | 📈 +42 | 0 | — | `experimental` |

## 📂 By Category

- `data-agent`: **LlamaIndex** (62.9)
- `enterprise`: **Semantic Kernel** (57.4)
- `experimental`: **Swarm** (9.9)
- `lightweight`: **Smolagents** (42.1)
- `memory`: **Letta** (44.4)
- `multi-agent`: **CrewAI** (88.0), **Agno** (68.6), **AG2** (49.6), **AutoGen** (38.7)
- `optimization`: **DSPy** (60.0)
- `orchestration`: **LangGraph** (77.0), **Claude Agent SDK** (71.1), **OpenAI Agents SDK** (63.9), **Google ADK** (51.3)
- `pipeline`: **Haystack** (52.1)
- `structured`: **PydanticAI** (55.2)
- `tooling`: **Composio** (67.5)
- `typescript`: **Mastra** (79.5)
- `web-agent`: **BrowserUse** (68.8)

## 🔍 Top 5 — Score Breakdown

| Framework | Star Velocity | Release Freshness | Issue Health | Commit Activity | Community | Fork Ratio |
|-----------|:---:|:---:|:---:|:---:|:---:|:---:|
| **CrewAI** | 88.1 | 100.0 | 95.9 | 100 | 59.6 | 56.1 |
| **Mastra** | 49.1 | 100.0 | 95.5 | 100 | 92.4 | 36.4 |
| **LangGraph** | 100 | 99.7 | 73.6 | 44.0 | 55.0 | 66.9 |
| **Claude Agent SDK** | 100 | 100.0 | 87.9 | 27.0 | 10.4 | 64.5 |
| **BrowserUse** | 100 | 94.0 | 95.3 | 0.0 | 63.0 | 44.4 |

## 💡 Key Insights

- **Hottest framework**: CrewAI with a Pulse Score of 88.0
- **Fastest growing**: BrowserUse gained +1479 stars this week
- **Most active development**: Mastra with 866 commits in the last 4 weeks
- **Stale releases**: AutoGen, Swarm haven't released in a while

## 📦 Recent Releases

- **Mastra** [`@mastra/core@1.47.0`](https://github.com/mastra-ai/mastra/releases/tag/@mastra/core@1.47.0) — today
- **PydanticAI** [`v2.2.0`](https://github.com/pydantic/pydantic-ai/releases/tag/v2.2.0) — today
- **CrewAI** [`1.15.2a1`](https://github.com/crewAIInc/crewAI/releases/tag/1.15.2a1) — today *(pre-release)*
- **Claude Agent SDK** [`v2.1.197`](https://github.com/anthropics/claude-code/releases/tag/v2.1.197) — today
- **LangGraph** [`1.2.7`](https://github.com/langchain-ai/langgraph/releases/tag/1.2.7) — 1 day ago
- **Composio** [`@composio/cli@0.2.32-beta.280`](https://github.com/ComposioHQ/composio/releases/tag/@composio/cli@0.2.32-beta.280) — 1 day ago *(pre-release)*
- **AG2** [`v0.14.0`](https://github.com/ag2ai/ag2/releases/tag/v0.14.0) — 5 days ago
- **LlamaIndex** [`v0.14.23`](https://github.com/run-llama/llama_index/releases/tag/v0.14.23) — 6 days ago
- **OpenAI Agents SDK** [`v0.17.7`](https://github.com/openai/openai-agents-python/releases/tag/v0.17.7) — 7 days ago
- **Agno** [`v2.6.19`](https://github.com/agno-agi/agno/releases/tag/v2.6.19) — 7 days ago

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

*Powered by GitHub Actions • Data refreshed daily • Last run: 2026-07-01 09:59 UTC*