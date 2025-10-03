# Research Agent - Project Structure

## Overview
Organized multi-agent research system with modular components.

## File Structure

```
research/
├── __init__.py          # Package initialization & exports
├── state.py             # State definitions (ResearchState)
├── tools.py             # Search & AI tools (Exa, Cerebras)
├── prompts.py           # All prompt templates
├── madrs.py             # Main multi-agent orchestration
└── fast-research.py     # Basic LangGraph research (original)
```

## Module Details

### 1. `state.py`
**Purpose**: Define state schemas for LangGraph

**Exports**:
- `ResearchState(TypedDict)`: Main state with:
  - `query`: Research topic
  - `subagent_results`: Accumulated results from multiple agents
  - `all_sources`: Accumulated sources (with `operator.add`)
  - `final_analysis`: Synthesized findings

**Usage**:
```python
from research.state import ResearchState
```

---

### 2. `tools.py`
**Purpose**: External API integrations (Exa search, Cerebras AI)

**Exports**:
- `search_web(query, num_results, max_chars)`: Exa web search
- `ask_ai(prompt, max_tokens, temperature)`: Cerebras LLM call
- `extract_sources(search_results)`: Extract clean source info
- `format_search_results(results, max_results)`: Format for context

**Usage**:
```python
from research.tools import search_web, ask_ai

results = search_web("AI agents 2025", num_results=5)
response = ask_ai("Analyze this data...")
```

**Environment Variables Required**:
- `EXA_API_KEY`
- `CEREBRAS_API_KEY`

---

### 3. `prompts.py`
**Purpose**: Centralized prompt templates

**Exports**:
- `get_subagent_prompt(query, perspective)`: For specialized subagents
- `get_analysis_prompt(query, context)`: For final analysis
- `get_search_query_prompt(query, perspective)`: Optimize search queries
- `get_synthesis_prompt(all_results)`: Synthesize multi-agent findings

**Usage**:
```python
from research.prompts import get_analysis_prompt

prompt = get_analysis_prompt(
    query="climate change solutions",
    context="[research data here]"
)
```

**Prompt Structure**:
- Clear sections with numbered steps
- Consistent formatting
- Perspective-based specialization
- Source attribution

---

### 4. `madrs.py`
**Purpose**: Multi-Agent Deep Research System (main orchestrator)

**Features**:
- Lead agent planning (decomposes queries into subtasks)
- Parallel subagent execution (3 specialists: Fundamentals, Trends, Applications)
- Lead agent synthesis (combines all findings)
- Interactive chatbot interface
- LangGraph workflow with memory

**Graph Structure**:
```
START → lead_planning → subagent_execution → lead_synthesis → END
```

**Usage**:
```bash
# Interactive mode
uv run madrs.py

# Or programmatic
from research.madrs import deep_research
result = deep_research("quantum computing 2025")
```

**State Flow**:
1. **Planning**: Query → 3 subtasks
2. **Execution**: 3 subagents search (2 sources each = 6 total)
3. **Synthesis**: Combine findings into report

---

## How the Modules Work Together

### Example Flow:

```python
# 1. Import modules
from research.state import ResearchState
from research.tools import search_web, ask_ai
from research.prompts import get_synthesis_prompt

# 2. Define state
state: ResearchState = {
    'query': 'AI agents in 2025',
    'subagent_results': [],
    'all_sources': [],
    'final_analysis': ''
}

# 3. Use tools
results = search_web(state['query'], num_results=5)

# 4. Use prompts
prompt = get_synthesis_prompt([{
    'analysis': 'Findings from agent 1...',
    'sources': results
}])

# 5. Get AI response
analysis = ask_ai(prompt)

# 6. Update state
state['final_analysis'] = analysis
```

---

## Key Benefits of This Structure

✅ **Separation of Concerns**:
- State definitions separate from logic
- Tools isolated from orchestration
- Prompts centralized for easy updates

✅ **Reusability**:
- Import only what you need
- Tools work independently or in graph
- Prompts can be used in any agent

✅ **Maintainability**:
- Single source of truth for prompts
- Easy to test individual components
- Clear dependencies

✅ **Scalability**:
- Add new tools without touching orchestration
- Create new prompts without modifying tools
- Extend state schema easily

---

## Running the System

### Interactive Chatbot:
```bash
cd research
uv run madrs.py
```

### Programmatic Usage:
```python
from research.madrs import deep_research

result = deep_research("climate change solutions 2025")
print(result['synthesis'])
print(f"Sources: {result['total_sources']}")
```

---

## Next Steps / Future Enhancements

1. **Add More Tools**: 
   - PDF extraction
   - YouTube transcript search
   - Academic paper search

2. **Improve Prompts**:
   - Add few-shot examples
   - Domain-specific templates
   - Multi-language support

3. **Enhanced State**:
   - Add conversation history
   - Track citation quality
   - Store intermediate reasoning

4. **Testing**:
   - Unit tests for each tool
   - Mock API responses
   - Integration tests for graph flow

---

## Dependencies

Required packages:
```
langchain-cerebras
langchain-core
langgraph
exa-py
python-dotenv
```

Install with:
```bash
uv pip install langchain-cerebras langchain-core langgraph exa-py python-dotenv
```
