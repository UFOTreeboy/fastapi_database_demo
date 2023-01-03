from fastapi import FastAPI, Request, Depends, Form, status
from fastapi.templating import Jinja2Templates
import model
from database import engine, sessionlocal
from sqlalchemy.orm import Session
from fastapi.responses import RedirectResponse
from fastapi.staticfiles import StaticFiles
import uvicorn,os



model.Base.metadata.create_all(bind=engine)

templates = Jinja2Templates(directory="templates")

app = FastAPI()

app.mount("/fastapi_database_demo/static/", StaticFiles(directory="static"), name="static")


def get_db():
    db = sessionlocal()
    try:
        yield db
    finally:
        db.close()

#註冊路由"/"，並且在index.html顯示已輸入之內容功能
@app.get("/")
async def home(request: Request, db: Session = Depends(get_db)):
    todos = db.query(model.Todo).order_by(model.Todo.id.desc()).limit(20)#最多只顯示前8筆資料
    return templates.TemplateResponse("index.html", {"request": request, "todos": todos})

#假如task一定要接收表單的資料task:str = Form(...),如果願意接收空值則是改成task:str = Form(None)。
#註冊路由"/add"，接受來自html的請求之後，會導向@app.get("/")註冊的home函式。
@app.post("/add")
async def add(request: Request, task:str = Form(None) , name:str = Form(None) ,db: Session = Depends(get_db)):
    todo = model.Todo(task=task,name=name)
    db.add(todo)
    db.commit()
    return RedirectResponse(url=app.url_path_for("home"), status_code=status.HTTP_303_SEE_OTHER)

#在接收來自html的請求之後，會導向@app.get("/")註冊的home函式。
@app.post("/edit/{todo_id}")
async def add(request: Request, todo_id: int, task:str = Form(None),name:str = Form(None),completed: bool = Form(False), db: Session = Depends(get_db)):
    todo = db.query(model.Todo).filter(model.Todo.id == todo_id).first()
    todo.task = task
    todo.name = name
    todo.completed = completed
    db.commit()
    return RedirectResponse(url=app.url_path_for("home"), status_code=status.HTTP_303_SEE_OTHER)

#小功能，對特定ID進行編輯，會導向edit.html頁面。
@app.get("/edit/{todo_id}")
async def add(request: Request, todo_id: int, db: Session = Depends(get_db)):
    todo = db.query(model.Todo).filter(model.Todo.id == todo_id).first()
    return templates.TemplateResponse("edit.html", {"request": request, "todo": todo})

#小功能，刪除特定ID後，會導向@app.get("/")註冊的home函式。
@app.get("/delete/{todo_id}")
async def add(request: Request, todo_id: int, db: Session = Depends(get_db)):
    todo = db.query(model.Todo).filter(model.Todo.id == todo_id).first()
    db.delete(todo)
    db.commit()
    return RedirectResponse(url=app.url_path_for("home"), status_code=status.HTTP_303_SEE_OTHER)

#展開所有文字
@app.post("/user")
async def home(request: Request, db: Session = Depends(get_db)):
    todos = db.query(model.Todo).order_by(model.Todo.id.desc())
    return templates.TemplateResponse("user.html", {"request": request, "todos": todos})


if __name__ == "__main__":
    uvicorn.run("main:app", host="0.0.0.0", port=os.getenv("PORT", default=5000), log_level="info")