from fastapi import FastAPI, Request, HTTPException
from fastapi.responses import HTMLResponse
from fastapi.templating import Jinja2Templates
import json
import os

app = FastAPI(title="Kanjitest.online API")

# Path management: Senior-level dynamic pathing
BASE_DIR = os.path.dirname(os.path.abspath(__file__))
# Note: folder name used as requested: kanjitest-online/web-platform
templates = Jinja2Templates(directory=os.path.join(BASE_DIR, "templates"))

def load_data(level: str):
    """Loads JSON data from the repository data-engine."""
    try:
        # Adjusted for your flat GitHub structure until folders are pushed
        data_path = f"data-engine/processed/{level}/kanji.json"
        with open(data_path, "r", encoding="utf-8") as f:
            return json.load(f)
    except FileNotFoundError:
        return None

@app.get("/", response_class=HTMLResponse)
async def home(request: Request):
    return templates.TemplateResponse("index.html", {"request": request})

@app.get("/{level}", response_class=HTMLResponse)
async def level_view(request: Request, level: str):
    kanji_data = load_data(level.lower())
    if not kanji_data:
        raise HTTPException(status_code=404, detail="Level not found")
    return templates.TemplateResponse("level.html", {
        "request": request,
        "level": level.upper(),
        "kanji": kanji_data
    })

if __name__ == "__main__":
    import uvicorn
    uvicorn.run(app, host="0.0.0.0", port=8000)
