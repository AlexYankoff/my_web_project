from django.contrib.auth.models import User
from django.core.validators import MinValueValidator, MaxValueValidator
from django.db import models


class Student(models.Model):
    first_name = models.CharField(
        max_length=20,
        blank= True,)
    last_name = models.CharField(
        max_length=20,
        blank= True,)
    school_class = models.CharField(
        max_length=3,
        blank= True)

    user = models.OneToOneField(
        User,
        on_delete=models.CASCADE,
        primary_key= True, #user го правим на primary_key
        )

    is_complete = models.BooleanField(
        default=False,
    )

    def __str__(self):
        return f'{self.first_name} {self.last_name} - {self.school_class}'


class Teacher(models.Model):
    first_name = models.CharField(max_length=20)
    last_name = models.CharField(max_length=20)
    subject = models.CharField(max_length=30)

    user = models.OneToOneField(
        User,
        on_delete=models.CASCADE,
        primary_key= True, #user го правим на primary_key
        )

    is_complete = models.BooleanField(
        default=False,)

    def __str__(self):
        return f'{self.first_name} {self.last_name} - {self.subject}'


class Homework(models.Model):

    STATUS_CHOICES =(
        ('Submitted', 'Submitted'),
        ('Checked', 'Checked'),
        ('Canceled', 'Canceled')
    )


    title = models.CharField(max_length=30)
    student = models.ForeignKey(Student, on_delete=models.CASCADE)
    teacher = models.ForeignKey(Teacher, on_delete=models.CASCADE)
    upload = models.FileField(upload_to='homeworks/')

    score = models.FloatField(blank=True, null=True,
                              validators=[MinValueValidator(2.0), MaxValueValidator(6.0)])
    status = models.CharField(
        max_length=10,
        choices=STATUS_CHOICES,
        default='Submitted'
            )


class Comment(models.Model):
    comment = models.TextField()
    homework = models.ForeignKey(Homework, on_delete=models.CASCADE)

    user = models.ForeignKey(
        User,
        on_delete=models.CASCADE,
        )



