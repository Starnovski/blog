from django.shortcuts import render
from .models import Post

# Create your views here.

def post_index(request):
    posts = Post.objects.all()
    return render(request, 'post_index.html', {'posts': posts})

def post_details(request, pk):
    post = Post.objects.get(pk=pk)
    return render(request, 'post_details.html', {'post':post})
