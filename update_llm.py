# update_llm.py

from llm import llm

def update_slides(old_json, user_prompt):
    prompt = f"""
You are an expert presentation editor.

Here is an existing presentation:
{old_json}

Update it based on this instruction:
"{user_prompt}"

Rules:
- Keep number of slides same or slightly improved
- Improve clarity and professionalism
- Add/remove points if needed
- Keep bullet format
- RETURN ONLY VALID JSON

Format:
{{
  "slides": [
    {{
      "title": "string",
      "content": ["point1", "point2"]
    }}
  ]
}}
"""

    response = llm.invoke(prompt)
    return response