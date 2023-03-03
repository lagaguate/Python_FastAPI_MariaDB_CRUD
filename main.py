# Inicio del proyecto 
# Curso Crud con Python y FastAPI

# 1. Levantar uvicorn main:app --reload

from fastapi import FastAPI
from fastapi.responses import HTMLResponse
from router.router import user

app = FastAPI()

app.include_router(user)
