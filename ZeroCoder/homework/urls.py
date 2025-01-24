from django.urls import path
from . import views

urlpatterns = [
    path('hw/', views.data),
    path('hw1/', views.test)
]