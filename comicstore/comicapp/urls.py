from django.urls import path
from . import views

urlpatterns = [
    path('comics/', views.index, name='all-comics'),
    path('comics/<slug:comics_slug>', views.comics_details, name='comics-details')
]