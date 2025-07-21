# Base code for Startup Copilot AI Agent

from langchain.agents import initialize_agent, Tool
from langchain.chat_models import ChatOpenAI
from langchain.tools import DuckDuckGoSearchRun
from langchain.prompts import PromptTemplate
from langchain.schema import SystemMessage
from langgraph.graph import END, StateGraph

# -----------------------------
# Setup LLM and Search Tool
# -----------------------------
llm = ChatOpenAI(temperature=0, model_name="gpt-4")
search_tool = DuckDuckGoSearchRun()

# -----------------------------
# Define Tools
# -----------------------------
def generate_business_plan(industry, idea):
    prompt = f"""
    Create a one-page lean business plan for the following startup:
    Industry: {industry}
    Idea: {idea}
    Format: Problem, Solution, Market, Unique Value, Channels, Revenue, Cost Structure, Metrics, Team
    """
    return llm.predict(prompt)

def generate_pitch_slide_content(idea):
    prompt = f"""
    Create bullet points for a 5-slide investor pitch deck:
    1. Problem
    2. Solution
    3. Market Opportunity
    4. Traction/Team
    5. Funding Ask
    Based on this idea: {idea}
    """
    return llm.predict(prompt)

def competitor_analysis(idea):
    results = search_tool.run(f"Startups similar to {idea}")
    prompt = f"Summarize the competitors to this startup idea based on this search result:\n{results}"
    return llm.predict(prompt)

# -----------------------------
# LangGraph State Machine
# -----------------------------
class AgentState(dict):
    pass

def plan_node(state):
    industry = state['industry']
    idea = state['idea']
    state['business_plan'] = generate_business_plan(industry, idea)
    return state

def pitch_node(state):
    state['pitch_deck'] = generate_pitch_slide_content(state['idea'])
    return state

def competitors_node(state):
    state['competitors'] = competitor_analysis(state['idea'])
    return state

builder = StateGraph(AgentState)
builder.add_node("Plan", plan_node)
builder.add_node("Pitch", pitch_node)
builder.add_node("Competitors", competitors_node)

builder.set_entry_point("Plan")
builder.add_edge("Plan", "Pitch")
builder.add_edge("Pitch", "Competitors")
builder.add_edge("Competitors", END)

graph = builder.compile()

# -----------------------------
# Sample Input and Execution
# -----------------------------
inputs = {
    "industry": "AgriTech",
    "idea": "A smart irrigation system that uses AI to optimize water usage for small farmers."
}

final_output = graph.invoke(inputs)

print("\n--- Business Plan ---\n", final_output['business_plan'])
print("\n--- Pitch Deck ---\n", final_output['pitch_deck'])
print("\n--- Competitor Analysis ---\n", final_output['competitors'])
