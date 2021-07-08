from django.urls import path

from my_web_project.main.views import list_homeworks

urlpatterns = [
    path('', list_homeworks, name='list_homeworks')

]
