from django.shortcuts import render

# Create your views here.
def index(request):
    comics = [{
        'title':'#1 Wolverine Origins',
        'episodes':'12',
        'slug':'wolverine'
    },
    {
        'title':'#2 Magneto Origins',
        'episodes':'11',
        'slug':'magneto'
    }]
    return render(request, 'comicapp/index.html',
                  {'show_comics': True,
                    'comics':comics
                   })
