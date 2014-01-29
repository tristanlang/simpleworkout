from django.conf.urls import patterns, url

from workout import views

urlpatterns = patterns('',
    url(r'^about/$', views.about, name='about'),
    url(r'^main/$', views.workout, name='main'),
    url(r'^history/$', views.history, name='history'),
    url(r'^new/$', views.new, name='new'),
    url(r'^login/$', views.login_view, name='login'),
    url(r'^logout/$', views.logout_view, name='logout'),
    url(r'^preferences/$', views.preferences, name='preferences'),
)