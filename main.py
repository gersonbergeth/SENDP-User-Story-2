from fastapi import FastAPI
from fastapi.responses import FileResponse
from fastapi.staticfiles import StaticFiles
import os

app = FastAPI()

# Serve static assets
if os.path.isdir("assets"):
    app.mount("/assets", StaticFiles(directory="assets"), name="assets")

@app.get("/")
def index():
    return FileResponse("index.html")

@app.get("/{path:path}")
def catch_all(path: str):
    if os.path.isfile(path):
        return FileResponse(path)
    return FileResponse("index.html")
