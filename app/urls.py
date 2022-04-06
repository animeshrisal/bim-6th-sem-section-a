from . import views
from django.urls import path

urlpatterns = [
    path('', views.index),
    path('about/', views.about),
    path('number/<int:id>/', views.number),
    path('movies/<int:id>/', views.get_movie),
    path('movies/page/<int:page_number>/', views.get_movies),
    path('post_movie/', views.post_movie),
    path('update_movie/<int:id>/', views.update_movie),
    path('delete_movie/<int:id>/', views.delete_movie),
    path('signup/', views.signup, name="User Sign Up"),
    path('signin/', views.signin, name="User Sign In"),
    path('signout/', views.signout, name="User Sign Out"),
    path('add_to_favorite/<int:id>', 
            views.add_to_favorite, 
            name="Add to favorite"),
    path('remove_from_favorites/<int:id>',
            views.remove_from_favorites, 
            name="Remove from favorite"),
    path('user_favorites/', 
            views.get_user_favorites, 
            name="Get User Favorites"),
    path('upload_dataset/', views.upload_dataset, name="Upload dataset"),
]
