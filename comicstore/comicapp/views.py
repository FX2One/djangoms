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

def comics_details(request, comics_slug):
    selected_comic = {
        'title':'Wolverine Origins',
        'description':'Comic telling a whole story about Wolverine'}
    return render(request, 'comicapp/comics_details.html',{
        'comic_title': selected_comic['title'],
        'comic_description': selected_comic['description']
    })

