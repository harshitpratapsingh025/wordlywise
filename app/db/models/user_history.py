from sqlalchemy import Column, Integer, String, Text, DateTime
from sqlalchemy.dialects.postgresql import JSONB
from datetime import datetime
from app.db.base import Base


class UserHistory(Base):
    __tablename__ = "user_history"

    id = Column(Integer, primary_key=True, index=True)
    user_id = Column(Integer, nullable=False)
    word = Column(String(100), unique=True, nullable=False)
    part_of_speech = Column(String(50), nullable=True)
    meaning = Column(Text, nullable=False)
    examples = Column(JSONB, nullable=True)    # list of example sentences
    use_cases = Column(JSONB, nullable=True)   # list of use cases
    created_at = Column(DateTime, default=datetime.datetime.utcnow)
