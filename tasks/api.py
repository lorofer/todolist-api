from fastapi import APIRouter
from typing import List

from . import models, schemas


task_router = APIRouter(tags=["tasks"])

@task_router.get("/api/get-tasks", response_model=List[schemas.Task])
async def get():
    return await models.Task.objects.all()

@task_router.post("/api/add-task", response_model=schemas.Task)
async def add_task(task: schemas.AddTask):
    new_task = await models.Task.objects.create(**task.model_dump())
    return new_task

@task_router.put("/api/update-task", response_model=schemas.Task)
async def update_task(task: schemas.Task):
    reponse = await models.Task.objects.get(id=task.id)
    reponse.title = task.title
    reponse.description = task.description
    await reponse.update(["title", "description"])
    return reponse

@task_router.delete("/api/delete-task", response_model=schemas.Task)
async def delete(task_id: int):
    task = await models.Task.objects.get(id=task_id)
    await task.delete()
    return task
