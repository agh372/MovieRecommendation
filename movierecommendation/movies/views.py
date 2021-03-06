# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.shortcuts import get_object_or_404, render
from django.http import HttpResponseRedirect
from django.core.urlresolvers import reverse
from .models import Review, Movie
from .forms import ReviewForm
from django.core.paginator import Paginator
import datetime

from django.contrib.auth.decorators import login_required


def review_list(request):
    latest_review_list = Review.objects.order_by('-pub_date').all()
    page = request.GET.get('page', 1)
    paginator = Paginator(latest_review_list, 252)
    try:
        queryset = paginator.page(page)
    except PageNotAnInteger:
        queryset = paginator.page(1)
    except EmptyPage:
        queryset = paginator.page(paginator.num_pages)
    context = {'latest_review_list':queryset}
    return render(request, 'movies/review_list.html', context)


def review_detail(request, review_id):
    review = get_object_or_404(Review, pk=review_id)
    return render(request, 'movies/review_detail.html', {'review': review})


def movie_list(request):
    for x in Review.objects.all().iterator(): x.delete()     
    movie_list = Movie.objects.order_by('-name').all()
    page = request.GET.get('page', 1)
    paginator = Paginator(movie_list, 84)
    try:
        queryset = paginator.page(page)
    except PageNotAnInteger:
        queryset = paginator.page(1)
    except EmptyPage:
        queryset = paginator.page(paginator.num_pages)
    context = {'movie_list':queryset}
    return render(request, 'movies/movie_list.html', context)


def movie_detail(request, movie_id):
    movie = get_object_or_404(Movie, pk=movie_id)
    return render(request, 'movies/movie_detail.html', {'movie': movie})


@login_required
def add_review(request, movie_id):
    movie = get_object_or_404(Movie, pk=movie_id)
    if request.POST:
        form = ReviewForm(request.POST)
    else:
        form = ReviewForm()  
    if form.is_valid():
        user_name = request.user.username
        review = form.save(commit=False) # commit = False means that this instantiate but not save a Review model object
        review.movie = movie
        review.user_name = user_name # Why use this instead of a ForeignKey to user?
        review.pub_date = datetime.datetime.now() # works as long as pub_date is a DateTimeField
        review.save() # save to the DB now
        return HttpResponseRedirect(reverse('movies:movie_detail', args=(movie.id,))) # THIS will redirect only upon form save
    return render(request, 'movies/movie_detail.html', {'movie': movie, 'form': form})


def user_review_list(request, username=None):
    if not username:
        username = request.user.username
    latest_review_list = Review.objects.filter(user_name=username).order_by('-pub_date')
    context = {'latest_review_list':latest_review_list, 'username':username}
    return render(request, 'movies/user_review_list.html', context)


@login_required
def user_recommendation_list(request):
    return 0