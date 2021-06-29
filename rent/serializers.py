from rest_framework import serializers
from .models import Rent
from user.serializers import UserSerializer
from car.serializers import CarSerializer
from car.models import Car
from user.models import User


class RentalSerializer(serializers.ModelSerializer):
    car = CarSerializer(read_only=True)
    car_id = serializers.PrimaryKeyRelatedField(write_only=True,
                                                source='car',
                                                queryset=Car.objects.all())

    price = serializers.IntegerField(read_only=True)

    class Meta:
        model = Rent
        fields = ('id',  'car',
                  'car_id', 'start', 'end', 'price')


class CreateRentalSerializer(serializers.ModelSerializer):
    car = CarSerializer(read_only=True)
    car_id = serializers.PrimaryKeyRelatedField(write_only=True,
                                                source='car',
                                                queryset=Car.objects.all())
    user = UserSerializer(read_only=True)
    user_id = serializers.PrimaryKeyRelatedField(write_only=True,
                                                 source='user',
                                                 queryset=User.objects.all())
    start = serializers.DateTimeField(format="%Y-%m-%dT%H:%M")
    end = serializers.DateTimeField(format="%Y-%m-%dT%H:%M")

    class Meta:
        model = Rent
        fields = ('id', 'user', 'user_id', 'car',
                  'car_id', 'start', 'end', 'price')


class GetAvailbleCarSerailizer(serializers.Serializer):
    car = CarSerializer(read_only=True)
    car_id = serializers.PrimaryKeyRelatedField(write_only=True,
                                                source='car',
                                                queryset=Car.objects.all())
    start = serializers.DateTimeField(format="%Y-%m-%dT%H:%M")
    end = serializers.DateTimeField(format="%Y-%m-%dT%H:%M")
    price = serializers.CharField()

    class Meta:
        model = Rent
        fields = ('car', 'price', 'start', 'end', 'car_id')


class PersonPerCarSerializer(serializers.ModelSerializer):
    car = CarSerializer(read_only=True)
    user = UserSerializer(read_only=True)
    start = serializers.DateTimeField(read_only=True)
    end = serializers.DateTimeField(read_only=True)

    class Meta:
        model = Rent
        fields = ('id', 'car', 'user', 'start', 'end')
