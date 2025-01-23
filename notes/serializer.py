from rest_framework import serializers
from .models import Book, Author

class AuthorSerializer(serializers.ModelSerializer):
    class Meta:
        model = Author
        fields = ['id','name']

# class BookSerializer(serializers.ModelSerializer):
#     class Meta:
#         model = Book
#         fields = ['id','title','publish_date','isbn','author']

class Book_AuthorSerializer(serializers.ModelSerializer):
    author = AuthorSerializer(many=True)
    class Meta:
        model = Book
        fields = ['id','title','publish_date','isbn','author','cover_image']

    def create(self, validated_data):
        author_data = validated_data.pop('author')
        book = Book.objects.create(**validated_data)
        for author_data in author_data:
            author_data,created = Author.objects.get_or_create(**author_data)
            book.author.add(author_data)
        return book

    def update(self, instance, validated_data):
        authors = validated_data.pop('author',[])
        instance = super().update(instance, validated_data)
        if authors is not None:
            instance.author.clear()
            for author_data in authors:
                author = Author.objects.get(**author_data)
                instance.author.add(author)
        # instance.save()
        return instance