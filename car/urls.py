from xml.etree.ElementInclude import include
from .views import *
from django.urls import path,include

app_name = 'car'

urlpatterns = [
    path('list/', CarListView.as_view(), name='car-list'),
    path('<int:pk>/',CarDetailView.as_view(), name='car-detail'),
    path('add/',CarCreateView.as_view(), name='car-create'),
    path('company/add/',CompanyCreateView.as_view(),name='company-create'),
    path('',include('rent.urls',namespace='car-rent')),
    ]
