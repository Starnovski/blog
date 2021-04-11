from django.shortcuts import render, get_object_or_404
from django.core.paginator import Paginator, EmptyPage, PageNotAnInteger
import matplotlib as mpl
from .models import Post, Comment, Category

# Create your views here.

def post_index(request):
    categories = Category.objects.all()
    posts = Post.objects.all()
    paginator = Paginator(posts, 5)
    page = request.GET.get('page')
    try:
        posts = paginator.page(page)
    except PageNotAnInteger:
        posts = paginator.page(1)
    except EmptyPage:
        posts = paginator.page(paginator.num_pages)
    return render(request, 'post_index.html', {'page':page, 'posts': posts, 'categories':categories})

def categories_posts(request, pk):
    categories = Category.objects.all()
    posts = Post.objects.filter(category = pk)
    paginator = Paginator(posts, 5)
    page = request.GET.get('page')
    try:
        posts = paginator.page(page)
    except PageNotAnInteger:
        posts = paginator.page(1)
    except EmptyPage:
        posts = paginator.page(paginator.num_pages)
    return render(request, 'post_index.html', {'page':page, 'posts': posts, 'categories':categories})


def post_details(request, pk):
    categories = Category.objects.all()
    post = get_object_or_404(Post, pk=pk)
    comments = post.comments.all()
    return render(request, 'post_details.html', {'post':post, 'comments':comments, 'categories':categories})
