from django.urls import path
from . import views

urlpatterns = [
    path('', views.data),
    path('hw1/', views.test)
]