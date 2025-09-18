from sqlalchemy import Column, ForeignKey, ForeignKey, Integer, String, Text, DateTime, func
from sqlalchemy.dialects.postgresql import JSONB
from sqlalchemy.dialects.postgresql import UUID
from uuid import uuid4
from datetime import datetime
from app.db.base import Base


class UserHistory(Base):
    __tablename__ = "user_history"

    id = Column(UUID(as_uuid=True), primary_key=True, default=uuid4)
    user_id = Column(
        UUID(as_uuid=True),
        ForeignKey("users.id", ondelete="CASCADE"),
        nullable=False,
    )
    word = Column(String(100), unique=True, nullable=False)
    part_of_speech = Column(String(50), nullable=True)
    meaning = Column(Text, nullable=False)
    examples = Column(JSONB, nullable=True)    # list of example sentences
    use_cases = Column(JSONB, nullable=True)   # list of use cases
    created_at = Column(DateTime, default=func.now())
