from django.urls import path
from .views import AvailableCarView, RentACarView,CalculatePrice

app_name = 'car-rent'

urlpatterns = [
    path('search-cars/',AvailableCarView.as_view(),name="search-cars"),
    path('book/',RentACarView.as_view(),name='book-car'),
    path('calculate-price/',CalculatePrice.as_view(),name='calculate-price'),
]
