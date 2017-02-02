from django.conf.urls import url
from . import views

app_name = 'shawn'
urlpatterns = [
    url(r'^$', views.indexview, name='index'),
    url(r'^AboutMe', views.AboutMe, name='AboutMe'),
    url(r'^Blog$', views.Blogs, name='Blog'),
    url(r'^Search', views.Search, name='Search'),
    url(r'^Blog/(?P<BlogId>[0-9]+)', views.BlogDetails, name='Detail'),
]
