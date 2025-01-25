from django.urls import path
from . import views

# для 1го урока
urlpatterns = [
    path('', views.index),
    path('new', views.new),
]