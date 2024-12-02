
from typing import List, Optional, Dict, Any, Tuple, Union
from django.http import Http404
from .repository import Repository
from django.db import IntegrityError, models, transaction
from ninja_extra import status
from .models import Book
from django.db.models import Q
from reportlab.pdfgen import canvas
from reportlab.lib.pagesizes import letter
from io import BytesIO


class Services:

    repository = Repository
    whitelist_disable_models: List[Optional[str]] = []


    @classmethod
    def validate_payload(
        cls, *, payload: Dict[str, Any], id: Optional[int] = None, **kwargs
    ) -> Tuple[int, Optional[models.Model | Dict[str, str]]]:
        
        required_fields = []
        missing_fields = [field for field in required_fields if field not in payload]

        if missing_fields:
            return status.HTTP_400_BAD_REQUEST, {
                "message": f"Os campos {missing_fields} são obrigatórios"
            }
        
        instance: Optional[models.Model] = None

        if id:
            try:
                instance = cls.repository.get(id=id)
            except Http404:
                return status.HTTP_404_NOT_FOUND, {"message": (
                    f"{cls.repository.model._meta.verbose_name}"
                    " Não foi encontrado"
                )}
            
        return status.HTTP_200_OK, instance
    

    @classmethod
    def list(
        cls, *, filters: Optional[Dict[str, Any]] = None
    ) -> models.QuerySet:
        queryset = cls.repository.list()
        
        if filters:
            search = filters.pop("search")
            if search:
                queryset = queryset.filter(
                    Q(title__icontains=search) | Q(author__icontains=search)
                )
        return queryset
    
    @classmethod
    def get(
        cls, *, id: int
    ) -> Tuple[int, models.Model | Dict[str, str]]:
        try:
            return status.HTTP_200_OK, cls.repository.get(id=id)
        except Http404:
            return status.HTTP_404_NOT_FOUND, {"message": (
                f"{cls.repository.model._meta.verbose_name}"
                " Não foi encontrado"
            )}
        
    @classmethod
    def post(
        cls, *, payload: Dict[str, Any], last_book_id: int, **kwargs
    ) -> Tuple[int, models.Model | Dict[str, str]]:
        try:
            with transaction.atomic():
                status_code: int
                message: Dict[str, str]

                status_code, message = cls.validate_payload(payload=payload)

                if status_code != status.HTTP_200_OK:
                    return status_code, message
                
                instance = cls.repository.post(payload=payload, last_book_id=last_book_id)
                return status.HTTP_201_CREATED, instance
            
        except IntegrityError as error:
            return status.HTTP_500_INTERNAL_SERVER_ERROR, {"message": str(error)}
        
    @classmethod
    def put(
        cls,
        *,
        id: int,
        payload: Dict[str, Any],
        last_book_id: int,
        **kwargs
    ) -> Tuple[int, Union[models.Model | Dict[str, str]]]:
        try:
            with transaction.atomic():
                status_code: int
                message: Dict[str, str]

                status_code, message_or_object = cls.validate_payload(payload=payload, id=id)

                if status_code != status.HTTP_200_OK:
                    message: Dict[str, str] = message_or_object
                    return status_code, message
                
                instance: models.Model = message_or_object

                instance = cls.repository.put(instance=instance, payload=payload, last_book_id=last_book_id)
                return status.HTTP_200_OK, instance
            
        except IntegrityError as error:
            return status.HTTP_500_INTERNAL_SERVER_ERROR, {"message": str(error)}
        

    @classmethod
    def patch(
        cls,
        *,
        id: int,
        payload: Dict[str, Any],
        **kwargs
    ) -> Tuple[int, Union[models.Model | Dict[str, str]]]:
        try:
            with transaction.atomic():
                status_code: int
                message: Dict[str, str]

                status_code, message_or_object = cls.validate_payload(payload=payload, id=id)

                if status_code != status.HTTP_200_OK:
                    message: Dict[str, str] = message_or_object
                    return status_code, message
                
                instance: models.Model = message_or_object

                instance = cls.repository.patch(instance=instance, payload=payload)
                return status.HTTP_200_OK, instance
            
        except IntegrityError as error:
            return status.HTTP_500_INTERNAL_SERVER_ERROR, {"message": str(error)}
        
    @classmethod
    def delete(
        cls, *, id: int
    ) -> Tuple[int, Dict[str, str]]:
        try:
            with transaction.atomic():
                status_code: int
                message_or_object: Dict[str, str] | models.Model

                status_code, message_or_object = cls.get(id=id)

                if status_code != status.HTTP_200_OK:
                    message: Dict[str, str] = message_or_object
                    return status_code, message
                
                instance: models.Model = message_or_object
                
                instance = cls.repository.delete(instance=instance)

                return status.HTTP_204_NO_CONTENT, instance
            
        except IntegrityError as error:
            return status.HTTP_500_INTERNAL_SERVER_ERROR, {"message": str(error)}
        