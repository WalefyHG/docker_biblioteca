from django.core.management.base import BaseCommand
from livros.models import Book
from user.models import User
from datetime import date
import random
from django.contrib.auth.hashers import make_password

class Command(BaseCommand):

    help = 'Popula o banco de dados com 10 livros'

    def handle(self, *args, **kwargs):
        for i in range(1, 11):
            created = Book.objects.create(
                title=f"Book {i}",
                author=f"Author {i}",
                pages=random.randint(100, 500),
                price=random.randint(10, 100),
                pubdate=date.today()
            )

            if created:
                self.stdout.write(self.style.SUCCESS(f'Book {i} criado com sucesso!'))


        # Criando Usuarios

        for i in range(1, 11):

            password = make_password("123456")

            created = User.objects.create(
                email=f"usuario{i}@gmail.com",
                password=password,
                first_name=f"Usuario {i}",
                last_name=f"Sobrenome {i}",
                is_active=True,
                is_staff=False,
                is_superuser=False,
                date_joined=date.today()
            )

            if created:
                self.stdout.write(self.style.SUCCESS(f'Usuário {i} criado com sucesso!'))

        
        self.stdout.write(self.style.SUCCESS('Dados populados com sucesso!'))