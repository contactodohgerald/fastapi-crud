from typing import TYPE_CHECKING, List
import fastapi as _fastapi
import sqlalchemy.orm as _orm

import services as _services

import schemas.user as _schemas

if TYPE_CHECKING:
    from sqlalchemy.orm import Session


app = _fastapi.FastAPI()

@app.get("/api/users", response_model=List[_schemas._User])
async def get_users(db: _orm.Session = _fastapi.Depends(_services.get_db)):
    return await _services.get_all_users(db=db)

@app.get("/api/user/{user_id}/", response_model=_schemas._User)
async def get_user(user_id: str, db: _orm.Session = _fastapi.Depends(_services.get_db)):
    user = await _services.get_user(user_id=user_id, db=db)
    if user is None:
        raise _fastapi.HTTPException(status_code=404, detail="User was not found")
    return user


@app.post("/api/users", response_model=_schemas._User)
async def create_user(user: _schemas.CreateUser,  db: _orm.Session = _fastapi.Depends(_services.get_db),):
    return await _services.create_user(user=user, db=db)

@app.put("/api/user/{user_id}/", response_model=_schemas._User)
async def update_acct(
        user_id: str, 
        user_data: _schemas.CreateUser, 
        db: _orm.Session = _fastapi.Depends(_services.get_db)
    ):
    user = await _services.get_user(user_id=user_id, db=db)
    if user is None:
        raise _fastapi.HTTPException(status_code=404, detail="User was not found")

    return await _services.update_user(user_data=user_data, user=user, db=db)

@app.delete("/api/user/{user_id}/")
async def delete_acct(user_id: str, db: _orm.Session = _fastapi.Depends(_services.get_db)):
    user = await _services.get_user(user_id=user_id, db=db)
    if user is None:
        raise _fastapi.HTTPException(status_code=404, detail="User was not found")

    await _services.delete_user(user=user, db=db)    
    return "User deleted successfully"

