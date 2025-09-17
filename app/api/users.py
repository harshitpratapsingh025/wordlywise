from fastapi import APIRouter, Depends
from app.schemas.user import UserRead
from app.core.security import get_current_user
from app.db.session import async_session
from app.db.models.user import User
from sqlalchemy import select

router = APIRouter()

@router.get("/", response_model=list[UserRead])
async def get_all_users():
    async with async_session() as session:  
        q = await session.execute(select(User))
        users = q.scalars().all()
        return users

