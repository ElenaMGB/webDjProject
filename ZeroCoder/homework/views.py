from django.http import HttpResponse

# Create your views here.
def data(request):
    return HttpResponse("<h1>Приветствую! Это моя 1 домашняя работа на Django</h1>")

def test(request):
    return HttpResponse("<h1>А это 2я страница моего 1го домашнего проекта на Django</h1>")