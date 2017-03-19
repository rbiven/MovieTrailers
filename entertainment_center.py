# -*- coding: utf-8 -*-
"""
Created on Fri Mar 17 14:06:41 2017

@author: Ricky

This file creates a list of instances for the Movie class.  Each instance has 
the following variables: Title, Storyline, Poster Image, and Trailor link.
"""

import media
import fresh_tomatoes

toy_story = media.Movie("Toy Story",
                    "Woody (Tom Hanks), a good-hearted cowboy doll who belongs to a young"
                    " boy named Andy (John Morris), sees his position as Andy's favorite "
                    "toy jeopardized when his parents buy him a Buzz Lightyear (Tim Allen)" 
                    " action figure.",
                    "http://vignette4.wikia.nocookie.net/disney/images/8/80/Toy_Story_-_Poster.jpg/revision/latest?cb=20150108180742",
                    "https://www.youtube.com/watch?v=KYz2wyBy3kc")

moana = media.Movie("Moana",
                    "An adventurous teenager sails out on a daring mission to save her people.",
                    "http://www.impawards.com/2016/posters/moana_ver8.jpg",
                    "https://www.youtube.com/watch?v=LKFuXETZUsI")
                    
dredd = media.Movie("Dredd",
                    "Mega City One is a vast, violent metropolis where felons rule the "
                    "streets. The only law lies with cops called 'judges,' who act as judge," 
                    " jury and executioner, and Dredd (Karl Urban) is one of the city's most" 
                    " feared.",
                    "http://www.impawards.com/2012/posters/dredd_ver2.jpg",
                    "https://www.youtube.com/watch?v=qVIba2N6MTA")
                    
brave = media.Movie("Brave",
                    "Merida (Kelly Macdonald), the impetuous but courageous daughter "
                    "of Scottish King Fergus (Billy Connolly) and Queen Elinor (Emma "
                    "Thompson), is a skilled archer who wants to carve out her own "
                    "path in life.",
                    "http://cdn.collider.com/wp-content/uploads/brave-movie-poster1.jpg",
                    "https://www.youtube.com/watch?v=TEHWDA_6e3M")
                    
big_fish = media.Movie("Big Fish",
                    "When his father, Edward Bloom, is on his deathbed, William tries "
                    "to uncover the truth of his father's past through his father's "
                    "exaggerated story.",
                    "http://www.impawards.com/2003/posters/big_fish.jpg",
                    "https://www.youtube.com/watch?v=M3YVTgTl-F0")
                    
incredibles = media.Movie("The Incredibles",
                    "Married superheroes Mr. Incredible (Craig T. Nelson) and Elastigirl "
                    "(Holly Hunter) are forced to assume mundane lives as Bob and Helen "
                    "Parr after all super-powered activities have been banned by the "
                    "government.",
                    "http://www.impawards.com/2004/posters/incredibles_ver9.jpg",
                    "https://www.youtube.com/watch?v=fwHlyurv-0U")
                        
movies = [toy_story, moana, dredd, brave, big_fish, incredibles]                        
                       
# fresh_tomatoes is a python file created to build the movie trailor website
# with the instances provided above. 
fresh_tomatoes.open_movies_page(movies)

print(media.Movie.__doc__)