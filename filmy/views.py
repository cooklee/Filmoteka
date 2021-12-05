from django.http import HttpResponse
from django.shortcuts import render, redirect

# Create your views here.
from django.views import View

from filmy.models import Person, Film, Genre, Starring


def index(request):
    return render(request, 'b2.html')


def show_osoby(request):

    nazwisko = request.GET.get('last_name', '')
    imie = request.GET.get('first_name', '')
    osoby = Person.objects.all()
    osoby = osoby.filter(last_name__icontains=nazwisko)
    osoby = osoby.filter(first_name__icontains=imie)
    return render(request,'osoby.html', {'object_list':osoby})

def osoba_detail(request, pk):
    osoba = Person.objects.get(pk=pk)
    return render(request, 'osoba.html', {'osoba':osoba})

def add_osoba(request):
    if request.method == 'GET':
        return render(request, 'add_osoba.html')
    else:
        imie = request.POST['first_name']
        nazwisko = request.POST['last_name']
        Person.objects.create(first_name=imie, last_name=nazwisko)
        return redirect('/osoby/')


def show_filmy(request):
    movies = Film.objects.all()
    return render(request,'filmy.html', {'object_list':movies})


def add_filmy(request):
    genre = Genre.objects.all()
    persons = Person.objects.all()
    if request.method == 'GET':
        return render(request, 'add_film.html', {'genre':genre, 'osoby':persons})
    else:
        title = request.POST.get('title')
        year = request.POST.get('year')
        director_id = request.POST.get('director')
        director = Person.objects.get(pk=director_id)
        genre_ids = request.POST.getlist('genre')
        f = Film.objects.create(title=title, year=year, director=director)
        f.genre.set(genre_ids)
        return redirect('/filmy/')


def film_detail(request, pk):
    film = Film.objects.get(pk=pk)
    if request.method == 'POST':
        title = request.POST.get('title')
        year = request.POST.get('year')
        director_id = request.POST.get('director')
        director = Person.objects.get(pk=director_id)
        film.title = title
        film.year = year
        film.director = director
        genre_ids = request.POST.getlist('genre')
        film.genre.set(genre_ids)
        film.save()
    persons = Person.objects.all()
    genre = Genre.objects.all()
    return render(request,'film_detail.html', {'film':film, 'persons':persons, 'genre':genre})

class AddGenreView(View):
    def get(self, request):
        return render(request, 'add_genre.html')

    def post(self, request):
        name = request.POST.get('name')
        Genre.objects.create(name=name)
        return redirect('/genre/')

def add_genre(request):
    if request.method == 'GET':
        return render(request, 'add_genre.html')
    else:
        name = request.POST.get('name')
        Genre.objects.create(name=name)
        return redirect('/genre/')

def genre(request):
    genre = Genre.objects.all()
    return render(request, 'list_view.html', {'object_list':genre})


def delete_osoby(request, pk):
    person = Person.objects.get(pk=pk)
    if request.method == 'GET':
        return render(request, 'delete_template.html', {'object':person})
    person.delete()
    return redirect('/osoby/')


class AddActorToMovie(View):
    def get(self, request, film_pk):
        persons = Person.objects.all()
        return render(request, 'add_actor_to_movie.html', {'persons':persons, 'film':Film.objects.get(pk=film_pk)})

    def post(self, request, film_pk):
        film = Film.objects.get(pk=film_pk)
        person_id = request.POST.get('actor')
        role = request.POST.get('role')
        person = Person.objects.get(pk=person_id)
        Starring.objects.create(film=film, actor=person, role=role)
        return redirect(f'/film/{film_pk}/add_actor/')
