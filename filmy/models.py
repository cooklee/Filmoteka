from django.db import models

# Create your models here.


class Genre(models.Model):
    name = models.CharField(max_length=25)

    def __str__(self):
        return self.name

class Person(models.Model):
    first_name = models.CharField(max_length=23)
    last_name = models.CharField(max_length=50)

    def __str__(self):
        return f"{self.first_name} {self.last_name}"

    def get_absolute_url(self):
        return f"/osoby/{self.id}/"

class Film(models.Model):
    title = models.CharField(max_length=50)
    year = models.IntegerField()
    director = models.ForeignKey(Person, on_delete=models.CASCADE, null=True)
    genre = models.ManyToManyField(Genre)

    def __str__(self):
        return f"{self.title} {self.year}"


    def get_absolute_url(self):
        return f"/film/{self.id}/"

