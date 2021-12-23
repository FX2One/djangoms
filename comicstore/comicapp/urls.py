from django.urls import path
from . import views

urlpatterns = [
    path('comics/', views.index),
    path('comics/<slug:comics_slug>', views.comics_details)
]