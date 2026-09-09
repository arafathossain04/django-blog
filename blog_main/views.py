# modules
from django.shortcuts import render, redirect
from blogs.models import *
from assignments.models import *
from .forms import RegistrationForm

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

def register(request):
    if request.method == 'POST':
        form = RegistrationForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('home')
        else:
            print(form.errors)
    else:
        form = RegistrationForm()
    context = {
        'form': form
    }
    return render(request, 'register.html', context)