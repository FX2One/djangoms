from django.shortcuts import render, redirect
from .models import Comic, Available
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
                subscriber_email = subscription_form.cleaned_data['email']
                subscriber, _ = Available.objects.get_or_create(email=subscriber_email) #_ usually stored as was_created
                selected_comic.subscribers.add(subscriber)
                return redirect('confirm-subscription')
        return render(request, 'comicapp/comics_details.html',{
            'comic_found': True,
            'comic': selected_comic,
            'form': subscription_form
         })
    except Exception as e:
        return render(request,'comicapp/comics_details.html',{'comic_found': False})

def confirm_subscription(request):
    return render(request, 'comicapp/sub-success.html')