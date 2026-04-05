from django.db import models
from django.conf import settings

User = settings.AUTH_USER_MODEL


class Student(models.Model):
    """
    Represents a student profile linked to a user with STUDENT role.
    Created automatically via signal when a user registers as a student.
    """
    user = models.OneToOneField(
        User,
        on_delete=models.CASCADE,
        related_name="student_profile"
    )
    class_name = models.CharField(max_length=50)

    def __str__(self):
        return self.user.email


class Course(models.Model):
    """
    Represents a course or subject offered in the system.
    """
    name = models.CharField(max_length=100)
    code = models.CharField(max_length=20, unique=True)

    def __str__(self):
        return f"{self.name} ({self.code})"


class Score(models.Model):
    """
    Stores a student's score for a specific course.
    Supports multiple records for trend and performance analysis.
    """
    student = models.ForeignKey(
        Student,
        on_delete=models.CASCADE,
        related_name="scores"
    )
    course = models.ForeignKey(
        Course,
        on_delete=models.CASCADE,
        related_name="scores"
    )
    score = models.FloatField()
    date = models.DateField(auto_now_add=True)

    def __str__(self):
        return f"{self.student} - {self.course} - {self.score}"


class Attendance(models.Model):
    """
    Tracks student attendance records over time.
    Used for attendance trends and risk analysis.
    """
    STATUS_CHOICES = (
        ("present", "Present"),
        ("absent", "Absent"),
    )

    student = models.ForeignKey(
        Student,
        on_delete=models.CASCADE,
        related_name="attendance"
    )
    date = models.DateField()
    status = models.CharField(max_length=10, choices=STATUS_CHOICES)

    def __str__(self):
        return f"{self.student} - {self.date} - {self.status}"