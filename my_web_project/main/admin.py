from django.contrib import admin

# Register your models here.
from my_web_project.main.models import Student, Teacher, Homework, Comment


class StudentAdmin(admin.ModelAdmin):
    list_display = ['first_name', 'last_name', 'school_class']
    list_filter = ['school_class']


class TeacherAdmin(admin.ModelAdmin):
    list_display = ['first_name', 'last_name', 'subject']
    list_filter = ['subject']


class HomeworkAdmin(admin.ModelAdmin):
    list_display = ['title', 'student', 'teacher','image', 'score', 'status']
    list_filter = ['teacher','student']


admin.site.register(Student, StudentAdmin)
admin.site.register(Teacher, TeacherAdmin)
admin.site.register(Homework, HomeworkAdmin)
admin.site.register(Comment)
