from django.shortcuts import render
from .models import Post

# Create your views here.

def index(request):
    posts = Post.objects.all()
    return render(request, 'index.html', {'posts': posts})

def post(request, id):
    post = Post.objects.get(id=int(id))
    return render(request, 'post.html', {'post': post})