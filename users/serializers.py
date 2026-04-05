from rest_framework import serializers
from django.contrib.auth import get_user_model
from rest_framework_simplejwt.serializers import TokenObtainPairSerializer

User = get_user_model()


class RegisterSerializer(serializers.ModelSerializer):
    """
    Serializer for user registration.

    - Accepts: email, username, password, role
    - Prevents registration as ADMIN (security measure)
    - Hashes password before saving user
    - Creates and returns a new user instance

    Validation:
        - role must not be ADMIN

    Output:
        - user instance (without password)
    """
    password = serializers.CharField(write_only=True)

    class Meta:
        model = User
        fields = ["id", "email", "username", "password", "role"]

    def validate_role(self, value):
        if value == "ADMIN":
            raise serializers.ValidationError("Cannot register as admin.")
        return value

    def create(self, validated_data):
        password = validated_data.pop("password")
        user = User(**validated_data)
        user.set_password(password)  # ensures password is hashed
        user.save()
        return user


class UserSerializer(serializers.ModelSerializer):
    """
    Serializer for representing user data.

    - Used for returning user details in responses
    - Excludes sensitive fields like password

    Output:
        - id
        - email
        - username
        - role
    """
    class Meta:
        model = User
        fields = ["id", "email", "username", "role"]


class CustomTokenSerializer(TokenObtainPairSerializer):
    """
    Custom JWT token serializer.

    - Extends SimpleJWT TokenObtainPairSerializer
    - Adds user information to the token response
    - Used during login

    Input:
        - email
        - password

    Output:
        - access token
        - refresh token
        - user details (email, role)
    """

    def validate(self, attrs):
        data = super().validate(attrs)

        # Add custom user data to response
        data["user"] = {
            "email": self.user.email,
            "role": self.user.role,
        }

        return data