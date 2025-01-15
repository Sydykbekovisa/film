from django.urls import path

from .views import MovieListView, MovieDeleteView, MovieUpdateView, MovieDetailView, MovieCreateView

urlpatterns = [
    path('', MovieListView.as_view(), name='movie-list'),
    path('<int:pk>/', MovieDetailView.as_view(), name='movie-detail'),
    path('update/<int:pk>/', MovieUpdateView.as_view(), name='movie-update'),
    path('delete/<int:pk>/', MovieDeleteView.as_view(), name='movie-delete'),
    path('add/', MovieCreateView.as_view(), name='movie-add')
]