from django.contrib import admin

# Register your models here.

from .models import Tag, Category, Post

admin.site.register(Tag)
admin.site.register(Category)
admin.site.register(Post)
