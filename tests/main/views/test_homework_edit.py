from django.contrib.auth import get_user_model
from django.contrib.auth.models import Group
from django.test import TestCase, Client


from my_web_project.main.models import Homework, Student, Teacher

UserModel = get_user_model()


class HomeworkEditTests(TestCase):
    def setUp(self):
        self.client = Client()
        self.user = UserModel.objects.create_user(username='student101', password='q1w2e3r4!')
        self.group_student = Group(name='Student')
        self.group_student.save()
        self.user.groups.add(self.group_student)
        self.student = Student.objects.get(pk=1)

        Homework.objects.create(
            title="My test homework",
            student=self.student,
            upload='homeworks/Homework-_History_1.docx'

        )


    def test_homeworkEditOpening_successful(self):
        self.client.force_login(self.user)

        response = self.client.get('/homeworks/edit/1')

        self.assertEqual(response.status_code, 200)


