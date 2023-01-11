# blog/models.py

# Import django modules
from django.shortcuts import render, get_object_or_404
from django.core.paginator import Paginator, EmptyPage

# Import from locals
from .models import Post

# Create your views here.


# VIEWS: post_list
def post_list(request):    
	post_list = Post.published.all()
	# Pagination with 3 posts per page
	paginator = Paginator(post_list, 3)
	page_number = request.GET.get('page', 1)
	
	try:
		posts = paginator.page(page_number)    
	except EmptyPage:
		# If page_number is out of range deliver last page of results
		posts = paginator.page(paginator.num_pages)

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