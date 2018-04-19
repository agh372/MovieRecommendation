import sys, os 
import pandas as pd

os.environ.setdefault("DJANGO_SETTINGS_MODULE", "movierecommendation.settings")

import django
django.setup()

from movies.models import Movie 


def save_movie_from_row(movie_row):
    movie = Movie()
    movie.movie_id = movie_row[0]
    movie.name = movie_row[1]
    movie.genre = movie_row[2]
    movie.save()
    
    
if __name__ == "__main__":
    
    if len(sys.argv) == 2:
        print "Reading from file " + str(sys.argv[1])
        movies_df = pd.read_csv(sys.argv[1])
        print movies_df

        movies_df.apply(
            save_movie_from_row,
            axis=1
        )

        print "There are {} movies".format(Movie.objects.count())
        
    else:
        print "Please, provide Movie file path"
