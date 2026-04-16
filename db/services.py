from db.models import  Messages
from db.database import SessionLocal   
from sqlalchemy.orm import Session
from datetime import datetime





def create_message(db: Session, content: str, sender: str):
    db_message = Messages(content=content, sender=sender, timestamp=datetime.now())
    
    db.add(db_message)
    db.commit()
    db.refresh(db_message)
    return db_message

def get_messages(db: Session, skip: int = 0, limit: int = 100):
    return db.query(Messages).offset(skip).limit(limit).all()  


