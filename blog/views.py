from django.shortcuts import render
from django.http import HttpResponse


def posts_list(request):
    n = 'First name'
    names = {'name': n}
    return render(request, 'blog/index.html', names)
