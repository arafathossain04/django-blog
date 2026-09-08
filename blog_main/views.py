# modules
from django.shortcuts import render
from blogs.models import *
from assignments.models import *

#main work
def home(request):
    featured_posts = Blog.objects.filter(is_featured=True, status='published').order_by("-created_at")
    posts = Blog.objects.filter(is_featured=False, status='published')
    try:
        about = AboutUs.objects.get()
    except:
        about = None
    
    context = {
        'featured_posts': featured_posts,
        'posts': posts,
        'about': about,
    }
    return render(request, 'home.html', context)