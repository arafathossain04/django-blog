from django.db import models

# Create your models here.

class AboutUs(models.Model):
    about_heading = models.CharField(max_length=20)
    establish_time = models.CharField(max_length=20)
    mission = models.TextField(max_length=250)
    about_image = models.ImageField(upload_to='uploads/%Y/%m/%d')
    about_body = models.TextField(max_length=1000)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    
    class Meta:
        verbose_name_plural = 'About'
    
    def __str__(self):
        return self.about_heading

class SocialLink(models.Model):
    platform = models.CharField(max_length=20)
    link = models.URLField(max_length=200)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    
    def __str__(self):
        return self.platform