from django.urls import path

from . import views

urlpatterns = [
    path("", views.starting_page, name="starting-page"),
    path("posts", views.posts, name="posts-page"),
    path("posts/<slug:slug>", views.induvidual_post, name="induvidual-post-page") # is SEO friendly posts/my-first-post
]