from rest_framework.test import APITestCase
from rest_framework import status
from .models import Movie


class MovieAPITest(APITestCase):
    def setUp(self):
        # Создаём тестовый фильм
        self.movie = Movie.objects.create(
            title="Inception",
            director="Christopher Nolan",
            description="A mind-bending thriller",
            release_date="2010-07-16",
            genre="Sci-Fi",
            rating=8.8,
            duration=148
        )
        self.movie_url = f"/movies/{self.movie.id}/"

    def test_get_movies_list(self):
        """Тест получения списка фильмов."""
        response = self.client.get("/movies/")
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(len(response.data), 1)
        self.assertEqual(response.data[0]["title"], "Inception")

    def test_get_single_movie(self):
        """Тест получения одного фильма."""
        response = self.client.get(self.movie_url)
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(response.data["title"], "Inception")
        self.assertEqual(response.data["director"], "Christopher Nolan")

    def test_create_movie(self):
        """Тест создания нового фильма."""
        data = {
            "title": "The Matrix",
            "director": "The Wachowskis",
            "description": "A dystopian sci-fi thriller",
            "release_date": "1999-03-31",
            "genre": "Sci-Fi",
            "rating": 8.7,
            "duration": 136
        }
        response = self.client.post("/movies/", data)
        self.assertEqual(response.status_code, status.HTTP_201_CREATED)
        self.assertEqual(Movie.objects.count(), 2)
        self.assertEqual(Movie.objects.last().title, "The Matrix")

    def test_update_movie(self):
        """Тест обновления фильма."""
        data = {
            "title": "Inception (Updated)",
            "director": "Christopher Nolan",
            "description": "An updated description",
            "release_date": "2010-07-16",
            "genre": "Sci-Fi",
            "rating": 9.0,
            "duration": 148
        }
        response = self.client.put(self.movie_url, data)
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.movie.refresh_from_db()
        self.assertEqual(self.movie.title, "Inception (Updated)")
        self.assertEqual(self.movie.rating, 9.0)

    def test_delete_movie(self):
        """Тест удаления фильма."""
        response = self.client.delete(self.movie_url)
        self.assertEqual(response.status_code, status.HTTP_204_NO_CONTENT)
        self.assertEqual(Movie.objects.count(), 0)
