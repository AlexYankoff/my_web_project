from django.contrib.auth import get_user_model
from django.db.models.signals import post_save, pre_save
from django.dispatch import receiver
from django.shortcuts import redirect

from my_web_project.main.models import Student, Teacher

UserModel = get_user_model()


@receiver(post_save, sender=UserModel)
def user_created(sender, instance, created, **kwargs):
    if created:
        if not instance.is_staff:
            student = Student(
                user=instance,
            )
            student.save()
            return redirect('index_page')

        else:
            teacher = Teacher(
                user=instance,
            )
            teacher.save()
            return redirect('index_page')

@receiver(pre_save, sender=Student)
def check_is_complete(sender, instance, **kwargs):
    if instance.first_name and instance.last_name and instance.school_class:
        instance.is_complete = True
