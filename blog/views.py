from django.shortcuts import render
from .models import Tag, Category, Post
# Create your views here.
def index(request):
    tags = Tag.objects.all()
    categories = Category.objects.all()
    posts = Post.objects.all()
    context = {'tags': tags, 'posts': posts, 'categories': categories}
    return render(request,'blog/index.html', context)
