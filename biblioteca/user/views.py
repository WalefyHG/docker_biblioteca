from typing import List
from ninja import Form, Query
from ninja_extra import route, api_controller
from user.schemas import UserFilterSchema, UserSchemaOut, UserSchemaIn, UserSchemaPut, UserErroResponse, UserDeleteSchema
from user.models import User
from django.shortcuts import get_object_or_404
from ninja.errors import HttpError
from django.contrib.auth.hashers import make_password
from .services import Services
from utils.main_permission.permissions import AdminPermission

@api_controller(
    'user/',
    tags=["Rotas do Usuario"],
    auth=None,
)

class UserController:

    services = Services

    @route.post('create', response={201: UserSchemaOut, 400: UserErroResponse})
    def create_user(self, request, payload: Form[UserSchemaIn]):

        password = make_password(payload.password)

        payload_input = UserSchemaIn(
            email=payload.email,
            password=password,
            first_name=payload.first_name,
            last_name=payload.last_name,
            is_active=payload.is_active,
            is_staff=payload.is_staff,
            is_superuser=payload.is_superuser,
            date_joined=payload.date_joined,
            type_user=payload.type_user
        )

        return self.services.post(payload=payload_input.dict(), last_user_id=User.objects.last().id)


    @route.get('list', response={200: List[UserSchemaOut], 400: UserErroResponse})
    def list_user(self, request):
        return self.services.list() 
    
    @route.get('list_for_search', response={200: List[UserSchemaOut], 400: UserErroResponse})
    def list_user_search(self, request, search: UserFilterSchema = Query(...)):
        return self.services.list(filters=search.dict())
    
    @route.put('update/{id}', response={200: UserSchemaOut, 404: UserErroResponse})
    def update_user(self, request, id: int, payload: UserSchemaPut):
        return self.services.put(id=id, payload=payload.dict(), last_user_id=User.objects.last().id)
    
    @route.patch('update/{id}', response={200: UserSchemaOut, 404: UserErroResponse})
    def patch_user(self, request, id: int, payload: UserSchemaPut):
        return self.services.patch(id=id, payload=payload.dict())
    
    @route.delete('delete/{id}', response={204: UserDeleteSchema, 404: UserErroResponse})
    def delete_user(self, request, id: int):
        return self.services.delete(id=id)