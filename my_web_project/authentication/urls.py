from django.urls import path

from my_web_project.authentication.views import index_page, login_user, logout_user, student_details, register_student, \
    register_teacher, teacher_details

urlpatterns =[
    path('', index_page, name='index_page'),
    path('registerstudent/', register_student, name ='register user'),
    path('registerteacher/',register_teacher, name ='register teacher'),
    path('login/', login_user, name='login user'),
    path('logout/', logout_user, name='logout user'),
    path('studentdetails/',student_details,name = 'student details'),
    path('teacherdetails/',teacher_details, name='teacher details'),
]