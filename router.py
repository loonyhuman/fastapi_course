from fastapi import APIRouter
from repository import TaskRepository
from schemas import STask, STaskAdd, STaskId


router = APIRouter(
    prefix = "/tasks",
    tags = ["Таски"]
)

@router.post("/tasks")
async def add_task(
    task: STaskAdd
) -> STaskId:
    task_id = await TaskRepository.add_one(task)
    return {"ok": True, "task_id": task_id}


@router.get("")
async def get_tasks() -> list[STask]:
    tasks = await TaskRepository.find_all()
    return tasks