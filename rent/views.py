from .models import Rent
from rest_framework.generics import ListAPIView, CreateAPIView, GenericAPIView
from .serializers import CreateRentalSerializer, RentalSerializer, GetAvailbleCarSerailizer
from rest_framework.permissions import IsAuthenticated
from car.models import Car
from django.shortcuts import get_list_or_404
from rest_framework.response import Response
from rest_framework import status
from datetime import datetime
# Create your views here.


def calculatePrice(start_time, end_time, car_obj):
    end = datetime.strptime(end_time, "%Y-%m-%dT%H:%M").timestamp()
    start = datetime.strptime(
        start_time, "%Y-%m-%dT%H:%M").timestamp()

    time_diff = int(end-start)//3600
    price = car_obj.deposit + (car_obj.price_per_hour) * \
        (int(time_diff)) + car_obj.base_price
    print(price)
    data = {'start': start, 'end': end, 'car': car_obj,
            'price': int(price), 'car_id': car_obj.id}
    return data


class AvailableCarView(ListAPIView):
    serializer_class = GetAvailbleCarSerailizer
    queryset = Rent.objects.all()

    def get_queryset(self, *args, **kwargs):
        queryset = super().get_queryset()
        start_date = self.request.query_params.get('start_date')
        end_date = self.request.query_params.get('end_date')
        filter_params = dict(start__date__lte=end_date,
                             end__date__gte=start_date)
        if start_date and end_date:
            try:
                queryset = queryset.exclude(**filter_params)
            except:
                queryset = queryset
        return queryset


class CarPerPersonView(ListAPIView):
    serializer_class = RentalSerializer
    permission_classes = [IsAuthenticated]

    def get_queryset(self, *args, **kwargs):
        user = self.request.user if self.request.user.is_authenticated else 0
        return get_list_or_404(Rent, user=user)


class RentACarView(CreateAPIView):
    serializer_class = CreateRentalSerializer
    queryset = Rent.objects.all()
    permission_classes = [IsAuthenticated]

    def create(self, request, *args, **kwargs):
        data = request.data
        data._mutable = True
        car = Car.objects.filter(id=data.get('car_id')).first()
        data = calculatePrice(data.get('start'), data.get('end'), car)
        serializer = self.serializer_class(data=data)
        serializer.is_valid(raise_exception=True)
        self.perform_create(serializer)
        return Response(serializer.data, status=status.HTTP_201_CREATED)


class CalculatePrice(GenericAPIView):
    serializer_class = GetAvailbleCarSerailizer
    queryset = Rent.objects.all()

    def post(self, *args, **kwargs):
        start = self.request.data.get('start')
        end = self.request.data.get('end')
        car = Car.objects.filter(id=self.request.data.get('car_id')).first()
        data = calculatePrice(start, end, car)
        serializer = self.serializer_class(data=data)
        serializer.is_valid(raise_exception=True)
        return Response(serializer.data, status=status.HTTP_200_OK)
