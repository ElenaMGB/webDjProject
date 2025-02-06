from django.shortcuts import render

from .models import News_post


# Create your views here.
def home(request):
    # news = News_post.objects.all()
    # return  render(request, 'main/new.html') #до подключения таблиц отсылка к пустой новостной странице
    return render(request, 'news/news.html') #пока без контекста
    # return render(request, 'news/news.html', {'news': news})