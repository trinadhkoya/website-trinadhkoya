import logging

from application.models import Post

logger = logging.getLogger(__name__)

from django.shortcuts import render


# Create your views here.
def index(request):
    logger.info('what is this', request)
    return render(request, 'index.html', {'title': 'Welcome to HomePage - Trinadh Koya'})


def about(request):
    print("request is", request)

    return render(request, 'about.html', {'title': 'About - Trinadh Koya'})


def gallery(request):
    print("request is", request)

    return render(request, 'gallery.html', {'title': 'Gallery - Trinadh Koya'})


def contact(request):
    print("request is", request)

    return render(request, 'contact.html', {'title': 'Contact - Trinadh Koya'})


def blog(request):
    posts = Post.objects.all()
    return render(request, 'blog.html', {'title': 'Blog - Trinadh Koya', 'posts': posts})


def resume(request):
    print("request is", request)

    return render(request, 'resume.html', {'title': 'Resume - Trinadh Koya'})
