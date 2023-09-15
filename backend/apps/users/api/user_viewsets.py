from rest_framework import status
from rest_framework import viewsets
from rest_framework.response import Response
from apps.users.api.serializers import UserSerializer, UserListSerializer
from apps.users.models import User

class UserViewSet(viewsets.ModelViewSet):
    queryset = User.objects.filter(is_active=True).order_by('id')
    serializer_class = UserSerializer

    def get_queryset(self, pk=None):
        if pk is None:
            query = self.queryset.values('id', 'username', 'name', 'last_name', 'email',  'password')
            return query
        else:
            return self.queryset.filter(id=pk).first()

    def list(self, request):
        """
            Obtains the list of all active users in the application.
        """
        user_serializer = UserListSerializer(self.get_queryset(), many=True)
        return Response(user_serializer.data, status=status.HTTP_200_OK)

    def create(self, request):
        """
            Create a new user.
        """
        serializer = self.serializer_class(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response({'message': 'User create successfull'}, status= status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
    
    def update(self, request, pk=None):
        """
            Update the data of an existing user.
        """
        if self.get_queryset(pk):
            product_serializer = self.serializer_class(self.get_queryset(pk), data=request.data)
            if product_serializer.is_valid():
                product_serializer.save()
                return Response(product_serializer.data, status=status.HTTP_200_OK)
            return Response(product_serializer.errors, status=status.HTTP_400_BAD_REQUEST)
    
    def destroy(self, request, pk=None):
        """
            Deleting an existing user.
        """
        product =  self.get_queryset(pk)
        if product:
            product.is_active = False
            product.save()
            return Response({'message': 'User deleted successfull'}, status=status.HTTP_200_OK)
        return Response({'error': 'Do not exist this user'}, status=status.HTTP_400_BAD_REQUEST)