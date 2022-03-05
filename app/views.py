from django.http import HttpResponse
from django.shortcuts import render
from .models import Movie

# Create your views here.
def index(request):
    return HttpResponse('Hello World')

def about(request):
    return HttpResponse('About Page')

def number(request, id):
    return HttpResponse(id)

def get_movie(request, id):
    try:
        movie = Movie.objects.get(pk=id)
        return render(request, 'movie.html', {'movie': movie})
    except Movie.DoesNotExist:
        return render(request, '404.html')