from ninja import Schema
from datetime import datetime


class LivroSchemaIn(Schema):
    title: str
    author: str
    pages: int
    price: float
    pubdate: datetime



class LivroSchemaOut(Schema):
    id: int
    title: str
    author: str
    pages: int
    price: float
    pubdate: datetime


class LivroSchemaPut(Schema):
    title: str = ''
    author: str = ''
    pages: int = None
    price: float = None
    pubdate: datetime = None