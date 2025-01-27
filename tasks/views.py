from fastapi import APIRouter

from tasks import crud
from tasks.schemas import Task

router = APIRouter(prefix="/tasks", tags=["Tasks"])

@router.get("/")
def get_tasks():
    return crud.get_tasks()