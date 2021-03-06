from django.contrib.auth import get_user_model
from django.contrib.auth.models import Group
from django.test import TestCase, Client
from django.urls import reverse

from my_web_project.main.models import Homework, Student

UserModel = get_user_model()


class HomeworksListTests(TestCase):
    def setUp(self):
        self.client = Client()
        self.user = UserModel.objects.create_user(username='student101', password='q1w2e3r4!')
        self.group_student = Group(name='Student')
        self.group_student.save()
        self.user.groups.add(self.group_student)
        self.student = Student.objects.get(pk=1)

    def test_noUser_redirectLogToLogin(self):
        response = self.client.get(reverse('homeworks_list'))

        self.assertEqual(response.status_code, 302)

    def test_userLoggedIn_successful(self):
        self.client.force_login(self.user)

        response = self.client.get(reverse('homeworks_list'))

        self.assertEqual(response.status_code, 200)

    def test_student_CreateHomework_success(self):
        Homework.objects.create(
            title="My test homework",
            student=self.student,
            upload='homeworks/Homework-_History_1.docx'

        )


