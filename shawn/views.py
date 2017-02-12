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
        comments = BlogDetail.objects.filter(blog=BlogId).values('num', 'comment')
        rangemax = BlogDetail.objects.filter(blog=BlogId).values_list('num', flat=True).aggregate(Max('num'))
        return render(request, "shawn/BlogDetail.html", {'comments': comments, 'BlogOverview': BlogOverview, 'range': range(0, (rangemax['num__max']+1))})
    else:
		return render(request, "shawn/BlogDetail.html", {'BlogOverview': BlogOverview})

def Search(request,):
    SearchText = request.GET.get('text')
    Result = Blog.objects.filter(Q(title__contains=SearchText)|Q(content__contains=SearchText))
    return render(request, "shawn/Results.html", {'Result': Result})

def Comments(request, BlogId):
    comment = request.POST['comment']
    num = request.POST['num']
    BlogDetailC = BlogDetail.objects.create(blog_id=BlogId, num=num, comment=comment)
    #BlogDetailC.save()
    return redirect("/shawn/Blog/"+BlogId)

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
    req = json.loads(request)
    print "1"
    status = req.POST.get('status')
    path = req.POST.get('path')
    print status, path
    if status == 'logout':
        logout(req)
        return redirect(path)
    elif status == "login":
        return render(req,"shawn/AuthL.html", {'path': path})
    elif status == "signup":
        return render(req,"shawn/AuthS.html", {'path': path})

