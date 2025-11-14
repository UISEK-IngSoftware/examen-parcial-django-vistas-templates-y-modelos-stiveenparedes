from django.shortcuts import render, get_object_or_404, redirect
from django.template import loader
from .models import Movie
from .forms import MovieForm

def index(request):
    movies = Movie.objects.all()
    template = loader.get_template('index.html')
    return render(request, 'index.html', {'movies': movies})

def detail(request, movie_id):
    movie = get_object_or_404(Movie, id=movie_id)
    return render(request, 'detail.html', {'movie': movie})

def add_movie(request):
    if request.method == 'POST':
        form = MovieForm(request.POST, request.FILES)
        if form.is_valid():
            form.save()
            return redirect('movies:index')
    else:
        form = MovieForm()

    return render(request, 'movie_form.html', {'form': form})

def edit_movie(request, movie_id):
    movie = get_object_or_404(Movie, id=movie_id)
    if request.method == 'POST':
        form = MovieForm(request.POST, request.FILES, instance=movie)
        if form.is_valid():
            form.save()
            return redirect('movies:detail', movie_id=movie.id)
    else:
        form = MovieForm(instance=movie)

    return render(request, 'movie_form.html', {'form': form, 'movie': movie})

def delete_movie(request, movie_id):
    movie = get_object_or_404(Movie, id=movie_id)
    movie.delete()
    return redirect('movies:index')
