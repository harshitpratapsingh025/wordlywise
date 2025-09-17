import sqlalchemy as sa
from sqlalchemy.dialects.postgresql import UUID
from uuid import uuid4
from app.db.session import Base


class User(Base):
    __tablename__ = "users"
    id = sa.Column(UUID(as_uuid=True), primary_key=True, default=uuid4)
    name = sa.Column(sa.String(80), nullable=False)
    email = sa.Column(sa.String(255), unique=True, nullable=False)
    avatar = sa.Column(sa.Text, nullable=True)
    gender = sa.Column(sa.Boolean, nullable=True)
    password_hash = sa.Column(sa.Text, nullable=False)
    created_at = sa.Column(sa.DateTime, server_default=sa.func.now())
    updated_at = sa.Column(
        sa.DateTime, server_default=sa.func.now(), onupdate=sa.func.now()
    )
