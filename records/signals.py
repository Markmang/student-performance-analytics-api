from django.db.models.signals import post_save
from django.dispatch import receiver
from django.contrib.auth import get_user_model

from .models import Student

User = get_user_model()


@receiver(post_save, sender=User)
def manage_student_profile(sender, instance, created, **kwargs):
    """
    Ensures that any user with role STUDENT has a Student profile.

    - Creates profile on user creation
    - Creates profile if role is changed to STUDENT
    - Prevents duplicate profiles
    """

    if instance.role == "STUDENT":
        Student.objects.get_or_create(
            user=instance,
            defaults={"class_name": "SS1"}
        )