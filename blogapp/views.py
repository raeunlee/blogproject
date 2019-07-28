from django.shortcuts import render, get_object_or_404, redirect
from django.utils import timezone
from .models import Blog

def home(request):
    blogs = Blog.objects
    return render(request, 'home.html', {'blogs':blogs})

def detail(requset, blog_id):
    details = get_object_or_404(Blog, pk=blog_id)
    return render(request, 'detail.html',{'details':details})

def new(request):
    return render(request, 'new.html')

def create(request):
    blog = Blog()
    blog.title = request.Get['title']
    blog.body = rquest.Get['body']
    blog.pub_date = timezone.datetime.now()
    blog.save()
    return redirect('/blog/'+str(blog.id))