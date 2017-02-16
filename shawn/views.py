from django.shortcuts import render, get_list_or_404, get_object_or_404

# Create your views here.
from django.views import generic
from django.shortcuts import render, redirect
from django.http import HttpResponse, HttpResponseRedirect
import json
from django.urls import reverse
from .models import Blog, BlogDetail
from django.db.models import Q, Max
from django.views.decorators.cache import cache_page
from django.contrib.auth.models import User
from django.contrib.auth import authenticate, login, logout
from django.core import serializers
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
    BlogPage = BlogDetail.objects.filter(blog=BlogId)
    #BlogPage = get_list_or_404(BlogDetail, blog=BlogId)
    #BlogOverview = Blog.objects.filter(id=BlogId)
    BlogOverview = get_object_or_404(Blog, id=BlogId)
    if BlogPage:
        #comments = BlogDetail.objects.filter(blog=BlogId).values('comment')
        comments = BlogDetail.objects.filter(blog=BlogId)
        comments = serializers.serialize("json",BlogDetail.objects.all())
        #rangemax = BlogDetail.objects.filter(blog=BlogId).values_list('num', flat=True).aggregate(Max('num'))
        #rangemax = 10
        #return render(request, "shawn/BlogDetail.html", {'comments': comments, 'BlogOverview': BlogOverview, 'range': range(0, (rangemax['num__max']+1))})
        return render(request, "shawn/BlogDetail.html", {'comments': comments, 'BlogOverview': BlogOverview,
                                                         'range': range(0, (10 + 1))})
    else:
		return render(request, "shawn/BlogDetail.html", {'BlogOverview': BlogOverview})

def Search(request,):
    SearchText = request.GET.get('text')
    Result = Blog.objects.filter(Q(title__contains=SearchText)|Q(content__contains=SearchText))
    return render(request, "shawn/Results.html", {'Result': Result})

def Comments(request, BlogId):
    print "11111"
    if request.method == 'GET':
        id = request.GET['id']
        comments = list(BlogDetail.objects.filter(blog=id).values_list('comment', flat=True))
        #comments = serializers.serialize("json", BlogDetail.objects.all())
        print BlogDetail.objects.filter(blog=id).values_list('blog', flat=True)
        comments = json.dumps(comments)
        return HttpResponse(comments)

    if request.method == 'POST':
        comment = request.POST['text']
        #num = request.POST['num']
        print comment
        BlogDetailC = BlogDetail.objects.create(blog_id=BlogId, comment=comment)
        #BlogDetailC.save()
        comments = list(BlogDetail.objects.filter(blog=BlogId).values_list('comment', flat=True))
        comments = json.dumps(comments)
        return HttpResponse(comments)

def AuthL(request,):
    path = request.get['path']
    return render(request, "shawn/Auth.html", {'path': path})

def AuthSL(request,):
    user = request.POST["user"]
    passwd = request.POST["passwd"]
    path = request.POST['path']
    if request.POST["signup"]:
        cpasswd = request.POST["cpasswd"]
        if cpasswd == passwd:
            User.objects.create_user(username=user, password=passwd)
            Logininfo = authenticate(username=user, password = passwd)
            login(request, Logininfo)
            return redirect(path)
        else:
            return render(request, "shawn/AuthS.html", {"errormsg": "Password is different"})


    Login = authenticate(username=user, password=passwd)
    if Login is not None:
        login(request, Login)
        return redirect(path)






def Auth(request,):
    #req = json.loads(request.)
    print "1"
    status = request.GET.get('status')
    path = request.GET.get('path')
    print status, path
    if status == 'logout':
        logout(request)
        return redirect(path)
    elif status == "login":
        #return redirect("/shawn/AuthL", {'path': path})
        return render(request,"shawn/AuthL.html", {'path': path})
    elif status == "signup":
        return render(request,"shawn/AuthS.html", {'path': path})

