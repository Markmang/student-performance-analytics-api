import os
import django
import random
from datetime import date, timedelta

os.environ.setdefault("DJANGO_SETTINGS_MODULE", "config.settings")
django.setup()

from django.contrib.auth import get_user_model
from records.models import Student, Course, Score, Attendance

User = get_user_model()


# -----------------------------
# CREATE COURSES
# -----------------------------
courses = []
course_data = [
    ("Mathematics", "MTH101"),
    ("Physics", "PHY101"),
    ("Chemistry", "CHM101"),
    ("Biology", "BIO101"),
]

for name, code in course_data:
    course, _ = Course.objects.get_or_create(name=name, code=code)
    courses.append(course)


# -----------------------------
# CREATE STUDENTS
# -----------------------------
students = []

for i in range(25):
    email = f"student{i}@mail.com"

    if not User.objects.filter(email=email).exists():
        user = User.objects.create_user(
            email=email,
            username=f"student{i}",
            password="123456",
            role="STUDENT"
        )
    else:
        user = User.objects.get(email=email)

    if hasattr(user, "student_profile"):
        students.append(user.student_profile)


# -----------------------------
# GENERATE SCORES
# -----------------------------
for student in students:
    for course in courses:
        existing_scores = Score.objects.filter(
            student=student,
            course=course
        ).count()

        if existing_scores < 5:
            for _ in range(5 - existing_scores):
                Score.objects.create(
                    student=student,
                    course=course,
                    score=random.randint(20, 100)
                )


# -----------------------------
# GENERATE ATTENDANCE
# -----------------------------
for student in students:
    existing_days = Attendance.objects.filter(student=student).count()

    if existing_days < 30:
        for i in range(30 - existing_days):
            Attendance.objects.create(
                student=student,
                date=date.today() - timedelta(days=i),
                status=random.choice(["present", "absent"])
            )


print("Seeding complete and safe")