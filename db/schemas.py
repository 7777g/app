from pydantic import BaseModel, Field

class User(BaseModel):
    id: int = Field(..., description="The unique identifier of the user")
    name: str = Field(..., description="The name of the user")
    email: str = Field(..., description="The email address of the user")

    class Config:
        orm_mode = True     

from pydantic import BaseModel, Field
from datetime import datetime

class Message(BaseModel):
    id: int = Field(..., description="The unique identifier of the message")
    content: str = Field(..., description="The content of the message")
    sender: str = Field(..., description="The sender of the message")
    timestamp: datetime = Field(..., description="The timestamp of when the message was sent")

    class Config:
        orm_mode = True

