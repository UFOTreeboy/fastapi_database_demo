from fastapi import FastAPI
from fastapi.staticfiles import StaticFiles
from routes.article import app_article

app = FastAPI()

app.include_router(app_article)

app.mount("/fastapi_database_demo/static/", StaticFiles(directory="static"), name="static")
