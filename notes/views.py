from django.http import Http404
from django.shortcuts import render , get_object_or_404
from rest_framework.views import  APIView
from rest_framework.response import Response
from .models import Book,Author
from .serializer import BookSerializer,AuthorSerializer
from rest_framework import status,viewsets,generics
from rest_framework.permissions import IsAdminUser

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

class api_data(APIView):

    def get_object(self,pk):
        try:
            return Book.objects.get(pk=pk)
        except Book.DoesNotExist:
            raise Http404

    def get(self, request , pk):
        queryset = self.get_object(pk)
        serializer_class = BookSerializer(queryset)
        return Response(serializer_class.data)

    def put(self, request , pk):
        queryset = self.get_object(pk)
        serializer = BookSerializer(queryset,data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    def delete(self, request, pk):
        queryset = self.get_object(pk)
        queryset.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)

class BookViewSet(viewsets.ModelViewSet):
    queryset = Book.objects.all()
    serializer_class = BookSerializer

class BookList(generics.ListCreateAPIView):
    queryset = Author.objects.all()
    serializer_class = AuthorSerializer
    # permission_classes = [IsAdminUser]

class BookList1(generics.RetrieveUpdateDestroyAPIView):
    queryset = Author.objects.all()
    serializer_class = AuthorSerializer
    # permission_classes = [IsAdminUser]




