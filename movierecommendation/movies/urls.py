from django.conf.urls import url

from . import views

urlpatterns = [
    # ex: /
    url(r'^$', views.review_list, name='review_list'),
    url(r'^review/(?P<review_id>/d+)/$', views.review_detail, name='review_detail'),
    url(r'^movie$', views.movie_list, name='movie_list'),
    url(r'^movie/(?P<movie_id>/d+)/$', views.movie_detail, name='movie_detail'),
    url(r'^movie/(?P<movie_id>/d+)/add_review/$', views.add_review, name='add_review'),
    
]
