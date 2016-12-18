class Movie():
    """A movie object.

    Attributes:
        title: A string representing the title of a movie.
        storyline: A string that represents a short summary of a movie.
        poster_image_url: A string that links to a url that represents the cover artwork of a movie.
        trailer_youtube_url: A link to the movies trailer on YouTube.

    """


    def __init__(self, movie_title, movie_storyline, poster_image, trailer_youtube):
        """
        Constructor requiring all four arguments in order to properly describe a movie in order for the web page to function properly
        :param movie_title: String
        :param movie_storyline: String
        :param poster_image: String
        :param trailer_youtube: String
        """

        self.title = movie_title
        self.storyline = movie_storyline
        self.poster_image_url = poster_image
        self.trailer_youtube_url = trailer_youtube

    def __str__(self):
        """Overrides the objects __str__ method in order to display a movie title with the print() method"""
        return self.title


class Movies():
    """Acts as a database to store movies added by the user

    Attributes:
        movies: A list representing all the movie objects a user has created.
    """

    movies = []

    def __init__(self):
        """
        initializes an empty list of movies
        """

        self.movies = []


    def add_movie(self, movie):
        """Adds a movie to the database.

        :param movie: Movie

        """

        self.movies.append(movie)

    def remove_movie(self, movie_title):
        """Removes a movie from the database

        Iterates through the movies[] list and removes a movie whose title matches the
        param EXACTLY. It then removes the movie object from the movies[] list.

        :param movie_title: String used to compare titles in the database
        """

        index = 0
        wasFound = False
        # Look for movie in database
        for movie in self.movies:
            if movie.title == movie_title:
                index = self.movies.index(movie)
                wasFound = True
        if wasFound:
            deleted_movie = self.movies.pop(index)
            print("Deleting " + deleted_movie.title)
            print("Success!")
        else:
            print("Couldn't find " + movie_title + " in the list!")

    def get_movies(self):
        """Returns a list[] of all movies currently in the database

        :return: List[] of movies
        """
        return self.movies




