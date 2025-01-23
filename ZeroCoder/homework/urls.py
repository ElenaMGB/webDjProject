from django.urls import path
from . import views

urlpatterns = [
    path('', views.page1),
    path('hw1/', views.page2)
]