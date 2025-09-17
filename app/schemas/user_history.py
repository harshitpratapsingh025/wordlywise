from uuid import UUID
from pydantic import BaseModel
from typing import List, Optional
from datetime import datetime


class UserHistoryBase(BaseModel):
    word: str
    user_id: UUID
    part_of_speech: Optional[str] = None
    meaning: str
    examples: Optional[List[str]] = []
    use_cases: Optional[List[str]] = []

class UserHistoryCreate(UserHistoryBase):
    pass


class UserHistoryOut(UserHistoryBase):
    id: UUID
    created_at: datetime

    class Config:
        orm_mode = True
