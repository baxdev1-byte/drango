from django.shortcuts import render, get_object_or_404
from blog.models import Post

def blog_home(request):
    posts = Post.objects.filter(status=1)
    return render(request, 'blog/blog_home.html', {'posts': posts})

def blog_details(request, pid):
    posts = get_object_or_404(Post, pk=pid, status=1)
    return render(request, 'blog/blog_detail.html', context={'posts': posts})



