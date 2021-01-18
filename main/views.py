from django.shortcuts import render

# Create your views here.


def homepage(request):
    return render(request, 'index.html')


def test(request):
    return render(request, 'test.html')


def third(request):
    return render(request, 'test3.html')


def add(request):
    return render(request, 'add.html')


def update(request):
    return render(request, 'update.html')


def delete(request):
    return render(request, 'delete.html')
