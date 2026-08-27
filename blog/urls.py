from django.urls import path
from . import views

app_name = 'blog'
urlpatterns = [
    path('', views.blog_home , name='blog_home'),
    path('details/<int:pid>', views.blog_details , name='blog_details'),
    path('test/', views.test , name='blog_test'),

]