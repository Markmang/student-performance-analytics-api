from django.contrib import admin
from .models import Student, Course, Score, Attendance


@admin.register(Student)
class StudentAdmin(admin.ModelAdmin):
    list_display = ("id", "user", "class_name")
    search_fields = ("user__email",)


@admin.register(Course)
class CourseAdmin(admin.ModelAdmin):
    list_display = ("id", "name", "code")
    search_fields = ("name", "code")


@admin.register(Score)
class ScoreAdmin(admin.ModelAdmin):
    list_display = ("id", "student", "course", "score", "date")
    list_filter = ("course",)


@admin.register(Attendance)
class AttendanceAdmin(admin.ModelAdmin):
    list_display = ("id", "student", "date", "status")
    list_filter = ("status",)
