from django.urls import path

from my_web_project.authentication.views import index_page, login_user, logout_user, student_details, register_user

urlpatterns =[
    path('', index_page, name='index_page'),
    path('registeruser/', register_user, name ='register user'),
    path('login/', login_user, name='login user'),
    path('logout/', logout_user, name='logout user'),
    path('studentdetails/',student_details,name = 'student details'),
]