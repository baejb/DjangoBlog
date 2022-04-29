from django.shortcuts import render

# Create your views here.
from blog.models import Post


def landing(request):
    recent_posts: Post.object.order_by('-pk')[:3]
    return render(request, 'single_pages/landing.html',{
        'recent_post': recent_posts,
    })

def about_me(request):
    return render(request, 'single_pages/about_me.html')