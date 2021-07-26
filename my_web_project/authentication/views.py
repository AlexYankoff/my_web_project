from django.contrib.auth import login, authenticate, logout
from django.contrib.auth.decorators import login_required
from django.contrib.auth.forms import UserCreationForm
from django.shortcuts import render, redirect

from my_web_project.authentication.forms import LoginForm, StudentForm, MyUserCreationForm, TeacherForm
from my_web_project.main.models import Student, Teacher


def index_page(request):
    return render(request, 'index.html')


def register_student(request):
    if request.method == 'GET':
        context = {
            # 'form': UserRegisterForm()
            'form': MyUserCreationForm(),
        }
        return render(request, 'authentication/register_user.html', context)
    else:

        form = MyUserCreationForm(request.POST)  # ползваме си built-in фомра

        if form.is_valid():
            user = form.save()
            user.groups.add(1)
            login(request, user)
            return redirect('index_page')

        context = {
            'form': MyUserCreationForm(request.POST)  # ako има грешки, покажи попълнената форма
        }
    return render(request, 'authentication/register_user.html', context)


def register_teacher(request):
    if request.method == 'GET':
        context = {
            'form': MyUserCreationForm(initial={
                'is_staff': True,}
            ),

        }

        return render(request, 'authentication/register_user.html', context)
    else:

        form = MyUserCreationForm(request.POST)  # ползваме си built-in фомра

        if form.is_valid():

            user = form.save(commit=False)
            user.is_staff= True
            user.save()
            user.groups.add(2)
            login(request, user)
            return redirect('index_page')

        context = {
            'form': MyUserCreationForm(request.POST)  # ako има грешки, покажи попълнената форма
        }
    return render(request, 'authentication/register_user.html', context)


def login_user(request):
    if request.method == 'POST':
        form = LoginForm(request.POST)
        if form.is_valid():
            user = form.save()
            login(request, user)
            return redirect('index_page')
    else:
        form = LoginForm()
    context = {
        'form': form,
    }
    return render(request, 'authentication/login.html', context)


def logout_user(request):
    logout(request)
    return redirect('index_page')


@login_required
def student_details(request):
    student = Student.objects.get(pk=request.user.id)
    if request.method == 'POST':
        form = StudentForm(request.POST, instance=student)
        if form.is_valid():
            form.save()
            return redirect('index_page')
    else:
        form = StudentForm(instance=student)

    context = {
        'form': form,
    }
    return render(request, 'authentication/student_details.html', context)


@login_required
def teacher_details(request):
    teacher = Teacher.objects.get(pk=request.user.id)
    if request.method == 'POST':
        form = TeacherForm(request.POST, instance=teacher)
        if form.is_valid():
            form.save()
            return redirect('index_page')
    else:
        form = TeacherForm(instance=teacher)

    context = {
        'form': form,
    }
    return render(request, 'authentication/student_details.html', context)