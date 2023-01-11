# blog/models.py

# Import django modules
from django.db import models
from django.utils import timezone
from django.contrib.auth.models import User

# Create your models here.

'''Create a custom manager to retrieve all posts 
that have a PUBLISHED status.
It will allow us to retrieve posts using the 
notation Post.published.all().'''

# MODEL: PublishedManager
class PublishedManager(models.Manager):    
	def get_queryset(self):
		return super().get_queryset()\
		.filter(status=Post.Status.PUBLISHED)


# MODEL: Post
class Post(models.Model):

	# Defining Blog Status
	class Status(models.TextChoices):        
		DRAFT = 'DF', 'Draft'        
		PUBLISHED = 'PB', 'Published'

	# Table fields 
	title = models.CharField(max_length=250)    
	slug = models.SlugField(max_length=250)
	# Adding a many-to-one relationship
	author = models.ForeignKey(User,                               
		on_delete=models.CASCADE,                               
		related_name='blog_posts') 
	body = models.TextField()
	# Adding datetime fields
	publish = models.DateTimeField(default=timezone.now)    
	created = models.DateTimeField(auto_now_add=True)
	updated = models.DateTimeField(auto_now=True)
	# Adding a status field
	status = models.CharField(
		max_length=2,                              
		choices=Status.choices,                              
		default=Status.DRAFT)

	# Use the PublishedManager
	objects = models.Manager() # The default manager.    
	published = PublishedManager() # Our custom manager.

	# Defining a default sort order
	class Meta:        
		ordering = ['-publish']

	# Adding a database index
	class Meta:        
		ordering = ['-publish']        
		indexes = [            
			models.Index(fields=['-publish']),        
		]

	# Adding string method 
	def __str__(self):
		return self.title