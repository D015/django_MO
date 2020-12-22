from django.shortcuts import render
from django.http import HttpResponse
from .models import Post


def posts_list(request):
    posts = Post.objects.all()

    # post = Post.objects.get(slug='new-slug')
    # print(post)
    # post.slug = 'new-post'
    # post.save()

    return render(request, 'blog/index.html', context={'posts': posts})

def post_detail(request, slug):
    post = Post.objects.get(slug__iexact=slug)
    return render(request, 'blog/post_detail.html', context={'post': post})
