from pydantic import BaseModel
from typing import List

class WordResponse(BaseModel):
    word: str
    part_of_speech: str
    meaning: str
    examples: List[str]
    use_cases: List[str]
    
    
class WordPayload(BaseModel):
    word: str