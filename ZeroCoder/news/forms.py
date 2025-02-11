# from .models import News_post
# from django.forms import ModelForm
#
# class News_postForm(ModelForm): #название класса обычно создают как название таблицы(from models.py и слова Forms)
# 	class Meta:
# 		model = News_post
# 		fields = ['title', 'short_description', 'text', 'pub_date'] # поля берем из models.py и можно не все,только нужные)


#добавляем при объединении красивой и функциональной форм. Widgets отвечают за оформление полей автоформы
from .models import News_post
from django.forms import ModelForm, TextInput, DateTimeInput, Textarea

class News_postForm(ModelForm):
	class Meta:
		model = News_post
		fields = ['title', 'short_description', 'text', 'pub_date', 'user_tell']
		widgets = {
			'title': TextInput(attrs={'class': 'form-control', 'placeholder': 'Заголовок новости'}),
			'short_description': TextInput(attrs={'class': 'form-control', 'placeholder': 'Краткое описание новости'}),
			'text': Textarea(attrs={'class': 'form-control', 'placeholder': 'Содержание новости'}),
			'pub_date': DateTimeInput(attrs={'class': 'form-control', 'placeholder': 'Дата публикации'}),
			'user_tell': TextInput(attrs={'class': 'form-control', 'placeholder': 'Ваше имя'})
		}