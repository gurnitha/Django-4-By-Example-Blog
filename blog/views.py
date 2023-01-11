# blog/models.py

# Import django modules
from django.shortcuts import render
from django.shortcuts import render, get_object_or_404

# Import from locals
from .models import Post

# Create your views here.


# VIEWS: post_list
def post_list(request):
	posts = Post.published.all()    
	return render(request,'blog/post/list.html',{'posts': posts})


# VIEWS: post_detail
def post_detail(request, id):    
	post = get_object_or_404(Post,id=id,status=Post.Status.PUBLISHED)    
	return render(request,'blog/post/detail.html',{'post': post})