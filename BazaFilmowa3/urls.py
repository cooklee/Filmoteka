"""BazaFilmowa3 URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.2/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path

from filmy import views

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', views.index),
    path('osoby/', views.show_osoby),
    path('osoby/<int:pk>/', views.osoba_detail),
    path('add_osoba/', views.add_osoba),
    path('filmy/', views.show_filmy),
    path('add_filmy/', views.add_filmy),
    path('film/<int:pk>/', views.film_detail),
    path('film/<int:film_pk>/add_actor/', views.AddActorToMovie.as_view()),
    path('add_genre/', views.add_genre ),
    path('genre/', views.genre),
    path('delete_osoby/<int:pk>/', views.delete_osoby ),
    path('set_session/', views.SessionFunView.as_view()),
    path('show_session/', views.ShowSession.as_view()),
    path('cookiemonster/', views.CookieeMonsterFunView.as_view()),
    path("delete_cookie/",views.DeleteCookiee.as_view())
]
