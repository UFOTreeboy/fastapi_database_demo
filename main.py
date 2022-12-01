from fastapi import FastAPI, Request, Depends, Form, status
from fastapi.templating import Jinja2Templates
import models
import user
from database import engine, sessionlocal
from sqlalchemy.orm import Session
from fastapi.responses import RedirectResponse
from fastapi.staticfiles import StaticFiles

#使用metadata.create_all模組建立位於models的SQL表格
models.Base.metadata.create_all(bind=engine)

#使用Jinja2Templates模組來讀取templates的網頁檔案
templates = Jinja2Templates(directory="templates")

app = FastAPI()

#讀取靜態資源，如圖檔或是CSS
#app.mount("/static", StaticFiles(directory="static"), name="static")

#讀取資料庫
def get_db():
    db = sessionlocal()
    try:
        yield db
    finally:
        db.close()

@app.get("/")
async def home(request: Request, db: Session = Depends(get_db)):
    todos = db.query(models.Todo).order_by(models.Todo.id.desc())
    return templates.TemplateResponse("index.html", {"request": request, "todos": todos})