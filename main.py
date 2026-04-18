# # main.py
# from fastapi import FastAPI
# from fastapi.responses import FileResponse

# from llm import generate_slide_json
# from utils import parse_json_safe
# from ppt_generator import create_ppt

# app = FastAPI()

# @app.post("/generate-ppt")
# def generate_ppt(prompt: str):
#     raw = generate_slide_json(prompt)
#     data = parse_json_safe(raw)

#     file_path = create_ppt(data)
    
#     return FileResponse(
#         file_path,
#         media_type="application/vnd.openxmlformats-officedocument.presentationml.presentation",
#         filename="presentation.pptx"
#     )


# main.py
from fastapi import FastAPI, UploadFile, File
from fastapi.responses import FileResponse
import shutil

from runner import run_agent

app = FastAPI()

@app.post("/agent")
async def agent(prompt: str, file: UploadFile = File(None)):
    
    file_path = None

    if file:
        file_path = f"temp_{file.filename}"
        with open(file_path, "wb") as buffer:
            shutil.copyfileobj(file.file, buffer)

    output = run_agent(prompt, file_path)

    return FileResponse(
        output,
        media_type="application/vnd.openxmlformats-officedocument.presentationml.presentation",
        filename="output.pptx"
    )