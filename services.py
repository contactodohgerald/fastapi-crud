from typing import TYPE_CHECKING, List
import database as _database
import schemas.user as _schemas
import models.user as _models

if TYPE_CHECKING:
    from sqlalchemy.orm import Session

def _add_tables():
    return _database.Base.metadata.create_all(bind = _database.engine)


def get_db():
    db = _database.SessionLocal()
    try:
        yield db
    finally: 
        db.close()

async def get_all_users(db: "Session") -> List[_schemas._User]:
    users = db.query(_models.User).all()
    return list(map(_schemas._User.from_orm, users))

async def get_user(user_id: str, db: "Session"):
    user = db.query(_models.User).filter(_models.User.unique_id == user_id).first()
    return user

async def create_user(user: _schemas.CreateUser, db: "Session") -> _schemas._User:
    user = _models.User(**user.dict())
    db.add(user)
    db.commit()
    db.refresh(user)
    return _schemas._User.from_orm(user) 

async def delete_user(user: _models.User, db: "Session"):
    db.delete(user)
    db.commit()

async def update_user(user_data: _schemas.CreateUser, user: _models.User, db: "Session") -> _schemas._User:
    user.first_name = user_data.first_name    
    user.last_name = user_data.last_name    
    user.email = user_data.email    
    user.gender = user_data.gender    
    user.phone_number = user_data.phone_number

    db.commit()
    db.refresh(user)  
    return _schemas._User.from_orm(user)