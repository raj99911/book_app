from django.urls import path


from .views import *


urlpatterns = [
    path('user_auth/',UserRegistration.as_view(),name='user_auth')
]

