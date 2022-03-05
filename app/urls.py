from . import views
from django.urls import path

urlpatterns = [
    path('', views.index),
    path('about/', views.about),
    path('number/<int:id>/', views.number),
    path('movies/<int:id>/', views.get_movie),
    path('movies/', views.get_movies)
]
