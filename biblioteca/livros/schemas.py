from typing import Optional
from ninja import Field, Schema, FilterSchema
from datetime import date


class LivroSchemaIn(Schema):
    title: str
    author: str
    pages: int
    price: float
    pubdate: date



class LivroSchemaOut(Schema):
    id: int
    title: str
    author: str
    pages: int
    price: float
    pubdate: date


class LivroSchemaPut(Schema):
    title: Optional[str] = ''
    author: Optional[str] = ''
    pages: Optional[int] = None
    price: Optional[float] = None
    pubdate: Optional[date] = None


class LivroResponseError(Schema):
    message: str


class LivroDeleteSchemaOut(Schema):
    title: str
    author: str
    pages: int
    price : float
    pubdate: date


class BookFilterSchema(FilterSchema):
    search: Optional[str] = Field(None, alias="Procurar", description="Busque pelo titulo ou pelo author")