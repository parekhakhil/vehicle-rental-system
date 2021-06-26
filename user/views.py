from .models import User
from .serializers import UserSerializer, TokenSerializer
from rest_framework.generics import CreateAPIView, ListAPIView, RetrieveUpdateDestroyAPIView
from rest_framework.permissions import AllowAny, IsAuthenticated
from .permissions import CustomIsAdminUser
from .pagination import CustomPagination
from rest_framework.response import Response
from rest_framework import status
from django.contrib.auth import authenticate
from rest_framework.authtoken.models import Token
from rest_framework.views import APIView

# Create your views here.


class UserLoginView(APIView):
    def post(self, request, format='json'):
        mobile = request.data.get('mobile')
        password = request.data.get('password')
        if mobile is None or password is None:
            return Response({'error': 'Please provide both mobile and password'},
                            status=status.HTTP_400_BAD_REQUEST)
        user = authenticate(username=mobile, password=password)
        if not user:
            return Response({'error': 'You have entered an invalid mobile number or password.'},
                            status=status.HTTP_400_BAD_REQUEST)
        token, _ = Token.objects.get_or_create(user=user)
        serializer = TokenSerializer(token)
        # serializer = UserSerializer(user, many=True)

        return Response({"detail": serializer.data},
                        status=status.HTTP_200_OK)


class UserList(ListAPIView):
    serializer_class = UserSerializer
    queryset = User.objects.all()
    permission_classes = [CustomIsAdminUser]
    pagination_class = CustomPagination


class UserCreateView(CreateAPIView):
    serializer_class = UserSerializer
    queryset = User.objects.all()
    permission_classes = [AllowAny]


class UserDetailView(RetrieveUpdateDestroyAPIView):
    serializer_class = UserSerializer
    queryset = User.objects.all()
    permission_classes = [IsAuthenticated]


class UserLogoutView(APIView):
    permission_classes = [IsAuthenticated]

    def get(self, request):
        request.user.auth_token.delete()
        return Response({"status": True, 'detail': "ok"}, status=status.HTTP_200_OK)
