import pandas as pd


def scores_to_dataframe(queryset):
    """Convert score queryset to DataFrame."""
    data = list(queryset.values("student_id", "course__name", "score", "date"))
    return pd.DataFrame(data)


def attendance_to_dataframe(queryset):
    """Convert attendance queryset to DataFrame."""
    data = list(queryset.values("student_id", "date", "status"))
    return pd.DataFrame(data)