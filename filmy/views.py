from django.http import HttpResponse
from django.shortcuts import render, redirect

# Create your views here.
from filmy.models import Person, Film


def index(request):
    return render(request, 'b2.html')


def show_osoby(request):

    nazwisko = request.GET.get('last_name', '')
    imie = request.GET.get('first_name', '')
    osoby = Person.objects.all()
    osoby = osoby.filter(last_name__icontains=nazwisko)
    osoby = osoby.filter(first_name__icontains=imie)
    return render(request,'object_list.html', {'object_list':osoby})


def add_osoba(request):
    if request.method == 'GET':
        return render(request, 'add_osoba.html')
    else:
        imie = request.POST.get('first_name')
        nazwisko = request.POST.get('last_name')
        Person.objects.create(first_name=imie, last_name=nazwisko)
        return redirect('/osoby/')


def show_filmy(request):
    movies = Film.objects.all()
    return render(request,'object_list.html', {'object_list':movies})


def add_filmy(request):
    if request.method == 'GET':
        return render(request, 'add_film.html')
    else:
        title = request.POST.get('title')
        year = request.POST.get('year')
        Film.objects.create(title=title, year=year)
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
        film.save()
    persons = Person.objects.all()
    return render(request,'film_detail.html', {'film':film, 'persons':persons})


