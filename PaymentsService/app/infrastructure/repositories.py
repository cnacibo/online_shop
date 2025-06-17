# PaymentsService/app/infrastructure/repositories.py
from sqlalchemy import Column, Integer, String, Float, Enum, Boolean, JSON
from app.infrastructure.database import Base


class AccountModel(Base):
    __tablename__ = "accounts"
    __table_args__ = {"schema": "payments"}

    user_id = Column(String, primary_key=True, index=True)
    balance = Column(Float, default=0.0)

class OutboxEventModel(Base):
    __tablename__ = "outbox"
    __table_args__ = {"schema": "payments"}

    id = Column(Integer, primary_key=True, index=True)
    event_type = Column(String)
    payload = Column(JSON)
    sent = Column(Boolean, default=False)

class InboxEventModel(Base):
    __tablename__ = "inbox"
    __table_args__ = {"schema": "payments"}

    id = Column(Integer, primary_key=True, index=True)
    event_type = Column(String)
    payload = Column(JSON)
    processed = Column(Boolean, default=False)
