from django.test import TestCase, Client
from django.urls import reverse


class IndexTests(TestCase):
    def test_ifTempateIs_Correct(self):
        client = Client()
        response = client.get(reverse('index_page'))
        self.assertTemplateUsed(response,'index.html')