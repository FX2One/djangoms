from django.db import models

# Create your models here.
class Comic(models.Model):
    title = models.CharField(max_length=255)
    slug = models.SlugField(unique=True)
    description = models.TextField()
    image = models.ImageField(upload_to='images')

    def __str__(self):
        return f'{self.title} - {self.slug}'

class ComicSeries(models.Model):
    series = models.CharField(max_length=200)
    publishing = models.CharField(max_length=300)
    episodes = models.IntegerField()

    def __str__(self):
        return f'series: {self.series}, publishing: {self.publishing}'

