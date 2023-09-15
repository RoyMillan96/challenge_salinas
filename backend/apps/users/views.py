
from django.contrib.auth import authenticate
from rest_framework import status
from rest_framework.response import Response
from rest_framework.generics import GenericAPIView
from rest_framework_simplejwt.views import TokenObtainPairView
from rest_framework_simplejwt.tokens import RefreshToken

from apps.users.api.serializers import (
    CustomTokenObtainPairSerializer, CustomUserSerializer,
    LogoutSerializer
)

from apps.users.models import User

class Login(TokenObtainPairView):
    serializer_class = CustomTokenObtainPairSerializer

    def post(self, request, *args, **kwargs):
        """
            Takes the user's credentials to log in and returns the access token to requests.
        """
        username = request.data.get('username', '')
        password = request.data.get('password', '')
        user = authenticate(username=username, password=password)
        if user:
            login_serializer = self.serializer_class(data=request.data)
            if login_serializer.is_valid():
                user_serializer = CustomUserSerializer(user)
                return Response(
                    {
                    'token': login_serializer.validated_data.get('access'),
                    'refresh-token': login_serializer.validated_data.get('refresh'),
                    'user': user_serializer.data,
                    'message': 'Login successfull'
                    }, 
                    status=status.HTTP_200_OK
                )
            return Response({'error': 'Data invalid'}, status=status.HTTP_400_BAD_REQUEST)
        return Response({'error': 'Data invalid'}, status=status.HTTP_400_BAD_REQUEST)


class Logout(GenericAPIView):
    serializer_class = LogoutSerializer

    def post(self, request, *args, **kwargs):
        """
            Closes the user's session and prevents requests if not logged in.
        """
        user_id = request.data.get('user')
        user = User.objects.filter(id=user_id)
        if user.exists():
            RefreshToken.for_user(user.first())
            return Response({'message': 'Logout successfull'}, status=status.HTTP_200_OK)
        return Response({'error': 'User does not exist'}, status=status.HTTP_400_BAD_REQUEST)