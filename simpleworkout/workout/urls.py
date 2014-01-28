from django.conf.urls import patterns, url

from workout import views

urlpatterns = patterns('',
    url(r'^about/$', views.about, name='about'),
)