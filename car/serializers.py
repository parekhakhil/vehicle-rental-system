from rest_framework import serializers
from .models import Car, Company


class CompanySerializer(serializers.ModelSerializer):
    class Meta:
        model = Company
        fields = ['id', 'name']


class CarSerializer(serializers.ModelSerializer):
    company = CompanySerializer(read_only=True)
    company_id = serializers.PrimaryKeyRelatedField(write_only=True,
                                                    source='company',
                                                    queryset=Company.objects.all())

    class Meta:
        model = Car
        fields = ('id', 'model', 'licence_number', 'company',
                  'base_price', 'price_per_hour', 'deposit', 'company_id')
