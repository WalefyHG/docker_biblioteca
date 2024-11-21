from typing import List
from ninja.router import Router
from .schemas import LivroSchemaIn, LivroSchemaOut, LivroSchemaPut
from .models import Book
from django.shortcuts import get_object_or_404
from ninja.pagination import paginate

router = Router()

@router.get('/pegarLivros', response=List[LivroSchemaOut])
@paginate
def get_livros(request):
    return Book.objects.all()

@router.post('/criarLivros', response=LivroSchemaOut)
def post_livros(request, payload: LivroSchemaIn):

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

@router.put('/atualizarLivros/{id}', response=LivroSchemaOut )
def put_livro(request, id: int, payload: LivroSchemaPut):
    
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


@router.delete("/deletarLivro/{id}", response={200: str})
def delete_livro(request, id: int):

    livro_obj = get_object_or_404(Book, id=id)

    livro_obj.delete()

    return "Livro deletado com sucesso"

@router.get("/listarLivro/{id}", response=LivroSchemaOut)
def get_livro_id(request, id: int):

    livro_obj = get_object_or_404(Book, id=id)

    return livro_obj