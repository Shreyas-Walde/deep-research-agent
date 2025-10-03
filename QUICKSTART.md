# Quick Reference Guide

## 🚀 Quick Commands

### Start the Research Agent
```bash
cd research
uv run madrs.py
```

### Run with Python
```bash
cd research
python madrs.py  # If uv is not installed
```

## 📝 Common Queries

### Research Examples

```
# Technology
"Latest developments in quantum computing"
"AI agents and autonomous systems 2025"
"Blockchain applications in healthcare"

# Science
"Recent discoveries in space exploration"
"Climate change mitigation strategies"
"CRISPR gene editing advancements"

# Business
"Remote work trends 2025"
"Startup funding landscape"
"Digital transformation best practices"

# Health
"Mental health technology innovations"
"Personalized medicine breakthroughs"
"Nutrition science latest findings"
```

## 🔧 Troubleshooting

### Common Issues

#### 1. ModuleNotFoundError: No module named 'exa_py'
```bash
# Solution: Install dependencies
uv pip install exa-py langchain-cerebras langgraph
```

#### 2. Missing API Keys
```bash
# Solution: Create .env file
echo 'CEREBRAS_API_KEY="your_key"' > .env
echo 'EXA_API_KEY="your_key"' >> .env
```

#### 3. Import Error from Local Modules
```bash
# Solution: Run from research directory
cd research
uv run madrs.py
```

#### 4. Rate Limit Errors
```bash
# Solution: Add delays between queries or upgrade API plan
# Cerebras: Check https://cloud.cerebras.ai/
# Exa: Check https://exa.ai/pricing
```

## 🎯 API Limits

| Provider | Free Tier | Rate Limit |
|----------|-----------|------------|
| Cerebras | Varies | Check dashboard |
| Exa | 1000 searches/month | 100 req/min |

## 💡 Tips & Tricks

### 1. Better Research Queries
```
❌ Bad: "AI"
✅ Good: "AI agents practical applications 2025"

❌ Bad: "technology"
✅ Good: "emerging technologies transforming education"
```

### 2. Adjust Source Count
```python
# In madrs.py, line ~200
sources = search_web(search_query, num_results=3)  # Increase for more depth
```

### 3. Save Research Results
```python
import json

result = deep_research("your query")

with open("research.json", "w") as f:
    json.dump(result, f, indent=2)
```

### 4. Batch Processing
```python
queries = ["query1", "query2", "query3"]
results = [deep_research(q) for q in queries]
```

## 📊 Performance Optimization

### Speed Up Research
1. Use Cerebras (already fastest)
2. Reduce num_results per subagent
3. Shorter max_tokens for LLM
4. Skip memory if not needed

### Improve Quality
1. Increase num_results per subagent
2. Add more specialized agents
3. Enhance prompt templates
4. Filter sources more carefully

## 🔑 Environment Variables

```bash
# Required
CEREBRAS_API_KEY=csk-xxx...
EXA_API_KEY=xxx...

# Optional (future use)
GOOGLE_API_KEY=xxx...
OPENAI_API_KEY=xxx...
```

## 📱 Keyboard Shortcuts

| Key | Action |
|-----|--------|
| `Ctrl+C` | Force exit |
| `exit` / `quit` / `q` | Graceful exit |
| `Enter` | Submit query |

## 🌐 Useful Links

- [Cerebras Cloud](https://cloud.cerebras.ai/)
- [Exa Search](https://exa.ai/)
- [LangGraph Docs](https://langchain-ai.github.io/langgraph/)
- [LangChain Docs](https://python.langchain.com/)

## 📚 Further Reading

- [Multi-Agent Systems](https://en.wikipedia.org/wiki/Multi-agent_system)
- [LLM Inference Speed](https://artificialanalysis.ai/models)
- [Prompt Engineering Guide](https://www.promptingguide.ai/)

---

**Need more help? Check the main [README.md](README.md) or open an [issue](https://github.com/yourusername/faster-research-agent/issues)!**
