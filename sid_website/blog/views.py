from datetime import date

from django.shortcuts import render

# temp dummy data for dynamic rendering
all_posts = [
    {
        "slug": "colors",
        "image": "colors.jpg",
        "author": "Sid",
        "date": date(2022, 2, 16),
        "title": "Colors",
        "excerpt": """Lorem ipsum dolor sit amet consectetur adipisicing elit. Quaerat laborum odio dignissimos hic error laboriosam, doloribus eum nobis
                      asperiores totam dolorem fugit nam quas accusamus animi, corporis sapiente ad aspernatur.
        """,
        "content": """
                    Lorem ipsum dolor sit amet consectetur adipisicing elit. Quaerat laborum odio dignissimos 
                    hic error laboriosam, doloribus eum nobis asperiores totam dolorem fugit nam quas accusamus
                    animi, corporis sapiente ad aspernatur.

                    Lorem ipsum dolor sit amet consectetur adipisicing elit. Quaerat laborum odio dignissimos 
                    hic error laboriosam, doloribus eum nobis asperiores totam dolorem fugit nam quas accusamus
                    animi, corporis sapiente ad aspernatur.

                    Lorem ipsum dolor sit amet consectetur adipisicing elit. Quaerat laborum odio dignissimos 
                    hic error laboriosam, doloribus eum nobis asperiores totam dolorem fugit nam quas accusamus
                    animi, corporis sapiente ad aspernatur.

                    Lorem ipsum dolor sit amet consectetur adipisicing elit. Quaerat laborum odio dignissimos 
                    hic error laboriosam, doloribus eum nobis asperiores totam dolorem fugit nam quas accusamus
                    animi, corporis sapiente ad aspernatur.
        """
    },
    {
        "slug": "robot",
        "image": "robot.jpg",
        "author": "Sid",
        "date": date(2022, 2, 15),
        "title": "Robot",
        "excerpt": """Lorem ipsum dolor sit amet consectetur adipisicing elit. Quaerat laborum odio dignissimos hic error laboriosam, doloribus eum nobis
                      asperiores totam dolorem fugit nam quas accusamus animi, corporis sapiente ad aspernatur.
        """,
        "content": """
                    Lorem ipsum dolor sit amet consectetur adipisicing elit. Quaerat laborum odio dignissimos 
                    hic error laboriosam, doloribus eum nobis asperiores totam dolorem fugit nam quas accusamus
                    animi, corporis sapiente ad aspernatur.

                    Lorem ipsum dolor sit amet consectetur adipisicing elit. Quaerat laborum odio dignissimos 
                    hic error laboriosam, doloribus eum nobis asperiores totam dolorem fugit nam quas accusamus
                    animi, corporis sapiente ad aspernatur.

                    Lorem ipsum dolor sit amet consectetur adipisicing elit. Quaerat laborum odio dignissimos 
                    hic error laboriosam, doloribus eum nobis asperiores totam dolorem fugit nam quas accusamus
                    animi, corporis sapiente ad aspernatur.

                    Lorem ipsum dolor sit amet consectetur adipisicing elit. Quaerat laborum odio dignissimos 
                    hic error laboriosam, doloribus eum nobis asperiores totam dolorem fugit nam quas accusamus
                    animi, corporis sapiente ad aspernatur.
        """
    },
    {
        "slug": "sunset",
        "image": "sunset.jpg",
        "author": "Sid",
        "date": date(2022, 2, 14),
        "title": "Sunset",
        "excerpt": """Lorem ipsum dolor sit amet consectetur adipisicing elit. Quaerat laborum odio dignissimos hic error laboriosam, doloribus eum nobis
                      asperiores totam dolorem fugit nam quas accusamus animi, corporis sapiente ad aspernatur.
        """,
        "content": """
                    Lorem ipsum dolor sit amet consectetur adipisicing elit. Quaerat laborum odio dignissimos 
                    hic error laboriosam, doloribus eum nobis asperiores totam dolorem fugit nam quas accusamus
                    animi, corporis sapiente ad aspernatur.

                    Lorem ipsum dolor sit amet consectetur adipisicing elit. Quaerat laborum odio dignissimos 
                    hic error laboriosam, doloribus eum nobis asperiores totam dolorem fugit nam quas accusamus
                    animi, corporis sapiente ad aspernatur.

                    Lorem ipsum dolor sit amet consectetur adipisicing elit. Quaerat laborum odio dignissimos 
                    hic error laboriosam, doloribus eum nobis asperiores totam dolorem fugit nam quas accusamus
                    animi, corporis sapiente ad aspernatur.

                    Lorem ipsum dolor sit amet consectetur adipisicing elit. Quaerat laborum odio dignissimos 
                    hic error laboriosam, doloribus eum nobis asperiores totam dolorem fugit nam quas accusamus
                    animi, corporis sapiente ad aspernatur.
        """
    },

]

def get_date(post):
    return post['date']

# Create your views here.

def starting_page(request):
    sorted_posts = sorted(all_posts, key=get_date)
    latest_posts = sorted_posts[-2:]
    return render(request, "blog/index.html", {
        "posts": latest_posts
    })

def posts(request):
    return render(request, "blog/all-posts.html", {
        "all_posts": all_posts
    })

def induvidual_post(request, slug):
    identified_post = next(post for post in all_posts if post['slug'] == slug)
    return render(request, "blog/post-detail.html", {
        "post": identified_post
    })