from django.conf.urls import patterns, url

from utilizer import views

urlpatterns = patterns('',
    url(r'^$', views.index, name='index'),
    url(r'getrandomarticle/$', views.getResult, name='randomarticle'),
    url(r'login/$', views.login, name='login'),
)