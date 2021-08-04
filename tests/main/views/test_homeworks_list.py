
from django.test import TestCase, Client
from django.urls import reverse
from unittest.mock import patch


class HomeworksListTests(TestCase):
    #@patch('my_web_project.main.models.Homework.objects')
    def test_example(self): #homework_mock as param
       # homework_mock.all.return_value = {
       #    'id':1,
       #    'student_id':2,
       #    'teacher_id':3,
       #    'title': 'Hoho',
       #    'status': 'Submitted',
       #    'upload':'homeworks/ho.doc',
       #}
       #ако подадем и  user_id ще можем да тестваме с мокването
        client = Client()
        client.login(username='student1', password='q1w2e3r41')
        response = client.get(reverse('homeworks_list'), user_id=1)
        pass
        self.assertEqual(response.status_code, 200)
