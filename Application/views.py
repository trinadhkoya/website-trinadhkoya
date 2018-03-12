from django.shortcuts import render


# Create your views here.
def index(request):
    return render(request, 'application/index.html')


def about(request):
    return render(request, 'application/about.html')


def gallery(request):
    return render(request, 'application/gallery.html')


def contact(request):
    return render(request, 'application/contact.html')


def blog(request):
    return render(request, 'application/blog.html')


def resume(request):
    return render(request, 'application/resume.html')
