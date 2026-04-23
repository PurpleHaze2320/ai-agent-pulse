# 🔬 AI Agent Framework Pulse Tracker

[![Daily Update](https://github.com/PurpleHaze2320/ai-agent-pulse/actions/workflows/track.yml/badge.svg)](https://github.com/PurpleHaze2320/ai-agent-pulse/actions/workflows/track.yml)
[![Frameworks Tracked](https://img.shields.io/badge/frameworks-19-blue)](https://github.com/PurpleHaze2320/ai-agent-pulse)
[![License: MIT](https://img.shields.io/badge/License-MIT-green.svg)](https://opensource.org/licenses/MIT)
[![GitHub stars](https://img.shields.io/github/stars/PurpleHaze2320/ai-agent-pulse?style=social)](https://github.com/PurpleHaze2320/ai-agent-pulse/stargazers)

> Automated daily tracking of the AI agent framework ecosystem's health, momentum, and trends.
> Last updated: **2026-04-23 08:04 UTC** | Tracking **19** frameworks

## How It Works

This bot runs daily via GitHub Actions and collects metrics from the GitHub API for the most important
AI agent frameworks. It computes a **Pulse Score** (0-100) based on six weighted signals: star velocity,
release freshness, issue health, commit activity, community size, and fork engagement. The result is
a living dashboard that shows which frameworks are gaining momentum and which are losing steam.

## 🏆 Pulse Leaderboard

| Rank | Framework | Pulse | Stars | ⭐ 7d | Commits (4w) | Last Release | Category |
|------|-----------|-------|-------|-------|--------------|--------------|----------|
| 1 | [Mastra](https://github.com/mastra-ai/mastra) | 🟢 **73.8** | 23.2k | 🚀 +196 | 786 | 14 days ago | `typescript` |
| 2 | [PydanticAI](https://github.com/pydantic/pydantic-ai) | 🟢 **73.5** | 16.6k | 🚀 +163 | 119 | today | `structured` |
| 3 | [CrewAI](https://github.com/crewAIInc/crewAI) | 🟢 **70.6** | 49.6k | 🚀 +635 | 0 | today | `multi-agent` |
| 4 | [OpenAI Agents SDK](https://github.com/openai/openai-agents-python) | 🟢 **70.6** | 24.7k | 🚀 +3846 | 0 | today | `orchestration` |
| 5 | [LangGraph](https://github.com/langchain-ai/langgraph) | 🟡 **69.2** | 30.1k | 🚀 +697 | 0 | today | `orchestration` |
| 6 | [BrowserUse](https://github.com/browser-use/browser-use) | 🟡 **69.0** | 89.6k | 🚀 +1582 | 0 | 21 days ago | `web-agent` |
| 7 | [Claude Agent SDK](https://github.com/anthropics/claude-code) | 🟡 **64.6** | 117.1k | 🚀 +2498 | 0 | today | `orchestration` |
| 8 | [LlamaIndex](https://github.com/run-llama/llama_index) | 🟡 **59.5** | 48.8k | 🚀 +208 | 0 | 2 days ago | `data-agent` |
| 9 | [Google ADK](https://github.com/google/adk-python) | 🟡 **53.1** | 19.2k | 🚀 +195 | 0 | today | `orchestration` |
| 10 | [Agno](https://github.com/agno-agi/agno) | 🟡 **52.9** | 39.6k | 🚀 +152 | 0 | 8 days ago | `multi-agent` |
| 11 | [DSPy](https://github.com/stanfordnlp/dspy) | 🟡 **52.0** | 33.9k | 🚀 +191 | 0 | 1 day ago | `optimization` |
| 12 | [Haystack](https://github.com/deepset-ai/haystack) | 🟡 **50.6** | 25.0k | 🚀 +109 | 0 | 2 days ago | `pipeline` |
| 13 | [Semantic Kernel](https://github.com/microsoft/semantic-kernel) | 🟡 **49.6** | 27.8k | 📈 +49 | 0 | 15 days ago | `enterprise` |
| 14 | [AG2](https://github.com/ag2ai/ag2) | 🟡 **47.4** | 4.4k | 📈 +31 | 0 | 5 days ago | `multi-agent` |
| 15 | [Letta](https://github.com/letta-ai/letta) | 🟡 **46.4** | 22.2k | 🚀 +144 | 0 | 22 days ago | `memory` |
| 16 | [Composio](https://github.com/ComposioHQ/composio) | 🟡 **44.5** | 27.9k | 📈 +89 | 0 | 5 days ago | `tooling` |
| 17 | [AutoGen](https://github.com/microsoft/autogen) | 🟡 **44.4** | 57.4k | 🚀 +221 | 0 | 6 mo ago | `multi-agent` |
| 18 | [Smolagents](https://github.com/huggingface/smolagents) | 🟠 **39.6** | 26.8k | 🚀 +188 | 0 | 3 mo ago | `lightweight` |
| 19 | [Swarm](https://github.com/openai/swarm) | 🔴 **10.4** | 21.4k | 📈 +54 | 0 | — | `experimental` |

## 📂 By Category

- `data-agent`: **LlamaIndex** (59.5)
- `enterprise`: **Semantic Kernel** (49.6)
- `experimental`: **Swarm** (10.4)
- `lightweight`: **Smolagents** (39.6)
- `memory`: **Letta** (46.4)
- `multi-agent`: **CrewAI** (70.6), **Agno** (52.9), **AG2** (47.4), **AutoGen** (44.4)
- `optimization`: **DSPy** (52.0)
- `orchestration`: **OpenAI Agents SDK** (70.6), **LangGraph** (69.2), **Claude Agent SDK** (64.6), **Google ADK** (53.1)
- `pipeline`: **Haystack** (50.6)
- `structured`: **PydanticAI** (73.5)
- `tooling`: **Composio** (44.5)
- `typescript`: **Mastra** (73.8)
- `web-agent`: **BrowserUse** (69.0)

## 🔍 Top 5 — Score Breakdown

| Framework | Star Velocity | Release Freshness | Issue Health | Commit Activity | Community | Fork Ratio |
|-----------|:---:|:---:|:---:|:---:|:---:|:---:|
| **Mastra** | 37.5 | 95.3 | 94.4 | 100 | 79.0 | 33.4 |
| **PydanticAI** | 31.0 | 100.0 | 83.1 | 100 | 85.2 | 47.5 |
| **CrewAI** | 100 | 100.0 | 95.6 | 0.0 | 57.4 | 54.8 |
| **OpenAI Agents SDK** | 100 | 100.0 | 96.2 | 0.0 | 50.8 | 61.1 |
| **LangGraph** | 100 | 100.0 | 79.4 | 0.0 | 54.8 | 68.3 |

## 💡 Key Insights

- **Hottest framework**: Mastra with a Pulse Score of 73.8
- **Fastest growing**: OpenAI Agents SDK gained +3846 stars this week
- **Most active development**: Mastra with 786 commits in the last 4 weeks
- **Stale releases**: Swarm haven't released in a while

## 📦 Recent Releases

- **PydanticAI** [`v1.86.0`](https://github.com/pydantic/pydantic-ai/releases/tag/v1.86.0) — today
- **OpenAI Agents SDK** [`v0.14.5`](https://github.com/openai/openai-agents-python/releases/tag/v0.14.5) — today
- **Claude Agent SDK** [`v2.1.118`](https://github.com/anthropics/claude-code/releases/tag/v2.1.118) — today
- **CrewAI** [`1.14.3a3`](https://github.com/crewAIInc/crewAI/releases/tag/1.14.3a3) — today *(pre-release)*
- **LangGraph** [`cli==0.4.24`](https://github.com/langchain-ai/langgraph/releases/tag/cli==0.4.24) — today
- **Google ADK** [`v2.0.0b1`](https://github.com/google/adk-python/releases/tag/v2.0.0b1) — today *(pre-release)*
- **DSPy** [`3.2.0`](https://github.com/stanfordnlp/dspy/releases/tag/3.2.0) — 1 day ago
- **LlamaIndex** [`v0.14.21`](https://github.com/run-llama/llama_index/releases/tag/v0.14.21) — 2 days ago
- **Haystack** [`v2.28.0`](https://github.com/deepset-ai/haystack/releases/tag/v2.28.0) — 2 days ago
- **Composio** [`@composio/cli@0.2.25-beta.215`](https://github.com/ComposioHQ/composio/releases/tag/@composio/cli@0.2.25-beta.215) — 5 days ago *(pre-release)*

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

*Powered by GitHub Actions • Data refreshed daily • Last run: 2026-04-23 08:04 UTC*