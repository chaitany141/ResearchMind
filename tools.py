from langchain.tools import tool
import requests
from bs4 import BeautifulSoup
from tavily import TavilyClient
import os
from dotenv import load_dotenv
load_dotenv()

tavily_client = TavilyClient(api_key=os.getenv("TAVILY_API_KEY"))

@tool
def web_search(query:str) -> str:
    """Search the web for latest information on a topic. Return Titles, URLs and snippets."""
    results = tavily_client.search(query=query, max_results=5)

    out = []

    for r in results.get("results", []):
        out.append(f"Title: {r.get('title', '')}")
        out.append(f"URL: {r.get('url', '')}")
        out.append(f"Snippet: {r.get('content', '')}")
        out.append("---")
        
    return "\n".join(out)

@tool
def scrape_url(url: str) -> str:
    """Scrape the text content of a given URL using BeautifulSoup."""
    try:
        response = requests.get(url, timeout=10)
        response.raise_for_status()
        soup = BeautifulSoup(response.content, 'html.parser')
        
        # Extract text and remove extra whitespace
        text = soup.get_text(separator=' ', strip=True)
        return text
    except Exception as e:
        return f"Error scraping {url}: {str(e)}"
