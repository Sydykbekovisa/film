from rest_framework.generics import ListAPIView, RetrieveAPIView, RetrieveUpdateAPIView, DestroyAPIView, CreateAPIView
from rest_framework.filters import SearchFilter, OrderingFilter
from rest_framework.permissions import IsAdminUser

from django_filters.rest_framework import DjangoFilterBackend

from .models import Movie, Genre
from .serializers import MovieListSerializers, MovieDetailSerializers, MovieAddUpdateSerializers


class MovieListView(ListAPIView):
    queryset = Movie.objects.all()
    serializer_class = MovieListSerializers
    filter_backends = [SearchFilter, DjangoFilterBackend, OrderingFilter]
    search_fields = ['title']
    filterset_fields = ['genre']
    ordering = ['-release_date']


class MovieDetailView(RetrieveAPIView):
    queryset = Movie
    serializer_class = MovieDetailSerializers


class MovieUpdateView(RetrieveUpdateAPIView):
    queryset = Movie
    serializer_class = MovieAddUpdateSerializers
    permission_classes = [IsAdminUser]

    def put(self, request, *args, **kwargs):
        return self.update(request, *args, **kwargs)


class MovieDeleteView(DestroyAPIView):
    queryset = Movie
    serializer_class = MovieDetailSerializers
    permission_classes = [IsAdminUser]


class MovieCreateView(CreateAPIView):
    queryset = Movie
    serializer_class = MovieAddUpdateSerializers
    permission_classes = [IsAdminUser]
