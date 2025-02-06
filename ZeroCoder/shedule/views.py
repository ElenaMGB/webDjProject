from django.shortcuts import render

# from .models import News_post
# Create your views here.
def shedule_home(request):
    # shedule = News_post.objects.all()
    # return render(request, 'main/lesson.html') #до подключения таблицы отсылка к странице 5 "Уроки"
    return render(request, 'shedule/shedule.html')