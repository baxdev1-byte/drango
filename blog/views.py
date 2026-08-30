from django.core.paginator import Paginator, EmptyPage, PageNotAnInteger
from django.shortcuts import render, get_object_or_404
from blog.models import Post, Category

def blog_home(request, **kwargs):
    posts = Post.objects.filter(status=True)
    """if user select posts by categories"""
    if kwargs.get('cat_name') is not None:
        posts = posts.filter(category__name=kwargs['cat_name'])
    """if user select posts by author"""
    if kwargs.get('author_uname') is not None:
        posts = posts.filter(author__username=kwargs['author_uname'])
    """if user select posts by tag"""
    if kwargs.get('tag_name') is not None:
        posts = posts.filter(tag__name=kwargs['tag_name'])

    try:
        posts = Paginator(posts, 2)
        page_number = request.GET.get('page')
        posts = posts.get_page(page_number)
    except PageNotAnInteger:
        posts = posts.get_page(1)
    except EmptyPage:
        posts = posts.get_page(1)

    return render(request, 'blog/blog_home.html', {'posts': posts})

def blog_details(request, pid):
    posts = get_object_or_404(Post, pk=pid, status=1)
    return render(request, 'blog/blog_detail.html', context={'posts': posts})

def blog_category(request, cat_name):
    # posts = Post.objects.filter(status=True, category__name=name)
    category = get_object_or_404(Category, name=cat_name)
    posts = category.blog_posts.filter(status=1)
    return render(request, 'blog/blog_home.html', {'posts': posts})

def blog_search(request):
    posts = Post.objects.filter(status=True)
    if request.method == 'GET':
        if search_key := request.GET.get('s'):
            posts = posts.filter(title__icontains=search_key)
    return render(request, 'blog/blog_home.html', {'posts': posts})




