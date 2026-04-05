# 🔬 AI Agent Framework Pulse Tracker

> Automated daily tracking of the AI agent framework ecosystem's health, momentum, and trends.
> Last updated: **2026-04-05 07:16 UTC** | Tracking **19** frameworks

## How It Works

This bot runs daily via GitHub Actions and collects metrics from the GitHub API for the most important
AI agent frameworks. It computes a **Pulse Score** (0-100) based on six weighted signals: star velocity,
release freshness, issue health, commit activity, community size, and fork engagement. The result is
a living dashboard that shows which frameworks are gaining momentum and which are losing steam.

## 🏆 Pulse Leaderboard

| Rank | Framework | Pulse | Stars | ⭐ 7d | Commits (4w) | Last Release | Category |
|------|-----------|-------|-------|-------|--------------|--------------|----------|
| 1 | [Mastra](https://github.com/mastra-ai/mastra) | 🟡 **68.9** | 22.7k | 🚀 +121 | 633 | 9 days ago | `typescript` |
| 2 | [BrowserUse](https://github.com/browser-use/browser-use) | 🟡 **65.3** | 86.1k | 🚀 +519 | 0 | 2 days ago | `web-agent` |
| 3 | [Claude Agent SDK](https://github.com/anthropics/claude-code) | 🟡 **64.3** | 109.0k | 🚀 +6864 | 0 | 1 day ago | `orchestration` |
| 4 | [CrewAI](https://github.com/crewAIInc/crewAI) | 🟡 **55.0** | 48.1k | 🚀 +252 | 0 | 2 days ago | `multi-agent` |
| 5 | [LangGraph](https://github.com/langchain-ai/langgraph) | 🟡 **54.5** | 28.4k | 🚀 +263 | 0 | 1 day ago | `orchestration` |
| 6 | [LlamaIndex](https://github.com/run-llama/llama_index) | 🟡 **53.4** | 48.3k | 📈 +88 | 0 | 1 day ago | `data-agent` |
| 7 | [Agno](https://github.com/agno-agi/agno) | 🟡 **49.3** | 39.2k | 📈 +89 | 0 | 2 days ago | `multi-agent` |
| 8 | [Semantic Kernel](https://github.com/microsoft/semantic-kernel) | 🟡 **49.0** | 27.6k | 📈 +37 | 0 | 11 days ago | `enterprise` |
| 9 | [OpenAI Agents SDK](https://github.com/openai/openai-agents-python) | 🟡 **48.2** | 20.6k | 📈 +77 | 0 | 4 days ago | `orchestration` |
| 10 | [PydanticAI](https://github.com/pydantic/pydantic-ai) | 🟡 **47.6** | 16.1k | 📈 +81 | 0 | 2 days ago | `structured` |
| 11 | [AG2](https://github.com/ag2ai/ag2) | 🟡 **47.0** | 4.4k | ↗️ +16 | 0 | today | `multi-agent` |
| 12 | [Haystack](https://github.com/deepset-ai/haystack) | 🟡 **46.9** | 24.7k | 📈 +35 | 0 | 3 days ago | `pipeline` |
| 13 | [Google ADK](https://github.com/google/adk-python) | 🟡 **46.0** | 18.7k | 📈 +49 | 0 | 2 days ago | `orchestration` |
| 14 | [Letta](https://github.com/letta-ai/letta) | 🟡 **42.7** | 21.9k | 📈 +47 | 0 | 4 days ago | `memory` |
| 15 | [DSPy](https://github.com/stanfordnlp/dspy) | 🟡 **42.4** | 33.4k | 📈 +81 | 0 | 1 mo ago | `optimization` |
| 16 | [Composio](https://github.com/ComposioHQ/composio) | 🟡 **41.9** | 27.6k | 📈 +32 | 0 | 2 days ago | `tooling` |
| 17 | [AutoGen](https://github.com/microsoft/autogen) | 🟠 **39.7** | 56.7k | 🚀 +122 | 0 | 6 mo ago | `multi-agent` |
| 18 | [Smolagents](https://github.com/huggingface/smolagents) | 🟠 **34.8** | 26.4k | 📈 +56 | 0 | 2 mo ago | `lightweight` |
| 19 | [Swarm](https://github.com/openai/swarm) | 🔴 **9.2** | 21.3k | ↗️ +9 | 0 | — | `experimental` |

## 📂 By Category

- `data-agent`: **LlamaIndex** (53.4)
- `enterprise`: **Semantic Kernel** (49.0)
- `experimental`: **Swarm** (9.2)
- `lightweight`: **Smolagents** (34.8)
- `memory`: **Letta** (42.7)
- `multi-agent`: **CrewAI** (55.0), **Agno** (49.3), **AG2** (47.0), **AutoGen** (39.7)
- `optimization`: **DSPy** (42.4)
- `orchestration`: **Claude Agent SDK** (64.3), **LangGraph** (54.5), **OpenAI Agents SDK** (48.2), **Google ADK** (46.0)
- `pipeline`: **Haystack** (46.9)
- `structured`: **PydanticAI** (47.6)
- `tooling`: **Composio** (41.9)
- `typescript`: **Mastra** (68.9)
- `web-agent`: **BrowserUse** (65.3)

## 🔍 Top 5 — Score Breakdown

| Framework | Star Velocity | Release Freshness | Issue Health | Commit Activity | Community | Fork Ratio |
|-----------|:---:|:---:|:---:|:---:|:---:|:---:|
| **Mastra** | 18.8 | 97.0 | 94.0 | 100 | 74.6 | 32.5 |
| **BrowserUse** | 80.4 | 99.3 | 97.1 | 0.0 | 61.0 | 46.2 |
| **Claude Agent SDK** | 100 | 99.7 | 79.1 | 0.0 | 9.4 | 66.1 |
| **CrewAI** | 39.1 | 99.3 | 94.7 | 0.0 | 56.8 | 54.5 |
| **LangGraph** | 40.8 | 99.7 | 80.9 | 0.0 | 54.4 | 68.4 |

## 💡 Key Insights

- **Hottest framework**: Mastra with a Pulse Score of 68.9
- **Fastest growing**: Claude Agent SDK gained +6864 stars this week
- **Most active development**: Mastra with 633 commits in the last 4 weeks
- **Stale releases**: Swarm haven't released in a while

## 📦 Recent Releases

- **AG2** [`v0.11.5`](https://github.com/ag2ai/ag2/releases/tag/v0.11.5) — today
- **Claude Agent SDK** [`v2.1.92`](https://github.com/anthropics/claude-code/releases/tag/v2.1.92) — 1 day ago
- **LlamaIndex** [`v0.14.20`](https://github.com/run-llama/llama_index/releases/tag/v0.14.20) — 1 day ago
- **LangGraph** [`1.1.6`](https://github.com/langchain-ai/langgraph/releases/tag/1.1.6) — 1 day ago
- **PydanticAI** [`v1.77.0`](https://github.com/pydantic/pydantic-ai/releases/tag/v1.77.0) — 2 days ago
- **CrewAI** [`1.13.0`](https://github.com/crewAIInc/crewAI/releases/tag/1.13.0) — 2 days ago
- **Google ADK** [`v1.28.1`](https://github.com/google/adk-python/releases/tag/v1.28.1) — 2 days ago
- **Agno** [`v2.5.14`](https://github.com/agno-agi/agno/releases/tag/v2.5.14) — 2 days ago
- **Composio** [`@composio/vercel@0.6.8`](https://github.com/ComposioHQ/composio/releases/tag/@composio/vercel@0.6.8) — 2 days ago
- **BrowserUse** [`0.12.6`](https://github.com/browser-use/browser-use/releases/tag/0.12.6) — 2 days ago

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

*Powered by GitHub Actions • Data refreshed daily • Last run: 2026-04-05 07:16 UTC*