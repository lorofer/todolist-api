import os

import data_base_module

from tasks.views import router as tasks_router

from fastapi import FastAPI, Depends, Body
from starlette.responses import JSONResponse
from starlette.middleware.cors import CORSMiddleware

from sqlalchemy.orm import Session

origins = ["http://localhost:3000"]

app = FastAPI()
app.include_router(tasks_router)
app.add_middleware(
    CORSMiddleware,
    allow_origins=origins,  # Список разрешенных источников
    allow_credentials=True,
    allow_methods=["*"],  # Разрешенные методы
    allow_headers=["*"],  # Разрешенные заголовки
)

def get_db():
    db = data_base_module.SessionLocal()
    try:
        yield db
    finally:
        db.close()

# @app.get("/api/get-tasks")
# def get(db: Session = Depends(get_db)):
#     return db.query(data_base_module.Task).all()

@app.post("/api/add-task")
def add_task(body = Body(), db: Session = Depends(get_db)):
    new_task = data_base_module.Task(title=body["title"], description=body["description"])

    db.add(new_task)
    db.commit()
    db.refresh(new_task)

    return new_task

@app.put("/api/update-task")
def update_task(body = Body(), db: Session = Depends(get_db)):
    task = db.query(data_base_module.Task).filter(data_base_module.Task.id == body['id']).first()

    if task is None:
        return JSONResponse(status_code=404, content={"message": "Задача не найдена"})

    task.title = body['title']
    task.description = body['description']
    db.commit()
    db.refresh(task)

    return task

@app.delete("/api/delete-task")
def delete(my_task = data_base_module.Task, db: Session = Depends(get_db)):
    task = db.query(data_base_module.Task).filter(data_base_module.Task.id == my_task.id).first()

    if task is None:
        return JSONResponse(status_code=404, content={"message": "Задача не найдена"})

    db.delete(task)
    db.commit()
    return task