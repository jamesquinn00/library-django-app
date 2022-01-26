from django.db import models

# Create your models here.
class Author(models.Model):
    name = models.CharField(max_length=50)
    year_born = models.IntegerField()

    def __str__(self):
        return self.name

class Book(models.Model):
    name = models.CharField(max_length=50)
    author = models.ForeignKey(Author, on_delete=models.SET_NULL, null=True)
    year = models.IntegerField()

    def __str__(self):
        return f'{self.name} ({self.books.name})'