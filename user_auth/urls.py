from django.urls import path


from .views import *
from rest_framework_simplejwt.views import(TokenObtainPairView,TokenRefreshView,)

urlpatterns = [
    path('register/',UserRegistration.as_view(),name='user_auth'),
    path('token/', TokenObtainPairView.as_view(), name='token_obtain_pair'),
    path('token/refresh/', TokenRefreshView.as_view(), name='token_refresh'),
]

