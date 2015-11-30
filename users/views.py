import json

from django.contrib.auth import authenticate, login, logout
from django.contrib.auth import update_session_auth_hash

from rest_framework import permissions, status, views
from rest_framework.response import Response

from users.models import UserAccount, User
from users.permissions import IsAccountOwner
from users.serializers import UserAccountSerializer, UserSerializer


class UserListView(views.APIView):

    def get_permissions(self):
        if self.request.method in permissions.SAFE_METHODS:
            return (permissions.AllowAny(),)

        if self.request.method == 'POST':
            return (permissions.AllowAny(),)

        return (permissions.IsAuthenticated())

    # Handel GET request to get list of all users
    def get(self, request, format=None):
        users = UserAccount.objects.all()
        serializer = UserAccountSerializer(users, many=True)
        return Response(serializer.data)

    # Handel POST request to create new users
    def post(self, request, format=None):
        serializer = UserAccountSerializer(data=request.data)

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


class UserDetailView(views.APIView):

    def get_permissions(self):
        if self.request.method in permissions.SAFE_METHODS:
            return (permissions.AllowAny(),)

        return (permissions.IsAuthenticated(), IsAccountOwner(),)

    def get_object(self, username):
        return UserAccount.objects.get(user__username=username)

    # Handel GET request to get a specific user
    def get(self, request, username, format=None):
        try:
            user = self.get_object(username)
            serializer = UserAccountSerializer(user)
            return Response(serializer.data)
        except:
            return Response(status=status.HTTP_404_NOT_FOUND)

    # Handle PUT request to update user profile
    def put(self, request, username, format=None):
        data = UserAccountSerializer(data=request.data).data

        user = User.objects.get(username=username)
        user_serializer = UserSerializer(user,
                                         data=data['user'])

        if user_serializer.is_valid():
            user_serializer.save()

            account = self.get_object(username)
            account.school = data.get('school')
            account.class_in_school = data.get('class_in_school')
            account.save()

            update_session_auth_hash(request, user)

            return Response(UserAccountSerializer(account).data)

        return Response(user_serializer.errors,
                        status=status.HTTP_400_BAD_REQUEST)

    # Handle DELETE request
    def delete(self, request, username, format=None):
        user_account = self.get_object(username)
        user_account.delete()
        user = User.objects.get(username=username)
        user.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)


class LoginView(views.APIView):

    # Handle POST request to login a user
    def post(self, request, format=None):
        data = json.loads(request.body)

        username = data.get('username', None)
        password = data.get('password', None)

        account = authenticate(username=username, password=password)

        if account is not None:
            if account.is_active:
                login(request, account)

                serialized = UserSerializer(account)

                return Response(serialized.data)
            else:
                return Response({
                    'status': 'Unauthorized',
                    'message': 'This account has been disabled.'
                }, status=status.HTTP_401_UNAUTHORIZED)
        else:
            return Response({
                'status': 'Unauthorized',
                'message': 'Username/password combination invalid.'
            }, status=status.HTTP_401_UNAUTHORIZED)


class LogoutView(views.APIView):
    permission_classes = (permissions.IsAuthenticated,)

    # Handle POST request to logout a user
    def post(self, request, format=None):
        logout(request)

        return Response({}, status=status.HTTP_204_NO_CONTENT)
