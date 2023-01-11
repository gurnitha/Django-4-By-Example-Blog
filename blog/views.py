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
def post_detail(request, year, month, day, post):
	post = get_object_or_404(Post,
							status=Post.Status.PUBLISHED,
							slug=post,
							publish__year=year,
							publish__month=month,
							publish__day=day)   
	return render(request,'blog/post/detail.html',{'post': post})