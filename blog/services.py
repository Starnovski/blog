from django.core.paginator import Paginator, EmptyPage, PageNotAnInteger
from django.http import request
from .models import Post, Comment, Category
import json
import urllib

#Some fragments of code are used in more than one view, so I decided to create that file
#to put it here

def pagination(request, object, number_of_posts):
    paginator = Paginator(object, number_of_posts)
    page = request.GET.get('page')
    try:
        posts = paginator.page(page)
    except PageNotAnInteger:
        posts = paginator.page(1)
    except EmptyPage:
        posts = paginator.page(paginator.num_pages)

    return posts, page



def post_stats(categories, posts):
    percents = []
    for category in categories:
        category_posts = Post.objects.filter(category = category.id)
        percents.append(len(category_posts) / len(posts) * 100)

    return percents


def get_category_names(categories):
    category_names = []
    for category in categories:
        category_names.append(category.name)

    return category_names


def get_forum_latest_topic():
    url = "http://localhost:3000/api/v1/topics/latest"
    try:
        response = urllib.request.urlopen(url)
        forum_topic = json.loads(response.read())
    except:
        forum_topic = []

    return forum_topic
