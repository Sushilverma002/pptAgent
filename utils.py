# utils.py
import json
import re

def parse_json_safe(text: str):
    if not text or text.strip() == "":
        raise Exception("Empty response from LLM")

    # Remove markdown ```json ```
    text = text.strip()
    text = re.sub(r"^```json", "", text)
    text = re.sub(r"^```", "", text)
    text = re.sub(r"```$", "", text)

    # Extract JSON block (important)
    match = re.search(r"\{.*\}", text, re.DOTALL)
    if not match:
        raise Exception("No JSON found in response")

    json_str = match.group(0)

    return json.loads(json_str)