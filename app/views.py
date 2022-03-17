from django.http import HttpResponse
from django.shortcuts import redirect, render

from app.forms import MovieForm
from .models import Movie

def get_movie(request, id):
    try:
        movie = Movie.objects.get(pk=id)
        return render(request, 'movie.html', {'movie': movie})
    except Movie.DoesNotExist:
        return render(request, '404.html')


# Create your views here.
def index(request):
    return HttpResponse('Hello World')

def about(request):
    return HttpResponse('About Page')

def number(request, id):
    return HttpResponse(id)


def get_movies(request):
    movies = Movie.objects.all()
    return render(request, 'movies.html', {'movies': movies})

def post_movie(request):
    movie_form = MovieForm()
    
    if request.method == "POST":
        movie_form = MovieForm(request.POST)

        if movie_form.is_valid():
            movie_form.save()

            return redirect('/movies')

    return render(request, 'post_movie.html', {'movie_form': movie_form})


def post_movie(request):
    movie_form = MovieForm()

    if request.method == "POST":
        movie_form = MovieForm(request.POST)

        if movie_form.is_valid():
            movie_form.save()

            return redirect('/movies/page/1')

    return render(request, 'post_movie.html', {'movie_form': movie_form})

def update_movie(request, id):
    movie = Movie.objects.get(pk=id)

    if request.method == "POST":
        movie_form = MovieForm(request.POST, instance=movie)
        if movie_form.is_valid():
            movie_form.save()
            return redirect('/movies/{}'.format(id))

    elif request.method == "GET":
        movie_form = MovieForm(instance=movie)

    return render(request, 'update_movie.html', {'form': movie_form})

def delete_movie(request, id):
    movie = Movie.objects.get(pk=id)
    movie.delete()
    return redirect('/movies/')