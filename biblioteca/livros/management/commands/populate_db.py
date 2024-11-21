from django.core.management.base import BaseCommand
from livros.models import Book
from datetime import date
import random

class Command(BaseCommand):

    help = 'Popula o banco de dados com 10 livros'

    def handle(self, *args, **kwargs):
        for i in range(1, 11):
            Book.objects.create(
                title=f"Book {i}",
                author=f"Author {i}",
                pages=random.randint(100, 500),
                price=random.randint(10, 100),
                pubdate=date.today()
            )
        self.stdout.write(self.style.SUCCESS('Dados populados com sucesso!'))