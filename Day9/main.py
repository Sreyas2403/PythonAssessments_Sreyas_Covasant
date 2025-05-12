from fastapi import FastAPI, Request, Form
from fastapi.responses import HTMLResponse
from fastapi.templating import Jinja2Templates
from sqlalchemy import create_engine, text
import os

app = FastAPI()
templates = Jinja2Templates(directory="templates")

def get_db():
    DATABASE = os.path.join(".", "people.db")
    engine = create_engine(f"sqlite:///{DATABASE}")
    return engine

def get_one(name):
    engine = get_db()
    with engine.connect() as conn:
        result = conn.execute(
            text("SELECT age FROM people WHERE name = :name"),
            {"name": name}
        ).fetchone()
        return result[0] if result else None

@app.get("/helloj", response_class=HTMLResponse)
async def get_helloj_form(request: Request):
    return templates.TemplateResponse("helloj.html", {"request": request, "age": None})

@app.post("/helloj", response_class=HTMLResponse)
async def post_helloj(request: Request, name: str = Form(...)):
    age = get_one(name)
    return templates.TemplateResponse("helloj.html", {"request": request, "age": age, "name": name})
