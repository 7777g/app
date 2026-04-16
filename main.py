# from db.models import Messages
# from typing import List

# from db.services import get_messages
# from fastapi import FastAPI, Depends, HTTPException, status
# from db.services import get_messages
# from sqlalchemy.orm import Session
# from db.database import get_db,engine, Base 


# app = FastAPI()

# @app.get("/")
# def read_root():
#     return {"message": "Welcome to the Chat API!"}

# @app.post("/messages/", response_model=Messages)
# def create_message(content: str, sender: str, timestamp: str, db: Session = Depends(get_db)):
#     return create_message(db=db, content=content, sender=sender, timestamp=timestamp)   \
#         or HTTPException(status_code=status.HTTP_400_BAD_REQUEST, detail="Message creation failed")

# @app.get("/messages/", response_model=List[Message])
# def read_messages(skip: int = 0, limit: int = 100, db: Session = Depends(get_db)):
#     return get_messages(db=db, skip=skip, limit=limit)
# if __name__ == "__main__":  
#     Base.metadata.create_all(bind=engine)


from typing import List
from fastapi import FastAPI, Depends, HTTPException, status
from sqlalchemy.orm import Session
from db.database import get_db, engine, Base
from db.models import Messages
from db.services import get_messages, create_message as create_message_service
from db.schemas import Message  # Pydantic schema
from fastapi.middleware.cors import CORSMiddleware
app = FastAPI()

app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],  # or specify your frontend URL
    allow_methods=["*"],
    allow_headers=["*"],
)



Base.metadata.create_all(bind=engine)

@app.get("/")
def read_root():
    return {"message": "Welcome to the Chat API!"}

# @app.post("/messages/", response_model=Message)  # Use Pydantic schema, not SQLAlchemy model
# def create_message(content: str, sender: str, timestamp: str, db: Session = Depends(get_db)):
#     result = create_message_service(db=db, content=content, sender=sender, timestamp=timestamp)
#     if not result:
#         raise HTTPException(status_code=status.HTTP_400_BAD_REQUEST, detail="Message creation failed")
#     return result

@app.post("/messages/", response_model=Message)
def create_message(content: str, sender: str, db: Session = Depends(get_db)):
    return create_message_service(db=db, content=content, sender=sender)

@app.get("/messages/", response_model=List[Message])  # Use Pydantic schema
def read_messages(skip: int = 0, limit: int = 100, db: Session = Depends(get_db)):
    return get_messages(db=db, skip=skip, limit=limit)