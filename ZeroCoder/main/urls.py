from django.urls import path
from . import views

# # для 1го урока
# urlpatterns = [
#     path('', views.index),
#     path('new', views.new)
# ]

# для 2го урока
urlpatterns = [
    path('', views.index, name='home'),
    path('new/', views.new, name='page2'),
    path('program/', views.program, name='page3'),
    path('teacher/', views.teacher, name='page4'),
    path('lesson/', views.lesson, name='page5'),
    path('event/', views.event, name='page6'),
    path('forparents/', views.forparents, name='page7')
]