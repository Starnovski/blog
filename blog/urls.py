from django.urls import include, path
from . import views


urlpatterns = [
    path('', views.post_index, name='post_index'),
    path('post/<int:pk>', views.post_details, name='post_details'),
    path('category/<int:pk>', views.categories_posts, name='categories_posts'),

]
