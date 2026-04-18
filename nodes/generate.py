# nodes/generate.py
from llm import generate_slide_json
from utils import parse_json_safe

def generate_node(state):
    raw = generate_slide_json(state["user_input"])
    data = parse_json_safe(raw)

    return {**state, "ppt_json": data}