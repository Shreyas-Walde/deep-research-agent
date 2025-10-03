"""Multi-Agent Deep Research System
Interactive Perplexity-style chatbot"""

import os
from typing import List, Dict, Annotated
import operator
from dotenv import load_dotenv

# LangChain imports
from langchain_cerebras import ChatCerebras
from langchain_core.messages import HumanMessage, BaseMessage

# LangGraph imports
from langgraph.graph import StateGraph, END, START
from langgraph.checkpoint.memory import MemorySaver

# Local imports
from tools import search_web as search_tool, ask_ai as ai_tool, extract_sources
from prompts import get_synthesis_prompt

load_dotenv()

CEREBRAS_API_KEY = os.getenv("CEREBRAS_API_KEY")
EXA_API_KEY = os.getenv("EXA_API_KEY")

if not CEREBRAS_API_KEY or not EXA_API_KEY:
    raise ValueError("Missing API keys! Check your .env file")

# Initialize LangChain-Cerebras 
llm = ChatCerebras(
    model="llama-4-scout-17b-16e-instruct",
    api_key=CEREBRAS_API_KEY,
    temperature=0.2,
    max_tokens=600
)

print("✅ MULTI-AGENT DEEP RESEARCH SYSTEM")


# Define State
class ResearchState(dict):
    """State schema for multi-agent research workflow"""
    # Input
    query: str
    
    # Lead Agent planning phase
    subtasks: List[Dict]  # [{"id": 1, "focus": "...", "search_query": "..."}]
    
    # Subagent execution results (accumulated)
    subagent_results: Annotated[List[Dict], operator.add]
    
    # All sources collected (accumulated from all subagents)
    all_sources: Annotated[List[Dict], operator.add]
    
    # Final synthesis
    synthesis: str
    
    # Metadata
    total_sources: int # number of resources


# Wrapper functions for compatibility
def search_web(query: str, num_results: int = 2) -> List[Dict]:
    """Exa web search tool wrapper"""
    try:
        results = search_tool(query, num_results=num_results)
        
        # Filter and clean sources (min 200 chars)
        sources = []
        for r in results:
            if hasattr(r, 'text') and r.text and len(r.text) >= 200:
                sources.append({
                    "title": r.title,
                    "content": r.text[:1000],  # Max 1000 chars
                    "url": r.url if hasattr(r, 'url') else ""
                })
        
        return sources
    
    except Exception as e:
        print(f"  ✗ Search error: {e}")
        return []


def ask_ai(messages: List[BaseMessage]) -> str:
    """AI response using LangChain wrapper"""
    try:
        response = llm.invoke(messages)
        return response.content
    
    except Exception as e:
        print(f"  ✗ AI error: {e}")
        return ""





def lead_agent_planning_node(state: ResearchState) -> ResearchState:
    """Lead Agents"""
    query = state["query"]
    
    # Create decomposition prompt
    planning_prompt = f"""You are a Lead Research Agent. Break down this query into 3 specialized subtasks for parallel execution:

"{query}"

Create 3 distinct subtasks:
1. FUNDAMENTALS: Core concepts, definitions, principles
2. TRENDS: Latest developments, 2025 updates, recent progress
3. APPLICATIONS: Real-world use cases, implementations, impact

For each subtask, provide a focused search query.

Format your response EXACTLY like this:
SUBTASK 1: [search query for fundamentals]
SUBTASK 2: [search query for latest trends]
SUBTASK 3: [search query for applications]"""
    
    # Get AI response
    response = ask_ai([HumanMessage(content=planning_prompt)])
    
    # Parse subtasks
    subtasks = []
    lines = response.split("\n")
    
    for line in lines:
        line = line.strip()
        if line.startswith("SUBTASK 1:"):
            search_query = line.replace("SUBTASK 1:", "").strip()
            subtasks.append({
                "id": 1,
                "focus": "Fundamentals",
                "search_query": search_query
            })
        elif line.startswith("SUBTASK 2:"):
            search_query = line.replace("SUBTASK 2:", "").strip()
            subtasks.append({
                "id": 2,
                "focus": "Trends",
                "search_query": search_query
            })
        elif line.startswith("SUBTASK 3:"):
            search_query = line.replace("SUBTASK 3:", "").strip()
            subtasks.append({
                "id": 3,
                "focus": "Applications",
                "search_query": search_query
            })
    
    # Fallback if parsing fails
    if len(subtasks) != 3:
        print("Parsing failed, using default subtasks")
        subtasks = [
            {"id": 1, "focus": "Fundamentals", "search_query": f"{query} fundamentals basics principles"},
            {"id": 2, "focus": "Trends", "search_query": f"{query} latest developments 2025 trends"},
            {"id": 3, "focus": "Applications", "search_query": f"{query} applications use cases implementation"}
        ]
    
    print(f"✓ Subtasks created:")
    for subtask in subtasks:
        print(f"{subtask['id']}. {subtask['focus']}: {subtask['search_query']}")
    
    return {
        **state,
        "subtasks": subtasks,
        "subagent_results": [],
        "all_sources": []
    }


