from django.shortcuts import render
from rest_framework.generics import CreateAPIView

# Create your views here.
from .models import User
from .serializer import CustomUserSerializer

class UserRegistration(CreateAPIView):
    serializer_class = CustomUserSerializer
    queryset = User.objects.all()