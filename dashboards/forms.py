from django import forms
from blogs.models import Category, Blog
from django.contrib.auth.models import User
from django.contrib.auth.forms import UserCreationForm


class CategoryForm(forms.ModelForm):
    class Meta:
        model = Category
        fields = '__all__'

class PostForm(forms.ModelForm):
    class Meta:
        model = Blog
        fields = [
            'title',
            'category',
            'featured_image',
            'short_description',
            'blog_body',
            'status',
            'is_featured'
            ]

class UserForm(UserCreationForm):
    class Meta:
        model = User
        fields = ['first_name', 'last_name', 'username', 'email', 'password1', 'password2', 'is_active', 'is_staff', 'groups']

class EditUserForm(forms.ModelForm):
    class Meta:
        model = User
        fields = ['first_name', 'last_name', 'username', 'email', 'is_active', 'is_staff', 'groups']