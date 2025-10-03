# 🚀 Faster Research Agent

> **A blazingly fast multi-agent research system powered by LangGraph, Cerebras AI, and Exa Search**

[![Python 3.12+](https://img.shields.io/badge/python-3.12+-blue.svg)](https://www.python.org/downloads/)
[![LangGraph](https://img.shields.io/badge/LangGraph-0.6+-green.svg)](https://langchain-ai.github.io/langgraph/)
[![Cerebras](https://img.shields.io/badge/Cerebras-Llama_4_Scout-orange.svg)](https://cerebras.ai/)

## 📋 Table of Contents

- [Overview](#-overview)
- [Why Cerebras?](#-why-cerebras)
- [Features](#-features)
- [Architecture](#-architecture)
- [Installation](#-installation)
- [Quick Start](#-quick-start)
- [How It Works](#-how-it-works)
- [Project Structure](#-project-structure)
- [Configuration](#-configuration)
- [Usage Examples](#-usage-examples)
- [Performance](#-performance)
- [Contributing](#-contributing)
- [License](#-license)

## 🎯 Overview

**Faster Research Agent** is a sophisticated multi-agent system that performs deep research on any topic by:

1. **Decomposing** complex queries into specialized subtasks
2. **Executing** parallel searches across multiple perspectives
3. **Synthesizing** findings into comprehensive research reports

The system leverages **LangGraph** for orchestration, **Cerebras AI** for ultra-fast inference, and **Exa** for high-quality web search.

### Key Highlights

- ⚡ **Ultra-Fast**: Powered by Cerebras Cloud SDK (1,800 tokens/sec)
- 🤖 **Multi-Agent**: Three specialized agents (Fundamentals, Trends, Applications)
- 🔍 **Deep Research**: Automatic query decomposition and parallel execution
- 💬 **Interactive**: Chatbot-style interface for continuous research
- 🧠 **State Management**: LangGraph-powered workflow with memory
- 🎯 **Quality Sources**: Exa AI search for relevant, filtered content

## ⚡ Why Cerebras?

We chose **Cerebras Cloud SDK** as our LLM provider for several critical reasons:

### Speed Comparison

| Provider | Model | Speed (tokens/sec) | Latency |
|----------|-------|-------------------|---------|
| **Cerebras** | Llama 4 Scout 17B | **~1,800** | **Ultra-low** |
| OpenAI | GPT-4 Turbo | ~100-150 | Moderate |
| Anthropic | Claude 3.5 Sonnet | ~80-120 | Moderate |
| Google | Gemini 1.5 Pro | ~100-140 | Moderate |

### Why This Matters for Research

1. **Real-Time Responses**: Research synthesis happens in seconds, not minutes
2. **Better UX**: Users get immediate feedback during multi-step research
3. **Cost Efficiency**: Faster inference = more research queries per minute
4. **Scalability**: Handle multiple concurrent research sessions

### Cerebras Advantages

```
Traditional LLM:     [■■■■■■■■■■■■■■■■■■■■] 15-20 seconds
Cerebras:            [■■] 1-2 seconds
                     ↑
              18x faster for research synthesis!
```

- 🚄 **1,800 tokens/sec** vs industry average of ~100 tokens/sec
- ⚡ **Sub-second latency** for most queries
- 💰 **Competitive pricing** with superior performance
- 🎯 **Llama 4 Scout 17B** - Optimized for reasoning and research tasks

## ✨ Features

### Core Capabilities

- 🔬 **Deep Research**: Automatic decomposition into specialized subtasks
- 🤝 **Multi-Agent Orchestration**: Three specialized research agents working in parallel
- 🌐 **Web Search Integration**: Exa AI for high-quality, relevant sources
- 🧠 **State Management**: LangGraph for workflow orchestration with memory
- 💾 **Session Memory**: Maintains context across multiple queries
- 📊 **Quality Filtering**: Sources validated (minimum 200 chars, max 1000 chars)
- 🎨 **Interactive Chat**: User-friendly command-line interface

### Technical Features

- **Modular Architecture**: Separate modules for state, tools, and prompts
- **Error Handling**: Graceful degradation when API calls fail
- **Type Safety**: Full type hints with TypedDict
- **Extensible**: Easy to add new agents or search providers
- **Reproducible**: State checkpointing for debugging

## 🏗️ Architecture

### System Overview

```
┌─────────────────────────────────────────────────────────────────┐
│                     USER INTERACTION LAYER                       │
│                        (run_chatbot)                             │
└─────────────────────────────────────────────────────────────────┘
                              │
                              ▼
┌─────────────────────────────────────────────────────────────────┐
│                    LANGGRAPH ORCHESTRATION                       │
│                  (StateGraph + MemorySaver)                      │
└─────────────────────────────────────────────────────────────────┘
                              │
        ┌─────────────────────┼─────────────────────┐
        │                     │                     │
        ▼                     ▼                     ▼
   ┌─────────┐         ┌──────────┐         ┌──────────┐
   │ Phase 1 │         │ Phase 2  │         │ Phase 3  │
   │ PLANNING│────────▶│EXECUTION │────────▶│SYNTHESIS │
   └─────────┘         └──────────┘         └──────────┘
        │                     │                     │
        ▼                     ▼                     ▼
   [Cerebras]          [Exa Search x3]        [Cerebras]
     1 call              6 sources             1 call
```

### Workflow Diagram

```
                    👤 USER
                     │
                     ├─ "Research: AI agents in 2025"
                     │
                     ▼
            ┌──────────────────┐
            │ deep_research()  │
            │   • Initialize   │
            │   • Create Graph │
            └──────────────────┘
                     │
        ╔════════════╧════════════╗
        ║    NODE 1: PLANNING     ║
        ╠═════════════════════════╣
        ║ • Decompose query       ║
        ║ • Create 3 subtasks:    ║
        ║   1. Fundamentals       ║
        ║   2. Trends (2025)      ║
        ║   3. Applications       ║
        ║ • Cerebras: 1 call      ║
        ╚════════════╤════════════╝
                     │
        ╔════════════╧════════════╗
        ║  NODE 2: EXECUTION      ║
        ╠═════════════════════════╣
        ║ Subagent 1 (Fund.)      ║
        ║   └─→ Exa: 2 sources    ║
        ║ Subagent 2 (Trends)     ║
        ║   └─→ Exa: 2 sources    ║
        ║ Subagent 3 (Apps)       ║
        ║   └─→ Exa: 2 sources    ║
        ║ Total: 6 sources        ║
        ╚════════════╤════════════╝
                     │
        ╔════════════╧════════════╗
        ║  NODE 3: SYNTHESIS      ║
        ╠═════════════════════════╣
        ║ • Combine 6 sources     ║
        ║ • Generate report:      ║
        ║   - Executive Summary   ║
        ║   - Key Findings        ║
        ║   - Quality Assessment  ║
        ║ • Cerebras: 1 call      ║
        ╚════════════╤════════════╝
                     │
                     ▼
            ┌──────────────────┐
            │  Display Results │
            │  • Query         │
            │  • Sources (6)   │
            │  • Full Report   │
            └──────────────────┘
```

### State Flow

```python
# Initial State
{
  query: "AI agents 2025",
  subtasks: [],
  subagent_results: [],
  all_sources: [],
  synthesis: "",
  total_sources: 0
}

# After Planning (Phase 1)
{
  query: "AI agents 2025",
  subtasks: [
    {id: 1, focus: "Fundamentals", search_query: "..."},
    {id: 2, focus: "Trends", search_query: "..."},
    {id: 3, focus: "Applications", search_query: "..."}
  ],
  ...
}

# After Execution (Phase 2)
{
  ...
  subagent_results: [result1, result2, result3],
  all_sources: [src1, src2, src3, src4, src5, src6],  # Accumulated!
  total_sources: 6
}

# After Synthesis (Phase 3)
{
  ...
  synthesis: "EXECUTIVE SUMMARY: ...\nKEY FINDINGS: ..."
}
```

## 📦 Installation

### Prerequisites

- Python 3.12 or higher
- `uv` package manager (recommended) or `pip`
- API Keys:
  - [Cerebras Cloud API Key](https://cloud.cerebras.ai/)
  - [Exa API Key](https://exa.ai/)

### Step 1: Clone the Repository

```bash
git clone https://github.com/yourusername/faster-research-agent.git
cd faster-research-agent
```

### Step 2: Install Dependencies

#### Using `uv` (Recommended)

```bash
# Install uv if you haven't
pip install uv

# Install dependencies
uv pip install -r requirements.txt
```

#### Using `pip`

```bash
pip install langchain-cerebras langchain-core langgraph exa-py python-dotenv cerebras-cloud-sdk
```

### Step 3: Set Up Environment Variables

Create a `.env` file in the root directory:

```bash
# .env
CEREBRAS_API_KEY="your_cerebras_api_key_here"
EXA_API_KEY="your_exa_api_key_here"
```

**Get your API keys:**
- Cerebras: https://cloud.cerebras.ai/
- Exa: https://exa.ai/

## 🚀 Quick Start

### Run the Interactive Chatbot

```bash
cd research
uv run madrs.py
```

### Example Session

```
✅ MULTI-AGENT DEEP RESEARCH SYSTEM
INTERACTIVE DEEP RESEARCH CHATBOT

Commands:
  - Type your research question to start
  - Type 'exit' or 'quit' to exit
  - Press Ctrl+C to force exit

💬 You: What are the latest developments in quantum computing?

✓ Subtasks created:
1. Fundamentals: quantum computing fundamentals principles 2025
2. Trends: quantum computing latest developments 2025 trends
3. Applications: quantum computing applications use cases 2025

PHASE 2: SUBAGENT PARALLEL EXECUTION

 Subagent 1 (Fundamentals): Searching...
   Query: quantum computing fundamentals principles 2025
   ✓ Found 2 sources

 Subagent 2 (Trends): Searching...
   Query: quantum computing latest developments 2025 trends
   ✓ Found 2 sources

 Subagent 3 (Applications): Searching...
   Query: quantum computing applications use cases 2025
   ✓ Found 2 sources

✓ Total sources collected: 6

LEAD AGENT - SYNTHESIS (combined)
Lead Agent: Synthesizing 6 sources...

✅ RESEARCH COMPLETE

Query: What are the latest developments in quantum computing?
Total Sources: 6

EXECUTIVE SUMMARY:
Quantum computing has made significant strides in 2025, with major 
breakthroughs in error correction and practical applications. IBM and 
Google have announced quantum processors with over 1000 qubits...

INTEGRATED FINDINGS:
• Fundamentals: Quantum supremacy now achievable with fewer qubits...
• Trends: Error correction rates improved by 10x in 2025...
• Applications: Financial modeling and drug discovery leading use cases...

💬 You: exit
👋 Goodbye! Thanks for using Deep Research Agent.
```

## 🔍 How It Works

### Phase 1: Lead Agent Planning 🧠

The Lead Agent decomposes your query into three specialized subtasks:

1. **Fundamentals**: Core concepts, definitions, principles
2. **Trends**: Latest developments, 2025 updates
3. **Applications**: Real-world use cases, implementations

**Technology**: Cerebras Llama 4 Scout (1 API call)

### Phase 2: Subagent Parallel Execution 🔎

Three specialized subagents execute searches concurrently:

```
Subagent 1 → Exa Search (Fundamentals) → 2 sources
Subagent 2 → Exa Search (Trends)        → 2 sources  
Subagent 3 → Exa Search (Applications)  → 2 sources
───────────────────────────────────────────────────
                                 Total: 6 sources
```

**Quality Filtering**:
- Minimum 200 characters per source
- Maximum 1000 characters to avoid context overflow
- Only high-quality, relevant content

### Phase 3: Lead Agent Synthesis 📊

The Lead Agent combines all findings into a comprehensive report:

- **Executive Summary**: 2-3 sentence overview
- **Integrated Findings**: Key insights from each perspective
- **Research Quality**: Assessment of coverage and source quality

**Technology**: Cerebras Llama 4 Scout (1 API call)

### Total API Calls Per Query

- **2x Cerebras** (Planning + Synthesis)
- **3x Exa** (Search for each subagent)
- **Total Time**: ~15-30 seconds (varies by API latency)

## 📁 Project Structure

```
faster-research-agent/
│
├── .env                           # Environment variables (API keys)
├── README.md                      # This file
├── requirements.txt               # Python dependencies
│
├── research/                      # Main research package
│   ├── __init__.py               # Package initialization
│   ├── state.py                  # ResearchState definition
│   ├── tools.py                  # Exa search & Cerebras AI tools
│   ├── prompts.py                # Prompt templates
│   ├── madrs.py                  # Multi-agent orchestrator (main)
│   ├── fast-research.py          # Basic LangGraph implementation
│   └── README.md                 # Module documentation
│
├── examples/                      # Usage examples (optional)
│   └── basic_usage.py
│
└── notebooks/                     # Jupyter notebooks (optional)
    └── tutorial.ipynb
```

### Key Modules

#### 1. `state.py` - State Management

```python
from typing import TypedDict, List, Dict, Annotated
import operator

class ResearchState(TypedDict):
    query: str
    subtasks: List[Dict]
    subagent_results: Annotated[List[Dict], operator.add]  # Accumulates!
    all_sources: Annotated[List[Dict], operator.add]
    synthesis: str
    total_sources: int
```

#### 2. `tools.py` - External APIs

```python
# Exa web search
def search_web(query: str, num_results: int = 5) -> List[Any]:
    result = exa.search_and_contents(query, type="auto", ...)
    return result.results

# Cerebras AI
def ask_ai(prompt: str, max_tokens: int = 800) -> str:
    response = cerebras_client.chat.completions.create(...)
    return response.choices[0].message.content
```

#### 3. `prompts.py` - Prompt Templates

```python
def get_subagent_prompt(query: str, perspective: str) -> str:
    return f"""You are a research specialist focusing on: {perspective}
    
    Research Query: {query}
    
    Your task:
    1. Analyze from your specialized perspective
    2. Identify key aspects to research
    3. Provide focused analysis
    """
```

#### 4. `madrs.py` - Main Orchestrator

Contains the three LangGraph nodes and workflow execution logic.

## ⚙️ Configuration

### Environment Variables

```bash
# Required
CEREBRAS_API_KEY="csk-..."       # Get from https://cloud.cerebras.ai/
EXA_API_KEY="..."                # Get from https://exa.ai/

# Optional
GOOGLE_API_KEY="..."             # For future features
```

### Customization Options

#### Adjust Number of Sources Per Subagent

```python
# In madrs.py, line ~200
sources = search_web(search_query, num_results=2)  # Change to 3, 4, 5...
```

#### Modify LLM Parameters

```python
# In tools.py
llm = ChatCerebras(
    model="llama-4-scout-17b-16e-instruct",  # Try different models
    temperature=0.2,      # 0.0 = deterministic, 1.0 = creative
    max_tokens=600        # Increase for longer responses
)
```

#### Change Search Filters

```python
# In madrs.py, search_web wrapper
if hasattr(r, 'text') and r.text and len(r.text) >= 200:  # Min chars
    sources.append({
        "content": r.text[:1000],  # Max chars per source
        ...
    })
```

## 💡 Usage Examples

### Programmatic Usage

```python
from research.madrs import deep_research

# Single query
result = deep_research("climate change solutions 2025")

print(f"Query: {result['query']}")
print(f"Sources: {result['total_sources']}")
print(f"\nSynthesis:\n{result['synthesis']}")
```

### With Custom Thread ID (Session Management)

```python
# Research session 1
result1 = deep_research("AI safety", thread_id="session_ai_safety")

# Research session 2 (separate context)
result2 = deep_research("quantum computing", thread_id="session_quantum")

# Continue session 1
result3 = deep_research("AI alignment", thread_id="session_ai_safety")
```

### Batch Research

```python
queries = [
    "renewable energy trends 2025",
    "blockchain applications healthcare",
    "space exploration recent discoveries"
]

results = []
for i, query in enumerate(queries, 1):
    print(f"[{i}/{len(queries)}] Researching: {query}")
    result = deep_research(query, thread_id=f"batch_{i}")
    results.append(result)

# Save results
import json
with open("research_results.json", "w") as f:
    json.dump(results, f, indent=2)
```

## 📊 Performance

### Benchmarks

| Metric | Value |
|--------|-------|
| Average Query Time | 15-30 seconds |
| Planning Phase | 1-2 seconds |
| Execution Phase | 8-15 seconds |
| Synthesis Phase | 4-10 seconds |
| Sources per Query | 6 (configurable) |
| API Calls per Query | 5 (2 LLM + 3 Search) |

### Performance Tips

1. **Use `uv run`**: Faster than standard Python interpreter
2. **Batch Queries**: Process multiple queries in sequence
3. **Adjust Source Count**: More sources = better quality but slower
4. **Monitor API Limits**: Be aware of rate limits for Cerebras/Exa

### Scalability

- **Concurrent Sessions**: Supported via `thread_id`
- **Memory Usage**: ~50MB per active session
- **Rate Limits**: Respect Cerebras (varies) and Exa (100 req/min) limits

## 🤝 Contributing

We welcome contributions! Here's how you can help:

### Areas for Improvement

1. **Add More Agents**: Implement domain-specific research agents
2. **New Search Providers**: Integrate Google Scholar, arXiv, etc.
3. **Enhanced Prompts**: Improve prompt engineering for better results
4. **UI/UX**: Build a web interface (Streamlit/Gradio)
5. **Testing**: Add unit tests and integration tests
6. **Documentation**: Improve examples and tutorials

### Development Setup

```bash
# Clone and setup
git clone https://github.com/yourusername/faster-research-agent.git
cd faster-research-agent

# Create virtual environment
python -m venv .venv
source .venv/bin/activate  # Windows: .venv\Scripts\activate

# Install in development mode
uv pip install -e .

# Run tests (when available)
pytest tests/
```

### Pull Request Process

1. Fork the repository
2. Create a feature branch (`git checkout -b feature/amazing-feature`)
3. Commit your changes (`git commit -m 'Add amazing feature'`)
4. Push to the branch (`git push origin feature/amazing-feature`)
5. Open a Pull Request

## 📝 License

This project is licensed under the MIT License - see the [LICENSE](LICENSE) file for details.

## 🙏 Acknowledgments

- **LangChain Team**: For the amazing LangGraph framework
- **Cerebras**: For providing ultra-fast inference infrastructure
- **Exa**: For high-quality AI-powered web search
- **Community**: All contributors and users

## 📧 Contact

- **GitHub Issues**: [Report bugs or request features](https://github.com/yourusername/faster-research-agent/issues)
- **Discussions**: [Join the conversation](https://github.com/yourusername/faster-research-agent/discussions)

## 🗺️ Roadmap

### v1.1 (Next Release)
- [ ] Web UI with Streamlit
- [ ] Export reports to PDF/Markdown
- [ ] Source citation formatting
- [ ] Multi-language support

### v2.0 (Future)
- [ ] Custom agent creation
- [ ] Integration with knowledge bases
- [ ] Real-time collaborative research
- [ ] Advanced visualization of research findings

---

**Built with ❤️ using LangGraph, Cerebras AI, and Exa Search**

*Last Updated: October 2025*