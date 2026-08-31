from django.urls import path
from blog.feeds import LatestEntriesFeed

from . import views

app_name = 'blog'
urlpatterns = [
    path('', views.blog_home , name='blog_home'),
    path('details/<int:pid>', views.blog_details , name='blog_details'),
    path('category/<str:cat_name>', views.blog_home , name='blog_category'),
    path('author/<str:author_uname>', views.blog_home , name='blog_author'),
    path('tag/<str:tag_name>', views.blog_home , name='blog_tag'),
    path('search/', views.blog_search , name='blog_search'),
    path("rss/feed/", LatestEntriesFeed()),

]