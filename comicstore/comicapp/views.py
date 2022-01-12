from django.shortcuts import render
from .models import Comic
# Create your views here.
def index(request):
    comics = Comic.objects.all()
    return render(request, 'comicapp/index.html',{'comics':comics})

def comics_details(request, comics_slug):
    selected_comic = Comic.objects.get(slug=comics_slug)
    return render(request, 'comicapp/comics_details.html',{
        'comic_title': selected_comic.title,
        'comic_description': selected_comic.description
    })

