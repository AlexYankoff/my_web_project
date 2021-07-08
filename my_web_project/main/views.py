from django.shortcuts import render


def list_homeworks(request):
    return render(request, 'list_homeworks.html')
