from django.db import models


class Student(models.Model):
    first_name = models.CharField(max_length=20)
    last_name = models.CharField(max_length=20)
    school_class = models.CharField(max_length=3)

    def __str__(self):
        return f'{self.first_name} {self.last_name} - {self.school_class}'


class Teacher(models.Model):
    first_name = models.CharField(max_length=20)
    last_name = models.CharField(max_length=20)
    subject = models.CharField(max_length=30)

    def __str__(self):
        return f'{self.first_name} {self.last_name} - {self.subject}'


class Homework(models.Model):

    STATUS_CHOICES =(
        ('Completed', 'Completed'),
        ('Submitted', 'Submitted'),
        ('Canceled', 'Canceled')
    )


    title = models.CharField(max_length=30)
    student = models.ForeignKey(Student, on_delete=models.CASCADE)
    teacher = models.ForeignKey(Teacher, on_delete=models.CASCADE)
    image = models.ImageField(
        upload_to = 'pets',
    )
    score = models.FloatField(blank=True,null=True)
    status = models.CharField(
        max_length=10,
        choices=STATUS_CHOICES,
        default='Submitted'
            )


class Comment(models.Model):
    comment = models.TextField()
    homework = models.ForeignKey(Homework, on_delete=models.CASCADE)



