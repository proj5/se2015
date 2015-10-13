from rest_framework import serializers

from users.models import UserAccount
from django.contrib.auth.models import User


class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ('username', 'email', 'password', 'first_name', 'last_name')
        lookup_field = 'username'


class UserAccountSerializer(serializers.ModelSerializer):
    user = UserSerializer()

    class Meta:
        model = UserAccount
        fields = ('user', 'school', 'class_in_school',
                  'created_at', 'updated_at')

        # lookup_field = 'user__username'
        read_only_fields = ('created_at', 'updated_at',)

    def create(self, validated_data):
        print("Attention Here <--------")
        return UserAccount.objects.create_user(validated_data)
