# runner.py
from graph import graph

def run_agent(user_input, file_path=None):
    state = {
        "user_input": user_input,
        "file_path": file_path
    }

    result = graph.invoke(state)
    return result["output_path"]