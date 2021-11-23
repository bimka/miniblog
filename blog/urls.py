from django.urls import path
from . import views


urlpatterns = [
    path('', views.index, name='index'),
    path('add_a_joke', views.Add_a_joke.as_view(), name='add_a_joke'), 
]
