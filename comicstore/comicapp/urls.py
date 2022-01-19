from django.urls import path
from . import views

urlpatterns = [
    path('', views.index, name='all-comics'),
    path('<slug:comics_slug>/success', views.confirm_subscription, name='confirm-subscription'),
    path('<slug:comics_slug>', views.comics_details, name='comics-detail')
]