from rest_framework import serializers
from .models import User
from rest_framework.authtoken.models import Token


class UserSerializer(serializers.ModelSerializer):
    status = serializers.CharField(read_only=True)
    password = serializers.CharField(write_only=True)
    confirm_password = serializers.CharField(
        write_only=True, allow_blank=False)

    def create(self, validated_data):
        user = User.objects.create_user(
            name=validated_data.get('name'),
            mobile=validated_data.get('mobile'),
            email=validated_data.get('email'),
            password=validated_data.get('password'),
            confirm_password=validated_data.get('confirm_password'))
        return user

    class Meta:
        model = User
        fields = [ 'id', 'name', 'email', 'mobile',
                  'status', 'password', 'confirm_password']


class TokenSerializer(serializers.ModelSerializer):

    user = UserSerializer(many=False, read_only=True)

    class Meta:
        model = Token
        fields = ('key', 'user')
