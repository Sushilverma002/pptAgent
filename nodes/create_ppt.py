# nodes/create_ppt.py
from ppt_generator import create_ppt

def create_ppt_node(state):
    output = create_ppt(
        state["ppt_json"],
        template_path=state.get("template")
    )

    return {**state, "output_path": output}