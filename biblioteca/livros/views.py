from typing import List
from ninja import Form, Query
from ninja_extra import api_controller, route
from .schemas import LivroSchemaIn, LivroSchemaOut, LivroSchemaPut, LivroResponseError, LivroDeleteSchemaOut, BookFilterSchema
from .models import Book
from django.shortcuts import get_object_or_404
from ninja_extra.pagination import paginate, PageNumberPaginationExtra, PaginatedResponseSchema
from .services import Services
from utils.main_permission.permissions import AdminPermission

@api_controller(
    'book/',
    tags=["Rota dos Livros"],
    
)
class LivroController:

    services = Services

    @route.get('/list', response={200: PaginatedResponseSchema[LivroSchemaOut], 404: LivroResponseError})
    @paginate(PageNumberPaginationExtra, page_size=5)
    def get_livros(self, request):
        return self.services.list()
    
    @route.post('/create', response={201: LivroSchemaOut, 400: LivroResponseError})
    def post_livros(self, request, payload: Form[LivroSchemaIn]):

        last_book_id = Book.objects.latest('id').id
        return self.services.post(payload=payload.dict(), last_book_id=last_book_id)
    

    @route.put('/update/{id}', response={200: LivroSchemaOut, 404: LivroResponseError})
    def put_livro(self, request, id: int, payload: LivroSchemaPut):
    
        livro_obj = get_object_or_404(Book, id=id)
        return self.services.put(instance=livro_obj, id=id , payload=payload.dict(), last_book_id=Book.objects.latest('id').id)
    

    @route.patch('/update_partial/{id}', response=LivroSchemaOut)
    def patch_livro(self, request, id: int, payload: LivroSchemaPut):

        livro_obj = get_object_or_404(Book, id=id)
        return self.services.patch(instance=livro_obj, id=id , payload=payload.dict())
    
    @route.delete("/delete/{id}", response={204: LivroDeleteSchemaOut, 404: LivroResponseError})
    def delete_livro(self, request, id: int):

        return self.services.delete(id=id)
    

    @route.get("/list_book_for_filters", response=List[LivroSchemaOut])
    def get_livro_id(self, request, filters:BookFilterSchema = Query(...)):

        return self.services.list(filters=filters.dict())
        