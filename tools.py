from langchain_community.tools import DuckDuckGoSearchRun
from langchain_community.utilities import WikipediaAPIWrapper
from langchain_community.tools import WikipediaQueryRun
from langchain_core.tools import tool
from datetime import datetime

# 1. The Search Tool (Now uses the 'ddgs' package internally)
search_tool = DuckDuckGoSearchRun()

# 2. The Wikipedia Tool
api_wrapper = WikipediaAPIWrapper(top_k_results=1, doc_content_chars_max=500)
wiki_tool = WikipediaQueryRun(api_wrapper=api_wrapper)

# 3. The Custom Save Tool
@tool
def save_text_to_file(data: str):
    """Saves research data to research_output.txt. Use this for final results."""
    filename = "research_output.txt"
    timestamp = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
    with open(filename, "a", encoding="utf-8") as f:
        f.write(f"--- {timestamp} ---\n{data}\n\n")
    return f"Saved to {filename}"

# Export for main.py
tools = [search_tool, wiki_tool, save_text_to_file]