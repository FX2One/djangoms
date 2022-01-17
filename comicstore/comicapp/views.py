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
        if request.method == 'GET':
            subscription_form = SubscriptionForm()
        else:
            subscription_form = SubscriptionForm(request.POST)
            if subscription_form.is_valid():
                subscriber = subscription_form.save()
                selected_comic.subscribers.add(subscriber)
        return render(request, 'comicapp/comics_details.html',{
            'comic_found': True,
            'comic': selected_comic,
            'form': subscription_form
         })
    except Exception as e:
        return render(request,'comicapp/comics_details.html',{'comic_found': False})

