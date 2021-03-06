from django.contrib.auth.decorators import login_required
from django.shortcuts import render, redirect

from my_web_project.common.forms import CommentForm
from my_web_project.core.decorators import group_required
from my_web_project.main.forms import HomeworkForm, HomeworkEditForm, HomeworkCheckForm
from my_web_project.main.models import Homework


@login_required()
def homeworks_list(request):
    homeworks = Homework.objects.all()
    user_id = request.user.id
    context = {
        'homeworks': homeworks,
        'user_id':user_id
    }

    return render(request, 'homework/homeworks_list.html', context)


@login_required()
def homeworks_my(request):
    homeworks = Homework.objects.all()
    context = {
        'homeworks': homeworks,
    }

    return render(request, 'homework/homeworks_my.html', context)


@group_required(['Student', ])
def homework_create(request):
    if request.method == 'POST':
        form = HomeworkForm(request.POST, request.FILES, )
        if form.is_valid():
            form.save()
            return redirect('homeworks_list')
    else:
        form = HomeworkForm(
            initial={
                'student': request.user.id,
            }
        )

    context = {
        'form': form,
    }

    return render(request, 'homework/homework_create.html', context)


def homework_details(request, pk):
    homework = Homework.objects.get(pk=pk)

    student_owner = homework.student_id == request.user.id
    assigned_teacher = homework.teacher_id == request.user.id

    context = {
        'homework': homework,
        'comment_form': CommentForm(
            initial={
                'homework_pk': pk,
            }
        ),
        'comments': homework.comment_set.all(),
        'student_owner': student_owner,
        'assigned_teacher': assigned_teacher,
    }

    return render(request, 'homework/homework_detail.html', context)


def homework_edit(request, pk):
    homework = Homework.objects.get(pk=pk)
    if request.method == 'POST':
        form = HomeworkEditForm(request.POST, request.FILES, instance=homework)
        if form.is_valid():
            form.save()
            return redirect('homeworks_list')
    else:
        form = HomeworkEditForm(instance=homework)

    context = {
        'form': form,
        'homework': homework,
    }

    return render(request, 'homework/homework_edit.html', context)


def homework_check(request, pk):
    homework = Homework.objects.get(pk=pk)
    if request.method == 'POST':
        form = HomeworkCheckForm(request.POST, request.FILES, instance=homework)
        if form.is_valid():
            form.save()
            return redirect('homeworks_list')
    else:
        form = HomeworkCheckForm(instance=homework)

    context = {
        'form': form,
        'homework': homework,
    }

    return render(request, 'homework/homework_check.html', context)


def homework_delete(request, pk):
    homework = Homework.objects.get(pk=pk)
    if request.method == 'POST':
        homework.delete()
        return redirect('homeworks_list')
    else:
        context = {
            'homework': homework,
        }
        return render(request, 'homework/homework_delete.html', context)


def homework_comment(request, pk):
    form = CommentForm(request.POST)
    if form.is_valid():
        comment = form.save(commit=False)
        comment.user = request.user
        comment.save()

    return redirect('homework_details', pk)
