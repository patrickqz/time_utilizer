from django.conf.urls import url, patterns

from utilizer import views

urlpatterns = [
    url(r'^$', views.index, name='index'),
    url(r'^(/add/)$', views.addLink, name='addLink'),
    url(r'^/result/(?P<tag>+\s)/(?P<timeToRead>+\d)$', views.getResult, name='getResult')
]