def subagent_execution_node(state: ResearchState) -> ResearchState:
    """Subagent Parallel Execution"""

    print("PHASE 2: SUBAGENT PARALLEL EXECUTION")
    
    subtasks = state["subtasks"]
    all_subagent_results = []
    all_sources_collected = []
    
    # Execute each subagent (simulated parallel execution)
    for subtask in subtasks:
        subtask_id = subtask["id"]
        focus = subtask["focus"]
        search_query = subtask["search_query"]
        
        print(f"\n Subagent {subtask_id} ({focus}): Searching...")
        print(f"   Query: {search_query}")
        
        # Search web (2 results per subagent)
        sources = search_web(search_query, num_results=2)
        
        print(f"   ✓ Found {len(sources)} sources")
        
        # Store subagent result
        subagent_result = {
            "subtask_id": subtask_id,
            "focus": focus,
            "search_query": search_query,
            "sources": sources,
            "source_count": len(sources)
        }
        
        all_subagent_results.append(subagent_result)
        all_sources_collected.extend(sources)
    
    total_sources = len(all_sources_collected)
    print(f"\n✓ Total sources collected: {total_sources}")
    
    return {
        **state,
        "subagent_results": all_subagent_results,
        "all_sources": all_sources_collected,
        "total_sources": total_sources
    }


def lead_agent_synthesis_node(state: ResearchState) -> ResearchState:
    """Lead Agent - Synthesis -> all three subtask"""

    print("LEAD AGENT - SYNTHESIS (combined)")

    
    query = state["query"]
    subagent_results = state["subagent_results"]
    all_sources = state["all_sources"]
    
    print(f"Lead Agent: Synthesizing {len(all_sources)} sources...")
    
    if not all_sources:
        return {
            **state,
            "synthesis": "No sources found to synthesize."
        }
    
    # Build synthesis context
    context = f"RESEARCH QUERY: {query}\n\n"
    context += "FINDINGS FROM SPECIALIZED AGENTS:\n\n"
    
    for result in subagent_results:
        context += f"--- {result['focus']} Agent (Subtask {result['subtask_id']}) ---\n"
        context += f"Search: {result['search_query']}\n"
        context += f"Sources: {result['source_count']}\n\n"
        
        for i, source in enumerate(result['sources'], 1):
            # Limit to 400 chars per source as per doc
            content_snippet = source['content'][:400]
            context += f"  {i}. {source['title']}\n"
            context += f"     {content_snippet}...\n\n"
    
    # Synthesis prompt
    synthesis_prompt = f"""{context}

As the Lead Agent, synthesize these parallel findings into a comprehensive research report:

EXECUTIVE SUMMARY:
[2-3 sentences covering the most important insights across all agents]

INTEGRATED FINDINGS:
• [Key finding from Fundamentals research]
• [Key finding from Trends research]
• [Key finding from Applications research]
• [Cross-cutting insight that emerged]

RESEARCH QUALITY:
- Total sources analyzed: {len(all_sources)}
- Coverage assessment: [Brief note on how well the research covered the topic]"""
    
    # Get synthesis
    synthesis = ask_ai([HumanMessage(content=synthesis_prompt)])
    
    return {
        **state,
        "synthesis": synthesis
    }


# ============================================
# GRAPH CONSTRUCTION
# ============================================

def create_research_graph():
    """
    Build the LangGraph multi-agent workflow
    
    Flow: START → lead_planning → subagent_execution → lead_synthesis → END
    """
    # Create graph with memory
    workflow = StateGraph(ResearchState)
    
    # Add nodes
    workflow.add_node("lead_planning", lead_agent_planning_node)
    workflow.add_node("subagent_execution", subagent_execution_node)
    workflow.add_node("lead_synthesis", lead_agent_synthesis_node)
    
    # Define edges (linear flow)
    workflow.add_edge(START, "lead_planning")
    workflow.add_edge("lead_planning", "subagent_execution")
    workflow.add_edge("subagent_execution", "lead_synthesis")
    workflow.add_edge("lead_synthesis", END)
    
    # Compile with memory
    memory = MemorySaver()
    app = workflow.compile(checkpointer=memory)
    
    return app


# Initiate deep research
def deep_research(query: str, thread_id: str = "default") -> Dict:
    """Execute multi-agent deep research"""
    
    # Create graph
    app = create_research_graph()
    
    # Initial state
    initial_state = {
        "query": query,
        "subtasks": [],
        "subagent_results": [],
        "all_sources": [],
        "synthesis": "",
        "total_sources": 0
    }
    
    # Run graph with memory
    config = {"configurable": {"thread_id": thread_id}}
    final_state = app.invoke(initial_state, config)
    
    return final_state



def run_chatbot():

    print("INTERACTIVE DEEP RESEARCH CHATBOT")

    print("\nCommands:")
    print("  - Type your research question to start")
    print("  - Type 'exit' or 'quit' to exit")
    print("  - Press Ctrl+C to force exit")

    
    thread_id = "research_session"
    exit_loop = ['exit', 'quit', 'q']
    while True:
        try:
            # Get user input
            user_input = input("\n💬 You: ").strip()
            
            # Check for exit commands
            if user_input.lower() in exit_loop :
                print("\n👋 Goodbye! Thanks for using Deep Research Agent.")

                break
            
            # Validate input
            if not user_input:
                print("Please enter a valid query.")
                continue
            
            # Run deep research
            result = deep_research(user_input, thread_id)
            
            # Display results
            print("✅ RESEARCH COMPLETE")

            print(f"\nQuery: {result['query']}")
            print(f"Total Sources: {result['total_sources']}")
            print(f"\n{result['synthesis']}")

        
        except KeyboardInterrupt:
            print("\n\n👋 Interrupted. Goodbye!")
            break
        
        except Exception as e:
            print(f"\n❌ Error: {e}")
            print("Please try again.")



if __name__ == "__main__":
    # Run interactive chatbot
    run_chatbot()
