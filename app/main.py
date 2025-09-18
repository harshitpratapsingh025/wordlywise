from fastapi import FastAPI
from app.api import users, auth, word
from app.db.session import async_engine
from contextlib import asynccontextmanager

@asynccontextmanager
async def lifespan(app: FastAPI):
    # Startup
    from app.db.base import Base

    async with async_engine.begin() as conn:
        await conn.run_sync(Base.metadata.create_all)
    yield
    
app = FastAPI(title="AI Blog — Backend", lifespan=lifespan)

# Include routers
app.include_router(auth.router, prefix="/api/auth", tags=["auth"])
app.include_router(word.router, prefix="/api/word", tags=["word"])
app.include_router(users.router, prefix="/api/users", tags=["users"])

@app.get("/")
async def root():
    return {"message": "AI Blog backend running"}
