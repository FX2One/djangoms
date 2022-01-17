from django.shortcuts import render
from .models import Comic
from .forms import SubscriptionForm
# Create your views here.
def index(request):
    comics = Comic.objects.all()
    return render(request, 'comicapp/index.html',{'comics':comics})

def comics_details(request, comics_slug):
    try:
        selected_comic = Comic.objects.get(slug=comics_slug)
        subscription_form = SubscriptionForm
        return render(request, 'comicapp/comics_details.html',{
            'comic_found': True,
            'comic': selected_comic,
            'form': subscription_form
        })
    except Exception as e:
        return render(request,'comicapp/comics_details.html',{'comic_found': False})

