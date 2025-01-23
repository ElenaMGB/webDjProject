from django.shortcuts import render
from django.http import HttpResponse
# Create your views here.
def index(request):
    return HttpResponse("<h1>Hello Elena! Это мой первый проект на Django</h1>")

def new(request):
    return HttpResponse("<h1>News - это 2я страница моего проекта на Django</h1>")
