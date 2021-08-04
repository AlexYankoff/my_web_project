from django.test import TestCase, Client
from django.urls import reverse


class IndexTests(TestCase):
    def test_example(self):
        client = Client()
        response = client.get(reverse('index_page'))
        self.assertTemplateUsed(response,'index.html')