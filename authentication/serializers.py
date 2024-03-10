from rest_framework import serializers
from authentication.models import User
from django.contrib.auth import authenticate


class RegistrationSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ('name', 'surname', 'login', 'password', 'token',)

    password = serializers.CharField(
        max_length=128,
        min_length=8,
        write_only=True
    )
    token = serializers.CharField(max_length=255, read_only=True)

    def create(self, validated_data):
        return User.objects.create_user(**validated_data)


class LoginSerializer(serializers.Serializer):
    login = serializers.CharField(max_length=100)
    password = serializers.CharField(
        max_length=128,
        min_length=8
    )
    token = serializers.CharField(max_length=255, read_only=True)

    def validate(self, data):
        login = data.get('login', None)
        password = data.get('password', None)

        if login is None:
            raise serializers.ValidationError(
                'Login is required to log in.'
            )

        if password is None:
            raise serializers.ValidationError(
                'A password is required to log in.'
            )

        user = authenticate(username=login, password=password)

        if user is None:
            raise serializers.ValidationError(
                'A user with this login and password was not found.'
            )

        if not user.is_active:
            raise serializers.ValidationError(
                'This user has been deactivated.'
            )

        return {
            'login': user.login,
            'token': user.token
        }


class UserSerializer(serializers.ModelSerializer):

    password = serializers.CharField(
        max_length=128,
        min_length=8,
        write_only=True
    )

    class Meta:
        model = User
        fields = '__all__'

        read_only_fields = ('token',)

    def update(self, instance, validated_data):

        password = validated_data.pop('password', None)
        validated_data.pop('groups', None)
        validated_data.pop('user_permissions', None)

        for key, value in validated_data.items():
            setattr(instance, key, value)

        if password is not None:
            instance.set_password(password)

        instance.save()

        return instance
