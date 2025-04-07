from django.urls import path
from . import views

app_name = 'Todo'

urlpatterns = [
    path('', views.index, name='index'),
]