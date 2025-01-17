from django.db import models
import uuid,random



def generate_isbn():
    a = str(uuid.uuid4())
    isbn1 = a.replace("-", "")
    isbn = isbn1[0:14]
    return isbn

class Author(models.Model):
    name = models.CharField(max_length=100)

    def __str__(self):
        return self.name

class Book(models.Model):
    title = models.CharField(max_length=100)
    author = models.ManyToManyField(Author)
    publish_date = models.DateField()
    isbn = models.CharField(default = generate_isbn)

    def __str__(self):
        return self.title




