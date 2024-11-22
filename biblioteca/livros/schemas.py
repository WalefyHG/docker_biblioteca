from ninja import Schema
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
    title: str = ''
    author: str = ''
    pages: int = None
    price: float = None
    pubdate: date = None