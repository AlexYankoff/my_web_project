from django.urls import path

from my_web_project.authentication.views import index_page, register_student, login_user, logout_user, register_user

urlpatterns =[
    path('', index_page, name='index_page'),
    path('registerstudent/', register_student, name ='register student'),
    path('login/', login_user, name='login user'),
    path('logout/', logout_user, name='logout user'),
    path('registeruser/',register_user, name='register user')
]