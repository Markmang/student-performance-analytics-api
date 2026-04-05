from rest_framework import generics, status
from rest_framework.response import Response
from rest_framework.permissions import IsAuthenticated

from .models import Student, Course, Score, Attendance
from .serializers import (
    StudentSerializer,
    CourseSerializer,
    ScoreSerializer,
    AttendanceSerializer,
)
from .permissions import IsAdmin, IsTeacherOrAdmin


class StudentListView(generics.ListAPIView):
    """List all students."""
    queryset = Student.objects.all()
    serializer_class = StudentSerializer
    permission_classes = [IsAuthenticated]


class CourseCreateView(generics.CreateAPIView):
    """Create a course (admin only)."""
    queryset = Course.objects.all()
    serializer_class = CourseSerializer
    permission_classes = [IsAdmin]
    

    def create(self, request, *args, **kwargs):
        serializer = self.get_serializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        serializer.save()
        return Response(serializer.data, status=status.HTTP_201_CREATED)


class CourseListView(generics.ListAPIView):
    """List all courses."""
    queryset = Course.objects.all()
    serializer_class = CourseSerializer
    permission_classes = [IsAuthenticated]


class ScoreCreateView(generics.CreateAPIView):
    """Add score (teacher/admin only)."""
    queryset = Score.objects.all()
    serializer_class = ScoreSerializer
    permission_classes = [IsTeacherOrAdmin]

    def create(self, request, *args, **kwargs):
        serializer = self.get_serializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        serializer.save()
        return Response(serializer.data, status=status.HTTP_201_CREATED)


class AttendanceCreateView(generics.CreateAPIView):
    """Mark attendance (teacher/admin only)."""
    queryset = Attendance.objects.all()
    serializer_class = AttendanceSerializer
    permission_classes = [IsTeacherOrAdmin]

    def create(self, request, *args, **kwargs):
        serializer = self.get_serializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        serializer.save()
        return Response(serializer.data, status=status.HTTP_201_CREATED)