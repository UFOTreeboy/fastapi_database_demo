from fastapi import FastAPI, Request, Depends, Form, status
from fastapi.templating import Jinja2Templates
import model
from database import engine, sessionlocal
from sqlalchemy.orm import Session
from fastapi.responses import RedirectResponse
from fastapi.staticfiles import StaticFiles

model.Base.metadata.create_all(bind=engine)

templates = Jinja2Templates(directory="templates")

app = FastAPI()

app.mount("/static", StaticFiles(directory="static"), name="static")

def get_db():
    db = sessionlocal()
    try:
        yield db
    finally:
        db.close()

@app.get("/")
async def home(request: Request, db: Session = Depends(get_db)):
    todos = db.query(model.Todo).order_by(model.Todo.id.desc())
    return templates.TemplateResponse("index.html", {"request": request, "todos": todos})

@app.post("/add")
async def add(request: Request, task: str = Form(...),name: str = Form(...) ,db: Session = Depends(get_db)):
    todo = model.Todo(task=task,name=name)
    db.add(todo)
    db.commit()
    return RedirectResponse(url=app.url_path_for("home"), status_code=status.HTTP_303_SEE_OTHER)

@app.get("/edit/{todo_id}")
async def add(request: Request, todo_id: int, db: Session = Depends(get_db)):
    todo = db.query(model.Todo).filter(model.Todo.id == todo_id).first()
    return templates.TemplateResponse("edit.html", {"request": request, "todo": todo})

@app.post("/edit/{todo_id}")
async def add(request: Request, todo_id: int, task: str = Form(...),name: str = Form(...),completed: bool = Form(False), db: Session = Depends(get_db)):
    todo = db.query(model.Todo).filter(model.Todo.id == todo_id).first()
    todo.task = task
    todo.name = name
    todo.completed = completed
    db.commit()
    return RedirectResponse(url=app.url_path_for("home"), status_code=status.HTTP_303_SEE_OTHER)

@app.get("/delete/{todo_id}")
async def add(request: Request, todo_id: int, db: Session = Depends(get_db)):
    todo = db.query(model.Todo).filter(model.Todo.id == todo_id).first()
    db.delete(todo)
    db.commit()
    return RedirectResponse(url=app.url_path_for("home"), status_code=status.HTTP_303_SEE_OTHER)