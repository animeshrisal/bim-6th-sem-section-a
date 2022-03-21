from django.http import HttpResponse
from django.shortcuts import redirect, render

from django.contrib.auth.forms import AuthenticationForm, UserCreationForm
from django.contrib.auth import authenticate, login, logout

from .forms import MovieForm
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

            return redirect('/movies')

    return render(request, 'post_movie.html', {'movie_form': movie_form})

def update_movie(request, id):
    movie = Movie.objects.get(pk=id)

    if request.method == "POST":
        movie_form = MovieForm(request.POST, instance=movie)
        if movie_form.is_valid():
            movie_form.save()
            return redirect('/movies/{}'.format(id))

 
    movie_form = MovieForm(instance=movie)

    return render(request, 'update_movie.html', {'form': movie_form})

def delete_movie(request, id):
    movie = Movie.objects.get(pk=id)
    movie.delete()
    return redirect('/movies/')

def signin(request):
    form = AuthenticationForm()
    if request.method == "POST":
        form = AuthenticationForm(data=request.POST)

        if form.is_valid():
            user = authenticate(
                username=form.cleaned_data['username'], 
                password=form.cleaned_data['password'])
            login(request, user)
            return redirect('/movies/')

    return render(request, 'signin.html', {'form': form})

def signup(request):
    form = UserCreationForm()
    if request.method == "POST":
        form = UserCreationForm(request.POST)

        if form.is_valid():
            form.save()
            user = authenticate(
                username=form.cleaned_data['username'], password=form.cleaned_data['password1'])
            login(request, user)
            return redirect('/movies/')

    return render(request, 'signup.html', {'form': form})

def signout(request):
    logout(request)
    return redirect('/movies/')

def add_to_favorite(request, id):
    movie = Movie.objects.get(id=id)
    movie.favorite.add(request.user)

    return redirect('/movies/{0}'.format(id))

def remove_from_favorites(request, id):
    movie = Movie.objects.get(id=id)
    movie.favorite.remove(request.user)

    return redirect('/movies/{0}'.format(id))