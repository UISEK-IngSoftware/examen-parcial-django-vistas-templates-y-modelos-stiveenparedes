from django.db import models

# Create your models here.
class Movie(models.Model):

    GENRES = [
        ('ACCION', 'Acción'),
        ('COMEDIA', 'Comedia'),
        ('DRAMA', 'Drama'),
        ('TERROR', 'Terror'),
        ('SCI-FI', 'Ciencia Ficción'),
        ('ROMANCE', 'Romance'),
    ]

    title = models.CharField(max_length=200)
    genre = models.CharField(max_length=50, choices=GENRES)
    director = models.CharField(max_length=100)
    release_date = models.DateField()
    synopsis = models.TextField()
    picture = models.ImageField(upload_to='movie_pictures/', null=True, blank=True)

    def __str__(self):
        return self.title