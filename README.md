# 🔬 AI Agent Framework Pulse Tracker

[![Daily Update](https://github.com/PurpleHaze2320/ai-agent-pulse/actions/workflows/track.yml/badge.svg)](https://github.com/PurpleHaze2320/ai-agent-pulse/actions/workflows/track.yml)
[![Frameworks Tracked](https://img.shields.io/badge/frameworks-19-blue)](https://github.com/PurpleHaze2320/ai-agent-pulse)
[![License: MIT](https://img.shields.io/badge/License-MIT-green.svg)](https://opensource.org/licenses/MIT)
[![GitHub stars](https://img.shields.io/github/stars/PurpleHaze2320/ai-agent-pulse?style=social)](https://github.com/PurpleHaze2320/ai-agent-pulse/stargazers)

> Automated daily tracking of the AI agent framework ecosystem's health, momentum, and trends.
> Last updated: **2026-09-21 12:27 UTC** | Tracking **19** frameworks

## How It Works

This bot runs daily via GitHub Actions and collects metrics from the GitHub API for the most important
AI agent frameworks. It computes a **Pulse Score** (0-100) based on six weighted signals: star velocity,
release freshness, issue health, commit activity, community size, and fork engagement. The result is
a living dashboard that shows which frameworks are gaining momentum and which are losing steam.

## 🏆 Pulse Leaderboard

| Rank | Framework | Pulse | Stars | ⭐ 7d | Commits (4w) | Last Release | Category |
|------|-----------|-------|-------|-------|--------------|--------------|----------|
| 1 | [BrowserUse](https://github.com/browser-use/browser-use) | 🟢 **89.2** | 115.7k | 🚀 +1123 | 131 | 17 days ago | `web-agent` |
| 2 | [Claude Agent SDK](https://github.com/anthropics/claude-code) | 🟢 **85.6** | 147.4k | 🚀 +2414 | 110 | 2 days ago | `orchestration` |
| 3 | [CrewAI](https://github.com/crewAIInc/crewAI) | 🟢 **83.2** | 58.9k | 🚀 +338 | 101 | 4 days ago | `multi-agent` |
| 4 | [OpenAI Agents SDK](https://github.com/openai/openai-agents-python) | 🟢 **78.1** | 29.6k | 🚀 +186 | 130 | 3 days ago | `orchestration` |
| 5 | [Mastra](https://github.com/mastra-ai/mastra) | 🟢 **77.9** | 28.2k | 🚀 +208 | 1514 | 5 days ago | `typescript` |
| 6 | [PydanticAI](https://github.com/pydantic/pydantic-ai) | 🟢 **74.9** | 20.1k | 🚀 +161 | 212 | 2 days ago | `structured` |
| 7 | [Google ADK](https://github.com/google/adk-python) | 🟢 **72.8** | 21.6k | 📈 +56 | 298 | 2 days ago | `orchestration` |
| 8 | [Haystack](https://github.com/deepset-ai/haystack) | 🟢 **70.4** | 26.6k | 📈 +61 | 166 | 18 days ago | `pipeline` |
| 9 | [LangGraph](https://github.com/langchain-ai/langgraph) | 🟢 **70.2** | 42.1k | 🚀 +454 | 34 | 24 days ago | `orchestration` |
| 10 | [Composio](https://github.com/ComposioHQ/composio) | 🟡 **68.0** | 30.3k | 🚀 +105 | 219 | today | `tooling` |
| 11 | [DSPy](https://github.com/stanfordnlp/dspy) | 🟡 **59.2** | 38.2k | 🚀 +169 | 38 | 9 days ago | `optimization` |
| 12 | [LlamaIndex](https://github.com/run-llama/llama_index) | 🟡 **58.6** | 52.3k | 🚀 +103 | 25 | 1 mo ago | `data-agent` |
| 13 | [AG2](https://github.com/ag2ai/ag2) | 🟡 **58.2** | 4.9k | ↗️ +20 | 43 | 9 days ago | `multi-agent` |
| 14 | [Semantic Kernel](https://github.com/microsoft/semantic-kernel) | 🟡 **52.1** | 28.6k | 📈 +28 | 12 | 17 days ago | `enterprise` |
| 15 | [Agno](https://github.com/agno-agi/agno) | 🟡 **51.1** | 42.3k | 🚀 +114 | 0 | 4 days ago | `multi-agent` |
| 16 | [Letta](https://github.com/letta-ai/letta) | 🟠 **38.8** | 24.8k | 📈 +90 | 2 | 4 mo ago | `memory` |
| 17 | [Smolagents](https://github.com/huggingface/smolagents) | 🟠 **35.5** | 29.4k | 🚀 +107 | 0 | 3 mo ago | `lightweight` |
| 18 | [AutoGen](https://github.com/microsoft/autogen) | 🟠 **33.2** | 61.1k | 🚀 +114 | 0 | 11 mo ago | `multi-agent` |
| 19 | [Swarm](https://github.com/openai/swarm) | 🔴 **9.7** | 22.0k | 📈 +26 | 0 | — | `experimental` |

## 📂 By Category

- `data-agent`: **LlamaIndex** (58.6)
- `enterprise`: **Semantic Kernel** (52.1)
- `experimental`: **Swarm** (9.7)
- `lightweight`: **Smolagents** (35.5)
- `memory`: **Letta** (38.8)
- `multi-agent`: **CrewAI** (83.2), **AG2** (58.2), **Agno** (51.1), **AutoGen** (33.2)
- `optimization`: **DSPy** (59.2)
- `orchestration`: **Claude Agent SDK** (85.6), **OpenAI Agents SDK** (78.1), **Google ADK** (72.8), **LangGraph** (70.2)
- `pipeline`: **Haystack** (70.4)
- `structured`: **PydanticAI** (74.9)
- `tooling`: **Composio** (68.0)
- `typescript`: **Mastra** (77.9)
- `web-agent`: **BrowserUse** (89.2)

## 🔍 Top 5 — Score Breakdown

| Framework | Star Velocity | Release Freshness | Issue Health | Commit Activity | Community | Fork Ratio |
|-----------|:---:|:---:|:---:|:---:|:---:|:---:|
| **BrowserUse** | 100 | 94.3 | 91.4 | 100 | 72.2 | 44.0 |
| **Claude Agent SDK** | 100 | 99.3 | 87.7 | 100 | 10.8 | 65.4 |
| **CrewAI** | 68.4 | 98.7 | 92.5 | 100 | 67.0 | 58.0 |
| **OpenAI Agents SDK** | 37.4 | 99.0 | 99.0 | 100 | 76.8 | 64.6 |
| **Mastra** | 42.3 | 98.3 | 95.5 | 100 | 93.2 | 40.2 |

## 💡 Key Insights

- **Hottest framework**: BrowserUse with a Pulse Score of 89.2
- **Fastest growing**: Claude Agent SDK gained +2414 stars this week
- **Most active development**: Mastra with 1514 commits in the last 4 weeks
- **Stale releases**: AutoGen, Swarm haven't released in a while

## 📦 Recent Releases

- **Composio** [`@composio/cli@0.4.2-beta.400`](https://github.com/ComposioHQ/composio/releases/tag/@composio/cli@0.4.2-beta.400) — today *(pre-release)*
- **PydanticAI** [`v2.46.0`](https://github.com/pydantic/pydantic-ai/releases/tag/v2.46.0) — 2 days ago
- **Claude Agent SDK** [`v2.1.278`](https://github.com/anthropics/claude-code/releases/tag/v2.1.278) — 2 days ago
- **Google ADK** [`v2.9.2`](https://github.com/google/adk-python/releases/tag/v2.9.2) — 2 days ago
- **OpenAI Agents SDK** [`v0.22.3`](https://github.com/openai/openai-agents-python/releases/tag/v0.22.3) — 3 days ago
- **CrewAI** [`1.15.22`](https://github.com/crewAIInc/crewAI/releases/tag/1.15.22) — 4 days ago
- **Agno** [`v3.0.10`](https://github.com/agno-agi/agno/releases/tag/v3.0.10) — 4 days ago
- **Mastra** [`@mastra/core@1.67.0`](https://github.com/mastra-ai/mastra/releases/tag/@mastra/core@1.67.0) — 5 days ago
- **DSPy** [`3.4.0b1`](https://github.com/stanfordnlp/dspy/releases/tag/3.4.0b1) — 9 days ago *(pre-release)*
- **AG2** [`v1.0.5`](https://github.com/ag2ai/ag2/releases/tag/v1.0.5) — 9 days ago

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

*Powered by GitHub Actions • Data refreshed daily • Last run: 2026-09-21 12:27 UTC*