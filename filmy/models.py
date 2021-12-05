from django.db import models

# Create your models here.


class Genre(models.Model):
    name = models.CharField(max_length=25)

    def __str__(self):
        return self.name

class Person(models.Model):
    first_name = models.CharField(max_length=23)
    last_name = models.CharField(max_length=50)
    #film_set
    #film_set

    def __str__(self):
        return f"{self.first_name} {self.last_name}"

    def get_absolute_url(self):
        return f"/osoby/{self.id}/"

    def get_delete_url(self):
        return f"/delete_osoby/{self.id}/"


class Starring(models.Model):
    actor = models.ForeignKey(Person, on_delete=models.CASCADE, related_name='played_in')
    film = models.ForeignKey("Film", on_delete=models.CASCADE, related_name='starring')
    role = models.CharField(max_length=123)

class Film(models.Model):
    title = models.CharField(max_length=50)
    year = models.IntegerField()
    director = models.ForeignKey(Person, on_delete=models.CASCADE, null=True, related_name="directed_by")
    screenplay = models.ForeignKey(Person, on_delete=models.CASCADE, null=True, related_name='writen')
    actors = models.ManyToManyField(Person, related_name='starring', through=Starring)
    genre = models.ManyToManyField(Genre)

    def __str__(self):
        return f"{self.title} {self.year}"


    def get_absolute_url(self):
        return f"/film/{self.id}/"

