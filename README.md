# 🔬 AI Agent Framework Pulse Tracker

[![Daily Update](https://github.com/PurpleHaze2320/ai-agent-pulse/actions/workflows/track.yml/badge.svg)](https://github.com/PurpleHaze2320/ai-agent-pulse/actions/workflows/track.yml)
[![Frameworks Tracked](https://img.shields.io/badge/frameworks-19-blue)](https://github.com/PurpleHaze2320/ai-agent-pulse)
[![License: MIT](https://img.shields.io/badge/License-MIT-green.svg)](https://opensource.org/licenses/MIT)
[![GitHub stars](https://img.shields.io/github/stars/PurpleHaze2320/ai-agent-pulse?style=social)](https://github.com/PurpleHaze2320/ai-agent-pulse/stargazers)

> Automated daily tracking of the AI agent framework ecosystem's health, momentum, and trends.
> Last updated: **2026-04-17 07:58 UTC** | Tracking **19** frameworks

## How It Works

This bot runs daily via GitHub Actions and collects metrics from the GitHub API for the most important
AI agent frameworks. It computes a **Pulse Score** (0-100) based on six weighted signals: star velocity,
release freshness, issue health, commit activity, community size, and fork engagement. The result is
a living dashboard that shows which frameworks are gaining momentum and which are losing steam.

## 🏆 Pulse Leaderboard

| Rank | Framework | Pulse | Stars | ⭐ 7d | Commits (4w) | Last Release | Category |
|------|-----------|-------|-------|-------|--------------|--------------|----------|
| 1 | [Mastra](https://github.com/mastra-ai/mastra) | 🟢 **74.5** | 23.1k | 🚀 +226 | 779 | 8 days ago | `typescript` |
| 2 | [OpenAI Agents SDK](https://github.com/openai/openai-agents-python) | 🟢 **70.7** | 21.5k | 🚀 +775 | 0 | 1 day ago | `orchestration` |
| 3 | [CrewAI](https://github.com/crewAIInc/crewAI) | 🟢 **70.5** | 49.1k | 🚀 +581 | 0 | 1 day ago | `multi-agent` |
| 4 | [BrowserUse](https://github.com/browser-use/browser-use) | 🟡 **69.4** | 88.2k | 🚀 +1326 | 0 | 15 days ago | `web-agent` |
| 5 | [LangGraph](https://github.com/langchain-ai/langgraph) | 🟡 **69.3** | 29.5k | 🚀 +631 | 0 | today | `orchestration` |
| 6 | [Claude Agent SDK](https://github.com/anthropics/claude-code) | 🟡 **64.5** | 115.0k | 🚀 +3082 | 0 | today | `orchestration` |
| 7 | [LlamaIndex](https://github.com/run-llama/llama_index) | 🟡 **56.8** | 48.6k | 🚀 +172 | 0 | 13 days ago | `data-agent` |
| 8 | [PydanticAI](https://github.com/pydantic/pydantic-ai) | 🟡 **54.2** | 16.4k | 🚀 +204 | 0 | today | `structured` |
| 9 | [Agno](https://github.com/agno-agi/agno) | 🟡 **53.7** | 39.5k | 🚀 +176 | 0 | 2 days ago | `multi-agent` |
| 10 | [Google ADK](https://github.com/google/adk-python) | 🟡 **51.8** | 19.0k | 🚀 +178 | 0 | today | `orchestration` |
| 11 | [Semantic Kernel](https://github.com/microsoft/semantic-kernel) | 🟡 **49.7** | 27.7k | 📈 +44 | 0 | 9 days ago | `enterprise` |
| 12 | [Haystack](https://github.com/deepset-ai/haystack) | 🟡 **48.2** | 24.9k | 📈 +78 | 0 | 15 days ago | `pipeline` |
| 13 | [AG2](https://github.com/ag2ai/ag2) | 🟡 **46.8** | 4.4k | 📈 +29 | 0 | 12 days ago | `multi-agent` |
| 14 | [DSPy](https://github.com/stanfordnlp/dspy) | 🟡 **46.4** | 33.8k | 🚀 +184 | 0 | 2 mo ago | `optimization` |
| 15 | [Letta](https://github.com/letta-ai/letta) | 🟡 **45.9** | 22.1k | 🚀 +133 | 0 | 16 days ago | `memory` |
| 16 | [AutoGen](https://github.com/microsoft/autogen) | 🟡 **45.3** | 57.2k | 🚀 +256 | 0 | 6 mo ago | `multi-agent` |
| 17 | [Composio](https://github.com/ComposioHQ/composio) | 🟡 **45.0** | 27.8k | 🚀 +105 | 0 | today | `tooling` |
| 18 | [Smolagents](https://github.com/huggingface/smolagents) | 🟠 **37.9** | 26.7k | 🚀 +145 | 0 | 3 mo ago | `lightweight` |
| 19 | [Swarm](https://github.com/openai/swarm) | 🔴 **9.8** | 21.3k | 📈 +40 | 0 | — | `experimental` |

## 📂 By Category

- `data-agent`: **LlamaIndex** (56.8)
- `enterprise`: **Semantic Kernel** (49.7)
- `experimental`: **Swarm** (9.8)
- `lightweight`: **Smolagents** (37.9)
- `memory`: **Letta** (45.9)
- `multi-agent`: **CrewAI** (70.5), **Agno** (53.7), **AG2** (46.8), **AutoGen** (45.3)
- `optimization`: **DSPy** (46.4)
- `orchestration`: **OpenAI Agents SDK** (70.7), **LangGraph** (69.3), **Claude Agent SDK** (64.5), **Google ADK** (51.8)
- `pipeline`: **Haystack** (48.2)
- `structured`: **PydanticAI** (54.2)
- `tooling`: **Composio** (45.0)
- `typescript`: **Mastra** (74.5)
- `web-agent`: **BrowserUse** (69.4)

## 🔍 Top 5 — Score Breakdown

| Framework | Star Velocity | Release Freshness | Issue Health | Commit Activity | Community | Fork Ratio |
|-----------|:---:|:---:|:---:|:---:|:---:|:---:|
| **Mastra** | 39.3 | 97.3 | 94.6 | 100 | 77.0 | 33.0 |
| **OpenAI Agents SDK** | 100 | 99.7 | 96.1 | 0.0 | 49.2 | 64.5 |
| **CrewAI** | 100 | 99.7 | 95.9 | 0.0 | 57.0 | 54.7 |
| **BrowserUse** | 100 | 95.0 | 97.7 | 0.0 | 61.8 | 45.9 |
| **LangGraph** | 100 | 100.0 | 79.9 | 0.0 | 54.4 | 68.4 |

## 💡 Key Insights

- **Hottest framework**: Mastra with a Pulse Score of 74.5
- **Fastest growing**: Claude Agent SDK gained +3082 stars this week
- **Most active development**: Mastra with 779 commits in the last 4 weeks
- **Stale releases**: Swarm haven't released in a while

## 📦 Recent Releases

- **Google ADK** [`v1.31.0`](https://github.com/google/adk-python/releases/tag/v1.31.0) — today
- **PydanticAI** [`v1.84.0`](https://github.com/pydantic/pydantic-ai/releases/tag/v1.84.0) — today
- **Composio** [`@composio/cli@0.2.25-beta.214`](https://github.com/ComposioHQ/composio/releases/tag/@composio/cli@0.2.25-beta.214) — today *(pre-release)*
- **Claude Agent SDK** [`v2.1.112`](https://github.com/anthropics/claude-code/releases/tag/v2.1.112) — today
- **LangGraph** [`cli==0.4.22`](https://github.com/langchain-ai/langgraph/releases/tag/cli==0.4.22) — today
- **CrewAI** [`1.14.2rc1`](https://github.com/crewAIInc/crewAI/releases/tag/1.14.2rc1) — 1 day ago *(pre-release)*
- **OpenAI Agents SDK** [`v0.14.1`](https://github.com/openai/openai-agents-python/releases/tag/v0.14.1) — 1 day ago
- **Agno** [`v2.5.17`](https://github.com/agno-agi/agno/releases/tag/v2.5.17) — 2 days ago
- **Mastra** [`@mastra/core@1.24.0`](https://github.com/mastra-ai/mastra/releases/tag/@mastra/core@1.24.0) — 8 days ago
- **Semantic Kernel** [`python-1.41.2`](https://github.com/microsoft/semantic-kernel/releases/tag/python-1.41.2) — 9 days ago

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

*Powered by GitHub Actions • Data refreshed daily • Last run: 2026-04-17 07:58 UTC*