from django.shortcuts import render
from .serializers import CompanySerializer, CarSerializer
from .models import Car, Company
from rest_framework.generics import RetrieveUpdateDestroyAPIView, ListAPIView, CreateAPIView
from user.pagination import CustomPagination
from user.permissions import CustomIsAdminUser
# Create your views here.


class CarListView(ListAPIView):
    serializer_class = CarSerializer
    queryset = Car.objects.all()
    pagination_class = CustomPagination


class CarCreateView(CreateAPIView):
    permission_classes = [CustomIsAdminUser]
    serializer_class = CarSerializer
    queryset = Car.objects.all()


class CompanyCreateView(CreateAPIView):
    permission_classes = [CustomIsAdminUser]
    serializer_class = CompanySerializer
    queryset = Company.objects.all()


class CarDetailView(RetrieveUpdateDestroyAPIView):
    serializer_class = CarSerializer
    queryset = Car.objects.all()
    permission_classes = [CustomIsAdminUser]
