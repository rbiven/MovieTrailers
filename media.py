# -*- coding: utf-8 -*-
"""
Created on Fri Mar 17 14:01:20 2017

@author: Ricky

Building a class for a movie trailer webpage
"""
import webbrowser


class Movie():
    """This class provides a way to store movie related information.
The class Movie has the following instance variables:
       -Title
       -Storyline
       -Poster Image
       -Trailer
    """

    # VALID_RATINGS = ["G", "PG", "PG-13", "R"]

    def __init__(self, movie_title, movie_storyline,
                 poster_image, trailer_youtube):
        self.title = movie_title
        self.storyline = movie_storyline
        self.poster_image_url = poster_image
        self.trailer_youtube_url = trailer_youtube

    # show_trailor will open a trailer URL when the movie poster is selected.
    def show_trailer(self):
        webbrowser.open(self.trailer_youtube_url)
