from django.urls import path
from . import views

urlpatterns = [
    # path('', views.index),
    # path('new', views.new),
    path('hw/', views.page1),
    path('hw1/', views.page2)
]