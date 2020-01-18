from django.shortcuts import render
from . models import Post

def home(request):
    context = {
     'posts': Post.objects.all()[:4]
    }
    return render(request, 'blog/home.html',context)

def about(request):
    return render(request, 'blog/about.html',{ 'title': 'about'})
