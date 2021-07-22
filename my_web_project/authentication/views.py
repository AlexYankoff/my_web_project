from django.contrib.auth import login, authenticate, logout
from django.contrib.auth.forms import UserCreationForm
from django.shortcuts import render, redirect

from my_web_project.authentication.forms import StudentRegisterForm, LoginForm, UserRegisterForm


def index_page(request):
    return render(request, 'index.html')


def register_student(request):
    if request.method == 'GET':
        context = {
            'form': StudentRegisterForm()
        }
        return render(request, 'authentication/register_student.html', context)
    else:
        form = StudentRegisterForm(request.POST)

        if form.is_valid():
            user = form.save()
            login(request, user)
            return redirect('index_page')

        context = {
            'form'  # ako има грешки, покажи попълнената форма
        }
    return render(request, 'authentication/register_student.html', context)


def register_user(request):
    if request.method == 'GET':
        context = {
            #'form': UserRegisterForm()
            'form': UserCreationForm(),
        }
        return render(request, 'authentication/register_student.html', context)
    else:
        #form = UserRegisterForm(request.POST)
        form = UserCreationForm(request.POST) # ползваме си built-in фомра

        if form.is_valid():
            user = form.save()
            user.groups.add(1)
            login(request, user)
            return redirect('index_page')

        context = {
            'form' : UserCreationForm(request.POST) # ako има грешки, покажи попълнената форма
        }
    return render(request, 'authentication/register_student.html', context)

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
    return render(request,'authentication/login.html', context)


def logout_user(request):
    logout(request)
    return redirect('index_page')
