# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models
from django.contrib.auth.models import User
import numpy as np


class Movie(models.Model):
    movie_id = models.IntegerField()
    name = models.CharField(max_length=200)
    genre = models.CharField(max_length=200)

    def average_rating(self):
        all_ratings = map(lambda x: x.rating, self.review_set.all())
        return np.mean(all_ratings)
        
    def __unicode__(self):
        return self.name


class Review(models.Model):
    RATING_CHOICES = (
        (1, '1'),
        (2, '2'),
        (3, '3'),
        (4, '4'),
        (5, '5'),
    )
    movie = models.ForeignKey(Movie)
    pub_date = models.DateTimeField('date published')
    user_id = models.IntegerField(max_length=100)  
    rating = models.IntegerField(choices=RATING_CHOICES)

class Tags(models.Model):
    movie = models.ForeignKey(Movie)
    pub_date = models.DateTimeField('date published')
    user_id = models.IntegerField(max_length=100)  
    tags = models.CharField(max_length=100)

class Cluster(models.Model):
    name = models.CharField(max_length=100)
    users = models.ManyToManyField(User)

    def get_members(self):
        return "\n".join([u.username for u in self.users.all()])

