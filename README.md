# 🔬 AI Agent Framework Pulse Tracker

[![Daily Update](https://github.com/PurpleHaze2320/ai-agent-pulse/actions/workflows/track.yml/badge.svg)](https://github.com/PurpleHaze2320/ai-agent-pulse/actions/workflows/track.yml)
[![Frameworks Tracked](https://img.shields.io/badge/frameworks-19-blue)](https://github.com/PurpleHaze2320/ai-agent-pulse)
[![License: MIT](https://img.shields.io/badge/License-MIT-green.svg)](https://opensource.org/licenses/MIT)
[![GitHub stars](https://img.shields.io/github/stars/PurpleHaze2320/ai-agent-pulse?style=social)](https://github.com/PurpleHaze2320/ai-agent-pulse/stargazers)

> Automated daily tracking of the AI agent framework ecosystem's health, momentum, and trends.
> Last updated: **2026-09-03 10:57 UTC** | Tracking **19** frameworks

## How It Works

This bot runs daily via GitHub Actions and collects metrics from the GitHub API for the most important
AI agent frameworks. It computes a **Pulse Score** (0-100) based on six weighted signals: star velocity,
release freshness, issue health, commit activity, community size, and fork engagement. The result is
a living dashboard that shows which frameworks are gaining momentum and which are losing steam.

## 🏆 Pulse Leaderboard

| Rank | Framework | Pulse | Stars | ⭐ 7d | Commits (4w) | Last Release | Category |
|------|-----------|-------|-------|-------|--------------|--------------|----------|
| 1 | [BrowserUse](https://github.com/browser-use/browser-use) | 🟢 **89.2** | 112.1k | 🚀 +721 | 144 | 17 days ago | `web-agent` |
| 2 | [OpenAI Agents SDK](https://github.com/openai/openai-agents-python) | 🟢 **76.1** | 29.2k | 🚀 +158 | 201 | 14 days ago | `orchestration` |
| 3 | [PydanticAI](https://github.com/pydantic/pydantic-ai) | 🟢 **75.3** | 19.7k | 🚀 +165 | 237 | today | `structured` |
| 4 | [Mastra](https://github.com/mastra-ai/mastra) | 🟢 **75.1** | 27.7k | 🚀 +142 | 1418 | 5 days ago | `typescript` |
| 5 | [Google ADK](https://github.com/google/adk-python) | 🟢 **73.3** | 21.4k | 📈 +81 | 449 | 6 days ago | `orchestration` |
| 6 | [Haystack](https://github.com/deepset-ai/haystack) | 🟢 **71.4** | 26.4k | 📈 +65 | 191 | today | `pipeline` |
| 7 | [LangGraph](https://github.com/langchain-ai/langgraph) | 🟢 **70.7** | 41.0k | 🚀 +422 | 29 | 6 days ago | `orchestration` |
| 8 | [Claude Agent SDK](https://github.com/anthropics/claude-code) | 🟢 **70.3** | 143.9k | 🚀 +695 | 26 | today | `orchestration` |
| 9 | [Agno](https://github.com/agno-agi/agno) | 🟡 **65.5** | 42.0k | 📈 +84 | 75 | 2 days ago | `multi-agent` |
| 10 | [CrewAI](https://github.com/crewAIInc/crewAI) | 🟡 **63.9** | 58.0k | 🚀 +359 | 0 | 6 days ago | `multi-agent` |
| 11 | [LlamaIndex](https://github.com/run-llama/llama_index) | 🟡 **63.7** | 52.0k | 📈 +100 | 42 | 14 days ago | `data-agent` |
| 12 | [DSPy](https://github.com/stanfordnlp/dspy) | 🟡 **63.7** | 37.7k | 🚀 +123 | 61 | 12 days ago | `optimization` |
| 13 | [AG2](https://github.com/ag2ai/ag2) | 🟡 **60.0** | 4.9k | ↗️ +9 | 53 | 5 days ago | `multi-agent` |
| 14 | [Semantic Kernel](https://github.com/microsoft/semantic-kernel) | 🟡 **53.4** | 28.5k | 📈 +22 | 19 | 15 days ago | `enterprise` |
| 15 | [Composio](https://github.com/ComposioHQ/composio) | 🟡 **48.7** | 30.0k | 🚀 +124 | 0 | today | `tooling` |
| 16 | [Letta](https://github.com/letta-ai/letta) | 🟡 **41.7** | 24.6k | 🚀 +134 | 3 | 3 mo ago | `memory` |
| 17 | [Smolagents](https://github.com/huggingface/smolagents) | 🟠 **37.6** | 29.1k | 🚀 +120 | 2 | 3 mo ago | `lightweight` |
| 18 | [AutoGen](https://github.com/microsoft/autogen) | 🟠 **33.9** | 60.8k | 🚀 +130 | 0 | 11 mo ago | `multi-agent` |
| 19 | [Swarm](https://github.com/openai/swarm) | 🔴 **9.1** | 21.9k | ↗️ +8 | 0 | — | `experimental` |

## 📂 By Category

- `data-agent`: **LlamaIndex** (63.7)
- `enterprise`: **Semantic Kernel** (53.4)
- `experimental`: **Swarm** (9.1)
- `lightweight`: **Smolagents** (37.6)
- `memory`: **Letta** (41.7)
- `multi-agent`: **Agno** (65.5), **CrewAI** (63.9), **AG2** (60.0), **AutoGen** (33.9)
- `optimization`: **DSPy** (63.7)
- `orchestration`: **OpenAI Agents SDK** (76.1), **Google ADK** (73.3), **LangGraph** (70.7), **Claude Agent SDK** (70.3)
- `pipeline`: **Haystack** (71.4)
- `structured`: **PydanticAI** (75.3)
- `tooling`: **Composio** (48.7)
- `typescript`: **Mastra** (75.1)
- `web-agent`: **BrowserUse** (89.2)

## 🔍 Top 5 — Score Breakdown

| Framework | Star Velocity | Release Freshness | Issue Health | Commit Activity | Community | Fork Ratio |
|-----------|:---:|:---:|:---:|:---:|:---:|:---:|
| **BrowserUse** | 100 | 94.3 | 92.7 | 100 | 70.4 | 44.0 |
| **OpenAI Agents SDK** | 34.0 | 95.3 | 98.5 | 100 | 73.6 | 63.9 |
| **PydanticAI** | 32.9 | 100.0 | 81.7 | 100 | 94.8 | 53.5 |
| **Mastra** | 31.4 | 98.3 | 95.2 | 100 | 93.2 | 39.4 |
| **Google ADK** | 17.2 | 98.0 | 90.8 | 100 | 83.8 | 73.6 |

## 💡 Key Insights

- **Hottest framework**: BrowserUse with a Pulse Score of 89.2
- **Fastest growing**: BrowserUse gained +721 stars this week
- **Most active development**: Mastra with 1418 commits in the last 4 weeks
- **Stale releases**: AutoGen, Swarm haven't released in a while

## 📦 Recent Releases

- **Haystack** [`v3.1.1`](https://github.com/deepset-ai/haystack/releases/tag/v3.1.1) — today
- **PydanticAI** [`v2.38.0`](https://github.com/pydantic/pydantic-ai/releases/tag/v2.38.0) — today
- **Composio** [`@composio/cli@0.4.1-beta.374`](https://github.com/ComposioHQ/composio/releases/tag/@composio/cli@0.4.1-beta.374) — today *(pre-release)*
- **Claude Agent SDK** [`v2.1.259`](https://github.com/anthropics/claude-code/releases/tag/v2.1.259) — today
- **Agno** [`v3.0.5`](https://github.com/agno-agi/agno/releases/tag/v3.0.5) — 2 days ago
- **AG2** [`v1.0.3`](https://github.com/ag2ai/ag2/releases/tag/v1.0.3) — 5 days ago
- **Mastra** [`@mastra/core@1.63.0`](https://github.com/mastra-ai/mastra/releases/tag/@mastra/core@1.63.0) — 5 days ago
- **Google ADK** [`v1.39.1`](https://github.com/google/adk-python/releases/tag/v1.39.1) — 6 days ago
- **LangGraph** [`sdk==0.4.4`](https://github.com/langchain-ai/langgraph/releases/tag/sdk==0.4.4) — 6 days ago
- **CrewAI** [`1.15.18`](https://github.com/crewAIInc/crewAI/releases/tag/1.15.18) — 6 days ago

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

*Powered by GitHub Actions • Data refreshed daily • Last run: 2026-09-03 10:57 UTC*