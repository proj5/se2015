from rest_framework import permissions, status, viewsets
from rest_framework.response import Response

from users.models import UserAccount
from users.permissions import IsAccountOwner
from users.serializers import UserAccountSerializer


class UserAccountViewSet(viewsets.ModelViewSet):
    queryset = UserAccount.objects.all()
    serializer_class = UserAccountSerializer
    lookup_field = 'user__username'

    def get_permissions(self):
        if self.request.method in permissions.SAFE_METHODS:
            return (permissions.AllowAny(),)

        if self.request.method == 'POST':
            return (permissions.AllowAny(),)

        return (permissions.IsAuthenticated(), IsAccountOwner(),)

    def create(self, request):
        serializer = self.serializer_class(data=request.data)

        print(request.data)

        if serializer.is_valid():
            data = serializer.validated_data['user']

            username = data.get('username')
            email = data.get('email')
            password = data.get('password')

            UserAccount.objects.create_user(username, email, password,
                                            **serializer.validated_data)

            return Response(serializer.validated_data,
                            status=status.HTTP_201_CREATED)

        return Response({
            'status': 'Bad request',
            'message': 'Account could not be created with received data.'
        }, status=status.HTTP_400_BAD_REQUEST)
