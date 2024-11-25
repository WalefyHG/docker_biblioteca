
from typing import Dict
from django.shortcuts import get_object_or_404
from .models import User
from django.db import models

class Repository:

    model = User

    @classmethod
    def list(cls) -> models.QuerySet:
        return cls.model.objects.all().order_by("id")
    
    @classmethod
    def get(cls, *, id: int) -> models.Model:
        return get_object_or_404(cls.model, id=id)
    
    @classmethod
    def update_payload(
        cls, *, payload: Dict, last_user_id: int, **kwargs
    ) -> Dict:
        updated_payload: Dict = {
            **payload,
            "last_user_id": last_user_id
        }
        return updated_payload
    
    @classmethod
    def post(cls, *, payload: Dict, last_user_id: int, **kwargs) -> models.Model:
        payload = cls.update_payload(payload=payload, last_user_id=last_user_id)
        
        payload.pop("last_user_id", None)

        return cls.model.objects.create(**payload)
    
    @classmethod
    def put(
        cls,
        *,
        instance: models.Model,
        payload: Dict,
        last_user_id: int,
        **kwargs
    ) -> models.Model:
        payload = cls.update_payload(payload=payload, last_user_id=last_user_id)
        for attr, value in payload.items():
            setattr(instance, attr, value)
        instance.save()
        return instance
    
    @classmethod
    def patch(
        cls,
        *,
        instance: models.Model,
        payload: Dict,
        **kwargs
    ) -> models.Model:
        for attr, value in payload.items():
            setattr(instance, attr, value)
        instance.save()
        return instance
    
    @classmethod
    def delete(cls, *, instance: models.Model, **kwargs) -> models.Model:
        instance.delete()
        return instance
    