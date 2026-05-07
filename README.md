# 🔬 AI Agent Framework Pulse Tracker

[![Daily Update](https://github.com/PurpleHaze2320/ai-agent-pulse/actions/workflows/track.yml/badge.svg)](https://github.com/PurpleHaze2320/ai-agent-pulse/actions/workflows/track.yml)
[![Frameworks Tracked](https://img.shields.io/badge/frameworks-19-blue)](https://github.com/PurpleHaze2320/ai-agent-pulse)
[![License: MIT](https://img.shields.io/badge/License-MIT-green.svg)](https://opensource.org/licenses/MIT)
[![GitHub stars](https://img.shields.io/github/stars/PurpleHaze2320/ai-agent-pulse?style=social)](https://github.com/PurpleHaze2320/ai-agent-pulse/stargazers)

> Automated daily tracking of the AI agent framework ecosystem's health, momentum, and trends.
> Last updated: **2026-05-07 08:42 UTC** | Tracking **19** frameworks

## How It Works

This bot runs daily via GitHub Actions and collects metrics from the GitHub API for the most important
AI agent frameworks. It computes a **Pulse Score** (0-100) based on six weighted signals: star velocity,
release freshness, issue health, commit activity, community size, and fork engagement. The result is
a living dashboard that shows which frameworks are gaining momentum and which are losing steam.

## 🏆 Pulse Leaderboard

| Rank | Framework | Pulse | Stars | ⭐ 7d | Commits (4w) | Last Release | Category |
|------|-----------|-------|-------|-------|--------------|--------------|----------|
| 1 | [Mastra](https://github.com/mastra-ai/mastra) | 🟢 **76.2** | 23.6k | 🚀 +195 | 885 | today | `typescript` |
| 2 | [CrewAI](https://github.com/crewAIInc/crewAI) | 🟢 **71.2** | 50.8k | 🚀 +460 | 0 | today | `multi-agent` |
| 3 | [OpenAI Agents SDK](https://github.com/openai/openai-agents-python) | 🟢 **71.0** | 26.0k | 🚀 +387 | 0 | today | `orchestration` |
| 4 | [LangGraph](https://github.com/langchain-ai/langgraph) | 🟡 **68.9** | 31.4k | 🚀 +520 | 0 | 1 day ago | `orchestration` |
| 5 | [BrowserUse](https://github.com/browser-use/browser-use) | 🟡 **68.0** | 92.6k | 🚀 +1308 | 0 | 1 mo ago | `web-agent` |
| 6 | [Claude Agent SDK](https://github.com/anthropics/claude-code) | 🟡 **64.8** | 121.1k | 🚀 +1769 | 0 | today | `orchestration` |
| 7 | [LlamaIndex](https://github.com/run-llama/llama_index) | 🟡 **56.7** | 49.2k | 🚀 +132 | 0 | 16 days ago | `data-agent` |
| 8 | [Agno](https://github.com/agno-agi/agno) | 🟡 **54.2** | 40.0k | 🚀 +152 | 0 | today | `multi-agent` |
| 9 | [PydanticAI](https://github.com/pydantic/pydantic-ai) | 🟡 **53.5** | 16.9k | 🚀 +135 | 0 | today | `structured` |
| 10 | [Google ADK](https://github.com/google/adk-python) | 🟡 **51.4** | 19.5k | 🚀 +130 | 0 | 6 days ago | `orchestration` |
| 11 | [DSPy](https://github.com/stanfordnlp/dspy) | 🟡 **51.2** | 34.3k | 🚀 +147 | 0 | 1 day ago | `optimization` |
| 12 | [Semantic Kernel](https://github.com/microsoft/semantic-kernel) | 🟡 **50.3** | 27.9k | 📈 +32 | 0 | 7 days ago | `enterprise` |
| 13 | [AG2](https://github.com/ag2ai/ag2) | 🟡 **49.6** | 4.5k | 📈 +53 | 0 | 1 day ago | `multi-agent` |
| 14 | [Haystack](https://github.com/deepset-ai/haystack) | 🟡 **48.7** | 25.1k | 📈 +73 | 0 | 16 days ago | `pipeline` |
| 15 | [Composio](https://github.com/ComposioHQ/composio) | 🟡 **46.8** | 28.1k | 🚀 +128 | 0 | today | `tooling` |
| 16 | [Letta](https://github.com/letta-ai/letta) | 🟡 **44.8** | 22.5k | 🚀 +102 | 0 | 1 mo ago | `memory` |
| 17 | [AutoGen](https://github.com/microsoft/autogen) | 🟡 **43.1** | 57.8k | 🚀 +187 | 0 | 7 mo ago | `multi-agent` |
| 18 | [Smolagents](https://github.com/huggingface/smolagents) | 🟠 **37.2** | 27.1k | 🚀 +129 | 0 | 3 mo ago | `lightweight` |
| 19 | [Swarm](https://github.com/openai/swarm) | 🔴 **9.5** | 21.4k | 📈 +29 | 0 | — | `experimental` |

## 📂 By Category

- `data-agent`: **LlamaIndex** (56.7)
- `enterprise`: **Semantic Kernel** (50.3)
- `experimental`: **Swarm** (9.5)
- `lightweight`: **Smolagents** (37.2)
- `memory`: **Letta** (44.8)
- `multi-agent`: **CrewAI** (71.2), **Agno** (54.2), **AG2** (49.6), **AutoGen** (43.1)
- `optimization`: **DSPy** (51.2)
- `orchestration`: **OpenAI Agents SDK** (71.0), **LangGraph** (68.9), **Claude Agent SDK** (64.8), **Google ADK** (51.4)
- `pipeline`: **Haystack** (48.7)
- `structured`: **PydanticAI** (53.5)
- `tooling`: **Composio** (46.8)
- `typescript`: **Mastra** (76.2)
- `web-agent`: **BrowserUse** (68.0)

## 🔍 Top 5 — Score Breakdown

| Framework | Star Velocity | Release Freshness | Issue Health | Commit Activity | Community | Fork Ratio |
|-----------|:---:|:---:|:---:|:---:|:---:|:---:|
| **Mastra** | 40.5 | 100.0 | 94.4 | 100 | 84.6 | 34.2 |
| **CrewAI** | 100 | 100.0 | 98.5 | 0.0 | 58.8 | 55.2 |
| **OpenAI Agents SDK** | 100 | 100.0 | 96.8 | 0.0 | 53.0 | 61.3 |
| **LangGraph** | 100 | 99.7 | 78.1 | 0.0 | 54.8 | 68.0 |
| **BrowserUse** | 100 | 88.3 | 96.5 | 0.0 | 62.8 | 45.3 |

## 💡 Key Insights

- **Hottest framework**: Mastra with a Pulse Score of 76.2
- **Fastest growing**: Claude Agent SDK gained +1769 stars this week
- **Most active development**: Mastra with 885 commits in the last 4 weeks
- **Stale releases**: Swarm haven't released in a while

## 📦 Recent Releases

- **OpenAI Agents SDK** [`v0.16.0`](https://github.com/openai/openai-agents-python/releases/tag/v0.16.0) — today
- **PydanticAI** [`v1.91.0`](https://github.com/pydantic/pydantic-ai/releases/tag/v1.91.0) — today
- **Claude Agent SDK** [`v2.1.132`](https://github.com/anthropics/claude-code/releases/tag/v2.1.132) — today
- **CrewAI** [`1.14.5a3`](https://github.com/crewAIInc/crewAI/releases/tag/1.14.5a3) — today *(pre-release)*
- **Agno** [`v2.6.5`](https://github.com/agno-agi/agno/releases/tag/v2.6.5) — today
- **Mastra** [`@mastra/core@1.32.0`](https://github.com/mastra-ai/mastra/releases/tag/@mastra/core@1.32.0) — today
- **Composio** [`@composio/cli@0.2.29-beta.239`](https://github.com/ComposioHQ/composio/releases/tag/@composio/cli@0.2.29-beta.239) — today *(pre-release)*
- **AG2** [`v0.12.3`](https://github.com/ag2ai/ag2/releases/tag/v0.12.3) — 1 day ago
- **DSPy** [`3.2.1`](https://github.com/stanfordnlp/dspy/releases/tag/3.2.1) — 1 day ago
- **LangGraph** [`sdk==0.3.14`](https://github.com/langchain-ai/langgraph/releases/tag/sdk==0.3.14) — 1 day ago

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

*Powered by GitHub Actions • Data refreshed daily • Last run: 2026-05-07 08:42 UTC*