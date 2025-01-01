from django.shortcuts import render
from rest_framework.views import  APIView
from rest_framework.response import Response
from .models import Book
from .serializer import BookSerializer
from rest_framework import status

# Create your views here.
class api_view(APIView):

    def get(self, request):
        queryset = Book.objects.all()
        serializer_class = BookSerializer(queryset, many=True)
        return Response(serializer_class.data)

    def post(self, request):
        serializer = BookSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
