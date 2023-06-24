import pytest

from movies.models import Movie


@pytest.fixture(scope="function")
def add_movie():
    def add_movie(title, genre, year):
        movie = Movie.objects.create(title=title, genre=genre, year=year)
        return movie

    return add_movie
