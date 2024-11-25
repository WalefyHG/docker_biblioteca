from django.db import models

# Create your models here.

# Classe para modelagem do livro
class Book(models.Model):
    title = models.CharField(max_length=100, blank=True, null=True)
    author = models.CharField(max_length=100, blank=True, null=True)
    pages = models.IntegerField(blank=True, null=True)
    price = models.DecimalField(max_digits=5, decimal_places=2, blank=True, null=True)
    pubdate = models.DateField(blank=True, null=True)

    def __str__(self):
        return self.title