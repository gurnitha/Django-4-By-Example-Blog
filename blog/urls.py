# blog/urls.py

# Import django modules
from django.urls import path


# Import from locals
from . import views


app_name = 'blog'

urlpatterns = [
	# post views    
	path('', views.post_list, name='post_list'),    
	path('<int:id>/', views.post_detail, name='post_detail'),
]