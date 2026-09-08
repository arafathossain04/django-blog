from django.contrib import admin
from .models import AboutUs, SocialLink
# Register your models here.

class AboutAdmin(admin.ModelAdmin):
    def has_add_permission(self, request):
        count = AboutUs.objects.all().count()
        if count == 0:
            return True
        return False
admin.site.register(AboutUs, AboutAdmin)
admin.site.register(SocialLink)