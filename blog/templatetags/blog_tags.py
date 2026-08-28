from django import template
from blog.models import Post, Category

register = template.Library()

@register.simple_tag(name='posts')
def func():
    posts = Post.objects.all()
    return posts
@register.filter
def snippet(value, arg=20):
    return f'{value[:arg]}...'

@register.inclusion_tag('blog/blog_latestposts.html')
def latestposts(arg=2):
    posts = Post.objects.filter(status=1).order_by('-published_date')[:arg]
    return {'posts': posts}

@register.inclusion_tag('blog/blog_postscategories.html')
def postscategory():
    categories = Category.objects.all()
    cat_dict = {}
    for cat in categories:
        cat_dict[cat] = Post.objects.filter(status=1, category=cat).count()
    return {'categories': cat_dict}