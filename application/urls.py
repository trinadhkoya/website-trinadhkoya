from django.conf.urls import url

from application import views

app_name = 'application'

urlpatterns = [
    url(r'^$', views.index, name='index'),
    url(r'^about/$', views.about, name='about'),
    url(r'^gallery/$', views.gallery, name='gallery'),
    url(r'^resume/$', views.resume, name='resume'),
    url(r'^blog/$', views.blog, name='blog'),
    url(r'^contact/$', views.contact, name='contact'),

]
