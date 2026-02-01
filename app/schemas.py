from pydantic import BaseModel
from typing import Optional
from datetime import datetime

class TaskBase(BaseModel):
    title: str
    description: Optional[str] = None

class TaskCreate(TaskBase):
    completed: bool = False

class TaskUpdate(TaskBase):
    pass

class TaskResponse(TaskBase):
    id: int
    completed: bool
    created_at: datetime

    class Config:
        orm_mode = True
