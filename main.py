import os
from dotenv import load_dotenv
from pydantic import BaseModel, Field
from langchain_google_genai import ChatGoogleGenerativeAI
from langchain.agents import create_agent # The 2026 standard
from tools import tools # Import the list from your tools.py

load_dotenv()

# 1. Define your Structured Schema
class ResearchResponse(BaseModel):
    """The final research report format."""
    topic: str = Field(description="The main subject of research")
    summary: str = Field(description="A concise summary of findings")
    sources: list[str] = Field(description="List of sources used")
    tools_used: list[str] = Field(description="Tools used during the research")

# 2. Initialize Gemini 3
llm = ChatGoogleGenerativeAI(
    model="gemini-3-flash-preview", 
    google_api_key=os.getenv("GOOGLE_API_KEY"),
    thinking_level="high" 
)

# 3. Create the Agent
# We pass the tools list and the response_format for structured output
agent_executor = create_agent(
    llm, 
    tools=tools, 
    system_prompt=(
        "You are a professional research assistant. "
        "Use your tools to find accurate information. "
        "Once you have enough info, summarize it and save it to a file "
        "using the save_text_to_file tool before providing your final answer."
    ),
    response_format=ResearchResponse
)

print("--- AIAgent Active (Tools & Structured Mode) ---")

query = "Research the latest breakthroughs in 5G remote surgery as of early 2026."

# 4. Invoke the Agent
try:
    raw_output = agent_executor.invoke({"messages": [("human", query)]})
    
    # Check for the structured response
    if "structured_response" in raw_output:
        result = raw_output["structured_response"]
        print("\n--- Research Results ---")
        print(f"Topic: {result.topic}")
        print(f"Summary: {result.summary}")
        print(f"Sources: {', '.join(result.sources)}")
    else:
        print("\n--- Raw Response (Fallback) ---")
        print(raw_output["messages"][-1].content)

except Exception as e:
    print(f"An error occurred: {e}")