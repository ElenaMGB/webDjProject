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
    path('new', views.new, name='page2')
]