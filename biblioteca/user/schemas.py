from ninja import Schema
from datetime import datetime


class UserSchemaIn(Schema):
    email: str
    password: str
    first_name: str
    last_name: str
    is_active: bool = True
    is_staff: bool = False
    is_superuser: bool = False
    date_joined: datetime = None

class UserSchemaOut(Schema):
    id: int
    email: str
    first_name: str
    last_name: str
    is_active: bool
    is_staff: bool
    is_superuser: bool
    date_joined: datetime

class UserSchemaPut(Schema):
    email: str = ''
    password: str = ''
    first_name: str = ''
    last_name: str = ''
    is_active: bool = None
    is_staff: bool = False
    is_superuser: bool = False
    date_joined: datetime = None
