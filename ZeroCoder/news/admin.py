from django.contrib import admin
from .models import News_post

# Register your models here.


class NewsAdmin(admin.ModelAdmin):
    list_display = ('id', 'title', 'short_description', 'text', 'pub_date', 'user_tell')  # Отображаемые поля
    search_fields = ('user_tell',)  # Поле для поиска
    list_filter = ('pub_date',)  # Фильтрация
    ordering = ('-pub_date',)  # Сортировка (по убыванию даты создания)
    readonly_fields = ('user_tell',)

admin.site.register(News_post, NewsAdmin)