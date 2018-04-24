import sys, os 
import pandas as pd
import datetime

os.environ.setdefault("DJANGO_SETTINGS_MODULE", "movierecommendation.settings")

import django
django.setup()

from movies.models import Review, Movie 


def save_review_from_row(review_row):
    review = Review()
    review.user_id = review_row[0]
    try:
        review.movie = Movie.objects.get(id=review_row[1])
    except Movie.DoesNotExist:
        review.movie = Movie.objects.get(id=8695)
    review.rating = review_row[2]
    review.pub_date = datetime.datetime.now()
    if review.movie != Movie.objects.get(id=8695):
        review.save()
    
    
if __name__ == "__main__":
    
    if len(sys.argv) == 2:
        print "Reading from file " + str(sys.argv[1])
        reviews_df = pd.read_csv(sys.argv[1])
        print reviews_df

        reviews_df.apply(
            save_review_from_row,
            axis=1
        )

        print "There are {} reviews in DB".format(Review.objects.count())
        
    else:
        print "Please, provide Reviews file path"
