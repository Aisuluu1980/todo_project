from django.shortcuts import render, redirect
from .models import ToDo

# Create your views here.


def homepage(request):
    todo_list = ToDo.objects.all()
    return render(request, 'index.html', {"todo_list": todo_list})


# def test(request):
#     todo_list = ToDo.objects.all()
#     return render(request, 'test.html', {"todo_list": todo_list})


def third(request):
    return render(request, 'test3.html')


def add(request):
    form = request.POST
    text = form['todo_text']
    todo = ToDo(text=text)
    todo.save()
    return redirect(homepage)


def update(request):
    return render(request, 'update.html')


def delete(request, id):
    todo = ToDo.objects.get(id=id)
    todo.delete()
    return redirect(homepage)
