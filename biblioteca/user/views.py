from typing import List
from ninja_extra import route, api_controller
from user.schemas import UserSchemaOut, UserSchemaIn, UserSchemaPut
from user.models import User
from django.shortcuts import get_object_or_404
from ninja.errors import HttpError
from django.contrib.auth.hashers import make_password

@api_controller(
    'user/',
    tags=["Rotas do Usuario"],
)

class UserController:
    @route.post('create', response={200: UserSchemaOut})
    def create_user(self, request, payload: UserSchemaIn):
        
        if User.objects.filter(email=payload.email):
            raise HttpError(400, "Email já cadastrado")

        password = make_password(payload.password)

        user = User.objects.create_user(
            email=payload.email,
            password=password,
            first_name=payload.first_name,
            last_name=payload.last_name,
            is_active=payload.is_active,
            is_staff=payload.is_staff,
            is_superuser=payload.is_superuser,
            date_joined=payload.date_joined,
        )


        return user
    
    @route.get('list', response={200: List[UserSchemaOut]})
    def list_user(self, request):
        return User.objects.all()
    
    @route.get('get/{id}', response={200: UserSchemaOut})
    def get_user(self, request, id: int):
        return get_object_or_404(User, id=id)
    
    @route.put('update/{id}', response={200: UserSchemaOut})
    def update_user(self, request, id: int, payload: UserSchemaPut):
        user = get_object_or_404(User, id=id)
        if payload.email:
            user.email = payload.email
        if payload.password:
            user.password = make_password(payload.password)
        if payload.first_name:
            user.first_name = payload.first_name
        if payload.last_name:
            user.last_name = payload.last_name
        if payload.is_active is not None:
            user.is_active = payload.is_active
        if payload.is_staff is not None:
            user.is_staff = payload.is_staff
        if payload.is_superuser is not None:
            user.is_superuser = payload.is_superuser
        if payload.date_joined:
            user.date_joined = payload.date_joined
        user.save()

        return user
    

    @route.delete('delete/{id}', response={200: UserSchemaOut})
    def delete_user(self, request, id: int):
        user = get_object_or_404(User, id=id)
        user.delete()
        return user