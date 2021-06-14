from .models.movies import Movies
from django.http import HttpRequest, HttpResponse
from django.shortcuts import render, redirect
from .forms import RemoveForm

# Create your views here.
def populate(request):
    movies_dict = [
        {
            "episode_nb": 1,
            "title": "The Phantom Menace",
            "director": "George Lucas",
            "producer": "Rick McCallum",
            "release_date": "1999-05-19"
        },
        {
            "episode_nb": 2,
            "title": "Attack of the Clones",
            "director": "George Lucas",
            "producer": "Rick McCallum",
            "release_date": "2002-05-16"
        },
        {
            "episode_nb": 3,
            "title": "Revenge of the Sith",
            "director": "George Lucas",
            "producer": "Rick McCallum",
            "release_date": "2005-05-19"
        },
        {
            "episode_nb": 4,
            "title": "A New Hope",
            "director": "George Lucas",
            "producer": "Gary Kurtz, Rick McCallum",
            "release_date": "1977-05-25"
        },
        {
            "episode_nb": 5,
            "title": "The Empire Strikes Back",
            "director": "Irvin Kershner",
            "producer": "Gary Kurtz, Rick McCallum",
            "release_date": "1980-05-17"
        },
        {
            "episode_nb": 6,
            "title": "Return of the Jedi",
            "director": "Richard Marquand",
            "producer": "Howard G. Kazanjian, George Lucas, Rick McCallum",
            "release_date": "1983-05-25"
        },
        {
            "episode_nb": 7,
            "title": "The Force Awakens",
            "director": "J. J. Abrams",
            "producer": "Kathleen Kennedy, J. J. Abrams, Bryan Burk",
            "release_date": "2015-12-11"
        }
        ]
    result = []
    for movie in movies_dict:
        try:
            Movies.objects.create(
                title = movie['title'],
                episode_nb = movie['episode_nb'],
                director = movie['director'],
                producer = movie['producer'],
                release_date = movie['release_date']
            )
            result.append("{} - OK<br>".format(movie['title'] ))
        except Exception as e:
            result.append(e)
            result.append("<br>")
    return HttpResponse(result)

def display(request):
    try:
        movies = Movies.objects.all()
        return render(request, 'ex05/display.html', { "movies" : movies})
    except Exception as e:
        return HttpResponse("No data available")

def remove(request):
    try:
        movies = Movies.objects.all()
        choice = ((movie.title, movie.title) for movie in movies)
        if request.method == 'POST':
            data = RemoveForm(choice, request.POST)
            if data.is_valid() == True:
                delete_title = data.cleaned_data['titles']
                movie_title = Movies.objects.get(title=delete_title)
                movie_title.delete()
            return redirect(request.path)
        return render(request, 'ex05/remove.html', {"RemoveForm": RemoveForm(choice)})

    except Exception as e:
        # return HttpResponse("No data available")
        print(e)
        return HttpResponse(e)


