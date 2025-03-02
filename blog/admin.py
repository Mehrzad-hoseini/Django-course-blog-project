from django.contrib import admin
from .models import Post

# Register your models here.

class PostAdmin(admin.ModelAdmin):
    list_display = ('title', 'status', 'datetime_updated',)
    ordering = ('status', 'datetime_updated',)


admin.site.register(Post, PostAdmin)

