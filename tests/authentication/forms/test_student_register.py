from django.test import TestCase

from my_web_project.authentication.forms import  MyUserCreationForm


class StudentTests(TestCase):
    def test_studentRegisterForm_whenValid(self):
        data = {
            'username': 'student44',
            'password1': 'q1w2e3r4!',
            'password2': 'q1w2e3r4!',

        }

        form = MyUserCreationForm(data)

        self.assertTrue(form.is_valid())

    def test_studentRegisterForm_whenPasswordValidationFail(self):
        data = {
            'username': 'student44',
            'password1': 'q1',
            'password2': 'q1',

        }

        form = MyUserCreationForm(data)

        self.assertFalse(form.is_valid())

    def test_studentRegisterForm_whenPasswordsNotMatch(self):
        data = {
            'username': 'student44',
            'password1': 'q1w2e3r4!',
            'password2': '11w2e3r4!',

        }

        form = MyUserCreationForm(data)

        self.assertFalse(form.is_valid())


