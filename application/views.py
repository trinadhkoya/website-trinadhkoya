import logging

logger = logging.getLogger(__name__)

from django.shortcuts import render


# Create your views here.
def index(request):
    logger.info('what is this', request)
    return render(request, 'index.html')


def about(request):
    print("request is", request)

    return render(request, 'about.html')


def gallery(request):
    print("request is", request)

    return render(request, 'gallery.html')


def contact(request):
    print("request is", request)

    return render(request, 'contact.html')


def blog(request):
    print("request is", request)

    return render(request, 'blog.html')


def resume(request):
    print("request is", request)

    return render(request, 'resume.html')
