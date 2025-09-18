from fastapi import APIRouter, HTTPException
from app.schemas.ai import WordResponse, WordPayload
from app.services.ai_service import get_word_meaning

router = APIRouter()

@router.get("/meaning/{word}", response_model=WordResponse)
async def get_meaning(word: str):
    try:
        res = await get_word_meaning(word)
        return res
    except Exception as exc:
        print(f'Error occurred: {exc}')
        raise HTTPException(status_code=500, detail=str(exc))
    
@router.post("/meaning", response_model=WordResponse)
async def get_meaning(payload: WordPayload):
    try:
        res = await get_word_meaning(payload.word)
        return res
    except Exception as exc:
        print(f'Error occurred: {exc}')
        raise HTTPException(status_code=500, detail=str(exc))

