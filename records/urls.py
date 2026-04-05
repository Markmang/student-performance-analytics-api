from django.urls import path
from .views import (
    StudentListView,
    CourseCreateView,
    CourseListView,
    ScoreCreateView,
    AttendanceCreateView,
)

urlpatterns = [
    path("students/", StudentListView.as_view()),
    path("courses/", CourseCreateView.as_view()),
    path("courses/list/", CourseListView.as_view()),
    path("scores/", ScoreCreateView.as_view()),
    path("attendance/", AttendanceCreateView.as_view()),
]