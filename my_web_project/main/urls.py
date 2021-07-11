from django.urls import path

from my_web_project.main.views import homeworks_list, homework_create, homework_details, homework_edit, homework_delete, \
    homework_comment

urlpatterns = [
    path('', homeworks_list, name='homeworks_list'),
    path('create/', homework_create, name='homework_create'),
    path('details/<int:pk>', homework_details, name='homework_details'),
    path('edit/<int:pk>', homework_edit, name='homework_edit'),
    path('delete/<int:pk>', homework_delete, name='homework_delete'),
    path('comment/<int:pk>', homework_comment, name='homework_comment'),

]
