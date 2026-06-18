# 🔬 AI Agent Framework Pulse Tracker

[![Daily Update](https://github.com/PurpleHaze2320/ai-agent-pulse/actions/workflows/track.yml/badge.svg)](https://github.com/PurpleHaze2320/ai-agent-pulse/actions/workflows/track.yml)
[![Frameworks Tracked](https://img.shields.io/badge/frameworks-19-blue)](https://github.com/PurpleHaze2320/ai-agent-pulse)
[![License: MIT](https://img.shields.io/badge/License-MIT-green.svg)](https://opensource.org/licenses/MIT)
[![GitHub stars](https://img.shields.io/github/stars/PurpleHaze2320/ai-agent-pulse?style=social)](https://github.com/PurpleHaze2320/ai-agent-pulse/stargazers)

> Automated daily tracking of the AI agent framework ecosystem's health, momentum, and trends.
> Last updated: **2026-06-18 10:38 UTC** | Tracking **19** frameworks

## How It Works

This bot runs daily via GitHub Actions and collects metrics from the GitHub API for the most important
AI agent frameworks. It computes a **Pulse Score** (0-100) based on six weighted signals: star velocity,
release freshness, issue health, commit activity, community size, and fork engagement. The result is
a living dashboard that shows which frameworks are gaining momentum and which are losing steam.

## 🏆 Pulse Leaderboard

| Rank | Framework | Pulse | Stars | ⭐ 7d | Commits (4w) | Last Release | Category |
|------|-----------|-------|-------|-------|--------------|--------------|----------|
| 1 | [CrewAI](https://github.com/crewAIInc/crewAI) | 🟢 **91.1** | 53.9k | 🚀 +618 | 114 | today | `multi-agent` |
| 2 | [BrowserUse](https://github.com/browser-use/browser-use) | 🟢 **89.8** | 99.4k | 🚀 +1169 | 408 | 5 days ago | `web-agent` |
| 3 | [LangGraph](https://github.com/langchain-ai/langgraph) | 🟢 **82.5** | 35.1k | 🚀 +681 | 71 | 1 day ago | `orchestration` |
| 4 | [Mastra](https://github.com/mastra-ai/mastra) | 🟢 **79.3** | 25.2k | 🚀 +237 | 817 | 5 days ago | `typescript` |
| 5 | [Agno](https://github.com/agno-agi/agno) | 🟢 **72.7** | 40.8k | 🚀 +119 | 104 | today | `multi-agent` |
| 6 | [Claude Agent SDK](https://github.com/anthropics/claude-code) | 🟢 **71.6** | 133.2k | 🚀 +1437 | 30 | today | `orchestration` |
| 7 | [Google ADK](https://github.com/google/adk-python) | 🟢 **71.1** | 20.2k | 📈 +92 | 269 | today | `orchestration` |
| 8 | [PydanticAI](https://github.com/pydantic/pydantic-ai) | 🟡 **68.9** | 17.8k | 🚀 +130 | 77 | 7 days ago | `structured` |
| 9 | [AG2](https://github.com/ag2ai/ag2) | 🟡 **62.1** | 4.7k | 📈 +26 | 68 | 5 days ago | `multi-agent` |
| 10 | [LlamaIndex](https://github.com/run-llama/llama_index) | 🟡 **59.8** | 50.2k | 🚀 +129 | 24 | 1 mo ago | `data-agent` |
| 11 | [OpenAI Agents SDK](https://github.com/openai/openai-agents-python) | 🟡 **59.7** | 27.2k | 🚀 +158 | 28 | 7 days ago | `orchestration` |
| 12 | [Semantic Kernel](https://github.com/microsoft/semantic-kernel) | 🟡 **57.2** | 28.2k | 📈 +50 | 28 | 1 day ago | `enterprise` |
| 13 | [DSPy](https://github.com/stanfordnlp/dspy) | 🟡 **56.7** | 35.1k | 🚀 +130 | 38 | 21 days ago | `optimization` |
| 14 | [Composio](https://github.com/ComposioHQ/composio) | 🟡 **55.9** | 28.8k | 🚀 +107 | 44 | 1 day ago | `tooling` |
| 15 | [Haystack](https://github.com/deepset-ai/haystack) | 🟡 **50.0** | 25.6k | 📈 +66 | 0 | today | `pipeline` |
| 16 | [Letta](https://github.com/letta-ai/letta) | 🟡 **46.2** | 23.4k | 🚀 +132 | 0 | 1 mo ago | `memory` |
| 17 | [Smolagents](https://github.com/huggingface/smolagents) | 🟡 **43.4** | 27.9k | 🚀 +106 | 5 | 20 days ago | `lightweight` |
| 18 | [AutoGen](https://github.com/microsoft/autogen) | 🟠 **39.6** | 59.1k | 🚀 +184 | 0 | 8 mo ago | `multi-agent` |
| 19 | [Swarm](https://github.com/openai/swarm) | 🔴 **9.2** | 21.6k | 📈 +32 | 0 | — | `experimental` |

## 📂 By Category

- `data-agent`: **LlamaIndex** (59.8)
- `enterprise`: **Semantic Kernel** (57.2)
- `experimental`: **Swarm** (9.2)
- `lightweight`: **Smolagents** (43.4)
- `memory`: **Letta** (46.2)
- `multi-agent`: **CrewAI** (91.1), **Agno** (72.7), **AG2** (62.1), **AutoGen** (39.6)
- `optimization`: **DSPy** (56.7)
- `orchestration`: **LangGraph** (82.5), **Claude Agent SDK** (71.6), **Google ADK** (71.1), **OpenAI Agents SDK** (59.7)
- `pipeline`: **Haystack** (50.0)
- `structured`: **PydanticAI** (68.9)
- `tooling`: **Composio** (55.9)
- `typescript`: **Mastra** (79.3)
- `web-agent`: **BrowserUse** (89.8)

## 🔍 Top 5 — Score Breakdown

| Framework | Star Velocity | Release Freshness | Issue Health | Commit Activity | Community | Fork Ratio |
|-----------|:---:|:---:|:---:|:---:|:---:|:---:|
| **CrewAI** | 100 | 100.0 | 96.9 | 100 | 59.4 | 56.0 |
| **BrowserUse** | 100 | 98.3 | 95.5 | 100 | 63.0 | 44.6 |
| **LangGraph** | 100 | 99.7 | 74.7 | 71.0 | 55.0 | 67.0 |
| **Mastra** | 50.7 | 98.3 | 94.9 | 100 | 91.8 | 35.8 |
| **Agno** | 24.8 | 100.0 | 80.9 | 100 | 89.0 | 54.3 |

## 💡 Key Insights

- **Hottest framework**: CrewAI with a Pulse Score of 91.1
- **Fastest growing**: Claude Agent SDK gained +1437 stars this week
- **Most active development**: Mastra with 817 commits in the last 4 weeks
- **Stale releases**: Swarm haven't released in a while

## 📦 Recent Releases

- **Haystack** [`v2.30.2`](https://github.com/deepset-ai/haystack/releases/tag/v2.30.2) — today
- **CrewAI** [`1.14.8a`](https://github.com/crewAIInc/crewAI/releases/tag/1.14.8a) — today *(pre-release)*
- **Google ADK** [`v1.35.2`](https://github.com/google/adk-python/releases/tag/v1.35.2) — today
- **Claude Agent SDK** [`v2.1.181`](https://github.com/anthropics/claude-code/releases/tag/v2.1.181) — today
- **Agno** [`v2.6.17`](https://github.com/agno-agi/agno/releases/tag/v2.6.17) — today
- **Semantic Kernel** [`python-1.43.1`](https://github.com/microsoft/semantic-kernel/releases/tag/python-1.43.1) — 1 day ago
- **LangGraph** [`cli==0.4.30`](https://github.com/langchain-ai/langgraph/releases/tag/cli==0.4.30) — 1 day ago
- **Composio** [`@composio/cli@0.2.32-beta.265`](https://github.com/ComposioHQ/composio/releases/tag/@composio/cli@0.2.32-beta.265) — 1 day ago *(pre-release)*
- **BrowserUse** [`0.13.2`](https://github.com/browser-use/browser-use/releases/tag/0.13.2) — 5 days ago
- **AG2** [`v0.13.4`](https://github.com/ag2ai/ag2/releases/tag/v0.13.4) — 5 days ago

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

*Powered by GitHub Actions • Data refreshed daily • Last run: 2026-06-18 10:38 UTC*