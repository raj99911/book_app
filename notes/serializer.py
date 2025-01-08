from rest_framework import serializers
from .models import Book, Author

class AuthorSerializer(serializers.ModelSerializer):
    class Meta:
        model = Author
        fields = ['id','name']

class BookSerializer(serializers.ModelSerializer):
    class Meta:
        model = Book
        fields = ['id','title','publish_date','isbn','author']
