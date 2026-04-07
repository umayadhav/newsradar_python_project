# news/urls.py
from django.urls import path
from . import views

urlpatterns = [
    path('',                          views.home,             name='home'),
    path('category/<str:category>/',  views.category,         name='category'),
    path('search/',                   views.search,           name='search'),
    path('favourites/',               views.favourites_view,  name='favourites'),
    path('favourite/add/',            views.add_favourite,    name='add_favourite'),
    path('favourite/remove/<int:index>/', views.remove_favourite, name='remove_favourite'),
    path('digest/',                   views.digest,           name='digest'),
]