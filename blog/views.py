# blog/models.py

# Import django modules
from django.shortcuts import render

# Import from locals
from .models import Post

# Create your views here.


# VIEWS: post_list
def post_list(request):
	posts = Post.published.all()    
	return render(request,'blog/post/list.html',{'posts': posts})
