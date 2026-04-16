from db.database import Base
from sqlalchemy import Column, Integer, String, DateTime


class Messages(Base):
    __tablename__ = "messages"

    id = Column(Integer, primary_key=True, index=True)
    content = Column(String, nullable=False)
    sender = Column(String, nullable=False)
    timestamp = Column(DateTime, nullable=False)