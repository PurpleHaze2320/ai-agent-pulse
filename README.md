# 🔬 AI Agent Framework Pulse Tracker

[![Daily Update](https://github.com/PurpleHaze2320/ai-agent-pulse/actions/workflows/track.yml/badge.svg)](https://github.com/PurpleHaze2320/ai-agent-pulse/actions/workflows/track.yml)
[![Frameworks Tracked](https://img.shields.io/badge/frameworks-19-blue)](https://github.com/PurpleHaze2320/ai-agent-pulse)
[![License: MIT](https://img.shields.io/badge/License-MIT-green.svg)](https://opensource.org/licenses/MIT)
[![GitHub stars](https://img.shields.io/github/stars/PurpleHaze2320/ai-agent-pulse?style=social)](https://github.com/PurpleHaze2320/ai-agent-pulse/stargazers)

> Automated daily tracking of the AI agent framework ecosystem's health, momentum, and trends.
> Last updated: **2026-07-26 08:33 UTC** | Tracking **19** frameworks

## How It Works

This bot runs daily via GitHub Actions and collects metrics from the GitHub API for the most important
AI agent frameworks. It computes a **Pulse Score** (0-100) based on six weighted signals: star velocity,
release freshness, issue health, commit activity, community size, and fork engagement. The result is
a living dashboard that shows which frameworks are gaining momentum and which are losing steam.

## 🏆 Pulse Leaderboard

| Rank | Framework | Pulse | Stars | ⭐ 7d | Commits (4w) | Last Release | Category |
|------|-----------|-------|-------|-------|--------------|--------------|----------|
| 1 | [BrowserUse](https://github.com/browser-use/browser-use) | 🟢 **84.3** | 106.8k | 🚀 +1318 | 75 | 9 days ago | `web-agent` |
| 2 | [Mastra](https://github.com/mastra-ai/mastra) | 🟢 **79.3** | 26.6k | 🚀 +247 | 912 | 10 days ago | `typescript` |
| 3 | [Google ADK](https://github.com/google/adk-python) | 🟢 **77.7** | 20.9k | 🚀 +225 | 254 | 4 days ago | `orchestration` |
| 4 | [CrewAI](https://github.com/crewAIInc/crewAI) | 🟢 **76.3** | 56.1k | 🚀 +373 | 54 | 1 day ago | `multi-agent` |
| 5 | [OpenAI Agents SDK](https://github.com/openai/openai-agents-python) | 🟢 **75.1** | 28.2k | 🚀 +165 | 129 | 9 days ago | `orchestration` |
| 6 | [Agno](https://github.com/agno-agi/agno) | 🟢 **73.9** | 41.4k | 🚀 +149 | 122 | today | `multi-agent` |
| 7 | [LangGraph](https://github.com/langchain-ai/langgraph) | 🟢 **70.5** | 38.2k | 🚀 +571 | 18 | 16 days ago | `orchestration` |
| 8 | [Haystack](https://github.com/deepset-ai/haystack) | 🟢 **70.4** | 26.0k | 📈 +74 | 211 | 5 days ago | `pipeline` |
| 9 | [Claude Agent SDK](https://github.com/anthropics/claude-code) | 🟡 **69.2** | 139.1k | 🚀 +884 | 21 | 1 day ago | `orchestration` |
| 10 | [Composio](https://github.com/ComposioHQ/composio) | 🟡 **66.7** | 29.4k | 📈 +95 | 110 | 5 days ago | `tooling` |
| 11 | [LlamaIndex](https://github.com/run-llama/llama_index) | 🟡 **59.4** | 51.1k | 🚀 +164 | 15 | 1 mo ago | `data-agent` |
| 12 | [PydanticAI](https://github.com/pydantic/pydantic-ai) | 🟡 **56.4** | 18.8k | 🚀 +170 | 0 | 1 day ago | `structured` |
| 13 | [Semantic Kernel](https://github.com/microsoft/semantic-kernel) | 🟡 **50.2** | 28.4k | 📈 +41 | 0 | 18 days ago | `enterprise` |
| 14 | [DSPy](https://github.com/stanfordnlp/dspy) | 🟡 **49.3** | 36.4k | 🚀 +168 | 0 | 1 mo ago | `optimization` |
| 15 | [AG2](https://github.com/ag2ai/ag2) | 🟡 **48.6** | 4.8k | ↗️ +17 | 0 | 22 days ago | `multi-agent` |
| 16 | [Letta](https://github.com/letta-ai/letta) | 🟡 **42.2** | 24.0k | 🚀 +103 | 0 | 2 mo ago | `memory` |
| 17 | [Smolagents](https://github.com/huggingface/smolagents) | 🟡 **40.4** | 28.5k | 🚀 +104 | 4 | 1 mo ago | `lightweight` |
| 18 | [AutoGen](https://github.com/microsoft/autogen) | 🟠 **35.6** | 60.0k | 🚀 +162 | 0 | 9 mo ago | `multi-agent` |
| 19 | [Swarm](https://github.com/openai/swarm) | 🔴 **10.2** | 21.9k | 📈 +34 | 0 | — | `experimental` |

## 📂 By Category

- `data-agent`: **LlamaIndex** (59.4)
- `enterprise`: **Semantic Kernel** (50.2)
- `experimental`: **Swarm** (10.2)
- `lightweight`: **Smolagents** (40.4)
- `memory`: **Letta** (42.2)
- `multi-agent`: **CrewAI** (76.3), **Agno** (73.9), **AG2** (48.6), **AutoGen** (35.6)
- `optimization`: **DSPy** (49.3)
- `orchestration`: **Google ADK** (77.7), **OpenAI Agents SDK** (75.1), **LangGraph** (70.5), **Claude Agent SDK** (69.2)
- `pipeline`: **Haystack** (70.4)
- `structured`: **PydanticAI** (56.4)
- `tooling`: **Composio** (66.7)
- `typescript`: **Mastra** (79.3)
- `web-agent`: **BrowserUse** (84.3)

## 🔍 Top 5 — Score Breakdown

| Framework | Star Velocity | Release Freshness | Issue Health | Commit Activity | Community | Fork Ratio |
|-----------|:---:|:---:|:---:|:---:|:---:|:---:|
| **BrowserUse** | 100 | 97.0 | 94.6 | 75.0 | 63.0 | 44.0 |
| **Mastra** | 51.1 | 96.7 | 94.0 | 100 | 93.0 | 37.8 |
| **Google ADK** | 40.3 | 98.7 | 87.5 | 100 | 75.8 | 72.0 |
| **CrewAI** | 78.2 | 99.7 | 96.1 | 54.0 | 59.6 | 56.7 |
| **OpenAI Agents SDK** | 34.1 | 97.0 | 98.2 | 100 | 62.6 | 62.1 |

## 💡 Key Insights

- **Hottest framework**: BrowserUse with a Pulse Score of 84.3
- **Fastest growing**: BrowserUse gained +1318 stars this week
- **Most active development**: Mastra with 912 commits in the last 4 weeks
- **Stale releases**: AutoGen, Swarm haven't released in a while

## 📦 Recent Releases

- **Agno** [`v2.8.3`](https://github.com/agno-agi/agno/releases/tag/v2.8.3) — today
- **Claude Agent SDK** [`v2.1.220`](https://github.com/anthropics/claude-code/releases/tag/v2.1.220) — 1 day ago
- **PydanticAI** [`v2.18.0`](https://github.com/pydantic/pydantic-ai/releases/tag/v2.18.0) — 1 day ago
- **CrewAI** [`1.15.6`](https://github.com/crewAIInc/crewAI/releases/tag/1.15.6) — 1 day ago
- **Google ADK** [`v1.36.2`](https://github.com/google/adk-python/releases/tag/v1.36.2) — 4 days ago
- **Composio** [`@composio/cli@0.2.33-beta.298`](https://github.com/ComposioHQ/composio/releases/tag/@composio/cli@0.2.33-beta.298) — 5 days ago *(pre-release)*
- **Haystack** [`v3.0.0`](https://github.com/deepset-ai/haystack/releases/tag/v3.0.0) — 5 days ago
- **BrowserUse** [`0.13.6`](https://github.com/browser-use/browser-use/releases/tag/0.13.6) — 9 days ago
- **OpenAI Agents SDK** [`v0.18.3`](https://github.com/openai/openai-agents-python/releases/tag/v0.18.3) — 9 days ago
- **Mastra** [`@mastra/core@1.51.0`](https://github.com/mastra-ai/mastra/releases/tag/@mastra/core@1.51.0) — 10 days ago

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

*Powered by GitHub Actions • Data refreshed daily • Last run: 2026-07-26 08:33 UTC*