from django.shortcuts import render, get_object_or_404
from .models import AboutUs

# Create your views here.

def about_us(request):
    about = get_object_or_404(AboutUs)
    
    context = {
        'about': about,
    }
    return render(request, 'about.html', context)