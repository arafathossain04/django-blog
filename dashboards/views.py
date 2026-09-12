from django.shortcuts import render, redirect, get_object_or_404
from blogs.models import Category, Blog
from django.contrib.auth.models import User
from django.contrib.auth.decorators import login_required
from .forms import *
from django.template.defaultfilters import slugify

# Create your views here.
@login_required(login_url='login')
def dashboard(request):
    category_count = Category.objects.all().count()
    post_count = Blog.objects.all().count()
    context = {
        'category_count': category_count,
        'post_count': post_count,
    }
    
    return render(request, 'dashboard/dashboard.html', context)

# CRUD operation for Categories
#read
def categories(request):
    return render(request, 'dashboard/categories.html')
#create
def add_category(request):
    if request.method == 'POST':
        form = CategoryForm(request.POST)
        if form.is_valid:
            form.save()
            return redirect('categories')
        else:
            print(form.errors)
    else:
        form = CategoryForm()
    context = {
        'form': form,
    }
    return render(request, 'dashboard/add_category.html', context)
#update
def edit_category(request, pk):
    category = get_object_or_404(Category, pk=pk)
    if request.method == 'POST':
        form = CategoryForm(request.POST, instance=category)
        if form.is_valid():
            form.save()
            return redirect('categories')
        else:
            print(form.errors)
    else:
        form = CategoryForm(instance=category)
    context = {
        'form': form,
        'category': category,
    }
    return render(request, 'dashboard/edit_category.html', context)
#delete
def delete_category(request, pk):
    category = get_object_or_404(Category, pk=pk)
    category.delete()
    return redirect('categories')

# CRUD operation for posts
# read
def posts(request):
    posts = Blog.objects.all()
    
    context = {
        'posts': posts,
    }
    return render(request, 'dashboard/posts.html', context)

# create
def add_post(request):
    if request.method == 'POST':
        form = PostForm(request.POST, request.FILES)
        if form.is_valid():
            post = form.save(commit=False) # temporarily saving
            post.author = request.user
            title = form.cleaned_data['title']
            post.slug = slugify(title)
            post.save()
            return redirect('posts')
        else:
            print(form.errors)
    else:
        form = PostForm()
    
    context = {
        'form': form,
    }
    return render(request, 'dashboard/add_post.html', context)

#update
def edit_post(request, pk):
    post = get_object_or_404(Blog, pk=pk)
    if request.method == 'POST':
        form = PostForm(request.POST, request.FILES, instance=post)
        if form.is_valid():
            post = form.save()
            title = form.cleaned_data['title']
            post.slug = slugify(title)
            post.save()
            return redirect('posts')
        else:
            print(form.errors)
    else:
        form = PostForm(instance=post)
    
    context = {
        'form': form,
        'post': post,
    }
    return render(request, 'dashboard/edit_post.html', context)

# delete
def delete_post(request, pk):
    post = get_object_or_404(Blog, pk=pk)
    post.delete()
    return redirect('posts')

# CRUD operation for users
# read
def users(request):
    users = User.objects.all().order_by('-date_joined')
    
    context = {
        'users': users,
    }
    return render(request, 'dashboard/users.html', context)

# create
def add_user(request):
    if request.method == 'POST':
        form = UserForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('users')
        else:
            print(form.errors)
    else:
        form = UserForm()
    
    context = {
        'form': form,
    }
    return render(request, 'dashboard/add_user.html', context)

# update
def edit_user(request, pk):
    user = get_object_or_404(User, pk=pk)
    if request.method == 'POST':
        form = EditUserForm(request.POST, instance=user)
        if form.is_valid():
            form.save()
            return redirect('users')
        else:
            print(form.errors)
    else:
        form = EditUserForm(instance=user)
        
    context = {
        'form': form,
        'user': user,
    }
    return render(request, 'dashboard/edit_user.html', context)

# delete
def delete_user(request, pk):
    user = get_object_or_404(User, pk=pk)
    user.delete()
    return redirect('users')