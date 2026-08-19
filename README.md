# 🔬 AI Agent Framework Pulse Tracker

[![Daily Update](https://github.com/PurpleHaze2320/ai-agent-pulse/actions/workflows/track.yml/badge.svg)](https://github.com/PurpleHaze2320/ai-agent-pulse/actions/workflows/track.yml)
[![Frameworks Tracked](https://img.shields.io/badge/frameworks-19-blue)](https://github.com/PurpleHaze2320/ai-agent-pulse)
[![License: MIT](https://img.shields.io/badge/License-MIT-green.svg)](https://opensource.org/licenses/MIT)
[![GitHub stars](https://img.shields.io/github/stars/PurpleHaze2320/ai-agent-pulse?style=social)](https://github.com/PurpleHaze2320/ai-agent-pulse/stargazers)

> Automated daily tracking of the AI agent framework ecosystem's health, momentum, and trends.
> Last updated: **2026-08-19 06:52 UTC** | Tracking **19** frameworks

## How It Works

This bot runs daily via GitHub Actions and collects metrics from the GitHub API for the most important
AI agent frameworks. It computes a **Pulse Score** (0-100) based on six weighted signals: star velocity,
release freshness, issue health, commit activity, community size, and fork engagement. The result is
a living dashboard that shows which frameworks are gaining momentum and which are losing steam.

## 🏆 Pulse Leaderboard

| Rank | Framework | Pulse | Stars | ⭐ 7d | Commits (4w) | Last Release | Category |
|------|-----------|-------|-------|-------|--------------|--------------|----------|
| 1 | [BrowserUse](https://github.com/browser-use/browser-use) | 🟢 **90.0** | 109.7k | 🚀 +798 | 116 | 2 days ago | `web-agent` |
| 2 | [Mastra](https://github.com/mastra-ai/mastra) | 🟢 **77.2** | 27.3k | 🚀 +176 | 1486 | 2 days ago | `typescript` |
| 3 | [PydanticAI](https://github.com/pydantic/pydantic-ai) | 🟢 **74.6** | 19.4k | 🚀 +136 | 247 | today | `structured` |
| 4 | [Google ADK](https://github.com/google/adk-python) | 🟢 **74.3** | 21.2k | 🚀 +104 | 405 | 1 day ago | `orchestration` |
| 5 | [LangGraph](https://github.com/langchain-ai/langgraph) | 🟢 **73.7** | 40.0k | 🚀 +483 | 32 | 7 days ago | `orchestration` |
| 6 | [Haystack](https://github.com/deepset-ai/haystack) | 🟢 **71.1** | 26.2k | 📈 +66 | 176 | today | `pipeline` |
| 7 | [Composio](https://github.com/ComposioHQ/composio) | 🟡 **68.6** | 29.8k | 🚀 +126 | 297 | today | `tooling` |
| 8 | [Claude Agent SDK](https://github.com/anthropics/claude-code) | 🟡 **67.8** | 141.9k | 🚀 +800 | 14 | today | `orchestration` |
| 9 | [DSPy](https://github.com/stanfordnlp/dspy) | 🟡 **66.1** | 37.4k | 🚀 +273 | 47 | 15 days ago | `optimization` |
| 10 | [CrewAI](https://github.com/crewAIInc/crewAI) | 🟡 **62.3** | 57.3k | 🚀 +321 | 0 | 5 days ago | `multi-agent` |
| 11 | [AG2](https://github.com/ag2ai/ag2) | 🟡 **62.3** | 4.9k | 📈 +21 | 62 | 4 days ago | `multi-agent` |
| 12 | [LlamaIndex](https://github.com/run-llama/llama_index) | 🟡 **60.0** | 51.7k | 🚀 +160 | 24 | 1 mo ago | `data-agent` |
| 13 | [Agno](https://github.com/agno-agi/agno) | 🟡 **59.5** | 41.8k | 🚀 +101 | 43 | 5 days ago | `multi-agent` |
| 14 | [OpenAI Agents SDK](https://github.com/openai/openai-agents-python) | 🟡 **57.3** | 28.8k | 🚀 +187 | 0 | 2 days ago | `orchestration` |
| 15 | [Semantic Kernel](https://github.com/microsoft/semantic-kernel) | 🟡 **54.2** | 28.5k | ↗️ +20 | 18 | today | `enterprise` |
| 16 | [Letta](https://github.com/letta-ai/letta) | 🟡 **41.0** | 24.3k | 📈 +91 | 4 | 3 mo ago | `memory` |
| 17 | [Smolagents](https://github.com/huggingface/smolagents) | 🟠 **37.8** | 28.9k | 🚀 +110 | 0 | 2 mo ago | `lightweight` |
| 18 | [AutoGen](https://github.com/microsoft/autogen) | 🟠 **34.1** | 60.5k | 🚀 +126 | 0 | 10 mo ago | `multi-agent` |
| 19 | [Swarm](https://github.com/openai/swarm) | 🔴 **9.4** | 21.9k | ↗️ +16 | 0 | — | `experimental` |

## 📂 By Category

- `data-agent`: **LlamaIndex** (60.0)
- `enterprise`: **Semantic Kernel** (54.2)
- `experimental`: **Swarm** (9.4)
- `lightweight`: **Smolagents** (37.8)
- `memory`: **Letta** (41.0)
- `multi-agent`: **CrewAI** (62.3), **AG2** (62.3), **Agno** (59.5), **AutoGen** (34.1)
- `optimization`: **DSPy** (66.1)
- `orchestration`: **Google ADK** (74.3), **LangGraph** (73.7), **Claude Agent SDK** (67.8), **OpenAI Agents SDK** (57.3)
- `pipeline`: **Haystack** (71.1)
- `structured`: **PydanticAI** (74.6)
- `tooling`: **Composio** (68.6)
- `typescript`: **Mastra** (77.2)
- `web-agent`: **BrowserUse** (90.0)

## 🔍 Top 5 — Score Breakdown

| Framework | Star Velocity | Release Freshness | Issue Health | Commit Activity | Community | Fork Ratio |
|-----------|:---:|:---:|:---:|:---:|:---:|:---:|
| **BrowserUse** | 100 | 99.3 | 93.6 | 100 | 66.8 | 44.0 |
| **Mastra** | 38.7 | 99.3 | 96.1 | 100 | 93.0 | 38.9 |
| **PydanticAI** | 29.8 | 100.0 | 82.7 | 100 | 95.0 | 52.6 |
| **Google ADK** | 20.7 | 99.7 | 90.2 | 100 | 83.4 | 72.9 |
| **LangGraph** | 100 | 97.7 | 69.7 | 32.0 | 55.6 | 67.4 |

## 💡 Key Insights

- **Hottest framework**: BrowserUse with a Pulse Score of 90.0
- **Fastest growing**: Claude Agent SDK gained +800 stars this week
- **Most active development**: Mastra with 1486 commits in the last 4 weeks
- **Stale releases**: AutoGen, Swarm haven't released in a while

## 📦 Recent Releases

- **PydanticAI** [`v2.32.0`](https://github.com/pydantic/pydantic-ai/releases/tag/v2.32.0) — today
- **Composio** [`@composio/slim@0.17.0`](https://github.com/ComposioHQ/composio/releases/tag/@composio/slim@0.17.0) — today
- **Claude Agent SDK** [`v2.1.235`](https://github.com/anthropics/claude-code/releases/tag/v2.1.235) — today
- **Semantic Kernel** [`dotnet-1.80.0`](https://github.com/microsoft/semantic-kernel/releases/tag/dotnet-1.80.0) — today
- **Haystack** [`v3.1.0-rc1`](https://github.com/deepset-ai/haystack/releases/tag/v3.1.0-rc1) — today *(pre-release)*
- **Google ADK** [`v2.7.1`](https://github.com/google/adk-python/releases/tag/v2.7.1) — 1 day ago
- **OpenAI Agents SDK** [`v0.21.1`](https://github.com/openai/openai-agents-python/releases/tag/v0.21.1) — 2 days ago
- **BrowserUse** [`0.13.8`](https://github.com/browser-use/browser-use/releases/tag/0.13.8) — 2 days ago
- **Mastra** [`@mastra/core@1.59.0`](https://github.com/mastra-ai/mastra/releases/tag/@mastra/core@1.59.0) — 2 days ago
- **AG2** [`v1.0.2`](https://github.com/ag2ai/ag2/releases/tag/v1.0.2) — 4 days ago

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

*Powered by GitHub Actions • Data refreshed daily • Last run: 2026-08-19 06:52 UTC*