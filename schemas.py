from typing import Optional
from pydantic import BaseModel


class STaskAdd(BaseModel):
    name: str
    description: Optional[str] = None # Работает в Python 3.10+

class STask(STaskAdd):
    id: int
    
    
class STaskId(BaseModel):
    ok: bool = True
    task_id: int