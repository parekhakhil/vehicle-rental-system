from .views import *
from django.urls import path
from rent.views import CarPerPersonView

app_name = 'user'

urlpatterns = [
    path('list/', UserList.as_view(), name='user-list'),
    path('register/', UserCreateView.as_view(), name='register'),
    path('login/', UserLoginView.as_view(), name='login'),
    path('<int:pk>/', UserDetailView.as_view(), name='user_detail'),
    path('logout/', UserLogoutView.as_view(), name='logout'),
    path('booking/',CarPerPersonView.as_view(), name='user-booking'),
]
