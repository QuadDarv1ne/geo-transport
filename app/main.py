# app/main.py
from fastapi import FastAPI
from starlette.staticfiles import StaticFiles
from fastapi.templating import Jinja2Templates
from fastapi.requests import Request
from starlette.responses import HTMLResponse
from app.core.config import settings
from app.api import endpoints

app = FastAPI(debug=settings.debug)

app.mount("/static", StaticFiles(directory="static"), name="static")
templates = Jinja2Templates(directory="app/templates")

@app.get("/", response_class=HTMLResponse)
async def read_root(request: Request):
    return templates.TemplateResponse("index.html", {"request": request, "settings": settings})

app.include_router(endpoints.router)