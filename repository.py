from sqlalchemy import select
from database import new_session, Task0rm
from main import STaskAdd
from schemas import STask


class TaskRepository:
    @classmethod
    async def add_one(cls, data: STaskAdd):
        async with new_session() as session:
            task_dict = data.model_dump()
            
            task = Task0rm(**task_dict)
            session.add(task)
            await session.flush()
            await session.commit()
            return task.id
            
        
    @classmethod
    async def find_all(cls) -> list[STask]:
        async with new_session() as session:
            query = select(Task0rm)
            result = await session.execute(query)
            task_models = result.scalars().all()
            task_schemas = [STask.model_validate(task_model) for task_model in task_models]
            return task_models