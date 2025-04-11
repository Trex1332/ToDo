from django.urls import path
from . import views

app_name = 'Todo'

urlpatterns = [
    path('', views.index, name='index'),
    path('delete/<int:todo_id>/', views.delete_todo, name='delete_todo'),
    path('add/', views.add, name='add_todo'),
]