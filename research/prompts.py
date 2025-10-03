"""Prompt templates for the research agent"""

from typing import List, Dict


def get_subagent_prompt(query: str, agent_perspective: str) -> str:
    """Generate prompt for a subagent with specific perspective"""
    return f"""You are a research specialist focusing on: {agent_perspective}

Research Query: {query}

Your task:
1. Analyze this query from your specialized perspective
2. Identify the most important aspects to research
3. Provide a focused analysis (2-3 paragraphs)

Focus on: {agent_perspective}"""


def get_analysis_prompt(query: str, context: str) -> str:
    """Generate prompt for final analysis"""
    return f"""Research Query: {query}

Context from multiple research specialists:
{context}

Based on all the research above, provide a comprehensive final analysis that:

1. **SUMMARY**: Synthesize the key findings (2-3 sentences)

2. **KEY INSIGHTS**: List 5 most important insights as bullet points

3. **CONTRADICTIONS/GAPS**: Note any contradictions or information gaps

4. **CONCLUSION**: Provide actionable conclusions (2-3 sentences)

5. **FURTHER RESEARCH**: Suggest 2-3 areas for deeper investigation

Format your response clearly with these sections."""


def get_search_query_prompt(query: str, perspective: str) -> str:
    """Generate optimized search query for a specific perspective"""
    return f"""Original query: {query}
Perspective: {perspective}

Generate an optimized search query (max 10 words) that will find the most relevant sources for this perspective."""


def get_synthesis_prompt(all_results: List[Dict]) -> str:
    """Generate prompt for synthesizing multiple agent results"""
    context = ""
    for i, result in enumerate(all_results, 1):
        context += f"\n--- Research Agent {i} ---\n"
        context += f"Analysis: {result.get('analysis', 'N/A')}\n"
        context += f"Sources: {len(result.get('sources', []))} URLs\n"
    
    return f"""Multiple research agents have analyzed the query from different perspectives:

{context}

Synthesize ALL the findings above into one cohesive report that:
1. Combines insights from all perspectives
2. Identifies patterns and connections
3. Resolves any contradictions
4. Provides a unified conclusion

Be comprehensive but concise."""
