# 🔬 AI Agent Framework Pulse Tracker

[![Daily Update](https://github.com/PurpleHaze2320/ai-agent-pulse/actions/workflows/track.yml/badge.svg)](https://github.com/PurpleHaze2320/ai-agent-pulse/actions/workflows/track.yml)
[![Frameworks Tracked](https://img.shields.io/badge/frameworks-19-blue)](https://github.com/PurpleHaze2320/ai-agent-pulse)
[![License: MIT](https://img.shields.io/badge/License-MIT-green.svg)](https://opensource.org/licenses/MIT)
[![GitHub stars](https://img.shields.io/github/stars/PurpleHaze2320/ai-agent-pulse?style=social)](https://github.com/PurpleHaze2320/ai-agent-pulse/stargazers)

> Automated daily tracking of the AI agent framework ecosystem's health, momentum, and trends.
> Last updated: **2026-07-05 09:13 UTC** | Tracking **19** frameworks

## How It Works

This bot runs daily via GitHub Actions and collects metrics from the GitHub API for the most important
AI agent frameworks. It computes a **Pulse Score** (0-100) based on six weighted signals: star velocity,
release freshness, issue health, commit activity, community size, and fork engagement. The result is
a living dashboard that shows which frameworks are gaining momentum and which are losing steam.

## 🏆 Pulse Leaderboard

| Rank | Framework | Pulse | Stars | ⭐ 7d | Commits (4w) | Last Release | Category |
|------|-----------|-------|-------|-------|--------------|--------------|----------|
| 1 | [CrewAI](https://github.com/crewAIInc/crewAI) | 🟢 **87.7** | 54.9k | 🚀 +447 | 93 | 3 days ago | `multi-agent` |
| 2 | [Mastra](https://github.com/mastra-ai/mastra) | 🟢 **81.5** | 25.8k | 🚀 +302 | 843 | 3 days ago | `typescript` |
| 3 | [LangGraph](https://github.com/langchain-ai/langgraph) | 🟢 **77.1** | 36.5k | 🚀 +580 | 46 | 5 days ago | `orchestration` |
| 4 | [Google ADK](https://github.com/google/adk-python) | 🟢 **72.6** | 20.5k | 🚀 +144 | 263 | 16 days ago | `orchestration` |
| 5 | [Agno](https://github.com/agno-agi/agno) | 🟢 **71.1** | 41.0k | 🚀 +126 | 93 | today | `multi-agent` |
| 6 | [Claude Agent SDK](https://github.com/anthropics/claude-code) | 🟢 **70.3** | 136.1k | 🚀 +1375 | 24 | 1 day ago | `orchestration` |
| 7 | [BrowserUse](https://github.com/browser-use/browser-use) | 🟡 **69.8** | 102.8k | 🚀 +1757 | 0 | 3 days ago | `web-agent` |
| 8 | [Composio](https://github.com/ComposioHQ/composio) | 🟡 **67.0** | 29.1k | 📈 +98 | 119 | 1 day ago | `tooling` |
| 9 | [OpenAI Agents SDK](https://github.com/openai/openai-agents-python) | 🟡 **65.7** | 27.7k | 🚀 +172 | 55 | 11 days ago | `orchestration` |
| 10 | [LlamaIndex](https://github.com/run-llama/llama_index) | 🟡 **59.0** | 50.6k | 🚀 +193 | 0 | 10 days ago | `data-agent` |
| 11 | [PydanticAI](https://github.com/pydantic/pydantic-ai) | 🟡 **56.0** | 18.2k | 🚀 +178 | 0 | 1 day ago | `structured` |
| 12 | [DSPy](https://github.com/stanfordnlp/dspy) | 🟡 **56.0** | 35.8k | 🚀 +303 | 3 | 1 mo ago | `optimization` |
| 13 | [Semantic Kernel](https://github.com/microsoft/semantic-kernel) | 🟡 **50.4** | 28.3k | 📈 +48 | 0 | 18 days ago | `enterprise` |
| 14 | [AG2](https://github.com/ag2ai/ag2) | 🟡 **50.1** | 4.7k | ↗️ +19 | 0 | 1 day ago | `multi-agent` |
| 15 | [Haystack](https://github.com/deepset-ai/haystack) | 🟡 **49.1** | 25.8k | 📈 +61 | 0 | 17 days ago | `pipeline` |
| 16 | [Letta](https://github.com/letta-ai/letta) | 🟡 **43.8** | 23.7k | 🚀 +103 | 0 | 1 mo ago | `memory` |
| 17 | [Smolagents](https://github.com/huggingface/smolagents) | 🟡 **41.8** | 28.2k | 🚀 +131 | 0 | 1 mo ago | `lightweight` |
| 18 | [AutoGen](https://github.com/microsoft/autogen) | 🟠 **38.4** | 59.5k | 🚀 +193 | 0 | 9 mo ago | `multi-agent` |
| 19 | [Swarm](https://github.com/openai/swarm) | 🔴 **9.2** | 21.8k | 📈 +23 | 0 | — | `experimental` |

## 📂 By Category

- `data-agent`: **LlamaIndex** (59.0)
- `enterprise`: **Semantic Kernel** (50.4)
- `experimental`: **Swarm** (9.2)
- `lightweight`: **Smolagents** (41.8)
- `memory`: **Letta** (43.8)
- `multi-agent`: **CrewAI** (87.7), **Agno** (71.1), **AG2** (50.1), **AutoGen** (38.4)
- `optimization`: **DSPy** (56.0)
- `orchestration`: **LangGraph** (77.1), **Google ADK** (72.6), **Claude Agent SDK** (70.3), **OpenAI Agents SDK** (65.7)
- `pipeline`: **Haystack** (49.1)
- `structured`: **PydanticAI** (56.0)
- `tooling`: **Composio** (67.0)
- `typescript`: **Mastra** (81.5)
- `web-agent`: **BrowserUse** (69.8)

## 🔍 Top 5 — Score Breakdown

| Framework | Star Velocity | Release Freshness | Issue Health | Commit Activity | Community | Fork Ratio |
|-----------|:---:|:---:|:---:|:---:|:---:|:---:|
| **CrewAI** | 93.4 | 99.0 | 95.6 | 93.0 | 59.6 | 56.1 |
| **Mastra** | 57.7 | 99.0 | 95.5 | 100 | 92.6 | 36.5 |
| **LangGraph** | 100 | 98.3 | 73.5 | 46.0 | 55.0 | 67.0 |
| **Google ADK** | 27.2 | 94.7 | 85.0 | 100 | 70.4 | 71.3 |
| **Agno** | 24.6 | 100.0 | 80.3 | 93.0 | 88.8 | 54.6 |

## 💡 Key Insights

- **Hottest framework**: CrewAI with a Pulse Score of 87.7
- **Fastest growing**: BrowserUse gained +1757 stars this week
- **Most active development**: Mastra with 843 commits in the last 4 weeks
- **Stale releases**: AutoGen, Swarm haven't released in a while

## 📦 Recent Releases

- **Agno** [`v2.7.0a1-1`](https://github.com/agno-agi/agno/releases/tag/v2.7.0a1-1) — today *(pre-release)*
- **PydanticAI** [`v2.5.0`](https://github.com/pydantic/pydantic-ai/releases/tag/v2.5.0) — 1 day ago
- **Claude Agent SDK** [`v2.1.201`](https://github.com/anthropics/claude-code/releases/tag/v2.1.201) — 1 day ago
- **AG2** [`v1.0.0b0`](https://github.com/ag2ai/ag2/releases/tag/v1.0.0b0) — 1 day ago
- **Composio** [`@composio/cli@0.2.32-beta.281`](https://github.com/ComposioHQ/composio/releases/tag/@composio/cli@0.2.32-beta.281) — 1 day ago *(pre-release)*
- **CrewAI** [`1.15.2a2`](https://github.com/crewAIInc/crewAI/releases/tag/1.15.2a2) — 3 days ago *(pre-release)*
- **Mastra** [`@mastra/core@1.48.0`](https://github.com/mastra-ai/mastra/releases/tag/@mastra/core@1.48.0) — 3 days ago
- **BrowserUse** [`0.13.3`](https://github.com/browser-use/browser-use/releases/tag/0.13.3) — 3 days ago
- **LangGraph** [`1.2.7`](https://github.com/langchain-ai/langgraph/releases/tag/1.2.7) — 5 days ago
- **LlamaIndex** [`v0.14.23`](https://github.com/run-llama/llama_index/releases/tag/v0.14.23) — 10 days ago

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

*Powered by GitHub Actions • Data refreshed daily • Last run: 2026-07-05 09:13 UTC*