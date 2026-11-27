# 🔬 AI Agent Framework Pulse Tracker

[![Daily Update](https://github.com/PurpleHaze2320/ai-agent-pulse/actions/workflows/track.yml/badge.svg)](https://github.com/PurpleHaze2320/ai-agent-pulse/actions/workflows/track.yml)
[![Frameworks Tracked](https://img.shields.io/badge/frameworks-19-blue)](https://github.com/PurpleHaze2320/ai-agent-pulse)
[![License: MIT](https://img.shields.io/badge/License-MIT-green.svg)](https://opensource.org/licenses/MIT)
[![GitHub stars](https://img.shields.io/github/stars/PurpleHaze2320/ai-agent-pulse?style=social)](https://github.com/PurpleHaze2320/ai-agent-pulse/stargazers)

> Automated daily tracking of the AI agent framework ecosystem's health, momentum, and trends.
> Last updated: **2026-11-27 16:25 UTC** | Tracking **19** frameworks

## How It Works

This bot runs daily via GitHub Actions and collects metrics from the GitHub API for the most important
AI agent frameworks. It computes a **Pulse Score** (0-100) based on six weighted signals: star velocity,
release freshness, issue health, commit activity, community size, and fork engagement. The result is
a living dashboard that shows which frameworks are gaining momentum and which are losing steam.

## 🏆 Pulse Leaderboard

| Rank | Framework | Pulse | Stars | ⭐ 7d | Commits (4w) | Last Release | Category |
|------|-----------|-------|-------|-------|--------------|--------------|----------|
| 1 | [BrowserUse](https://github.com/browser-use/browser-use) | 🟢 **90.1** | 122.2k | 🚀 +616 | 1229 | today | `web-agent` |
| 2 | [Claude Agent SDK](https://github.com/anthropics/claude-code) | 🟢 **85.2** | 157.3k | 🚀 +880 | 223 | 2 days ago | `orchestration` |
| 3 | [CrewAI](https://github.com/crewAIInc/crewAI) | 🟢 **77.7** | 61.3k | 🚀 +201 | 177 | 3 days ago | `multi-agent` |
| 4 | [LangGraph](https://github.com/langchain-ai/langgraph) | 🟢 **76.4** | 45.5k | 🚀 +314 | 77 | 1 day ago | `orchestration` |
| 5 | [Mastra](https://github.com/mastra-ai/mastra) | 🟢 **75.9** | 29.9k | 🚀 +166 | 2431 | 2 days ago | `typescript` |
| 6 | [Google ADK](https://github.com/google/adk-python) | 🟢 **74.6** | 22.4k | 📈 +89 | 272 | 2 days ago | `orchestration` |
| 7 | [OpenAI Agents SDK](https://github.com/openai/openai-agents-python) | 🟢 **72.9** | 30.9k | 🚀 +117 | 89 | 3 days ago | `orchestration` |
| 8 | [Haystack](https://github.com/deepset-ai/haystack) | 🟢 **70.8** | 27.1k | 📈 +58 | 279 | 17 days ago | `pipeline` |
| 9 | [AG2](https://github.com/ag2ai/ag2) | 🟢 **70.0** | 5.1k | ↗️ +16 | 107 | 4 days ago | `multi-agent` |
| 10 | [Agno](https://github.com/agno-agi/agno) | 🟡 **69.0** | 43.3k | 📈 +81 | 139 | 9 days ago | `multi-agent` |
| 11 | [Composio](https://github.com/ComposioHQ/composio) | 🟡 **68.7** | 31.3k | 🚀 +123 | 327 | today | `tooling` |
| 12 | [DSPy](https://github.com/stanfordnlp/dspy) | 🟡 **59.9** | 39.3k | 🚀 +107 | 59 | 16 days ago | `optimization` |
| 13 | [Semantic Kernel](https://github.com/microsoft/semantic-kernel) | 🟡 **58.0** | 28.8k | 📈 +21 | 39 | 20 days ago | `enterprise` |
| 14 | [LlamaIndex](https://github.com/run-llama/llama_index) | 🟡 **56.9** | 53.0k | 📈 +58 | 22 | 13 days ago | `data-agent` |
| 15 | [PydanticAI](https://github.com/pydantic/pydantic-ai) | 🟡 **49.0** | 21.4k | 🚀 +115 | 0 | 1 mo ago | `structured` |
| 16 | [Smolagents](https://github.com/huggingface/smolagents) | 🟠 **34.8** | 30.6k | 🚀 +108 | 23 | 6 mo ago | `lightweight` |
| 17 | [Letta](https://github.com/letta-ai/letta) | 🟠 **32.3** | 25.6k | 📈 +64 | 0 | 6 mo ago | `memory` |
| 18 | [AutoGen](https://github.com/microsoft/autogen) | 🟠 **29.4** | 62.0k | ↗️ +18 | 1 | 1y ago | `multi-agent` |
| 19 | [Swarm](https://github.com/openai/swarm) | 🔴 **9.8** | 22.2k | 📈 +28 | 0 | — | `experimental` |

## 📂 By Category

- `data-agent`: **LlamaIndex** (56.9)
- `enterprise`: **Semantic Kernel** (58.0)
- `experimental`: **Swarm** (9.8)
- `lightweight`: **Smolagents** (34.8)
- `memory`: **Letta** (32.3)
- `multi-agent`: **CrewAI** (77.7), **AG2** (70.0), **Agno** (69.0), **AutoGen** (29.4)
- `optimization`: **DSPy** (59.9)
- `orchestration`: **Claude Agent SDK** (85.2), **LangGraph** (76.4), **Google ADK** (74.6), **OpenAI Agents SDK** (72.9)
- `pipeline`: **Haystack** (70.8)
- `structured`: **PydanticAI** (49.0)
- `tooling`: **Composio** (68.7)
- `typescript`: **Mastra** (75.9)
- `web-agent`: **BrowserUse** (90.1)

## 🔍 Top 5 — Score Breakdown

| Framework | Star Velocity | Release Freshness | Issue Health | Commit Activity | Community | Fork Ratio |
|-----------|:---:|:---:|:---:|:---:|:---:|:---:|
| **BrowserUse** | 100 | 100.0 | 89.6 | 100 | 72.2 | 44.8 |
| **Claude Agent SDK** | 100 | 99.3 | 85.5 | 100 | 11.4 | 64.0 |
| **CrewAI** | 44.9 | 99.0 | 85.3 | 100 | 78.4 | 60.7 |
| **LangGraph** | 65.9 | 99.7 | 79.3 | 77.0 | 57.6 | 69.2 |
| **Mastra** | 33.9 | 99.3 | 93.2 | 100 | 93.2 | 42.2 |

## 💡 Key Insights

- **Hottest framework**: BrowserUse with a Pulse Score of 90.1
- **Fastest growing**: Claude Agent SDK gained +880 stars this week
- **Most active development**: Mastra with 2431 commits in the last 4 weeks
- **⚠️ Archived**: AutoGen
- **Stale releases**: AutoGen, Swarm haven't released in a while

## 📦 Recent Releases

- **Composio** [`@composio/cli@0.6.5-beta.590`](https://github.com/ComposioHQ/composio/releases/tag/@composio/cli@0.6.5-beta.590) — today *(pre-release)*
- **BrowserUse** [`1.0.9`](https://github.com/browser-use/browser-use/releases/tag/1.0.9) — today
- **LangGraph** [`cli==0.4.44`](https://github.com/langchain-ai/langgraph/releases/tag/cli==0.4.44) — 1 day ago
- **Mastra** [`@mastra/core@1.86.0`](https://github.com/mastra-ai/mastra/releases/tag/@mastra/core@1.86.0) — 2 days ago
- **Claude Agent SDK** [`v2.1.332`](https://github.com/anthropics/claude-code/releases/tag/v2.1.332) — 2 days ago
- **Google ADK** [`v2.15.1`](https://github.com/google/adk-python/releases/tag/v2.15.1) — 2 days ago
- **CrewAI** [`1.15.45`](https://github.com/crewAIInc/crewAI/releases/tag/1.15.45) — 3 days ago
- **OpenAI Agents SDK** [`v0.26.0`](https://github.com/openai/openai-agents-python/releases/tag/v0.26.0) — 3 days ago
- **AG2** [`v1.3.4`](https://github.com/ag2ai/ag2/releases/tag/v1.3.4) — 4 days ago
- **Agno** [`v3.2.1`](https://github.com/agno-agi/agno/releases/tag/v3.2.1) — 9 days ago

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

*Powered by GitHub Actions • Data refreshed daily • Last run: 2026-11-27 16:25 UTC*