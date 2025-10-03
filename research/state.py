"""State definitions for the research agent"""

from typing import TypedDict, List, Dict, Annotated
import operator


class ResearchState(TypedDict):
    """Main state for multi-agent research system"""
    query: str
    research_topic: str
    subagent_results: Annotated[List[Dict], operator.add]
    all_sources: Annotated[List[Dict], operator.add]
    final_analysis: str
    num_results: int
