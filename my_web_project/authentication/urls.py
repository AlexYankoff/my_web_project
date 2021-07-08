from django.urls import path

from my_web_project.authentication.views import index_page

urlpatterns =[
    path('', index_page, name='index_page')
]