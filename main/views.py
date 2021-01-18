from django.shortcuts import render
from .models import ToDo

# Create your views here.


def homepage(request):
    todo_list = ToDo.objects.all()
    return render(request, 'index.html', {"todo_list": todo_list})


def test(request):
    todo_list = ToDo.objects.all()
    return render(request, 'test.html', {"todo_list": todo_list})


def third(request):
    return render(request, 'test3.html')


def add(request):
    return render(request, 'add.html')


def update(request):
    return render(request, 'update.html')


def delete(request):
    return render(request, 'delete.html')
