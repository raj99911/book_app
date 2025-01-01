from django.db import models
import uuid


# def generate_isbn(self):
#     a = str(uuid.uuid4())
#     isbn1 = a.replace("-", "")
#     isbn = isbn1[0:13]
#     return isbn



class Book(models.Model):
    title = models.CharField(max_length=100)
    author = models.CharField(max_length=100)
    publish_date = models.DateField()
    isbn = models.IntegerField(default = uuid.uuid4())

    def __str__(self):
        return self.title


