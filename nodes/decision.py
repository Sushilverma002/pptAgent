# nodes/decision.py
from llm import llm

def decide_action(state):
    prompt = f"""
Decide action:
- generate → new ppt
- update → modify ppt

Return only one word.

Input: {state["user_input"]}
"""
    action = llm.invoke(prompt).strip().lower()

    return {**state, "action": action}