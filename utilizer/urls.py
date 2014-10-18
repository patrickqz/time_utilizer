from django.conf.urls import url, patterns


from utilizer import views

urlpatterns = [
    url(r'^$', views.index, name='index'),
    url(r'^(/add/)$', views.addLink, name='addLink'),
    url(r'login/$', views.login, name='login'),
    url(r'^result/$', views.getResult, name='getResult')
]
