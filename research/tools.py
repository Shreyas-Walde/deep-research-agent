"""Tools for the research agent (Exa search and AI)"""

from exa_py import Exa
from cerebras.cloud.sdk import Cerebras
from typing import List, Dict, Any
import os
from dotenv import load_dotenv

load_dotenv()

# Initialize clients
exa = Exa(api_key=os.getenv("EXA_API_KEY"))
cerebras_client = Cerebras(api_key=os.getenv("CEREBRAS_API_KEY"))


def search_web(query: str, num_results: int = 5, max_chars: int = 1000) -> List[Any]:
    """
    Search the web using Exa's auto search
    
    Args:
        query: Search query string
        num_results: Number of results to return
        max_chars: Maximum characters per result
        
    Returns:
        List of search results with title, url, and text
    """
    try:
        result = exa.search_and_contents(
            query,
            type="auto",
            num_results=num_results,
            text={"max_characters": max_chars}
        )
        return result.results
    except Exception as e:
        print(f"❌ Search error: {e}")
        return []


def ask_ai(prompt: str, max_tokens: int = 800, temperature: float = 0.2) -> str:
    """
    Get AI response from Cerebras LLM
    
    Args:
        prompt: The prompt to send to the AI
        max_tokens: Maximum onse
        temperature: Temperature for response generation
        
    Returns:
        AI response as string
    """
    try:
        chat_completion = cerebras_client.chat.completions.create(
            messages=[
                {
                    "role": "user",
                    "content": prompt,
                }
            ],
            model="llama-4-scout-17b-16e-instruct",
            max_tokens=max_tokens,
            temperature=temperature
        )
        return chat_completion.choices[0].message.content
    except Exception as e:
        print(f"❌ AI error: {e}")
        return f"Error: {str(e)}"


def extract_sources(search_results: List[Any]) -> List[Dict[str, str]]:
    """
    Extract clean source information from search results
    
    Args:
        search_results: List of Exa search results
        
    Returns:
        List of dicts with title and url
    """
    sources = []
    for result in search_results:
        if hasattr(result, 'url') and hasattr(result, 'title'):
            sources.append({
                'title': result.title,
                'url': result.url
            })
    return sources


def format_search_results(search_results: List[Any], max_results: int = 5) -> str:
    """
    Format search results into readable context
    
    Args:
        search_results: List of Exa search results
        max_results: Maximum number of results to include
        
    Returns:
        Formatted string of search results
    """
    context = ""
    for i, result in enumerate(search_results[:max_results], 1):
        title = getattr(result, 'title', 'No title')
        text = getattr(result, 'text', 'No content')
        url = getattr(result, 'url', 'No URL')
        
        context += f"\n{i}. Title: {title}\n"
        context += f"   URL: {url}\n"
        context += f"   Content: {text[:300]}...\n"
    
    return context
