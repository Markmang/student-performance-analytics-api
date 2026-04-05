from django.urls import path
from .views import RegisterView, LoginView, MeView

urlpatterns = [
    path("api/auth/register/", RegisterView.as_view()),
    path("api/auth/login/", LoginView.as_view()),
    path("api/users/me/", MeView.as_view()),
]