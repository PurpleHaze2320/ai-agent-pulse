# 🔬 AI Agent Framework Pulse Tracker

[![Daily Update](https://github.com/PurpleHaze2320/ai-agent-pulse/actions/workflows/track.yml/badge.svg)](https://github.com/PurpleHaze2320/ai-agent-pulse/actions/workflows/track.yml)
[![Frameworks Tracked](https://img.shields.io/badge/frameworks-19-blue)](https://github.com/PurpleHaze2320/ai-agent-pulse)
[![License: MIT](https://img.shields.io/badge/License-MIT-green.svg)](https://opensource.org/licenses/MIT)
[![GitHub stars](https://img.shields.io/github/stars/PurpleHaze2320/ai-agent-pulse?style=social)](https://github.com/PurpleHaze2320/ai-agent-pulse/stargazers)

> Automated daily tracking of the AI agent framework ecosystem's health, momentum, and trends.
> Last updated: **2026-08-18 06:51 UTC** | Tracking **19** frameworks

## How It Works

This bot runs daily via GitHub Actions and collects metrics from the GitHub API for the most important
AI agent frameworks. It computes a **Pulse Score** (0-100) based on six weighted signals: star velocity,
release freshness, issue health, commit activity, community size, and fork engagement. The result is
a living dashboard that shows which frameworks are gaining momentum and which are losing steam.

## 🏆 Pulse Leaderboard

| Rank | Framework | Pulse | Stars | ⭐ 7d | Commits (4w) | Last Release | Category |
|------|-----------|-------|-------|-------|--------------|--------------|----------|
| 1 | [BrowserUse](https://github.com/browser-use/browser-use) | 🟢 **90.1** | 109.6k | 🚀 +849 | 113 | 1 day ago | `web-agent` |
| 2 | [CrewAI](https://github.com/crewAIInc/crewAI) | 🟢 **78.3** | 57.2k | 🚀 +306 | 82 | 4 days ago | `multi-agent` |
| 3 | [OpenAI Agents SDK](https://github.com/openai/openai-agents-python) | 🟢 **77.3** | 28.7k | 🚀 +182 | 337 | 1 day ago | `orchestration` |
| 4 | [Mastra](https://github.com/mastra-ai/mastra) | 🟢 **76.9** | 27.3k | 🚀 +167 | 1399 | 1 day ago | `typescript` |
| 5 | [PydanticAI](https://github.com/pydantic/pydantic-ai) | 🟢 **74.9** | 19.4k | 🚀 +146 | 228 | today | `structured` |
| 6 | [Google ADK](https://github.com/google/adk-python) | 🟢 **74.4** | 21.2k | 📈 +97 | 388 | today | `orchestration` |
| 7 | [LangGraph](https://github.com/langchain-ai/langgraph) | 🟢 **73.5** | 39.9k | 🚀 +479 | 31 | 6 days ago | `orchestration` |
| 8 | [Haystack](https://github.com/deepset-ai/haystack) | 🟡 **69.2** | 26.2k | 📈 +65 | 160 | 28 days ago | `pipeline` |
| 9 | [Composio](https://github.com/ComposioHQ/composio) | 🟡 **68.3** | 29.7k | 🚀 +120 | 285 | today | `tooling` |
| 10 | [Claude Agent SDK](https://github.com/anthropics/claude-code) | 🟡 **67.6** | 141.8k | 🚀 +819 | 13 | today | `orchestration` |
| 11 | [DSPy](https://github.com/stanfordnlp/dspy) | 🟡 **66.6** | 37.4k | 🚀 +294 | 46 | 14 days ago | `optimization` |
| 12 | [AG2](https://github.com/ag2ai/ag2) | 🟡 **61.9** | 4.9k | 📈 +21 | 59 | 3 days ago | `multi-agent` |
| 13 | [LlamaIndex](https://github.com/run-llama/llama_index) | 🟡 **59.8** | 51.7k | 🚀 +166 | 22 | 1 mo ago | `data-agent` |
| 14 | [Agno](https://github.com/agno-agi/agno) | 🟡 **59.3** | 41.8k | 📈 +97 | 42 | 4 days ago | `multi-agent` |
| 15 | [Semantic Kernel](https://github.com/microsoft/semantic-kernel) | 🟡 **52.8** | 28.5k | ↗️ +20 | 15 | 11 days ago | `enterprise` |
| 16 | [Letta](https://github.com/letta-ai/letta) | 🟡 **41.8** | 24.3k | 🚀 +109 | 4 | 3 mo ago | `memory` |
| 17 | [Smolagents](https://github.com/huggingface/smolagents) | 🟠 **37.5** | 28.8k | 📈 +99 | 0 | 2 mo ago | `lightweight` |
| 18 | [AutoGen](https://github.com/microsoft/autogen) | 🟠 **34.1** | 60.5k | 🚀 +125 | 0 | 10 mo ago | `multi-agent` |
| 19 | [Swarm](https://github.com/openai/swarm) | 🔴 **9.5** | 21.9k | ↗️ +17 | 0 | — | `experimental` |

## 📂 By Category

- `data-agent`: **LlamaIndex** (59.8)
- `enterprise`: **Semantic Kernel** (52.8)
- `experimental`: **Swarm** (9.5)
- `lightweight`: **Smolagents** (37.5)
- `memory`: **Letta** (41.8)
- `multi-agent`: **CrewAI** (78.3), **AG2** (61.9), **Agno** (59.3), **AutoGen** (34.1)
- `optimization`: **DSPy** (66.6)
- `orchestration`: **OpenAI Agents SDK** (77.3), **Google ADK** (74.4), **LangGraph** (73.5), **Claude Agent SDK** (67.6)
- `pipeline`: **Haystack** (69.2)
- `structured`: **PydanticAI** (74.9)
- `tooling`: **Composio** (68.3)
- `typescript`: **Mastra** (76.9)
- `web-agent`: **BrowserUse** (90.1)

## 🔍 Top 5 — Score Breakdown

| Framework | Star Velocity | Release Freshness | Issue Health | Commit Activity | Community | Fork Ratio |
|-----------|:---:|:---:|:---:|:---:|:---:|:---:|
| **BrowserUse** | 100 | 99.7 | 93.7 | 100 | 66.8 | 44.0 |
| **CrewAI** | 64.9 | 98.7 | 94.7 | 82.0 | 60.0 | 57.1 |
| **OpenAI Agents SDK** | 36.4 | 99.7 | 99.4 | 100 | 70.2 | 63.0 |
| **Mastra** | 37.4 | 99.7 | 96.3 | 100 | 93.0 | 38.8 |
| **PydanticAI** | 31.1 | 100.0 | 82.5 | 100 | 95.0 | 52.6 |

## 💡 Key Insights

- **Hottest framework**: BrowserUse with a Pulse Score of 90.1
- **Fastest growing**: BrowserUse gained +849 stars this week
- **Most active development**: Mastra with 1399 commits in the last 4 weeks
- **Stale releases**: AutoGen, Swarm haven't released in a while

## 📦 Recent Releases

- **PydanticAI** [`v2.31.1`](https://github.com/pydantic/pydantic-ai/releases/tag/v2.31.1) — today
- **Claude Agent SDK** [`v2.1.234`](https://github.com/anthropics/claude-code/releases/tag/v2.1.234) — today
- **Google ADK** [`v2.7.1`](https://github.com/google/adk-python/releases/tag/v2.7.1) — today
- **Composio** [`@composio/cli@0.3.4-beta.353`](https://github.com/ComposioHQ/composio/releases/tag/@composio/cli@0.3.4-beta.353) — today *(pre-release)*
- **OpenAI Agents SDK** [`v0.21.1`](https://github.com/openai/openai-agents-python/releases/tag/v0.21.1) — 1 day ago
- **BrowserUse** [`0.13.8`](https://github.com/browser-use/browser-use/releases/tag/0.13.8) — 1 day ago
- **Mastra** [`@mastra/core@1.59.0`](https://github.com/mastra-ai/mastra/releases/tag/@mastra/core@1.59.0) — 1 day ago
- **AG2** [`v1.0.2`](https://github.com/ag2ai/ag2/releases/tag/v1.0.2) — 3 days ago
- **CrewAI** [`1.15.16`](https://github.com/crewAIInc/crewAI/releases/tag/1.15.16) — 4 days ago
- **Agno** [`v2.9.0`](https://github.com/agno-agi/agno/releases/tag/v2.9.0) — 4 days ago

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

*Powered by GitHub Actions • Data refreshed daily • Last run: 2026-08-18 06:51 UTC*