# 🔬 AI Agent Framework Pulse Tracker

[![Daily Update](https://github.com/PurpleHaze2320/ai-agent-pulse/actions/workflows/track.yml/badge.svg)](https://github.com/PurpleHaze2320/ai-agent-pulse/actions/workflows/track.yml)
[![Frameworks Tracked](https://img.shields.io/badge/frameworks-19-blue)](https://github.com/PurpleHaze2320/ai-agent-pulse)
[![License: MIT](https://img.shields.io/badge/License-MIT-green.svg)](https://opensource.org/licenses/MIT)
[![GitHub stars](https://img.shields.io/github/stars/PurpleHaze2320/ai-agent-pulse?style=social)](https://github.com/PurpleHaze2320/ai-agent-pulse/stargazers)

> Automated daily tracking of the AI agent framework ecosystem's health, momentum, and trends.
> Last updated: **2026-10-15 11:09 UTC** | Tracking **19** frameworks

## How It Works

This bot runs daily via GitHub Actions and collects metrics from the GitHub API for the most important
AI agent frameworks. It computes a **Pulse Score** (0-100) based on six weighted signals: star velocity,
release freshness, issue health, commit activity, community size, and fork engagement. The result is
a living dashboard that shows which frameworks are gaining momentum and which are losing steam.

## 🏆 Pulse Leaderboard

| Rank | Framework | Pulse | Stars | ⭐ 7d | Commits (4w) | Last Release | Category |
|------|-----------|-------|-------|-------|--------------|--------------|----------|
| 1 | [LangGraph](https://github.com/langchain-ai/langgraph) | 🟢 **81.0** | 43.3k | 🚀 +413 | 91 | today | `orchestration` |
| 2 | [BrowserUse](https://github.com/browser-use/browser-use) | 🟢 **79.7** | 118.0k | 🚀 +568 | 51 | 8 days ago | `web-agent` |
| 3 | [Claude Agent SDK](https://github.com/anthropics/claude-code) | 🟢 **78.6** | 151.0k | 🚀 +1124 | 63 | today | `orchestration` |
| 4 | [Mastra](https://github.com/mastra-ai/mastra) | 🟢 **77.4** | 28.8k | 🚀 +192 | 2043 | 1 day ago | `typescript` |
| 5 | [OpenAI Agents SDK](https://github.com/openai/openai-agents-python) | 🟢 **76.8** | 30.1k | 🚀 +144 | 223 | today | `orchestration` |
| 6 | [CrewAI](https://github.com/crewAIInc/crewAI) | 🟢 **76.2** | 59.7k | 🚀 +273 | 82 | 1 day ago | `multi-agent` |
| 7 | [Agno](https://github.com/agno-agi/agno) | 🟢 **71.9** | 42.7k | 🚀 +132 | 109 | 2 days ago | `multi-agent` |
| 8 | [Haystack](https://github.com/deepset-ai/haystack) | 🟢 **71.2** | 26.7k | 📈 +50 | 270 | today | `pipeline` |
| 9 | [AG2](https://github.com/ag2ai/ag2) | 🟡 **69.6** | 5.0k | ↗️ +13 | 120 | 4 days ago | `multi-agent` |
| 10 | [Composio](https://github.com/ComposioHQ/composio) | 🟡 **67.2** | 30.6k | 📈 +92 | 232 | today | `tooling` |
| 11 | [DSPy](https://github.com/stanfordnlp/dspy) | 🟡 **58.8** | 38.6k | 📈 +87 | 50 | 2 days ago | `optimization` |
| 12 | [LlamaIndex](https://github.com/run-llama/llama_index) | 🟡 **56.9** | 52.5k | 📈 +69 | 22 | 23 days ago | `data-agent` |
| 13 | [Google ADK](https://github.com/google/adk-python) | 🟡 **55.6** | 21.9k | 🚀 +118 | 0 | 1 day ago | `orchestration` |
| 14 | [Semantic Kernel](https://github.com/microsoft/semantic-kernel) | 🟡 **54.4** | 28.7k | 📈 +28 | 21 | 8 days ago | `enterprise` |
| 15 | [PydanticAI](https://github.com/pydantic/pydantic-ai) | 🟡 **53.3** | 20.6k | 🚀 +141 | 0 | 9 days ago | `structured` |
| 16 | [Letta](https://github.com/letta-ai/letta) | 🟠 **35.9** | 25.1k | 📈 +73 | 0 | 5 mo ago | `memory` |
| 17 | [Smolagents](https://github.com/huggingface/smolagents) | 🟠 **34.9** | 29.9k | 🚀 +121 | 5 | 4 mo ago | `lightweight` |
| 18 | [AutoGen](https://github.com/microsoft/autogen) | 🟠 **33.0** | 61.4k | 🚀 +120 | 0 | 1y ago | `multi-agent` |
| 19 | [Swarm](https://github.com/openai/swarm) | 🔴 **9.3** | 22.1k | ↗️ +15 | 0 | — | `experimental` |

## 📂 By Category

- `data-agent`: **LlamaIndex** (56.9)
- `enterprise`: **Semantic Kernel** (54.4)
- `experimental`: **Swarm** (9.3)
- `lightweight`: **Smolagents** (34.9)
- `memory`: **Letta** (35.9)
- `multi-agent`: **CrewAI** (76.2), **Agno** (71.9), **AG2** (69.6), **AutoGen** (33.0)
- `optimization`: **DSPy** (58.8)
- `orchestration`: **LangGraph** (81.0), **Claude Agent SDK** (78.6), **OpenAI Agents SDK** (76.8), **Google ADK** (55.6)
- `pipeline`: **Haystack** (71.2)
- `structured`: **PydanticAI** (53.3)
- `tooling`: **Composio** (67.2)
- `typescript`: **Mastra** (77.4)
- `web-agent`: **BrowserUse** (79.7)

## 🔍 Top 5 — Score Breakdown

| Framework | Star Velocity | Release Freshness | Issue Health | Commit Activity | Community | Fork Ratio |
|-----------|:---:|:---:|:---:|:---:|:---:|:---:|
| **LangGraph** | 82.1 | 100.0 | 65.2 | 91.0 | 56.6 | 68.0 |
| **BrowserUse** | 100 | 97.3 | 89.6 | 51.0 | 72.0 | 44.4 |
| **Claude Agent SDK** | 100 | 100.0 | 85.7 | 63.0 | 11.4 | 70.4 |
| **Mastra** | 38.5 | 99.7 | 95.7 | 100 | 93.4 | 41.4 |
| **OpenAI Agents SDK** | 29.2 | 100.0 | 99.7 | 100 | 80.2 | 65.2 |

## 💡 Key Insights

- **Hottest framework**: LangGraph with a Pulse Score of 81.0
- **Fastest growing**: Claude Agent SDK gained +1124 stars this week
- **Most active development**: Mastra with 2043 commits in the last 4 weeks
- **Stale releases**: AutoGen, Swarm haven't released in a while

## 📦 Recent Releases

- **Composio** [`@composio/cli@0.4.4-beta.428`](https://github.com/ComposioHQ/composio/releases/tag/@composio/cli@0.4.4-beta.428) — today *(pre-release)*
- **Haystack** [`v3.4.0`](https://github.com/deepset-ai/haystack/releases/tag/v3.4.0) — today
- **LangGraph** [`prebuilt==1.1.1`](https://github.com/langchain-ai/langgraph/releases/tag/prebuilt==1.1.1) — today
- **OpenAI Agents SDK** [`v0.24.0`](https://github.com/openai/openai-agents-python/releases/tag/v0.24.0) — today
- **Claude Agent SDK** [`v2.1.300`](https://github.com/anthropics/claude-code/releases/tag/v2.1.300) — today
- **Mastra** [`@mastra/core@1.77.0`](https://github.com/mastra-ai/mastra/releases/tag/@mastra/core@1.77.0) — 1 day ago
- **CrewAI** [`1.15.28`](https://github.com/crewAIInc/crewAI/releases/tag/1.15.28) — 1 day ago
- **Google ADK** [`v2.12.0`](https://github.com/google/adk-python/releases/tag/v2.12.0) — 1 day ago
- **DSPy** [`3.4.1`](https://github.com/stanfordnlp/dspy/releases/tag/3.4.1) — 2 days ago
- **Agno** [`v3.1.3`](https://github.com/agno-agi/agno/releases/tag/v3.1.3) — 2 days ago

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

*Powered by GitHub Actions • Data refreshed daily • Last run: 2026-10-15 11:09 UTC*