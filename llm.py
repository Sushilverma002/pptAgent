# llm.py
# from langchain_community.llms import Ollama
from langchain_ollama import OllamaLLM

llm = OllamaLLM(model="llama3")

def generate_slide_json(user_prompt: str):
    prompt = f"""
You are a JSON generator.

STRICT RULES:
- Return ONLY valid JSON
- Do NOT add explanation
- Do NOT use markdown
- Do NOT write anything before or after JSON

Format:
{{
  "slides": [
    {{
      "title": "string",
      "content": ["point1", "point2"]
    }}
  ]
}}

Create exactly 5 slides.

User input:
{user_prompt}
"""

    response = llm.invoke(prompt)
    print("RAW RESPONSE:\n", response)
    return response