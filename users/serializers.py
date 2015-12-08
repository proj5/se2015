from rest_framework import serializers

from users.models import UserAccount
# from django.contrib.auth.models import User


class UserSerializer(serializers.Serializer):
    password = serializers.CharField(write_only=True, required=False)
    confirm_password = serializers.CharField(write_only=True, required=False)
    email = serializers.EmailField()
    username = serializers.CharField(max_length=20)
    first_name = serializers.CharField(max_length=100)

    lookup_field = 'username'

    def update(self, instance, validated_data):
        instance.email = validated_data.get('email', instance.email)
        instance.first_name = validated_data.get('first_name',
                                                 instance.first_name)
        instance.save()

        password = validated_data.get('password', None)
        confirm_password = validated_data.get('confirm_password', None)

        if password and confirm_password and password == confirm_password:
            instance.set_password(password)
            instance.save()

        return instance


class UserAccountSerializer(serializers.ModelSerializer):
    user = UserSerializer()

    class Meta:
        model = UserAccount
        fields = (
            'id', 'user', 'school', 'class_in_school',
            # enable this line when client update this
            # 'facebook_id', 'avatar',
            'created_at', 'updated_at'
        )

        read_only_fields = ('created_at', 'updated_at',)


class AvatarSerializer(serializers.ModelSerializer):

    class Meta:
        model = UserAccount
        fields = ('avatar',)
