from typing import List
from ninja_extra import api_controller, route
from .schemas import LivroSchemaIn, LivroSchemaOut, LivroSchemaPut
from .models import Book
from django.shortcuts import get_object_or_404
from ninja_extra.pagination import paginate, PageNumberPaginationExtra, PaginatedResponseSchema


@api_controller(
    'book/',
    tags=["Rota dos Livros"],
    auth=None,
)
class LivroController:

    @route.get('/list', response={200: PaginatedResponseSchema[LivroSchemaOut]})
    @paginate(PageNumberPaginationExtra, page_size=5)
    def get_livros(self, request):
        livros = Book.objects.all().order_by('id')
        return livros

    @route.post('/create', response=LivroSchemaOut)
    def post_livros(self, request, payload: LivroSchemaIn):

        if Book.objects.filter(title=payload.title).exists():
            return "Livro já existe"

        livro = Book.objects.create(
            title = payload.title,
            author = payload.author,
            pages = payload.pages,
            price = payload.price,
            pubdate = payload.pubdate
        )

        livro.save()


        return livro

    @route.put('/update/{id}', response=LivroSchemaOut )
    def put_livro(self, request, id: int, payload: LivroSchemaPut):
    
        livro_obj = get_object_or_404(Book, id=id)

        if payload.title:
            livro_obj.title = payload.title

        if payload.author:
            livro_obj.author = payload.author

        if payload.pages:
            livro_obj.pages = payload.pages

        if payload.price:
            livro_obj.price = payload.price

        if payload.pubdate:
            livro_obj.pubdate = payload.pubdate

        livro_obj.save()

        return livro_obj


    @route.delete("/delete/{id}", response={200: str})
    def delete_livro(self, request, id: int):

        livro_obj = get_object_or_404(Book, id=id)

        livro_obj.delete()

        return "Livro deletado com sucesso"

    @route.get("/list_book_for_id/{id}", response=LivroSchemaOut)
    def get_livro_id(self, request, id: int):

        livro_obj = get_object_or_404(Book, id=id)

        return livro_obj


    @route.get("/list_book_for_title/{title}", response=List[LivroSchemaOut])
    def get_livro_title(self, request, title: str):

        livro_obj = Book.objects.filter(title=title)

        return livro_obj