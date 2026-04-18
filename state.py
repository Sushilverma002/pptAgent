# state.py
from typing import TypedDict, Optional

class AgentState(TypedDict):
    user_input: str
    action: Optional[str]
    ppt_json: Optional[dict]
    file_path: Optional[str]
    output_path: Optional[str]