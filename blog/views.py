from django.shortcuts import render

def blog_home(request):
    return render(request, 'blog/blog_home.html')

def blog_details(request):
    return render(request, 'blog/blog_detail.html')

