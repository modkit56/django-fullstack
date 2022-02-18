from django.urls import path

from . import views

urlpatterns = [
    path("", views.StartingPageView.as_view(), name="starting-page"),
    path("posts", views.AllPostsView.as_view(), name="posts-page"),
    path("posts/<slug:slug>", views.InduvidualPostView.as_view(), name="induvidual-post-page"), # is SEO friendly posts/my-first-post
    path("read-later", views.ReadLaterView.as_view(), name="read-later")
]