# 🔬 AI Agent Framework Pulse Tracker

[![Daily Update](https://github.com/PurpleHaze2320/ai-agent-pulse/actions/workflows/track.yml/badge.svg)](https://github.com/PurpleHaze2320/ai-agent-pulse/actions/workflows/track.yml)
[![Frameworks Tracked](https://img.shields.io/badge/frameworks-19-blue)](https://github.com/PurpleHaze2320/ai-agent-pulse)
[![License: MIT](https://img.shields.io/badge/License-MIT-green.svg)](https://opensource.org/licenses/MIT)
[![GitHub stars](https://img.shields.io/github/stars/PurpleHaze2320/ai-agent-pulse?style=social)](https://github.com/PurpleHaze2320/ai-agent-pulse/stargazers)

> Automated daily tracking of the AI agent framework ecosystem's health, momentum, and trends.
> Last updated: **2026-10-22 11:29 UTC** | Tracking **19** frameworks

## How It Works

This bot runs daily via GitHub Actions and collects metrics from the GitHub API for the most important
AI agent frameworks. It computes a **Pulse Score** (0-100) based on six weighted signals: star velocity,
release freshness, issue health, commit activity, community size, and fork engagement. The result is
a living dashboard that shows which frameworks are gaining momentum and which are losing steam.

## 🏆 Pulse Leaderboard

| Rank | Framework | Pulse | Stars | ⭐ 7d | Commits (4w) | Last Release | Category |
|------|-----------|-------|-------|-------|--------------|--------------|----------|
| 1 | [BrowserUse](https://github.com/browser-use/browser-use) | 🟢 **89.7** | 118.8k | 🚀 +803 | 142 | 6 days ago | `web-agent` |
| 2 | [LangGraph](https://github.com/langchain-ai/langgraph) | 🟢 **84.5** | 43.7k | 🚀 +409 | 112 | 2 days ago | `orchestration` |
| 3 | [CrewAI](https://github.com/crewAIInc/crewAI) | 🟢 **78.5** | 60.0k | 🚀 +254 | 108 | 8 days ago | `multi-agent` |
| 4 | [OpenAI Agents SDK](https://github.com/openai/openai-agents-python) | 🟢 **77.2** | 30.2k | 🚀 +173 | 137 | 7 days ago | `orchestration` |
| 5 | [Claude Agent SDK](https://github.com/anthropics/claude-code) | 🟢 **76.7** | 152.8k | 🚀 +1863 | 54 | today | `orchestration` |
| 6 | [Mastra](https://github.com/mastra-ai/mastra) | 🟢 **76.6** | 29.0k | 🚀 +171 | 2163 | today | `typescript` |
| 7 | [Google ADK](https://github.com/google/adk-python) | 🟢 **74.8** | 22.0k | 📈 +100 | 512 | 8 days ago | `orchestration` |
| 8 | [Haystack](https://github.com/deepset-ai/haystack) | 🟢 **71.7** | 26.8k | 📈 +63 | 259 | today | `pipeline` |
| 9 | [Agno](https://github.com/agno-agi/agno) | 🟢 **71.5** | 42.9k | 🚀 +117 | 129 | today | `multi-agent` |
| 10 | [AG2](https://github.com/ag2ai/ag2) | 🟡 **69.9** | 5.0k | ↗️ +14 | 123 | today | `multi-agent` |
| 11 | [Composio](https://github.com/ComposioHQ/composio) | 🟡 **68.1** | 30.7k | 🚀 +119 | 312 | today | `tooling` |
| 12 | [LlamaIndex](https://github.com/run-llama/llama_index) | 🟡 **56.4** | 52.6k | 🚀 +110 | 15 | 1 mo ago | `data-agent` |
| 13 | [Semantic Kernel](https://github.com/microsoft/semantic-kernel) | 🟡 **54.5** | 28.7k | 📈 +25 | 24 | 15 days ago | `enterprise` |
| 14 | [PydanticAI](https://github.com/pydantic/pydantic-ai) | 🟡 **53.4** | 20.8k | 🚀 +158 | 0 | 16 days ago | `structured` |
| 15 | [DSPy](https://github.com/stanfordnlp/dspy) | 🟡 **48.0** | 38.7k | 📈 +85 | 0 | 9 days ago | `optimization` |
| 16 | [Letta](https://github.com/letta-ai/letta) | 🟠 **35.8** | 25.2k | 📈 +80 | 1 | 5 mo ago | `memory` |
| 17 | [Smolagents](https://github.com/huggingface/smolagents) | 🟠 **34.2** | 30.0k | 🚀 +127 | 3 | 4 mo ago | `lightweight` |
| 18 | [AutoGen](https://github.com/microsoft/autogen) | 🟠 **32.5** | 61.5k | 🚀 +103 | 1 | 1y ago | `multi-agent` |
| 19 | [Swarm](https://github.com/openai/swarm) | 🔴 **9.0** | 22.1k | ↗️ +11 | 0 | — | `experimental` |

## 📂 By Category

- `data-agent`: **LlamaIndex** (56.4)
- `enterprise`: **Semantic Kernel** (54.5)
- `experimental`: **Swarm** (9.0)
- `lightweight`: **Smolagents** (34.2)
- `memory`: **Letta** (35.8)
- `multi-agent`: **CrewAI** (78.5), **Agno** (71.5), **AG2** (69.9), **AutoGen** (32.5)
- `optimization`: **DSPy** (48.0)
- `orchestration`: **LangGraph** (84.5), **OpenAI Agents SDK** (77.2), **Claude Agent SDK** (76.7), **Google ADK** (74.8)
- `pipeline`: **Haystack** (71.7)
- `structured`: **PydanticAI** (53.4)
- `tooling`: **Composio** (68.1)
- `typescript`: **Mastra** (76.6)
- `web-agent`: **BrowserUse** (89.7)

## 🔍 Top 5 — Score Breakdown

| Framework | Star Velocity | Release Freshness | Issue Health | Commit Activity | Community | Fork Ratio |
|-----------|:---:|:---:|:---:|:---:|:---:|:---:|
| **BrowserUse** | 100 | 98.0 | 89.4 | 100 | 72.0 | 44.4 |
| **LangGraph** | 81.0 | 99.3 | 78.7 | 100 | 56.8 | 68.6 |
| **CrewAI** | 51.9 | 97.3 | 87.5 | 100 | 71.0 | 58.9 |
| **OpenAI Agents SDK** | 33.1 | 97.7 | 99.1 | 100 | 80.4 | 65.2 |
| **Claude Agent SDK** | 100 | 100.0 | 85.3 | 54.0 | 11.4 | 70.1 |

## 💡 Key Insights

- **Hottest framework**: BrowserUse with a Pulse Score of 89.7
- **Fastest growing**: Claude Agent SDK gained +1863 stars this week
- **Most active development**: Mastra with 2163 commits in the last 4 weeks
- **Stale releases**: AutoGen, Swarm haven't released in a while

## 📦 Recent Releases

- **Claude Agent SDK** [`v2.1.308`](https://github.com/anthropics/claude-code/releases/tag/v2.1.308) — today
- **Composio** [`versioning-example@0.1.10`](https://github.com/ComposioHQ/composio/releases/tag/versioning-example@0.1.10) — today
- **AG2** [`v1.2.1`](https://github.com/ag2ai/ag2/releases/tag/v1.2.1) — today
- **Haystack** [`v3.4.1`](https://github.com/deepset-ai/haystack/releases/tag/v3.4.1) — today
- **Mastra** [`@mastra/core@1.79.0`](https://github.com/mastra-ai/mastra/releases/tag/@mastra/core@1.79.0) — today
- **Agno** [`v3.1.8`](https://github.com/agno-agi/agno/releases/tag/v3.1.8) — today
- **LangGraph** [`cli==0.4.37`](https://github.com/langchain-ai/langgraph/releases/tag/cli==0.4.37) — 2 days ago
- **BrowserUse** [`0.13.13`](https://github.com/browser-use/browser-use/releases/tag/0.13.13) — 6 days ago
- **OpenAI Agents SDK** [`v0.24.0`](https://github.com/openai/openai-agents-python/releases/tag/v0.24.0) — 7 days ago
- **CrewAI** [`1.15.28`](https://github.com/crewAIInc/crewAI/releases/tag/1.15.28) — 8 days ago

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

*Powered by GitHub Actions • Data refreshed daily • Last run: 2026-10-22 11:29 UTC*