from fastapi import FastAPI, Request, File, UploadFile
import shutil
import os
import uuid
import json
import uvicorn

# from test import args
from test import read_image

app = FastAPI()

@app.get("/")
def home():
    return {"message": "Hello!"}

@app.get("/test/")
def home():
    return {"message": "Hello test!"}


@app.post("/api/v1/extract_text")
async def extract_text(image: UploadFile = File(...)):
    temp_file = _save_file_to_disk(image)
    text = await read_image(temp_file)
    return {"filename": image.filename, "text": text}

def _save_file_to_disk(uploaded_file, path=".", save_as="default"):
    extension = os.path.splitext(uploaded_file.filename)[-1]
    temp_file = os.path.join(path, save_as + extension)
    with open(temp_file, "wb") as buffer:
        shutil.copyfileobj(uploaded_file.file, buffer)
    return temp_file

# if __name__ == "__main__":
#     uvicorn.run("server:app", host="127.0.0.1", port=8000, reload=True)

