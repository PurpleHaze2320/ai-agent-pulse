# 🔬 AI Agent Framework Pulse Tracker

[![Daily Update](https://github.com/PurpleHaze2320/ai-agent-pulse/actions/workflows/track.yml/badge.svg)](https://github.com/PurpleHaze2320/ai-agent-pulse/actions/workflows/track.yml)
[![Frameworks Tracked](https://img.shields.io/badge/frameworks-19-blue)](https://github.com/PurpleHaze2320/ai-agent-pulse)
[![License: MIT](https://img.shields.io/badge/License-MIT-green.svg)](https://opensource.org/licenses/MIT)
[![GitHub stars](https://img.shields.io/github/stars/PurpleHaze2320/ai-agent-pulse?style=social)](https://github.com/PurpleHaze2320/ai-agent-pulse/stargazers)

> Automated daily tracking of the AI agent framework ecosystem's health, momentum, and trends.
> Last updated: **2026-10-20 11:13 UTC** | Tracking **19** frameworks

## How It Works

This bot runs daily via GitHub Actions and collects metrics from the GitHub API for the most important
AI agent frameworks. It computes a **Pulse Score** (0-100) based on six weighted signals: star velocity,
release freshness, issue health, commit activity, community size, and fork engagement. The result is
a living dashboard that shows which frameworks are gaining momentum and which are losing steam.

## 🏆 Pulse Leaderboard

| Rank | Framework | Pulse | Stars | ⭐ 7d | Commits (4w) | Last Release | Category |
|------|-----------|-------|-------|-------|--------------|--------------|----------|
| 1 | [BrowserUse](https://github.com/browser-use/browser-use) | 🟢 **89.8** | 118.6k | 🚀 +766 | 142 | 4 days ago | `web-agent` |
| 2 | [CrewAI](https://github.com/crewAIInc/crewAI) | 🟢 **78.3** | 59.9k | 🚀 +263 | 96 | 6 days ago | `multi-agent` |
| 3 | [OpenAI Agents SDK](https://github.com/openai/openai-agents-python) | 🟢 **77.1** | 30.2k | 🚀 +158 | 136 | 5 days ago | `orchestration` |
| 4 | [Mastra](https://github.com/mastra-ai/mastra) | 🟢 **76.2** | 28.9k | 🚀 +168 | 1959 | 4 days ago | `typescript` |
| 5 | [Google ADK](https://github.com/google/adk-python) | 🟢 **76.1** | 21.9k | 🚀 +125 | 460 | 6 days ago | `orchestration` |
| 6 | [Claude Agent SDK](https://github.com/anthropics/claude-code) | 🟢 **75.9** | 152.9k | 🚀 +2299 | 49 | today | `orchestration` |
| 7 | [PydanticAI](https://github.com/pydantic/pydantic-ai) | 🟢 **74.5** | 20.8k | 🚀 +158 | 807 | today | `structured` |
| 8 | [Agno](https://github.com/agno-agi/agno) | 🟢 **71.8** | 42.8k | 🚀 +126 | 111 | today | `multi-agent` |
| 9 | [Haystack](https://github.com/deepset-ai/haystack) | 🟢 **70.9** | 26.8k | 📈 +52 | 234 | 5 days ago | `pipeline` |
| 10 | [AG2](https://github.com/ag2ai/ag2) | 🟡 **69.2** | 5.0k | ↗️ +12 | 118 | 9 days ago | `multi-agent` |
| 11 | [Composio](https://github.com/ComposioHQ/composio) | 🟡 **68.2** | 30.6k | 🚀 +123 | 254 | today | `tooling` |
| 12 | [LangGraph](https://github.com/langchain-ai/langgraph) | 🟡 **63.3** | 43.6k | 🚀 +374 | 0 | today | `orchestration` |
| 13 | [DSPy](https://github.com/stanfordnlp/dspy) | 🟡 **58.8** | 38.7k | 📈 +93 | 52 | 7 days ago | `optimization` |
| 14 | [LlamaIndex](https://github.com/run-llama/llama_index) | 🟡 **56.3** | 52.6k | 🚀 +103 | 15 | 28 days ago | `data-agent` |
| 15 | [Semantic Kernel](https://github.com/microsoft/semantic-kernel) | 🟡 **54.1** | 28.7k | ↗️ +17 | 23 | 13 days ago | `enterprise` |
| 16 | [Letta](https://github.com/letta-ai/letta) | 🟠 **35.9** | 25.2k | 📈 +80 | 1 | 5 mo ago | `memory` |
| 17 | [Smolagents](https://github.com/huggingface/smolagents) | 🟠 **34.3** | 29.9k | 🚀 +126 | 3 | 4 mo ago | `lightweight` |
| 18 | [AutoGen](https://github.com/microsoft/autogen) | 🟠 **32.6** | 61.5k | 🚀 +104 | 1 | 1y ago | `multi-agent` |
| 19 | [Swarm](https://github.com/openai/swarm) | 🔴 **9.1** | 22.1k | ↗️ +9 | 0 | — | `experimental` |

## 📂 By Category

- `data-agent`: **LlamaIndex** (56.3)
- `enterprise`: **Semantic Kernel** (54.1)
- `experimental`: **Swarm** (9.1)
- `lightweight`: **Smolagents** (34.3)
- `memory`: **Letta** (35.9)
- `multi-agent`: **CrewAI** (78.3), **Agno** (71.8), **AG2** (69.2), **AutoGen** (32.6)
- `optimization`: **DSPy** (58.8)
- `orchestration`: **OpenAI Agents SDK** (77.1), **Google ADK** (76.1), **Claude Agent SDK** (75.9), **LangGraph** (63.3)
- `pipeline`: **Haystack** (70.9)
- `structured`: **PydanticAI** (74.5)
- `tooling`: **Composio** (68.2)
- `typescript`: **Mastra** (76.2)
- `web-agent`: **BrowserUse** (89.8)

## 🔍 Top 5 — Score Breakdown

| Framework | Star Velocity | Release Freshness | Issue Health | Commit Activity | Community | Fork Ratio |
|-----------|:---:|:---:|:---:|:---:|:---:|:---:|
| **BrowserUse** | 100 | 98.7 | 89.5 | 100 | 72.0 | 44.4 |
| **CrewAI** | 53.3 | 98.0 | 88.2 | 96.0 | 70.4 | 58.8 |
| **OpenAI Agents SDK** | 31.1 | 98.3 | 99.3 | 100 | 80.4 | 67.4 |
| **Mastra** | 34.6 | 98.7 | 95.6 | 100 | 93.4 | 41.7 |
| **Google ADK** | 22.6 | 98.0 | 95.0 | 100 | 85.6 | 80.5 |

## 💡 Key Insights

- **Hottest framework**: BrowserUse with a Pulse Score of 89.8
- **Fastest growing**: Claude Agent SDK gained +2299 stars this week
- **Most active development**: Mastra with 1959 commits in the last 4 weeks
- **Stale releases**: AutoGen, Swarm haven't released in a while

## 📦 Recent Releases

- **PydanticAI** [`v2.58.0`](https://github.com/pydantic/pydantic-ai/releases/tag/v2.58.0) — today
- **Composio** [`@composio/cli@0.4.6-beta.458`](https://github.com/ComposioHQ/composio/releases/tag/@composio/cli@0.4.6-beta.458) — today *(pre-release)*
- **Claude Agent SDK** [`v2.1.304`](https://github.com/anthropics/claude-code/releases/tag/v2.1.304) — today
- **LangGraph** [`cli==0.4.37`](https://github.com/langchain-ai/langgraph/releases/tag/cli==0.4.37) — today
- **Agno** [`v3.1.6`](https://github.com/agno-agi/agno/releases/tag/v3.1.6) — today
- **Mastra** [`@mastra/core@1.78.0`](https://github.com/mastra-ai/mastra/releases/tag/@mastra/core@1.78.0) — 4 days ago
- **BrowserUse** [`0.13.13`](https://github.com/browser-use/browser-use/releases/tag/0.13.13) — 4 days ago
- **Haystack** [`v3.4.0`](https://github.com/deepset-ai/haystack/releases/tag/v3.4.0) — 5 days ago
- **OpenAI Agents SDK** [`v0.24.0`](https://github.com/openai/openai-agents-python/releases/tag/v0.24.0) — 5 days ago
- **CrewAI** [`1.15.28`](https://github.com/crewAIInc/crewAI/releases/tag/1.15.28) — 6 days ago

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

*Powered by GitHub Actions • Data refreshed daily • Last run: 2026-10-20 11:13 UTC*