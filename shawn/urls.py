from django.conf.urls import url
from . import views

app_name = 'shawn'
urlpatterns = [
    url(r'^$', views.indexview, name='index'),
    url(r'^AboutMe', views.AboutMe, name='AboutMe'),
    url(r'^Blog$', views.Blogs, name='Blog'),
    url(r'^Search/$', views.Search, name='Search'),
    url(r'^Blog/(?P<BlogId>[0-9]+)$', views.BlogDetails, name='Detail'),
    url(r'^Blog/(?P<BlogId>[0-9]+)/comment', views.Comments, name='Comments'),
    url(r'^Auth/$', views.Auth, name='Auth'),
    url(r'^AuthL', views.AuthSL, name='AuthL'),
    url(r'^AuthS', views.AuthSL, name='AuthS'),
    #url(r'^Logout$', views.Logout, name='Logout'),
    url(r'^AuthSL$', views.AuthSL, name='AuthSL'),
]
