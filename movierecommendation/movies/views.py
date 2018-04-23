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
    latest_review_list = Review.objects.order_by('-pub_date')[:9]
    context = {'latest_review_list':latest_review_list}
    return render(request, 'movies/review_list.html', context)


def review_detail(request, review_id):
    review = get_object_or_404(Review, pk=review_id)
    return render(request, 'movies/review_detail.html', {'review': review})


# def movie_list(request):
#     movie_list = Movie.objects.order_by('-name')
#     print "There are {} movies".format(Movie.objects.count())
#     paginator = Paginator(movie_list, 21)
#     queryset = paginator.page(1)
#     context = {'movie_list':queryset}
#     return render(request, 'movies/movie_list.html', context)


def movie_list(request):
    current_page = request.GET.get('page' ,'1')
    current_page =int(current_page)
    limit = (21 * current_page)
    offset = (limit - 21)
    movie_list = Movie.objects.order_by('-name')[offset:limit]  # limiting movies based on current_page
    total_movies = Movie.objects.all().count()  
    total_pages = total_movies / 21
    if total_movies % 21 != 0:
        total_pages += 1 # adding one more page if the last page will contains less movies 
        pagination_string = make_pagination_html(current_page, total_pages)
    return render(request, 'movies/movie_list.html', {'movie_list': movie_list, 'pagination': pagination_string})

 

def make_pagination_html(current_page, total_pages):
    count_limit = 30
    current_page = int(current_page)
    pagination_string = ""
    if current_page > 1:
        pagination_string += '<a href="?page=%s">←</a>' % (current_page -1)
    pagination_string += "<li class='active'><a href='?page=%s' >%s</a></li>"  % (current_page, current_page)
    count = 1
    value = current_page - 1
    while value > 0 and count_limit < 5:
        pagination_string = "<li><a href='?page=%s'>%s</a></li>" % (value, value) + pagination_string
        value -= 1
        count_limit += 1
    value = current_page + 1
    while value < total_pages and count_limit < 10:
        pagination_string =  pagination_string +"<li><a href='?page=%s'>%s</a></li>" % (value, value)
        value += 1
        count_limit +=1
    if current_page < total_pages:
        pagination_string += '<a href="?page=%s">→</a>' % (current_page + 1)
    return pagination_string


def movie_detail(request, wine_id):
    movie = get_object_or_404(Movie, pk=movie_id)
    return render(request, 'movies/movie_detail.html', {'movie': movie})

def add_review(request, movie_id):
    movie = get_object_or_404(Movie, pk=movie_id)
    form = ReviewForm(request.POST)
    if form.is_valid():
        rating = form.cleaned_data['rating']
        user_name = form.cleaned_data['user_name']
        review = Review()
        review.movie = movie
        review.user_name = user_name
        review.rating = rating
        review.pub_date = datetime.datetime.now()
        review.save()
        return HttpResponseRedirect(reverse('movies:movie_detail', args=(movie.id,)))

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