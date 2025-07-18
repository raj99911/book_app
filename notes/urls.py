from django.urls import path
from .views import *
from rest_framework.routers import DefaultRouter, SimpleRouter

urlpatterns1 = [
    path('index/', api_view.as_view(), name='index'),
    path('data/<int:pk>/', api_data.as_view(), name='data'),
    path('generic/', BookList.as_view(), name='user-list'),
    path('generic1/<int:pk>/', BookList1.as_view(), name='user-list'),
    path('login/', UserLoginAPIView.as_view(), name='login')

]
# user_list = UserViewSet.as_view({'get': 'list'}),
# user_detail = UserViewSet.as_view({'get': 'retrieve'}),
router = DefaultRouter()
# router = SimpleRouter()
router.register(r'book-viewset', BookViewSet, basename='user')
urlpatterns = urlpatterns1 + router.urls
