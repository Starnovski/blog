from django.shortcuts import render, get_object_or_404
from .services import *
from .forms import CommentForm
from django.http import HttpResponseRedirect
import io
import urllib, base64
from .models import Post, Comment, Category

# Create your views here.

def post_index(request):
    categories = Category.objects.all()
    posts = Post.objects.all()

    #Getting stats and category names to create diagram
    percents = post_stats(categories, posts)
    category_names = get_category_names(categories)
    counter = 0
    cat_stats = {}
    for category_name in category_names:
        cat_stats[category_name] = percents[counter]
        counter += 1



    forum_topic = get_forum_latest_topic()

    #Using 'pagination' function, written down in services.py
    posts, page = pagination(request, posts, 5)

    return render(request, 'post_index.html', {'page':page, 'posts': posts, 'categories':categories, 'cat_stats':cat_stats, 'forum_topic':forum_topic,})


def categories_posts(request, pk):
    categories = Category.objects.all()
    posts = Post.objects.filter(category = pk)

    #Using 'pagination' function, written down in services.py
    posts, page = pagination(request, posts, 5)

    return render(request, 'post_index.html', {'page':page, 'posts': posts, 'categories':categories})


def post_details(request, pk):
    categories = Category.objects.all()
    post = get_object_or_404(Post, pk=pk)
    comments = post.comments.all()
    #Getting a form
    if request.method == 'POST':
        form = CommentForm(request.POST)
        if form.is_valid():
            comment = form.save(commit=False)
            comment.post = post
            comment.save()
            form = CommentForm()
            return HttpResponseRedirect('/')
    else:
        form = CommentForm()
    return render(request, 'post_details.html', {'post':post, 'comments':comments, 'categories':categories,'form':form})
