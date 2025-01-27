from django.contrib.auth import authenticate,login
from django.http import Http404
from django.shortcuts import render , get_object_or_404
from rest_framework.views import  APIView
from rest_framework.response import Response
from .models import Book,Author
from .serializer import AuthorSerializer,Book_AuthorSerializer
from rest_framework import status,viewsets,generics
from rest_framework.authentication import BasicAuthentication,SessionAuthentication ,TokenAuthentication
from rest_framework.permissions import IsAdminUser,AllowAny,BasePermission,IsAuthenticated
from rest_framework.authtoken.models import Token
from .permission import IsAdminOrReadOnly
from .pagination import LargeResultsSetPagination
from rest_framework import filters


# Create your views here.
class api_view(APIView):

    def get(self, request):
        queryset = Book.objects.all()
        serializer_class = Book_AuthorSerializer(queryset, many=True)
        return Response(serializer_class.data)

    def post(self, request):
        serializer = Book_AuthorSerializer(data=request.data)
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
        serializer_class = Book_AuthorSerializer(queryset)
        return Response(serializer_class.data)

    def put(self, request , pk):
        queryset = self.get_object(pk)
        serializer = Book_AuthorSerializer(queryset,data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    def patch(self, request , pk):
        queryset = self.get_object(pk)
        serializer = Book_AuthorSerializer(queryset,data=request.data,partial=True)
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
    serializer_class = Book_AuthorSerializer
    # filterset_fields = ['isbn', 'publish_date']
    filter_backends = [filters.SearchFilter,filters.OrderingFilter]
    search_fields = ['publish_date','^author__name']
    ordering_fields = ['publish_date']
    # authentication_classes = [TokenAuthentication]
    # permission_classes = [IsAdminUser]

class BookList(generics.ListCreateAPIView):
    queryset = Author.objects.all()
    serializer_class = AuthorSerializer
    # authentication_classes = [TokenAuthentication]
    permission_classes = [IsAuthenticated]

    # pagination_class = LargeResultsSetPagination

    def get_permissions(self):
        if self.request.method == 'GET':
            return [IsAuthenticated()]
        else:
            return  [IsAdminUser()]

class BookList1(generics.RetrieveUpdateDestroyAPIView):
    queryset = Author.objects.all()
    serializer_class = AuthorSerializer
    authentication_classes = [TokenAuthentication]
    permission_classes = [IsAdminOrReadOnly]


class UserLoginAPIView(APIView):
    permission_classes = [AllowAny]

    def post(self,request,*args,**kwargs):
        user = authenticate(email=request.data['email'],password=request.data['password'])
        if user:
            login(request, user)
            token, created = Token.objects.get_or_create(user=user)
            return Response({
                'access_token':token.key,
            },status=201)
        else:
            return Response({'error':'Invalid credentials'},status=401)


