import datetime as _dt
import pydantic as _pydantic

class _BaseUser(_pydantic.BaseModel):
    unique_id: str
    first_name: str
    last_name: str
    email: str
    phone_number: str
    gender: str
    password: str


class _User(_BaseUser):
    _id: int
    date_created: _dt.datetime

    class Config:
        orm_mode = True


class CreateUser(_BaseUser):
    pass

