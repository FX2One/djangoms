from django.db import models

# Create your models here.
class ComicSeries(models.Model):
    series = models.CharField(max_length=200, default='SERIES')
    publishing = models.CharField(max_length=300)
    episodes = models.IntegerField()

    def __str__(self):
        return f'series: {self.series}'

class Available(models.Model):
    email = models.EmailField(unique=True, max_length=200)

    def __str__(self):
        return self.email

class Comic(models.Model):
    title = models.CharField(max_length=255)
    slug = models.SlugField(unique=True)
    description = models.TextField()
    image = models.ImageField(upload_to='images')
    series = models.ForeignKey(ComicSeries, on_delete=models.CASCADE)
    subscriber = models.ManyToManyField(Available, blank=True, null=True)
    

    def __str__(self):
        return f'{self.title} - {self.slug}'