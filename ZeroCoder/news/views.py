from django.shortcuts import render

from .models import News_post
from .forms import News_postForm

# Create your views here.
def home(request):
    news = News_post.objects.all() #переменная для получения всех записей. Добавляем после подключения учетки админа и создания новостей для показа их на стр.
    # return  render(request, 'main/new.html') #до подключения таблиц отсылка к пустой новостной странице
    # return render(request, 'news/news.html') #пока без контекста до подключения словаря и таблиц
    return render(request, 'news/news.html', {'news': news}) #+словарь для передачи информации в html-шаблон.

def create_news(request):
	# return render(request, 'news/add_new_post.html') #для 1-го варианта создания форм
# для 2го варианта через файл forms.py:
    form = News_postForm()
    return render(request, 'news/add_new_post.html', {'form': form})