from django.shortcuts import render
from django.views.generic import ListView, DetailView
from django.views.generic.base import View

from .models import Movie


class MovieView(ListView):
    """List of films"""
    model = Movie
    queryset = Movie.objects.filter(draft=False)
    # template_name = "movies/movies.html"


class MovieDetailView(DetailView):
    """Full description of the film"""
    model = Movie
    slug_field = 'url'