from django.shortcuts import render
from django.http import HttpResponse
# Create your views here.
def index(request):
    # строка для 1-го урока
    # return HttpResponse("<h1>Hello Elena! Это мой первый проект на Django</h1>")
    # строка для 2-го урока
    # в контекст указываем название переменной, куда всё будет подставляться.
    return render (request, 'main/index.html', {'caption':"Лучик"})


def new(request):
    # строка для 1-го урока
    # return HttpResponse("<h1>News - это 2я страница моего проекта на Django</h1>")
    # строка для 2-го урока
    return render (request, 'main/new.html')
