# 🔬 AI Agent Framework Pulse Tracker

[![Daily Update](https://github.com/PurpleHaze2320/ai-agent-pulse/actions/workflows/track.yml/badge.svg)](https://github.com/PurpleHaze2320/ai-agent-pulse/actions/workflows/track.yml)
[![Frameworks Tracked](https://img.shields.io/badge/frameworks-19-blue)](https://github.com/PurpleHaze2320/ai-agent-pulse)
[![License: MIT](https://img.shields.io/badge/License-MIT-green.svg)](https://opensource.org/licenses/MIT)
[![GitHub stars](https://img.shields.io/github/stars/PurpleHaze2320/ai-agent-pulse?style=social)](https://github.com/PurpleHaze2320/ai-agent-pulse/stargazers)

> Automated daily tracking of the AI agent framework ecosystem's health, momentum, and trends.
> Last updated: **2026-09-25 11:32 UTC** | Tracking **19** frameworks

## How It Works

This bot runs daily via GitHub Actions and collects metrics from the GitHub API for the most important
AI agent frameworks. It computes a **Pulse Score** (0-100) based on six weighted signals: star velocity,
release freshness, issue health, commit activity, community size, and fork engagement. The result is
a living dashboard that shows which frameworks are gaining momentum and which are losing steam.

## 🏆 Pulse Leaderboard

| Rank | Framework | Pulse | Stars | ⭐ 7d | Commits (4w) | Last Release | Category |
|------|-----------|-------|-------|-------|--------------|--------------|----------|
| 1 | [BrowserUse](https://github.com/browser-use/browser-use) | 🟢 **88.9** | 116.2k | 🚀 +1170 | 131 | 21 days ago | `web-agent` |
| 2 | [Claude Agent SDK](https://github.com/anthropics/claude-code) | 🟢 **85.8** | 148.0k | 🚀 +1990 | 124 | today | `orchestration` |
| 3 | [CrewAI](https://github.com/crewAIInc/crewAI) | 🟢 **80.8** | 59.0k | 🚀 +279 | 108 | 8 days ago | `multi-agent` |
| 4 | [Mastra](https://github.com/mastra-ai/mastra) | 🟢 **76.9** | 28.3k | 🚀 +172 | 2008 | today | `typescript` |
| 5 | [OpenAI Agents SDK](https://github.com/openai/openai-agents-python) | 🟢 **76.4** | 29.7k | 🚀 +147 | 149 | 7 days ago | `orchestration` |
| 6 | [Google ADK](https://github.com/google/adk-python) | 🟢 **72.9** | 21.6k | 📈 +69 | 411 | 6 days ago | `orchestration` |
| 7 | [Agno](https://github.com/agno-agi/agno) | 🟢 **70.7** | 42.3k | 🚀 +101 | 131 | 1 day ago | `multi-agent` |
| 8 | [LangGraph](https://github.com/langchain-ai/langgraph) | 🟢 **70.3** | 42.3k | 🚀 +382 | 41 | 1 day ago | `orchestration` |
| 9 | [Composio](https://github.com/ComposioHQ/composio) | 🟡 **67.3** | 30.3k | 📈 +85 | 292 | today | `tooling` |
| 10 | [AG2](https://github.com/ag2ai/ag2) | 🟡 **62.3** | 5.0k | ↗️ +19 | 61 | today | `multi-agent` |
| 11 | [LlamaIndex](https://github.com/run-llama/llama_index) | 🟡 **61.2** | 52.3k | 🚀 +103 | 29 | 3 days ago | `data-agent` |
| 12 | [DSPy](https://github.com/stanfordnlp/dspy) | 🟡 **60.8** | 38.3k | 🚀 +154 | 46 | today | `optimization` |
| 13 | [PydanticAI](https://github.com/pydantic/pydantic-ai) | 🟡 **54.5** | 20.2k | 🚀 +142 | 0 | today | `structured` |
| 14 | [Semantic Kernel](https://github.com/microsoft/semantic-kernel) | 🟡 **51.7** | 28.6k | 📈 +27 | 12 | 21 days ago | `enterprise` |
| 15 | [Haystack](https://github.com/deepset-ai/haystack) | 🟡 **51.4** | 26.6k | 📈 +59 | 0 | 1 day ago | `pipeline` |
| 16 | [Letta](https://github.com/letta-ai/letta) | 🟠 **38.4** | 24.9k | 📈 +92 | 2 | 4 mo ago | `memory` |
| 17 | [Smolagents](https://github.com/huggingface/smolagents) | 🟠 **35.4** | 29.5k | 🚀 +105 | 2 | 3 mo ago | `lightweight` |
| 18 | [AutoGen](https://github.com/microsoft/autogen) | 🟠 **33.0** | 61.2k | 🚀 +110 | 0 | 12 mo ago | `multi-agent` |
| 19 | [Swarm](https://github.com/openai/swarm) | 🔴 **9.5** | 22.0k | 📈 +21 | 0 | — | `experimental` |

## 📂 By Category

- `data-agent`: **LlamaIndex** (61.2)
- `enterprise`: **Semantic Kernel** (51.7)
- `experimental`: **Swarm** (9.5)
- `lightweight`: **Smolagents** (35.4)
- `memory`: **Letta** (38.4)
- `multi-agent`: **CrewAI** (80.8), **Agno** (70.7), **AG2** (62.3), **AutoGen** (33.0)
- `optimization`: **DSPy** (60.8)
- `orchestration`: **Claude Agent SDK** (85.8), **OpenAI Agents SDK** (76.4), **Google ADK** (72.9), **LangGraph** (70.3)
- `pipeline`: **Haystack** (51.4)
- `structured`: **PydanticAI** (54.5)
- `tooling`: **Composio** (67.3)
- `typescript`: **Mastra** (76.9)
- `web-agent`: **BrowserUse** (88.9)

## 🔍 Top 5 — Score Breakdown

| Framework | Star Velocity | Release Freshness | Issue Health | Commit Activity | Community | Fork Ratio |
|-----------|:---:|:---:|:---:|:---:|:---:|:---:|
| **BrowserUse** | 100 | 93.0 | 91.0 | 100 | 72.2 | 44.0 |
| **Claude Agent SDK** | 100 | 100.0 | 87.1 | 100 | 11.2 | 66.2 |
| **CrewAI** | 59.9 | 97.3 | 92.1 | 100 | 67.2 | 58.1 |
| **Mastra** | 36.8 | 100.0 | 95.6 | 100 | 93.2 | 40.3 |
| **OpenAI Agents SDK** | 31.4 | 97.7 | 98.7 | 100 | 77.0 | 64.8 |

## 💡 Key Insights

- **Hottest framework**: BrowserUse with a Pulse Score of 88.9
- **Fastest growing**: Claude Agent SDK gained +1990 stars this week
- **Most active development**: Mastra with 2008 commits in the last 4 weeks
- **Stale releases**: AutoGen, Swarm haven't released in a while

## 📦 Recent Releases

- **Mastra** [`@mastra/core@1.71.0`](https://github.com/mastra-ai/mastra/releases/tag/@mastra/core@1.71.0) — today
- **PydanticAI** [`v2.50.0`](https://github.com/pydantic/pydantic-ai/releases/tag/v2.50.0) — today
- **DSPy** [`3.4.0`](https://github.com/stanfordnlp/dspy/releases/tag/3.4.0) — today
- **AG2** [`v1.1.0`](https://github.com/ag2ai/ag2/releases/tag/v1.1.0) — today
- **Claude Agent SDK** [`v2.1.282`](https://github.com/anthropics/claude-code/releases/tag/v2.1.282) — today
- **Composio** [`versioning-example@0.1.5`](https://github.com/ComposioHQ/composio/releases/tag/versioning-example@0.1.5) — today
- **Haystack** [`v3.2.0`](https://github.com/deepset-ai/haystack/releases/tag/v3.2.0) — 1 day ago
- **LangGraph** [`cli==0.4.32.dev0`](https://github.com/langchain-ai/langgraph/releases/tag/cli==0.4.32.dev0) — 1 day ago
- **Agno** [`v3.0.11`](https://github.com/agno-agi/agno/releases/tag/v3.0.11) — 1 day ago
- **LlamaIndex** [`v0.14.25`](https://github.com/run-llama/llama_index/releases/tag/v0.14.25) — 3 days ago

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

*Powered by GitHub Actions • Data refreshed daily • Last run: 2026-09-25 11:32 UTC*