# nodes/update.py
from extractor import extract_ppt
from update_llm import update_slides
from utils import parse_json_safe

def update_node(state):
    old = extract_ppt(state["file_path"])
    raw = update_slides(old, state["user_input"])
    data = parse_json_safe(raw)

    return {**state, "ppt_json": data}