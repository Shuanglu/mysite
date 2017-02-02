from django.shortcuts import render, get_list_or_404, get_object_or_404

# Create your views here.
from django.views import generic
from django.shortcuts import render
from django.http import HttpResponse, HttpResponseRedirect
from django.urls import reverse
from .models import Blog, BlogDetail
from django.db.models import Q
from django.views.decorators.cache import cache_page
@cache_page(60 * 15)
def indexview(request,):
    return render(request, "shawn/index.html")

@cache_page(60 * 15)
def AboutMe(request,):
    return render(request, "shawn/AboutMe.html")

def Blogs(request,):
    BlogList = Blog.objects.order_by('-id')
    print BlogList
    return render(request, "shawn/Blog.html", {'BlogList': BlogList})

def BlogDetails(request, BlogId):
    print 'BlogPage'
    BlogPage = BlogDetail.objects.filter(blog=BlogId)
    #BlogPage = get_list_or_404(BlogDetail, blog=BlogId)
    #BlogOverview = Blog.objects.filter(id=BlogId)
    BlogOverview = get_object_or_404(Blog, id=BlogId)
    if BlogPage:
        comments = BlogDetail.objects.filter(blog=BlogId).values('num', 'comment')
    else:
        comments = 'none' 
    return render(request, "shawn/BlogDetail.html", {'comments': comments,'BlogOverview': BlogOverview})

def Search(request,):
    SearchText = request.POST['SearchText']
    Result = Blog.objects.filter(Q(title__contains=SearchText)|Q(content__contains=SearchText))
    
    return render(request, "shawn/Results.html", {'Result': Result})

