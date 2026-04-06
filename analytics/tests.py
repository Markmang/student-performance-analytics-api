from django.urls import reverse
from rest_framework.test import APITestCase
from rest_framework import status
from django.contrib.auth import get_user_model

from records.models import Student, Course, Score, Attendance
from datetime import date
import random

User = get_user_model()


class AnalyticsTestCase(APITestCase):
    """
    Tests core analytics functionality:
    - Student analytics endpoint
    - Course analytics endpoint
    - Global analytics endpoint
    """

    def setUp(self):
        # Create user and authenticate
        self.user = User.objects.create_user(
            email="testuser@mail.com",
            username="testuser",
            password="testpass123",
            role="ADMIN"
        )

        self.client.force_authenticate(user=self.user)

        # Create student
        student_user = User.objects.create_user(
            email="student@test.com",
            username="student",
            password="testpass123",
            role="STUDENT"
        )
        self.student = student_user.student_profile

        # Create course
        self.course = Course.objects.create(
            name="Mathematics",
            code="MTH101"
        )

        # Create scores
        for _ in range(5):
            Score.objects.create(
                student=self.student,
                course=self.course,
                score=random.randint(40, 90)
            )

        # Create attendance
        for i in range(10):
            Attendance.objects.create(
                student=self.student,
                date=date.today(),
                status=random.choice(["present", "absent"])
            )

    def test_student_analytics_endpoint(self):
        """Test student analytics aggregation endpoint."""
        url = f"/api/analytics/students/{self.student.id}/"
        response = self.client.get(url)

        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertIn("insights", response.data)
        self.assertIn("risk", response.data)
        self.assertIn("prediction", response.data)
        self.assertIn("attendance_trend", response.data)

    def test_course_analytics_endpoint(self):
        """Test course analytics endpoint."""
        url = f"/api/analytics/courses/{self.course.name}/"
        response = self.client.get(url)

        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertIn("statistics", response.data)
        self.assertIn("best_students", response.data)
        self.assertIn("at_risk_students", response.data)

    def test_global_analytics_endpoint(self):
        """Test global analytics endpoint."""
        url = "/api/analytics/overview/"
        response = self.client.get(url)

        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertIn("attendance_trend", response.data)
        self.assertIn("best_students", response.data)
        self.assertIn("at_risk_students", response.data)