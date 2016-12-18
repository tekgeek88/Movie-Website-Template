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


from media import Movie, Movies
import time
import fresh_tomatoes
import sys
from sample_movies import SampleMovies


def get_movie_from_user():
    """Prompts the user for movie details

    Gets movie information like title, storyline, image url, and YouTube link in
    order to create a movie object

    :return: A newly created movie object
    """

    new_movie = Movie(raw_input("Enter movie title: "),
                            raw_input("Enter movie storyline: "),
                            raw_input("Enter movie's poster image url: "),
                            raw_input("Enter movie's trailer link from YouTube: "))

    return new_movie

# Run the main program
while (True):
    # Greet user and display a the Main Menu
    print("\n\n\n********************************************")
    print("**                                        **")
    print("**     Favorite Movies Page Generator     **")
    print("**            By: Carl Argabright         **")
    print("**                                        **")
    print("********************************************\n\n\n")
    print("Main Menu\n\n")
    print("(0) Load sample movie database\n")
    print("(1) Add Movies")
    print("(2) Remove Movie")
    print("(3) Update Movies Page")
    print("(4) Exit program\n")

    # Get user input
    userInput = raw_input("Enter your selection: ")

    # A series of control structures that define the methods
    # called by the users selection on the main menu
    if userInput == "0":
        print("Loading sample movie database...")
        time.sleep(1)  # Makes program appear to have a large database
        database.movies = SampleMovies().get_sample_movies()
        fresh_tomatoes.open_movies_page(database.get_movies())
        time.sleep(1)
    elif userInput == "1":
        print("Preparing to add Movies")
        time.sleep(1)
        has_another = False
        while True:
            database.add_movie(get_movie_from_user())
            print("\nSuccess!\n")
            has_another = raw_input("Add another movie (y/n): ")
            if has_another != "y":
                break
        time.sleep(1)
    elif userInput == "2":
        print("Preparing to remove movies...")
        time.sleep(1)
        has_another = False
        while True:
            database.remove_movie(raw_input("Which movie title would you like to remove (Must be typed exacty!): "))
            has_another = raw_input("Delete another movie? (y/n): ")
            if has_another != "y":
                break

    elif userInput == "3":
        print("Updating movies page")
        time.sleep(1)
        fresh_tomatoes.open_movies_page(database.get_movies())
    elif userInput == "4":
        print("\n\nThank you for using the Movie Page Generator!\n")
        print("Cleaning up program...")
        time.sleep(1)
        print("Closing program...")
        time.sleep(1)
        sys.exit()
    else:
        print("oops! try again...")
        time.sleep(1)
