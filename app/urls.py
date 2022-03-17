from . import views
from django.urls import path

urlpatterns = [
    path('', views.index),
    path('about/', views.about),
    path('number/<int:id>/', views.number),
    path('movies/<int:id>/', views.get_movie),
    path('movies/', views.get_movies),
    path('post_movie/', views.post_movie),
    path('update_movie/<int:id>/', views.update_movie),
    path('delete_movie/<int:id>/', views.delete_movie),
]
