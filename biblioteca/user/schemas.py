from typing import Optional
from ninja import Field, Schema, FilterSchema
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
    type_user: str 

class UserSchemaOut(Schema):
    id: int
    email: str
    first_name: str
    last_name: str
    is_active: bool
    is_staff: bool
    is_superuser: bool
    date_joined: datetime
    type_user: str

class UserSchemaPut(Schema):
    email: str = ''
    password: str = ''
    first_name: str = ''
    last_name: str = ''
    is_active: bool = None
    is_staff: bool = False
    is_superuser: bool = False
    date_joined: datetime = None
    type_user: str = ''



class UserErroResponse(Schema):
    message: str


class UserDeleteSchema(Schema):
    email: str
    first_name: str
    last_name: str
    is_active: bool
    is_staff: bool
    is_superuser: bool
    date_joined: datetime
    type_user: str


class UserFilterSchema(FilterSchema):
    search: Optional[str]  = Field(None, title="Search", alias="Procurar" , description="Procure pelo Primeiro ou Ultimo nome do usuário")