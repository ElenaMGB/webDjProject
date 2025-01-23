from django.urls import path
from . import views

urlpatterns = [
    path('', views.index),
    path('new', views.new),
    # path('page1', views.new),
    # path('page2', views.new)
]
