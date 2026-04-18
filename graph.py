# graph.py
from langgraph.graph import StateGraph, END

from state import AgentState
from nodes.decision import decide_action
from nodes.generate import generate_node
from nodes.update import update_node
from nodes.template import template_node
from nodes.create_ppt import create_ppt_node

builder = StateGraph(AgentState)

# Add nodes
builder.add_node("decide", decide_action)
builder.add_node("generate", generate_node)
builder.add_node("update", update_node)
builder.add_node("template", template_node)
builder.add_node("create_ppt", create_ppt_node)

# Entry
builder.set_entry_point("decide")

# Conditional routing
def route(state):
    if state["action"] == "update":
        return "update"
    return "generate"

builder.add_conditional_edges(
    "decide",
    route,
    {
        "generate": "generate",
        "update": "update"
    }
)

# Flow
builder.add_edge("generate", "template")
builder.add_edge("update", "template")
builder.add_edge("template", "create_ppt")
builder.add_edge("create_ppt", END)

graph = builder.compile()