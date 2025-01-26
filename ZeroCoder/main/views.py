from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.
def index(request):
    # строка для 1-го урока
    # return HttpResponse("<h1>Hello Elena! Это мой первый проект на Django</h1>")

    # # строка для 2-го урока
    # # Подстановка из Python способ1: в контекст указываем название переменной, куда всё будет подставляться.
    # return render (request, 'main/index.html', {'caption':"Наш реабилитационный центр"})

    # Подстановка из Python способ2: в контекст указываем название переменной, куда всё будет подставляться.
    data = {
        'caption': "Наш реабилитационный центр"
    }
    return render(request, 'main/index.html', data)

def new(request):
    # строка для 1-го урока
    # return HttpResponse("<h1>News - это 2я страница моего проекта на Django</h1>")

    # строка для 2-го урока
    return render (request, 'main/new.html')
def program(request):
    return render (request, 'main/program.html')

def teacher(request):
    return render (request, 'main/teacher.html')

def lesson(request):
    return render (request, 'main/lesson.html')
def event(request):
    return render (request, 'main/event.html')
def forparents(request):
    return render (request, 'main/forparents.html')