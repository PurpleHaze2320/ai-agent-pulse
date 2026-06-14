# 🔬 AI Agent Framework Pulse Tracker

[![Daily Update](https://github.com/PurpleHaze2320/ai-agent-pulse/actions/workflows/track.yml/badge.svg)](https://github.com/PurpleHaze2320/ai-agent-pulse/actions/workflows/track.yml)
[![Frameworks Tracked](https://img.shields.io/badge/frameworks-19-blue)](https://github.com/PurpleHaze2320/ai-agent-pulse)
[![License: MIT](https://img.shields.io/badge/License-MIT-green.svg)](https://opensource.org/licenses/MIT)
[![GitHub stars](https://img.shields.io/github/stars/PurpleHaze2320/ai-agent-pulse?style=social)](https://github.com/PurpleHaze2320/ai-agent-pulse/stargazers)

> Automated daily tracking of the AI agent framework ecosystem's health, momentum, and trends.
> Last updated: **2026-06-14 09:44 UTC** | Tracking **19** frameworks

## How It Works

This bot runs daily via GitHub Actions and collects metrics from the GitHub API for the most important
AI agent frameworks. It computes a **Pulse Score** (0-100) based on six weighted signals: star velocity,
release freshness, issue health, commit activity, community size, and fork engagement. The result is
a living dashboard that shows which frameworks are gaining momentum and which are losing steam.

## 🏆 Pulse Leaderboard

| Rank | Framework | Pulse | Stars | ⭐ 7d | Commits (4w) | Last Release | Category |
|------|-----------|-------|-------|-------|--------------|--------------|----------|
| 1 | [CrewAI](https://github.com/crewAIInc/crewAI) | 🟢 **89.5** | 53.5k | 🚀 +561 | 93 | 2 days ago | `multi-agent` |
| 2 | [LangGraph](https://github.com/langchain-ai/langgraph) | 🟢 **81.6** | 34.7k | 🚀 +627 | 66 | 1 day ago | `orchestration` |
| 3 | [Mastra](https://github.com/mastra-ai/mastra) | 🟢 **78.4** | 25.0k | 🚀 +204 | 710 | 1 day ago | `typescript` |
| 4 | [Agno](https://github.com/agno-agi/agno) | 🟢 **71.3** | 40.7k | 🚀 +119 | 93 | 1 day ago | `multi-agent` |
| 5 | [Claude Agent SDK](https://github.com/anthropics/claude-code) | 🟢 **70.5** | 132.3k | 🚀 +1531 | 25 | 1 day ago | `orchestration` |
| 6 | [Haystack](https://github.com/deepset-ai/haystack) | 🟢 **70.4** | 25.6k | 📈 +90 | 105 | 4 days ago | `pipeline` |
| 7 | [Google ADK](https://github.com/google/adk-python) | 🟢 **70.1** | 20.1k | 📈 +94 | 180 | 4 days ago | `orchestration` |
| 8 | [BrowserUse](https://github.com/browser-use/browser-use) | 🟢 **70.1** | 98.7k | 🚀 +1190 | 0 | 1 day ago | `web-agent` |
| 9 | [PydanticAI](https://github.com/pydantic/pydantic-ai) | 🟡 **68.5** | 17.7k | 🚀 +169 | 67 | 3 days ago | `structured` |
| 10 | [LlamaIndex](https://github.com/run-llama/llama_index) | 🟡 **60.6** | 50.1k | 🚀 +152 | 23 | 1 mo ago | `data-agent` |
| 11 | [OpenAI Agents SDK](https://github.com/openai/openai-agents-python) | 🟡 **59.7** | 27.1k | 🚀 +172 | 23 | 3 days ago | `orchestration` |
| 12 | [DSPy](https://github.com/stanfordnlp/dspy) | 🟡 **56.2** | 35.0k | 🚀 +123 | 36 | 17 days ago | `optimization` |
| 13 | [Semantic Kernel](https://github.com/microsoft/semantic-kernel) | 🟡 **51.9** | 28.1k | 📈 +49 | 5 | 10 days ago | `enterprise` |
| 14 | [Composio](https://github.com/ComposioHQ/composio) | 🟡 **51.1** | 28.8k | 📈 +90 | 24 | 5 days ago | `tooling` |
| 15 | [AG2](https://github.com/ag2ai/ag2) | 🟡 **49.1** | 4.7k | 📈 +33 | 0 | 1 day ago | `multi-agent` |
| 16 | [Letta](https://github.com/letta-ai/letta) | 🟡 **46.6** | 23.3k | 🚀 +133 | 0 | 1 mo ago | `memory` |
| 17 | [Smolagents](https://github.com/huggingface/smolagents) | 🟡 **43.5** | 27.8k | 🚀 +109 | 4 | 16 days ago | `lightweight` |
| 18 | [AutoGen](https://github.com/microsoft/autogen) | 🟡 **40.5** | 58.9k | 🚀 +199 | 0 | 8 mo ago | `multi-agent` |
| 19 | [Swarm](https://github.com/openai/swarm) | 🔴 **9.7** | 21.6k | 📈 +43 | 0 | — | `experimental` |

## 📂 By Category

- `data-agent`: **LlamaIndex** (60.6)
- `enterprise`: **Semantic Kernel** (51.9)
- `experimental`: **Swarm** (9.7)
- `lightweight`: **Smolagents** (43.5)
- `memory`: **Letta** (46.6)
- `multi-agent`: **CrewAI** (89.5), **Agno** (71.3), **AG2** (49.1), **AutoGen** (40.5)
- `optimization`: **DSPy** (56.2)
- `orchestration`: **LangGraph** (81.6), **Claude Agent SDK** (70.5), **Google ADK** (70.1), **OpenAI Agents SDK** (59.7)
- `pipeline`: **Haystack** (70.4)
- `structured`: **PydanticAI** (68.5)
- `tooling`: **Composio** (51.1)
- `typescript`: **Mastra** (78.4)
- `web-agent`: **BrowserUse** (70.1)

## 🔍 Top 5 — Score Breakdown

| Framework | Star Velocity | Release Freshness | Issue Health | Commit Activity | Community | Fork Ratio |
|-----------|:---:|:---:|:---:|:---:|:---:|:---:|
| **CrewAI** | 100 | 99.3 | 96.9 | 93.0 | 59.4 | 56.0 |
| **LangGraph** | 100 | 99.7 | 75.3 | 66.0 | 55.0 | 67.1 |
| **Mastra** | 45.7 | 99.7 | 95.1 | 100 | 92.0 | 35.5 |
| **Agno** | 24.8 | 99.7 | 81.5 | 93.0 | 89.0 | 54.3 |
| **Claude Agent SDK** | 100 | 99.7 | 87.0 | 25.0 | 10.2 | 64.8 |

## 💡 Key Insights

- **Hottest framework**: CrewAI with a Pulse Score of 89.5
- **Fastest growing**: Claude Agent SDK gained +1531 stars this week
- **Most active development**: Mastra with 710 commits in the last 4 weeks
- **Stale releases**: Swarm haven't released in a while

## 📦 Recent Releases

- **Claude Agent SDK** [`v2.1.177`](https://github.com/anthropics/claude-code/releases/tag/v2.1.177) — 1 day ago
- **BrowserUse** [`0.13.2`](https://github.com/browser-use/browser-use/releases/tag/0.13.2) — 1 day ago
- **AG2** [`v0.13.4`](https://github.com/ag2ai/ag2/releases/tag/v0.13.4) — 1 day ago
- **LangGraph** [`1.2.5`](https://github.com/langchain-ai/langgraph/releases/tag/1.2.5) — 1 day ago
- **Agno** [`v2.6.14`](https://github.com/agno-agi/agno/releases/tag/v2.6.14) — 1 day ago
- **Mastra** [`@mastra/core@1.42.0`](https://github.com/mastra-ai/mastra/releases/tag/@mastra/core@1.42.0) — 1 day ago
- **CrewAI** [`1.14.7`](https://github.com/crewAIInc/crewAI/releases/tag/1.14.7) — 2 days ago
- **OpenAI Agents SDK** [`v0.17.5`](https://github.com/openai/openai-agents-python/releases/tag/v0.17.5) — 3 days ago
- **PydanticAI** [`v2.0.0b7`](https://github.com/pydantic/pydantic-ai/releases/tag/v2.0.0b7) — 3 days ago *(pre-release)*
- **Google ADK** [`v1.35.0`](https://github.com/google/adk-python/releases/tag/v1.35.0) — 4 days ago

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

*Powered by GitHub Actions • Data refreshed daily • Last run: 2026-06-14 09:44 UTC*