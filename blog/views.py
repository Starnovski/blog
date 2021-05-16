from django.shortcuts import render, get_object_or_404
from .services import *
import matplotlib.pyplot as ppl
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

    #Creating image of matplotlib diagram
    ppl.clf()
    ppl.bar((category_names), (percents))
    fig = ppl.gcf()
    buf = io.BytesIO()
    fig.savefig(buf, format='png')
    buf.seek(0)
    string = base64.b64encode(buf.read())
    uri = urllib.parse.quote(string)

    forum_topic = get_forum_latest_topic()

    #Using 'pagination' function, written down in services.py
    posts, page = pagination(request, posts, 5)

    return render(request, 'post_index.html', {'page':page, 'posts': posts, 'categories':categories, 'data':uri, 'percents':percents, 'forum_topic':forum_topic})


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
    return render(request, 'post_details.html', {'post':post, 'comments':comments, 'categories':categories})
