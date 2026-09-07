from django.shortcuts import render, get_object_or_404
from .models import Blog, Category

# Create your views here.
def posts_by_category(request, category_id):
    posts = Blog.objects.filter(status= 'published', category = category_id)
    category = get_object_or_404(Category, id= category_id)
    context = {
        'posts': posts,
        'category': category,
    }
    return render(request, 'posts_by_cat.html', context)

def blogs(request, slug):
    single_blog = get_object_or_404(Blog, slug=slug, status= 'published')
    
    context = {
        'single_blog': single_blog,
    }
    return render(request, 'blogs.html', context)