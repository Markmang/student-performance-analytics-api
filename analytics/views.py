from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework.permissions import IsAuthenticated
from rest_framework import status

from .services import (
    StudentAnalyticsService,
    CourseAnalyticsService,
    GlobalAnalyticsService,
)


class StudentAnalyticsView(APIView):
    """
    Return all analytics for a specific student.
    """
    permission_classes = [IsAuthenticated]

    def get(self, request, student_id):
        data = {
            "insights": StudentAnalyticsService.insights(student_id),
            "risk": StudentAnalyticsService.risk(student_id),
            "prediction": StudentAnalyticsService.predict(student_id),
            "attendance_trend": StudentAnalyticsService.attendance_trend(student_id),
        }

        return Response(data, status=status.HTTP_200_OK)


class CourseAnalyticsView(APIView):
    """
    Return all analytics for a specific course.
    """
    permission_classes = [IsAuthenticated]

    def get(self, request, course_name):
        data = {
            "statistics": CourseAnalyticsService.statistics(),
            "at_risk_students": CourseAnalyticsService.at_risk(course_name),
            "best_students": CourseAnalyticsService.best_students(course_name),
            "attendance_trend": CourseAnalyticsService.attendance_trend(course_name),
        }

        return Response(data, status=status.HTTP_200_OK)


class GlobalAnalyticsView(APIView):
    """
    Return overall system analytics.
    """
    permission_classes = [IsAuthenticated]

    def get(self, request):
        data = {
            "attendance_trend": GlobalAnalyticsService.attendance_trend(),
            "best_students": GlobalAnalyticsService.best_students(),
            "at_risk_students": GlobalAnalyticsService.at_risk_students(),
        }

        return Response(data, status=status.HTTP_200_OK)