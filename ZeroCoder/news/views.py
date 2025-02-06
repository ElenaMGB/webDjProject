from django.shortcuts import render

from .models import News_post


# Create your views here.
def home(request):
    news = News_post.objects.all() #переменная для получения всех записей. Добавляем после подключения учетки админа и создания новостей для показа их на стр.
    # return  render(request, 'main/new.html') #до подключения таблиц отсылка к пустой новостной странице
    # return render(request, 'news/news.html') #пока без контекста до подключения словаря и таблиц
    return render(request, 'news/news.html', {'news': news}) #+словарь для передачи информации в html-шаблон.