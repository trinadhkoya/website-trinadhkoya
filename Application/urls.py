from django.conf.urls import url

from Application import views

urlpatterns = [
    url(r'', views.index, name='index'),
    url(r'^about.html/$',views.about,name='about')
]
