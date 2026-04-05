from django.urls import path
from .views import (
    StudentAnalyticsView,
    CourseAnalyticsView,
    GlobalAnalyticsView,
)

urlpatterns = [
    path("students/<int:student_id>/", StudentAnalyticsView.as_view()),
    path("courses/<str:course_name>/", CourseAnalyticsView.as_view()),
    path("overview/", GlobalAnalyticsView.as_view()),
]