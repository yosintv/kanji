from fastapi import FastAPI, Request, HTTPException
from fastapi.responses import HTMLResponse
from fastapi.templating import Jinja2Templates
import yaml
import json
import os

app = FastAPI()

# Load Configuration from YAML
def load_config():
    with open("config.yml", "r") as f:
        return yaml.safe_load(f)

config = load_config()
templates = Jinja2Templates(directory="templates")

def get_kanji(level: str):
    # Dynamically find your JSON data based on the level
    data_path = os.path.join("..", "data-engine", "processed", level.lower(), "kanji.json")
    if os.path.exists(data_path):
        with open(data_path, "r", encoding="utf-8") as f:
            return json.load(f)
    return None

@app.get("/", response_class=HTMLResponse)
async def home(request: Request):
    return templates.TemplateResponse("index.html", {"request": request})

@app.get("/{level}", response_class=HTMLResponse)
async def view_level(request: Request, level: str):
    data = get_kanji(level)
    if not data:
        raise HTTPException(status_code=404, detail="Level data not found")
    return templates.TemplateResponse("level.html", {
        "request": request, 
        "level": level.upper(), 
        "kanji": data
    })
