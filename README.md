# 🔬 AI Agent Framework Pulse Tracker

[![Daily Update](https://github.com/PurpleHaze2320/ai-agent-pulse/actions/workflows/track.yml/badge.svg)](https://github.com/PurpleHaze2320/ai-agent-pulse/actions/workflows/track.yml)
[![Frameworks Tracked](https://img.shields.io/badge/frameworks-19-blue)](https://github.com/PurpleHaze2320/ai-agent-pulse)
[![License: MIT](https://img.shields.io/badge/License-MIT-green.svg)](https://opensource.org/licenses/MIT)
[![GitHub stars](https://img.shields.io/github/stars/PurpleHaze2320/ai-agent-pulse?style=social)](https://github.com/PurpleHaze2320/ai-agent-pulse/stargazers)

> Automated daily tracking of the AI agent framework ecosystem's health, momentum, and trends.
> Last updated: **2026-09-27 11:45 UTC** | Tracking **19** frameworks

## How It Works

This bot runs daily via GitHub Actions and collects metrics from the GitHub API for the most important
AI agent frameworks. It computes a **Pulse Score** (0-100) based on six weighted signals: star velocity,
release freshness, issue health, commit activity, community size, and fork engagement. The result is
a living dashboard that shows which frameworks are gaining momentum and which are losing steam.

## 🏆 Pulse Leaderboard

| Rank | Framework | Pulse | Stars | ⭐ 7d | Commits (4w) | Last Release | Category |
|------|-----------|-------|-------|-------|--------------|--------------|----------|
| 1 | [Claude Agent SDK](https://github.com/anthropics/claude-code) | 🟢 **85.7** | 148.3k | 🚀 +1397 | 119 | 1 day ago | `orchestration` |
| 2 | [BrowserUse](https://github.com/browser-use/browser-use) | 🟢 **77.5** | 116.5k | 🚀 +1019 | 44 | 23 days ago | `web-agent` |
| 3 | [CrewAI](https://github.com/crewAIInc/crewAI) | 🟢 **76.9** | 59.1k | 🚀 +276 | 83 | 10 days ago | `multi-agent` |
| 4 | [Mastra](https://github.com/mastra-ai/mastra) | 🟢 **76.1** | 28.4k | 🚀 +159 | 1750 | 2 days ago | `typescript` |
| 5 | [OpenAI Agents SDK](https://github.com/openai/openai-agents-python) | 🟢 **76.1** | 29.7k | 🚀 +143 | 158 | 9 days ago | `orchestration` |
| 6 | [PydanticAI](https://github.com/pydantic/pydantic-ai) | 🟢 **74.3** | 20.2k | 🚀 +143 | 419 | 1 day ago | `structured` |
| 7 | [Google ADK](https://github.com/google/adk-python) | 🟢 **73.5** | 21.7k | 📈 +77 | 317 | 1 day ago | `orchestration` |
| 8 | [Haystack](https://github.com/deepset-ai/haystack) | 🟢 **71.0** | 26.6k | 📈 +52 | 174 | 3 days ago | `pipeline` |
| 9 | [Agno](https://github.com/agno-agi/agno) | 🟡 **69.7** | 42.4k | 📈 +92 | 98 | 3 days ago | `multi-agent` |
| 10 | [Composio](https://github.com/ComposioHQ/composio) | 🟡 **66.8** | 30.3k | 📈 +78 | 254 | 2 days ago | `tooling` |
| 11 | [LangGraph](https://github.com/langchain-ai/langgraph) | 🟡 **65.0** | 42.3k | 🚀 +350 | 22 | 3 days ago | `orchestration` |
| 12 | [DSPy](https://github.com/stanfordnlp/dspy) | 🟡 **63.0** | 38.4k | 🚀 +216 | 46 | 2 days ago | `optimization` |
| 13 | [LlamaIndex](https://github.com/run-llama/llama_index) | 🟡 **58.4** | 52.3k | 📈 +88 | 19 | 5 days ago | `data-agent` |
| 14 | [Semantic Kernel](https://github.com/microsoft/semantic-kernel) | 🟡 **50.2** | 28.6k | 📈 +28 | 5 | 23 days ago | `enterprise` |
| 15 | [AG2](https://github.com/ag2ai/ag2) | 🟡 **50.1** | 5.0k | 📈 +24 | 0 | 2 days ago | `multi-agent` |
| 16 | [Letta](https://github.com/letta-ai/letta) | 🟠 **38.3** | 24.9k | 📈 +95 | 2 | 4 mo ago | `memory` |
| 17 | [Smolagents](https://github.com/huggingface/smolagents) | 🟠 **35.2** | 29.5k | 🚀 +104 | 2 | 4 mo ago | `lightweight` |
| 18 | [AutoGen](https://github.com/microsoft/autogen) | 🟠 **33.1** | 61.2k | 🚀 +114 | 0 | 12 mo ago | `multi-agent` |
| 19 | [Swarm](https://github.com/openai/swarm) | 🔴 **9.5** | 22.0k | ↗️ +20 | 0 | — | `experimental` |

## 📂 By Category

- `data-agent`: **LlamaIndex** (58.4)
- `enterprise`: **Semantic Kernel** (50.2)
- `experimental`: **Swarm** (9.5)
- `lightweight`: **Smolagents** (35.2)
- `memory`: **Letta** (38.3)
- `multi-agent`: **CrewAI** (76.9), **Agno** (69.7), **AG2** (50.1), **AutoGen** (33.1)
- `optimization`: **DSPy** (63.0)
- `orchestration`: **Claude Agent SDK** (85.7), **OpenAI Agents SDK** (76.1), **Google ADK** (73.5), **LangGraph** (65.0)
- `pipeline`: **Haystack** (71.0)
- `structured`: **PydanticAI** (74.3)
- `tooling`: **Composio** (66.8)
- `typescript`: **Mastra** (76.1)
- `web-agent`: **BrowserUse** (77.5)

## 🔍 Top 5 — Score Breakdown

| Framework | Star Velocity | Release Freshness | Issue Health | Commit Activity | Community | Fork Ratio |
|-----------|:---:|:---:|:---:|:---:|:---:|:---:|
| **Claude Agent SDK** | 100 | 99.7 | 86.7 | 100 | 11.2 | 66.9 |
| **BrowserUse** | 100 | 92.3 | 90.8 | 44.0 | 72.2 | 44.1 |
| **CrewAI** | 58.7 | 96.7 | 91.8 | 83.0 | 67.2 | 58.1 |
| **Mastra** | 34.5 | 99.3 | 95.2 | 100 | 93.2 | 40.4 |
| **OpenAI Agents SDK** | 30.1 | 97.0 | 99.1 | 100 | 78.2 | 64.8 |

## 💡 Key Insights

- **Hottest framework**: Claude Agent SDK with a Pulse Score of 85.7
- **Fastest growing**: Claude Agent SDK gained +1397 stars this week
- **Most active development**: Mastra with 1750 commits in the last 4 weeks
- **Stale releases**: AutoGen, Swarm haven't released in a while

## 📦 Recent Releases

- **PydanticAI** [`v2.51.0`](https://github.com/pydantic/pydantic-ai/releases/tag/v2.51.0) — 1 day ago
- **Claude Agent SDK** [`v2.1.283`](https://github.com/anthropics/claude-code/releases/tag/v2.1.283) — 1 day ago
- **Google ADK** [`v2.10.0`](https://github.com/google/adk-python/releases/tag/v2.10.0) — 1 day ago
- **Mastra** [`@mastra/core@1.71.0`](https://github.com/mastra-ai/mastra/releases/tag/@mastra/core@1.71.0) — 2 days ago
- **DSPy** [`3.4.0`](https://github.com/stanfordnlp/dspy/releases/tag/3.4.0) — 2 days ago
- **AG2** [`v1.1.0`](https://github.com/ag2ai/ag2/releases/tag/v1.1.0) — 2 days ago
- **Composio** [`versioning-example@0.1.5`](https://github.com/ComposioHQ/composio/releases/tag/versioning-example@0.1.5) — 2 days ago
- **Haystack** [`v3.2.0`](https://github.com/deepset-ai/haystack/releases/tag/v3.2.0) — 3 days ago
- **LangGraph** [`cli==0.4.32.dev0`](https://github.com/langchain-ai/langgraph/releases/tag/cli==0.4.32.dev0) — 3 days ago
- **Agno** [`v3.0.11`](https://github.com/agno-agi/agno/releases/tag/v3.0.11) — 3 days ago

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

*Powered by GitHub Actions • Data refreshed daily • Last run: 2026-09-27 11:45 UTC*