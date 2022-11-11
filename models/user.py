import datetime as _dt
import sqlalchemy as _sql

import database as _database

class User(_database.Base):
    __tablename__ = "users"

    _id = _sql.Column(_sql.Integer, primary_key = True, index=True)
    unique_id = _sql.Column(_sql.String, index = True, unique = True)
    first_name = _sql.Column(_sql.String, index = True)
    last_name = _sql.Column(_sql.String, index = True)
    email = _sql.Column(_sql.String, index = True, unique = True)
    phone_number = _sql.Column(_sql.String, index = True, unique = True)
    gender = _sql.Column(_sql.String, index = True)
    password = _sql.Column(_sql.String, index = True)
    status = _sql.Column(_sql.Boolean, index = True, default = False)
    date_created = _sql.Column(_sql.DateTime, default = _dt.datetime.utcnow)

