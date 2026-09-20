# 🔬 AI Agent Framework Pulse Tracker

[![Daily Update](https://github.com/PurpleHaze2320/ai-agent-pulse/actions/workflows/track.yml/badge.svg)](https://github.com/PurpleHaze2320/ai-agent-pulse/actions/workflows/track.yml)
[![Frameworks Tracked](https://img.shields.io/badge/frameworks-19-blue)](https://github.com/PurpleHaze2320/ai-agent-pulse)
[![License: MIT](https://img.shields.io/badge/License-MIT-green.svg)](https://opensource.org/licenses/MIT)
[![GitHub stars](https://img.shields.io/github/stars/PurpleHaze2320/ai-agent-pulse?style=social)](https://github.com/PurpleHaze2320/ai-agent-pulse/stargazers)

> Automated daily tracking of the AI agent framework ecosystem's health, momentum, and trends.
> Last updated: **2026-09-20 11:00 UTC** | Tracking **19** frameworks

## How It Works

This bot runs daily via GitHub Actions and collects metrics from the GitHub API for the most important
AI agent frameworks. It computes a **Pulse Score** (0-100) based on six weighted signals: star velocity,
release freshness, issue health, commit activity, community size, and fork engagement. The result is
a living dashboard that shows which frameworks are gaining momentum and which are losing steam.

## 🏆 Pulse Leaderboard

| Rank | Framework | Pulse | Stars | ⭐ 7d | Commits (4w) | Last Release | Category |
|------|-----------|-------|-------|-------|--------------|--------------|----------|
| 1 | [BrowserUse](https://github.com/browser-use/browser-use) | 🟢 **89.3** | 115.4k | 🚀 +1019 | 131 | 16 days ago | `web-agent` |
| 2 | [Claude Agent SDK](https://github.com/anthropics/claude-code) | 🟢 **85.7** | 146.9k | 🚀 +1988 | 109 | 1 day ago | `orchestration` |
| 3 | [CrewAI](https://github.com/crewAIInc/crewAI) | 🟢 **84.3** | 58.8k | 🚀 +373 | 99 | 3 days ago | `multi-agent` |
| 4 | [Mastra](https://github.com/mastra-ai/mastra) | 🟢 **77.9** | 28.2k | 🚀 +208 | 1477 | 4 days ago | `typescript` |
| 5 | [OpenAI Agents SDK](https://github.com/openai/openai-agents-python) | 🟢 **77.3** | 29.6k | 🚀 +172 | 98 | 2 days ago | `orchestration` |
| 6 | [PydanticAI](https://github.com/pydantic/pydantic-ai) | 🟢 **75.3** | 20.1k | 🚀 +171 | 212 | 1 day ago | `structured` |
| 7 | [Google ADK](https://github.com/google/adk-python) | 🟢 **73.0** | 21.6k | 📈 +60 | 293 | 1 day ago | `orchestration` |
| 8 | [Haystack](https://github.com/deepset-ai/haystack) | 🟢 **70.7** | 26.6k | 📈 +68 | 160 | 17 days ago | `pipeline` |
| 9 | [Agno](https://github.com/agno-agi/agno) | 🟢 **70.1** | 42.3k | 🚀 +113 | 95 | 3 days ago | `multi-agent` |
| 10 | [LangGraph](https://github.com/langchain-ai/langgraph) | 🟡 **69.8** | 42.0k | 🚀 +447 | 33 | 23 days ago | `orchestration` |
| 11 | [Composio](https://github.com/ComposioHQ/composio) | 🟡 **67.7** | 30.3k | 🚀 +103 | 214 | 2 days ago | `tooling` |
| 12 | [DSPy](https://github.com/stanfordnlp/dspy) | 🟡 **58.9** | 38.2k | 🚀 +159 | 38 | 8 days ago | `optimization` |
| 13 | [LlamaIndex](https://github.com/run-llama/llama_index) | 🟡 **58.5** | 52.2k | 📈 +99 | 25 | 1 mo ago | `data-agent` |
| 14 | [AG2](https://github.com/ag2ai/ag2) | 🟡 **56.8** | 4.9k | ↗️ +19 | 36 | 8 days ago | `multi-agent` |
| 15 | [Semantic Kernel](https://github.com/microsoft/semantic-kernel) | 🟡 **52.1** | 28.6k | 📈 +27 | 12 | 16 days ago | `enterprise` |
| 16 | [Letta](https://github.com/letta-ai/letta) | 🟠 **38.8** | 24.8k | 📈 +89 | 2 | 4 mo ago | `memory` |
| 17 | [Smolagents](https://github.com/huggingface/smolagents) | 🟠 **35.6** | 29.4k | 🚀 +110 | 0 | 3 mo ago | `lightweight` |
| 18 | [AutoGen](https://github.com/microsoft/autogen) | 🟠 **33.0** | 61.1k | 🚀 +111 | 0 | 11 mo ago | `multi-agent` |
| 19 | [Swarm](https://github.com/openai/swarm) | 🔴 **9.5** | 22.0k | 📈 +21 | 0 | — | `experimental` |

## 📂 By Category

- `data-agent`: **LlamaIndex** (58.5)
- `enterprise`: **Semantic Kernel** (52.1)
- `experimental`: **Swarm** (9.5)
- `lightweight`: **Smolagents** (35.6)
- `memory`: **Letta** (38.8)
- `multi-agent`: **CrewAI** (84.3), **Agno** (70.1), **AG2** (56.8), **AutoGen** (33.0)
- `optimization`: **DSPy** (58.9)
- `orchestration`: **Claude Agent SDK** (85.7), **OpenAI Agents SDK** (77.3), **Google ADK** (73.0), **LangGraph** (69.8)
- `pipeline`: **Haystack** (70.7)
- `structured`: **PydanticAI** (75.3)
- `tooling`: **Composio** (67.7)
- `typescript`: **Mastra** (77.9)
- `web-agent`: **BrowserUse** (89.3)

## 🔍 Top 5 — Score Breakdown

| Framework | Star Velocity | Release Freshness | Issue Health | Commit Activity | Community | Fork Ratio |
|-----------|:---:|:---:|:---:|:---:|:---:|:---:|
| **BrowserUse** | 100 | 94.7 | 91.6 | 100 | 72.2 | 44.0 |
| **Claude Agent SDK** | 100 | 99.7 | 87.6 | 100 | 10.8 | 65.3 |
| **CrewAI** | 73.3 | 99.0 | 92.8 | 99.0 | 67.0 | 57.9 |
| **Mastra** | 42.0 | 98.7 | 95.5 | 100 | 93.2 | 40.1 |
| **OpenAI Agents SDK** | 35.5 | 99.3 | 99.0 | 98.0 | 76.4 | 64.6 |

## 💡 Key Insights

- **Hottest framework**: BrowserUse with a Pulse Score of 89.3
- **Fastest growing**: Claude Agent SDK gained +1988 stars this week
- **Most active development**: Mastra with 1477 commits in the last 4 weeks
- **Stale releases**: AutoGen, Swarm haven't released in a while

## 📦 Recent Releases

- **PydanticAI** [`v2.46.0`](https://github.com/pydantic/pydantic-ai/releases/tag/v2.46.0) — 1 day ago
- **Claude Agent SDK** [`v2.1.278`](https://github.com/anthropics/claude-code/releases/tag/v2.1.278) — 1 day ago
- **Google ADK** [`v2.9.2`](https://github.com/google/adk-python/releases/tag/v2.9.2) — 1 day ago
- **OpenAI Agents SDK** [`v0.22.3`](https://github.com/openai/openai-agents-python/releases/tag/v0.22.3) — 2 days ago
- **Composio** [`@composio/cli@0.4.2-beta.398`](https://github.com/ComposioHQ/composio/releases/tag/@composio/cli@0.4.2-beta.398) — 2 days ago *(pre-release)*
- **CrewAI** [`1.15.22`](https://github.com/crewAIInc/crewAI/releases/tag/1.15.22) — 3 days ago
- **Agno** [`v3.0.10`](https://github.com/agno-agi/agno/releases/tag/v3.0.10) — 3 days ago
- **Mastra** [`@mastra/core@1.67.0`](https://github.com/mastra-ai/mastra/releases/tag/@mastra/core@1.67.0) — 4 days ago
- **DSPy** [`3.4.0b1`](https://github.com/stanfordnlp/dspy/releases/tag/3.4.0b1) — 8 days ago *(pre-release)*
- **AG2** [`v1.0.5`](https://github.com/ag2ai/ag2/releases/tag/v1.0.5) — 8 days ago

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

*Powered by GitHub Actions • Data refreshed daily • Last run: 2026-09-20 11:00 UTC*