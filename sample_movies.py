"""
Copyright 2016 Carl Argabright

   Licensed under the Apache License, Version 2.0 (the "License");
   you may not use this file except in compliance with the License.
   You may obtain a copy of the License at

       http://www.apache.org/licenses/LICENSE-2.0

   Unless required by applicable law or agreed to in writing, software
   distributed under the License is distributed on an "AS IS" BASIS,
   WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
   See the License for the specific language governing permissions and
   limitations under the License.
"""


import media

# This module contains hard coded movie data that can be used
# to see the results of the Movie Trailer Website without the
# user having to add all of their favorite movie titles.
toy_story = media.Movie("Toy Story",
                        "A story about a boy and his toys that come to life",
                        "https://upload.wikimedia.org/wikipedia/en/1/13/Toy_Story.jpg",  # NoQA
                        "https://www.youtube.com/watch?v=KYz2wyBy3kc")

avatar = media.Movie("Avatar",
                     "A story about a marine",
                     "https://upload.wikimedia.org/wikipedia/en/b/b0/Avatar-Teaser-Poster.jpg",  # NoQA
                     "https://www.youtube.com/watch?v=5PSNL1qE6VY")

full_metal_jacket = media.Movie("Full Metal Jacket",
                                "A few marines arrive at boot camp and get the training of their life.",  # NoQA
                                "https://upload.wikimedia.org/wikipedia/en/9/99/Full_Metal_Jacket_poster.jpg",  # NoQA
                                "https://www.youtube.com/watch?v=x9f6JaaX7Wg")

hackers = media.Movie("Hackers",
                      "A few fun loving hackers get blamed for something the didn't do",  # NoQA
                      "https://upload.wikimedia.org/wikipedia/en/6/67/Hackersposter.jpg",  # NoQA
                      "https://www.youtube.com/watch?v=Rn2cf_wJ4f4")

star_wars = media.Movie("Star Wars: The Force Awakens",
                        "Disney acquired Lucas Films and thought they could make a better movie",  # NoQA
                        "https://upload.wikimedia.org/wikipedia/en/a/a2/Star_Wars_The_Force_Awakens_Theatrical_Poster.jpg",  # NoQA
                        "https://www.youtube.com/watch?v=sGbxmsDFVnE")

the_matrix = media.Movie("The Matrix",
                         "Reality is only perceived reality and the ones who do not know must be secretly protected",  # NoQA
                         "https://upload.wikimedia.org/wikipedia/en/c/c1/The_Matrix_Poster.jpg",  # NoQA
                         "https://www.youtube.com/watch?v=vKQi3bBA1y8")


class SampleMovies:
    """A quick and dirty way to represent a List[] of movies hard coded in the
    current module.
    """

    # A sample list of movies the user can preload to test the page.
    sample_movies = []

    def __init__(self):
        """
        Default constructor that initializes this class with a list of all
        the hard coded movies in this module.
        """

        self.sample_movies = [toy_story, avatar, full_metal_jacket,
                              hackers, star_wars, the_matrix]

    def get_sample_movies(self):
        """ Returns a list of sample movies to the caller.

        :return: List[] of sample movies.
        """
        return self.sample_movies
