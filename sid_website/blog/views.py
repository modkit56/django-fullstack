from re import template
from django.shortcuts import render, get_object_or_404
from django.views.generic import ListView, DetailView

from . models import Post

# Create your views here.

class StartingPageView(ListView):
    template_name = "blog/index.html"
    model = Post
    ordering = ["-date"]
    context_object_name = "posts" # provided under this name

    def get_queryset(self):
        queryset = super().get_queryset()
        data = queryset[:3]
        return data

class AllPostsView(ListView):
    template_name = "blog/all-posts.html"
    model = Post
    ordering = ["-date"]
    context_object_name = "all_posts"

# no need to query manually as we are inheriting from the DefaultView which does the job for us
class InduvidualPostView(DetailView):
    template_name = "blog/post-detail.html"
    model = Post

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context["post_tags"] = self.object.tags.all()
        return context


# def starting_page(request):
#     latest_posts = Post.objects.all().order_by("-date")[:3] # this changes to a SQL Query (no performance hit)
#     return render(request, "blog/index.html", {
#         "posts": latest_posts
#     })

# def posts(request):
#     all_posts = Post.objects.all().order_by("-date")
#     return render(request, "blog/all-posts.html", {
#         "all_posts": all_posts
#     })

# def induvidual_post(request, slug):
#     identified_post = get_object_or_404(Post, slug=slug) # slug on the right side is the argument of the function, other one is attribute
#     return render(request, "blog/post-detail.html", {
#         "post": identified_post,
#         "post_tags": identified_post.tags.all()
#     })