from django.shortcuts import redirect
from django.views.generic import ListView, DetailView
from django.views.generic.base import View
from django.db.models import Q, OuterRef, Subquery, Case, When
from .forms import ReviewForm
from .models import Movie, Category, Actor, Genre


class GenreYear:
    """Genres and release years of filmsв"""

    def get_genres(self):
        return Genre.objects.all()

    def get_years(self):
        return Movie.objects.filter(draft=False).values("year")


class MovieView(GenreYear, ListView):
    """List of films"""

    model = Movie
    queryset = Movie.objects.filter(draft=False)

    def get_context_data(self, *args, **kwargs):
        context = super().get_context_data(*args, **kwargs)
        context["categories"] = Category.objects.all()
        context["form"] = ReviewForm()
        return context


class MovieDetailView(GenreYear, DetailView):
    """Full description of the film"""

    model = Movie
    slug_field = "url"


class AddReview(View):
    """Reviews"""

    def post(self, request, pk):
        form = ReviewForm(request.POST)
        movie = Movie.objects.get(id=pk)
        if form.is_valid():
            form = form.save(commit=False)
            if request.POST.get("parent", None):
                form.parent_id = int(request.POST.get("parent"))
            form.movie = movie
            form.save()
        return redirect(movie.get_absolute_url())


class ActorView(GenreYear, DetailView):
    """Displaying information about an actor"""

    model = Actor
    template_name = "movies/actor.html"
    slug_field = "name"


class FilterMoviesView(GenreYear, ListView):
    """Movie filter"""

    def get_queryset(self):
        queryset = Movie.objects.filter(
            Q(year__in=self.request.GET.getlist("year")) |
            Q(genres__in=self.request.GET.getlist("genre"))
        )
        return queryset
    #
    # def get_context_data(self, *args, **kwargs):
    #     context = super().get_context_data(*args, **kwargs)
    #     context["year"] = ''.join([f"year={x}&" for x in self.request.GET.getlist("year")])
    #     context["genre"] = ''.join([f"genre={x}&" for x in self.request.GET.getlist("genre")])
    #     return context
