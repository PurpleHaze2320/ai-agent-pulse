# 🔬 AI Agent Framework Pulse Tracker

> Automated daily tracking of the AI agent framework ecosystem's health, momentum, and trends.
> Last updated: **2026-04-04 07:09 UTC** | Tracking **19** frameworks

## How It Works

This bot runs daily via GitHub Actions and collects metrics from the GitHub API for the most important
AI agent frameworks. It computes a **Pulse Score** (0-100) based on six weighted signals: star velocity,
release freshness, issue health, commit activity, community size, and fork engagement. The result is
a living dashboard that shows which frameworks are gaining momentum and which are losing steam.

## 🏆 Pulse Leaderboard

| Rank | Framework | Pulse | Stars | ⭐ 7d | Commits (4w) | Last Release | Category |
|------|-----------|-------|-------|-------|--------------|--------------|----------|
| 1 | [Mastra](https://github.com/mastra-ai/mastra) | 🟡 **67.6** | 22.7k | 📈 +87 | 940 | 8 days ago | `typescript` |
| 2 | [Claude Agent SDK](https://github.com/anthropics/claude-code) | 🟡 **64.4** | 108.3k | 🚀 +6191 | 0 | today | `orchestration` |
| 3 | [BrowserUse](https://github.com/browser-use/browser-use) | 🟡 **60.0** | 85.9k | 🚀 +382 | 0 | 1 day ago | `web-agent` |
| 4 | [LlamaIndex](https://github.com/run-llama/llama_index) | 🟡 **52.5** | 48.3k | 📈 +65 | 0 | today | `data-agent` |
| 5 | [CrewAI](https://github.com/crewAIInc/crewAI) | 🟡 **51.9** | 48.0k | 🚀 +171 | 0 | 1 day ago | `multi-agent` |
| 6 | [LangGraph](https://github.com/langchain-ai/langgraph) | 🟡 **51.8** | 28.4k | 🚀 +192 | 0 | today | `orchestration` |
| 7 | [Semantic Kernel](https://github.com/microsoft/semantic-kernel) | 🟡 **48.5** | 27.6k | 📈 +23 | 0 | 10 days ago | `enterprise` |
| 8 | [Agno](https://github.com/agno-agi/agno) | 🟡 **48.4** | 39.2k | 📈 +62 | 0 | 1 day ago | `multi-agent` |
| 9 | [OpenAI Agents SDK](https://github.com/openai/openai-agents-python) | 🟡 **47.5** | 20.6k | 📈 +58 | 0 | 3 days ago | `orchestration` |
| 10 | [PydanticAI](https://github.com/pydantic/pydantic-ai) | 🟡 **47.3** | 16.1k | 📈 +71 | 0 | 1 day ago | `structured` |
| 11 | [Haystack](https://github.com/deepset-ai/haystack) | 🟡 **46.3** | 24.7k | ↗️ +19 | 0 | 2 days ago | `pipeline` |
| 12 | [AG2](https://github.com/ag2ai/ag2) | 🟡 **45.7** | 4.4k | ↗️ +12 | 0 | 17 days ago | `multi-agent` |
| 13 | [Google ADK](https://github.com/google/adk-python) | 🟡 **45.6** | 18.7k | 📈 +36 | 0 | 1 day ago | `orchestration` |
| 14 | [Letta](https://github.com/letta-ai/letta) | 🟡 **42.1** | 21.9k | 📈 +28 | 0 | 3 days ago | `memory` |
| 15 | [DSPy](https://github.com/stanfordnlp/dspy) | 🟡 **41.5** | 33.4k | 📈 +56 | 0 | 1 mo ago | `optimization` |
| 16 | [Composio](https://github.com/ComposioHQ/composio) | 🟡 **41.5** | 27.6k | ↗️ +19 | 0 | 1 day ago | `tooling` |
| 17 | [AutoGen](https://github.com/microsoft/autogen) | 🟠 **38.6** | 56.7k | 📈 +91 | 0 | 6 mo ago | `multi-agent` |
| 18 | [Smolagents](https://github.com/huggingface/smolagents) | 🟠 **34.1** | 26.4k | 📈 +36 | 0 | 2 mo ago | `lightweight` |
| 19 | [Swarm](https://github.com/openai/swarm) | 🔴 **9.1** | 21.3k | ↗️ +8 | 0 | — | `experimental` |

## 📂 By Category

- `data-agent`: **LlamaIndex** (52.5)
- `enterprise`: **Semantic Kernel** (48.5)
- `experimental`: **Swarm** (9.1)
- `lightweight`: **Smolagents** (34.1)
- `memory`: **Letta** (42.1)
- `multi-agent`: **CrewAI** (51.9), **Agno** (48.4), **AG2** (45.7), **AutoGen** (38.6)
- `optimization`: **DSPy** (41.5)
- `orchestration`: **Claude Agent SDK** (64.4), **LangGraph** (51.8), **OpenAI Agents SDK** (47.5), **Google ADK** (45.6)
- `pipeline`: **Haystack** (46.3)
- `structured`: **PydanticAI** (47.3)
- `tooling`: **Composio** (41.5)
- `typescript`: **Mastra** (67.6)
- `web-agent`: **BrowserUse** (60.0)

## 🔍 Top 5 — Score Breakdown

| Framework | Star Velocity | Release Freshness | Issue Health | Commit Activity | Community | Fork Ratio |
|-----------|:---:|:---:|:---:|:---:|:---:|:---:|
| **Mastra** | 13.5 | 97.3 | 94.0 | 100 | 74.4 | 32.5 |
| **Claude Agent SDK** | 100 | 100.0 | 79.2 | 0.0 | 9.4 | 65.6 |
| **BrowserUse** | 59.2 | 99.7 | 97.1 | 0.0 | 61.0 | 46.3 |
| **LlamaIndex** | 10.1 | 100.0 | 97.3 | 0.0 | 94.8 | 59.3 |
| **CrewAI** | 26.5 | 99.7 | 94.9 | 0.0 | 56.8 | 54.4 |

## 💡 Key Insights

- **Hottest framework**: Mastra with a Pulse Score of 67.6
- **Fastest growing**: Claude Agent SDK gained +6191 stars this week
- **Most active development**: Mastra with 940 commits in the last 4 weeks
- **Stale releases**: Swarm haven't released in a while

## 📦 Recent Releases

- **Claude Agent SDK** [`v2.1.92`](https://github.com/anthropics/claude-code/releases/tag/v2.1.92) — today
- **LlamaIndex** [`v0.14.20`](https://github.com/run-llama/llama_index/releases/tag/v0.14.20) — today
- **LangGraph** [`1.1.6`](https://github.com/langchain-ai/langgraph/releases/tag/1.1.6) — today
- **PydanticAI** [`v1.77.0`](https://github.com/pydantic/pydantic-ai/releases/tag/v1.77.0) — 1 day ago
- **CrewAI** [`1.13.0`](https://github.com/crewAIInc/crewAI/releases/tag/1.13.0) — 1 day ago
- **Google ADK** [`v1.28.1`](https://github.com/google/adk-python/releases/tag/v1.28.1) — 1 day ago
- **Agno** [`v2.5.14`](https://github.com/agno-agi/agno/releases/tag/v2.5.14) — 1 day ago
- **Composio** [`@composio/vercel@0.6.8`](https://github.com/ComposioHQ/composio/releases/tag/@composio/vercel@0.6.8) — 1 day ago
- **BrowserUse** [`0.12.6`](https://github.com/browser-use/browser-use/releases/tag/0.12.6) — 1 day ago
- **Haystack** [`v2.27.0`](https://github.com/deepset-ai/haystack/releases/tag/v2.27.0) — 2 days ago

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

*Powered by GitHub Actions • Data refreshed daily • Last run: 2026-04-04 07:09 UTC*