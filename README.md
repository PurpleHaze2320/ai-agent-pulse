# 🔬 AI Agent Framework Pulse Tracker

> Automated daily tracking of the AI agent framework ecosystem's health, momentum, and trends.
> Last updated: **2026-04-02 03:55 UTC** | Tracking **19** frameworks

## How It Works

This bot runs daily via GitHub Actions and collects metrics from the GitHub API for the most important
AI agent frameworks. It computes a **Pulse Score** (0-100) based on six weighted signals: star velocity,
release freshness, issue health, commit activity, community size, and fork engagement. The result is
a living dashboard that shows which frameworks are gaining momentum and which are losing steam.

## 🏆 Pulse Leaderboard

| Rank | Framework | Pulse | Stars | ⭐ 7d | Commits (4w) | Last Release | Category |
|------|-----------|-------|-------|-------|--------------|--------------|----------|
| 1 | [BrowserUse](https://github.com/browser-use/browser-use) | 🟡 **64.9** | 85.6k | ↗️ +3 | 133 | 7 days ago | `web-agent` |
| 2 | [LangGraph](https://github.com/langchain-ai/langgraph) | 🟡 **64.5** | 28.2k | ↗️ +3 | 127 | 1 day ago | `orchestration` |
| 3 | [Mastra](https://github.com/mastra-ai/mastra) | 🟡 **64.4** | 22.6k | ➡️ +0 | 873 | 6 days ago | `typescript` |
| 4 | [Google ADK](https://github.com/google/adk-python) | 🟡 **63.9** | 18.7k | ➡️ +0 | 131 | 6 days ago | `orchestration` |
| 5 | [LlamaIndex](https://github.com/run-llama/llama_index) | 🟡 **49.6** | 48.2k | ↗️ +1 | 0 | 7 days ago | `data-agent` |
| 6 | [Semantic Kernel](https://github.com/microsoft/semantic-kernel) | 🟡 **47.8** | 27.6k | ➡️ +0 | 0 | 7 days ago | `enterprise` |
| 7 | [Agno](https://github.com/agno-agi/agno) | 🟡 **45.9** | 39.1k | ➡️ +0 | 0 | 1 day ago | `multi-agent` |
| 8 | [Haystack](https://github.com/deepset-ai/haystack) | 🟡 **45.7** | 24.7k | ➡️ +0 | 0 | today | `pipeline` |
| 9 | [CrewAI](https://github.com/crewAIInc/crewAI) | 🟡 **45.4** | 47.8k | ↗️ +2 | 0 | today | `multi-agent` |
| 10 | [OpenAI Agents SDK](https://github.com/openai/openai-agents-python) | 🟡 **45.3** | 20.5k | ↗️ +1 | 0 | 1 day ago | `orchestration` |
| 11 | [AG2](https://github.com/ag2ai/ag2) | 🟡 **45.2** | 4.3k | ➡️ +0 | 0 | 15 days ago | `multi-agent` |
| 12 | [PydanticAI](https://github.com/pydantic/pydantic-ai) | 🟡 **44.6** | 16.0k | ↗️ +1 | 0 | today | `structured` |
| 13 | [Claude Agent SDK](https://github.com/anthropics/claude-code) | 🟡 **42.6** | 102.2k | 📈 +90 | 0 | today | `orchestration` |
| 14 | [Letta](https://github.com/letta-ai/letta) | 🟡 **41.2** | 21.8k | ➡️ +0 | 0 | 1 day ago | `memory` |
| 15 | [Composio](https://github.com/ComposioHQ/composio) | 🟡 **40.8** | 27.6k | ➡️ +0 | 0 | today | `tooling` |
| 16 | [DSPy](https://github.com/stanfordnlp/dspy) | 🟠 **39.5** | 33.4k | ➡️ +0 | 0 | 1 mo ago | `optimization` |
| 17 | [AutoGen](https://github.com/microsoft/autogen) | 🟠 **35.3** | 56.6k | ➡️ +0 | 0 | 6 mo ago | `multi-agent` |
| 18 | [Smolagents](https://github.com/huggingface/smolagents) | 🟠 **33.0** | 26.4k | ↗️ +1 | 0 | 2 mo ago | `lightweight` |
| 19 | [Swarm](https://github.com/openai/swarm) | 🔴 **8.8** | 21.3k | ➡️ +0 | 0 | — | `experimental` |

## 📂 By Category

- `data-agent`: **LlamaIndex** (49.6)
- `enterprise`: **Semantic Kernel** (47.8)
- `experimental`: **Swarm** (8.8)
- `lightweight`: **Smolagents** (33.0)
- `memory`: **Letta** (41.2)
- `multi-agent`: **Agno** (45.9), **CrewAI** (45.4), **AG2** (45.2), **AutoGen** (35.3)
- `optimization`: **DSPy** (39.5)
- `orchestration`: **LangGraph** (64.5), **Google ADK** (63.9), **OpenAI Agents SDK** (45.3), **Claude Agent SDK** (42.6)
- `pipeline`: **Haystack** (45.7)
- `structured`: **PydanticAI** (44.6)
- `tooling`: **Composio** (40.8)
- `typescript`: **Mastra** (64.4)
- `web-agent`: **BrowserUse** (64.9)

## 🔍 Top 5 — Score Breakdown

| Framework | Star Velocity | Release Freshness | Issue Health | Commit Activity | Community | Fork Ratio |
|-----------|:---:|:---:|:---:|:---:|:---:|:---:|
| **BrowserUse** | 0.5 | 97.7 | 97.1 | 100 | 61.0 | 46.3 |
| **LangGraph** | 0.5 | 99.7 | 81.2 | 100 | 54.4 | 68.4 |
| **Mastra** | 0 | 98.0 | 94.1 | 100 | 74.2 | 32.4 |
| **Google ADK** | 0 | 98.0 | 82.5 | 100 | 51.4 | 67.7 |
| **LlamaIndex** | 0.2 | 97.7 | 97.3 | 0.0 | 94.8 | 59.3 |

## 💡 Key Insights

- **Hottest framework**: BrowserUse with a Pulse Score of 64.9
- **Fastest growing**: Claude Agent SDK gained +90 stars this week
- **Most active development**: Mastra with 873 commits in the last 4 weeks
- **Stale releases**: Swarm haven't released in a while

## 📦 Recent Releases

- **PydanticAI** [`v1.76.0`](https://github.com/pydantic/pydantic-ai/releases/tag/v1.76.0) — today
- **Claude Agent SDK** [`v2.1.90`](https://github.com/anthropics/claude-code/releases/tag/v2.1.90) — today
- **CrewAI** [`1.13.0a6`](https://github.com/crewAIInc/crewAI/releases/tag/1.13.0a6) — today *(pre-release)*
- **Haystack** [`v2.27.0`](https://github.com/deepset-ai/haystack/releases/tag/v2.27.0) — today
- **Composio** [`@composio/cli@0.2.18`](https://github.com/ComposioHQ/composio/releases/tag/@composio/cli@0.2.18) — today
- **OpenAI Agents SDK** [`v0.13.4`](https://github.com/openai/openai-agents-python/releases/tag/v0.13.4) — 1 day ago
- **Agno** [`v2.5.13`](https://github.com/agno-agi/agno/releases/tag/v2.5.13) — 1 day ago
- **Letta** [`0.16.7`](https://github.com/letta-ai/letta/releases/tag/0.16.7) — 1 day ago
- **LangGraph** [`1.1.4`](https://github.com/langchain-ai/langgraph/releases/tag/1.1.4) — 1 day ago
- **Google ADK** [`v2.0.0a2`](https://github.com/google/adk-python/releases/tag/v2.0.0a2) — 6 days ago *(pre-release)*

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

*Powered by GitHub Actions • Data refreshed daily • Last run: 2026-04-02 03:55 UTC*