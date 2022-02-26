from django.urls import path
from . import views

urlpatterns = [
    path('', views.index, name='index'), # routes the views to root directory
]