# 🔬 AI Agent Framework Pulse Tracker

> Automated daily tracking of the AI agent framework ecosystem's health, momentum, and trends.
> Last updated: **2026-04-03 07:18 UTC** | Tracking **19** frameworks

## How It Works

This bot runs daily via GitHub Actions and collects metrics from the GitHub API for the most important
AI agent frameworks. It computes a **Pulse Score** (0-100) based on six weighted signals: star velocity,
release freshness, issue health, commit activity, community size, and fork engagement. The result is
a living dashboard that shows which frameworks are gaining momentum and which are losing steam.

## 🏆 Pulse Leaderboard

| Rank | Framework | Pulse | Stars | ⭐ 7d | Commits (4w) | Last Release | Category |
|------|-----------|-------|-------|-------|--------------|--------------|----------|
| 1 | [Mastra](https://github.com/mastra-ai/mastra) | 🟡 **66.3** | 22.6k | 📈 +51 | 906 | 7 days ago | `typescript` |
| 2 | [Claude Agent SDK](https://github.com/anthropics/claude-code) | 🟡 **64.3** | 107.2k | 🚀 +5077 | 0 | today | `orchestration` |
| 3 | [BrowserUse](https://github.com/browser-use/browser-use) | 🟡 **54.3** | 85.8k | 🚀 +233 | 0 | today | `web-agent` |
| 4 | [LlamaIndex](https://github.com/run-llama/llama_index) | 🟡 **50.9** | 48.2k | 📈 +37 | 0 | 8 days ago | `data-agent` |
| 5 | [LangGraph](https://github.com/langchain-ai/langgraph) | 🟡 **49.0** | 28.3k | 🚀 +120 | 0 | 2 days ago | `orchestration` |
| 6 | [CrewAI](https://github.com/crewAIInc/crewAI) | 🟡 **48.8** | 47.9k | 📈 +89 | 0 | today | `multi-agent` |
| 7 | [Semantic Kernel](https://github.com/microsoft/semantic-kernel) | 🟡 **48.3** | 27.6k | ↗️ +16 | 0 | 9 days ago | `enterprise` |
| 8 | [Agno](https://github.com/agno-agi/agno) | 🟡 **47.5** | 39.1k | 📈 +38 | 0 | today | `multi-agent` |
| 9 | [OpenAI Agents SDK](https://github.com/openai/openai-agents-python) | 🟡 **46.7** | 20.5k | 📈 +35 | 0 | 2 days ago | `orchestration` |
| 10 | [Haystack](https://github.com/deepset-ai/haystack) | 🟡 **46.2** | 24.7k | ↗️ +13 | 0 | 1 day ago | `pipeline` |
| 11 | [PydanticAI](https://github.com/pydantic/pydantic-ai) | 🟡 **46.0** | 16.1k | 📈 +35 | 0 | today | `structured` |
| 12 | [AG2](https://github.com/ag2ai/ag2) | 🟡 **45.5** | 4.3k | ↗️ +5 | 0 | 16 days ago | `multi-agent` |
| 13 | [Google ADK](https://github.com/google/adk-python) | 🟡 **45.1** | 18.7k | 📈 +22 | 0 | today | `orchestration` |
| 14 | [Letta](https://github.com/letta-ai/letta) | 🟡 **41.8** | 21.9k | ↗️ +18 | 0 | 2 days ago | `memory` |
| 15 | [Composio](https://github.com/ComposioHQ/composio) | 🟡 **41.4** | 27.6k | ↗️ +17 | 0 | today | `tooling` |
| 16 | [DSPy](https://github.com/stanfordnlp/dspy) | 🟡 **41.0** | 33.4k | 📈 +41 | 0 | 1 mo ago | `optimization` |
| 17 | [AutoGen](https://github.com/microsoft/autogen) | 🟠 **37.0** | 56.6k | 📈 +48 | 0 | 6 mo ago | `multi-agent` |
| 18 | [Smolagents](https://github.com/huggingface/smolagents) | 🟠 **33.9** | 26.4k | 📈 +27 | 0 | 2 mo ago | `lightweight` |
| 19 | [Swarm](https://github.com/openai/swarm) | 🔴 **9.2** | 21.3k | ↗️ +10 | 0 | — | `experimental` |

## 📂 By Category

- `data-agent`: **LlamaIndex** (50.9)
- `enterprise`: **Semantic Kernel** (48.3)
- `experimental`: **Swarm** (9.2)
- `lightweight`: **Smolagents** (33.9)
- `memory`: **Letta** (41.8)
- `multi-agent`: **CrewAI** (48.8), **Agno** (47.5), **AG2** (45.5), **AutoGen** (37.0)
- `optimization`: **DSPy** (41.0)
- `orchestration`: **Claude Agent SDK** (64.3), **LangGraph** (49.0), **OpenAI Agents SDK** (46.7), **Google ADK** (45.1)
- `pipeline`: **Haystack** (46.2)
- `structured`: **PydanticAI** (46.0)
- `tooling`: **Composio** (41.4)
- `typescript`: **Mastra** (66.3)
- `web-agent`: **BrowserUse** (54.3)

## 🔍 Top 5 — Score Breakdown

| Framework | Star Velocity | Release Freshness | Issue Health | Commit Activity | Community | Fork Ratio |
|-----------|:---:|:---:|:---:|:---:|:---:|:---:|
| **Mastra** | 7.9 | 97.7 | 94.2 | 100 | 74.4 | 32.5 |
| **Claude Agent SDK** | 100 | 100.0 | 79.0 | 0.0 | 9.4 | 64.8 |
| **BrowserUse** | 36.1 | 100.0 | 97.1 | 0.0 | 61.0 | 46.3 |
| **LlamaIndex** | 5.7 | 97.3 | 97.3 | 0.0 | 94.8 | 59.3 |
| **LangGraph** | 18.6 | 99.3 | 81.1 | 0.0 | 54.4 | 68.4 |

## 💡 Key Insights

- **Hottest framework**: Mastra with a Pulse Score of 66.3
- **Fastest growing**: Claude Agent SDK gained +5077 stars this week
- **Most active development**: Mastra with 906 commits in the last 4 weeks
- **Stale releases**: Swarm haven't released in a while

## 📦 Recent Releases

- **PydanticAI** [`v1.77.0`](https://github.com/pydantic/pydantic-ai/releases/tag/v1.77.0) — today
- **Claude Agent SDK** [`v2.1.91`](https://github.com/anthropics/claude-code/releases/tag/v2.1.91) — today
- **CrewAI** [`1.13.0`](https://github.com/crewAIInc/crewAI/releases/tag/1.13.0) — today
- **Google ADK** [`v1.28.1`](https://github.com/google/adk-python/releases/tag/v1.28.1) — today
- **Agno** [`v2.5.14`](https://github.com/agno-agi/agno/releases/tag/v2.5.14) — today
- **Composio** [`@composio/vercel@0.6.8`](https://github.com/ComposioHQ/composio/releases/tag/@composio/vercel@0.6.8) — today
- **BrowserUse** [`0.12.6`](https://github.com/browser-use/browser-use/releases/tag/0.12.6) — today
- **Haystack** [`v2.27.0`](https://github.com/deepset-ai/haystack/releases/tag/v2.27.0) — 1 day ago
- **OpenAI Agents SDK** [`v0.13.4`](https://github.com/openai/openai-agents-python/releases/tag/v0.13.4) — 2 days ago
- **Letta** [`0.16.7`](https://github.com/letta-ai/letta/releases/tag/0.16.7) — 2 days ago

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

*Powered by GitHub Actions • Data refreshed daily • Last run: 2026-04-03 07:18 UTC*