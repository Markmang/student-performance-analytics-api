import pandas as pd
from records.models import Student, Score, Attendance
from .pandas_engine import scores_to_dataframe, attendance_to_dataframe
from .ml import train_model


class StudentAnalyticsService:
    """Handles student-level analytics."""

    @staticmethod
    def insights(student_id):
        student = Student.objects.get(id=student_id)
        df = scores_to_dataframe(student.scores.all())

        avg = df["score"].mean()
        best = df.groupby("course__name")["score"].mean().idxmax()
        worst = df.groupby("course__name")["score"].mean().idxmin()

        return {
            "average_score": round(avg, 2),
            "best_course": best,
            "weakest_course": worst,
        }

    @staticmethod
    def attendance_trend(student_id):
        student = Student.objects.get(id=student_id)
        df = attendance_to_dataframe(student.attendance.all())

        df["date"] = pd.to_datetime(df["date"])
        df["week"] = df["date"].dt.isocalendar().week

        grouped = df.groupby("week")["status"].apply(
            lambda x: (x == "present").sum() / len(x) * 100
        )

        return {
            "labels": list(grouped.index.astype(str)),
            "values": list(grouped.values),
        }

    @staticmethod
    def risk(student_id):
        student = Student.objects.get(id=student_id)

        score_df = scores_to_dataframe(student.scores.all())
        avg = score_df["score"].mean()

        attendance_df = attendance_to_dataframe(student.attendance.all())
        present = (attendance_df["status"] == "present").sum()
        rate = present / len(attendance_df) * 100

        risk = "HIGH" if avg < 50 or rate < 60 else "LOW"

        return {
            "average_score": avg,
            "attendance_rate": rate,
            "risk_level": risk,
        }

    @staticmethod
    def predict(student_id):
        student = Student.objects.get(id=student_id)

        score_df = scores_to_dataframe(student.scores.all())
        avg = score_df["score"].mean()

        attendance_df = attendance_to_dataframe(student.attendance.all())
        present = (attendance_df["status"] == "present").sum()
        rate = present / len(attendance_df) * 100

        model = train_model()
        prediction = model.predict([[avg, rate]])[0]

        return {
            "predicted_risk": "HIGH" if prediction == 1 else "LOW"
        }


class CourseAnalyticsService:
    """Handles course-level analytics."""

    @staticmethod
    def statistics():
        df = scores_to_dataframe(Score.objects.all())
        grouped = df.groupby("course__name")["score"].mean()

        return {
            "labels": list(grouped.index),
            "values": list(grouped.values),
        }

    @staticmethod
    def at_risk(course_name):
        df = scores_to_dataframe(
            Score.objects.filter(course__name=course_name)
        )

        grouped = df.groupby("student_id")["score"].mean()
        return list(grouped[grouped < 50].index)

    @staticmethod
    def best_students(course_name):
        df = scores_to_dataframe(
            Score.objects.filter(course__name=course_name)
        )

        grouped = df.groupby("student_id")["score"].mean()
        return list(grouped.sort_values(ascending=False).head(5).index)

    @staticmethod
    def attendance_trend(course_name):
        students = Student.objects.filter(
            scores__course__name=course_name
        ).distinct()

        attendance = []
        for s in students:
            attendance.extend(s.attendance.all())

        df = pd.DataFrame([
            {"date": a.date, "status": a.status}
            for a in attendance
        ])

        df["date"] = pd.to_datetime(df["date"])
        df["week"] = df["date"].dt.isocalendar().week

        grouped = df.groupby("week")["status"].apply(
            lambda x: (x == "present").sum() / len(x) * 100
        )

        return {
            "labels": list(grouped.index.astype(str)),
            "values": list(grouped.values),
        }


class GlobalAnalyticsService:
    """Handles system-wide analytics."""

    @staticmethod
    def attendance_trend():
        df = attendance_to_dataframe(Attendance.objects.all())

        df["date"] = pd.to_datetime(df["date"])
        df["week"] = df["date"].dt.isocalendar().week

        grouped = df.groupby("week")["status"].apply(
            lambda x: (x == "present").sum() / len(x) * 100
        )

        return {
            "labels": list(grouped.index.astype(str)),
            "values": list(grouped.values),
        }

    @staticmethod
    def best_students():
        df = scores_to_dataframe(Score.objects.all())
        grouped = df.groupby("student_id")["score"].mean()

        return list(grouped.sort_values(ascending=False).head(5).index)

    @staticmethod
    def at_risk_students():
        df = scores_to_dataframe(Score.objects.all())
        grouped = df.groupby("student_id")["score"].mean()

        return list(grouped[grouped < 50].index)