from django.urls import path
from . import views

urlpatterns = [
	path('', views.shedule_home, name='schedule_home'),
]