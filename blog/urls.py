from . import views
from django.urls import include
from django.urls import path
from .feeds import LatestPostsFeed, AtomSiteNewsFeed
from .views import *


urlpatterns = [
    path("feed/rss", LatestPostsFeed(), name="post_feed"),
    path("feed/atom", AtomSiteNewsFeed()),
    path("", views.PostList.as_view(), name="home"),
    path("<slug:slug>/", views.post_detail, name="post_detail"),
	path('q/search/', searchposts, name='searchposts'),
	path('about', about, name='about'),
	path('contact', contact, name='contact'),
	path('privacy-and-privacy', privacy, name='privacy'),
	path('disclaimer', disclaimer, name='disclaimer'),
	path('terms-and-condition', terms, name='terms'),
]