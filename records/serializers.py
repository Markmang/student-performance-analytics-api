from rest_framework import serializers
from .models import Student, Course, Score, Attendance


class StudentSerializer(serializers.ModelSerializer):
    """Serializer for student profiles."""

    class Meta:
        model = Student
        fields = ["id", "user", "class_name"]


class CourseSerializer(serializers.ModelSerializer):
    """Serializer for courses."""

    class Meta:
        model = Course
        fields = ["id", "name", "code"]


class ScoreSerializer(serializers.ModelSerializer):
    """Serializer for student scores."""

    class Meta:
        model = Score
        fields = ["id", "student", "course", "score", "date"]


class AttendanceSerializer(serializers.ModelSerializer):
    """Serializer for attendance records."""

    class Meta:
        model = Attendance
        fields = ["id", "student", "date", "status"]