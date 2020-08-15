from django.shortcuts import render, redirect
from django.views.generic import ListView, DetailView
from django.views.generic.base import View
from .forms import ReviewForm
from .models import Movie


class MovieView(ListView):
    """List of films"""
    model = Movie
    queryset = Movie.objects.filter(draft=False)



class MovieDetailView(DetailView):
    """Full description of the film"""
    model = Movie
    slug_field = 'url'

class AddReview(View):
    """Reviews"""
    def post(self, request, pk):
        form = ReviewForm(request.POST)
        movie = Movie.objects.get(id=pk)
        if form.is_valid():
            form = form.save(commit=False)
            form.movie = movie
            form.save()
        return redirect(movie.get_absolute_url())