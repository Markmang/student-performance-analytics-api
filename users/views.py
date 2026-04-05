from rest_framework import generics, status
from rest_framework.response import Response
from rest_framework.permissions import AllowAny, IsAuthenticated
from rest_framework_simplejwt.tokens import RefreshToken
from rest_framework_simplejwt.views import TokenObtainPairView
from rest_framework.views import APIView

from .serializers import RegisterSerializer, UserSerializer, CustomTokenSerializer
from django.contrib.auth import get_user_model

User = get_user_model()


class RegisterView(generics.CreateAPIView):
    """
    Handles user registration.

    - Allows public access (no authentication required)
    - Creates a new user (STUDENT or TEACHER only)
    - Automatically generates JWT tokens upon successful registration
    - Returns user data along with access and refresh tokens

    Response:
        201 CREATED on success
    """
    queryset = User.objects.all()
    serializer_class = RegisterSerializer
    permission_classes = [AllowAny]

    def create(self, request, *args, **kwargs):
        serializer = self.get_serializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        user = serializer.save()

    
        refresh = RefreshToken.for_user(user)

        return Response(
            {
                "user": UserSerializer(user).data,
                "access": str(refresh.access_token),
                "refresh": str(refresh),
            },
            status=status.HTTP_201_CREATED  
        )


class LoginView(TokenObtainPairView):
    """
    Handles user authentication (login).

    - Accepts email and password
    - Returns JWT access and refresh tokens
    - Uses custom serializer to include user details in response

    Response:
        200 OK on success
    """
    serializer_class = CustomTokenSerializer


class MeView(APIView):
    """
    Returns the currently authenticated user's details.

    - Requires authentication (JWT or session)
    - Used to fetch logged-in user profile info

    Endpoint:
        GET /api/users/me/

    Response:
        200 OK with user data
    """
    permission_classes = [IsAuthenticated]

    def get(self, request):
        return Response(UserSerializer(request.user).data, status=status.HTTP_200_OK)