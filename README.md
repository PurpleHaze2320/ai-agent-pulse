# 🔬 AI Agent Framework Pulse Tracker

[![Daily Update](https://github.com/PurpleHaze2320/ai-agent-pulse/actions/workflows/track.yml/badge.svg)](https://github.com/PurpleHaze2320/ai-agent-pulse/actions/workflows/track.yml)
[![Frameworks Tracked](https://img.shields.io/badge/frameworks-19-blue)](https://github.com/PurpleHaze2320/ai-agent-pulse)
[![License: MIT](https://img.shields.io/badge/License-MIT-green.svg)](https://opensource.org/licenses/MIT)
[![GitHub stars](https://img.shields.io/github/stars/PurpleHaze2320/ai-agent-pulse?style=social)](https://github.com/PurpleHaze2320/ai-agent-pulse/stargazers)

> Automated daily tracking of the AI agent framework ecosystem's health, momentum, and trends.
> Last updated: **2026-08-14 07:39 UTC** | Tracking **19** frameworks

## How It Works

This bot runs daily via GitHub Actions and collects metrics from the GitHub API for the most important
AI agent frameworks. It computes a **Pulse Score** (0-100) based on six weighted signals: star velocity,
release freshness, issue health, commit activity, community size, and fork engagement. The result is
a living dashboard that shows which frameworks are gaining momentum and which are losing steam.

## 🏆 Pulse Leaderboard

| Rank | Framework | Pulse | Stars | ⭐ 7d | Commits (4w) | Last Release | Category |
|------|-----------|-------|-------|-------|--------------|--------------|----------|
| 1 | [BrowserUse](https://github.com/browser-use/browser-use) | 🟢 **89.0** | 109.2k | 🚀 +1025 | 161 | 17 days ago | `web-agent` |
| 2 | [CrewAI](https://github.com/crewAIInc/crewAI) | 🟢 **81.8** | 57.1k | 🚀 +342 | 91 | today | `multi-agent` |
| 3 | [Mastra](https://github.com/mastra-ai/mastra) | 🟢 **77.5** | 27.2k | 🚀 +180 | 1470 | 1 day ago | `typescript` |
| 4 | [LangGraph](https://github.com/langchain-ai/langgraph) | 🟢 **75.6** | 39.7k | 🚀 +570 | 40 | 2 days ago | `orchestration` |
| 5 | [Haystack](https://github.com/deepset-ai/haystack) | 🟡 **69.7** | 26.2k | 📈 +74 | 204 | 24 days ago | `pipeline` |
| 6 | [Claude Agent SDK](https://github.com/anthropics/claude-code) | 🟡 **68.5** | 141.4k | 🚀 +869 | 19 | today | `orchestration` |
| 7 | [Composio](https://github.com/ComposioHQ/composio) | 🟡 **68.0** | 29.7k | 🚀 +110 | 312 | today | `tooling` |
| 8 | [Agno](https://github.com/agno-agi/agno) | 🟡 **65.9** | 41.7k | 📈 +89 | 74 | today | `multi-agent` |
| 9 | [DSPy](https://github.com/stanfordnlp/dspy) | 🟡 **64.9** | 37.2k | 🚀 +512 | 0 | 10 days ago | `optimization` |
| 10 | [LlamaIndex](https://github.com/run-llama/llama_index) | 🟡 **62.6** | 51.6k | 🚀 +197 | 29 | 1 mo ago | `data-agent` |
| 11 | [OpenAI Agents SDK](https://github.com/openai/openai-agents-python) | 🟡 **56.4** | 28.6k | 🚀 +172 | 0 | 3 days ago | `orchestration` |
| 12 | [PydanticAI](https://github.com/pydantic/pydantic-ai) | 🟡 **55.9** | 19.3k | 🚀 +170 | 0 | today | `structured` |
| 13 | [Semantic Kernel](https://github.com/microsoft/semantic-kernel) | 🟡 **54.1** | 28.4k | ↗️ +19 | 20 | 7 days ago | `enterprise` |
| 14 | [Google ADK](https://github.com/google/adk-python) | 🟡 **53.5** | 21.1k | 📈 +74 | 0 | today | `orchestration` |
| 15 | [AG2](https://github.com/ag2ai/ag2) | 🟡 **49.2** | 4.9k | ↗️ +20 | 0 | 16 days ago | `multi-agent` |
| 16 | [Letta](https://github.com/letta-ai/letta) | 🟡 **41.5** | 24.2k | 📈 +100 | 3 | 3 mo ago | `memory` |
| 17 | [Smolagents](https://github.com/huggingface/smolagents) | 🟠 **37.5** | 28.8k | 📈 +92 | 0 | 2 mo ago | `lightweight` |
| 18 | [AutoGen](https://github.com/microsoft/autogen) | 🟠 **34.3** | 60.4k | 🚀 +132 | 0 | 10 mo ago | `multi-agent` |
| 19 | [Swarm](https://github.com/openai/swarm) | 🔴 **9.6** | 21.9k | ↗️ +18 | 0 | — | `experimental` |

## 📂 By Category

- `data-agent`: **LlamaIndex** (62.6)
- `enterprise`: **Semantic Kernel** (54.1)
- `experimental`: **Swarm** (9.6)
- `lightweight`: **Smolagents** (37.5)
- `memory`: **Letta** (41.5)
- `multi-agent`: **CrewAI** (81.8), **Agno** (65.9), **AG2** (49.2), **AutoGen** (34.3)
- `optimization`: **DSPy** (64.9)
- `orchestration`: **LangGraph** (75.6), **Claude Agent SDK** (68.5), **OpenAI Agents SDK** (56.4), **Google ADK** (53.5)
- `pipeline`: **Haystack** (69.7)
- `structured`: **PydanticAI** (55.9)
- `tooling`: **Composio** (68.0)
- `typescript`: **Mastra** (77.5)
- `web-agent`: **BrowserUse** (89.0)

## 🔍 Top 5 — Score Breakdown

| Framework | Star Velocity | Release Freshness | Issue Health | Commit Activity | Community | Fork Ratio |
|-----------|:---:|:---:|:---:|:---:|:---:|:---:|
| **BrowserUse** | 100 | 94.3 | 93.9 | 100 | 66.8 | 44.0 |
| **CrewAI** | 70.6 | 100.0 | 94.9 | 91.0 | 60.0 | 57.1 |
| **Mastra** | 40.3 | 99.7 | 95.6 | 100 | 92.8 | 38.7 |
| **LangGraph** | 100 | 99.3 | 70.1 | 40.0 | 55.4 | 67.1 |
| **Haystack** | 14.9 | 92.0 | 98.4 | 100 | 82.0 | 45.9 |

## 💡 Key Insights

- **Hottest framework**: BrowserUse with a Pulse Score of 89.0
- **Fastest growing**: BrowserUse gained +1025 stars this week
- **Most active development**: Mastra with 1470 commits in the last 4 weeks
- **Stale releases**: AutoGen, Swarm haven't released in a while

## 📦 Recent Releases

- **PydanticAI** [`v2.30.0`](https://github.com/pydantic/pydantic-ai/releases/tag/v2.30.0) — today
- **CrewAI** [`1.15.16`](https://github.com/crewAIInc/crewAI/releases/tag/1.15.16) — today
- **Claude Agent SDK** [`v2.1.232`](https://github.com/anthropics/claude-code/releases/tag/v2.1.232) — today
- **Google ADK** [`v2.7.0`](https://github.com/google/adk-python/releases/tag/v2.7.0) — today
- **Composio** [`@composio/cli@0.3.4-beta.351`](https://github.com/ComposioHQ/composio/releases/tag/@composio/cli@0.3.4-beta.351) — today *(pre-release)*
- **Agno** [`v2.9.0`](https://github.com/agno-agi/agno/releases/tag/v2.9.0) — today
- **Mastra** [`@mastra/core@1.58.0`](https://github.com/mastra-ai/mastra/releases/tag/@mastra/core@1.58.0) — 1 day ago
- **LangGraph** [`1.2.11`](https://github.com/langchain-ai/langgraph/releases/tag/1.2.11) — 2 days ago
- **OpenAI Agents SDK** [`v0.20.0`](https://github.com/openai/openai-agents-python/releases/tag/v0.20.0) — 3 days ago
- **Semantic Kernel** [`python-1.44.1`](https://github.com/microsoft/semantic-kernel/releases/tag/python-1.44.1) — 7 days ago

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

*Powered by GitHub Actions • Data refreshed daily • Last run: 2026-08-14 07:39 UTC*