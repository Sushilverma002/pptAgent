# nodes/template.py
from template_selector import choose_template

def template_node(state):
    template = choose_template(state["user_input"])
    return {**state, "template": template}