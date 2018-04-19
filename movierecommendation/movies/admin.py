# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.contrib import admin

from .models import Movie, Review

class ReviewAdmin(admin.ModelAdmin):
    model = Review
    list_display = ('movie', 'rating', 'user_name', 'pub_date')
    list_filter = ['pub_date', 'user_name']
    search_fields = ['comment']
    
admin.site.register(Movie)
admin.site.register(Review, ReviewAdmin)

