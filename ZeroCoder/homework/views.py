from django.http import HttpResponse

# Create your views here.
def page1(request):
    return HttpResponse("<h1>Приветствую! Это моя домашняя работа на Django</h1>")

def page2(request):
    return HttpResponse("<h1>А это 2я страница моего домашнего проекта на Django</h1>")