from dotenv import load_dotenv
from app.schemas.ai import WordResponse
from .utils.ai_client import run_ai_task
from .utils.ai_models import get_llm
from .utils.ai_prompts import word_meaning_prompt

load_dotenv()

async def get_word_meaning(word: str, provider="groq", model=None):
    llm = get_llm(provider=provider, model=model)
    return await run_ai_task(
        prompt_template=word_meaning_prompt,
        schema=WordResponse,
        variables={"word": word},
        llm=llm
    )